import csv,copy,html,json,math,re,shutil,sys,zipfile
from pathlib import Path
from datetime import datetime,timezone
from xml.sax.saxutils import escape
import argparse
import xlsxwriter
from document_format import write_documents, normalize_bold
parser=argparse.ArgumentParser(description="Regenerate catalogue and report from the shared manifest")
parser.add_argument('--language',choices=['en','zh-CN'],default='en')
parser.add_argument('--translations',type=Path)
parser.add_argument('--audit-dir',type=Path)
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
LANG=ROOT if args.language=='en' else ROOT/'zh-CN'
OUT=LANG/'docs';CAT=LANG/'catalogue';R=args.audit_dir or ROOT/'.build'/args.language
for target in [OUT,CAT,R]:target.mkdir(parents=True,exist_ok=True)
translations=json.load(open(args.translations)) if args.translations else {}
def tr(value):return normalize_bold(translations.get(value,value)) if isinstance(value,str) else value
pub=json.load(open(ROOT/'catalogue/manifest.json'));selected=pub['selected'];counts=pub['counts'];by={x['no']:x for x in selected}
survey=json.load(open(ROOT/'evidence/archive_summary.json'));sources=copy.deepcopy({x['id']:x for x in survey['sources']});sources['R10D33']['title']='dbGaP phs003751.v1.p1 study metadata';sources.update({x['id']:x for x in json.load(open(ROOT/'evidence/evidence_register.json'))});blocks=[]
def p(s):blocks.append({'type':'p','text':str(s)})
def h(s,level=1):blocks.append({'type':'h'+str(level),'text':str(s)})
def table(headers,rows):blocks.append({'type':'table','headers':headers,'rows':[[str(v) if v is not None else 'Not established' for v in row] for row in rows]})
def cites(ids):return ' '.join('['+sources[i]['title']+']('+sources[i]['url']+')' for i in ids if i in sources)
def reftext(x):return '; '.join('fa ID '+str(z['fa_no'])+' / '+z['accession_version'] for z in x['reference_proposals']) or 'Mixture/feature reference not fixed; no single genomic FASTA is nominated'
def fmtbase(v):
 if v is None:return 'Exact selected-source sequence yield not established'
 divisor,unit=(1e9,'billion') if v>=1e9 else (1e6,'million')
 return format(v,',')+' bases ('+format(v/divisor,'.3f')+' '+unit+')'
def fmtbytes(v):
 divisor,unit=(1e3,'kB') if v<1e6 else ((1e6,'MB') if v<1e9 else (1e9,'GB'))
 return format(v,',')+' bytes ('+format(v/divisor,'.3f')+' decimal '+unit+')'
def runlinks(x):
 if x['no']==8:return '[CNR1409093 / CNX1236558](https://db.cngb.org/search/run/CNR1409093/)'
 return ', '.join('['+v+'](https://www.ebi.ac.uk/ena/browser/view/'+v+')' for v in x['run_accessions']) if x['source_format']!='BAM' else '[PAW70337 SUP flow-cell source]('+x['source_url']+')'
h('FASTQ compression benchmark dataset')
p('Dataset version '+pub['dataset_version']+' • 20 October 2026')
p('This dataset is for testing lossless FASTQ compression and decompression. It contains 52 public datasets covering common sequencing technologies and uses. Each entry explains why it was chosen, lists the files to download, and describes the input to test. The repository contains the catalogue and instructions; sequencing files are downloaded separately.')
table(['Collection','Quantity'],[['Datasets',str(counts['selected_datasets'])+' (51 FASTQ datasets and one BAM source)'],['Files to download',str(counts['source_objects'])+' ('+str(counts['source_object_formats']['FASTQ.gz'])+' gzip FASTQ files and one BAM)'],['Listed download bytes',format(counts['listed_source_bytes'],',')],['Suggested reference versions',str(len(pub['references']))]])
p('A fair lossless test must recover the exact uncompressed FASTQ bytes, including read names, sequences, quality characters, order and formatting. Downloaded gzip files are containers to decompress first. The one BAM input needs the fixed export described in the preparation guide. Download sizes are not uncompressed FASTQ sizes or compression results.')
for b in copy.deepcopy(json.load(open(ROOT/'evidence/survey_report_blocks.json'))):
 if 'text' in b:b['text']=b['text'].replace('](benchmark_dataset.xlsx)','](../catalogue/benchmark_dataset.xlsx)').replace('](survey_discovery_register.csv)','](../evidence/survey_discovery_register.csv)')
 blocks.append(b)
