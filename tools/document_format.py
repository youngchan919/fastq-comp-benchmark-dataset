import html,re,zipfile
from xml.sax.saxutils import escape

def write_documents(blocks, OUT):
    def inline(s):
     s=html.escape(s);s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<a href="{m[2]}">{m[1]}</a>',s)
     return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
    ht=['<!doctype html><meta charset="utf-8"><title>FASTQ compression benchmark dataset</title><style>body{font:16px/1.55 Arial,sans-serif;color:#183047;max-width:1100px;margin:40px auto;padding:0 24px}h1{font-size:27px;margin-top:34px}h2{font-size:19px;margin-top:22px}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border:1px solid #bdcbd3;padding:8px;text-align:left;vertical-align:top}th{background:#e7eff4}a{color:#075b9a}tr{break-inside:avoid}h1,h2{break-after:avoid}</style>']
    for b in blocks:
     if b['type']=='table':ht.append('<table><thead><tr>'+''.join('<th>'+inline(x)+'</th>' for x in b['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>' for row in b['rows'])+'</tbody></table>')
     else:ht.append('<'+b['type']+'>'+inline(b['text'])+'</'+b['type']+'>')
    (OUT/'report.html').write_text('\n'.join(ht))
    
    W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';RR='http://schemas.openxmlformats.org/officeDocument/2006/relationships';rels=[]
    def run(s):return '<w:r><w:t xml:space="preserve">'+escape(s)+'</w:t></w:r>'
    def content(s):
     s=s.replace('**','');parts=[];pos=0
     for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',s):
      parts.append(run(s[pos:m.start()]));rels.append(m[2]);parts.append(f'<w:hyperlink r:id="rId{len(rels)}"><w:r><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr><w:t>'+escape(m[1])+'</w:t></w:r></w:hyperlink>');pos=m.end()
     return ''.join(parts)+run(s[pos:])
    def xp(s,style='Normal'):return '<w:p><w:pPr><w:pStyle w:val="'+style+'"/></w:pPr>'+content(s)+'</w:p>'
    body=[]
    for b in blocks:
     if b['type']=='table':
      parts=['<w:tbl><w:tblPr><w:tblW w:w="9360" w:type="dxa"/><w:tblBorders>'+''.join('<w:'+x+' w:val="single" w:sz="4" w:color="BDCBD3"/>' for x in ['top','left','bottom','right','insideH','insideV'])+'</w:tblBorders></w:tblPr>']
      for ri,row in enumerate([b['headers']]+b['rows']):
       parts.append('<w:tr><w:trPr><w:cantSplit/>'+('<w:tblHeader/>' if ri==0 else '')+'</w:trPr>')
       for cell in row:parts.append('<w:tc><w:tcPr><w:tcW w:w="'+str(9360//len(row))+'" w:type="dxa"/>'+('<w:shd w:fill="E7EFF4"/>' if ri==0 else '')+'</w:tcPr>'+xp(cell,'TableText')+'</w:tc>')
       parts.append('</w:tr>')
      body.append(''.join(parts)+'</w:tbl>')
     else:body.append(xp(b['text'],{'h1':'Heading1','h2':'Heading2'}.get(b['type'],'Normal')))
    doc=f'<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="{W}" xmlns:r="{RR}"><w:body>'+''.join(body)+'<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1000" w:bottom="1000" w:left="1000" w:right="1000"/></w:sectPr></w:body></w:document>'
    styles=f'''<?xml version="1.0"?><w:styles xmlns:w="{W}"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="21"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="130" w:line="270" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style><w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:pPr><w:keepNext/><w:spacing w:before="330" w:after="180"/></w:pPr><w:rPr><w:b/><w:sz w:val="30"/><w:color w:val="183047"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:pPr><w:keepNext/><w:spacing w:before="230" w:after="100"/></w:pPr><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table Text"/><w:rPr><w:sz w:val="18"/></w:rPr></w:style></w:styles>'''
    rel='<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(f'<Relationship Id="rId{i}" Type="{RR}/hyperlink" Target="{escape(u,{chr(34):"&quot;"})}" TargetMode="External"/>' for i,u in enumerate(rels,1))+f'<Relationship Id="styles" Type="{RR}/styles" Target="styles.xml"/></Relationships>'
    with zipfile.ZipFile(OUT/'report.docx','w',zipfile.ZIP_DEFLATED) as z:
     z.writestr('[Content_Types].xml','<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/xml"/><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>')
     z.writestr('_rels/.rels',f'<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="document" Type="{RR}/officeDocument" Target="word/document.xml"/></Relationships>')
     z.writestr('word/document.xml',doc);z.writestr('word/styles.xml',styles);z.writestr('word/_rels/document.xml.rels',rel)
    
    return len(rels)
