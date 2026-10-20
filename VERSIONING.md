# Dataset versions

[Home](README.md)

The current collection is **v1.0.0**. `VERSION` and `dataset_version` in the catalogue identify it. `schema_version` describes the manifest format and is separate.

A data version fixes the selected files, declared complete input units, reference versions and the rules that determine prepared FASTQ bytes. Some source checksums and preparation results are still unknown; a version number does not claim that all files have been downloaded or verified. The dated verification table reports that separately.

- **New input bytes or scientific definition:** use a new data version, such as v2.0.0, when adding/removing files or changing their contents, references or prepared-byte rules. Keep previous release tags unchanged.
- **Same inputs, improved repository:** use a patch version, such as v1.0.1, for corrected documentation, compatible tooling or added verification results that do not change the test inputs.
- **Annual review:** reconsider the evidence and availability once a year. A review does not require changing files or creating a new data version.

Release tags are immutable. A published tag must continue to identify the same Git commit; corrections use a new tag. Use the dataset version and the prepared FASTQ hashes when reporting a benchmark. A publisher checksum, a downloaded-file hash and a prepared-FASTQ hash identify different things and should be labelled accordingly.
