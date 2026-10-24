# FASTQ compression benchmark dataset

**English** · [简体中文](zh-CN/)

**Dataset version: v1.1.0** · [Version policy](VERSIONING.md)

This dataset is for testing lossless FASTQ compression and decompression. It contains **52 public datasets** covering common sequencing technologies and uses. Each entry explains why it was chosen, lists the files to download, and describes how to use it. This repository contains the catalogue and instructions; sequencing files are downloaded separately.

The benchmark input is **uncompressed FASTQ**. Downloaded gzip files must be decompressed first. Lossless recovery means restoring the same names, sequences, quality characters, order and formatting—not just the same biological sequences.

## What is included?

| Item | Count |
|---|---:|
| Datasets in one collection | 52 |
| Files to download | 91: 90 gzip FASTQ files and one BAM |
| Total listed download size | 1,404,952,612,896 bytes (1.405 decimal TB) |
| Files with a publisher MD5 | 75 |
| Suggested reference versions | 18 |

The data cover human and other genomes, bulk and single-cell RNA, tags and spatial reads, chromatin libraries, targeted markers, isolates and mixed communities. The list includes short and long reads from several technologies. Each selected archive input is one complete run, with all its listed ends. The BAM and single CNGB FASTQ retain their declared public-source units. Keep every listed file.

## Find a dataset

- [Catalogue](catalogue/README.md) · [Excel workbook](catalogue/benchmark_dataset.xlsx) · [CSV](catalogue/catalogue.csv).
- [Why these datasets?](docs/report.md) · [Word report](docs/report.docx) · [HTML report](docs/report.html).
- [Every file and download link](catalogue/files.tsv) · [Suggested references](catalogue/references.tsv).
- [Checksums and dated verification results](checksums/README.md).
- [Preparation instructions](docs/preparation.md) · [Citation](CITATION.md) · [Rights/license status](RIGHTS.md).

The workbook keeps the familiar `fq`, `Files` and `fa` sheets. `Reasons` gives a short explanation for each dataset; `Details` contains the full amount evidence and processing notes. The machine-readable list is [manifest.json](catalogue/manifest.json). The catalogue, workbook and downloader use the same file list.

## Download

Python 3.8+ and GNU wget are required. Choose a fresh, version-specific download folder, such as `downloads/v1.1.0`. Existing jobs and download folders have not been moved or changed.

```bash
# List the files without downloading anything.
python3 download_benchmark.py --dry-run

# Download all selected files, keeping existing valid files and usable partials.
python3 download_benchmark.py --output downloads/v1.1.0 --jobs 8

# Or download only these dataset IDs, including all their listed files.
python3 download_benchmark.py --ids 10,29 --output downloads/v1.1.0
```

The downloader checks the listed size and publisher MD5 where available. It keeps incomplete files as `.part` and does not overwrite an existing completed file. A checksum failure is reported; it is not silently accepted. Size-only agreement is weaker than a checksum match. If a previous partial has wrong bytes, resuming it cannot repair those bytes.

All 91 source files have been downloaded and checked. The [MD5SUMS file](checksums/MD5SUMS) covers every file: 75 values match the publisher's MD5, and 16 were calculated locally after integrity checks. The [verification table](checksums/verification.tsv) records the MD5 source and check dates. See the [checksum instructions](checksums/README.md) to verify your downloads.

Data 8 is one CNGB `WY_reads.fq.gz` file, not mates or two chunks. Its listed size is 130,270,589,600 bytes and no publisher MD5 is available. Data 6 is a BAM file that needs the fixed FASTQ export described below. Neither has an established exact selected-source base total.

## Prepare and test

Follow the [complete preparation guide](docs/preparation.md). For each gzip source, check the full stream, decompress it separately and record the FASTQ byte count and SHA-256. Keep mate/run boundaries and preserve the bytes. For Data 6, use the documented SAMtools 1.22/htslib 1.22 export policy; it has synthetic tests but has not been run on the real BAM.

References are suggested versions, not verified downloads or guaranteed sample matches. Spatial masks and tag definitions may help interpretation or a custom reference; they are not required for generic lossless FASTQ compression.

The archive survey covers releases through 30 September 2026 and the preceding twelve months, using the original source/retrieval dates. Global figures include China. Archive hosting is not the location or volume of commercial production. See the report for the actual findings and limits.

## Rebuild and check the repository

```bash
# Tiny synthetic tests; no real sequence data are read.
python3 -m unittest discover -s tests -v

# Rebuild English documents and tables; requires XlsxWriter and markdown-it-py.
python3 tools/build.py
```

The fixed BAM export tests require SAMtools 1.22/htslib 1.22. Source integrity checks, document checks and compression benchmarks answer different questions. This repository does not report measured compression ratios or throughput. See [validation scope](docs/validation.md). Native Office pagination has not been checked.
