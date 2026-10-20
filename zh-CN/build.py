import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TRANSLATIONS = ROOT / 'zh-CN' / 'translation_map.json'
AUDIT = ROOT / '.build' / 'zh-CN'

subprocess.run([
    sys.executable,
    str(ROOT / 'tools' / 'build.py'),
    '--language', 'zh-CN',
    '--translations', str(TRANSLATIONS),
    '--audit-dir', str(AUDIT),
], cwd=ROOT, check=True)
subprocess.run([
    sys.executable,
    str(ROOT / 'zh-CN' / 'postprocess_workbook.py'),
    str(ROOT / 'zh-CN' / 'catalogue' / 'benchmark_dataset.xlsx'),
    str(TRANSLATIONS),
], check=True)

manifest = json.loads((ROOT / 'catalogue' / 'manifest.json').read_text(encoding='utf-8'))
translations = json.loads(TRANSLATIONS.read_text(encoding='utf-8'))
rows = [
    '# 数据集目录',
    '',
    '[English](../../README.md) · [简体中文首页](../README.md)',
    '',
    f"同一集合，数据集版本 {manifest['dataset_version']}。选择理由见[完整报告](../docs/report.md)或工作簿“选择理由”表；“文件”表列出全部下载文件。",
    '',
    '| 数据编号 | 数据集 | 公共编号 | 文件数 | 报告碱基数 | 下载字节数 |',
    '|---:|---|---|---:|---:|---:|',
]
for item in manifest['selected']:
    amount = item['metadata']['reported_base_count']
    amount_text = f'{amount:,}' if amount is not None else '尚未确定'
    size = sum(file['listed_bytes'] for file in item['files'])
    title = translations.get(item['display_name'], item['display_name'])
    rows.append(
        f"| {item['no']} | {title} | {item['identity']} | {len(item['files'])} | {amount_text} | {size:,} |"
    )
(ROOT / 'zh-CN' / 'catalogue' / 'README.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
