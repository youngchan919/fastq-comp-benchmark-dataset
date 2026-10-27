# FASTQ compression benchmark dataset

Dataset version 1.2.0 • 27 October 2026

This dataset is for testing lossless FASTQ compression and decompression. It contains 52 public datasets covering common sequencing technologies and uses. Each entry explains why it was chosen, lists the files to download, and describes the input to test. The repository contains the catalogue and instructions; sequencing files are downloaded separately.

| Collection | Quantity |
| --- | --- |
| Datasets | 52 (51 FASTQ datasets and one BAM source) |
| Files to download | 91 (90 gzip FASTQ files and one BAM) |
| Listed download bytes | 1,404,952,612,896 |
| Suggested reference versions | 18 |

A fair lossless test must recover the exact uncompressed FASTQ bytes, including read names, sequences, quality characters, order and formatting. Downloaded gzip files are containers to decompress first. The one BAM input needs the fixed export described in the preparation guide. Download sizes are not uncompressed FASTQ sizes or compression results.

# What the annual public archive view establishes

The fixed cutoff is 30 September 2026. Stock includes all first public releases before 1 October 2026; the annual increment covers 1 October 2025–30 September 2026. The validated snapshot was retrieved 9 October 2026. Runs measure archived units; reported bases measure declared sequence volume; distinct known studies indicate research breadth. Release date is not sequencing/basecalling date, and study counts are not additive across categories. [Archive metadata](https://www.ebi.ac.uk/ena/portal/api/)

| Window | Runs | Reported 10¹⁵ bases | Known studies | Missing organism, runs |
| --- | --- | --- | --- | --- |
| Stock | 44,218,223 | 102.7062 | 703,005 | 3.82% |
| Annual increment | 5,872,478 | 23.5313 | 114,478 | 23.18% |

Stock has 378 missing/invalid base counts and 1,939,374 zero-base runs; the annual increment has 400,864 zero-base runs. Missing study labels affect 359,717 stock runs and 684 annual-increment runs. Organism labels are missing from 3.82% of stock runs and 23.18% of annual-increment runs; the share with missing organism names remains visible beside rankings. Exact totals and field distributions are in the [workbook](../catalogue/benchmark_dataset.xlsx).

The archive’s assay labels describe different sampling: whole-genome sequencing (WGS) spans genomes; exome sequencing (WXS) targets coding regions; RNA-Seq samples transcripts; amplicons focus on chosen regions. These labels do not fully specify preparation. Source describes the broad material, selection describes how a library was chosen, and layout distinguishes single from paired reads. Those fields must be considered together.

| Strategy | Stock runs | Stock base share | Annual-increment runs | Known stock studies |
| --- | --- | --- | --- | --- |
| AMPLICON | 18,359,855 | 4.66% | 2,070,368 | 116,706 |
| WGS | 9,295,474 | 37.84% | 1,458,845 | 192,425 |
| RNA-Seq | 8,648,389 | 37.48% | 1,233,249 | 279,311 |
| OTHER | 3,094,386 | 6.02% | 491,878 | 67,861 |
| RAD-Seq | 772,730 | 0.52% | 134,053 | 3,790 |
| Targeted-Capture | 624,557 | 0.95% | 124,748 | 4,554 |
| WXS | 561,043 | 1.51% | 21,343 | 7,569 |
| ChIP-Seq | 528,615 | 1.62% | 45,705 | 21,319 |
| WGA | 456,200 | 1.15% | 45,575 | 11,320 |
| Bisulfite-Seq | 295,839 | 2.17% | 63,930 | 5,593 |
| CLONE | 292,776 | 0.02% | 1,861 | 979 |
| ATAC-seq | 285,961 | 1.52% | 50,460 | 9,288 |

WGS and RNA-Seq together account for most reported bases, whereas amplicons account for 41.52% of stock runs but only 4.66% of bases. RAD/GBS and capture/functional libraries also have meaningful project breadth. Paired layout accounts for 77.08% of stock runs and 91.19% of bases. No single statistic determines the number of inputs; runs, bases and studies answer different questions.

| Raw platform label | Stock run share | Stock base share | Annual base share | Known stock studies |
| --- | --- | --- | --- | --- |
| ILLUMINA | 90.22% | 89.06% | 83.31% | 645,005 |
| DNBSEQ | 0.86% | 4.56% | 9.30% | 10,047 |
| BGISEQ | 0.74% | 2.46% | 3.16% | 9,502 |
| OXFORD_NANOPORE | 2.55% | 1.19% | 1.65% | 18,307 |
| PACBIO_SMRT | 2.18% | 1.98% | 2.01% | 28,602 |
| ION_TORRENT | 1.25% | 0.15% | 0.04% | 7,537 |
| ELEMENT | 0.21% | 0.15% | 0.33% | 1,014 |
| ULTIMA | 0.01% | 0.06% | 0.06% | 37 |

Raw labels remain separate. DNBSEQ/BGISEQ cannot simply be renamed a manufacturer market share. Platform, model, source and strategy combinations distinguish MiSeq community/genomic amplicons from high-throughput genomic/transcript work. For example, MiSeq METAGENOMIC/AMPLICON has 4,854,104 stock runs across 49,876 studies, while NovaSeq 6000 VIRAL RNA/AMPLICON has 4,287,045 runs across 142 studies. Similar run totals do not imply equally broad demand. Concentration and recent public release help interpret historical or emerging platforms. [Archive metadata](https://www.ebi.ac.uk/ena/portal/api/)

Raw organism rankings bring human/mouse, microbial isolates and communities into view, together with substantial plant and animal research. Wheat, rice, cotton, livestock, rat and primate labels broaden material considerations. Named organisms, communities, strain or other extended labels, and missing names are shown separately; no strain, subspecies or synonym merge is assumed. These are archive labels, not taxonomically verified species-market ranks.

Library_selection is absent from the saved metadata extract. Separate 14 October separately retrieved run counts total 44,218,009 stock and 5,872,258 annual-increment runs. Leading stock labels are pcr 36.99%, random 18.75% and cdna 13.53%; annual increment is pcr 38.45%, random 20.65% and cdna 13.15%. They describe broad selection labels, not complete preparation or measured file structure; they are not joined to the saved base/study statistics. [Selection-field counts](https://www.ebi.ac.uk/ena/portal/api/count)

# What the China archive view can and cannot compare

| Source and vintage | Actual finding | Limit |
| --- | --- | --- |
| CNSA live chart retrieved 15Oct 2026, September point | 339,790 public runs;1,352,228 total runs | Current-vintage holdings point; not a verified first-release or immutable month-end census. |
| CNSA current model table | Explicit Samples/Experiments/Runs; T1:393,676 runs;BGISEQ500:244,358;G400:114,987;T7:74,348;NovaSeq 6000:84,521 | Unfiltered population; public subset/cutoff/geography unresolved. First 25 of 62 models retrieved. |
| GSA publication, December 2024 statistics | GSA965,023 archived runs; GSA-Human 1,248,968. Published open datasets 11,174 and 1,168 respectively. | Archived/public/open/controlled and dataset/run units differ. Worldwide submissions. |
| GSA mirrored NCBI holdings, December 2024 | 34,456,823 mirrored runs | Overlap with worldwide archive; never add as extra domestic production. |

These official sources show substantial China-hosted sequencing activity and technology/material variety. They do not supply comparable national public platform/assay percentages for the global annual window. The GSA live route failed; its archive-author publication and official news provide valid separate scope findings. A 100 PB submitted-holdings announcement is not public FASTQ bytes. Current unfiltered CNSA organism/sample charts are not normalized as public or domestic-production shares. Reused source retrieval dates are preserved; no new national census was attempted. [CNSA statistics and official aggregate endpoints](https://db.cngb.org/cnsa/statistic/) [The GSA Family in 2025](https://academic.oup.com/gpb/article/23/4/qzaf072/8241968) [GSA user-submitted holdings exceed 100 PB](https://ngdc.cncb.ac.cn/news/255)

# What the applied-use survey found

Broad application portfolios, material/industry accounts and operating/deployed service routes were examined separately and cross-checked. This is a purposeful primary-source survey, not a representative sales sample. A provider menu establishes availability; a completed research project, commissioned service, instrument deployment and recurring production claim each establish something different. The [discovery register](../evidence/survey_discovery_register.csv) records routes, findings, exclusions and unknowns. Sources that mix arrays, proteins, images or generic genetic testing are not all counted as FASTQ demand.

**Clinical and reproductive use**. CERTANIA lists arrays alongside sequencing, so its entire reproductive portfolio cannot be treated as read demand. Annoroad’s 15 April 2026 draft filing identifies non-invasive prenatal testing (NIPT) and copy-number sequencing (CNV-seq) solutions supplied to 109 hospitals and 15 independent clinical laboratories by 31 December 2025. These are supplied institutions, not annual tests or runs. NIPT/CNV describes an application; the cited evidence does not establish whether sampling is genome-wide or targeted. NHS WGS, an accredited Ion Torrent laboratory and commercial exome/NGS testing provide separate applied-use support. [CERTANIA portfolio](https://certania.com/services/molecular-diagnostics-and-genomics) [Annoroad 2026 filing](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [NHS genomic service](https://www.england.nhs.uk/nhs-genomic-medicine-service/) [Targeted laboratory service](https://pmc.ncbi.nlm.nih.gov/articles/PMC10958377/) [Natera 2025 report](https://www.sec.gov/Archives/edgar/data/1604821/000110465926047801/ntra-20251231xars.pdf) [Burning Rock 2025 report](https://ir.brbiotech.com/static-files/c8cee243-84ea-4ac3-b94f-3b76dbabdcc4)

**Population, reference and ecological material**. DArT explicitly offers sequencing-based reduced-representation genotyping; not every genotype report or ecological project necessarily used it. Provider research accounts involve wheat, grape/Vitis, buckwheat and sugarcane genomic/reference work. PIC reports genome information for more than 8,000 elite pigs as an accumulated resource, while a poultry WGS paper and breeding-reference projects are completed research. None is converted into annual species sales. [DArTseq service](https://www.diversityarrays.com/services/dartseq/) [DArT ecological services](https://www.diversityarrays.com/industries/ecologists-and-biodiversity/) [Annoroad 2026 filing](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Annoroad research accounts](https://www.annoroad.com/) [PIC genome resource](https://cms.genusplc.com/pic-nz/services/data-capture/) [Poultry WGS research](https://link.springer.com/article/10.1186/s12711-026-01085-2) [Breeding-reference project](https://www.plantbreeding.wur.nl/Solyntus/)

**Environmental and food uses**. China’s environment ministry describes actual aquatic DNA sequencing and a demonstrated 19-section Yangtze application. The exact library/instrument is not established. Food Forensics offers NGS ingredient identification; Hebei reports completed food-authenticity sequencing research separately from digital PCR. These give real sequencing links, while exact target sampling remains unresolved. Generic ecological DNA testing without a sequencing link remains an inquiry. [MEE monitoring account](https://www.mee.gov.cn/ywdt/hjywnews/202603/t20260312_1146462.shtml) [Food Forensics service](https://www.foodforensics.co.uk/technical-solutions/ngs-testing) [Hebei food research](https://scjg.hebei.gov.cn/info/84546) [Food NGS workflow](https://www.thermofisher.com/sg/en/home/industrial/food-beverage/food-authenticity-labeling/ngs-food-screening-species-identification.html)

**Biopharma and modern research**. GenomeScan explicitly offers producer-cell WGS; Eurofins and a China-facing HyQure service advertise NGS characterization. These establish availability, not annual production volumes or all quality-control tests. SeqMatic’s operating services distinguish DNA/RNA, epigenomics, spatial and single-cell workflows, with 10x/Parse as workflow suppliers rather than sequencer manufacturers. Applied company research corroborates some tagged/functional library uses. [GenomeScan service](https://genomescan.nl/genetic-characterization/) [HyQure service](https://www.hyqure.com/gmp-ngs-services) [Eurofins BPT services](https://www.eurofins.com/en/biopharma-services/biopharma-product-testing/services/next-generation-sequencing-ngs/) [SeqMatic portfolio](https://www.seqmatic.com/services/) [Company single-cell research](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292621) [Company CUT&RUN research](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7883167)

**Scale and technology direction**. Novogene reports 45,885.51 TB of produced sequence in FY2025, defining 1 TB as 10¹² bases: consolidated worldwide output, not storage bytes or China-only production. Named provider operation supports Ultima alongside established short/long-read families. MGI reports CycloneSEQ installations at two named China service sites. Roche’s dated 29 June 2026 SBX launch and July financial disclosure are more specific in time than an undated generic development footnote, but launch/research collaboration still does not establish broad production. These are scoped business/research reasons for technology attention, not novelty or corporate-size arguments. [Novogene 2025 report](https://static.cninfo.com.cn/finalpage/2026-04-15/1225103513.PDF) [SeqMatic portfolio](https://www.seqmatic.com/services/) [CycloneSEQ installations](https://www.mgi-tech.com/mgi-news/945.html) [Roche June launch](https://www.roche.com/investors/updates/inv-update-2026-06-29) [Roche July results](https://www.roche.com/media/releases/med-cor-2026-07-23) [Undated Roche page](https://diagnostics.roche.com/global/en/products/product-category/lab-type/sequencing.html) [SBX research presentations](https://diagnostics.roche.com/se/en/diagnostics-insights/introductory-sequencing-by-expansion-webinar.html)

# How the datasets were chosen

The archive survey shows which kinds of sequencing are common and how much sequence they contain. Publicly documented research, services and technology deployments add uses that archive counts alone may miss. Worldwide includes China; the two views are never added. A service listing establishes availability, not sales volume. A crop’s economic value alone does not establish sequencing demand.

| Selection rule | What it means here |
| --- | --- |
| Choose important workloads | Use archive runs, reported bases and research breadth alongside documented applied use. Do not give every species, manufacturer or named application its own file automatically. |
| Keep useful differences | Include important library, technology, read and reference differences. Similar quality alphabets do not establish similar frequency patterns. A difference is not a measured compression advantage. |
| Use a complete, sensible input | A complete deposited run or public vendor output can be the appropriate unit. Compare sequence amount with the same task and unit; do not prefer smaller files simply to save space. |
| Fix the bytes and references | List every file belonging to the input. Preserve exact prepared FASTQ bytes and state reference versions and remaining preparation. Select before testing compressors. |

Source-study comparisons support particular examples; they are not universal production norms. There is no minimum file size, target dataset count, score or claim that this is the smallest possible collection. Annual review may keep the same inputs when their reasons remain sound.

The workbook separates the sequencer manufacturer from the library method. Illumina and MGI commonly supply parallel short reads; ONT, CycloneSEQ and PacBio supply single-molecule long-read technologies. These are often called second- and third-generation sequencing. A 10x or CITE library label does not identify the sequencer. Archive strategy labels describe what was sampled, while layout describes single or paired reads.

The collection includes human and other genome sequencing; bulk, small and single-cell RNA; CITE tags and spatial reads; chromatin libraries; targeted markers; isolates and mixed communities. The workbook’s Coverage, Materials and Technology sheets explain the links between those uses and the selected entries. Detailed archive tables and source notes remain available there.

Reported sequence totals are separate from file sizes and read/spot counts. Known selected FASTQ totals sum to 2,012,275,239,298 bases across 50 inputs. Exact source totals for Data 6 and Data 8 are unknown and excluded; associated analysis or SRA totals are not substituted. Study counts are not added across overlapping categories.

# Why some files are small

11 complete inputs contain less than one decimal GB of compressed downloads after all their files are counted. A target library, individual cell, sample tag or compact genome can be a meaningful small input. Amount is judged against the task, not a one-GB floor. Startup and reference overhead can matter for small files, but no such performance has been measured here. Files are not padded or repeated to make them larger.

# The 52 datasets

Read the reasons below alongside the [workbook](../catalogue/benchmark_dataset.xlsx), [all file links](../catalogue/files.tsv) and [current verification notes](../checksums/README.md). Data IDs identify entries within this version. Each entry’s amount is reported sequence, while its listed bytes describe the download. In the workbook, Reasons gives the short explanation and Details preserves the full amount evidence, processing notes and observation scope.

## Data 1. Human genome — MGI G400

This human whole-genome run represents routine MGI short-read sequencing. Its inspected reads use a wide range of quality characters. Together with Data 2 and 3, it lets a compressor face different quality patterns without changing the broad human-genome task.

Amount: 122,627,292,300 bases (122.627 billion). Download: 73,841,588,662 bytes (73.842 decimal GB) in 2 file(s).

Why this amount: 122.63 billion bases is roughly a 40x human-genome budget.

Public run(s): [ERR17003126](https://www.ebi.ac.uk/ena/browser/view/ERR17003126). Reference: fa ID 1 / GCF_000001405.40.

## Data 2. Human genome — MGI T7, concentrated qualities

This human whole-genome run adds a different quality pattern from Data 1. In the saved prefixes, the most common quality character accounts for 90.07% of R1 positions and 86.46% of R2 positions. These observations describe only the inspected reads; they do not establish a whole-file distribution or a compression result.

Amount: 131,251,843,800 bases (131.252 billion). Download: 66,737,537,425 bytes (66.738 decimal GB) in 2 file(s).

Why this amount: 131.25 billion bases is roughly a 42x human-genome budget, within common WGS planning.

Public run(s): [ERR16794642](https://www.ebi.ac.uk/ena/browser/view/ERR16794642). Reference: fa ID 1 / GCF_000001405.40.

## Data 3. Human genome — MGI T7, four-symbol qualities

This human genomic run adds a four-symbol quality pattern to the broader quality ranges in Data 1 and 2. It comes from an RPE1 ploidy-benchmark study, so it is not presented as an ordinary diploid patient sample. Seeing four symbols does not establish how the qualities were produced.

Amount: 127,540,227,000 bases (127.540 billion). Download: 48,041,300,140 bytes (48.041 decimal GB) in 2 file(s).

Why this amount: 127.54 billion bases lies within the eight-positive-run study range (nine records; one zero total).

Public run(s): [SRR33329596](https://www.ebi.ac.uk/ena/browser/view/SRR33329596). Reference: fa ID 1 / GCF_000001405.40.

## Data 4. Human genome — NovaSeq X Plus

This run represents mainstream Illumina whole-genome sequencing. The input is a complete deposited run/lane output, a unit that users can receive and store separately from other runs of the same sample. Its amount is close to the middle of its source study.

Amount: 39,313,093,714 bases (39.313 billion). Download: 15,853,763,048 bytes (15.854 decimal GB) in 2 file(s).

Why this amount: 39.31 billion bases is close to the 35.48-billion median of 24 comparable runs in its source study and within the positive-volume NovaSeq X archive middle-half range.

Public run(s): [ERR15383198](https://www.ebi.ac.uk/ena/browser/view/ERR15383198). Reference: fa ID 1 / GCF_000001405.40.

## Data 5. Human ultra-long nanopore reads

This input adds ultra-long human genomic reads alongside the ordinary nanopore and PacBio consensus inputs. The source study explicitly used ultra-long sequencing. The complete run provides a real example of that workload rather than a file assembled by selecting unusually long reads here.

Amount: 49,183,304,334 bases (49.183 billion). Download: 40,884,662,813 bytes (40.885 decimal GB) in 1 file(s).

Why this amount: 49.18 billion bases is close to the median 51.65 billion among 74 positive-yield source-study runs (79 records; five zero totals).

Public run(s): [ERR12954382](https://www.ebi.ac.uk/ena/browser/view/ERR12954382). Reference: fa ID 1 / GCF_000001405.40.

## Data 6. Human nanopore reads — one ONT flow cell

This named ONT flow-cell output represents current R10.4.1/Dorado human genomic sequencing. It is supplied as a complete BAM file. A fixed export rule will create the FASTQ to benchmark; that export has not been run, and its exact read and base totals are not yet known.

Amount: Exact selected-source sequence yield not established. Download: 171,763,325,052 bytes (171.763 decimal GB) in 1 file(s).

Why this amount: The release describes about 140 Gb per flow cell.

Public run(s): [PAW70337 SUP flow-cell source](https://ont-open-data.s3.amazonaws.com/giab_2025.01/basecalling/sup/HG002/PAW70337/calls.sorted.bam). Reference: fa ID 1 / GCF_000001405.40.

Check before use: The separate mapped-analysis totals are not verified as the exact BAM/export yield. The specified FASTQ export has not been run.

## Data 7. Human PacBio HiFi reads

This barcode-specific PacBio output adds HiFi consensus reads alongside raw PacBio CLR and nanopore reads. It is a documented output from one sequencing cell, not an arbitrary slice. Other outputs from the same sample are separate choices, not unlisted parts of this declared input.

Amount: 48,501,907,479 bases (48.502 billion). Download: 23,718,059,148 bytes (23.718 decimal GB) in 1 file(s).

Why this amount: The submitted source identifies a barcode-specific HiFi cell output with 48,501,907,479 reported bases.

Public run(s): [ERR14732808](https://www.ebi.ac.uk/ena/browser/view/ERR14732808). Reference: fa ID 1 / GCF_000001405.40.

Check before use: The selected amount is a barcode-specific cell output, not an entire Revio cell or every library for the individual.

## Data 8. Human CycloneSEQ nanopore reads

This file lets the collection test another nanopore technology alongside Oxford Nanopore. It contains human HG002 whole-genome reads from CycloneSEQ G400-ER. The chosen CNGB download is one single-read FASTQ file, not paired mates. The survey links the public research and named installations that support including this technology.

Amount: Exact selected-source sequence yield not established. Download: 130,270,589,600 bytes (130.271 decimal GB) in 1 file(s).

Why this amount: One CNGB FASTQ file, WY_reads.fq.gz, is listed at 130,270,589,600 compressed bytes. Its exact total reads and bases are unknown.

Public run(s): [CNR1409093 / CNX1236558](https://db.cngb.org/search/run/CNR1409093/). Reference: fa ID 1 / GCF_000001405.40.

Check before use: No publisher MD5 is available. Matching the listed size is not a full integrity check. Exact total reads and bases, and byte equivalence to SRA files, are unknown.

Method and amount sources: [CNGB exact run and experiment metadata](https://db.cngb.org/search/experiment/CNX1236558/) [Bounded prefix inspection of selected CNGB object](https://ftp.cngb.org/pub/CNSA/data7/CNP0007646/CNS1382495/CNX1236558/CNR1409093/WY_reads.fq.gz)

## Data 9. Human exome sequencing

This library represents human exome sequencing, which samples selected coding regions rather than the whole genome. It comes from an FFPE tumour study. Keeping that context explicit avoids treating its amount and preparation as a generic germline sample.

Amount: 5,446,687,469 bases (5.447 billion). Download: 2,415,095,443 bytes (2.415 decimal GB) in 2 file(s).

Why this amount: The source has 38 FFPE exome runs with median 5.650 billion bases.

Public run(s): [ERR12411150](https://www.ebi.ac.uk/ena/browser/view/ERR12411150). Reference: fa ID 1 / GCF_000001405.40.

## Data 10. Maize resequencing

This PCR-free maize library represents ordinary crop resequencing. Its amount is close to the middle of the study's 513 libraries with reported yields. Both FASTQ ends of the SW1611 run are included. The proposed B73 reference is from the same species but a different inbred line.

Amount: 47,789,487,240 bases (47.789 billion). Download: 24,082,143,756 bytes (24.082 decimal GB) in 2 file(s).

Why this amount: The primary panel study describes approximately 20× DNA resequencing.

Public run(s): [SRR8906645](https://www.ebi.ac.uk/ena/browser/view/SRR8906645). Reference: fa ID 10 / GCF_902167145.1.

Check before use: Trimming is indicated by the submitted filename, but the exact steps are unknown. The actual FASTQ lengths and qualities have not been inspected.

Method and amount sources: [Maize association-panel primary study](https://www.nature.com/articles/s41588-019-0427-6) [Exact PCR-free maize experiment](https://www.ebi.ac.uk/ena/browser/view/SRX5692588) [Exact SW1611 maize sample](https://www.ebi.ac.uk/ena/browser/view/SAMN11370298) [Exact maize run quantities and representation](https://www.ncbi.nlm.nih.gov/sra/SRR8906645)

## Data 11. Human targeted sequencing — Ion Torrent

This human amplicon run adds targeted sequencing on a semiconductor instrument. It differs from whole-genome sequencing in what is sampled and from the Illumina/MGI inputs in technology. Its amount is close to the middle of 133 comparable runs from the same study.

Amount: 1,497,990,828 bases (1.498 billion). Download: 1,154,396,293 bytes (1.154 decimal GB) in 1 file(s).

Why this amount: The selected named amplicon run has 1,497,990,828 reported bases.

Public run(s): [DRR341924](https://www.ebi.ac.uk/ena/browser/view/DRR341924). Reference: fa ID 1 / GCF_000001405.40.

## Data 12. Spruce target capture

This spruce library represents population genotyping by target capture. Its 335 million reported bases are small relative to the proposed 11.96-billion-base spruce reference. That contrast is worth testing for reference-based compression, but no effect has been measured. The archive groups three submitted lane pairs into the two listed FASTQ ends.

Amount: 335,384,842 bases (335.385 million). Download: 177,775,032 bytes (177.775 decimal MB) in 2 file(s).

Why this amount: The 335,384,842-base archive run lies in the lower range of 7,729 project runs with median 584 million bases.

Public run(s): [SRR19440963](https://www.ebi.ac.uk/ena/browser/view/SRR19440963). Reference: fa ID 15 / GCA_900067695.1.

Check before use: The source grouping is metadata evidence, not body-level merge or order verification.

Method and amount sources: [Exact spruce capture experiment and submitted objects](https://www.ncbi.nlm.nih.gov/sra/SRX15494349) [Versioned spruce assembly metadata](https://www.ebi.ac.uk/ena/browser/view/GCA_900067695.1)

## Data 13. Quinoa reduced-representation genotyping

This RAD library represents crop genotyping from selected parts of a genome. Its amount is close to the middle of 136 comparable study runs. A whole-genome-sized file would describe a different task, so this complete paired run is an appropriate small input.

Amount: 894,720,418 bases (894.720 million). Download: 571,962,433 bytes (571.962 decimal MB) in 2 file(s).

Why this amount: 895 million bases is close to the median 872 million among 136 matching population-study runs.

Public run(s): [DRR095727](https://www.ebi.ac.uk/ena/browser/view/DRR095727). Reference: fa ID 16 / GCF_001683475.1.

## Data 14. Pig genome with supplied constant qualities

This pig genomic run covers livestock sequencing and a file in which the inspected qualities are constant. Those qualities are part of the bytes to preserve. Their origin is unknown, so they are not described as typical native MGI quality output.

Amount: 26,338,729,500 bases (26.339 billion). Download: 10,018,740,265 bytes (10.019 decimal GB) in 2 file(s).

Why this amount: 26.34 billion bases is close to the very tight approximately 26.19-billion median of 147 source-study runs.

Public run(s): [SRR24804436](https://www.ebi.ac.uk/ena/browser/view/SRR24804436). Reference: fa ID 2 / GCF_054392235.1.

Check before use: The original role is an assembly/resequencing study component.

## Data 15. Mouse genome sequencing

This mouse tail-DNA run adds a commonly used research animal and its genome reference. It is one complete germline library. Its amount is the lowest of five similarly prepared tail libraries, rather than a subset created for this benchmark. The sample's exact match to the proposed strain reference still needs checking.

Amount: 100,892,053,998 bases (100.892 billion). Download: 48,335,307,261 bytes (48.335 decimal GB) in 2 file(s).

Why this amount: Five like-prepared germline-tail outputs contain 100.892–139.281 billion bases, with median 118.131 billion.

Public run(s): [ERR14032264](https://www.ebi.ac.uk/ena/browser/view/ERR14032264). Reference: fa ID 3 / GCF_000001635.27.

## Data 16. Wheat whole-genome resequencing — Thatcher

This ordinary wheat resequencing run adds a large, polyploid crop genome. Both FASTQ ends of one Thatcher sample are included. The primary study reports about 542.5 billion bases and 35× coverage for this sample; this is a real study input, not a subset made to reach a benchmark size. The proposed Chinese Spring assembly is from the same species but a different cultivar.

Amount: 542,472,250,800 bases (542.472 billion). Download: 273,813,897,418 bytes (273.814 decimal GB) in 2 file(s).

Why this amount: One Thatcher resequencing run contains 542,472,250,800 reported bases; the primary study reports approximately 542.5 Gb and 35×.

Public run(s): [ERR9904291](https://www.ebi.ac.uk/ena/browser/view/ERR9904291). Reference: fa ID 18 / GCF_018294505.1.

Method and amount sources: [Thatcher run, experiment and file metadata](https://www.ebi.ac.uk/ena/browser/view/ERR9904291) [Wheat study reporting Thatcher resequencing amount](https://www.nature.com/articles/s41588-023-01401-2) [ENA counts, release dates and file checksums for the selected wheat, CITE and CHO runs](https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=run_accession%3D%22ERR9904291%22+OR+run_accession%3D%22ERR2189808%22+OR+run_accession%3D%22SRR19066659%22+OR+run_accession%3D%22SRR19066665%22+OR+run_accession%3D%22SRR19066668%22&fields=run_accession%2Cread_count%2Cbase_count%2Cfirst_public%2Cfastq_bytes%2Cfastq_md5&format=json&limit=5)

## Data 17. Potato genome assembly — Altus library

This PCR-free Altus library adds a tetraploid crop-assembly example. The input is one complete library with a documented 470-base insert. The 470 bases describe the full DNA insert sequenced from both ends, not the length of either read or just the gap between them. Other insert sizes and linked-read preparations are separate libraries.

Amount: 70,556,516,868 bases (70.557 billion). Download: 52,291,517,076 bytes (52.292 decimal GB) in 2 file(s).

Why this amount: Three same-sample libraries with 470 bp inserts contain 68.017,70.557 and 70.976 billion bases.

Public run(s): [SRR14993639](https://www.ebi.ac.uk/ena/browser/view/SRR14993639). Reference: fa ID 6 / GCF_000226075.1.

Check before use: This is one named PCR-free library, not the entire cultivar assembly dataset.

Method and amount sources: [Altus potato genome-assembly project](https://www.ebi.ac.uk/ena/browser/view/PRJNA718240)

## Data 18. Shrimp genome sequencing

This run adds a marine invertebrate used in aquaculture breeding research. It gives the collection an animal genome and reference beyond human, mouse and livestock. Its amount is close to the middle of ten comparable runs in the source study.

Amount: 26,760,937,872 bases (26.761 billion). Download: 18,466,075,422 bytes (18.466 decimal GB) in 2 file(s).

Why this amount: 26.76 billion bases is close to the 26.96-billion median among ten matched inbreeding-study runs.

Public run(s): [DRR1000971](https://www.ebi.ac.uk/ena/browser/view/DRR1000971). Reference: fa ID 11 / GCF_042767895.1.

## Data 19. Chicken genome sequencing

This input covers poultry genome resequencing, supported by the breeding-use survey. It is drawn from a substantial study of laying hens. Its amount falls within the middle 80% of the study's reported run amounts.

Amount: 19,596,096,600 bases (19.596 billion). Download: 14,336,554,441 bytes (14.337 decimal GB) in 2 file(s).

Why this amount: 19.60 billion bases lies within the 13.90–20.80-billion middle-80% range of the 1,004-layer study.

Public run(s): [ERR13943038](https://www.ebi.ac.uk/ena/browser/view/ERR13943038). Reference: fa ID 12 / GCF_016699485.2.

## Data 20. Human raw PacBio CLR reads

This HG002 library adds raw PacBio CLR reads alongside HiFi consensus reads. The exact library is labelled HG002-CLR. Its supplied quality values and archive format are kept as deposited; they are not assumed to describe native qualities or every raw PacBio file.

Amount: 113,896,753,645 bases (113.897 billion). Download: 34,654,458,158 bytes (34.654 decimal GB) in 1 file(s).

Why this amount: 113.90 billion reported raw bases is a substantial genomic input.

Public run(s): [SRR8801873](https://www.ebi.ac.uk/ena/browser/view/SRR8801873). Reference: fa ID 1 / GCF_000001405.40.

## Data 21. Plant nanopore genome assembly

This Arabidopsis Col-0 input adds plant nuclear-genome assembly reads from nanopore sequencing. It is the complete submitted pass-read output of one named run. Fail reads and alternative basecalls are separate representations, not missing pieces of this chosen file.

Amount: 10,554,533,391 bases (10.555 billion). Download: 9,919,475,722 bytes (9.919 decimal GB) in 1 file(s).

Why this amount: The chosen pass output contains 10,554,533,391 reported bases.

Public run(s): [ERR13669551](https://www.ebi.ac.uk/ena/browser/view/ERR13669551). Reference: fa ID 9 / GCF_000001735.4.

Check before use: The chosen PASS output excludes fail reads.

## Data 22. Plant PacBio HiFi genome assembly

This Arabidopsis Col-0 readset adds plant HiFi consensus sequencing. The paper's accession, AT_HiFi library name and reported amount agree with the archive record. That documentation establishes the method; the archive filename containing _subreads does not establish it by itself.

Amount: 22,904,700,074 bases (22.905 billion). Download: 18,526,201,575 bytes (18.526 decimal GB) in 1 file(s).

Why this amount: The published plant HiFi readset contains 22.90 billion bases; exact archive metadata reports 22,904,700,074 bases for AT_HiFi.

Public run(s): [SRR14728885](https://www.ebi.ac.uk/ena/browser/view/SRR14728885). Reference: fa ID 9 / GCF_000001735.4.

Check before use: Documentary HiFi identity does not establish a particular quality alphabet or whole-file accuracy.

## Data 23. Human RNA sequencing — MGI

This input represents ordinary human RNA sequencing on MGI short-read instruments. It complements the human genomic inputs and the Illumina expression library. Its amount is close to the middle of eight runs in its source study.

Amount: 4,828,141,800 bases (4.828 billion). Download: 3,817,894,154 bytes (3.818 decimal GB) in 2 file(s).

Why this amount: 4.83 billion bases is near the 4.81-billion median of eight source-study runs and is a plausible ordinary expression-library amount.

Public run(s): [ERR10030615](https://www.ebi.ac.uk/ena/browser/view/ERR10030615). Reference: fa ID 1 / GCF_000001405.40.

## Data 24. Plant RNA sequencing

This wild-type Arabidopsis Col-0 replicate represents bulk plant RNA sequencing. It is one named expression library, with an amount within the range of fourteen RNA outputs in the source study. The comparison supports this example, not a universal production requirement.

Amount: 7,102,948,500 bases (7.103 billion). Download: 3,632,286,064 bytes (3.632 decimal GB) in 2 file(s).

Why this amount: Fourteen RNA outputs in the source study span 5.214–8.809 billion bases, with median 6.467 billion.

Public run(s): [SRR14627767](https://www.ebi.ac.uk/ena/browser/view/SRR14627767). Reference: fa ID 9 / GCF_000001735.4.

## Data 25. Human small-RNA sequencing

This biological replicate represents small-RNA sequencing. Short RNA molecules make it a naturally small input; the inspected reads vary from 18 to 44 bases. The library's read and base totals fit the source study. Its biological target does not establish which trimming steps were applied before deposition.

Amount: 284,297,641 bases (284.298 million). Download: 291,749,840 bytes (291.750 decimal MB) in 1 file(s).

Why this amount: 12.64 million reported single reads and 284 million bases match the eight-run study, whose base median is 286 million.

Public run(s): [DRR1089360](https://www.ebi.ac.uk/ena/browser/view/DRR1089360). Reference: fa ID 1 / GCF_000001405.40.

Method and amount sources: [Exact named small-RNA replicate](https://www.ncbi.nlm.nih.gov/sra/DRX1064881)

## Data 26. Human RNA sequencing — Illumina

This input represents a conventional Illumina human expression library. It complements the MGI and newer short-read RNA inputs. Its amount is close to the middle of twelve comparable runs in the source study.

Amount: 4,002,783,900 bases (4.003 billion). Download: 1,795,309,208 bytes (1.795 decimal GB) in 2 file(s).

Why this amount: 4.00 billion bases is close to the 4.11-billion median of 12 matching study runs and within the wider positive-volume NovaSeq RNA range.

Public run(s): [DRR1069746](https://www.ebi.ac.uk/ena/browser/view/DRR1069746). Reference: fa ID 1 / GCF_000001405.40.

## Data 27. Single-end RNA sequencing — Element AVITI

This AVITI library adds a commercially deployed short-read technology in its documented single-end RNA configuration. It should be tested as supplied, rather than judged against a paired-end library. Its amount is close to the middle of eighteen source-study runs.

Amount: 3,095,516,700 bases (3.096 billion). Download: 2,301,820,230 bytes (2.302 decimal GB) in 1 file(s).

Why this amount: 3.10 billion bases is close to the 2.98-billion median of 18 source-study runs and within the wider AVITI single-end RNA range across 20 known studies.

Public run(s): [SRR30608496](https://www.ebi.ac.uk/ena/browser/view/SRR30608496). Reference: fa ID 1 / GCF_000001405.40.

## Data 28. Nanopore transcript sequencing

This input adds nanopore reads from a transcript-derived library, alongside nanopore genomic reads. The source documents a full-length library; that describes the intended sampling, not a guarantee that every deposited read is long or complete. Its read count is comparable to the study's library amounts.

Amount: 2,480,166,369 bases (2.480 billion). Download: 2,307,675,498 bytes (2.308 decimal GB) in 1 file(s).

Why this amount: The source paper reports 310.8 million raw reads across 72 libraries, an arithmetic average of 4.32 million.

Public run(s): [SRR36288068](https://www.ebi.ac.uk/ena/browser/view/SRR36288068). Reference: fa ID 1 / GCF_000001405.40.

Check before use: This is same-study scale support, not a general long-RNA production norm.

## Data 29. One mouse Smart-seq2 cell

This mouse bladder cell adds transcript-wide single-cell RNA sequencing alongside the 3-prime CITE libraries. Smart-seq2 samples across transcripts; it does not make every read span a whole transcript. Both ends of one SRA run are included, with an amount within the middle half of 660 annotated cells.

Amount: 220,101,000 bases (220.101 million). Download: 97,956,122 bytes (97.956 decimal MB) in 2 file(s).

Why this amount: Among 660 author-annotated bladder cells with one listed run each, reported amounts have median 182,126,200 bases and middle-half range 139,362,300–226,050,350.

Public run(s): [SRR6520293](https://www.ebi.ac.uk/ena/browser/view/SRR6520293). Reference: fa ID 3 / GCF_000001635.27.

Check before use: The author and archive identify one cell in one run. The exact pre-upload processing stage and actual FASTQ properties remain unexamined.

Method and amount sources: [Primary transcript-wide single-cell atlas](https://www.nature.com/articles/s41586-018-0590-4) [Exact bladder Smart-seq2 method and experiment](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2967045) [Official single-cell run and original-file mapping](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE109nnn/GSE109774/suppl/GSE109774_list_of_SRR_accessions_and_raw_filenames.txt.gz) [Author bladder single-cell annotations](https://raw.githubusercontent.com/czbiohub-sf/tabula-muris/master/00_data_ingest/03_tissue_annotation_csv/Bladder_facs_annotation.csv) [Exact Smart-seq2 experiment run quantities](https://www.ebi.ac.uk/ena/browser/view/SRX3607041) [Exact selected Smart-seq2 run](https://www.ebi.ac.uk/ena/browser/view/SRR6520293)

## Data 30. CITE antibody tags

These antibody-derived tag reads complement the mRNA input in Data 31 and sample-tag input in Data 32 from the same CITE experiment. The selected input is one complete paired ADT run, with both ends. Tags carry a different kind of information from transcript reads; the three components are not replicate copies.

Amount: 13,478,870,416 bases (13.479 billion). Download: 5,458,838,862 bytes (5.459 decimal GB) in 2 file(s).

Why this amount: Among the two largest outputs from each of 19 ADT experiments (38 runs), reported bases have median 13.065736 billion and range 10.638356–18.672885 billion. The selected run has 13,478,870,416 reported bases.

Public run(s): [SRR19066659](https://www.ebi.ac.uk/ena/browser/view/SRR19066659). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Check before use: The two listed ends define this run. Cell-recovery targets do not establish its actual cell count; observations, where available, apply only to these exact files.

Method and amount sources: [CITE component-run metadata and matched amount comparisons](https://www.ebi.ac.uk/ena/browser/view/PRJNA834796) [ENA counts, release dates and file checksums for the selected wheat, CITE and CHO runs](https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=run_accession%3D%22ERR9904291%22+OR+run_accession%3D%22ERR2189808%22+OR+run_accession%3D%22SRR19066659%22+OR+run_accession%3D%22SRR19066665%22+OR+run_accession%3D%22SRR19066668%22&fields=run_accession%2Cread_count%2Cbase_count%2Cfirst_public%2Cfastq_bytes%2Cfastq_md5&format=json&limit=5)

## Data 31. CITE mRNA reads

These mRNA reads provide the transcript component of the same CITE experiment as the antibody-tag input in Data 30 and sample-tag input in Data 32. Both FASTQ ends of one complete paired run are included. The tag libraries cannot substitute for this expression library.

Amount: 35,465,206,140 bases (35.465 billion). Download: 18,634,282,939 bytes (18.634 decimal GB) in 2 file(s).

Why this amount: Among the two largest outputs from each of 19 mRNA experiments (38 runs), reported bases have median 38.490196 billion and range 34.674149–52.108714 billion. The selected run has 35,465,206,140 reported bases.

Public run(s): [SRR19066665](https://www.ebi.ac.uk/ena/browser/view/SRR19066665). Reference: fa ID 1 / GCF_000001405.40.

Check before use: The two listed ends define this run. Cell-recovery targets do not establish its actual cell count; observations, where available, apply only to these exact files.

Method and amount sources: [CITE component-run metadata and matched amount comparisons](https://www.ebi.ac.uk/ena/browser/view/PRJNA834796) [ENA counts, release dates and file checksums for the selected wheat, CITE and CHO runs](https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=run_accession%3D%22ERR9904291%22+OR+run_accession%3D%22ERR2189808%22+OR+run_accession%3D%22SRR19066659%22+OR+run_accession%3D%22SRR19066665%22+OR+run_accession%3D%22SRR19066668%22&fields=run_accession%2Cread_count%2Cbase_count%2Cfirst_public%2Cfastq_bytes%2Cfastq_md5&format=json&limit=5)

## Data 32. CITE sample tags

These sample-tag reads provide the sample-identification component of the same CITE experiment as Data 30 and Data 31. Both ends of one complete paired HTO run are included. It is a naturally small tag input; a tag definition may help interpretation or custom reference matching, but generic lossless compression does not require one.

Amount: 393,276,078 bases (393.276 million). Download: 172,719,082 bytes (172.719 decimal MB) in 2 file(s).

Why this amount: Across all 62 HTO runs, reported bases have median 0.3823 billion and range 0.3335–1.5649 billion. The selected run has 393,276,078 reported bases.

Public run(s): [SRR19066668](https://www.ebi.ac.uk/ena/browser/view/SRR19066668). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Check before use: The two listed ends define this run. Cell-recovery targets do not establish its actual cell count; observations, where available, apply only to these exact files.

Method and amount sources: [CITE component-run metadata and matched amount comparisons](https://www.ebi.ac.uk/ena/browser/view/PRJNA834796) [ENA counts, release dates and file checksums for the selected wheat, CITE and CHO runs](https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=run_accession%3D%22ERR9904291%22+OR+run_accession%3D%22ERR2189808%22+OR+run_accession%3D%22SRR19066659%22+OR+run_accession%3D%22SRR19066665%22+OR+run_accession%3D%22SRR19066668%22&fields=run_accession%2Cread_count%2Cbase_count%2Cfirst_public%2Cfastq_bytes%2Cfastq_md5&format=json&limit=5)

## Data 33. Spatial transcript sequencing — Stereo-seq

This run adds spatial transcript sequencing, where barcode and transcript reads serve different roles and can have different lengths. The complete named run is large because it is a real spatial input. Its capture area and cell/bin depths are unknown; neither should be inferred from file size.

Amount: 248,408,655,120 bases (248.409 billion). Download: 181,786,356,695 bytes (181.786 decimal GB) in 2 file(s).

Why this amount: The named L01 spatial run contains 248,408,655,120 reported bases.

Public run(s): [SRR29351083](https://www.ebi.ac.uk/ena/browser/view/SRR29351083). Reference: fa ID 1 / GCF_000001405.40.

Check before use: Capture area and observed cell/bin depths remain unknown.

## Data 34. Bulk ATAC sequencing

This K562 library represents a conventional paired bulk-ATAC replicate. It samples accessible chromatin rather than genome-wide DNA or RNA. Its amount is close to the middle of 32 study runs, although total bases do not establish the number of useful, distinct fragments.

Amount: 9,954,897,900 bases (9.955 billion). Download: 4,218,603,299 bytes (4.219 decimal GB) in 2 file(s).

Why this amount: Thirty-two positive ATAC source runs span 6.612–19.462 billion bases, with median 10.146 billion.

Public run(s): [SRR30495077](https://www.ebi.ac.uk/ena/browser/view/SRR30495077). Reference: fa ID 1 / GCF_000001405.40.

## Data 35. Rice ChIP sequencing

This rice library adds ChIP sequencing, which samples protein-associated chromatin. ATAC and CUT&RUN use different preparations and do not replace it. Its amount is close to the middle of eleven comparable runs in the study.

Amount: 7,848,285,900 bases (7.848 billion). Download: 3,388,187,408 bytes (3.388 decimal GB) in 2 file(s).

Why this amount: 7.85 billion bases is close to its 11-run study median of 7.98 billion and within the wider rice ChIP middle-80% range of 3.36–10.57 billion.

Public run(s): [DRR1000045](https://www.ebi.ac.uk/ena/browser/view/DRR1000045). Reference: fa ID 8 / GCF_034140825.1.

## Data 36. Human CUT&RUN sequencing

This run adds CUT&RUN, documented by its exact experiment even though the archive uses the broad OTHER label. It complements ATAC and ChIP inputs. Its amount falls within the middle 80% of thirty comparable study runs.

Amount: 2,142,233,300 bases (2.142 billion). Download: 1,123,492,148 bytes (1.123 decimal GB) in 2 file(s).

Why this amount: 2.14 billion bases lies inside the matched 30-run study’s middle-80% range of 1.79–5.13 billion.

Public run(s): [SRR26362943](https://www.ebi.ac.uk/ena/browser/view/SRR26362943). Reference: fa ID 1 / GCF_000001405.40; fa ID 13 / GCF_000001215.4.

Check before use: Normalization-reference composition and processed/usable depth remain unknown.

## Data 37. Yeast Hi-C sequencing

This yeast library adds proximity-ligation reads used to study contacts between genome regions. Its compact eukaryotic reference also differs from the large animal and plant references. Its amount lies within both the source-study range and the wider yeast Hi-C comparison.

Amount: 15,039,534,000 bases (15.040 billion). Download: 7,074,255,254 bytes (7.074 decimal GB) in 2 file(s).

Why this amount: 15.04 billion bases is within both its 56-run study range and the wider yeast Hi-C middle-80% range of 1.78–26.40 billion.

Public run(s): [SRR30894055](https://www.ebi.ac.uk/ena/browser/view/SRR30894055). Reference: fa ID 7 / GCF_000146045.2.

## Data 38. Human accessibility sequencing — Ultima

This Ultima input adds a deployed sequencing technology in an accessibility assay. The supplied single-read, variable-length format differs from the conventional paired ATAC input. Its amount is within the middle 80% of the 248-run source study.

Amount: 9,613,662,904 bases (9.614 billion). Download: 3,749,797,716 bytes (3.750 decimal GB) in 1 file(s).

Why this amount: 9.61 billion bases lies within the 248-run study’s middle-80% range of 3.93–11.02 billion.

Public run(s): [SRR34546226](https://www.ebi.ac.uk/ena/browser/view/SRR34546226). Reference: fa ID 1 / GCF_000001405.40.

## Data 39. Rice bisulfite sequencing

This rice library adds bisulfite sequencing, whose preparation changes the sequence letters being stored. Ordinary genome sequencing or capture does not supply the same condition. Its amount is comparable to its source study and the wider rice bisulfite examples.

Amount: 19,651,497,831 bases (19.651 billion). Download: 9,477,168,274 bytes (9.477 decimal GB) in 2 file(s).

Why this amount: 19.65 billion bases is close to its six-run study and within the wider rice bisulfite middle-80% range of 7.77–22.60 billion.

Public run(s): [DRR1009870](https://www.ebi.ac.uk/ena/browser/view/DRR1009870). Reference: fa ID 8 / GCF_034140825.1.

## Data 40. Fungal ITS community markers

This soil-root fungal library adds ITS marker sequencing on MiSeq. Both submitted read ends of FL_fungi_1 are included. Its amount is close to the middle of twelve ITS libraries from the same study. Those fungal libraries are compared separately from the study's bacterial 16S libraries.

Amount: 42,963,536 bases (42.964 million). Download: 19,328,691 bytes (19.329 decimal MB) in 2 file(s).

Why this amount: Twelve target-matched ITS libraries span 38.014–44.784 million bases, with median 42.678 million.

Public run(s): [SRR30515680](https://www.ebi.ac.uk/ena/browser/view/SRR30515680). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Method and amount sources: [Exact fungal ITS library and submitted pair](https://www.ncbi.nlm.nih.gov/sra/SRX25939332)

## Data 41. Bacterial 16S community markers

This soil-root bacterial library adds classic 16S community-marker sequencing. Both read ends of SH_bacteria_1 are included. Its amount is close to the middle of twelve bacterial libraries from the study; fungal ITS is a different target and does not replace this input.

Amount: 32,742,178 bases (32.742 million). Download: 17,916,463 bytes (17.916 decimal MB) in 2 file(s).

Why this amount: Twelve target-matched bacterial 16S libraries span 21.537–42.351 million bases, with median 32.662 million.

Public run(s): [SRR30515673](https://www.ebi.ac.uk/ena/browser/view/SRR30515673). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Method and amount sources: [Exact bacterial 16S library and submitted pair](https://www.ncbi.nlm.nih.gov/sra/SRX25939339)

## Data 42. Viral amplicon sequencing

This specimen-level viral amplicon run adds targeted sequencing of a small genome. Its amount is close to the middle of 58 comparable specimen outputs. A human whole-genome-sized delivery would not represent this task.

Amount: 67,831,999 bases (67.832 million). Download: 31,561,554 bytes (31.562 decimal MB) in 2 file(s).

Why this amount: 67.83 million bases is near the 73.35-million median among 58 comparable specimen runs, inside their middle-80% range.

Public run(s): [DRR1051020](https://www.ebi.ac.uk/ena/browser/view/DRR1051020). Reference: fa ID 14 / NC_045512.2.

## Data 43. Freshwater environmental-DNA markers

This input adds aquatic environmental-DNA marker sequencing. The library is associated with filter ITD20, extraction A and marker set VENE from Lugano. Both archive read ends are included. It is a sample/marker output, not an entire sequencing pool; the exact upstream filtering and barcode-splitting stage is unknown.

Amount: 22,955,020 bases (22.955 million). Download: 6,829,143 bytes (6.829 decimal MB) in 2 file(s).

Why this amount: Exact metadata lists the ITD20-A/VENE library, both submitted sample/marker-associated FASTQs and the two chosen archive ends.

Public run(s): [ERR7749063](https://www.ebi.ac.uk/ena/browser/view/ERR7749063). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Check before use: The precise upstream demultiplexing and filtering boundary remains unresolved.

Method and amount sources: [Exact short-read aquatic marker archive unit](https://www.ebi.ac.uk/ena/browser/view/ERR7749063) [Official aquatic sample/site table and naming descriptions](https://www.ebi.ac.uk/biostudies/studies/S-BSST391) [Author workflow manifest and sample sheet](https://github.com/envmetagen/mussels_package)

## Data 44. Tuberculosis bacterial isolate

This input adds a compact bacterial genome beyond E. coli and an inspected trimmed-read format. Its compressed size is below one GB, yet its reported bases are substantial relative to the reference. It lies somewhat above the source study's upper decile, rather than being an ordinary median example.

Amount: 833,183,051 bases (833.183 million). Download: 549,265,430 bytes (549.265 decimal MB) in 2 file(s).

Why this amount: 833 million bases is about 189 times the reference length in raw bases.

Public run(s): [ERR11252400](https://www.ebi.ac.uk/ena/browser/view/ERR11252400). Reference: fa ID 5 / GCF_000195955.2.

## Data 45. E. coli bacterial isolate

This named MG1655 strain provides a classic bacterial-isolate input with a compact reference. The paired run's amount is close to both its source-study median and the broader E. coli comparison. Exact sample/reference agreement and usable mapped coverage still need checking.

Amount: 450,083,225 bases (450.083 million). Download: 344,072,580 bytes (344.073 decimal MB) in 2 file(s).

Why this amount: 450 million bases is close to the broader E. coli Illumina median of 435 million and its eight-run study median of 428 million; it is about 97 times the reference length in raw bases.

Public run(s): [DRR171213](https://www.ebi.ac.uk/ena/browser/view/DRR171213). Reference: fa ID 4 / GCF_000005845.2.

## Data 46. Yeast whole-genome sequencing

This input adds a compact eukaryotic microbial genome alongside bacterial isolates. Genome sequencing also differs from the yeast Hi-C preparation. Its amount is toward the upper end of its study, making it a high-yield research example rather than a claimed universal norm.

Amount: 2,123,156,100 bases (2.123 billion). Download: 1,034,612,012 bytes (1.035 decimal GB) in 2 file(s).

Why this amount: 2.12 billion bases is near the upper quartile of its 61-run study and about 176 times the reference length in raw bases.

Public run(s): [SRR30502372](https://www.ebi.ac.uk/ena/browser/view/SRR30502372). Reference: fa ID 7 / GCF_000146045.2.

## Data 47. Long-read mock community

This run adds long reads from a known mixture of genomes. It differs from single-organism genome sequencing and short community-marker libraries. The source explicitly describes ultra-deep sequencing of a mock community, so its amount belongs to that research purpose.

Amount: 16,506,755,978 bases (16.507 billion). Download: 17,147,527,495 bytes (17.148 decimal GB) in 1 file(s).

Why this amount: 16.51 billion bases is close to the four-positive-run source-study range (six records; two zero totals).

Public run(s): [ERR3152366](https://www.ebi.ac.uk/ena/browser/view/ERR3152366). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

## Data 48. Fermentation community RNA

This paired library represents RNA sequencing of a cereal-fermentation community at one named timepoint. Its amount lies within five documented timepoints. It adds a mixed-community RNA task, rather than treating all metagenomic inputs as DNA sequencing.

Amount: 10,323,974,492 bases (10.324 billion). Download: 4,133,721,402 bytes (4.134 decimal GB) in 2 file(s).

Why this amount: Five named fermentation timepoints contain 10.324–11.764 billion bases, with median 11.198 billion.

Public run(s): [DRR1003246](https://www.ebi.ac.uk/ena/browser/view/DRR1003246). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

## Data 49. Soil shotgun community DNA

This input represents environmental shotgun DNA sequencing. It complements the gut and food mixtures and the targeted soil-marker inputs. Its amount is close to the middle of eight study runs and consistent with the wider soil comparison.

Amount: 10,115,398,800 bases (10.115 billion). Download: 7,496,700,808 bytes (7.497 decimal GB) in 2 file(s).

Why this amount: 10.12 billion bases is close to its eight-run study median of 10.32 billion and within the broad soil shotgun range; the median of known-study medians is 12.91 billion.

Public run(s): [DRR1000746](https://www.ebi.ac.uk/ena/browser/view/DRR1000746). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

## Data 50. Gut shotgun community DNA

This input represents ordinary human-gut shotgun DNA sequencing. It provides a host-associated community alongside soil and food mixtures. Its amount fits both its source study and the wider gut-study comparison.

Amount: 6,596,836,500 bases (6.597 billion). Download: 3,130,599,344 bytes (3.131 decimal GB) in 2 file(s).

Why this amount: 6.60 billion bases is close to its 30-run study and inside the wider gut shotgun middle-80% range of 0.29–9.86 billion; the median of study medians is 4.81 billion.

Public run(s): [DRR1003638](https://www.ebi.ac.uk/ena/browser/view/DRR1003638). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

## Data 51. Honey shotgun community DNA

This honey-derived run adds food-associated shotgun DNA sequencing. It is a complete paired run with an amount within the source study's 63-run range. The mixed reference setting differs from pure crop genomes and bacterial isolates; the actual ingredient/community proportions are not established.

Amount: 5,697,274,998 bases (5.697 billion). Download: 2,096,744,147 bytes (2.097 decimal GB) in 2 file(s).

Why this amount: 5.70 billion bases lies within the 0.74–6.14-billion middle-80% range of 63 matched honey-study runs.

Public run(s): [SRR27931704](https://www.ebi.ac.uk/ena/browser/view/SRR27931704). Reference: Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Method and amount sources: [Exact honey shotgun source sample](https://www.ebi.ac.uk/ena/browser/view/SRX23588786)

## Data 52. CHO genome-assembly research

This PCR-free CHO genomic run represents genome-assembly research on an industrial production-cell lineage. Both ends of one named CHO6262360 sample are included, with 67.10 billion reported bases. It is an assembly-related genomic workload, not a manufacturing quality-control assay or the entire project.

Amount: 67,097,495,750 bases (67.097 billion). Download: 39,740,914,851 bytes (39.741 decimal GB) in 2 file(s).

Why this amount: The named CHO6262360 paired genomic run contains 67,097,495,750 reported bases.

Public run(s): [ERR2189808](https://www.ebi.ac.uk/ena/browser/view/ERR2189808). Reference: fa ID 17 / GCF_003668045.3.

Check before use: ENA generated the listed FASTQs from submitted CRAM; they are not certified untouched instrument files. The exact CHO derivative and agreement with the proposed reference remain unknown. The files and their order, lengths, qualities and integrity have not been examined.

Method and amount sources: [CHO6262360 paired genomic run metadata](https://www.ebi.ac.uk/ena/browser/view/ERR2189808) [ENA counts, release dates and file checksums for the selected wheat, CITE and CHO runs](https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=run_accession%3D%22ERR9904291%22+OR+run_accession%3D%22ERR2189808%22+OR+run_accession%3D%22SRR19066659%22+OR+run_accession%3D%22SRR19066665%22+OR+run_accession%3D%22SRR19066668%22&fields=run_accession%2Cread_count%2Cbase_count%2Cfirst_public%2Cfastq_bytes%2Cfastq_md5&format=json&limit=5)

# Download, check and prepare the files

The [download and checksum guide](../checksums/README.md) separates publisher MD5 expectations from checks completed locally. Its status table is a dated snapshot, not a promise that every file has finished downloading. A matching size alone does not prove file integrity. A checksum for a compressed source file does not identify the decompressed FASTQ bytes.

Use the [preparation guide](preparation.md) to check source files, decompress each gzip file separately and record the uncompressed FASTQ byte count and SHA-256. Preserve names, sequence, quality, order and formatting. Do not concatenate mates, runs or chunks, normalize records or recompress the prepared input. Full gzip CRC/EOF checks must pass.

Data 6 requires the specified SAMtools 1.22/htslib 1.22 export. It uses natural QNAME order, primary unpaired records, stored qualities and a stop on missing primary qualities. This rule has synthetic tests, but the real BAM has not been exported. Prepared order is not native instrument order, and FASTQ does not preserve BAM tags or alignments.

Saved prefix observations apply only to the exact files identified in Files. They are nonrandom samples, not whole-file distributions or integrity checks. A quality character is an encoded value in the FASTQ quality line; modal share means the percentage of inspected quality positions occupied by its most common character. New or uninspected files do not inherit another file’s measurements.

Data 8 is one SINGLE CNGB file, not two mates or chunks. Its whole-file yield and byte equivalence to the associated SRA files are unknown. The saved prefix contains 258 complete reads with lengths 355–28,912 bases; it does not establish the distribution of the whole file. No publisher MD5 is available.

# Reference versions

The 18 reference choices were checked against NCBI on 27 October 2026. Use the current NCBI-designated reference genome for each species, retaining the MG1655 strain for the matching E. coli input. The fixed SARS-CoV-2 reference remains NC_045512.2. A current reference can have an old release date; it is not necessarily the most recently submitted assembly. Exact versions, download links and available publisher MD5 values are listed in the fa sheet and reference table. FASTA files were not downloaded in this update. A species reference does not guarantee a match to the sample, cultivar or transcript targets. Mixed communities and tag libraries have no single genome assigned.

fa 1: Homo sapiens — GRCh38.p14 / [GCF_000001405.40](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/). Human reference genome; matching to individual donors has not been checked.

fa 2: Sus scrofa — Sscrofa_HxYL_maternal_Yorkshire_Landrace_v2.0 / [GCF_054392235.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_054392235.1/). Yorkshire/Landrace pig reference; the selected FASTQ sample's breed has not been established.

fa 3: Mus musculus — GRCm39 / [GCF_000001635.27](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001635.27/). C57BL/6J mouse reference; donor substrain and transcript targets need checking. ERCC spike-ins require a separate reference.

fa 4: Escherichia coli str. K-12 substr. MG1655 — ASM584v2 / [GCF_000005845.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/). MG1655 reference for the MG1655 input; exact read-to-reference matching has not been measured.

fa 5: Mycobacterium tuberculosis H37Rv — ASM19595v2 / [GCF_000195955.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000195955.2/). H37Rv reference; the selected sample's exact strain match has not been checked.

fa 6: Solanum tuberosum — SolTub_3.0 / [GCF_000226075.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000226075.1/). DM 1-3 516 R44 reference for the Altus potato input; these are different cultivars.

fa 7: Saccharomyces cerevisiae S288C — R64 / [GCF_000146045.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000146045.2/). S288C yeast reference; exact strain matching has not been checked.

fa 8: Oryza sativa Japonica Group — AGIS1.0 / [GCF_034140825.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_034140825.1/). Nipponbare japonica rice reference; cultivars of the two selected rice inputs have not been confirmed.

fa 9: Arabidopsis thaliana — TAIR10.1 / [GCF_000001735.4](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001735.4/). Columbia Arabidopsis reference; sample and target matching has not been checked.

fa 10: Zea mays — Zm-B73-REFERENCE-NAM-5.0 / [GCF_902167145.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_902167145.1/). B73 maize reference for SW1611 reads; these are different inbred lines.

fa 11: Penaeus vannamei — ASM4276789v1 / [GCF_042767895.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_042767895.1/). JL-2024 whiteleg shrimp reference; exact sample matching has not been checked.

fa 12: Gallus gallus — bGalGal1.mat.broiler.GRCg7b / [GCF_016699485.2](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_016699485.2/). Broiler maternal chicken reference; matching to the selected laying-hen sample has not been checked.

fa 13: Drosophila melanogaster — Release 6 plus ISO1 MT / [GCF_000001215.4](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001215.4/). Drosophila reference; exact sample matching has not been checked.

fa 14: Severe acute respiratory syndrome coronavirus 2 — NC_045512.2 / [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2). Fixed Wuhan-Hu-1 reference; matching to the selected sample and targets has not been checked.

fa 15: Picea abies — Pabies01 / [GCA_900067695.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_900067695.1/). Norway spruce reference for the targeted input; exact sample and target matching has not been checked.

fa 16: Chenopodium quinoa — ASM168347v1 / [GCF_001683475.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_001683475.1/). QQ74 quinoa reference; exact cultivar matching has not been checked.

fa 17: Cricetulus griseus — CriGri-PICRH-1.0 / [GCF_003668045.3](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_003668045.3/). 17A/GY Chinese hamster reference for the CHO input; cell-line differences have not been measured.

fa 18: Triticum aestivum — IWGSC CS RefSeq v2.1 / [GCF_018294505.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_018294505.1/). Chinese Spring wheat reference for Thatcher reads; these are different cultivars.

Chinese Spring and the Thatcher wheat input are different cultivars. CITE tag definitions, spatial masks and taxonomy tables remain separate auxiliary files.

# Files for every input

The following list contains every selected file. Preserve the two ends of each paired run as separate FASTQs. The one BAM and one single-read CNGB file are listed separately. Names and URLs are exact catalogue values.

| Data ID | Run / source | End / role | Exact filename | Download |
| --- | --- | --- | --- | --- |
| 1 | ERR17003126 | Read end 1; pairing unverified | ERR17003126_1.fastq.gz | [ERR17003126_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR170/026/ERR17003126/ERR17003126_1.fastq.gz) |
| 1 | ERR17003126 | Read end 2; pairing unverified | ERR17003126_2.fastq.gz | [ERR17003126_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR170/026/ERR17003126/ERR17003126_2.fastq.gz) |
| 2 | ERR16794642 | Read end 1; pairing unverified | ERR16794642_1.fastq.gz | [ERR16794642_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR167/042/ERR16794642/ERR16794642_1.fastq.gz) |
| 2 | ERR16794642 | Read end 2; pairing unverified | ERR16794642_2.fastq.gz | [ERR16794642_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR167/042/ERR16794642/ERR16794642_2.fastq.gz) |
| 3 | SRR33329596 | Read end 1; pairing unverified | SRR33329596_1.fastq.gz | [SRR33329596_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR333/096/SRR33329596/SRR33329596_1.fastq.gz) |
| 3 | SRR33329596 | Read end 2; pairing unverified | SRR33329596_2.fastq.gz | [SRR33329596_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR333/096/SRR33329596/SRR33329596_2.fastq.gz) |
| 4 | ERR15383198 | Read end 1; pairing unverified | ERR15383198_1.fastq.gz | [ERR15383198_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR153/098/ERR15383198/ERR15383198_1.fastq.gz) |
| 4 | ERR15383198 | Read end 2; pairing unverified | ERR15383198_2.fastq.gz | [ERR15383198_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR153/098/ERR15383198/ERR15383198_2.fastq.gz) |
| 5 | ERR12954382 | Single supplied FASTQ object | ERR12954382.fastq.gz | [ERR12954382.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR129/082/ERR12954382/ERR12954382.fastq.gz) |
| 6 | ONT_GIAB2025_HG002_PAW70337_SUP | BAM source; later FASTQ export | calls.sorted.bam | [calls.sorted.bam](https://ont-open-data.s3.amazonaws.com/giab_2025.01/basecalling/sup/HG002/PAW70337/calls.sorted.bam) |
| 7 | ERR14732808 | Single supplied FASTQ object | ERR14732808.fastq.gz | [ERR14732808.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR147/008/ERR14732808/ERR14732808.fastq.gz) |
| 8 | CNR1409093 | Single-read FASTQ source; not mates | WY_reads.fq.gz | [WY_reads.fq.gz](https://ftp.cngb.org/pub/CNSA/data7/CNP0007646/CNS1382495/CNX1236558/CNR1409093/WY_reads.fq.gz) |
| 9 | ERR12411150 | Read end 1; pairing unverified | ERR12411150_1.fastq.gz | [ERR12411150_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR124/050/ERR12411150/ERR12411150_1.fastq.gz) |
| 9 | ERR12411150 | Read end 2; pairing unverified | ERR12411150_2.fastq.gz | [ERR12411150_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR124/050/ERR12411150/ERR12411150_2.fastq.gz) |
| 10 | SRR8906645 | Read end 1; pairing unverified | SRR8906645_1.fastq.gz | [SRR8906645_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR890/005/SRR8906645/SRR8906645_1.fastq.gz) |
| 10 | SRR8906645 | Read end 2; pairing unverified | SRR8906645_2.fastq.gz | [SRR8906645_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR890/005/SRR8906645/SRR8906645_2.fastq.gz) |
| 11 | DRR341924 | Single supplied FASTQ object | DRR341924.fastq.gz | [DRR341924.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR341/DRR341924/DRR341924.fastq.gz) |
| 12 | SRR19440963 | Read end 1; pairing unverified | SRR19440963_1.fastq.gz | [SRR19440963_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR194/063/SRR19440963/SRR19440963_1.fastq.gz) |
| 12 | SRR19440963 | Read end 2; pairing unverified | SRR19440963_2.fastq.gz | [SRR19440963_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR194/063/SRR19440963/SRR19440963_2.fastq.gz) |
| 13 | DRR095727 | Read end 1; pairing unverified | DRR095727_1.fastq.gz | [DRR095727_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR095/DRR095727/DRR095727_1.fastq.gz) |
| 13 | DRR095727 | Read end 2; pairing unverified | DRR095727_2.fastq.gz | [DRR095727_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR095/DRR095727/DRR095727_2.fastq.gz) |
| 14 | SRR24804436 | Read end 1; pairing unverified | SRR24804436_1.fastq.gz | [SRR24804436_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR248/036/SRR24804436/SRR24804436_1.fastq.gz) |
| 14 | SRR24804436 | Read end 2; pairing unverified | SRR24804436_2.fastq.gz | [SRR24804436_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR248/036/SRR24804436/SRR24804436_2.fastq.gz) |
| 15 | ERR14032264 | Read end 1 | ERR14032264_1.fastq.gz | [ERR14032264_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR140/064/ERR14032264/ERR14032264_1.fastq.gz) |
| 15 | ERR14032264 | Read end 2 | ERR14032264_2.fastq.gz | [ERR14032264_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR140/064/ERR14032264/ERR14032264_2.fastq.gz) |
| 16 | ERR9904291 | Read end 1 | ERR9904291_1.fastq.gz | [ERR9904291_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR990/001/ERR9904291/ERR9904291_1.fastq.gz) |
| 16 | ERR9904291 | Read end 2 | ERR9904291_2.fastq.gz | [ERR9904291_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR990/001/ERR9904291/ERR9904291_2.fastq.gz) |
| 17 | SRR14993639 | Read end 1; pairing unverified | SRR14993639_1.fastq.gz | [SRR14993639_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR149/039/SRR14993639/SRR14993639_1.fastq.gz) |
| 17 | SRR14993639 | Read end 2; pairing unverified | SRR14993639_2.fastq.gz | [SRR14993639_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR149/039/SRR14993639/SRR14993639_2.fastq.gz) |
| 18 | DRR1000971 | Read end 1; pairing unverified | DRR1000971_1.fastq.gz | [DRR1000971_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/001/DRR1000971/DRR1000971_1.fastq.gz) |
| 18 | DRR1000971 | Read end 2; pairing unverified | DRR1000971_2.fastq.gz | [DRR1000971_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/001/DRR1000971/DRR1000971_2.fastq.gz) |
| 19 | ERR13943038 | Read end 1; pairing unverified | ERR13943038_1.fastq.gz | [ERR13943038_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR139/038/ERR13943038/ERR13943038_1.fastq.gz) |
| 19 | ERR13943038 | Read end 2; pairing unverified | ERR13943038_2.fastq.gz | [ERR13943038_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR139/038/ERR13943038/ERR13943038_2.fastq.gz) |
| 20 | SRR8801873 | Single supplied FASTQ object | SRR8801873_subreads.fastq.gz | [SRR8801873_subreads.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR880/003/SRR8801873/SRR8801873_subreads.fastq.gz) |
| 21 | ERR13669551 | Single supplied FASTQ object | ERR13669551.fastq.gz | [ERR13669551.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR136/051/ERR13669551/ERR13669551.fastq.gz) |
| 22 | SRR14728885 | Single supplied FASTQ object | SRR14728885_subreads.fastq.gz | [SRR14728885_subreads.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR147/085/SRR14728885/SRR14728885_subreads.fastq.gz) |
| 23 | ERR10030615 | Read end 1; pairing unverified | ERR10030615_1.fastq.gz | [ERR10030615_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR100/015/ERR10030615/ERR10030615_1.fastq.gz) |
| 23 | ERR10030615 | Read end 2; pairing unverified | ERR10030615_2.fastq.gz | [ERR10030615_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR100/015/ERR10030615/ERR10030615_2.fastq.gz) |
| 24 | SRR14627767 | Read end 1 | SRR14627767_1.fastq.gz | [SRR14627767_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR146/067/SRR14627767/SRR14627767_1.fastq.gz) |
| 24 | SRR14627767 | Read end 2 | SRR14627767_2.fastq.gz | [SRR14627767_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR146/067/SRR14627767/SRR14627767_2.fastq.gz) |
| 25 | DRR1089360 | Single supplied FASTQ object | DRR1089360.fastq.gz | [DRR1089360.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR108/000/DRR1089360/DRR1089360.fastq.gz) |
| 26 | DRR1069746 | Read end 1; pairing unverified | DRR1069746_1.fastq.gz | [DRR1069746_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR106/006/DRR1069746/DRR1069746_1.fastq.gz) |
| 26 | DRR1069746 | Read end 2; pairing unverified | DRR1069746_2.fastq.gz | [DRR1069746_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR106/006/DRR1069746/DRR1069746_2.fastq.gz) |
| 27 | SRR30608496 | Single supplied FASTQ object | SRR30608496.fastq.gz | [SRR30608496.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR306/096/SRR30608496/SRR30608496.fastq.gz) |
| 28 | SRR36288068 | Single supplied FASTQ object | SRR36288068_1.fastq.gz | [SRR36288068_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR362/068/SRR36288068/SRR36288068_1.fastq.gz) |
| 29 | SRR6520293 | Read end 1; pairing unverified | SRR6520293_1.fastq.gz | [SRR6520293_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR652/003/SRR6520293/SRR6520293_1.fastq.gz) |
| 29 | SRR6520293 | Read end 2; pairing unverified | SRR6520293_2.fastq.gz | [SRR6520293_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR652/003/SRR6520293/SRR6520293_2.fastq.gz) |
| 30 | SRR19066659 | Read end 1 | SRR19066659_1.fastq.gz | [SRR19066659_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_1.fastq.gz) |
| 30 | SRR19066659 | Read end 2 | SRR19066659_2.fastq.gz | [SRR19066659_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_2.fastq.gz) |
| 31 | SRR19066665 | Read end 1 | SRR19066665_1.fastq.gz | [SRR19066665_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_1.fastq.gz) |
| 31 | SRR19066665 | Read end 2 | SRR19066665_2.fastq.gz | [SRR19066665_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_2.fastq.gz) |
| 32 | SRR19066668 | Read end 1 | SRR19066668_1.fastq.gz | [SRR19066668_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_1.fastq.gz) |
| 32 | SRR19066668 | Read end 2 | SRR19066668_2.fastq.gz | [SRR19066668_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_2.fastq.gz) |
| 33 | SRR29351083 | Read end 1; pairing unverified | SRR29351083_1.fastq.gz | [SRR29351083_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR293/083/SRR29351083/SRR29351083_1.fastq.gz) |
| 33 | SRR29351083 | Read end 2; pairing unverified | SRR29351083_2.fastq.gz | [SRR29351083_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR293/083/SRR29351083/SRR29351083_2.fastq.gz) |
| 34 | SRR30495077 | Read end 1 | SRR30495077_1.fastq.gz | [SRR30495077_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR304/077/SRR30495077/SRR30495077_1.fastq.gz) |
| 34 | SRR30495077 | Read end 2 | SRR30495077_2.fastq.gz | [SRR30495077_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR304/077/SRR30495077/SRR30495077_2.fastq.gz) |
| 35 | DRR1000045 | Read end 1; pairing unverified | DRR1000045_1.fastq.gz | [DRR1000045_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/005/DRR1000045/DRR1000045_1.fastq.gz) |
| 35 | DRR1000045 | Read end 2; pairing unverified | DRR1000045_2.fastq.gz | [DRR1000045_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/005/DRR1000045/DRR1000045_2.fastq.gz) |
| 36 | SRR26362943 | Read end 1; pairing unverified | SRR26362943_1.fastq.gz | [SRR26362943_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR263/043/SRR26362943/SRR26362943_1.fastq.gz) |
| 36 | SRR26362943 | Read end 2; pairing unverified | SRR26362943_2.fastq.gz | [SRR26362943_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR263/043/SRR26362943/SRR26362943_2.fastq.gz) |
| 37 | SRR30894055 | Read end 1; pairing unverified | SRR30894055_1.fastq.gz | [SRR30894055_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR308/055/SRR30894055/SRR30894055_1.fastq.gz) |
| 37 | SRR30894055 | Read end 2; pairing unverified | SRR30894055_2.fastq.gz | [SRR30894055_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR308/055/SRR30894055/SRR30894055_2.fastq.gz) |
| 38 | SRR34546226 | Single supplied FASTQ object | SRR34546226.fastq.gz | [SRR34546226.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR345/026/SRR34546226/SRR34546226.fastq.gz) |
| 39 | DRR1009870 | Read end 1; pairing unverified | DRR1009870_1.fastq.gz | [DRR1009870_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/000/DRR1009870/DRR1009870_1.fastq.gz) |
| 39 | DRR1009870 | Read end 2; pairing unverified | DRR1009870_2.fastq.gz | [DRR1009870_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/000/DRR1009870/DRR1009870_2.fastq.gz) |
| 40 | SRR30515680 | Read end 1 | SRR30515680_1.fastq.gz | [SRR30515680_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/080/SRR30515680/SRR30515680_1.fastq.gz) |
| 40 | SRR30515680 | Read end 2 | SRR30515680_2.fastq.gz | [SRR30515680_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/080/SRR30515680/SRR30515680_2.fastq.gz) |
| 41 | SRR30515673 | Read end 1 | SRR30515673_1.fastq.gz | [SRR30515673_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/073/SRR30515673/SRR30515673_1.fastq.gz) |
| 41 | SRR30515673 | Read end 2 | SRR30515673_2.fastq.gz | [SRR30515673_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/073/SRR30515673/SRR30515673_2.fastq.gz) |
| 42 | DRR1051020 | Read end 1; pairing unverified | DRR1051020_1.fastq.gz | [DRR1051020_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR105/000/DRR1051020/DRR1051020_1.fastq.gz) |
| 42 | DRR1051020 | Read end 2; pairing unverified | DRR1051020_2.fastq.gz | [DRR1051020_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR105/000/DRR1051020/DRR1051020_2.fastq.gz) |
| 43 | ERR7749063 | Read end 1; pairing unverified | ERR7749063_1.fastq.gz | [ERR7749063_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR774/003/ERR7749063/ERR7749063_1.fastq.gz) |
| 43 | ERR7749063 | Read end 2; pairing unverified | ERR7749063_2.fastq.gz | [ERR7749063_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR774/003/ERR7749063/ERR7749063_2.fastq.gz) |
| 44 | ERR11252400 | Read end 1; pairing unverified | ERR11252400_1.fastq.gz | [ERR11252400_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR112/000/ERR11252400/ERR11252400_1.fastq.gz) |
| 44 | ERR11252400 | Read end 2; pairing unverified | ERR11252400_2.fastq.gz | [ERR11252400_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR112/000/ERR11252400/ERR11252400_2.fastq.gz) |
| 45 | DRR171213 | Read end 1; pairing unverified | DRR171213_1.fastq.gz | [DRR171213_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR171/DRR171213/DRR171213_1.fastq.gz) |
| 45 | DRR171213 | Read end 2; pairing unverified | DRR171213_2.fastq.gz | [DRR171213_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR171/DRR171213/DRR171213_2.fastq.gz) |
| 46 | SRR30502372 | Read end 1; pairing unverified | SRR30502372_1.fastq.gz | [SRR30502372_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/072/SRR30502372/SRR30502372_1.fastq.gz) |
| 46 | SRR30502372 | Read end 2; pairing unverified | SRR30502372_2.fastq.gz | [SRR30502372_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR305/072/SRR30502372/SRR30502372_2.fastq.gz) |
| 47 | ERR3152366 | Single supplied FASTQ object | ERR3152366.fastq.gz | [ERR3152366.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR315/006/ERR3152366/ERR3152366.fastq.gz) |
| 48 | DRR1003246 | Read end 1 | DRR1003246_1.fastq.gz | [DRR1003246_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/006/DRR1003246/DRR1003246_1.fastq.gz) |
| 48 | DRR1003246 | Read end 2 | DRR1003246_2.fastq.gz | [DRR1003246_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/006/DRR1003246/DRR1003246_2.fastq.gz) |
| 49 | DRR1000746 | Read end 1; pairing unverified | DRR1000746_1.fastq.gz | [DRR1000746_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/006/DRR1000746/DRR1000746_1.fastq.gz) |
| 49 | DRR1000746 | Read end 2; pairing unverified | DRR1000746_2.fastq.gz | [DRR1000746_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/006/DRR1000746/DRR1000746_2.fastq.gz) |
| 50 | DRR1003638 | Read end 1; pairing unverified | DRR1003638_1.fastq.gz | [DRR1003638_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/008/DRR1003638/DRR1003638_1.fastq.gz) |
| 50 | DRR1003638 | Read end 2; pairing unverified | DRR1003638_2.fastq.gz | [DRR1003638_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/DRR100/008/DRR1003638/DRR1003638_2.fastq.gz) |
| 51 | SRR27931704 | Read end 1; pairing unverified | SRR27931704_1.fastq.gz | [SRR27931704_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR279/004/SRR27931704/SRR27931704_1.fastq.gz) |
| 51 | SRR27931704 | Read end 2; pairing unverified | SRR27931704_2.fastq.gz | [SRR27931704_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR279/004/SRR27931704/SRR27931704_2.fastq.gz) |
| 52 | ERR2189808 | Read end 1 | ERR2189808_1.fastq.gz | [ERR2189808_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR218/008/ERR2189808/ERR2189808_1.fastq.gz) |
| 52 | ERR2189808 | Read end 2 | ERR2189808_2.fastq.gz | [ERR2189808_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR218/008/ERR2189808/ERR2189808_2.fastq.gz) |

# Updates and citation

Review the archive and applied-use evidence annually. Keep dataset IDs and exact file lists stable within a data version. [Versioning](../VERSIONING.md) explains which changes need a new version; adding verification results does not imply different input bytes. See [citation](../CITATION.md) and [rights](../RIGHTS.md) for repository attribution and the current license status. This collection supplies test inputs and evidence, not measured compression results.
