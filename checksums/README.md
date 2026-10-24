# Check downloaded files

[Home](../README.md) · [简体中文](../zh-CN/checksums/README.md) · [All file links](../catalogue/files.tsv)

[MD5SUMS](MD5SUMS) contains a whole-file MD5 for every source file in dataset **v1.1.0**: **91 files from 52 datasets**. All files have been downloaded and checked. The verification table was updated on **24 October 2026**.

| MD5 source | Files | Checks completed |
|---|---:|---|
| Publisher | 75 | File size and whole-file MD5 match the publisher's values. |
| Calculated locally | 16 | Expected file size and full gzip/BAM integrity checks passed; we then calculated each file's MD5. |

The 16 local values identify our checked copies; they are not publisher-confirmed checksums. [verification.tsv](verification.tsv) records each file's MD5, its source, file size and check dates.

## Verify your downloads

Run this from your download directory, which must contain the `data/` folder:

```bash
cd YOUR_DOWNLOAD_FOLDER
md5sum -c /path/to/fastq-comp-benchmark-dataset/checksums/MD5SUMS
```

A complete matching download reports `OK` for all 91 files. Each end of a paired run is checked separately. A missing file is reported as missing; a checksum mismatch is reported as `FAILED`.

## What the checks cover

These MD5 values cover the downloaded files: **90 gzip FASTQ files and one BAM file**. They do not cover the uncompressed FASTQ files used in compression tests. Follow the [preparation guide](../docs/preparation.md) to prepare those inputs and record their byte counts and SHA-256 values.

Publisher MD5 checks were completed on the dates shown in the table. The 16 files without publisher MD5s passed full integrity checks on 22 October 2026; their local MD5 values were calculated on 24 October. No uncompressed FASTQ output is included in this checksum list.
