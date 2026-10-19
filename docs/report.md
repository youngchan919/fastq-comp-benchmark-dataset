# Building a public FASTQ compression benchmark

Global and China evidence, one public collection and preparation requirements • 19 October 2026

This report describes a public collection for lossless FASTQ compression tests. Public archive distributions and documented applied or research uses establish workload priorities; the selection principles then connect those needs to concrete inputs.

The purpose is to test useful kinds of input at representative real-world amounts. A complete named library may contain several paired runs; a documented flow-cell, barcode or lane output can also be a natural delivery unit. There is no rule that smaller inputs are preferable, or that every biological sample must include every preparation. Source-study quantities support the selected examples but do not establish market-wide production norms. Data IDs identify the current inputs in the workbook and report.

A FASTQ record stores a read name, sequence letters and one encoded quality character per base. Lossless decompression must restore the exact chosen input bytes, including names, sequences, qualities, order and formatting. A 150-base read has 150 quality positions, while a file can use four or 39 distinct quality characters across those positions. Frequency also matters: modal share means the percentage of inspected quality positions occupied by the most common quality character. These summaries do not measure compressor performance.

Uncompressed FASTQ bytes only; downloaded gzip objects are source containers, not benchmark inputs.

The NCBI Sequence Read Archive (SRA) and European Nucleotide Archive (ENA) organize public sequencing submissions into projects, samples, experiments and runs. Archive counts describe public submissions, not all production. One dataset here is a declared complete input unit, with every run, mate or chunk listed separately. Some compressors encode matching sequence segments through reference positions and differences, so a reference’s identity, version and match to the reads can affect representation and compression. Not every compressor requires a reference.

Four evidence views inform the choices: worldwide archives, worldwide applied/business use, China-hosted archives and China applied/business use. Worldwide includes China, so the views are not added. The archive cutoff is 30 September 2026. The survey findings below retain their stated source and retrieval dates.

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