h('How the datasets were chosen')
p('The archive survey shows which kinds of sequencing are common and how much sequence they contain. Publicly documented research, services and technology deployments add uses that archive counts alone may miss. Worldwide includes China; the two views are never added. A service listing establishes availability, not sales volume. A crop’s economic value alone does not establish sequencing demand.')
table(['Selection rule','What it means here'],[['Choose important workloads','Use archive runs, reported bases and research breadth alongside documented applied use. Do not give every species, manufacturer or named application its own file automatically.'],['Keep useful differences','Include important library, technology, read and reference differences. Similar quality alphabets do not establish similar frequency patterns. A difference is not a measured compression advantage.'],['Use a complete, sensible input','A complete deposited run or public vendor output can be the appropriate unit. Compare sequence amount with the same task and unit; do not prefer smaller files simply to save space.'],['Fix the bytes and references','List every file belonging to the input. Preserve exact prepared FASTQ bytes and state reference versions and remaining preparation. Select before testing compressors.']])
p('Source-study comparisons support particular examples; they are not universal production norms. There is no minimum file size, target dataset count, score or claim that this is the smallest possible collection. Annual review may keep the same inputs when their reasons remain sound.')
p('The workbook separates the sequencer manufacturer from the library method. Illumina and MGI commonly supply parallel short reads; ONT, CycloneSEQ and PacBio supply single-molecule long-read technologies. These are often called second- and third-generation sequencing. A 10x or CITE library label does not identify the sequencer. Archive strategy labels describe what was sampled, while layout describes single or paired reads.')
p('The collection includes human and other genome sequencing; bulk, small and single-cell RNA; CITE tags and spatial reads; chromatin libraries; targeted markers; isolates and mixed communities. The workbook’s Coverage, Materials and Technology sheets explain the links between those uses and the selected entries. Detailed archive tables and source notes remain available there.')
p('Reported sequence totals are separate from file sizes and read/spot counts. Known selected FASTQ totals sum to '+format(counts['known_reported_sequence_bases'],',')+' bases across 50 inputs. Exact source totals for Data 6 and Data 8 are unknown and excluded; associated analysis or SRA totals are not substituted. Study counts are not added across overlapping categories.')
h('Why some files are small')
p(str(len(pub['small_input_context']['dataset_ids']))+' complete inputs contain less than one decimal GB of compressed downloads after all their files are counted. A target library, individual cell, sample tag or compact genome can be a meaningful small input. Amount is judged against the task, not a one-GB floor. Startup and reference overhead can matter for small files, but no such performance has been measured here. Files are not padded or repeated to make them larger.')
h('The 52 datasets')
p('Read the reasons below alongside the [workbook](../catalogue/benchmark_dataset.xlsx), [all file links](../catalogue/files.tsv) and [current verification notes](../checksums/README.md). Data IDs identify entries within this version. Each entry’s amount is reported sequence, while its listed bytes describe the download. In the workbook, Reasons gives the short explanation and Details preserves the full amount evidence, processing notes and observation scope.')
for x in selected:
 n=x['no'];m=x['metadata'];h('Data '+str(n)+'. '+x['display_name'],2)
 p(x['reason'])
 p('Amount: '+fmtbase(m['reported_base_count'])+'. Download: '+fmtbytes(sum(f['listed_bytes'] for f in x['files']))+' in '+str(len(x['files']))+' file(s).')
 p('Why this amount: '+x['amount_summary'])
 p('Public run(s): '+runlinks(x)+'. Reference: '+reftext(x)+'.')
 if n in [6,7,8,10,12,14,17,21,22,28,29,30,31,32,33,36,43,52]:p('Check before use: '+x['checks_summary'])
 if x.get('unit_evidence_ids'):p('Method and amount sources: '+cites(x['unit_evidence_ids']))
