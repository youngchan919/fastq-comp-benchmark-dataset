# FASTQ compression benchmark dataset

**English** · [简体中文](zh-CN/)

A public dataset catalogue for anyone comparing **lossless FASTQ compression and decompression**. The collection combines public archive distributions with documented sequencing uses, then chooses explicit input units and representative sequence amounts. It is not tied to a compressor, manufacturer or team.

The folder contains metadata, evidence, reports and scripts—not sequencing or reference data. Benchmark targets are **uncompressed FASTQ bytes**; downloaded gzip files are source containers. Lossless recovery means restoring the exact prepared FASTQ bytes, including names, sequences, qualities, order and formatting.

| Current collection | Quantity |
|---|---:|
| Datasets in one collection | 52 |
| Listed source objects | 115: 114 gzip FASTQ files and 1 BAM |
| Listed compressed/source bytes | 1,419,456,345,104 (1.419 decimal TB) |
| Objects with publisher MD5 | 73 |
| Objects with size-only expectations | 42 |
| Versioned reference proposals | 18 |

Data IDs are stable identifiers; use the catalogue's actual rows. A dataset can be one paired run, an individual cell or a complete named multi-run library. Keep every listed mate, tag component and chunk. No source acquisition, full-file integrity verification or benchmark result is implied by this catalogue.

## Read the evidence and catalogue

- [Full report](docs/report.md) · [Word](docs/report.docx) · [HTML](docs/report.html): survey → principles → current collection, with a reason and appropriate amount for every input.
- [Readable catalogue](catalogue/README.md) · [Excel workbook](catalogue/benchmark_dataset.xlsx) · [CSV](catalogue/catalogue.csv).
- [Every source file](catalogue/files.tsv) and [every proposed reference](catalogue/references.tsv).
- [Preparation and verification](docs/preparation.md), including the explicit, unexecuted Data6 BAM-to-FASTQ rule.
- [Source register](evidence/evidence_register.json) and [survey discovery register](evidence/survey_discovery_register.csv).
- [Citation](CITATION.md), [rights/license status](RIGHTS.md) and [validation scope](docs/validation.md).

[Catalogue manifest](catalogue/manifest.json) is the **single authoritative inventory**. The workbook, readable tables, report and downloader derive their source identities, files and quantities from it. Source gzip/BAM sizes, reported sequence bases and unmeasured uncompressed FASTQ byte counts are separate quantities. Known selected-source sequence totals exclude Data6 and Data8, whose exact yields remain unknown.

The global archive snapshot covers stock through **30 September 2026** and the preceding twelve-month release increment. Its original retrieval dates remain stated in the report. Global includes China; archive hosting is not the location or volume of production. Compilation date: **19 October 2026**.

## Plan and download later

Python 3.8+ and GNU wget are needed on Linux/Unix. These commands are for a future acquisition; the package itself contains no source data.

```bash
# Print all 115 source jobs without network access or output-directory creation.
python3 download_benchmark.py --dry-run

# List one input, or acquire it into a separate destination when ready.
python3 download_benchmark.py --ids 10,30 --dry-run
python3 download_benchmark.py --ids 10,30 --output downloads

# References are proposed, versioned routes; inspect their status first.
python3 download_benchmark.py --kind references --dry-run

# Verify already acquired source files without a network transfer.
python3 download_benchmark.py --output downloads --verify-only
```

The downloader reads the manifest, resumes `.part` files, writes a status TSV and never overwrites an existing completed file. A publisher MD5 plus listed size is checked where available. **Size-only agreement is weaker and does not prove content integrity.** A reference without a published size/checksum receives only a FASTA-header check, not identity or full-integrity verification. Reference routes and exact read/reference compatibility remain proposals until verified. Keep local hashes and preparation receipts for actual tests.

Data8 is **CNR1409093 / CNX1236558**, one SINGLE `WY_reads.fq.gz` file, 130,270,589,600 listed bytes and no publisher MD5. CNGB metadata identifies human HG002 genomic WGS on G400-ER. A saved nonrandom prefix has 258 complete records, lengths 355–28,912 bases and no observed four-line format errors. This does not establish whole-file properties, yield, pairing or byte equivalence to associated SRA originals.

## Local checks and regeneration

```bash
# Tiny synthetic fixtures only; the export tests require the pinned SAMtools version.
python3 -m unittest discover -s tests -v

# Regenerate the English report and workbook from the manifest.
# Regeneration additionally requires the Python xlsxwriter package.
python3 tools/build.py
```

The tests exercise catalogue/download parity, synthetic verification and the pinned export rule. They do not access real sequencing data or measure compression performance. Package and cell checks are not native Office pagination proof.

Chinese documentation and catalogue use the same factual manifest and shared scripts. The English source is the reference for scientific identities and quantities; language review does not verify source data.
