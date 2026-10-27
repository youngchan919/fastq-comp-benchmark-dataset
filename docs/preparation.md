# Input preparation and verification

[English home](../README.md) · [简体中文](../zh-CN/)

Use the exact file list in the [manifest](../catalogue/manifest.json) and [Files table](../catalogue/files.tsv). This document specifies future preparation. No real source BAM has been exported and no compression benchmark has been run for this package.

## Preserve the declared input unit

A paired run requires both listed ends. The selected Thatcher wheat input, each CITE component and the CHO input each contain one complete paired run with two FASTQ files. Keep the distinct CITE component identities and both ends of every run. Do not silently drop files, concatenate unrelated inputs or expand a run to every library from its biological sample.

Data8 contains one SINGLE CNGB object, `WY_reads.fq.gz`. It is not a pair or two chunks. CNGB metadata links its project/sample/experiment/run identifiers and release on 4 December 2025. Its 130,270,589,600-byte expectation has no publisher MD5. Its exact whole-file read/base yield and byte equivalence to associated SRA representations remain unverified.

## Verify acquired sources before testing

The shared downloader lists the files and reports their verification status. For 75 files it has a publisher MD5 and listed size; 16 have no recorded publisher checksum. Neither a catalogue entry nor a successful request implies completed verification. Where no publisher checksum exists, record a local SHA-256 for subsequent reproducibility, recognizing that a local hash alone does not independently authenticate the publisher's content.

The [MD5SUMS file](../checksums/MD5SUMS) now covers all 91 downloaded sources. For the 16 without publisher MD5s, it records locally calculated values from copies that passed full gzip/BAM integrity checks. Follow the [checksum instructions](../checksums/README.md) to compare your downloads before preparing FASTQ inputs.

The reference table lists exact NCBI versions checked on 27 October 2026, with direct download links and publisher MD5 values for the 17 assembly FASTA files. The fixed NC_045512.2 nucleotide reference has no recorded publisher MD5. No FASTA was downloaded in this update. After downloading, check the publisher MD5 where available, run a full gzip integrity check for compressed files, and record the FASTA hash used in the benchmark. Confirm the relationship to the chosen sample: some references use different cultivars or strains. Mixed communities and feature libraries have no single genome assigned. Spatial masks/coordinates and CITE feature definitions support interpretation or custom matching.

## Gzip sources: uncompressed FASTQ is the benchmark target

**Benchmark inputs are uncompressed FASTQ bytes**. Downloaded gzip files are download containers, not inputs to the compressors being compared. Decompress each listed source separately, preserving every header, sequence, quality character, record, order and formatting byte. Do not concatenate mates, runs or chunks; do not trim, normalize, reformat or recompress the prepared FASTQ.

After downloaded-file verification, run the following Bash commands for each exact listed file. This example prepares one maize mate; repeat separately for its other mate and every other selected gzip source, using the corresponding paths. Use fresh output names. Successful `gzip -t` and `gzip -dc` require a complete gzip stream with valid CRC/length checks; an error or truncation stops the workflow. A failed `.part` output is not a benchmark input.

```bash
set -euo pipefail
set -o noclobber
source_gz='downloads/data/Data_10/SRR8906645_1.fastq.gz'
output_fastq='prepared/Data_10/SRR8906645_1.fastq'
mkdir -p -- prepared/Data_10
test ! -e "$output_fastq"
test ! -e "$output_fastq.part"
gzip --version
gzip -t -- "$source_gz"
gzip -dc -- "$source_gz" > "$output_fastq.part"
mv -- "$output_fastq.part" "$output_fastq"
wc -c -- "$output_fastq"
sha256sum -- "$source_gz" "$output_fastq"
```

Record the gzip version, exact commands, source identity and source checksum, output byte count and output SHA-256 in the preparation log. The source gzip checksum and prepared FASTQ hash identify different byte streams; neither substitutes for the other. Compression ratios and throughput must use the prepared uncompressed FASTQ byte count as their input denominator. No real source decompression was performed during packaging.

## Data6: pinned BAM-to-FASTQ rule

Data6 is the named ONT PAW70337 SUP flow-cell BAM. Its separate mapped-analysis quantities are not established as exact source/export yield. The lossless target is the resulting FASTQ, not preservation of BAM tags or alignments.

The included [prepare_data6.py](../prepare_data6.py) requires **SAMtools 1.22 with htslib 1.22**, reported by `samtools --version-only` as `1.22+htslib-1.22`.

1. Name-sort the fixed source BAM using `samtools sort -n -@ 0 -m 768M`, under `LC_ALL=C`.
2. Keep primary records, excluding secondary/supplementary flags `0x900`. Mapped and unmapped primary records are eligible. This rule expects unpaired records with stored sequence and quality.
3. Stop if primary records have paired/READ1/READ2 flags, duplicate QNAMEs, missing SEQ or missing QUAL. These conditions require an explicit preparation decision; the script does not silently discard them or synthesize qualities.
4. Run `samtools fastq -@ 0 -n -F 0x900` on the name-sorted BAM. Retain QNAME without added mate suffixes or copied tags. Use stored QUAL, without the OQ preference option. SAMtools converts reverse-strand alignments back to forward FASTQ orientation.
5. Write one plain `Data_6.fastq` and `preparation.json`. The log records the exact tool, source/output SHA-256, sizes, selected-record count and ordering/quality policy. Check the generated record count against the declared primary-record policy.

This is a fixed preparation choice, not native instrument order. Stored soft-clipped sequence can be exported; hard-clipped sequence absent from the BAM cannot be recovered. The real BAM's applicability and exact output yield remain **unexecuted/unverified**. Consult the pinned [fastq documentation](https://www.htslib.org/doc/1.22/samtools-fasta.html) and [sort documentation](https://www.htslib.org/doc/1.22/samtools-sort.html).

```bash
# No source read or output creation: inspect the declared policy.
python3 prepare_data6.py downloads/data/Data_6/calls.sorted.bam --dry-run

# Future preparation, only after source acquisition/verification and policy acceptance.
python3 prepare_data6.py downloads/data/Data_6/calls.sorted.bam --output prepared/Data_6
```

Tiny synthetic tests check primary filtering, natural name order, reverse orientation, stored quality rather than OQ, deterministic output and the explicit stop conditions. Passing them validates this software rule on fixtures; it does not validate or process Data6.

## Record the actual benchmark inputs

Keep each source identity/hash, complete file unit, preparation command/version, prepared uncompressed FASTQ hash/byte count and reference versions. Account for reference storage/preparation consistently across compressors. Evaluate exact decompression recovery against those fixed input bytes. This catalogue supplies no measured compression ratio, throughput or optimum/minimum collection claim.
