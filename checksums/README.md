# Download checksums and verification

[Home](../README.md) · [Files and download links](../catalogue/files.tsv)

The collection lists 115 files. Publishers supply MD5 values for 73 of them; the other 42 have no recorded publisher checksum. [MD5SUMS](MD5SUMS) contains those 73 expected values and the exact relative filenames. These are publisher values, not newly calculated SHA-256 values.

## Check downloaded files

Run this from the folder containing your downloaded `data/` directory, using the path to this repository:

```bash
cd YOUR_DOWNLOAD_FOLDER
md5sum -c /path/to/fastq-comp-benchmark-dataset/checksums/MD5SUMS
```

A matching result checks the full downloaded file against the publisher's MD5. Missing files are reported as missing; they are not proof of corrupt downloaded content. Do not treat a `.part` suffix, final filename or matching size as proof of completeness. For files without a publisher checksum, the [preparation guide](../docs/preparation.md) describes the remaining integrity checks.

## Dated local checks

The [verification table](verification.tsv) is a snapshot from **2026-10-20T03:39:26.216321+00:00**. Downloads and checks were still in progress. It reports every file, not just successful ones:

- **Awaiting verification: 5 files.**
- **Incomplete: 12 files.**
- **Not downloaded: 83 files.**
- **Publisher MD5 matched: 13 files.**
- **Size matched only: 2 files.**

“Publisher MD5 matched” means that the complete file and expected size were checked and its file identity still matched this snapshot. “Size matched only” is weaker: the contents are not certified. Incomplete, missing or awaiting-verification files have no completed check claimed. These statuses can change as downloading continues; they do not change the dataset version.

The checks concern downloaded gzip/BAM bytes. The actual compression input is uncompressed FASTQ. Its byte count and SHA-256 must be recorded after the specified decompression or BAM export. No calculated SHA-256 baseline is published here yet, and no prepared FASTQ checksum is invented.
