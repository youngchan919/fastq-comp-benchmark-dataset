#!/usr/bin/env python3
"""Download the pinned public benchmark using Python 3.8+ and GNU wget."""

import argparse
import concurrent.futures
import csv
import fcntl
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading
import time


MANIFEST = json.loads((Path(__file__).resolve().parent / 'catalogue' / 'manifest.json').read_text(encoding='utf-8'))


def select_jobs(ids, kind):
    datasets = MANIFEST["selected"]
    if ids:
        wanted = {int(value.strip()) for value in ids.split(",")}
        missing = wanted - {item["no"] for item in datasets}
        if missing:
            raise ValueError("Unknown Data IDs: " + ", ".join(map(str, sorted(missing))))
        datasets = [item for item in datasets if item["no"] in wanted]
    jobs = []
    if kind in ("data", "all"):
        for dataset in datasets:
            for source in dataset["files"]:
                jobs.append(dict(filename=source["physical_name"], url=source["url"],
                                 size=source["listed_bytes"], md5=source.get("publisher_md5", ""),
                                 label="Data " + str(dataset["no"]), kind="data",
                                 path="data/Data_{}/{}".format(dataset["no"], source["physical_name"])))
    if kind in ("references", "all"):
        ref_ids = {reference["fa_no"] for dataset in datasets for reference in dataset["reference_proposals"]}
        for reference in MANIFEST["references"]:
            if reference["no"] in ref_ids:
                jobs.append(dict(filename=reference["download_filename"], url=reference["download_url"],
                                 size=reference.get("listed_bytes"), md5=reference.get("publisher_md5", ""),
                                 label="fa " + str(reference["no"]), kind="reference",
                                 path="references/fa_{}/{}".format(reference["no"], reference["download_filename"])))
    return jobs


def write_manifest(handle, jobs):
    writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
    writer.writerow(["label", "kind", "path", "url", "expected_bytes", "publisher_md5"])
    for job in jobs:
        writer.writerow([job["label"], job["kind"], job["path"], job["url"],
                         job.get("size") if job.get("size") is not None else "",
                         job.get("md5", "")])


