# 输入准备与验证

[英文首页](../../README.md) · [简体中文](../README.md)

请使用[权威清单](../../catalogue/manifest.json)和[文件表](../catalogue/files.tsv)列出的精确文件清单。本文规定未来的数据准备方式。本软件包尚未从真实源 BAM 导出 FASTQ，也未为本软件包运行压缩基准测试。

## 按清单保留完整输入

一次双端测序运行必须包含清单所列的两个读段端。选入的 Thatcher 小麦输入、每个 CITE 组分和 CHO 输入各包含一次完整的双端测序运行，两个 FASTQ 文件均须保留。保留不同 CITE 组分的身份以及每次运行的两个读段端。不得悄悄丢弃文件、拼接无关输入，也不要把一次运行扩展为同一生物样本的所有文库。

Data 8 是单个 SINGLE CNGB 文件 `WY_reads.fq.gz`，不是一对文件，也不是两个分块。CNGB 元数据将其项目、样本、实验和测序运行标识与 2025 年 12 月 4 日的发布日期关联起来。该文件清单所列大小为 130,270,589,600 字节，没有发布者 MD5。其准确的全文件读数/碱基产出，以及与相关 SRA 表示之间的字节等价性，仍未验证。

## 测试前验证已获取的源文件

共享下载程序会记录计划获取的文件及每个文件的验证状态。75 个源文件同时有发布者提供的 MD5 和登记大小；16 个文件没有记录发布者校验和。目录中的记录或成功发起的请求，都不表示文件已经核验完成。没有发布者校验和时，应记录本地 SHA-256，以便后续复现；但本地哈希本身不能独立认证内容来自发布者。

[MD5SUMS](../../checksums/MD5SUMS) 已覆盖全部 91 个下载源文件。其中，16 个没有发布者 MD5 的文件已通过完整的 gzip/BAM 检查，并计算了本地 MD5。请先按[校验说明](../checksums/README.md)检查自己的下载文件，再准备 FASTQ 测试输入。

参考序列表区分带版本号的来源页面和拟议的直接 FASTA 获取路径。参考序列的大小/校验和信息不完整；只检查 FASTA 的首字符，不能验证整个文件或登录号身份。进行基于参考序列的比较前，应确认完整 FASTA 的完整性、固定版本，以及它与所选样本之间的关系。对于混合群落和特征文库，不得虚构单一基因组参考序列。空间掩码/坐标和 CITE 特征表可用于特定解释或自定义匹配，不适用于通用的逐字节无损压缩。

## Gzip 源文件：基准目标是未压缩 FASTQ

**基准输入是未压缩 FASTQ 字节**。下载的 gzip 文件是压缩后的分发文件，不是用于比较的压缩程序的输入。应逐个解压清单中的源文件，保留每个头部、序列、质量字符、记录、顺序和格式字节。不得拼接配对文件、测序运行或分块；不得修剪、规范化、重新排版或重新压缩准备后的 FASTQ。

确认 gzip 文件完整后，对每个确切列出的文件分别运行以下 Bash 命令。此示例准备玉米 Data 10 的一个配对端；应分别为另一个配对端和其他每个所选 gzip 源文件重复操作，并使用相应路径。使用全新的输出名称。成功运行 `gzip -t` 和 `gzip -dc` 要求 gzip 流完整且 CRC/长度校验有效；任何错误或截断都会中止流程。失败后留下的 `.part` 输出不是压缩测试的输入。

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

在准备记录中记录 gzip 版本、确切命令、源身份和源校验和、输出字节数以及输出 SHA-256。源 gzip 校验和与准备后 FASTQ 哈希标识的是不同字节流，二者不可互相替代。压缩比和吞吐量必须以准备后的未压缩 FASTQ 字节数作为输入分母。打包期间没有对任何真实源文件执行解压。

## Data 6：固定的 BAM 转 FASTQ 规则

Data 6 是指定的 ONT PAW70337 SUP 流动槽 BAM。单独的比对分析数量不能确定准确的源文件/导出产出量。无损目标是生成的 FASTQ，而不是保留 BAM 标签或比对结果。

随附的 [prepare_data6.py](../../prepare_data6.py) 要求 **SAMtools 1.22 with htslib 1.22**；`samtools --version-only` 应报告 `1.22+htslib-1.22`。

1. 在 `LC_ALL=C` 下，使用 `samtools sort -n -@ 0 -m 768M` 按名称对固定源 BAM 排序。
2. 保留主记录，排除次要/补充标志 `0x900`。已比对和未比对的主记录均可纳入。本规则预期记录未配对，且具有已存储的序列和质量值。
3. 如果主记录带有 paired/READ1/READ2 标志、QNAME 重复、SEQ 缺失或 QUAL 缺失，则停止。这些情况需要明确的准备决定；脚本不会悄悄丢弃记录或合成质量值。
4. 对按名称排序后的 BAM 运行 `samtools fastq -@ 0 -n -F 0x900`。保留 QNAME，不添加 mate 后缀或复制标签。使用已存储的 QUAL，不启用优先使用 OQ 的选项。SAMtools 会将反向链比对转换回正向 FASTQ 方向。
5. 写出一个纯文本 `Data_6.fastq` 和 `preparation.json`。收据记录确切工具、源/输出 SHA-256、大小、选定记录数，以及顺序/质量值策略。根据声明的主记录规则核对输出记录数。

这是固定的准备选择，并非仪器原始顺序。已存储的软剪切序列可以导出；BAM 中不存在的硬剪切序列无法恢复。真实 BAM 是否适用以及确切输出量仍**尚未执行/验证**。请参阅固定版本的 [fastq 文档](https://www.htslib.org/doc/1.22/samtools-fasta.html)和 [sort 文档](https://www.htslib.org/doc/1.22/samtools-sort.html)。

```bash
# 仅查看已声明的规则；不读取源文件，也不创建输出。
python3 prepare_data6.py downloads/data/Data_6/calls.sorted.bam --dry-run

# 只有获取并核验源文件、接受该规则后，才执行实际准备。
python3 prepare_data6.py downloads/data/Data_6/calls.sorted.bam --output prepared/Data_6
```

小型合成测试检查主记录筛选、自然名称排序、反向方向、使用存储质量值而非 OQ、确定性输出和明确停止条件。测试通过只能验证夹具上的软件规则，不能验证或处理 Data 6。

## 记录实际基准输入

保留每个源文件的身份/哈希、完整文件单位、准备命令/版本、准备后未压缩 FASTQ 的哈希/字节数，以及参考序列版本。不同压缩程序的参考序列存储/准备成本应采用一致方式核算。应针对固定输入字节评估精确解压恢复。此目录不提供实测压缩比、吞吐量或最优/最小集合结论。