Raw labels remain separate. DNBSEQ/BGISEQ cannot simply be renamed a manufacturer market share. Platform×model×source×strategy joints distinguish MiSeq community/genomic amplicons from high-throughput genomic/transcript work. For example, MiSeq METAGENOMIC/AMPLICON has 4,854,104 stock runs across 49,876 studies, while NovaSeq 6000 VIRAL RNA/AMPLICON has 4,287,045 runs across 142 studies. Similar run totals do not imply equally broad demand. Concentration and recent public release help interpret historical or emerging platforms. [Archive metadata](https://www.ebi.ac.uk/ena/portal/api/)

Raw organism rankings bring human/mouse, microbial isolates and communities into view, together with substantial plant and animal research. Wheat, rice, cotton, livestock, rat and primate labels broaden material considerations. Named organisms, communities, strain or other extended labels, and missing names are shown separately; no strain, subspecies or synonym merge is assumed. These are archive labels, not taxonomically verified species-market ranks.

Library_selection is absent from the frozen projection. Separate 14 October run-only marginals total 44,218,009 stock and 5,872,258 annual-increment runs. Leading stock labels are pcr 36.99%, random 18.75% and cdna 13.53%; annual increment is pcr 38.45%, random 20.65% and cdna 13.15%. They describe broad selection labels, not complete preparation or measured file structure; they are not joined to the frozen base/study statistics. [Selection-field counts](https://www.ebi.ac.uk/ena/portal/api/count)

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

**Clinical and reproductive use.** CERTANIA lists arrays alongside sequencing, so its entire reproductive portfolio cannot be treated as read demand. Annoroad’s 15 April 2026 draft filing identifies non-invasive prenatal testing (NIPT) and copy-number sequencing (CNV-seq) solutions supplied to 109 hospitals and 15 independent clinical laboratories by 31 December 2025. These are supplied institutions, not annual tests or runs. NIPT/CNV describes an application; the cited evidence does not establish whether sampling is genome-wide or targeted. NHS WGS, an accredited Ion Torrent laboratory and commercial exome/NGS testing provide separate applied-use support. [CERTANIA portfolio](https://certania.com/services/molecular-diagnostics-and-genomics) [Annoroad 2026 filing](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [NHS genomic service](https://www.england.nhs.uk/nhs-genomic-medicine-service/) [Targeted laboratory service](https://pmc.ncbi.nlm.nih.gov/articles/PMC10958377/) [Natera 2025 report](https://www.sec.gov/Archives/edgar/data/1604821/000110465926047801/ntra-20251231xars.pdf) [Burning Rock 2025 report](https://ir.brbiotech.com/static-files/c8cee243-84ea-4ac3-b94f-3b76dbabdcc4)

**Population, reference and ecological material.** DArT explicitly offers sequencing-based reduced-representation genotyping; not every genotype report or ecological project necessarily used it. Provider research accounts involve wheat, grape/Vitis, buckwheat and sugarcane genomic/reference work. PIC reports genome information for more than 8,000 elite pigs as an accumulated resource, while a poultry WGS paper and breeding-reference projects are completed research. None is converted into annual species sales. [DArTseq service](https://www.diversityarrays.com/services/dartseq/) [DArT ecological services](https://www.diversityarrays.com/industries/ecologists-and-biodiversity/) [Annoroad 2026 filing](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Annoroad research accounts](https://www.annoroad.com/) [PIC genome resource](https://cms.genusplc.com/pic-nz/services/data-capture/) [Poultry WGS research](https://link.springer.com/article/10.1186/s12711-026-01085-2) [Breeding-reference project](https://www.plantbreeding.wur.nl/Solyntus/)

**Environmental and food uses.** China’s environment ministry describes actual aquatic DNA sequencing and a demonstrated 19-section Yangtze application. The exact library/instrument is not established. Food Forensics offers NGS ingredient identification; Hebei reports completed food-authenticity sequencing research separately from digital PCR. These give real sequencing links, while exact target sampling remains unresolved. Generic ecological DNA testing without a sequencing link remains an inquiry. [MEE monitoring account](https://www.mee.gov.cn/ywdt/hjywnews/202603/t20260312_1146462.shtml) [Food Forensics service](https://www.foodforensics.co.uk/technical-solutions/ngs-testing) [Hebei food research](https://scjg.hebei.gov.cn/info/84546) [Food NGS workflow](https://www.thermofisher.com/sg/en/home/industrial/food-beverage/food-authenticity-labeling/ngs-food-screening-species-identification.html)

**Biopharma and modern research.** GenomeScan explicitly offers producer-cell WGS; Eurofins and a China-facing HyQure service advertise NGS characterization. These establish availability, not annual production volumes or all quality-control tests. SeqMatic’s operating services distinguish DNA/RNA, epigenomics, spatial and single-cell workflows, with 10x/Parse as workflow suppliers rather than sequencer manufacturers. Applied company research corroborates some tagged/functional library uses. [GenomeScan service](https://genomescan.nl/genetic-characterization/) [HyQure service](https://www.hyqure.com/gmp-ngs-services) [Eurofins BPT services](https://www.eurofins.com/en/biopharma-services/biopharma-product-testing/services/next-generation-sequencing-ngs/) [SeqMatic portfolio](https://www.seqmatic.com/services/) [Company single-cell research](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292621) [Company CUT&RUN research](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7883167)

**Scale and technology direction.** Novogene reports 45,885.51 TB of produced sequence in FY2025, defining 1 TB as 10¹² bases: consolidated worldwide output, not storage bytes or China-only production. Named provider operation supports Ultima alongside established short/long-read families. MGI reports CycloneSEQ installations at two named China service sites. Roche’s dated 29 June 2026 SBX launch and July financial disclosure are more specific in time than an undated generic development footnote, but launch/research collaboration still does not establish broad production. These are scoped business/research reasons for technology attention, not novelty or corporate-size arguments. [Novogene 2025 report](https://static.cninfo.com.cn/finalpage/2026-04-15/1225103513.PDF) [SeqMatic portfolio](https://www.seqmatic.com/services/) [CycloneSEQ installations](https://www.mgi-tech.com/mgi-news/945.html) [Roche June launch](https://www.roche.com/investors/updates/inv-update-2026-06-29) [Roche July results](https://www.roche.com/media/releases/med-cor-2026-07-23) [Undated Roche page](https://diagnostics.roche.com/global/en/products/product-category/lab-type/sequencing.html) [SBX research presentations](https://diagnostics.roche.com/se/en/diagnostics-insights/introductory-sequencing-by-expansion-webinar.html)

# How workloads and particular inputs were chosen

Archive exposure and publicly documented use establish important workflows; credible deployed or committed technology directions may also matter despite few public deposits. A particular input then needs a clear public identity, preparation, useful role, reference relationship and appropriate sequence amount. Different business purposes do not automatically require different files. Several needs can share an input, while distinct tagged, transformed, single/paired and raw/consensus representations may justify separate examples.

Representative amount is assessed in the relevant unit and purpose. The Renan polishing library and CHO genomic library include all their documented outputs. Each CITE component includes all four outputs of its own experiment, while ADT, mRNA and HTO remain separate. The Revio input is an explicitly identified barcode-specific cell output; it is not silently called an entire cell or all libraries for that person. A real run alone does not establish a universal production norm, and raw bases do not certify usable mapped depth.

Select public examples by these documented conditions, not compressor results, weighted scores, a desired entry count, a species checklist or one file per manufacturer. Preserve useful older conditions when their role is supported. The public-release cutoff is 30 September 2026; release date is distinct from sequencing and basecalling dates. No full source/reference data were downloaded, exported or benchmarked during packaging. Saved nonrandom prefix observations are scoped individually.

Instrument manufacturer, sequencer family and library supplier are separate fields. Illumina and MGI short-read systems commonly produce parallel, relatively fixed-length reads; ONT nanopore and PacBio single-molecule systems produce long-read representations. These are often called second- and third-generation technologies respectively. CycloneSEQ is an MGI nanopore family despite the archive’s broad BGISEQ label. A 10x, CITE or spatial library label does not identify the sequencer or prove its exact chemistry.

| Field | Meaning and selection consequence |
| --- | --- |
| Species/material | Human/model/crop/microbial references and mixed communities differ. Economic value alone does not establish sequencing demand; actual sample/reference agreement is a separate check. |
| Source | The broad material label: genomic, transcript-derived, community or another category. A broad archive label may require documentary clarification. |
| Strategy and selection | Strategy describes intended sampling; selection is a preparation label. WGS, RNA, exome/capture, amplicon, ATAC, ChIP, CUT&RUN and Hi-C are not interchangeable. Reproductive/CNV purpose alone does not prove capture or amplicon sampling. |
| Layout and components | Single/paired labels are distinct from library completeness. All mate ends, tags and chunks are explicit. An entire logical library may comprise several runs. |
| Read lengths, quality and headers | Only exact matched saved prefix observations establish measured properties. Unpreviewed objects are identified individually in Files. Prefixes are nonrandom, not whole-file distributions; similar alphabets need not have similar frequencies. |
| Reference and processing | Fix versioned reference identities and later FASTQ preparation/order. Raw CLR, consensus, trimming, filtering, merging, conversion and supplied constant qualities can change the byte representation. Interpretation masks/features are not automatic requirements for generic lossless compression. |

Reported read counts retain the source convention; no universal multiplier converts them to paired reads. Reported sequence bases are shown alongside counts. Known selected-source totals sum to 2,029,937,896,053 bases across 50 FASTQ inputs with known yield. Exact sequence-base totals are unavailable for Data 6 (BAM) and Data 8 (CNGB FASTQ), both excluded from this sum; associated analysis or SRA yields are not substituted as selected-source totals.

Saved profiles are reused only for exact matched file URLs. Observed properties apply only to the exact files identified in Files; they do not establish profiles for other files in the same library. The Files sheet identifies which exact objects have saved evidence. No whole-file integrity, pairing or representative distribution has been measured here. Publisher MD5 values are listed where already recorded, never claimed computed.

# Coverage served and needs still open

## Human genome-wide sequencing

Large reported base volume, broad study coverage and concrete applied services converge. This deserves more attention than allocating inputs equally by organism or manufacturer name. Data IDs: 1, 2, 3, 4, 5, 6, 7, 8. Selected examples are public research proxies. Whole-file structure, integrity and representativeness are not established. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Eurofins human WGS service](https://eurofinsgenomics.eu/en/next-generation-sequencing/ngs-built-for-you/inview-genome/inview-whole-genome-sequencing/) [Novogene FY2025 annual report](https://static.cninfo.com.cn/finalpage/2026-04-15/1225103513.PDF) [NHS commissioned whole-genome service](https://www.england.nhs.uk/nhs-genomic-medicine-service/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Complete Genomics service-provider network](https://www.completegenomics.com/products/sequencing-service-providers/)

## Exome, targeted and reproductive/copy-number sequencing

Exome testing, targeted laboratory services and company maize analytical target capture support targeted-library coverage. Reproductive/CNV services independently establish an applied sequencing use, but their purpose does not establish targeted sampling or a file structure different from WGS. Data IDs: 9, 11, 12. The current inputs cover exome, human circulating-DNA targets and nonhuman population capture. Prenatal/copy-number-specific sampling is not established by application names alone. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Corteva maize application dossier hosted by FSANZ](https://www.foodstandards.govt.nz/sites/default/files/2023-12/FSANZ%20DP51291%20Dossier%20Redacted_Redacted.pdf) [CERTANIA molecular diagnostics/genomics portfolio](https://certania.com/services/molecular-diagnostics-and-genomics) [Natera FY2025 annual report](https://www.sec.gov/Archives/edgar/data/1604821/000110465926047801/ntra-20251231xars.pdf) [Ion Torrent clinical laboratory implementation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10958377/) [Burning Rock FY2025 Form 20-F](https://ir.brbiotech.com/static-files/c8cee243-84ea-4ac3-b94f-3b76dbabdcc4)

## Population genotyping and breeding

Commercial sequencing availability and archive evidence justify a role that ordinary WGS does not describe. Economic importance of breeding alone is insufficient. Data IDs: 10, 12, 13. Ordinary maize genomic resequencing, quinoa RAD and conifer population capture are documented public research examples. Not all genotyping uses sequencing, and no species quota follows. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [DArT industry navigation](https://www.diversityarrays.com/industries/) [DArTseq service](https://www.diversityarrays.com/services/dartseq/) [DArT ecological services](https://www.diversityarrays.com/industries/ecologists-and-biodiversity/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Genus FY2025 annual report](https://www.genusplc.com/media/glah32tg/genus-annual-report-2025.pdf) [PIC genomic data capture](https://cms.genusplc.com/pic-nz/services/data-capture/)

## Reference genomes, pangenomes and non-model assembly

Reference and pangenome uses connect technology to material and research purpose. A public species list or genome economic value cannot prescribe extra files. Data IDs: 5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 20, 21, 22. Human long-read, mouse, wheat Renan, potato short-read, animal and Arabidopsis nuclear-genome roles have selected inputs. Plant HiFi processing is documented; its FASTQ properties remain unpreviewed. Reference-poor non-model assembly and intentional related-species reference testing remain general coverage boundaries. Cyclone whole-file yield and byte equivalence to the associated SRA originals remain unverified. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad identity and platform portfolio](https://www.annoroad.com/en/technology/platform) [Annoroad applied research news navigation](https://www.annoroad.com/) [Solyntus genome sequencing consortium](https://www.plantbreeding.wur.nl/Solyntus/) [Oxford Nanopore FY2025 annual report](https://nanoporetech.com/api/assets/f/196663/x/e6a62a9b49/ont-ar25-interactive-final.pdf) [PacBio FY2025 financial results](https://www.pacb.com/press_releases/pacbio-announces-fourth-quarter-and-full-year-2025-financial-results/)

## Bulk transcript and small-RNA sequencing

Large volume and service breadth support transcript sampling independently of genomic DNA. Small-RNA preparation changes the relevant file/reference question. Data IDs: 23, 24, 25, 26, 27. Bulk and short-RNA libraries have documented source roles and sequence amounts. Whole-file properties remain unverified. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [BGI Americas application navigation](https://bgiamericas.com/applications/) [Macrogen NGS portfolio](https://www.macrogen.com/en/business/research/ngs)

## Long-read transcript sequencing

Genomic long reads do not automatically represent transcript concentration, library-associated tags or full-length transcript preparation. Data IDs: 29. FL-cDNA is supported; direct RNA and PacBio transcript conditions remain unfilled, not inferred from platform alone. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Macrogen NGS portfolio](https://www.macrogen.com/en/business/research/ngs) [Oxford Nanopore FY2025 annual report](https://nanoporetech.com/api/assets/f/196663/x/e6a62a9b49/ont-ar25-interactive-final.pdf) [PacBio FY2025 financial results](https://www.pacb.com/press_releases/pacbio-announces-fourth-quarter-and-full-year-2025-financial-results/)

## Single-cell expression, immune and feature libraries

Archive weight, available services and company research corroborate the tagged-library need without any measured unique quality alphabet. Data IDs: 30, 31, 32, 33. The Smart-seq2 cell supplies documented transcript-wide sampling. Matched CITE ADT, mRNA and HTO components each include all four outputs of their experiment. Actual recovered cells, whole-file pairing and unpreviewed properties remain unknown. Feature/barcode definitions aid interpretation or custom matching, not generic lossless compression. Immune-receptor raw components remain unfilled. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Novartis submitted single-cell multi-omics series GSE292621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292621) [Cell Ranger FASTQ inputs](https://www.10xgenomics.com/support/software/cell-ranger/latest/analysis/inputs/cr-specifying-fastqs)

## Sequencing-based spatial expression

Coordinate/tag structures and documented representations give a clear workload relationship beyond generic bulk RNA. Data IDs: 34. Two Stereo-seq FASTQs are documented and have 35/100-base inspected prefixes. Full-file acquisition, integrity and pairing remain pending. Masks/coordinates are optional for generic lossless read compression but needed for spatial reconstruction or relevant custom matching. A complete Visium alternative remains unfilled; that does not negate the selected Stereo-seq raw-read role. [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [dbGaP phs003751.v1.p1 study metadata](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs003751.v1.p1) [BGI-Research: Research Breakthroughs Attract Global Attention](https://en.genomics.cn/news-6413.html) [MGI acquisition of STOmics and CycloneSEQ](https://mgi-tech.eu/news/mgi-tech-announces-acquisition-of-stomics-and-cycloneseq/) [Stereo-seq SAW format FAQ](https://enfile.stomics.tech/Stereo-seq%20SAW%20FAQ%20version%20A3.pdf) [Xenium output formats](https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/analysis/xoa-output-understanding-outputs) [Stereo-seq SAW computational inputs](https://www.stomics.tech/service/saw_8_1/docs/analysis/pipelines/index.html) [SingularG4X product/service portfolio](https://www.singulargenomics.com/g4x)

## Chromatin, targeted protein-DNA and proximity libraries

Shared short-read length or alphabet does not collapse different genomic sampling/pair relationships. A mixture role is not pure-species coverage. Data IDs: 35, 36, 37, 38, 39. Conventional human paired bulk ATAC, rice histone ChIP, human CUT&RUN, yeast Hi-C and Ultima ATAC have distinct documented preparations. Broad OTHER metadata alone does not establish CUT&RUN. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [Novartis CUT&RUN metadata GSM7883167](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7883167)

## Methylation and transformed-sequence reads

Documented transformation, rather than a species name, motivates the prospective composition/reference contrast. Data IDs: 40. Selected examples are public research proxies. Whole-file structure, integrity and representativeness are not established. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [CERTANIA molecular diagnostics/genomics portfolio](https://certania.com/services/molecular-diagnostics-and-genomics) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/)

## Marker, genomic, viral and forensic target sequencing

Huge run counts justify attention but not proportional input allocation. Pandemic deposits and project concentration must not determine the whole benchmark. Data IDs: 11, 41, 42, 43, 45. Bacterial 16S, fungal ITS, viral targets, human genomic targets and aquatic eDNA have explicit library units. Exact bacterial/fungal subregions remain unspecified. A conventional forensic-panel condition is not established by these inputs. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [NIST forensic reference certification](https://www.nist.gov/publications/make-it-snppy-updates-srm-2391d-pcr-based-dna-profiling-standard) [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [CDC PulseNet current WGS use](https://www.cdc.gov/pulsenet/php/about.html)

## Microbial isolates and industrial microbial genomes

An industrial sequencing link and reference role justify the need; fermentation economic value or resource deposit alone does not. Data IDs: 48, 49, 50. Bacterial/yeast genomic inputs are research proxies, not annual industrial throughput. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [MIRRI-ERIC service catalogue](https://www.mirri.org/services/) [ILRI sequencing platforms](https://www.ilri.org/sequencing-platforms) [Angel Yeast 2023 corporate social responsibility report](https://en.angelyeast.com/upload/files/2024/2023-angel-yeast-csr-report.pdf) [EFSA applicant WGS portal activity](https://www.efsa.europa.eu/en/events/ad-hoc-meeting-stakeholders-wgs-data-submission-efsa-mops-portal) [CDC PulseNet current WGS use](https://www.cdc.gov/pulsenet/php/about.html) [BGI Genomics FY2025 annual report](https://disc.static.szse.cn/disc/disk03/finalpage/2026-04-25/c79b8582-0ce3-4454-a325-c5a8f780bdd8.PDF)

## Shotgun communities and metatranscriptomes

Multiple genomes, uneven sampling and incomplete reference coverage are meaningful prospective conditions; a marker file is not a generic replacement. Data IDs: 51, 52, 53, 54, 55. Gut, soil and food shotgun DNA, a long-read mock community and fermentation-community RNA supply distinct mixture conditions. Mixture composition and reference sets remain unverified. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [BGI Americas application navigation](https://bgiamericas.com/applications/) [Macrogen NGS portfolio](https://www.macrogen.com/en/business/research/ngs) [BGI Genomics FY2025 annual report](https://disc.static.szse.cn/disc/disk03/finalpage/2026-04-25/c79b8582-0ce3-4454-a325-c5a8f780bdd8.PDF) [CNSA statistics and official aggregate endpoints](https://db.cngb.org/cnsa/statistic/)

## Environmental DNA and biodiversity monitoring

Actual sequencing use justifies coverage even without a clean archive label or market denominator; method uncertainty prevents presumed file equivalence, not recognition of the use. Data IDs: 45. The selected Lugano ITD20-A/VENE aquatic marker run serves the documented sample-associated eDNA role. Exact pre-upload stages remain qualified; it is not every environmental monitoring assay or an entire flow-cell. [DArT ecological services](https://www.diversityarrays.com/industries/ecologists-and-biodiversity/) [China environment ministry public account of eDNA monitoring](https://www.mee.gov.cn/ywdt/hjywnews/202603/t20260312_1146462.shtml) [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/)

## Food mixtures and authenticity

Processed multi-eukaryotic food mixtures are a real applied use that neither a pure crop genome nor a gut microbiome automatically represents. Data IDs: 55. Honey shotgun DNA supplies the selected food-mixture input. Ingredient composition and an exact mixture-reference set remain unverified; a targeted processed-food authentication configuration is not specified. [Food Forensics NGS testing](https://www.foodforensics.co.uk/technical-solutions/ngs-testing) [Hebei food institute completed milk-authenticity research](https://scjg.hebei.gov.cn/info/84546) [Thermo Fisher NGS food-species screening](https://www.thermofisher.com/sg/en/home/industrial/food-beverage/food-authenticity-labeling/ngs-food-screening-species-identification.html)

## Biopharma genomic characterization and sequence quality control

Direct NGS/WGS service links establish an industrial data use beyond generic pharma research. Library uncertainty does not erase that confirmed use, but prevents an invented assay specification. Data IDs: 56. The complete CHO genomic assembly library is a public production-cell reference-assembly research input. It does not specify a manufacturing-testing assay; exact cell-line/construct/reference match remains unknown. [GenomeScan genetic characterization](https://genomescan.nl/genetic-characterization/) [HyQure NGS services](https://www.hyqure.com/gmp-ngs-services) [Eurofins biopharma NGS services](https://www.eurofins.com/en/biopharma-services/biopharma-product-testing/services/next-generation-sequencing-ngs/)

# Material and reference choices

Human clinical and research material. Major material for genome-wide, exome/targeted, bulk-transcript and single-cell sequencing, with reproductive/copy-number use explicit and its sampling method checked separately. Data IDs: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 20, 23, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 39. Prenatal/copy-number-specific input remains unfilled; purpose does not establish sampling.

Biomedical research models. Preserve a meaningful model/reference interaction; no file for every model species. Data IDs: 15, 21, 22, 24, 30. Mouse genomic and single-cell expression and Arabidopsis nuclear-genome, HiFi and bulk-RNA model conditions supply different preparation/reference settings. The normalization-reference mixture is not pure fly genomic material.

Livestock, poultry and aquatic animal research. Seek a supported animal population/reference condition, with species tied to the actual use. Data IDs: 14, 18, 19. Public pig, poultry and aquaculture research examples have explicit genome/reference and file roles; they do not establish annual species demand.

Crop genomes and breeding/pangenome material. Choose distinct genomic/reduced-representation/reference roles, not a plant-name checklist. Data IDs: 10, 13, 16, 17. Ordinary SW1611 maize genomic resequencing, the full Renan wheat library, Altus potato PCR-free assembly library and quinoa RAD supply distinct documented preparation/reference roles. This is not a complete crop catalogue.

Forestry, wild and other non-model material. Non-model and reference-poor research can require distinct reference relationships; no compulsory species follows. Data IDs: 12. Spruce ordinary capture adds a conifer reference, but reference-poor/non-model long-genome assembly and intentionally related-species references remain unfilled.

Bacterial isolates and yeast/industrial microbes. Cover compact-reference and microbial eukaryotic genomic roles when a sequencing link is documented. Data IDs: 38, 48, 49, 50. Same-species defaults are proposed; exact isolate/strain and industrial-production identity remain unresolved.

Host-associated and environmental communities. Preserve mixed-reference material and distinguish markers from shotgun/transcript libraries. Data IDs: 41, 42, 51, 52, 53, 54. Bacterial 16S, fungal ITS, community shotgun DNA and fermentation RNA are distinct conditions. Soil DNA does not establish a soil RNA profile.

Aquatic environmental and biodiversity material. Recognize demonstrated sequencing-based monitoring; keep exact assay/form unresolved until documented. Data IDs: 45. ITD20-A/VENE is a sample-associated aquatic marker output from Lugano. Its exact pre-upload stages remain qualified; no whole-flow-cell claim follows.

Processed multi-species food material. Seek a documented food-mixture sequencing role, not one input per ingredient species. Data IDs: 52, 55. Honey shotgun DNA supplies a food-mixture genomic input. Exact ingredient composition and a fixed mixture-reference set remain unverified.

Biopharma production-cell/sequence material. Use a documented public proxy for confirmed genomic/sequence-characterization work when feasible. Data IDs: 56. The named CHO genomic assembly library is a public industrial production-cell research input; exact cell-line/construct/reference match remains unresolved.

# Technology choices and remaining inquiries

Illumina — Short-read SBS systems. 90.22% of stock public runs/89.06% of bases and operating-provider use support broad relevance; model×assay joints prevent treating MiSeq and high-throughput RNA/WGS as identical. Use the coverage judgment, not one file per company. Archive shares are not sales or China dominance; no requirement for every model. Selected Data IDs: 4, 9, 10, 12, 13, 15, 16, 17, 24, 26, 30, 31, 32, 33, 35, 36, 37, 38, 40, 41, 42, 43, 45, 48, 49, 50, 52, 53, 54, 55, 56. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [ILRI sequencing platforms](https://www.ilri.org/sequencing-platforms) [Eurofins human WGS service](https://eurofinsgenomics.eu/en/next-generation-sequencing/ngs-built-for-you/inview-genome/inview-whole-genome-sequencing/)

MGI / Complete Genomics — DNBSEQ/BGISEQ short-read families. DNBSEQ is 4.56% of stock bases and 9.30% of annual-increment bases, with a distinct BGISEQ label. Operating domestic provider and international network corroborate use. Genomic quality conditions, RNA and spatial roles follow documented workload and file evidence, without a model or assay quota. Do not merge raw labels into a market share or infer a sample’s production country. Selected Data IDs: 1, 2, 3, 14, 18, 19, 23, 25, 34. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Complete Genomics service-provider network](https://www.completegenomics.com/products/sequencing-service-providers/) [Annoroad identity and platform portfolio](https://www.annoroad.com/en/technology/platform) [Novogene FY2025 annual report](https://static.cninfo.com.cn/finalpage/2026-04-15/1225103513.PDF) [CNSA statistics and official aggregate endpoints](https://db.cngb.org/cnsa/statistic/)

Oxford Nanopore Technologies — Nanopore long-read systems. Archive breadth and actual operating services support a continuing production family; genomic versus transcript use is a meaningful interaction. Use the coverage judgment, not one file per company. Platform alone does not identify direct RNA, model, chemistry or actual length/quality distribution. Selected Data IDs: 5, 6, 21, 29, 51. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [ILRI sequencing platforms](https://www.ilri.org/sequencing-platforms) [Oxford Nanopore FY2025 annual report](https://nanoporetech.com/api/assets/f/196663/x/e6a62a9b49/ont-ar25-interactive-final.pdf) [Dorado output documentation](https://software-docs.nanoporetech.com/dorado/latest/basecaller/basecall_overview/)

PacBio — SMRT / consensus-HiFi long-read systems. 963,605 stock runs/28,602 studies plus provider operation and instrument business corroborate relevance. Human raw CLR, human HiFi barcode output and documented plant HiFi assembly reads provide separate representations. Manufacturer chemistry labels do not prove new FASTQ properties. Placements are not sequence bytes; one input per new chemistry is not automatic. Selected Data IDs: 7, 20, 22. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Annoroad identity and platform portfolio](https://www.annoroad.com/en/technology/platform) [PacBio FY2025 financial results](https://www.pacb.com/press_releases/pacbio-announces-fourth-quarter-and-full-year-2025-financial-results/) [Solyntus genome sequencing consortium](https://www.plantbreeding.wur.nl/Solyntus/)

Thermo Fisher Scientific — Ion Torrent semiconductor sequencing. Substantial archive run/study history, a deployed targeted clinical service and a specific food-identification offering support real uses. Use the coverage judgment, not one file per company. Service availability and archive history support semiconductor sequencing; the selected human genomic-target library does not represent every commercial assay. Selected Data IDs: 11. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [CERTANIA molecular diagnostics/genomics portfolio](https://certania.com/services/molecular-diagnostics-and-genomics) [Thermo Fisher NGS food-species screening](https://www.thermofisher.com/sg/en/home/industrial/food-beverage/food-authenticity-labeling/ngs-food-screening-species-identification.html) [Ion Torrent clinical laboratory implementation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10958377/)

Ultima Genomics — UG100 short-read family. SeqMatic explicitly reports operating Ultima; smaller public archive and a service network corroborate an emerging production use without requiring measured FASTQ novelty. Use the coverage judgment, not one file per company. No broad market share or separate requirement for every UG model follows. Selected Data IDs: 39. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Ultima certified service providers](https://www.ultimagenomics.com/products/certified-service-providers-old/)

Element Biosciences — AVITI short-read family. Archive 91,978 runs/1,014 studies and manufacturer-reported installations exceed novelty alone; concentration remains visible. Use the coverage judgment, not one file per company. Multiomic outputs are not all FASTQ. Do not equate one large archive project with general adoption. Selected Data IDs: 27. [Global public-read archive stock and annual increment](https://www.ebi.ac.uk/ena/portal/api/) [Element investor presentation](https://www.elementbiosciences.com/hubfs/element_biosciences_2025/pdfs/news_blog_pdf/Element-JPM-2025-Final.pdf)

MGI / CycloneSEQ — CycloneSEQ nanopore systems. Product-specific named installations at Ling-en Bio and Wuhan BGI service sites support a China deployment use independently of sparse/ambiguous archive labels. One CNGB SINGLE FASTQ source, CNR1409093 / CNX1236558, is listed at 130,270,589,600 compressed bytes. No publisher MD5 or exact equivalence to the associated SRA originals is established. Manufacturer-reported deployments do not establish national installed-base share, annual volume or unique measured FASTQ properties. Selected Data IDs: 8. [CycloneSEQ G400-ER first named installations](https://www.mgi-tech.com/mgi-news/945.html) [MGI acquisition of STOmics and CycloneSEQ](https://mgi-tech.eu/news/mgi-tech-announces-acquisition-of-stomics-and-cycloneseq/)

10x Genomics — Not sequencer manufacturers in this role. Operating provider services and research use support tagged single-cell workflows. Library roles are separate from the sequencing instrument. Exact GEO documents 10x Next GEM 3′ v3.0 and separate ADT, mRNA and HTO libraries. Use all four outputs per component. This chemistry context does not certify recovered cells or normalized read orientation. Exact sample 3 cell recovery and unpreviewed-file properties remain unknown. Feature definitions are optional for generic compression and relevant to custom matching. Selected Data IDs: 31, 32, 33. [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [Novartis submitted single-cell multi-omics series GSE292621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292621) [Cell Ranger FASTQ inputs](https://www.10xgenomics.com/support/software/cell-ranger/latest/analysis/inputs/cr-specifying-fastqs)

10x Genomics / STOmics — External compatible sequencer identified for actual library. Provider/research use and official Q4/Q40/input documentation support coordinate/tag and representation questions. The documented raw pair and manuscript support Stereo-seq. Other spatial imaging/coordinate products are not presumed FASTQ. Xenium/G4X image/coordinate outputs alone establish no FASTQ need; masks/features are not replaced by a genomic FASTA. Selected Data IDs: 34. [Annoroad HKEX application-proof business section](https://www.hkexnews.hk/app/sehk/2026/108447/a132011/sehk26041501668.pdf) [SeqMatic service and technology portfolio](https://www.seqmatic.com/services/) [BGI-Research: Research Breakthroughs Attract Global Attention](https://en.genomics.cn/news-6413.html) [Stereo-seq SAW format FAQ](https://enfile.stomics.tech/Stereo-seq%20SAW%20FAQ%20version%20A3.pdf) [Xenium output formats](https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/analysis/xoa-output-understanding-outputs) [Stereo-seq SAW computational inputs](https://www.stomics.tech/service/saw_8_1/docs/analysis/pipelines/index.html) [MGI acquisition of STOmics and CycloneSEQ](https://mgi-tech.eu/news/mgi-tech-announces-acquisition-of-stomics-and-cycloneseq/)

# The selected public inputs

This collection supplies useful examples of common public sequencing workloads and publicly supported applied or research uses. It contains 52 datasets: 51 with listed FASTQ routes and one BAM source requiring later FASTQ conversion. Its 115 physical source objects total 1,419,456,345,104 listed bytes (1.419 decimal TB). Source sizes are not uncompressed FASTQ sizes, market shares or benchmark results. The count follows individual decisions; it is not a quota or proven minimum.

The [workbook](../catalogue/benchmark_dataset.xlsx) has one dataset row per Data ID in fq, every physical object in Files, and versioned reference proposals in fa. Reasons, Coverage, Materials, Technology carry the supporting detail. Sequence amounts below are reported bases, separately from listed compressed-source sizes. The entries identify the intended test inputs and the preparation still needed.

## Why some input units are small

11 of the 52 complete input units have less than one decimal GB of listed compressed source data. This count sums all selected ends, runs and chunks of each dataset. Listed gzip bytes, reported sequence bases and read/spot counts are different measures; the uncompressed FASTQ byte counts have not been measured. One GB is a descriptive boundary, not an inclusion floor.

Small targets, reduced-representation libraries, short RNA, individual cells, sample tags and community markers can produce meaningful small files. A compact bacterial genome can also have substantial sequence coverage within a sub-GB compressed output. Each entry below connects its sample, library or delivered component to relevant source-workflow amounts. For example, the complete eight-file HTO component contains 1,566,671,480 reported bases in 687,740,927 listed compressed bytes. Source-cohort medians provide context, not a pass/fail threshold or universal production norm.

A processed or demultiplexed FASTQ can represent a real research or production workload. Describe its stage where documented; an unknown stage does not prove failure or incompleteness. Source-unit, amount and useful workload evidence support the small inputs here, with remaining uncertainties stated individually. No repetition, padding or forced combination is used to make a small input larger.

## Data 1. Homo sapiens — DNBSEQ-G400

This broad-quality human MGI whole-genome input has an ordinary family-study identity and 122.627 billion reported bases. The saved 150-base prefixes use 41 quality characters. It anchors broad-quality human MGI sequencing beside the more concentrated quality frequencies in Data 2 and the four-symbol representation in Data 3; one input per instrument model is not required.

Public source: [ERR17003126](https://www.ebi.ac.uk/ena/browser/view/ERR17003126). Input unit: one paired archive run.

Reported amount: 122,627,292,300 bases (122.627 billion). Listed source objects: 2; 73,841,588,662 bytes (73.842 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 122.63 billion bases is roughly a 40x human-genome budget. Eleven of 16 matched study records have positive totals; their median is 115.23 billion bases. This fits ordinary human WGS planning, although raw bases are not usable coverage.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 150–150; median 150; File 2: 150–150; median 150. Quality characters: File 1: 41; File 2: 41.

Limits and preparation: Use this as the broad-quality anchor, not an extra G400 quota. Complete-file quality distributions remain unchecked. Check whole files and pairing before testing.

## Data 2. Homo sapiens — DNBSEQ-T7

This human T7 whole-genome run supplies a real quality-frequency contrast at 131.252 billion reported bases. The most common symbol occupies 90.07% of inspected quality positions in R1 and 86.46% in R2. Saved summaries show a more concentrated quality distribution than Data 1. These are nonrandom prefix observations, not measured whole-file redundancy or compressor results; Data 1 remains the broad-quality MGI anchor.

Public source: [ERR16794642](https://www.ebi.ac.uk/ena/browser/view/ERR16794642). Input unit: one paired archive run.

Reported amount: 131,251,843,800 bases (131.252 billion). Listed source objects: 2; 66,737,537,425 bytes (66.738 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 131.25 billion bases is roughly a 42x human-genome budget, within common WGS planning. The source study contains only this run, so it cannot independently establish a population distribution.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 150–150; median 150; File 2: 150–150; median 150. Quality characters: File 1: 40; File 2: 40.

Limits and preparation: Saved prefixes give about 0.90/1.16 bits per quality position versus 1.78/2.04 for Data 1. These are marginal prefix summaries; full-file distributions and correlations remain unchecked. Check whole files and pairing before testing.

## Data 3. Homo sapiens — DNBSEQ-T7

This input supplies the observed four-symbol quality representation. A narrow alphabet is a useful condition beyond the two broad-alphabet examples.

Public source: [SRR33329596](https://www.ebi.ac.uk/ena/browser/view/SRR33329596). Input unit: one paired archive run.

Reported amount: 127,540,227,000 bases (127.540 billion). Listed source objects: 2; 48,041,300,140 bytes (48.041 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 127.54 billion bases lies within the eight-positive-run study range (nine records; one zero total). Its RPE1 ploidy-benchmark source is explicit; this is not described as a normal diploid patient genome.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 150–150; median 150; File 2: 150–150; median 150. Quality characters: File 1: 4; File 2: 4.

Limits and preparation: Do not infer why the qualities have four symbols or use a diploid usable-depth claim for the mixed-ploidy material. Check whole files and pairing before testing.

## Data 4. Homo sapiens — Illumina NovaSeq X Plus

This input supplies mainstream Illumina genomic output at a declared run/lane scale, a natural production delivery unit.

Public source: [ERR15383198](https://www.ebi.ac.uk/ena/browser/view/ERR15383198). Input unit: one paired archive run.

Reported amount: 39,313,093,714 bases (39.313 billion). Listed source objects: 2; 15,853,763,048 bytes (15.854 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 39.31 billion bases is close to the 35.48-billion median of 24 comparable runs in its source study and within the positive-volume NovaSeq X archive interquartile range.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 151–151; median 151; File 2: 151–151; median 151. Quality characters: File 1: 4; File 2: 4.

Limits and preparation: This is a declared run/lane input, not a demonstrated complete 30× human sample. Raw bases do not establish usable sample-level depth. Check whole files and pairing before testing.

## Data 5. Homo sapiens — PromethION

This input supplies the ultra-long genomic representation alongside current ordinary nanopore output and HiFi. The source explicitly belongs to an ultra-long sequencing study.

Public source: [ERR12954382](https://www.ebi.ac.uk/ena/browser/view/ERR12954382). Input unit: one archive run.

Reported amount: 49,183,304,334 bases (49.183 billion). Listed source objects: 1; 40,884,662,813 bytes (40.885 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 49.18 billion bases is close to the median 51.65 billion among 74 positive-yield source-study runs (79 records; five zero totals). This is a credible long-read run/library amount.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 454–501182; median 42100. Quality characters: File 1: 77.

Limits and preparation: The inspected length prefix contains only 456 records. It does not establish the complete read-length tail or an entire multi-run sample. Acquire and verify the complete listed file before testing.

## Data 6. Homo sapiens — PromethION

This input supplies a current R10.4.1/Dorado genomic output condition. The chosen object is a whole named flow-cell BAM, rather than an arbitrary byte slice.

Public source: [PAW70337 SUP flow-cell source](https://ont-open-data.s3.amazonaws.com/giab_2025.01/basecalling/sup/HG002/PAW70337/calls.sorted.bam). Input unit: one named manufacturer flow-cell BAM, pending FASTQ export.

Reported amount: Exact selected-source sequence yield not established. Listed source objects: 1; 171,763,325,052 bytes (171.763 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The release describes about 140 Gb per flow cell. The exact PAW70337 SUP analysis summary reports 153,264,463,825 bases and 8,155,127 reads, all mapped within that analysis. Its scope is distinct from the exact selected BAM/export yield.

Properties: BAM source only; no FASTQ prefix, lengths, headers or quality distribution inspected. Lengths: Not inspected; BAM source. Quality characters: Not inspected.

Limits and preparation: Exact selected BAM/export yield has not been established from the mapped-analysis summary. The declared unpaired-primary/name policy has only synthetic validation; unexpected pairing flags, duplicate primary names, absent SEQ or absent QUAL require review instead of silent omission. Prepared order is not native instrument order. Use the pinned prepare_data6.py rule: SAMtools 1.22/htslib 1.22, name-sort, primary unpaired records, stored QUAL and rejection of missing primary qualities. One plain FASTQ and a receipt with exact source/output SHA-256 and options are produced when run. Real-source preparation has not been executed.

## Data 7. Homo sapiens — Revio

This input supplies the consensus-long-read condition, which differs from raw CLR and nanopore.

Public source: [ERR14732808](https://www.ebi.ac.uk/ena/browser/view/ERR14732808). Input unit: Complete barcode-specific output of named Revio cell/run; not an entire cell or the full three-output sample library.

Reported amount: 48,501,907,479 bases (48.502 billion). Listed source objects: 1; 23,718,059,148 bytes (23.718 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The submitted source identifies a barcode-specific HiFi cell output with 48,501,907,479 reported bases. Three same-sample, same-library outputs total 135,306,939,495 bases; those other outputs are a full-library alternative, not missing parts of the selected barcode output. The documentary submitted filename is m84046_230703_215053_s2.hifi_reads.bc2031.bam. The chosen object remains the separately listed archive FASTQ, not that BAM.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 1947–38788; median 19615. Quality characters: File 1: 7.

Limits and preparation: The selected amount is a barcode-specific cell output, not an entire Revio cell or every library for the individual. Exact sample/reference matching remains unverified. Check whole files and pairing before testing.

## Data 8. Homo sapiens — CycloneSEQ G400-ER (CNGB G400-ER label)

This single-file CNGB source supplies the intended CycloneSEQ nanopore condition. Product-specific deployments and public research support that technology role despite sparse archive labels. The selected object is CNR1409093 in experiment CNX1236558, supplied as one SINGLE FASTQ file. CNGB metadata identifies HG002 genomic WGS on G400-ER; exact byte equivalence to the associated SRA representation has not been verified.

Public source: [CNR1409093 / CNX1236558](https://db.cngb.org/search/run/CNR1409093/). Input unit: One selected CNGB run/source object CNR1409093, WY_reads.fq.gz; single reads, not mates.

Reported amount: Exact selected-source sequence yield not established. Listed source objects: 1; 130,270,589,600 bytes (130.271 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The selected WY_reads.fq.gz object is listed at 130,270,589,600 compressed bytes. CNGB metadata documents release on 4 December 2025; exact whole-file read count and sequence-base yield have not been established. Associated-study quantities are not substituted for this file’s yield; compressed source size is not a production norm or uncompressed FASTQ size.

Unit and processing sources: [CNGB exact run and experiment metadata](https://db.cngb.org/search/experiment/CNX1236558/) [Bounded prefix inspection of selected CNGB object](https://ftp.cngb.org/pub/CNSA/data7/CNP0007646/CNS1382495/CNX1236558/CNR1409093/WY_reads.fq.gz)

Properties: Nonrandom prefix observation: 258 complete records after transferring 1,048,576 compressed bytes; 2,432,831 decompressed FASTQ bytes. Whole-file read/base totals, distributions and integrity remain unverified. Lengths: 355–28,912 bases in 258 complete nonrandom-prefix records. Quality characters: Not recorded.

Limits and preparation: No publisher MD5 is available for this object; verification is size-only against the listed 130,270,589,600 bytes. Size agreement alone does not prove content integrity. The SINGLE representation is not a pair of mates. Cached CNGB metadata identifies human HG002 genomic WGS, RANDOM selection, G400-ER and fragment/single layout. Exact byte equivalence to the SRA originals remains unverified. Prefix header observations do not establish whole-file pairing or integrity. Download the one exact listed CNGB object, record a local SHA-256 after acquisition and preserve its identity. A saved 19 October nonrandom prefix has 258 complete records and no observed four-line format errors; confirm complete integrity and properties before benchmarking. No full-file preparation or validation has been executed here.

## Data 9. Homo sapiens — Illumina NovaSeq 6000

This input supplies mainstream human exome sampling. Keep its actual tumor-study context visible rather than calling it a generic germline sample.

Public source: [ERR12411150](https://www.ebi.ac.uk/ena/browser/view/ERR12411150). Input unit: one paired archive run.

Reported amount: 5,446,687,469 bases (5.447 billion). Listed source objects: 2; 2,415,095,443 bytes (2.415 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The source has 38 FFPE exome runs with median 5.650 billion bases. The selected run has 5.447 billion bases and nominal 72 Mb enrichment. This supports the scoped source workflow, not verified usable tumor depth.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 146–151; median 151; File 2: 146–151; median 151. Quality characters: File 1: 3; File 2: 4.

Limits and preparation: The 72 Mb enrichment target is nominal, not measured on-target sequence. Intended usable tumor depth and the exact lane-to-library allocation remain unverified. Check whole files and pairing before testing.

## Data 10. Zea mays subsp. mays — Illumina NovaSeq 6000

This PCR-free SW1611 maize genomic library supplies ordinary crop population resequencing. Its 47.789 billion reported bases support the complete paired library at the scale of the documented 521-line association panel. The B73 reference is the same species but a different inbred line, giving an explicit reference relationship without claiming exact cultivar matching.

Public source: [SRR8906645](https://www.ebi.ac.uk/ena/browser/view/SRR8906645). Input unit: One complete deposited paired run for SW1611 library L84; both archive FASTQ ends.

Reported amount: 47,789,487,240 bases (47.789 billion). Listed source objects: 2; 24,082,143,756 bytes (24.082 decimal GB). fa ID 10 / GCA_902167145.1.

Size evidence: The primary panel study describes approximately 20× DNA resequencing. Its 513 positive reported library totals have median 47,915,875,698 bases and interquartile range 43,361,613,016–53,576,105,346. Eight zero-valued metadata totals are outside those positive-yield quantiles, not proven zero-yield samples. This input has 47,789,487,240 reported bases. These are source-cohort comparisons, not universal maize production norms.

Unit and processing sources: [Maize association-panel primary study](https://www.nature.com/articles/s41588-019-0427-6) [Exact PCR-free maize experiment](https://www.ebi.ac.uk/ena/browser/view/SRX5692588) [Exact SW1611 maize sample](https://www.ebi.ac.uk/ena/browser/view/SAMN11370298) [Exact maize run quantities and representation](https://www.ncbi.nlm.nih.gov/sra/SRR8906645)

Properties: Unpreviewed; no length, quality or header profile was inspected for these exact files. Whole-file integrity and pairing remain unverified. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The exact experiment states PCR-free genomic WGS. Its submitted alias Q88_1.trimed.fq.gz indicates trimming; the exact pipeline and untouched-instrument equivalence are unverified. NCBI metadata reports mean R1/R2 lengths of 148.43/145.89 bases, not newly inspected distributions or a specified nominal cycle length. Acquire both exact listed archive ends and verify integrity, pairing and prepared-byte order. Publisher MD5 values are listed, not computed. Fix reference version and account for reference bytes consistently.

## Data 11. Homo sapiens — Ion Torrent S5 XL

This input supplies targeted semiconductor output in a human sample, distinct from genome-wide sequencing and food-marker libraries.

Public source: [DRR341924](https://www.ebi.ac.uk/ena/browser/view/DRR341924). Input unit: one archive run.

Reported amount: 1,497,990,828 bases (1.498 billion). Listed source objects: 1; 1,154,396,293 bytes (1.154 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The selected named amplicon run has 1,497,990,828 reported bases. The 133 comparable source-study runs have median 1,644,565,071 bases. Panel-wide usable depth is not established.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The inspected source identifies a cfDNA amplicon run, but does not establish exact panel extent or the relation between supplied and integrated reads. No general panel-depth certification is claimed. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 12. Picea abies — Illumina HiSeq 2000

This spruce input supplies population target capture against a large conifer reference. The selected paired archive run has 335,384,842 reported bases; the proposed same-species assembly contains 11,961,396,284 bases. This small-target/large-reference relationship is a prospective compression condition, not a measured compression or reference-cost result. The named library groups six submitted lane/mate files across three lanes into the two selected archive ends.

Public source: [SRR19440963](https://www.ebi.ac.uk/ena/browser/view/SRR19440963). Input unit: One named capture archive run, selected as two archive FASTQ ends; supporting submission groups three lane pairs.

Reported amount: 335,384,842 bases (335.385 million). Listed source objects: 2; 177,775,032 bytes (177.775 decimal MB). fa ID 15 / GCA_900067695.1.

Size evidence: The 335,384,842-base archive run lies in the lower range of 7,729 project runs with median 584 million bases. The exact record groups L001–L003 lane pairs under UME_081104_P72_WE10. The primary paper reports 40,018 probes and average 15× for an earlier cohort, not this later library.

Unit and processing sources: [Exact spruce capture experiment and submitted objects](https://www.ncbi.nlm.nih.gov/sra/SRX15494349) [Versioned spruce assembly metadata](https://www.ebi.ac.uk/ena/browser/view/GCA_900067695.1)

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The source grouping is metadata evidence, not body-level merge or order verification. Exact normalized representation and library-specific usable target depth remain unverified. Probe count is not a target-base denominator; the earlier cohort’s 15× is not assigned to this run. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 13. Chenopodium quinoa — Illumina HiSeq 2500

This quinoa RAD input supplies reduced-representation crop genotyping. Its 895 million reported bases are close to the 872-million median of 136 matching population-study outputs. The complete paired run is meaningful at that targeted sampling scale; a whole-genome amount would describe a different workload.

Public source: [DRR095727](https://www.ebi.ac.uk/ena/browser/view/DRR095727). Input unit: one paired archive run.

Reported amount: 894,720,418 bases (894.720 million). Listed source objects: 2; 571,962,433 bytes (571.962 decimal MB). fa ID 16 / GCF_001683475.1.

Size evidence: 895 million bases is close to the median 872 million among 136 matching population-study runs.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: Do not assess RAD using whole-genome depth. Exact locus coverage is not established by these raw totals. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 14. Sus scrofa — DNBSEQ-G400

This input supplies livestock genomic material and one supplied constant-quality short-read representation. This one input serves both conditions.

Public source: [SRR24804436](https://www.ebi.ac.uk/ena/browser/view/SRR24804436). Input unit: one paired archive run.

Reported amount: 26,338,729,500 bases (26.339 billion). Listed source objects: 2; 10,018,740,265 bytes (10.019 decimal GB). fa ID 2 / GCA_000003025.6.

Size evidence: 26.34 billion bases is close to the very tight approximately 26.19-billion median of 147 source-study runs.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 150–150; median 150; File 2: 150–150; median 150. Quality characters: File 1: 1; File 2: 1.

Limits and preparation: The original role is an assembly/resequencing study component. The supplied constant qualities must not be advertised as typical native MGI qualities; their processing origin is unknown. Check whole files and pairing before testing.

## Data 15. Mus musculus — Illumina NovaSeq 6000

This is an explicitly identified mouse germline-tail whole-genome library, with 100.892 billion reported bases in a complete paired run. Five similarly prepared tail libraries contain 100.892–139.281 billion bases. It is the lower-yield member of that group, not an artificial subset; the source-workflow evidence supports its amount without establishing a universal mouse-production norm. Strain/reference identity remains qualified.

Public source: [ERR14032264](https://www.ebi.ac.uk/ena/browser/view/ERR14032264). Input unit: One complete paired germline-tail whole-genome run.

Reported amount: 100,892,053,998 bases (100.892 billion). Listed source objects: 2; 48,335,307,261 bytes (48.335 decimal GB). fa ID 3 / GCF_000001635.24.

Size evidence: Five like-prepared germline-tail outputs contain 100.892–139.281 billion bases, with median 118.131 billion. This complete 100.892-billion-base run is the lower-yield member. Much deeper colony libraries are not used as a homogeneous comparator.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The exact sample is Mus musculus, but its strain is not stated. The proposed mouse reference is a same-species proposal; no sequence match is verified. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 16. Triticum aestivum — Illumina NovaSeq 6000

This Renan wheat genomic library supplies the large/polyploid nuclear-genome assembly context. Its three paired run outputs belong to one named preparation used for assembly polishing and together contain 495.517 billion reported bases. Include all six files, keeping run boundaries. The chosen unit follows the documented library, not a numerical depth threshold or a preference for fewer bytes.

Public source: [ERR6348210](https://www.ebi.ac.uk/ena/browser/view/ERR6348210), [ERR6348211](https://www.ebi.ac.uk/ena/browser/view/ERR6348211), [ERR6348212](https://www.ebi.ac.uk/ena/browser/view/ERR6348212). Input unit: One named Renan genomic library: three complete paired runs and six separate files.

Reported amount: 495,517,462,387 bases (495.517 billion). Listed source objects: 6; 243,946,029,653 bytes (243.946 decimal GB). fa ID 18 / GCA_937894285.1.

Size evidence: The three outputs share the same sample and named preparation. Their 495,517,462,387 reported bases are the documented assembly-polishing library amount, not a sum engineered to reach 30× or an average production claim.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The three outputs define the named Renan library, not a universal wheat production norm. The same-cultivar reference identity is proposed at metadata level; FASTA contents and matching remain unverified. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 17. Solanum tuberosum — Illumina HiSeq 2500

This Altus potato PCR-free library supplies a tetraploid crop genome-assembly input and the observed longer short-read representation. Its 70.557 billion reported bases belong to one named 470 bp-insert library. This is a documented material/reference and preparation setting; 470 bp describes the insert, not read length or per-copy depth.

Public source: [SRR14993639](https://www.ebi.ac.uk/ena/browser/view/SRR14993639). Input unit: Complete named potato_Altus_PR_2_470bp paired run/library.

Reported amount: 70,556,516,868 bases (70.557 billion). Listed source objects: 2; 52,291,517,076 bytes (52.292 decimal GB). fa ID 6 / GCA_000226075.1.

Size evidence: Three same-sample libraries with 470 bp inserts contain 68.017,70.557 and 70.976 billion bases. Different 800 bp, mate-pair and linked-read preparations are separate libraries, not missing components of this input.

Unit and processing sources: [Altus potato genome-assembly project](https://www.ebi.ac.uk/ena/browser/view/PRJNA718240)

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 59–265; median 265; File 2: 59–265; median 265. Quality characters: File 1: 28; File 2: 31.

Limits and preparation: This is one named PCR-free library, not the entire cultivar assembly dataset. The 470 bp figure is insert size, not read length or verified per-copy depth. Check whole files and pairing before testing.

## Data 18. Penaeus vannamei — DNBSEQ-T7

This input supplies the aquaculture/invertebrate genomic material supported by the applied breeding-use survey.

Public source: [DRR1000971](https://www.ebi.ac.uk/ena/browser/view/DRR1000971). Input unit: one paired archive run.

Reported amount: 26,760,937,872 bases (26.761 billion). Listed source objects: 2; 18,466,075,422 bytes (18.466 decimal GB). fa ID 11 / GCF_042767895.1.

Size evidence: 26.76 billion bases is close to the 26.96-billion median among ten matched inbreeding-study runs. It is about 15 times the reference length in raw bases against the cited shrimp assembly.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 35–150; median 150; File 2: 35–150; median 150. Quality characters: File 1: 39; File 2: 39.

Limits and preparation: Raw reference-size ratios are not mapped coverage. The precise whole-sample allocation remains a later preparation check. Check complete files, pairing and sample/reference matching before testing.

## Data 19. Gallus gallus — DNBSEQ-T7

This input supplies poultry genomic material. It has an independent applied-use basis and a selected input drawn from a substantial actual animal cohort.

Public source: [ERR13943038](https://www.ebi.ac.uk/ena/browser/view/ERR13943038). Input unit: one paired archive run.

Reported amount: 19,596,096,600 bases (19.596 billion). Listed source objects: 2; 14,336,554,441 bytes (14.337 decimal GB). fa ID 12 / GCA_016699485.1.

Size evidence: 19.60 billion bases lies within the 13.90–20.80-billion P10–P90 range of the 1,004-layer study.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 150–150; median 150; File 2: 150–150; median 150. Quality characters: File 1: 34; File 2: 35.

Limits and preparation: One applied cohort supports the selected example; it is not a national or global poultry production distribution. Check complete files, pairing and sample/reference matching before testing.

## Data 20. Homo sapiens — Sequel

This input supplies raw CLR genomic reads alongside the separate consensus-long-read condition. The exact HG002-CLR library identity establishes its processing role; constant supplied qualities and archive representation remain qualified.

Public source: [SRR8801873](https://www.ebi.ac.uk/ena/browser/view/SRR8801873). Input unit: one archive run.

Reported amount: 113,896,753,645 bases (113.897 billion). Listed source objects: 1; 34,654,458,158 bytes (34.654 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 113.90 billion reported raw bases is a substantial genomic input. Its study contains only this matching record, so there is no independent within-study size distribution.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 51–87913; median 13433. Quality characters: File 1: 1.

Limits and preparation: Raw pass yield must not be compared directly with HiFi consensus yield or usable coverage. Constant supplied qualities and their archive representation remain explicit. Check whole files and pairing before testing.

## Data 21. Arabidopsis thaliana — GridION

This Col-0 Arabidopsis source explicitly documents a plant nuclear-genome nanopore assembly experiment. The chosen 10.555-billion-base input is the complete submitted ATRun2_SA_pass output of one named run. Alternative basecalls of the same experiment are alternative representations, not additional independent sequence.

Public source: [ERR13669551](https://www.ebi.ac.uk/ena/browser/view/ERR13669551). Input unit: Complete supplied ATRun2_SA_pass readset from one named run.

Reported amount: 10,554,533,391 bases (10.555 billion). Listed source objects: 1; 9,919,475,722 bytes (9.919 decimal GB). fa ID 9 / GCF_000001735.4.

Size evidence: The chosen pass output contains 10,554,533,391 reported bases. Its same-run fail output adds 2,223,574,952 bases, while other basecalls are alternatives. The primary source documents a plant nuclear-genome assembly experiment, not an organelle-only role.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The chosen PASS output excludes fail reads. Exact basecaller settings are not established, and no whole-flow-cell or whole-file property claim is made. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 22. Arabidopsis thaliana — Sequel II

This Arabidopsis Col-0 input supplies documented plant HiFi consensus reads for a nuclear assembly. The author-listed accession, AT_HiFi library and 22.90-billion-base published quantity agree with the archive total 22,904,700,074 bases. That documentary join supports its processing identity; the generic archive filename containing _subreads proves neither consensus nor raw-subread processing by itself. Its actual FASTQ quality alphabet and headers remain unexamined.

Public source: [SRR14728885](https://www.ebi.ac.uk/ena/browser/view/SRR14728885). Input unit: Complete deposited AT_HiFi plant nuclear-assembly readset.

Reported amount: 22,904,700,074 bases (22.905 billion). Listed source objects: 1; 18,526,201,575 bytes (18.526 decimal GB). fa ID 9 / GCF_000001735.4.

Size evidence: The published plant HiFi readset contains 22.90 billion bases; exact archive metadata reports 22,904,700,074 bases for AT_HiFi. The accession, library and quantity agree without a new body inspection.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: Documentary HiFi identity does not establish a particular quality alphabet or whole-file accuracy. The archive filename alone is not processing proof; no new prefix was examined. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 23. Homo sapiens — DNBSEQ-G400

This input supplies ordinary MGI transcript sequencing as an important library/technology condition.

Public source: [ERR10030615](https://www.ebi.ac.uk/ena/browser/view/ERR10030615). Input unit: one paired archive run.

Reported amount: 4,828,141,800 bases (4.828 billion). Listed source objects: 2; 3,817,894,154 bytes (3.818 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 4.83 billion bases is near the 4.81-billion median of eight source-study runs and is a plausible ordinary expression-library amount.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 100–100; median 100; File 2: 100–100; median 100. Quality characters: File 1: 38; File 2: 38.

Limits and preparation: Do not compare archive raw read counts directly with an aligned-read standard without resolving the count convention. Check whole files and pairing before testing.

## Data 24. Arabidopsis thaliana — Illumina NovaSeq 6000

This named wild-type Col-0 plant expression replicate supplies an ordinary bulk-RNA library with 7.103 billion reported bases. Fourteen source-study RNA outputs span 5.214–8.809 billion bases, with median 6.467 billion. The clear sample/preparation unit and source-workflow amount support this example; they are not a market-wide RNA production norm.

Public source: [SRR14627767](https://www.ebi.ac.uk/ena/browser/view/SRR14627767). Input unit: One complete paired wild-type expression replicate.

Reported amount: 7,102,948,500 bases (7.103 billion). Listed source objects: 2; 3,632,286,064 bytes (3.632 decimal GB). fa ID 9 / GCF_000001735.4.

Size evidence: Fourteen RNA outputs in the source study span 5.214–8.809 billion bases, with median 6.467 billion. The selected 7.103-billion-base input is a named wild-type expression replicate.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The source describes trimming for analysis; that does not prove the deposited FASTQ was trimmed or untouched. The proposed genomic reference needs an appropriate annotation only for modes that use it. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 25. Homo sapiens — DNBSEQ-G400

This named small-RNA biological replicate supplies the observed variable 18–44-base prefix representation. Its 12.64 million reported single reads and 284 million bases fit the eight-run source workflow. Biological selection of short RNA supports this small-library role; it does not identify the computational trimming stage of the deposited file.

Public source: [DRR1089360](https://www.ebi.ac.uk/ena/browser/view/DRR1089360). Input unit: one archive run.

Reported amount: 284,297,641 bases (284.298 million). Listed source objects: 1; 291,749,840 bytes (291.750 decimal MB). fa ID 1 / GCF_000001405.39.

Size evidence: 12.64 million reported single reads and 284 million bases match the eight-run study, whose base median is 286 million. Official small-RNA guidance varies by workflow; this is a credible research-library amount.

Unit and processing sources: [Exact named small-RNA replicate](https://www.ncbi.nlm.nih.gov/sra/DRX1064881)

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 18–44; median 22. Quality characters: File 1: 40.

Limits and preparation: The exact archive description identifies a size-selected short-RNA library, but does not establish computational trimming before deposition. Saved prefix lengths are not whole-file distributions. No universal read-count threshold or untouched-instrument-output requirement is applied. Check whole files and pairing before testing.

## Data 26. Homo sapiens — Illumina NovaSeq 6000

This input supplies a mainstream Illumina expression library.

Public source: [DRR1069746](https://www.ebi.ac.uk/ena/browser/view/DRR1069746). Input unit: one paired archive run.

Reported amount: 4,002,783,900 bases (4.003 billion). Listed source objects: 2; 1,795,309,208 bytes (1.795 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 4.00 billion bases is close to the 4.11-billion median of 12 matching study runs and within the wider positive-volume NovaSeq RNA range.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The broad RNA archive includes several library designs. Its raw volume supports plausibility, not compliance with a processed/aligned-read standard. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 27. Homo sapiens — Element AVITI

This input supplies a deployed short-read technology in its documented single-end RNA configuration. Do not force paired-end RNA expectations onto it.

Public source: [SRR30608496](https://www.ebi.ac.uk/ena/browser/view/SRR30608496). Input unit: one archive run.

Reported amount: 3,095,516,700 bases (3.096 billion). Listed source objects: 1; 2,301,820,230 bytes (2.302 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 3.10 billion bases is close to the 2.98-billion median of 18 source-study runs and within the wider AVITI single-end RNA range across 20 known studies.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This supports a public research input. Chemistry-specific quality distributions are still unexamined. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 29. Homo sapiens — PromethION

This input supplies nanopore transcript-derived reads separately from long genomic reads. The short raw mean does not invalidate the submitted full-length-library label.

Public source: [SRR36288068](https://www.ebi.ac.uk/ena/browser/view/SRR36288068). Input unit: one barcoded transcript library/run.

Reported amount: 2,480,166,369 bases (2.480 billion). Listed source objects: 1; 2,307,675,498 bytes (2.308 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The source paper reports 310.8 million raw reads across 72 libraries, an arithmetic average of 4.32 million. This input has 3.98 million reads and 2.48 billion bases.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This is same-study scale support, not a general long-RNA production norm. It is not direct RNA, and raw mean length is not comparable with the paper’s filtered/aligned mean. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 30. Mus musculus — Illumina NovaSeq 6000

This documented Smart-seq2 mouse cell supplies transcript-wide individual-cell sampling alongside the 3-prime CITE libraries. The exact cell is E20.D042253.3_9_M.1.1 from bladder tissue. One complete listed SRA run contains both paired ends and 220.101 million reported bases, within the matched annotated-cell cohort’s middle half. Transcript-wide sampling does not mean each short read spans a whole transcript.

Public source: [SRR6520293](https://www.ebi.ac.uk/ena/browser/view/SRR6520293). Input unit: One author-annotated Smart-seq2 cell library in one SRA run; both paired archive FASTQ ends.

Reported amount: 220,101,000 bases (220.101 million). Listed source objects: 2; 97,956,122 bytes (97.956 decimal MB). fa ID 3 / GCF_000001635.24.

Size evidence: Among 660 author-annotated bladder cells with one listed run each, reported amounts have median 182,126,200 bases and interquartile range 139,362,300–226,050,350. This cell has 220,101,000 bases, in the upper portion of that central range. Eight additional deposited one-run groups do not join the authors’ annotation and are outside this denominator. The comparison supports this natural individual-cell amount, not a general service or worldwide production norm.

Unit and processing sources: [Primary transcript-wide single-cell atlas](https://www.nature.com/articles/s41586-018-0590-4) [Exact bladder Smart-seq2 method and experiment](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2967045) [Official single-cell run and original-file mapping](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE109nnn/GSE109774/suppl/GSE109774_list_of_SRR_accessions_and_raw_filenames.txt.gz) [Author bladder single-cell annotations](https://raw.githubusercontent.com/czbiohub-sf/tabula-muris/master/00_data_ingest/03_tissue_annotation_csv/Bladder_facs_annotation.csv) [Exact Smart-seq2 experiment run quantities](https://www.ebi.ac.uk/ena/browser/view/SRX3607041) [Exact selected Smart-seq2 run](https://www.ebi.ac.uk/ena/browser/view/SRR6520293)

Properties: Unpreviewed; no length, quality or header profile was inspected for these exact files. Whole-file integrity and pairing remain unverified. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The full official filename manifest lists one run and two original FASTQ names for this exact well/plate/donor identity. Source label C1 is undefined; no additional part is listed. Completeness is at the deposited-FASTQ boundary, not all instrument/index, aligned-BAM or count-matrix assets. The author annotation does not certify the exact pre-upload processing stage. Archive descriptors specify nominal 100/100-base application reads; actual file properties remain unpreviewed. Acquire both listed archive ends and verify integrity and pairing. Keep the exact chosen FASTQ representation and order. Same-species GRCm38.p4 is proposed; exact donor substrain, transcript/patch equivalence and the study’s auxiliary ERCC version remain unverified. Such interpretation assets are not required for generic lossless FASTQ compression.

## Data 31. Homo sapiens — Illumina NovaSeq 6000

The antibody-derived tag library supplies the feature component of a matched CITE assay. It complements the mRNA and sample-hashtag libraries rather than duplicating them. Include all four run outputs of this same component experiment: 28.796 billion reported bases in eight files. This defines the complete supplied component-library input, not every capture well or all cells in the study.

Public source: [SRR19066657](https://www.ebi.ac.uk/ena/browser/view/SRR19066657), [SRR19066658](https://www.ebi.ac.uk/ena/browser/view/SRR19066658), [SRR19066659](https://www.ebi.ac.uk/ena/browser/view/SRR19066659), [SRR19066661](https://www.ebi.ac.uk/ena/browser/view/SRR19066661). Input unit: Complete ADT library/component: 4 paired runs, 8 separate files.

Reported amount: 28,795,741,128 bases (28.796 billion). Listed source objects: 8; 11,700,505,268 bytes (11.701 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: All four public outputs of this ADT component experiment sum to 28,795,741,128 reported bases. The common source documents chemistry and recovery targets, not observed selected-cell counts.

Properties: Saved nonrandom prefix observations apply only to 2 exact original objects of 8; other objects are unpreviewed. No whole-library profile is claimed. Lengths: Observations cover only the two exact files identified in Files. Quality characters: Observations cover only the two exact files identified in Files.

Limits and preparation: Recovery targets are not observed recovered cells. The five capture lanes are distinct from the four sequencing-run outputs, and all target cells cannot be assigned to this component. Prefix observations cover only the two exact files identified in Files. Keep all listed run outputs and both ends separate. Validate full-file integrity and pairing before compression. No files were acquired or concatenated.

## Data 32. Homo sapiens — Illumina NovaSeq 6000

The biological-transcript library supplies the mRNA component of the matched CITE assay; antibody and sample tags cannot replace it. Include all four outputs of this component experiment: 73.686 billion reported bases in eight files. Keep its files separate from the ADT and HTO components and do not infer observed cell recovery from loading targets.

Public source: [SRR19066662](https://www.ebi.ac.uk/ena/browser/view/SRR19066662), [SRR19066664](https://www.ebi.ac.uk/ena/browser/view/SRR19066664), [SRR19066665](https://www.ebi.ac.uk/ena/browser/view/SRR19066665), [SRR19066666](https://www.ebi.ac.uk/ena/browser/view/SRR19066666). Input unit: Complete mRNA library/component: 4 paired runs, 8 separate files.

Reported amount: 73,686,380,444 bases (73.686 billion). Listed source objects: 8; 38,755,683,391 bytes (38.756 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: All four public outputs of this mRNA component experiment sum to73,686,380,444 reported bases. The whole component is used rather than one arbitrary run fraction.

Properties: No inspected properties are recorded for any listed object. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The source sequencing target is not observed per-cell depth. Actual recovered cells and normalized read orientation remain unverified; all listed files are unpreviewed. Keep all listed run outputs and both ends separate. Validate full-file integrity and pairing before compression. No files were acquired or concatenated.

## Data 33. Homo sapiens — Illumina NovaSeq 6000

This hashtag library supplies the complementary sample-tag sequences of the matched CITE assay. Include all four outputs of the same component experiment: 1.567 billion reported bases in eight files. Genomic FASTA does not define these tag sequences; custom feature definitions are relevant to interpretation or feature-aware matching, not a prerequisite for generic lossless FASTQ compression.

Public source: [SRR19066668](https://www.ebi.ac.uk/ena/browser/view/SRR19066668), [SRR19066669](https://www.ebi.ac.uk/ena/browser/view/SRR19066669), [SRR19066671](https://www.ebi.ac.uk/ena/browser/view/SRR19066671), [SRR19066672](https://www.ebi.ac.uk/ena/browser/view/SRR19066672). Input unit: Complete HTO library/component: 4 paired runs, 8 separate files.

Reported amount: 1,566,671,480 bases (1.567 billion). Listed source objects: 8; 687,740,927 bytes (687.741 decimal MB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: All four outputs of this HTO component experiment sum to 1,566,671,480 reported bases in eight files, totalling 687,740,927 listed compressed bytes. This is the complete named tag component, separate from ADT and mRNA; its compressed size is not a per-cell sequence-depth measure.

Properties: No inspected properties are recorded for any listed object. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: Actual cell recovery and tag-reference definitions remain unresolved. Custom feature definitions aid interpretation or feature-aware matching; they are not required for generic lossless compression. Keep all listed run outputs and both ends separate. Validate full-file integrity and pairing before compression. No files were acquired or concatenated.

## Data 34. Homo sapiens — DNBSEQ-T7

This input supplies the spatial barcode/transcript condition, including its asymmetric reads. Large size is appropriate when it reflects the real input unit.

Public source: [SRR29351083](https://www.ebi.ac.uk/ena/browser/view/SRR29351083). Input unit: one spatial-transcript archive run.

Reported amount: 248,408,655,120 bases (248.409 billion). Listed source objects: 2; 181,786,356,695 bytes (181.786 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: The named L01 spatial run contains 248,408,655,120 reported bases. The source-study metadata has three positive totals among twelve records, with the selected amount near their middle. That limited comparison is not a general spatial-production norm.

Properties: Observed nonrandom prefix only; nonrandom prefix only, no whole-file/pair/integrity inference. Lengths: File1: 100–100; median 100.0; File2: 35–35; median 35.0. Quality characters: File1: 34; File2: 35.

Limits and preparation: Capture area and observed cell/bin depths remain unknown. Only three of twelve source-study metadata totals are positive, limiting the amount comparison. Masks and coordinates are interpretation assets, not prerequisites for compression of the supplied reads. Acquire and check the two listed FASTQs; whole-file pairing/integrity remain pending. Spatial masks/coordinates are not required for generic lossless compression, but are needed for reconstruction or relevant custom matching.

## Data 35. Homo sapiens — Illumina NovaSeq 6000

This human K562 library supplies a documented conventional paired bulk-ATAC replicate with 9.955 billion reported bases. Its 32-run source group has median 10.146 billion bases. The source documents its conventional bulk-ATAC preparation; raw amount does not establish usable unique fragments.

Public source: [SRR30495077](https://www.ebi.ac.uk/ena/browser/view/SRR30495077). Input unit: One complete paired bulk ATAC biological replicate.

Reported amount: 9,954,897,900 bases (9.955 billion). Listed source objects: 2; 4,218,603,299 bytes (4.219 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: Thirty-two positive ATAC source runs span 6.612–19.462 billion bases, with median 10.146 billion. The selected 9.955-billion-base run is a documented bulk replicate.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The source establishes a bulk ATAC library, not usable unique-fragment counts or an analysis-pipeline pass. The human reference does not prove K562-specific sequence matching. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 36. Oryza sativa — Illumina NovaSeq 6000

This input supplies protein-associated chromatin sampling, distinct from ATAC and CUT&RUN.

Public source: [DRR1000045](https://www.ebi.ac.uk/ena/browser/view/DRR1000045). Input unit: one paired archive run.

Reported amount: 7,848,285,900 bases (7.848 billion). Listed source objects: 2; 3,388,187,408 bytes (3.388 decimal GB). fa ID 8 / GCA_014636035.1.

Size evidence: 7.85 billion bases is close to its 11-run study median of 7.98 billion and within the wider rice ChIP P10–P90 range of 3.36–10.57 billion.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: Raw pairs do not establish aligned, unique or target-specific fragment yield. Whole-file acquisition/integrity and component/representation checks pending; see individual limits.

## Data 37. Homo sapiens — Illumina NovaSeq 6000

This input supplies the preparation established by the exact experiment despite the archive’s broad OTHER label.

Public source: [SRR26362943](https://www.ebi.ac.uk/ena/browser/view/SRR26362943). Input unit: one paired archive run.

Reported amount: 2,142,233,300 bases (2.142 billion). Listed source objects: 2; 1,123,492,148 bytes (1.123 decimal GB). fa ID 1 / GCF_000001405.39; fa ID 13 / GCF_000001215.4.

Size evidence: 2.14 billion bases lies inside the matched 30-run study’s P10–P90 range of 1.79–5.13 billion.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: Normalization-reference composition and processed/usable depth remain unknown. Do not treat this raw total as a pipeline acceptance result. Whole-file acquisition/integrity and component/representation checks pending; see individual limits.

## Data 38. Saccharomyces cerevisiae — Illumina NovaSeq 6000

This input supplies proximity-ligation reads and a compact eukaryotic reference context.

Public source: [SRR30894055](https://www.ebi.ac.uk/ena/browser/view/SRR30894055). Input unit: one paired archive run.

Reported amount: 15,039,534,000 bases (15.040 billion). Listed source objects: 2; 7,074,255,254 bytes (7.074 decimal GB). fa ID 7 / GCF_000146045.2.

Size evidence: 15.04 billion bases is within both its 56-run study range and the wider yeast Hi-C P10–P90 range of 1.78–26.40 billion.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This supports a yeast research run, not a universal Hi-C target. Valid contacts and intended spatial resolution remain separate from raw volume. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 39. Homo sapiens — UG 100

This input supplies a supported deployed/research technology with variable-length single-read output and an actual accessibility assay.

Public source: [SRR34546226](https://www.ebi.ac.uk/ena/browser/view/SRR34546226). Input unit: one archive run.

Reported amount: 9,613,662,904 bases (9.614 billion). Listed source objects: 1; 3,749,797,716 bytes (3.750 decimal GB). fa ID 1 / GCF_000001405.39.

Size evidence: 9.61 billion bases lies within the 248-run study’s P10–P90 range of 3.93–11.02 billion.

Properties: Observed nonrandom prefix only; nonrandom prefix only, no whole-file/pair/integrity inference. Lengths: File1: 47–323; median 163.0. Quality characters: File1: 11.

Limits and preparation: Do not apply Illumina paired-read or pipeline-pass rules directly. Raw total and the saved prefix do not establish whole-file properties. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 40. Oryza sativa — Illumina HiSeq 4000

This input supplies a transformed-sequence genomic library. Ordinary capture or WGS does not provide this condition.

Public source: [DRR1009870](https://www.ebi.ac.uk/ena/browser/view/DRR1009870). Input unit: one paired archive run.

Reported amount: 19,651,497,831 bases (19.651 billion). Listed source objects: 2; 9,477,168,274 bytes (9.477 decimal GB). fa ID 8 / GCA_014636035.1.

Size evidence: 19.65 billion bases is close to its six-run study and within the wider rice bisulfite P10–P90 range of 7.77–22.60 billion.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: No claim of mapped cytosine coverage, conversion efficiency or compression benefit follows from raw totals. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 41. Rhizosphere-soil fungal community — Illumina MiSeq

This named rhizosphere-soil library supplies fungal ITS marker sequencing with both submitted FASTQ ends. The exact library is FL_fungi_1, BioSample SAMN43469068. Its 42.964 million reported bases fit twelve ITS-matched libraries with median 42.678 million. This is a natural named marker-library output; it need not represent a whole sequencing pool.

Public source: [SRR30515680](https://www.ebi.ac.uk/ena/browser/view/SRR30515680). Input unit: One complete paired fungal ITS library.

Reported amount: 42,963,536 bases (42.964 million). Listed source objects: 2; 19,328,691 bytes (19.329 decimal MB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: Twelve target-matched ITS libraries span 38.014–44.784 million bases, with median 42.678 million. The selected amount is 42,963,536 bases; the twelve bacterial 16S outputs are excluded from this comparator.

Unit and processing sources: [Exact fungal ITS library and submitted pair](https://www.ncbi.nlm.nih.gov/sra/SRX25939332)

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The exact ITS subregion and pre-upload trimming/filtering stage remain unspecified. Submitted Original status identifies source objects, not untouched instrument reads. A processed but meaningful FASTQ remains eligible; a single tomato or fungal genome would not define this community reference. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 42. Rhizosphere-soil bacterial community — Illumina MiSeq

This named bacterial-community 16S library supplies both submitted FASTQ ends. The exact library is SH_bacteria_1, BioSample SAMN43469053. Its 32.742 million reported bases are close to the twelve target-matched outputs’ median of 32.662 million. It supplies a bacterial marker workload separately from fungal ITS, at a documented per-library boundary.

Public source: [SRR30515673](https://www.ebi.ac.uk/ena/browser/view/SRR30515673). Input unit: One complete paired bacterial 16S library.

Reported amount: 32,742,178 bases (32.742 million). Listed source objects: 2; 17,916,463 bytes (17.916 decimal MB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: Twelve target-matched bacterial 16S libraries span 21.537–42.351 million bases, with median 32.662 million. The selected named library has 32,742,178 reported bases and two listed ends.

Unit and processing sources: [Exact bacterial 16S library and submitted pair](https://www.ncbi.nlm.nih.gov/sra/SRX25939339)

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The exact 16S subregion and pre-upload processing stage remain unspecified. Neither merging nor untouched raw output is inferred from the file metadata; no single-genome community reference is assumed. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 43. Severe acute respiratory syndrome coronavirus 2 — NextSeq 1000

This specimen-scale viral-amplicon run supplies a small-genome target-sequencing condition. Its 67.83 million reported bases fit 58 comparable specimen outputs, near their 73.35-million median. A human whole-genome delivery amount would be inappropriate for this targeted viral input.

Public source: [DRR1051020](https://www.ebi.ac.uk/ena/browser/view/DRR1051020). Input unit: one paired archive run.

Reported amount: 67,831,999 bases (67.832 million). Listed source objects: 2; 31,561,554 bytes (31.562 decimal MB). fa ID 14 / NC_045512.2.

Size evidence: 67.83 million bases is near the 73.35-million median among 58 comparable specimen runs, inside their P10–P90 range.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This is a plausible specimen-scale targeted input. Target scheme, breadth and usable depth have not been checked. Whole-file acquisition/integrity and component/representation checks pending; see individual limits.

## Data 45. freshwater metagenome — Illumina MiSeq

This short-read aquatic marker input is associated with filter ITD20, extraction A and marker set VENE in Lugano. It supplies both archive read ends and 22,955,020 reported bases from a sample-associated research output. Its target/reference relationship differs from isolate genomes and microbial shotgun data.

Public source: [ERR7749063](https://www.ebi.ac.uk/ena/browser/view/ERR7749063). Input unit: ITD20-A / VENE sample-associated marker output; one paired archive run, two FASTQ ends.

Reported amount: 22,955,020 bases (22.955 million). Listed source objects: 2; 6,829,143 bytes (6.829 decimal MB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: Exact metadata lists the ITD20-A/VENE library, both submitted sample/marker-associated FASTQs and the two chosen archive ends. The study’s supplementary sample table maps ITD20 to a Lugano water filter. This supports the per-marker archive unit, not an entire flow-cell or a universal eDNA delivery amount.

Unit and processing sources: [Exact short-read aquatic marker archive unit](https://www.ebi.ac.uk/ena/browser/view/ERR7749063) [Official aquatic sample/site table and naming descriptions](https://www.ebi.ac.uk/biostudies/studies/S-BSST391) [Author workflow manifest and sample sheet](https://github.com/envmetagen/mussels_package)

Properties: Observed nonrandom prefix only; nonrandom prefix only, no whole-file/pair/integrity inference. Lengths: File1: 151–151; median 151.0. Quality characters: File1: 27.

Limits and preparation: The precise upstream demultiplexing and filtering boundary remains unresolved. The author workflow manifest/sample sheet describes an older 2019 run set and does not list the selected accessions; it cannot establish these files’ exact deposited stage. Full-file integrity and pairing remain unverified. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 48. Mycobacterium tuberculosis — NextSeq 2000

This bacterial-isolate input supplies a compact-reference context beyond the named E. coli strain and includes an observed trimmed-read representation. Its 833 million reported bases are approximately 189 reference lengths in raw sequence, modestly above the matched 350-run study’s upper decile. Sub-GB compressed size is compatible with that substantial isolate amount.

Public source: [ERR11252400](https://www.ebi.ac.uk/ena/browser/view/ERR11252400). Input unit: one paired archive run.

Reported amount: 833,183,051 bases (833.183 million). Listed source objects: 2; 549,265,430 bytes (549.265 decimal MB). fa ID 5 / GCF_000195955.2.

Size evidence: 833 million bases is about 189 times the reference length in raw bases. It is somewhat above the matched 350-run study’s upper decile of 790 million, rather than orders of magnitude away.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 35–151; median 151; File 2: 35–151; median 151. Quality characters: File 1: 6; File 2: 6.

Limits and preparation: Raw volume is not usable coverage. Exact sample-strain/reference agreement remains unverified. Check whole files and pairing before testing.

## Data 49. Escherichia coli str. K-12 substr. MG1655 — Illumina MiSeq

The explicitly named E. coli MG1655 strain supplies a compact bacterial-reference and classic isolate-library condition. Its 450-million-base paired run is close to the broader E. coli comparator median of 435 million and its eight-run study median of 428 million, approximately 97 reference lengths in raw sequence. Exact sample/reference agreement and usable coverage remain unverified.

Public source: [DRR171213](https://www.ebi.ac.uk/ena/browser/view/DRR171213). Input unit: one paired archive run.

Reported amount: 450,083,225 bases (450.083 million). Listed source objects: 2; 344,072,580 bytes (344.073 decimal MB). fa ID 4 / GCF_000005845.2.

Size evidence: 450 million bases is close to the broader E. coli Illumina median of 435 million and its eight-run study median of 428 million; it is about 97 times the reference length in raw bases.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This supports a standard isolate input. Full-file integrity and actual sample/reference sequence agreement remain later checks. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 50. Saccharomyces cerevisiae — Illumina NovaSeq 6000

This input supplies a compact eukaryotic microbial genome alongside bacterial isolates and yeast Hi-C.

Public source: [SRR30502372](https://www.ebi.ac.uk/ena/browser/view/SRR30502372). Input unit: one paired archive run.

Reported amount: 2,123,156,100 bases (2.123 billion). Listed source objects: 2; 1,034,612,012 bytes (1.035 decimal GB). fa ID 7 / GCF_000146045.2.

Size evidence: 2.12 billion bases is near the upper quartile of its 61-run study and about 176 times the reference length in raw bases. It is a high-end, credible yeast research input.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: Its ploidy/LOH study purpose is explicit. Do not claim all yeast production normally uses this depth or convert haploid-reference ratios into per-copy coverage. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 51. metagenome — GridION

This input supplies a known multi-genome long-read setting, distinct from pure genomes and short marker libraries.

Public source: [ERR3152366](https://www.ebi.ac.uk/ena/browser/view/ERR3152366). Input unit: one archive run.

Reported amount: 16,506,755,978 bases (16.507 billion). Listed source objects: 1; 17,147,527,495 bytes (17.148 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: 16.51 billion bases is close to the four-positive-run source-study range (six records; two zero totals). The study explicitly concerns ultra-deep sequencing of a mock community.

Properties: Saved nonrandom prefix aggregates only; whole-file distributions/integrity not established. Lengths: File 1: 50–32099; median 4038. Quality characters: File 1: 60.

Limits and preparation: This represents a real mock/community research input, not an ordinary soil or clinical metagenome depth. The deliberate composition and current basecalling vintage must stay visible. Check whole files and pairing before testing.

## Data 52. food fermentation metagenome — Illumina NovaSeq 6000

This cereal-fermentation community-RNA library is a named timepoint, with 10.324 billion reported bases in one complete paired run. Five documented timepoints span 10.324–11.764 billion bases. These quantities support the source-workflow amount; the 12-billion-base service example is context rather than an admission threshold. The chosen material is a fermentation community; its composition and reference coverage remain unverified.

Public source: [DRR1003246](https://www.ebi.ac.uk/ena/browser/view/DRR1003246). Input unit: One complete paired fermentation-timepoint RNA library.

Reported amount: 10,323,974,492 bases (10.324 billion). Listed source objects: 2; 4,133,721,402 bytes (4.134 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: Five named fermentation timepoints contain 10.324–11.764 billion bases, with median 11.198 billion. The selected 13-day run has 10,323,974,492 bases. The independent 12 Gb service example supplies context rather than a numerical minimum.

Properties: All listed files are unpreviewed; no measured length, quality or header profile is available. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The source identifies community RNA from a fermentation timepoint, but untouched instrument-output status is not certified. Community composition and a fixed transcript-reference set remain unverified. Use every exact listed object and preserve run boundaries; verify full-file integrity and pairing where applicable before testing. No preparation or acquisition was performed for this edition.

## Data 53. soil metagenome — HiSeq X Ten

This input supplies environmental shotgun DNA alongside host-associated and food mixtures.

Public source: [DRR1000746](https://www.ebi.ac.uk/ena/browser/view/DRR1000746). Input unit: one paired archive run.

Reported amount: 10,115,398,800 bases (10.115 billion). Listed source objects: 2; 7,496,700,808 bytes (7.497 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: 10.12 billion bases is close to its eight-run study median of 10.32 billion and within the broad soil shotgun range; the median of known-study medians is 12.91 billion.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: Community complexity and organism proportions are not measured by these totals. No single-genome coverage is assigned. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 54. human gut metagenome — Illumina NovaSeq 6000

This input supplies a mainstream host-associated shotgun input as the collection’s ordinary gut-DNA example.

Public source: [DRR1003638](https://www.ebi.ac.uk/ena/browser/view/DRR1003638). Input unit: one paired archive run.

Reported amount: 6,596,836,500 bases (6.597 billion). Listed source objects: 2; 3,130,599,344 bytes (3.131 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: 6.60 billion bases is close to its 30-run study and inside the wider gut shotgun P10–P90 range of 0.29–9.86 billion; the median of study medians is 4.81 billion.

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: The declared run amount and source-study context support this gut shotgun example. Full biological-sample allocation and whole-file properties remain unverified. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 55. food metagenome — Illumina NovaSeq 6000

This honey-origin shotgun DNA run supplies food-mixture genomic sequencing, with 5.697 billion reported bases in one paired archive run. Its amount fits the 63-run honey-study cohort. A mixed food-origin reference setting differs from pure crop genomes, bacterial isolates and gut communities; measured ingredient composition is not asserted.

Public source: [SRR27931704](https://www.ebi.ac.uk/ena/browser/view/SRR27931704). Input unit: one paired archive run.

Reported amount: 5,697,274,998 bases (5.697 billion). Listed source objects: 2; 2,096,744,147 bytes (2.097 decimal GB). Mixture/feature reference not fixed; no single genomic FASTA is nominated.

Size evidence: 5.70 billion bases lies within the 0.74–6.14-billion P10–P90 range of 63 matched honey-study runs.

Unit and processing sources: [Exact honey shotgun source sample](https://www.ebi.ac.uk/ena/browser/view/SRX23588786)

Properties: Unpreviewed; No length, quality or header profile was inspected; these properties remain unknown. Whole-file integrity and pairing are not established. Lengths: Not examined. Quality characters: Not examined.

Limits and preparation: This supports a per-product research run. It does not establish general food-industry delivery norms or measured community composition. Full acquisition/integrity/pairing and any auxiliary definitions pending.

## Data 56. Cricetulus griseus — Illumina HiSeq 2500

This complete CHO genomic assembly library supplies an industrial production-cell reference-assembly research input. Both paired runs of the same named preparation are included: 77,003,500,500 reported bases in four files. The named library defines a natural assembly-data unit; exact cell-line/reference agreement and whole-file properties remain unverified.

Public source: [ERR2192893](https://www.ebi.ac.uk/ena/browser/view/ERR2192893), [ERR2192894](https://www.ebi.ac.uk/ena/browser/view/ERR2192894). Input unit: Complete CHO genomic library/component: 2 paired runs, 4 separate files.

Reported amount: 77,003,500,500 bases (77.004 billion). Listed source objects: 4; 57,234,426,121 bytes (57.234 decimal GB). fa ID 17 / GCF_003668045.3.

Size evidence: Two public paired runs of the same named CHO genomic preparation sum to 77,003,500,500 reported bases. Both are included as one complete named library; this is source-workflow support for the declared assembly input, not a universal production norm.

Unit and processing sources: [Named CHO genomic assembly library](https://www.ebi.ac.uk/ena/browser/view/PRJEB12319)

Properties: No inspected properties are recorded for any listed object. Lengths: Unpreviewed. Quality characters: Unpreviewed.

Limits and preparation: The complete two-run named library is not the entire CHO assembly project. Submitted CRAM is represented by the selected archive FASTQ ends; the normalized representation and native order have not been body-verified. Keep all listed run outputs and both ends separate. Validate full-file integrity and pairing before compression. No files were acquired or concatenated.

# Versioned references and later FASTQ preparation

The 18 used reference identities have the fa IDs listed below. Renan GCA_937894285.1 is the proposed same-cultivar assembly. Landing pages are labelled separately from direct gzip FASTA routes. No reference body was acquired or verified. Same-species does not prove strain, cultivar, transcript or target matching. The human/fly normalization-reference proposal is not pure fly genomic coverage. Marker and community inputs do not receive invented single-genome FASTAs.

fa ID 1: Homo sapiens — GRCh38 / [GCF_000001405.39](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.39_GRCh38.p13/GCF_000001405.39_GRCh38.p13_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 2: Sus scrofa — Sscrofa11.1 / [GCA_000003025.6](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000003025.6/). Accession landing page; exact FASTA retrieval remains to be fixed. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 3: Mus musculus — GRCm38 / [GCF_000001635.24](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.24_GRCm38.p4/GCF_000001635.24_GRCm38.p4_genomic.fna.gz). Direct gzip FASTA route. Same-species genomic reference proposal for mouse inputs; sample/strain/target match and FASTA contents unverified. For Smart-seq2, transcript/patch equivalence and auxiliary ERCC version are separately unverified.

fa ID 4: Escherichia coli — ASM584 / [GCF_000005845.2](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 5: Mycobacterium tuberculosis — ASM19595v2 (H37Rv) / [GCF_000195955.2](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/955/GCF_000195955.2_ASM19595v2/GCF_000195955.2_ASM19595v2_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 6: Solanum tuberosum — SolTub_3.0 / [GCA_000226075.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/226/075/GCA_000226075.1_SolTub_3.0/GCA_000226075.1_SolTub_3.0_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 7: Saccharomyces cerevisiae — R64 / [GCF_000146045.2](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 8: Oryza sativa — ASM1463603v1 / [GCA_014636035.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/014/636/035/GCA_014636035.1_ASM1463603v1/GCA_014636035.1_ASM1463603v1_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 9: Arabidopsis thaliana — TAIR10.1 / [GCF_000001735.4](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 10: Zea mays — Zm-B73-REFERENCE-NAM-5.0 / [GCA_902167145.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/902/167/145/GCA_902167145.1_Zm-B73-REFERENCE-NAM-5.0/GCA_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz). Direct gzip FASTA route. Same-species, different-inbred B73 reference for SW1611. Exact sample/cultivar/contig matching and FASTA contents remain unverified.

fa ID 11: Penaeus vannamei — ASM4276789v1 / [GCF_042767895.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/042/767/895/GCF_042767895.1_ASM4276789v1/GCF_042767895.1_ASM4276789v1_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 12: Gallus gallus — bGalGal1.mat.broiler.GRCg7b / [GCA_016699485.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/699/485/GCA_016699485.1_bGalGal1.mat.broiler.GRCg7b/GCA_016699485.1_bGalGal1.mat.broiler.GRCg7b_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 13: Drosophila melanogaster — Release 6 plus ISO1 MT / [GCF_000001215.4](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/215/GCF_000001215.4_Release_6_plus_ISO1_MT/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna.gz). Direct gzip FASTA route. Same-species proposal only; sample/strain/target/contig match and FASTA contents unverified.

fa ID 14: Severe acute respiratory syndrome coronavirus 2 — NC_045512.2 / [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2). Accession landing page; exact FASTA retrieval remains to be fixed. Same-organism label proposal; isolate/variant/target compatibility untested.

fa ID 15: Picea abies — Pabies01 / [GCA_900067695.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/067/695/GCA_900067695.1_Pabies01/GCA_900067695.1_Pabies01_genomic.fna.gz). Direct gzip FASTA route. Proposed same-species assembly; sample/strain/cultivar/target matching and FASTA content unverified.

fa ID 16: Chenopodium quinoa — ASM168347v1 / [GCF_001683475.1](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/683/475/GCF_001683475.1_ASM168347v1/GCF_001683475.1_ASM168347v1_genomic.fna.gz). Direct gzip FASTA route. Proposed same-species assembly; sample/strain/cultivar/target matching and FASTA content unverified.

fa ID 17: Cricetulus griseus — CriGri-PICRH-1.0 / [GCF_003668045.3](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/003/668/045/GCF_003668045.3_CriGri-PICRH-1.0/GCF_003668045.3_CriGri-PICRH-1.0_genomic.fna.gz). Direct gzip FASTA route. Proposed same-species assembly; sample/strain/cultivar/target matching and FASTA content unverified.

fa ID 18: Triticum aestivum cultivar Renan — Triticum_aestivum_Renan_v2.1 / [GCA_937894285.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_937894285.1/). Accession landing page; exactFASTA object must be chosen later. Same Renan cultivar assemblyv2.1; no measured read match.

Generic lossless compression tests recovery of the chosen FASTQ bytes. Spatial masks, coordinates, feature tables and genomic FASTA are not automatic prerequisites. A selected reference-based compressor must use a fixed versioned reference; feature-aware matching or downstream reconstruction may require additional definitions. Component identity, actual file access and chosen representation remain separate requirements.

Before testing, acquire the exact listed objects through a usable public route, verify full-file integrity and component relationships, and fix the exact prepared FASTQ bytes. Account for reference bytes and preparation consistently across compressors. Preserve original versus prepared identities. This package specifies selection and later preparation. Saved prefix observations are scoped individually; no whole-collection verification or compression results are available. Packaging did not process real source data.

For each listed gzip source separately, require successful full gzip CRC/truncation validation and gzip -dc decompression. Preserve headers, sequences, quality characters, record order and formatting exactly. Keep mates, runs and chunks separate; do not concatenate, recompress, trim, normalize or reformat. Reject incomplete decompression outputs. Record gzip version and exact commands, source identity and source-container checksum, output byte count and output SHA-256. Source gzip checksums and prepared FASTQ hashes identify different byte streams. See the [preparation commands](preparation.md).

Data 6 is a BAM source only. Its mapped SUP flow-cell analysis reports 153,264,463,825 bases and 8,155,127 reads, but these are not verified as the exact selected BAM/export yield. The pinned, unexecuted [preparation rule](preparation.md) uses SAMtools 1.22/htslib 1.22, natural QNAME sorting, unpaired primary records, stored qualities and a stop on missing primary qualities. It records exact source/output hashes and options when run. Prepared order is not native instrument order. Losslessness applies to the resulting FASTQ, not BAM tags/alignments.

Data 8: One selected CNGB run/source object CNR1409093, WY_reads.fq.gz; single reads, not mates. No publisher MD5 is available for this object; verification is size-only against the listed 130,270,589,600 bytes. Size agreement alone does not prove content integrity. The SINGLE representation is not a pair of mates. Cached CNGB metadata identifies human HG002 genomic WGS, RANDOM selection, G400-ER and fragment/single layout. Exact byte equivalence to the SRA originals remains unverified. Prefix header observations do not establish whole-file pairing or integrity. Properties: Nonrandom prefix observation: 258 complete records after transferring 1,048,576 compressed bytes; 2,432,831 decompressed FASTQ bytes. Whole-file read/base totals, distributions and integrity remain unverified. Lengths: 355–28,912 bases in 258 complete nonrandom-prefix records.

Data 22 has documentary HiFi identity and an exact source/yield join. Its filename containing _subreads is an archive representation name, not independent proof of raw-subread or consensus processing. Actual qualities/headers remain unpreviewed. Spatial masks/coordinates and CITE feature/barcode definitions are needed for particular interpretation or custom reference matching, not generic byte-identical compression. Taxonomy tables are auxiliary, not a genomic reference or an admission criterion.

# Exact files for multi-run and chunked inputs

Each row is one exact physical object. Names and URLs are verbatim listed metadata. Keep the shown run boundaries and mate/chunk roles; no concatenated filename or combined archive accession has been fabricated. The Files worksheet contains the same detail for all 115 objects.

## Data 16 — Wheat cultivar Renan — 6 files

| Run / end or chunk | Exact physical filename | Full listed URL |
| --- | --- | --- |
| ERR6348210; Read end 1 | ERR6348210_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/000/ERR6348210/ERR6348210_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/000/ERR6348210/ERR6348210_1.fastq.gz) |
| ERR6348210; Read end 2 | ERR6348210_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/000/ERR6348210/ERR6348210_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/000/ERR6348210/ERR6348210_2.fastq.gz) |
| ERR6348211; Read end 1 | ERR6348211_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/001/ERR6348211/ERR6348211_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/001/ERR6348211/ERR6348211_1.fastq.gz) |
| ERR6348211; Read end 2 | ERR6348211_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/001/ERR6348211/ERR6348211_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/001/ERR6348211/ERR6348211_2.fastq.gz) |
| ERR6348212; Read end 1 | ERR6348212_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/002/ERR6348212/ERR6348212_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/002/ERR6348212/ERR6348212_1.fastq.gz) |
| ERR6348212; Read end 2 | ERR6348212_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/002/ERR6348212/ERR6348212_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR634/002/ERR6348212/ERR6348212_2.fastq.gz) |

## Data 31 — CITE ADT — 8 files

| Run / end or chunk | Exact physical filename | Full listed URL |
| --- | --- | --- |
| SRR19066657; Read end 1 | SRR19066657_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/057/SRR19066657/SRR19066657_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/057/SRR19066657/SRR19066657_1.fastq.gz) |
| SRR19066657; Read end 2 | SRR19066657_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/057/SRR19066657/SRR19066657_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/057/SRR19066657/SRR19066657_2.fastq.gz) |
| SRR19066658; Read end 1 | SRR19066658_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/058/SRR19066658/SRR19066658_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/058/SRR19066658/SRR19066658_1.fastq.gz) |
| SRR19066658; Read end 2 | SRR19066658_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/058/SRR19066658/SRR19066658_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/058/SRR19066658/SRR19066658_2.fastq.gz) |
| SRR19066659; Read end 1 | SRR19066659_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_1.fastq.gz) |
| SRR19066659; Read end 2 | SRR19066659_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/059/SRR19066659/SRR19066659_2.fastq.gz) |
| SRR19066661; Read end 1 | SRR19066661_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/061/SRR19066661/SRR19066661_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/061/SRR19066661/SRR19066661_1.fastq.gz) |
| SRR19066661; Read end 2 | SRR19066661_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/061/SRR19066661/SRR19066661_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/061/SRR19066661/SRR19066661_2.fastq.gz) |

## Data 32 — CITE mRNA — 8 files

| Run / end or chunk | Exact physical filename | Full listed URL |
| --- | --- | --- |
| SRR19066662; Read end 1 | SRR19066662_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/062/SRR19066662/SRR19066662_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/062/SRR19066662/SRR19066662_1.fastq.gz) |
| SRR19066662; Read end 2 | SRR19066662_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/062/SRR19066662/SRR19066662_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/062/SRR19066662/SRR19066662_2.fastq.gz) |
| SRR19066664; Read end 1 | SRR19066664_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/064/SRR19066664/SRR19066664_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/064/SRR19066664/SRR19066664_1.fastq.gz) |
| SRR19066664; Read end 2 | SRR19066664_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/064/SRR19066664/SRR19066664_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/064/SRR19066664/SRR19066664_2.fastq.gz) |
| SRR19066665; Read end 1 | SRR19066665_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_1.fastq.gz) |
| SRR19066665; Read end 2 | SRR19066665_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/065/SRR19066665/SRR19066665_2.fastq.gz) |
| SRR19066666; Read end 1 | SRR19066666_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/066/SRR19066666/SRR19066666_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/066/SRR19066666/SRR19066666_1.fastq.gz) |
| SRR19066666; Read end 2 | SRR19066666_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/066/SRR19066666/SRR19066666_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/066/SRR19066666/SRR19066666_2.fastq.gz) |

## Data 33 — CITE HTO — 8 files

| Run / end or chunk | Exact physical filename | Full listed URL |
| --- | --- | --- |
| SRR19066668; Read end 1 | SRR19066668_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_1.fastq.gz) |
| SRR19066668; Read end 2 | SRR19066668_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/068/SRR19066668/SRR19066668_2.fastq.gz) |
| SRR19066669; Read end 1 | SRR19066669_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/069/SRR19066669/SRR19066669_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/069/SRR19066669/SRR19066669_1.fastq.gz) |
| SRR19066669; Read end 2 | SRR19066669_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/069/SRR19066669/SRR19066669_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/069/SRR19066669/SRR19066669_2.fastq.gz) |
| SRR19066671; Read end 1 | SRR19066671_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/071/SRR19066671/SRR19066671_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/071/SRR19066671/SRR19066671_1.fastq.gz) |
| SRR19066671; Read end 2 | SRR19066671_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/071/SRR19066671/SRR19066671_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/071/SRR19066671/SRR19066671_2.fastq.gz) |
| SRR19066672; Read end 1 | SRR19066672_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/072/SRR19066672/SRR19066672_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/072/SRR19066672/SRR19066672_1.fastq.gz) |
| SRR19066672; Read end 2 | SRR19066672_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/072/SRR19066672/SRR19066672_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/072/SRR19066672/SRR19066672_2.fastq.gz) |

## Data 56 — CHO named library — 4 files

| Run / end or chunk | Exact physical filename | Full listed URL |
| --- | --- | --- |
| ERR2192893; Read end 1 | ERR2192893_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/003/ERR2192893/ERR2192893_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/003/ERR2192893/ERR2192893_1.fastq.gz) |
| ERR2192893; Read end 2 | ERR2192893_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/003/ERR2192893/ERR2192893_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/003/ERR2192893/ERR2192893_2.fastq.gz) |
| ERR2192894; Read end 1 | ERR2192894_1.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/004/ERR2192894/ERR2192894_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/004/ERR2192894/ERR2192894_1.fastq.gz) |
| ERR2192894; Read end 2 | ERR2192894_2.fastq.gz | [https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/004/ERR2192894/ERR2192894_2.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR219/004/ERR2192894/ERR2192894_2.fastq.gz) |

# Annual maintenance

Update annually using the latest completed September: stock through the cutoff and the preceding 12-month public-release increment. Reuse unchanged audited evidence and refresh consequential applied-use/deployment claims. Reassess useful workload/material/library/technology/reference conditions and representative input amounts. Add, replace or remove only for documented data issues or useful coverage improvement, recording lost and gained roles and exact input units. No change is a valid outcome. This collection is not a proven minimum and has no target count.