h('Download, check and prepare the files')
p('The [download and checksum guide](../checksums/README.md) separates publisher MD5 expectations from checks completed locally. Its status table is a dated snapshot, not a promise that every file has finished downloading. A matching size alone does not prove file integrity. A checksum for a compressed source file does not identify the decompressed FASTQ bytes.')
p('Use the [preparation guide](preparation.md) to check source files, decompress each gzip file separately and record the uncompressed FASTQ byte count and SHA-256. Preserve names, sequence, quality, order and formatting. Do not concatenate mates, runs or chunks, normalize records or recompress the prepared input. Full gzip CRC/EOF checks must pass.')
p('Data 6 requires the specified SAMtools 1.22/htslib 1.22 export. It uses natural QNAME order, primary unpaired records, stored qualities and a stop on missing primary qualities. This rule has synthetic tests, but the real BAM has not been exported. Prepared order is not native instrument order, and FASTQ does not preserve BAM tags or alignments.')
p('Saved prefix observations apply only to the exact files identified in Files. They are nonrandom samples, not whole-file distributions or integrity checks. A quality character is an encoded value in the FASTQ quality line; modal share means the percentage of inspected quality positions occupied by its most common character. New or uninspected files do not inherit another file’s measurements.')
p('Data 8 is one SINGLE CNGB file, not two mates or chunks. Its whole-file yield and byte equivalence to the associated SRA files are unknown. The saved prefix contains 258 complete reads with lengths 355–28,912 bases; it does not establish the distribution of the whole file. No publisher MD5 is available.')
h('Reference versions')
p('These 18 suggested references have fixed accession versions. They have not been downloaded or verified here. The fa sheet distinguishes source pages from proposed direct FASTA downloads. Same species does not establish the same strain, cultivar or transcript targets. A mixed community or tag library does not receive an invented single-genome reference.')
for z in pub['references']:p('fa '+str(z['no'])+': '+z['organism']+' — '+z['name']+' / ['+z['accession_version']+']('+z['route']+'). '+z['relationship'])
p('Renan GCA_937894285.1 is a same-species, different-cultivar reference proposal for the Thatcher wheat reads. CITE tag definitions and spatial masks/coordinates may be needed for interpretation or a custom reference, but not for exact compression and recovery of the supplied FASTQ. Taxonomy tables are auxiliary files, not genomic references.')
h('Files for every input')
p('The following list contains every selected file. Preserve the two ends of each paired run as separate FASTQs. The one BAM and one single-read CNGB file are listed separately. Names and URLs are exact catalogue values.')
table(['Data ID','Run / source','End / role','Exact filename','Download'],[[x['no'],f['run_accession'],f['role'],f['physical_name'],'['+f['physical_name']+']('+f['url']+')'] for x in selected for f in x['files']])
h('Updates and citation')
p('Review the archive and applied-use evidence annually. Keep dataset IDs and exact file lists stable within a data version. [Versioning](../VERSIONING.md) explains which changes need a new version; adding verification results does not imply different input bytes. See [citation](../CITATION.md) and [rights](../RIGHTS.md) for repository attribution and the current license status. This collection supplies test inputs and evidence, not measured compression results.')

md=[]
for b in blocks:
 if b['type']=='table':md+=['| '+' | '.join(b['headers'])+' |','| '+' | '.join('---' for _ in b['headers'])+' |']+['| '+' | '.join(str(c).replace('|',' / ').replace('\n','<br>') for c in row)+' |' for row in b['rows']]+['']
 else:md+=['#'*int(b['type'][1:])+' '+b['text'] if b['type'].startswith('h') else b['text'],'']
