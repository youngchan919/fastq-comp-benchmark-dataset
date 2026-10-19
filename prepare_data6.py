#!/usr/bin/env python3
"""Prepare Data 6 using a pinned SAMtools byte-output rule; never run implicitly."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

PINNED_VERSION = "1.22+htslib-1.22"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def prepare(source, output):
    version = subprocess.check_output(["samtools", "--version-only"], text=True).strip()
    if version != PINNED_VERSION:
        raise ValueError("This rule requires samtools " + PINNED_VERSION + "; found " + version)
    target = output / "Data_6.fastq"
    receipt = output / "preparation.json"
    if target.exists() or receipt.exists():
        raise FileExistsError("Prepared output exists; choose a fresh output directory")
    output.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["LC_ALL"] = "C"
    with tempfile.TemporaryDirectory(prefix="data6-", dir=output) as work:
        sorted_bam = Path(work) / "name_sorted.bam"
        sort_command = ["samtools", "sort", "-n", "-@", "0", "-m", "768M", "-o", str(sorted_bam), str(source)]
        subprocess.run(sort_command, check=True, env=environment)
        primary = subprocess.Popen(["samtools", "view", "-F", "0x900", str(sorted_bam)],
                                   stdout=subprocess.PIPE, text=True, env=environment)
        previous = None
        count = 0
        missing_qualities = 0
        problem = None
        for line in primary.stdout:
            fields = line.rstrip("\n").split("\t")
            name, flags = fields[0], int(fields[1])
            if flags & 0xC1:
                problem = "Unexpected paired/READ1/READ2 flags; this rule requires unpaired primary records"
            if name == previous:
                problem = "Duplicate primary QNAME; review the output rule instead of silently dropping records"
            if fields[9] == "*":
                problem = "Missing primary SEQ; this rule does not silently omit it"
            if fields[10] == "*":
                problem = "Missing primary QUAL; this rule does not synthesize qualities"
            previous = name
            count += 1
            missing_qualities += fields[10] == "*"
        primary.stdout.close()
        if primary.wait():
            raise RuntimeError("samtools view failed")
        if problem:
            raise ValueError(problem)
        command = ["samtools", "fastq", "-@", "0", "-n", "-F", "0x900", str(sorted_bam)]
        partial = Path(work) / "Data_6.fastq"
        with partial.open("wb") as handle:
            subprocess.run(command, stdout=handle, check=True, env=environment)
        with partial.open("rb") as handle:
            lines = sum(1 for _ in handle)
        if lines != count * 4:
            raise ValueError("FASTQ record count differs from the declared primary-record policy")
        result = {"source": str(source), "source_sha256": sha256(source), "source_bytes": source.stat().st_size,
                  "samtools_version": version, "commands": {"sort": sort_command, "fastq": command, "primary_check": ["samtools", "view", "-F", "0x900", str(sorted_bam)]}, "locale": "C", "rule": "name-sort; primary unpaired; -n -F0x900; stored QUAL, no OQ or copied tags",
                  "order": "SAMtools 1.22 natural QNAME order under LC_ALL=C; not claimed native instrument order",
                  "orientation": "SAMtools fastq restores forward orientation from reverse-strand BAM records",
                  "missing_quality_rule": "Reject missing primary QUAL; never synthesize qualities",
                  "primary_records": count, "missing_QUAL_records": missing_qualities,
                  "output": target.name, "output_bytes": partial.stat().st_size, "output_sha256": sha256(partial),
                  "lossless_target": "Exact resulting FASTQ bytes, not BAM tags/alignments or original instrument FASTQ"}
        os.link(partial, target)
        with receipt.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2)
            handle.write("\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bam", type=Path)
    parser.add_argument("--output", type=Path, default=Path("prepared/Data_6"))
    parser.add_argument("--dry-run", action="store_true", help="Describe the rule without opening the source BAM")
    args = parser.parse_args()
    if args.dry_run:
        print(json.dumps({"tool": PINNED_VERSION, "source": str(args.bam), "output": str(args.output / "Data_6.fastq"),
                          "policy": "name-sort, primary unpaired records, no tags/suffixes, forward orientation, stored QUAL, reject missing QUAL",
                          "execution": "Not executed; source not opened"}, indent=2))
        return 0
    print(json.dumps(prepare(args.bam, args.output), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
