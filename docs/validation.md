# What has been checked?

[Home](../README.md) · [Dated file checks](../checksums/README.md)

There are three separate checks:

- **The catalogue**: file identities, expected sizes/checksums, reference versions, reported amounts and all required mates/runs are consistent across the manifest, tables, workbook and downloader.
- **Downloaded files**: all 91 source files are complete. Whole-file MD5 and size checks passed for the 75 files with publisher checksums. The other 16 passed full gzip/BAM integrity checks and have locally calculated MD5 values. The dated verification table identifies the source of every MD5.
- **Preparation and compression**: gzip decompression and the real BAM export have not produced verified benchmark FASTQs here. No compression ratio or throughput result is claimed.

Eleven tiny synthetic software tests pass. They cover catalogue planning, local verification, rejection of bad checksums, the bounded proxy retry the fixed BAM export policy and actual Markdown/HTML/DOCX bold rendering. A local HTTPS/proxy test also confirmed recovery from one transient CONNECT503 error with certificate checking enabled. These tests do not authenticate real sequencing data.

Document checks inspect the actual XLSX/DOCX contents and links. Sample cell views use local fonts and configured widths; they are not native Excel or Word page rendering. The English and Chinese files must preserve the same scientific identities and quantities. Language review does not substitute for data checks or human approval of every sentence.

Suggested references still need content and sample/strain/target checks. Data 6 needs the specified real-source export; Data 8 has no publisher MD5 and unknown exact whole-file yield. Neither a version number nor a source listing removes these limits.