if args.language!='en':
 for block in blocks:
  if block['type']=='table':block['headers']=[tr(v) for v in block['headers']];block['rows']=[[tr(v) for v in row] for row in block['rows']]
  else:block['text']=tr(block['text']).replace('../evidence/','../../evidence/')
for block in blocks:
 if block['type']=='table':block['headers']=[normalize_bold(v) for v in block['headers']];block['rows']=[[normalize_bold(str(v)) for v in row] for row in block['rows']]
 else:block['text']=normalize_bold(block['text'])
md=[]
for block in blocks:
 if block['type']=='table':md+=['| '+' | '.join(block['headers'])+' |','| '+' | '.join('---' for _ in block['headers'])+' |']+['| '+' | '.join(str(c).replace('|',' / ').replace('\n','<br>') for c in row)+' |' for row in block['rows']]+['']
 else:md+=['#'*int(block['type'][1:])+' '+block['text'] if block['type'].startswith('h') else block['text'],'']
(OUT/'report.md').write_text('\n'.join(md),encoding='utf-8')
(R/'report_blocks.json').write_text(json.dumps(blocks,indent=2,ensure_ascii=False)+'\n')
link_count=write_documents(blocks,OUT)
evidence=json.load(open(ROOT/'evidence/evidence_register.json'))
# Human workbook layout follows the accepted fa/fq/Files arrangement.
wb=xlsxwriter.Workbook(CAT/'benchmark_dataset.xlsx');wb.set_properties({'title':'Public FASTQ compression benchmark','subject':'Dataset '+pub['dataset_version']+'; '+str(counts['selected_datasets'])+' datasets; 20 October 2026','author':''})
normal=wb.add_format({'font_name':'Arial','font_size':11,'text_wrap':True,'valign':'top','border':1,'border_color':'#D7DFE4'});head=wb.add_format({'font_name':'Arial','font_size':11,'bold':True,'bg_color':'#254B63','font_color':'white','text_wrap':True,'valign':'top','border':1});link=wb.add_format({'font_name':'Arial','font_size':11,'font_color':'#0563C1','underline':1,'text_wrap':True,'valign':'top','border':1});number=wb.add_format({'font_name':'Arial','font_size':11,'text_wrap':True,'valign':'top','border':1,'border_color':'#D7DFE4','num_format':'#,##0'});band=wb.add_format({'bold':True,'bg_color':'#D3E2ED','align':'center','valign':'vcenter','border':1,'font_size':12})
sheet_counts={};fit=[];sheet_data={}
def sheet(name,headers,rows,widths,start=0,full_url_columns=()):
 ws=wb.add_worksheet(name);ws.hide_gridlines(2);ws.freeze_panes(start+1,1);ws.set_zoom(85)
 for i,width in enumerate(widths):ws.set_column(i,i,width)
 ws.write_row(start,0,[tr(v) for v in headers],head);ws.set_row(start,52)
 for ri,row in enumerate(rows,start+1):
  for ci,value in enumerate(row):
   value=tr(value)
   if isinstance(value,(list,dict)):value=json.dumps(value,ensure_ascii=False)
   if value is None:value='Not established'
   if isinstance(value,str) and value.startswith(('https://','internal:')):ws.write_url(ri,ci,value,link,string=value if ci in full_url_columns else tr('Open source') if value.startswith('https://') else tr('Open detail'))
   elif isinstance(value,int) and abs(value)>=10**15:ws.write_string(ri,ci,str(value),normal)
   elif isinstance(value,int):ws.write_number(ri,ci,value,number)
   else:ws.write(ri,ci,value,normal)
  lines=max(sum(max(1,math.ceil(len(t)/max(8,widths[c]-2))) for t in str(v if v is not None else 'Not established').splitlines()) for c,v in enumerate(row));height=max(34,lines*16+14)
  if height>400:fit.append({'sheet':name,'excel_row':ri+1,'estimated_height':height})
  ws.set_row(ri,min(400,height))
 ws.autofilter(start,0,start+len(rows),len(headers)-1);ws.set_landscape();ws.fit_to_pages(1,0);ws.repeat_rows(0,start);ws.set_paper(9);sheet_counts[name]=len(rows);sheet_data[name]={'headers':headers,'rows':rows,'widths':widths,'start':start};return ws
