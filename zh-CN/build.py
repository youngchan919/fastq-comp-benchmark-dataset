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
