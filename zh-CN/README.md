# FASTQ 无损压缩基准数据集

[English](../README.md) · **简体中文**  
数据集版本：v1.1.0 · [版本说明](VERSIONING.md)

这份数据集用于测试 FASTQ 文件的无损压缩和解压。我们选择了 52 组公开数据，覆盖常见的测序技术和用途。每组数据都给出选择理由、下载地址和使用方法。这个仓库只保存清单和说明，测序文件需要另外下载。

基准输入是**未压缩的 FASTQ 文件**。下载得到的 gzip 文件需要先解压。无损恢复要求还原相同的读段名称、序列、质量字符、顺序和格式，而不只是得到相同的生物序列。

## 数据集包含什么

| 项目 | 数量 |
| --- | ---: |
| 数据集 | 52 |
| 待下载文件 | 91：90 个 gzip FASTQ 文件和 1 个 BAM 文件 |
| 清单所列下载总字节数 | 1,404,952,612,896 字节（1.405 十进制 TB） |
| 有发布者 MD5 值的文件 | 75 |
| 建议参考序列版本 | 18 |

数据包括人类及其他生物的基因组、整体和单细胞 RNA、标签与空间读段、染色质文库、靶向标记、分离株和混合群落，也涵盖多种技术产生的短读段与长读段。所选档案输入均为一次完整测序运行，并包含清单列出的全部读段端。BAM 和单个 CNGB FASTQ 保留各自声明的公开来源单位。请保留清单列出的每个文件。

## 查找数据和证据

- [完整选择报告](docs/report.md) · [Word 报告](docs/report.docx) · [HTML 报告](docs/report.html)。
- [可读目录](catalogue/README.md) · [Excel 工作簿](catalogue/benchmark_dataset.xlsx) · [CSV 目录](catalogue/catalogue.csv)。
- [全部文件及下载链接](catalogue/files.tsv) · [建议的参考序列](catalogue/references.tsv) · [机器可读清单](../catalogue/manifest.json)。
- [校验和及带日期的核验记录](../checksums/README.md) · [数据准备说明](docs/preparation.md)。
- [引用方式](CITATION.md) · [权利与许可状态](RIGHTS.md) · [验证范围](docs/validation.md)。

工作簿中的“数据集”表列出各组输入，“文件”表列出文件及下载信息，“参考序列”表列出参考方案；“选择理由”和“详细信息”分别提供简要说明与完整的数量依据、处理注意事项。目录、工作簿和下载程序共用同一文件清单。

## 下载

需要 Python 3.8 或更高版本以及 GNU wget。请将下载文件放在新的版本专属目录中，例如 `downloads/v1.1.0`。现有下载任务和目录没有移动或更改。

```bash
# 列出文件，不执行下载。
python3 download_benchmark.py --dry-run

# 下载所有入选文件；保留现有有效文件和可续传的部分文件。
python3 download_benchmark.py --output downloads/v1.1.0 --jobs 8

# 也可只下载指定数据集的全部清单文件。
python3 download_benchmark.py --ids 10,29 --output downloads/v1.1.0
```

下载程序会核对清单中的文件大小，并在有发布者 MD5 时检查该值。未完成的文件保留为 `.part`，MD5 不一致时会报告错误。

全部 91 个源文件均已下载并完成检查。[MD5SUMS 文件](../checksums/MD5SUMS)覆盖每个文件：75 个值与发布者提供的 MD5 一致，另外 16 个值由我们在完整性检查后计算。[核验表](../checksums/verification.tsv)记录了 MD5 来源和检查日期。请按[校验说明](checksums/README.md)检查自己的下载文件。

Data 8 是单个 CNGB 文件 `WY_reads.fq.gz`，不是一对读段或两个分块。清单所列文件大小为 130,270,589,600 字节，没有发布者 MD5 值。Data 6 是待按固定规则导出为 FASTQ 的 BAM 文件。两者所选来源的确切碱基总量均未确定。

## 准备和测试

请按[完整准备说明](docs/preparation.md)处理数据。每个 gzip 源文件都要检查完整数据流，单独解压，并记录 FASTQ 字节数和 SHA-256。不要合并配对文件、不同测序运行或分块，也不要改动文件字节。Data 6 使用文档规定的 SAMtools 1.22/htslib 1.22 导出规则；该规则已通过合成测试，但尚未用于真实 BAM。

建议的参考序列版本尚未在此处下载或验证，也不保证与样本匹配。空间掩码和标签定义可用于特定解释或自定义参考方案，但不是通用 FASTQ 无损压缩的必要输入。

归档调查覆盖截至 2026 年 9 月 30 日的存量及此前 12 个月的公开增量，并沿用原始来源和检索日期。全球统计包含中国。归档托管地不能说明商业生产地点或产量。报告详述调查结果及其限制。

## 重建和检查仓库

```bash
# 仅运行小型合成测试，不读取真实测序数据。
python3 -m unittest discover -s tests -v

# 重建英文文档和表格；需要安装 XlsxWriter 和 markdown-it-py。
python3 tools/build.py
```

固定 BAM 导出规则的测试需要 SAMtools 1.22/htslib 1.22。源文件完整性检查、文档检查和压缩基准测试回答的是不同问题。本仓库没有报告实测压缩比或吞吐量；参见[验证范围](docs/validation.md)。尚未检查原生 Office 分页效果。

各语言版本共用同一份数据清单；数据编号、文件身份和数量均按清单记录。