sheet('fa',['fa ID','Reference / assembly','Species / material','Accession / version','Reference source link','Link type','Use / relationship','Proposed FASTA download'],[[q['no'],q['name'],q['organism'],q['accession_version'],q['route'],q['route_type'],q['relationship'],q['download_url']] for q in pub['references']],[8,29,30,25,20,35,72,65])
file_rows=[];first={}
for x in selected:
 for f in x['files']:
  first.setdefault(x['no'],len(file_rows)+2);pr=f['properties'];md5=f.get('publisher_md5','');recorded=bool(re.fullmatch('[0-9a-fA-F]{32}',md5));file_rows.append([x['no'],f['run_accession'],f['role'],f['physical_name'],f['format'],f['listed_bytes'],md5 if recorded else 'Not recorded','Publisher value; see dated Verification sheet' if recorded else 'No publisher MD5 recorded',f['url'],pr['lengths'],pr['quality_characters'],pr['quality_ascii'],pr['headers'],pr['scope']])
reasonrow={x['no']:i for i,x in enumerate(selected,2)};fq_rows=[]
for x in selected:
 m=x['metadata'];pr=x['properties'];n=x['no'];organization=m['layout']+'; '+str(len(x['run_accessions']))+' run(s), '+str(len(x['files']))+' file(s). '+('One CNGB single-read FASTQ file' if n==8 else m['unit']);fq_rows.append([n,m['study'],m['sample'],m['experiment'],'\n'.join(x['run_accessions']) if x['source_format']!='BAM' else 'PAW70337 SUP BAM',x['source_url'],m['organism'],m['common_name'],m['source'],m['preparation'],m['strategy'],x['technology'],m['model'],x['manufacturer'],organization,pr['quality_characters'],pr['quality_ascii'],pr['lengths'],int(m['reported_read_count']) if str(m['reported_read_count']).isdigit() else m['reported_read_count'],m['reported_base_count'] if m['reported_base_count'] is not None else 'Not established for selected source',round(sum(f['listed_bytes'] for f in x['files'])/1e9,6),"internal:'Files'!A"+str(first[n]),m['first_public'],reftext(x),m['named_sample'],"internal:'Reasons'!A"+str(reasonrow[n])])
