# Validation scope

[English home](../README.md) · [简体中文](../zh-CN/)

The local inventory contains 52 datasets, 115 source objects (114 gzip FASTQ files and one BAM), 1,419,456,345,104 listed source bytes and 18 versioned reference proposals. There are 73 publisher-MD5 expectations and 42 size-only expectations. Known selected-source sequence totals exclude Data6 and Data8.

All 35 local package checks passed: manifest/catalogue/download-plan parity, exact file names and routes, quantities, current dataset/reference mappings, actual XLSX and DOCX content, internal links, complete multi-run file lists and public navigation. All nine synthetic functional tests passed. They exercise planning, local verification/resume behavior and the pinned BAM export rule, including missing-quality rejection. No real source BAM was processed by these tests.

Sample worksheet cells were rendered from the actual XLSX values with local fonts and configured widths; no sampled text overflow was found. These checks are not native Excel rendering or Word pagination proof.

The package does not certify source availability, whole-file integrity, source/reference compatibility, complete-library distributions or compression performance. Saved prefix observations are identified individually and are nonrandom. References remain metadata-level proposals. Data6 still requires applicable real-source preparation; Data8 has unknown exact whole-file yield and no publisher checksum. Author attribution and package license choice remain pending.