class Downloader:
    def __init__(self, output, retries, verify_only=False):
        self.output = Path(output)
        self.retries = retries
        self.verify_only = verify_only
        self.stopped = threading.Event()
        self.lock = threading.Lock()
        self.processes = set()

    def verify(self, job, path):
        size = path.stat().st_size
        expected = job.get("size")
        if expected is not None and size != expected:
            raise ValueError("Size mismatch: {} bytes; expected {}".format(size, expected))
        if size == 0:
            raise ValueError("Empty file")
        if job.get("md5"):
            checksum = hashlib.md5()
            with path.open("rb") as handle:
                while True:
                    if self.stopped.is_set():
                        raise InterruptedError("Interrupted during checksum verification")
                    block = handle.read(8 * 1024 * 1024)
                    if not block:
                        break
                    checksum.update(block)
            if checksum.hexdigest() != job["md5"]:
                raise ValueError("MD5 mismatch: got " + checksum.hexdigest())
            verification = "publisher-md5+size" if expected is not None else "publisher-md5"
        else:
            verification = "size-only" if expected is not None else "FASTA-header-only"
        if job["kind"] == "reference":
            opener = gzip.open if job["filename"].endswith(".gz") else open
            with opener(path, "rb") as handle:
                if handle.read(1) != b">":
                    raise ValueError("Reference is not a FASTA file; response may be an error page")
        return verification

    def stop(self):
        self.stopped.set()
        with self.lock:
            for process in list(self.processes):
                if process.poll() is None:
                    process.terminate()

    def one(self, job):
        target = self.output / job["path"]
        partial = target.with_name(target.name + ".part")
        result = {"status": "failed", "verification": "", "message": ""}
        try:
            if self.stopped.is_set():
                raise InterruptedError("Interrupted before starting")
            if target.exists():
                result["verification"] = self.verify(job, target)
                result["status"] = "existing"
                return result
            if self.verify_only:
                raise ValueError("Missing completed file")
            target.parent.mkdir(parents=True, exist_ok=True)
            ready = (partial.exists() and job.get("size") is not None
                     and partial.stat().st_size == job["size"])
            if partial.exists() and job.get("size") is not None:
                if partial.stat().st_size > job["size"]:
                    raise ValueError("Partial file exceeds expected size; move it aside before retrying")
            verification = ""
            if ready:
                verification = self.verify(job, partial)
            if not ready:
                log = self.output / "logs" / (job["path"] + ".wget.log")
                log.parent.mkdir(parents=True, exist_ok=True)
                command = ["wget", "--no-config", "--continue", "--no-verbose",
                           "--connect-timeout=30", "--read-timeout=120",
                           "--tries={}".format(self.retries + 1), "--waitretry=60",
                           "--retry-connrefused", "--retry-on-http-error=408,429,500,502,503,504",
                           "--no-use-server-timestamps", "--output-document", str(partial),
                           "--", job["url"]]
                environment = os.environ.copy()
                environment["LC_ALL"] = "C"
                for attempt in range(self.retries + 1):
                    with log.open("ab") as errors:
                        offset = errors.tell()
                        with self.lock:
                            if self.stopped.is_set():
                                raise InterruptedError("Interrupted before transfer")
                            process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=errors, env=environment)
                            self.processes.add(process)
                        try:
                            code = process.wait()
                        finally:
                            with self.lock:
                                self.processes.discard(process)
                    if self.stopped.is_set():
                        raise InterruptedError("Interrupted; partial file retained")
                    with log.open("rb") as errors:
                        errors.seek(offset)
                        transient_proxy_failure = (code == 4 and
                            b"Proxy tunneling failed: Service Unavailable" in errors.read())
                    if not transient_proxy_failure or attempt == self.retries:
                        break
                    if self.stopped.wait(min(60, 5 * (attempt + 1))):
                        raise InterruptedError("Interrupted during proxy retry; partial file retained")
                if code:
                    raise ValueError("wget exited {}. See {}. Partial file retained".format(code, log))
            result["verification"] = verification or self.verify(job, partial)
            if self.stopped.is_set():
                raise InterruptedError("Interrupted; partial file retained")
            # Publish the verified file without overwriting any existing destination.
            os.link(str(partial), str(target))
            partial.unlink()
            result["status"] = "downloaded"
            return result
        except InterruptedError as error:
            result["status"] = "interrupted"
            result["message"] = str(error)
        except (OSError, ValueError, EOFError) as error:
            result["message"] = str(error) + "; existing or partial data were not deleted."
        return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("downloads"),
                        help="Destination directory (default: downloads/)")
    parser.add_argument("--ids", help="Comma-separated Data IDs, e.g. 10,30; default: all datasets")
    parser.add_argument("--kind", choices=["data", "references", "all"], default="data",
                        help="Source reads/BAM, mapped FASTA references, or both (default: data)")
    parser.add_argument("--jobs", type=int, default=8, help="Parallel file transfers (default: 8)")
    parser.add_argument("--retries", type=int, default=4, help="Resume retries per file for transient errors (default: 4)")
    parser.add_argument("--dry-run", action="store_true", help="Print TSV plan; no network or file writes")
    parser.add_argument("--verify-only", action="store_true", help="Check local files; no network")
    args = parser.parse_args(argv)
    if args.jobs < 1 or args.retries < 0:
        parser.error("--jobs must be positive and --retries must be nonnegative")
    try:
        jobs = select_jobs(args.ids, args.kind)
    except ValueError as error:
        parser.error(str(error))
    known_bytes = sum(job.get("size") or 0 for job in jobs)
    unknown_sizes = sum(job.get("size") is None for job in jobs)
    md5_count = sum(bool(job.get("md5")) for job in jobs)
    print("{} files; {:,} known source bytes ({:.3f} decimal TB); {} unknown sizes; "
          "{} publisher MD5 checksums.".format(
              len(jobs), known_bytes, known_bytes / 10**12, unknown_sizes, md5_count), file=sys.stderr)
    if args.dry_run:
        write_manifest(sys.stdout, jobs)
        return 0
    if not args.verify_only and shutil.which("wget") is None:
        parser.error("GNU wget is required; make it available on PATH")
    args.output = args.output.expanduser().resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    downloader = Downloader(args.output, args.retries, args.verify_only)
    results = {job["path"]: {"status": "not-run", "verification": "", "message": ""} for job in jobs}
    interrupted = False
    with (args.output / ".download.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error("Another downloader is using this output directory")
        with (args.output / "download_manifest.tsv").open("w", newline="", encoding="utf-8") as handle:
            write_manifest(handle, jobs)
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs)
        futures = {pool.submit(downloader.one, job): job for job in jobs}
        pending = set(futures)
        previous_stored = None
        previous_report = time.monotonic()
        try:
            while pending:
                done, pending = concurrent.futures.wait(
                    pending, timeout=15, return_when=concurrent.futures.FIRST_COMPLETED)
                for future in done:
                    job = futures[future]
                    results[job["path"]] = future.result()
                    result = results[job["path"]]
                    print("{} {} [{}] {}".format(result["status"].upper(), job["path"],
                                                result["verification"], result["message"]), flush=True)
                if not done:
                    stored = 0
                    for job in jobs:
                        target = args.output / job["path"]
                        partial = target.with_name(target.name + ".part")
                        for candidate in (target, partial):
                            try:
                                stored += candidate.stat().st_size
                                break
                            except FileNotFoundError:
                                pass
                    now = time.monotonic()
                    speed = "measuring"
                    if previous_stored is not None and stored >= previous_stored:
                        speed = "{:.2f} MB/s".format((stored - previous_stored) / (now - previous_report) / 10**6)
                    with downloader.lock:
                        active = len(downloader.processes)
                    print("Progress: {}/{} attempts finished; {} active wget transfers; "
                          "{:.3f} GB at active paths (includes existing files); "
                          "recent file growth: {}.".format(
                              len(jobs) - len(pending), len(jobs), active, stored / 10**9, speed), flush=True)
                    previous_stored = stored
                    previous_report = now
        except KeyboardInterrupt:
            interrupted = True
            downloader.stop()
            for future in futures:
                future.cancel()
            print("Interrupted: stopping transfers and keeping partial files.", file=sys.stderr)
        finally:
            pool.shutdown(wait=True)
        for future, job in futures.items():
            if future.done() and not future.cancelled():
                results[job["path"]] = future.result()
            elif interrupted:
                results[job["path"]] = {"status": "interrupted", "verification": "", "message": "Not started"}
        report = args.output / "download_status.tsv"
        with report.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
            writer.writerow(["label", "path", "status", "verification", "message", "url"])
            for job in jobs:
                result = results[job["path"]]
                writer.writerow([job["label"], job["path"], result["status"], result["verification"],
                                 result["message"], job["url"]])
    good = sum(result["status"] in ("downloaded", "existing") for result in results.values())
    print("Finished: {}/{} files successful. Status: {}".format(good, len(jobs), report))
    return 130 if interrupted else (0 if good == len(jobs) else 1)


if __name__ == "__main__":
    sys.exit(main())