headers=['Data ID','Project','Sample','Experiment(s)','Run(s) / public source','Source link','Scientific species / material','Common name','Sample / library source','Preparation','What was sequenced','Short / long reads','Sequencer','Manufacturer','Ends / file organization','Quality characters seen in saved prefix','Character codes seen (ASCII)','Read lengths seen (bases)','Archive-reported read/spot count','Reported sequence bases','Listed file size (decimal GB)','Files / listed MD5','First-public date / evidence','Reference','Named sample/library (not verified truth)','Why included / document entry']
fq=sheet('fq',headers,fq_rows,[10,18,19,20,25,14,28,20,24,27,26,25,27,24,43,30,26,38,25,25,21,16,27,37,29,20],start=1);fq.activate()
for left,right,label in [(0,5,'Identity — '+str(counts['selected_datasets'])+' datasets'),(6,8,'Sample information'),(9,13,'Sequencing'),(14,25,'File information / reported amounts')]:fq.merge_range(0,left,0,right,label,band)
fq.set_row(0,29)
sheet('Files',['Data ID','Run / source','End or chunk / role','Exact physical filename','Supplied format','Listed bytes','Publisher MD5','MD5 status','Full listed URL','Saved prefix lengths','Saved quality characters','Saved ASCII range','Header observation','Properties scope'],file_rows,[10,25,37,65,20,23,36,32,80,48,38,35,35,80],full_url_columns=(8,))
sheet('Reasons',['Data ID','Current input','Why chosen','Why this amount','Checks before use','Preparation','Files observed'],[[x['no'],'; '.join(x['run_accessions']),x['reason'],x['amount_summary'],x['checks_summary'],x['preparation'],x['properties']['scope']] for x in selected],[8,30,100,110,100,70,65])
sheet('Details',['Data ID','Input','Full amount evidence','Processing and other limits','File-observation scope'],[[x['no'],x['identity'],x['size_evidence'],x['limits'],x['properties']['scope']] for x in selected],[8,30,110,110,80])
sheet('Coverage',['Need','Selected Data IDs','Reason','Global evidence','China evidence','Limits','Evidence IDs'],[[x['need'],', '.join(map(str,x['selected_numbers'])),x['reason'],x['global_evidence'],x['china_evidence'],x['limits'],', '.join(x['evidence_ids'])] for x in pub['coverage']],[40,32,75,70,70,100,27])
sheet('Materials',['Material / role','Selected Data IDs','Reason','Limits'],[[x['material'],', '.join(map(str,x['selected_numbers'])),x['reason'],x['limits']] for x in pub['materials']],[44,35,80,100])
sheet('Technology',['Company / role','Sequencer family','Library supplier distinction','Reason for attention','Selected Data IDs','Specific decision','Limits','Evidence IDs'],[[x['company'],x['family'],x['library_supplier'],x['reason'],', '.join(map(str,x['selected_numbers'])),x['selection_reason'],x['limits'],', '.join(x['evidence_ids'])] for x in pub['technologies']],[30,37,42,75,30,85,75,28])
sheet('Evidence',['ID','Source title','View / scope','Status','Actual finding','Limit','Source date','Retrieval date','Public link'],[[x.get(k,'Not recorded') for k in ['id','title','view','status','finding','limit','source_date','retrieved_date','url']] for x in evidence],[24,45,30,40,100,100,30,35,55],full_url_columns=(8,))
# Reuse the accepted archive table construction without running the old producer.
archive=survey['archive'];totals=[]
for frame,title in [('stock','All releases through 30 September 2026'),('rolling12','New releases: 1 October 2025–30 September 2026')]:
 t=archive['frames'][frame];missing=archive['views'][frame]['organism']['missing'][0];totals.append([title,t['run_count'],str(t['known_base_sum']),t['distinct_known_studies'],t['missing_invalid_base_runs'],t['zero_base_runs'],t['missing_study_runs'],missing['run_count'],missing['run_share_pct']])
sheet('Archive totals',['Window','Runs','Reported bases (exact text)','Known distinct studies','Missing/invalid base runs','Zero-base runs','Missing study runs','Missing organism-name runs','Missing organism-name %'],totals,[44,20,29,25,25,23,23,28,25])
for field,title,label in [('strategy','Archive strategy','library_strategy'),('platform','Archive platforms','instrument_platform'),('source','Archive sources','library_source'),('layout','Archive layout','library_layout'),('organism','Archive organisms','scientific_name')]:
 rows=[]
 for frame,title2 in [('stock','Stock'),('rolling12','Annual increment')]:
  for z in archive['views'][frame][field]['rows']:rows.append([title2,z[label] or '(missing)',z['run_count'],str(z['known_base_sum']),z['distinct_known_studies'],z['run_share_pct'],z['reported_base_share_pct'],z['missing_base_runs'],z['missing_study_runs']])
 sheet(title,['Window','Raw archive label','Runs','Reported bases (exact text)','Known distinct studies','Share of all window runs %','Share of all known window bases %','Missing base runs','Missing study runs'],rows,[23,40,20,29,25,28,30,23,23])
