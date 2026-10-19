# FASTQ 压缩基准数据集

[English](../README.md) · **简体中文**

供任何人比较**无损 FASTQ 压缩与解压**的公开数据目录。本集合结合公开档案分布与有文档记录的测序用途，再据此选择明确的输入单位和具有代表性的序列数量。它不针对某一种压缩程序、制造商或团队。

本目录包含元数据、证据、报告和脚本，不含测序数据或参考序列数据。基准输入是**未压缩 FASTQ 字节**；下载的 gzip 文件只是源容器。无损恢复要求还原完全相同的准备后 FASTQ 字节，包括名称、序列、质量值、顺序和格式。

| 当前集合 | 数量 |
|---|---:|
| 一个集合中的数据集 | 52 |
| 登记的源对象 | 115：114 个 gzip FASTQ 文件和 1 个 BAM |
| 登记的压缩源字节 | 1,419,456,345,104（1.419 十进制 TB）|
| 有发布者 MD5 的对象 | 73 |
| 仅有文件大小预期的对象 | 42 |
| 带版本号的参考序列提案 | 18 |

Data ID 是稳定标识符；请以目录中的实际条目为准。一个数据集可以是一个配对 run、单个细胞，或一个完整命名的多 run 文库。保留清单列出的每个配对端、标签组分和分块文件。目录并不表示已获取源数据、已验证全文件完整性或已有基准结果。

## 查看证据和目录

- [完整报告](docs/report.md) · [Word](docs/report.docx) · [HTML](docs/report.html)：从调查、选择原则到当前集合，并为每个输入说明理由和适当的数据量。
- [可读目录](catalogue/README.md) · [Excel 工作簿](catalogue/benchmark_dataset.xlsx) · [CSV](catalogue/catalogue.csv)。
- [所有源文件](catalogue/files.tsv)和[所有拟议参考序列](catalogue/references.tsv)。
- [准备与验证说明](docs/preparation.md)，包括明确规定但尚未执行的 Data 6 BAM 转 FASTQ 规则。
- [来源登记表](../evidence/evidence_register.json)和[调查发现登记表](../evidence/survey_discovery_register.csv)。
- [引用方式](CITATION.md)、[权利/许可证状态](RIGHTS.md)和[验证范围](docs/validation.md)。

[目录清单](../catalogue/manifest.json)是**唯一权威的库存记录**。工作簿、可读表、报告和下载程序均从该清单读取源身份、文件和数量。源 gzip/BAM 大小、报告的序列碱基数，以及尚未测量的未压缩 FASTQ 字节数，是彼此不同的数量。Data 6 和 Data 8 的确切产出量仍未知，因此不计入已知所选源序列总量。

全球档案快照统计截至 **2026 年 9 月 30 日**的存量，以及此前 12 个月首次公开的增量。报告保留各来源实际记录的检索日期。全球数据包含中国；档案托管地点不能代表生产地点或产量。整理日期：**2026 年 10 月 19 日**。

## 以后再计划和下载

未来获取数据需在 Linux/Unix 环境下安装 Python 3.8+ 和 GNU wget。本软件包本身不包含源数据。

```bash
# 不访问网络或创建输出目录，打印全部 115 项源数据任务。
python3 download_benchmark.py --dry-run

# 查看单个输入，或准备就绪后将数据获取到单独目录。
python3 download_benchmark.py --ids 10,30 --dry-run
python3 download_benchmark.py --ids 10,30 --output downloads

# 参考序列仅提供带版本号的建议来源；请先检查状态。
python3 download_benchmark.py --kind references --dry-run

# 不传输网络数据，验证已获取到本地的源文件。
python3 download_benchmark.py --output downloads --verify-only
```

下载程序读取清单，续传 `.part` 文件，写出状态 TSV，并且不会覆盖已完成的文件。若有发布者 MD5 和登记大小，程序会据此核验。**仅文件大小一致的验证力度较弱，不能证明内容完整。**若参考序列未公布大小/校验和，则只检查 FASTA 标题，不验证身份或完整性。参考来源以及读段与参考序列的确切匹配关系，在实际核验前都只是提案。请为实际测试保留本地哈希和准备收据。

Data 8 是 **CNR1409093 / CNX1236558**，一个 SINGLE 文件 `WY_reads.fq.gz`，登记大小为 130,270,589,600 字节，且没有发布者 MD5。CNGB 元数据将其识别为 G400-ER 上的人类 HG002 基因组 WGS。已保存的非随机前缀有 258 条完整记录，读长为 355–28,912 个碱基，未观察到四行格式错误。这不能证明全文件属性、产出量、配对关系或与相关 SRA 原始数据的字节等价性。

## 本地检查与重新生成

```bash
# 仅使用小型合成夹具；导出规则测试要求指定版本的 SAMtools。
python3 -m unittest discover -s tests -v

# 根据清单重新生成英文报告和工作簿。
# 重新生成还需要 Python xlsxwriter 包。
python3 tools/build.py
```

测试检查目录/下载计划一致性、合成验证行为和固定的导出规则。它们不会访问真实测序数据，也不会测量压缩性能。软件包与单元格检查不是原生 Office 分页渲染证明。

中文文档和目录使用相同的事实清单与共享脚本。英文源是科学身份与数量的参照；语言审查不等同于验证源数据。

---

[维护者：中文版重建说明](BUILD.md)
