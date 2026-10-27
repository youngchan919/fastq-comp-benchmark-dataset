# Dataset versions

[Home](README.md)

The current collection is **v1.2.0**. `VERSION` and `dataset_version` identify the pinned catalogue; `schema_version` describes its machine-readable format separately. Dataset numbers identify entries within a version. Cite the version, public source identities and prepared FASTQ hashes when comparing results.

- **Minor data version, such as v1.2.0:** changed selected files, complete input units, reference choices or catalogue numbering, while keeping the same benchmark meaning and preparation policy.
- **Major data version, such as v2.0.0:** incompatible changes to the benchmark definition, prepared-byte policy or catalogue interpretation.
- **Patch, such as v1.1.1:** corrected documentation, compatible tools or added verification results with unchanged selected input bytes and scientific definitions.
- **Annual review:** reconsider evidence and availability once a year; a review does not require changing inputs.

Published tags are immutable, including v1.0.0. A correction uses a new tag, never a moved tag. Use a fresh version-specific download directory so different catalogues do not mix files under the same numbered paths. A version number does not establish that files have finished downloading, passed integrity checks or matched their proposed references.

Source checksums and prepared FASTQ hashes concern different bytes and must be labelled separately. Unknown hashes and continuing downloads remain explicit in the dated verification table.