joints=[]
for frame,title in [('stock','Stock'),('rolling12','Annual increment')]:
 for z in archive['views'][frame]['platform_model_assay']['rows']:joints.append([title,z['instrument_platform'],z['instrument_model'],z['library_source'],z['library_strategy'],z['run_count'],str(z['known_base_sum']),z['distinct_known_studies'],z['run_share_pct'],z['reported_base_share_pct']])
sheet('Archive joints',['Window','Raw platform','Model','Source','Strategy','Runs','Reported bases (exact text)','Known studies','Window run share %','Window base share %'],joints,[23,25,32,27,27,20,29,23,23,23])
verification=list(csv.DictReader((ROOT/'checksums/verification.tsv').open(),delimiter='\t'))
sheet('Verification',['Data ID','File','Status','File MD5','MD5 source','Expected bytes','Publisher MD5','Checked UTC','Snapshot UTC','Content check','Content check date','Meaning'],[[int(z['Data ID']),z['Filename'],z['Status'],z['File MD5'],z['MD5 source'],int(z['Expected bytes']),z['Publisher MD5'],z['Checked UTC'],z['Snapshot UTC'],z['Content check'],z['Content check date'],z['Meaning']] for z in verification],[9,55,34,36,27,24,36,30,30,32,22,80])
sheet('Read me',['Topic','Meaning'],[['Dataset version',pub['dataset_version']+'; see VERSIONING.md. Verification is dated separately.'], ['Benchmark target', pub['preparation_rules']['gzip_FASTQ']['benchmark_target']+' '+pub['preparation_rules']['gzip_FASTQ']['policy']], ['Membership', str(counts['selected_datasets'])+' datasets in one collection with '+str(counts['source_objects'])+' files. See fq, Files and Reasons for current Data IDs and exact input units.'], ['Amounts', 'Reported sequence bases and source read/spot counts are separate from listed decimal GB/TB. No universal paired multiplier is applied. Exact selected-source totals for Data 6 and Data 8 are unknown; associated-analysis quantities are separate. Source-study support is not a global production norm.'], ['Small input units', str(len(pub['small_input_context']['dataset_ids']))+' complete datasets have less than one decimal GB of listed compressed source data. Sum all ends, runs and chunks before describing dataset size. Uncompressed FASTQ bytes are unmeasured. Small targets, tags, cells, markers and compact genomes can be meaningful workloads. Reasons explains each unit and its limits; no one-GB inclusion floor applies.'], ['Input units', 'Each selected archive input is one complete run; each paired run has two separate files. The BAM and one SINGLE CNGB FASTQ file retain their declared source units. The three CITE components are different library roles, not replicate copies.'], ['Properties', 'Observed prefix properties apply only to the exact matching URLs identified in Files; all other objects are unpreviewed. No whole-library profile, pairing or full-integrity verification is claimed.'], ['References', 'The used reference identities have stable fa IDs and exact versions. Landing pages are not direct FASTA links. Mixture and feature definitions remain unspecified where none was accepted.'], ['Evidence', 'Archive stock/annual and Global/China views retain saved source vintages. Worldwide includes China; hosting is not production. Study counts are not additive, and missing labels remain in denominators.'], ['Conditional preparation', 'Cyclone has size-only verification; exact source yield and SRA byte equivalence are unverified. The ONT BAM needs later export, with exact yield and order fixed. Spatial masks and CITE feature tables support interpretation or custom matching rather than generic lossless FASTQ compression.'], ['Selection field', 'The saved metadata extract lacks library_selection. Separate 14 October separately retrieved run counts have different denominators: stock 44,218,009 and annual 5,872,258. They are not joined to base or study counts.'], ['Maintenance', 'Annual stock plus the preceding twelve months. Replace or remove only for documented issues or useful coverage improvement, recording lost/gained roles and units. No change is a valid outcome.'], ['Validation limit', 'Local package, cell, text, hyperlink and geometry checks are not native Office visual page proof. Download and verification status is recorded separately; no compression benchmark or real BAM export is claimed.']],[26,125])
wb.close();(R/'sheet_data.json').write_text(json.dumps(sheet_data,indent=2,ensure_ascii=False)+'\n');(R/'layout_check.json').write_text(json.dumps({'method':'Configured widths and conservative wrapped-line height estimates; not native Excel/Office rendering','findings':fit,'native_office_rendered':False},indent=2)+'\n');production={'created_utc':datetime.now(timezone.utc).isoformat(),'counts':counts,'sheets':sheet_counts,'report_blocks':len(blocks),'docx_hyperlinks':link_count,'formatting':'OOXML/HTML and xlsxwriter; approximate row-fit checks only','native_office_rendered':False};(R/'production.json').write_text(json.dumps(production,indent=2)+'\n');print(json.dumps(production,indent=2))

