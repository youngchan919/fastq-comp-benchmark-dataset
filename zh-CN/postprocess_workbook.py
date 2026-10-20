import argparse
import json
import os
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('workbook', type=Path)
parser.add_argument('translations', type=Path)
args = parser.parse_args()
translations = json.loads(args.translations.read_text(encoding='utf-8'))
worksheet_names = {
    'fa': '参考序列', 'fq': '数据集', 'Files': '文件', 'Reasons': '选择理由',
    'Details': '详细信息', 'Coverage': '覆盖', 'Materials': '材料', 'Technology': '技术', 'Evidence': '证据',
    'Archive totals': '归档总量', 'Archive strategy': '归档策略',
    'Archive platforms': '归档平台', 'Archive sources': '归档来源',
    'Archive layout': '归档布局', 'Archive organisms': '归档生物', 'Verification': '核验记录',
    'Archive joints': '归档联合统计', 'Read me': '阅读说明',
}
with zipfile.ZipFile(args.workbook) as source:
    workbook = ET.fromstring(source.read('xl/workbook.xml'))
    relationships = ET.fromstring(source.read('xl/_rels/workbook.xml.rels'))
    rel_by_id = {rel.get('Id'): rel.get('Target') for rel in relationships}
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
          'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    readme = next(sheet for sheet in workbook.findall('m:sheets/m:sheet', ns)
                  if sheet.get('name') == 'Read me')
    target = rel_by_id[readme.get('{' + ns['r'] + '}id')]
    worksheet_path = 'xl/' + target if not target.startswith('/') else target[1:]
    worksheet = ET.fromstring(source.read(worksheet_path))
    shared = ET.fromstring(source.read('xl/sharedStrings.xml'))
    for item in shared.findall('m:si', ns):
        item_text = ''.join(node.text or '' for node in item.findall('.//m:t', ns))
        if item_text in ['Identity — 52 datasets', 'Sample information', 'Sequencing', 'File information / reported amounts']:
            nodes = item.findall('.//m:t', ns)
            if len(nodes) != 1:
                raise ValueError(f'Expected one text node for merged label: {item_text!r}')
            nodes[0].text = translations[item_text]
    cell = next(cell for cell in worksheet.findall('.//m:c', ns) if cell.get('r') == 'A9')
    shared_index = int(cell.find('m:v', ns).text)
    shared_item = shared.findall('m:si', ns)[shared_index]
    shared_text = ''.join(node.text or '' for node in shared_item.findall('.//m:t', ns))
    if shared_text != translations['References']:
        raise ValueError(f'Unexpected Read me!A8 label: {shared_text!r}')
    text_nodes = shared_item.findall('.//m:t', ns)
    if len(text_nodes) != 1:
        raise ValueError('Expected one text node for Read me!A8 label')
    text_nodes[0].text = '参考序列'
    localized_shared_strings = ET.tostring(shared, encoding='utf-8', xml_declaration=True)
fd, temp_name = tempfile.mkstemp(suffix='.xlsx', dir=args.workbook.parent)
os.close(fd)
try:
    with zipfile.ZipFile(args.workbook) as source, zipfile.ZipFile(temp_name, 'w', zipfile.ZIP_DEFLATED) as target:
        for item in source.infolist():
            data = source.read(item.filename)
            if item.filename == 'xl/sharedStrings.xml':
                data = localized_shared_strings
            elif item.filename == 'xl/workbook.xml':
                root = ET.fromstring(data)
                ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                for sheet in root.findall('m:sheets/m:sheet', ns):
                    sheet.set('name', worksheet_names[sheet.get('name')])
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            elif item.filename.startswith('xl/worksheets/sheet') and item.filename.endswith('.xml'):
                root = ET.fromstring(data)
                for element in root.iter():
                    if element.tag.endswith('hyperlink') and 'location' in element.attrib:
                        location = element.attrib['location']
                        for source_name, target_name in worksheet_names.items():
                            location = location.replace("'" + source_name + "'!", "'" + target_name + "'!")
                        element.attrib['location'] = location
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            target.writestr(item, data)
    os.replace(temp_name, args.workbook)
finally:
    if os.path.exists(temp_name):
        os.unlink(temp_name)
