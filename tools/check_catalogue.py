"""Check local catalogue, generated packages and navigation without source access."""
import argparse
import csv
import hashlib
import html
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as E
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--audit-dir', type=Path)
args = parser.parse_args()
manifest_path = ROOT / 'catalogue/manifest.json'
m = json.loads(manifest_path.read_text())
by = {x['no']: x for x in m['selected']}
files = [(x, f) for x in m['selected'] for f in x['files']]
checks = {}
checks['52_unique_stable_IDs'] = len(by) == len(m['selected']) == 52
checks['115_unique_source_objects'] = len(files) == len({f['url'] for x, f in files}) == 115
checks['source_bytes'] = sum(f['listed_bytes'] for x, f in files) == m['counts']['listed_source_bytes'] == 1419456345104
checks['MD5_and_size_only_status'] = sum(bool(f['publisher_md5']) for x, f in files) == 73 and sum(not bool(f['publisher_md5']) for x, f in files) == 42
checks['known_base_denominator'] = m['counts']['datasets_without_exact_source_base_total'] == [6, 8] and sum(x['metadata']['reported_base_count'] or 0 for x in by.values()) == m['counts']['known_reported_sequence_bases'] == 2029937896053
checks['Data8_single_current_source'] = by[8]['identity'] == 'CNR1409093' and by[8]['metadata']['experiment'] == 'CNX1236558' and by[8]['metadata']['layout'] == 'SINGLE' and len(by[8]['files']) == 1 and by[8]['files'][0]['physical_name'] == 'WY_reads.fq.gz' and by[8]['files'][0]['listed_bytes'] == 130270589600 and by[8]['files'][0]['publisher_md5'] == ''
checks['Data8_scope_and_no_inherited_yield'] = by[8]['metadata']['reported_base_count'] is None and '258 complete records' in by[8]['properties']['scope'] and '355–28,912' in by[8]['properties']['lengths'] and by[8]['properties']['quality_characters'] == 'Not recorded'
checks['all_active_reference_versions'] = len(m['references']) == 18 and {q['fa_no'] for x in by.values() for q in x['reference_proposals']} == {q['no'] for q in m['references']}
checks['all_coverage_IDs_resolve'] = all(set(x['selected_numbers']) <= set(by) for k in ['coverage', 'materials', 'technologies'] for x in m[k])
plan = subprocess.check_output([sys.executable, str(ROOT / 'download_benchmark.py'), '--dry-run'], text=True)
jobs = list(csv.DictReader(plan.splitlines(), delimiter='\t'))
checks['download_plan_parity'] = len(jobs) == len(files) and all(j['url'] == f['url'] and j['path'].endswith('/' + f['physical_name']) and int(j['expected_bytes']) == f['listed_bytes'] and j['publisher_md5'] == f['publisher_md5'] for j, (x, f) in zip(jobs, files))
source_table = list(csv.DictReader((ROOT / 'catalogue/files.tsv').open(), delimiter='\t'))
checks['source_table_parity'] = len(source_table) == 115 and all(r['URL'] == f['url'] and r['Filename'] == f['physical_name'] and r['Publisher MD5'] == f['publisher_md5'] and int(r['Listed bytes']) == f['listed_bytes'] for r, (x, f) in zip(source_table, files))
cat = list(csv.DictReader((ROOT / 'catalogue/catalogue.csv').open(encoding='utf-8-sig')))
checks['catalogue_csv_parity'] = len(cat) == 52 and all(int(r['Data ID']) == x['no'] and r['Identity'] == x['identity'] and r['Why included'] == x['reason'] and int(r['Listed compressed bytes']) == sum(f['listed_bytes'] for f in x['files']) for r, x in zip(cat, m['selected']))
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main', 'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
sheets, links, regions = {}, {}, {}
with zipfile.ZipFile(ROOT / 'catalogue/benchmark_dataset.xlsx') as z:
    checks['XLSX_package_and_XML'] = z.testzip() is None
    for name in z.namelist():
        if name.endswith(('.xml', '.rels')):
            E.fromstring(z.read(name))
    ss = [''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', ns)]
    wr = {x.attrib['Id']: x.attrib['Target'] for x in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    for sh in E.fromstring(z.read('xl/workbook.xml')).find('s:sheets', ns):
        path = 'xl/' + wr[sh.attrib['{' + ns['r'] + '}id']]
        t = E.fromstring(z.read(path))
        cells = {}
        for c in t.findall('.//s:sheetData/s:row/s:c', ns):
            v = c.findtext('s:v', default='', namespaces=ns)
            cells[c.attrib['r']] = ss[int(v)] if c.attrib.get('t') == 's' else v
        relpath = path.rsplit('/', 1)[0] + '/_rels/' + path.rsplit('/', 1)[1] + '.rels'
        rels = {x.attrib['Id']: x.attrib['Target'] for x in E.fromstring(z.read(relpath))} if relpath in z.namelist() else {}
        hl = {}
        for x in t.findall('s:hyperlinks/s:hyperlink', ns):
            hl[x.attrib['ref']] = 'internal:' + x.attrib['location'] if 'location' in x.attrib else rels[x.attrib['{' + ns['r'] + '}id']]
        sheets[sh.attrib['name']] = cells
        links[sh.attrib['name']] = hl
        regions[sh.attrib['name']] = {'cells': cells, 'row_heights': {x.attrib['r']: float(x.attrib.get('ht', '15')) for x in t.findall('s:sheetData/s:row', ns)}, 'columns': [x.attrib for x in t.findall('s:cols/s:col', ns)]}
    creator = E.fromstring(z.read('docProps/core.xml')).find('{http://purl.org/dc/elements/1.1/}creator')
    checks['no_invented_author'] = creator is None or not creator.text
fq, ff, rr, fa = [sheets[k] for k in ['fq', 'Files', 'Reasons', 'fa']]
def idrows(cells, start):
    return {int(v): int(k[1:]) for k, v in cells.items() if re.fullmatch('A[0-9]+', k) and int(k[1:]) >= start}
fqr, rrr, far = idrows(fq, 3), idrows(rr, 2), idrows(fa, 2)
checks['actual_current_ID_rows'] = set(fqr) == set(rrr) == set(by) and set(far) == {q['no'] for q in m['references']}
checks['actual_manufacturer_yield_units'] = all(fq['N' + str(fqr[n])] == x['manufacturer'] and fq['T' + str(fqr[n])] == str(x['metadata']['reported_base_count'] if x['metadata']['reported_base_count'] is not None else 'Not established for selected source') and ('One CNGB single-read FASTQ file' if n == 8 else x['metadata']['unit']) in fq['O' + str(fqr[n])] for n, x in by.items())
checks['actual_all_reasons_and_scopes'] = all(rr['C' + str(rrr[n])] == x['reason'] and rr['G' + str(rrr[n])] == x['properties']['scope'] for n, x in by.items())
checks['actual_all_files_verbatim'] = all(ff['A' + str(i)] == str(x['no']) and ff['D' + str(i)] == f['physical_name'] and ff['I' + str(i)] == f['url'] and int(ff['F' + str(i)]) == f['listed_bytes'] and ff['N' + str(i)] == f['properties']['scope'] for i, (x, f) in enumerate(files, 2))
internal = []
for n in by:
    for col, target_sheet in [('Z', 'Reasons'), ('V', 'Files')]:
        target = links['fq'][col + str(fqr[n])]
        sh, address = target[len('internal:'):].rsplit('!', 1)
        sh = sh.strip("'")
        internal.append(sh == target_sheet and sheets[sh][address] == str(n))
checks['104_links_same_DataID'] = len(internal) == 104 and all(internal)
checks['actual_reference_source_and_download_routes'] = all(fa['D' + str(far[q['no']])] == q['accession_version'] and links['fa']['E' + str(far[q['no']])] == q['route'] and links['fa']['H' + str(far[q['no']])] == q['download_url'] for q in m['references'])
w = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(ROOT / 'docs/report.docx') as z:
    checks['DOCX_package_and_XML'] = z.testzip() is None
    for name in z.namelist():
        if name.endswith(('.xml', '.rels')):
            E.fromstring(z.read(name))
    t = E.fromstring(z.read('word/document.xml'))
    text = '\n'.join(''.join(x.itertext()) for x in t.findall('.//w:body/*', w))
    dr = E.fromstring(z.read('word/_rels/document.xml.rels'))
    doclinks = [x.attrib['Target'] for x in dr if x.attrib.get('TargetMode') == 'External']
md = (ROOT / 'docs/report.md').read_text()
checks['all52_reasons_actual_DOCX_MD'] = all(x['reason'] in text and x['reason'] in md for x in by.values())
checks['Data8_current_actual_DOCX'] = all(v in text for v in ['CNR1409093', 'CNX1236558', 'WY_reads.fq.gz', '130,270,589,600', '258 complete reads', '355–28,912']) and 'Data 8 has two consecutive' not in text
checks['actual_current_counts_and_unknowns'] = all(v in text for v in ['115 (114 gzip FASTQ files and one BAM)', '1,419,456,345,104', '2,029,937,896,053', '50 inputs', 'Data 6 and Data 8 are unknown and excluded'])
checks['34_multirun_file_appendix_objects'] = sum(len(x['files']) for x in by.values() if len(x['run_accessions']) > 1) == 34 and all(f['physical_name'] in text and f['url'] in doclinks for x in by.values() if len(x['run_accessions']) > 1 for f in x['files'])
checks['survey_principles_result_order'] = text.index('What the annual public archive view establishes') < text.index('What the applied-use survey found') < text.index('How the datasets were chosen') < text.index('The 52 datasets')
checks['reference_proposals_and_preparation_unexecuted'] = all(v in text for v in ['SAMtools 1.22/htslib 1.22', 'stop on missing primary qualities', 'not native instrument order', 'They have not been downloaded or verified here'])
prep = (ROOT / 'docs/preparation.md').read_text()
checks['uncompressed_FASTQ_target_and_checked_decompression'] = all(v in text for v in ['exact uncompressed FASTQ bytes', 'Do not concatenate mates, runs or chunks', 'FASTQ byte count and SHA-256']) and all(v in prep for v in ['Benchmark inputs are uncompressed FASTQ bytes', 'gzip -t -- "$source_gz"', 'gzip -dc -- "$source_gz"', 'sha256sum -- "$source_gz" "$output_fastq"', 'CRC/length', 'Do not concatenate']) and 'fix whether the benchmark input' not in prep and 'If decompressed FASTQ is chosen' not in prep
checks['version_and_publisher_MD5_inventory'] = (ROOT/'VERSION').read_text().strip() == m['dataset_version'] == '1.0.0' and len((ROOT/'checksums/MD5SUMS').read_text().splitlines()) == 73 and {(line.split()[0],line.split()[1]) for line in (ROOT/'checksums/MD5SUMS').read_text().splitlines()} == {(f['publisher_md5'],'data/Data_'+str(x['no'])+'/'+f['physical_name']) for x,f in files if f['publisher_md5']}
verification_rows = list(csv.DictReader((ROOT/'checksums/verification.tsv').open(),delimiter='\t'))
checks['dated_115_file_verification_no_fake_SHA256'] = len(verification_rows) == 115 and len({z['Path'] for z in verification_rows}) == 115 and all(z['Snapshot UTC'] for z in verification_rows) and not (ROOT/'checksums/SHA256SUMS').exists()
checks['full_details_preserved_in_actual_workbook'] = all(x['size_evidence'] in sheets['Details'].values() and x['limits'] in sheets['Details'].values() for x in by.values())
checks['plain_reason_amount_and_checks_actual_workbook'] = all(rr['D'+str(rrr[n])] == x['amount_summary'] and rr['E'+str(rrr[n])] == x['checks_summary'] for n,x in by.items())
local_links = []
for p in ROOT.rglob('*.md'):
    if 'zh-CN' in p.relative_to(ROOT).parts:
        continue
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if not re.match(r'^[a-z]+://', target) and not target.startswith('#'):
            local_links.append((p, target, (p.parent / target.split('#')[0]).exists()))
for target in doclinks:
    if not re.match(r'^[a-z]+://', target):
        local_links.append((ROOT / 'docs/report.docx', target, (ROOT / 'docs' / target).exists()))
checks['English_local_navigation_and_document_links'] = all(ok for p, target, ok in local_links)
checks['Chinese_navigation_target_exists'] = (ROOT / 'zh-CN').is_dir() and '[简体中文](zh-CN/)' in (ROOT / 'README.md').read_text()
checks['license_and_attribution_pending_honest'] = m['publication_metadata']['authors'] is None and m['publication_metadata']['project_license'] is None and 'not yet been specified' in (ROOT / 'RIGHTS.md').read_text()
checks['no_history_sheets'] = not {'Changes', 'Considered'} & set(sheets)
public_text = '\n'.join(p.read_text() for p in ROOT.rglob('*') if p.suffix in ['.md', '.json', '.csv', '.tsv', '.py'] and p.name != 'check_catalogue.py')
checks['no_private_paths_or_conversation'] = not re.search(r'/zdswhst|/home/chenyuxin|/tmp/|idk/rounds|\bcolleague\b|product manager|internal proposal|customer conversation', public_text, re.I)
code = (ROOT / 'download_benchmark.py').read_text()
checks['one_manifest_no_local_download_workarounds'] = "'catalogue' / 'manifest.json'" in code and 'KNOWN_BAD_PARTIALS' not in code and 'no_proxy' not in code and not (ROOT / 'download_data8_cngb.py').exists()
checks['no_real_data_bundled'] = not any(p.is_file() and (p.name.endswith(('.fastq', '.fq', '.bam', '.cram', '.fna', '.fastq.gz', '.fq.gz', '.fna.gz'))) for p in ROOT.rglob('*'))
result = {'status': 'PASS' if all(checks.values()) else 'FAIL', 'checks': checks, 'counts': m['counts'], 'manifest_sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest(), 'scope': 'English package only; Chinese translation/review pending. Local package/cell/link checks, not native Office pagination or real-data validation.', 'failed_local_links': [str(p.relative_to(ROOT)) + ': ' + target for p, target, ok in local_links if not ok]}
if args.audit_dir:
    args.audit_dir.mkdir(parents=True, exist_ok=True)
    (args.audit_dir / 'actual_workbook_cells.json').write_text(json.dumps(regions, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['status'] == 'PASS' else 1)
