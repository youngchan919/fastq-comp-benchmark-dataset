# Download checksums and verification

[Home](../README.md) · [简体中文](../zh-CN/checksums/README.md) · [All file links](../catalogue/files.tsv)

The catalogue lists 91 files. Publishers provide MD5 values for 75; 16 have no recorded publisher checksum. [MD5SUMS](MD5SUMS) contains the expected values and current catalogue paths. These are publisher expectations, not newly calculated SHA-256 values.

## Check downloaded files

Use a fresh, version-specific download directory, such as `downloads/v1.1.0`. Existing download jobs and folders have not been changed. From the directory that contains its `data/` folder:

```bash
cd YOUR_DOWNLOAD_FOLDER
md5sum -c /path/to/fastq-comp-benchmark-dataset/checksums/MD5SUMS
```

A match means the whole downloaded file matches the publisher value. Missing files are reported as missing, not proved corrupt. Neither a `.part` suffix, a final filename nor size agreement alone proves completeness. Files without publisher checksums need the further checks in the [preparation guide](../docs/preparation.md).

## Dated verification records

The retained-file checks in [verification.tsv](verification.tsv) are the **2026-10-20T03:39:26.216321+00:00** snapshot. They follow identical source files, not dataset numbers or folder names. Paths shown are this version's catalogue paths; they do not claim the existing local folders were moved or that those paths were checked on disk. No new live filesystem scan was made for this catalogue update.

- **Incomplete: 10 files.**
- **Publisher MD5 matched: 13 files.**
- **Size matched only: 2 files.**
- **Not locally verified: 4 files.**
- **Not downloaded: 58 files.**
- **Awaiting verification: 4 files.**

Four newly selected wheat/CHO files were not in that snapshot. They have no recorded local verification or snapshot timestamp. Their publisher MD5 values are still available as expectations. The other rows retain the actual old check/snapshot dates and may no longer describe current download progress.

A publisher-MD5 match supports publisher-identical source bytes; size-only matches are weaker. These checks concern downloaded gzip/BAM bytes. Benchmark targets are uncompressed FASTQ bytes, with their own byte counts and SHA-256 after preparation. No calculated source or prepared-FASTQ SHA-256 baseline is published. Download progress and verification do not determine the dataset version.