with (CAT/'catalogue.csv').open('w',newline='',encoding='utf-8-sig') as handle:
 writer=csv.writer(handle);writer.writerow([tr(v) for v in ['Data ID','Identity','Organism','Method','Sequencer','Manufacturer','Input unit','Reported bases','Listed compressed bytes','Files','Why included','Limits']])
 for x in selected:writer.writerow([tr(v) for v in [x['no'],x['identity'],x['metadata']['organism'],x['metadata']['preparation'],x['metadata']['model'],x['manufacturer'],x['metadata']['unit'],x['metadata']['reported_base_count'],sum(f['listed_bytes'] for f in x['files']),len(x['files']),x['reason'],x['checks_summary']]])
with (CAT/'files.tsv').open('w',newline='',encoding='utf-8') as handle:
 writer=csv.writer(handle,delimiter='\t');writer.writerow([tr(v) for v in ['Data ID','Source run','Role','Filename','URL','Listed bytes','Publisher MD5','Expected verification']])
 for x in selected:
  for f in x['files']:writer.writerow([x['no'],f['run_accession'],tr(f['role']),f['physical_name'],f['url'],f['listed_bytes'],f.get('publisher_md5',''),tr(f['verification_expected'])])
with (CAT/'references.tsv').open('w',newline='',encoding='utf-8') as handle:
 writer=csv.writer(handle,delimiter='\t');writer.writerow([tr(v) for v in ['fa ID','Versioned accession','Name','Proposed FASTA filename','Proposed FASTA URL','Status']])
 for q in pub['references']:writer.writerow([q['no'],q['accession_version'],q['name'],q['download_filename'],q['download_url'],tr(q['download_status'])])
rows=['# '+tr('Dataset catalogue'),'',('[English](../README.md) | [简体中文](../zh-CN/)' if args.language=='en' else '[English](../../README.md) | [简体中文](../README.md)'),'',tr('One collection, dataset version ')+pub['dataset_version']+'. '+tr('Use the report or Reasons sheet for why each dataset was chosen; Files lists every download.'),'','| '+tr('Data ID')+' | '+tr('Dataset')+' | '+tr('Public ID')+' | '+tr('Files')+' | '+tr('Reported bases')+' | '+tr('Download bytes')+' |','|---|---|---|---:|---:|---:|']
for x in selected:rows.append('| '+str(x['no'])+' | '+tr(x['display_name'])+' | '+x['identity']+' | '+str(len(x['files']))+' | '+(format(x['metadata']['reported_base_count'],',') if x['metadata']['reported_base_count'] is not None else tr('Not established'))+' | '+format(sum(f['listed_bytes'] for f in x['files']),',')+' |')
(CAT/'README.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
if args.language=='en':
 strings=set()
 for block in blocks:
  if block['type']=='table':strings.update(block['headers']);strings.update(v for row in block['rows'] for v in row)
  else:strings.add(block['text'])
 for data in sheet_data.values():
  strings.update(data['headers']);strings.update(v for row in data['rows'] for v in row if isinstance(v,str) and not v.startswith(('https://','internal:')))
 (R/'translation_source.json').write_text(json.dumps({v:'' for v in sorted(strings)},ensure_ascii=False,indent=2)+'\n')
