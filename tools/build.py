import csv,copy,html,json,math,re,shutil,sys,zipfile
from pathlib import Path
from datetime import datetime,timezone
from xml.sax.saxutils import escape
import argparse
import xlsxwriter
from document_format import write_documents
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
def tr(value):return translations.get(value,value) if isinstance(value,str) else value
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
h('Building a public FASTQ compression benchmark')
p('Global and China evidence, one public collection and preparation requirements • 19 October 2026')
p('This report describes a public collection for lossless FASTQ compression tests. Public archive distributions and documented applied or research uses establish workload priorities; the selection principles then connect those needs to concrete inputs.')
p('The purpose is to test useful kinds of input at representative real-world amounts. A complete named library may contain several paired runs; a documented flow-cell, barcode or lane output can also be a natural delivery unit. There is no rule that smaller inputs are preferable, or that every biological sample must include every preparation. Source-study quantities support the selected examples but do not establish market-wide production norms. Data IDs identify the current inputs in the workbook and report.')
p('A FASTQ record stores a read name, sequence letters and one encoded quality character per base. Lossless decompression must restore the exact chosen input bytes, including names, sequences, qualities, order and formatting. A 150-base read has 150 quality positions, while a file can use four or 39 distinct quality characters across those positions. Frequency also matters: modal share means the percentage of inspected quality positions occupied by the most common quality character. These summaries do not measure compressor performance.')
p(pub['preparation_rules']['gzip_FASTQ']['benchmark_target'])
p('The NCBI Sequence Read Archive (SRA) and European Nucleotide Archive (ENA) organize public sequencing submissions into projects, samples, experiments and runs. Archive counts describe public submissions, not all production. One dataset here is a declared complete input unit, with every run, mate or chunk listed separately. Some compressors encode matching sequence segments through reference positions and differences, so a reference’s identity, version and match to the reads can affect representation and compression. Not every compressor requires a reference.')
p('Four evidence views inform the choices: worldwide archives, worldwide applied/business use, China-hosted archives and China applied/business use. Worldwide includes China, so the views are not added. The archive cutoff is 30 September 2026. The survey findings below retain their stated source and retrieval dates.')
for b in copy.deepcopy(json.load(open(ROOT/'evidence/survey_report_blocks.json'))):
 if 'text' in b:b['text']=b['text'].replace('](benchmark_dataset.xlsx)','](../catalogue/benchmark_dataset.xlsx)').replace('](survey_discovery_register.csv)','](../evidence/survey_discovery_register.csv)')
 blocks.append(b)
h('How workloads and particular inputs were chosen')
p('Archive exposure and publicly documented use establish important workflows; credible deployed or committed technology directions may also matter despite few public deposits. A particular input then needs a clear public identity, preparation, useful role, reference relationship and appropriate sequence amount. Different business purposes do not automatically require different files. Several needs can share an input, while distinct tagged, transformed, single/paired and raw/consensus representations may justify separate examples.')
p('Representative amount is assessed in the relevant unit and purpose. The Renan polishing library and CHO genomic library include all their documented outputs. Each CITE component includes all four outputs of its own experiment, while ADT, mRNA and HTO remain separate. The Revio input is an explicitly identified barcode-specific cell output; it is not silently called an entire cell or all libraries for that person. A real run alone does not establish a universal production norm, and raw bases do not certify usable mapped depth.')
p('Select public examples by these documented conditions, not compressor results, weighted scores, a desired entry count, a species checklist or one file per manufacturer. Preserve useful older conditions when their role is supported. The public-release cutoff is 30 September 2026; release date is distinct from sequencing and basecalling dates. No full source/reference data were downloaded, exported or benchmarked during packaging. Saved nonrandom prefix observations are scoped individually.')
p('Instrument manufacturer, sequencer family and library supplier are separate fields. Illumina and MGI short-read systems commonly produce parallel, relatively fixed-length reads; ONT nanopore and PacBio single-molecule systems produce long-read representations. These are often called second- and third-generation technologies respectively. CycloneSEQ is an MGI nanopore family despite the archive’s broad BGISEQ label. A 10x, CITE or spatial library label does not identify the sequencer or prove its exact chemistry.')
table(['Field','Meaning and selection consequence'],[['Species/material','Human/model/crop/microbial references and mixed communities differ. Economic value alone does not establish sequencing demand; actual sample/reference agreement is a separate check.'],['Source','The broad material label: genomic, transcript-derived, community or another category. A broad archive label may require documentary clarification.'],['Strategy and selection','Strategy describes intended sampling; selection is a preparation label. WGS, RNA, exome/capture, amplicon, ATAC, ChIP, CUT&RUN and Hi-C are not interchangeable. Reproductive/CNV purpose alone does not prove capture or amplicon sampling.'],['Layout and components','Single/paired labels are distinct from library completeness. All mate ends, tags and chunks are explicit. An entire logical library may comprise several runs.'],['Read lengths, quality and headers','Only exact matched saved prefix observations establish measured properties. Unpreviewed objects are identified individually in Files. Prefixes are nonrandom, not whole-file distributions; similar alphabets need not have similar frequencies.'],['Reference and processing','Fix versioned reference identities and later FASTQ preparation/order. Raw CLR, consensus, trimming, filtering, merging, conversion and supplied constant qualities can change the byte representation. Interpretation masks/features are not automatic requirements for generic lossless compression.']])
p('Reported read counts retain the source convention; no universal multiplier converts them to paired reads. Reported sequence bases are shown alongside counts. Known selected-source totals sum to '+format(counts['known_reported_sequence_bases'],',')+' bases across '+str(counts['source_format_dataset_counts']['FASTQ']-1)+' FASTQ inputs with known yield. Exact sequence-base totals are unavailable for Data 6 (BAM) and Data 8 (CNGB FASTQ), both excluded from this sum; associated analysis or SRA yields are not substituted as selected-source totals.')
p('Saved profiles are reused only for exact matched file URLs. Observed properties apply only to the exact files identified in Files; they do not establish profiles for other files in the same library. The Files sheet identifies which exact objects have saved evidence. No whole-file integrity, pairing or representative distribution has been measured here. Publisher MD5 values are listed where already recorded, never claimed computed.')
h('Coverage served and needs still open')
for x in pub['coverage']:
 h(x['need'],2);p(x['reason']+' Data IDs: '+', '.join(map(str,x['selected_numbers']))+'. '+x['limits']+' '+cites(x['evidence_ids']))
h('Material and reference choices')
for x in pub['materials']:p(x['material']+'. '+x['reason']+' Data IDs: '+', '.join(map(str,x['selected_numbers']))+'. '+x['limits'])
h('Technology choices and remaining inquiries')
for x in pub['technologies']:p(x['company']+' — '+x['family']+'. '+x['reason']+' '+x['selection_reason']+' '+x['limits']+' '+('Selected Data IDs: '+', '.join(map(str,x['selected_numbers']))+'. ' if x.get('selected_numbers') else 'No selected public input for this scoped technology need. ')+cites(x['evidence_ids']))
h('The selected public inputs')
p(f"This collection supplies useful examples of common public sequencing workloads and publicly supported applied or research uses. It contains {counts['selected_datasets']} datasets: {counts['source_format_dataset_counts']['FASTQ']} with listed FASTQ routes and one BAM source requiring later FASTQ conversion. Its {counts['source_objects']} physical source objects total {counts['listed_source_bytes']:,} listed bytes ({counts['listed_source_bytes']/1e12:.3f} decimal TB). Source sizes are not uncompressed FASTQ sizes, market shares or benchmark results. The count follows individual decisions; it is not a quota or proven minimum.")
p('The [workbook](../catalogue/benchmark_dataset.xlsx) has one dataset row per Data ID in fq, every physical object in Files, and versioned reference proposals in fa. Reasons, Coverage, Materials, Technology carry the supporting detail. Sequence amounts below are reported bases, separately from listed compressed-source sizes. The entries identify the intended test inputs and the preparation still needed.')
h('Why some input units are small',2)
p(str(len(pub['small_input_context']['dataset_ids']))+' of the '+str(counts['selected_datasets'])+' complete input units have less than one decimal GB of listed compressed source data. This count sums all selected ends, runs and chunks of each dataset. Listed gzip bytes, reported sequence bases and read/spot counts are different measures; the uncompressed FASTQ byte counts have not been measured. One GB is a descriptive boundary, not an inclusion floor.')
p('Small targets, reduced-representation libraries, short RNA, individual cells, sample tags and community markers can produce meaningful small files. A compact bacterial genome can also have substantial sequence coverage within a sub-GB compressed output. Each entry below connects its sample, library or delivered component to relevant source-workflow amounts. For example, the complete eight-file HTO component contains 1,566,671,480 reported bases in 687,740,927 listed compressed bytes. Source-cohort medians provide context, not a pass/fail threshold or universal production norm.')
p('A processed or demultiplexed FASTQ can represent a real research or production workload. Describe its stage where documented; an unknown stage does not prove failure or incompleteness. Source-unit, amount and useful workload evidence support the small inputs here, with remaining uncertainties stated individually. No repetition, padding or forced combination is used to make a small input larger.')
for x in selected:
 n=x['no'];m=x['metadata'];h('Data '+str(n)+'. '+m['organism']+' — '+m['model'],2);p(x['reason']);p('Public source: '+runlinks(x)+'. Input unit: '+m['unit']+'.')
 p('Reported amount: '+fmtbase(m['reported_base_count'])+'. Listed source objects: '+str(len(x['files']))+'; '+fmtbytes(sum(f['listed_bytes'] for f in x['files']))+'. '+reftext(x)+'.')
 p('Size evidence: '+x['size_evidence'])
 if x.get('unit_evidence_ids'):p('Unit and processing sources: '+cites(x['unit_evidence_ids']))
 p('Properties: '+x['properties']['scope']+' Lengths: '+x['properties']['lengths']+'. Quality characters: '+x['properties']['quality_characters']+'.')
 p('Limits and preparation: '+x['limits']+' '+x['preparation'])
h('Versioned references and later FASTQ preparation')
p('The '+str(len(pub['references']))+' used reference identities have the fa IDs listed below. Renan GCA_937894285.1 is the proposed same-cultivar assembly. Landing pages are labelled separately from direct gzip FASTA routes. No reference body was acquired or verified. Same-species does not prove strain, cultivar, transcript or target matching. The human/fly normalization-reference proposal is not pure fly genomic coverage. Marker and community inputs do not receive invented single-genome FASTAs.')
for q in pub['references']:p('fa ID '+str(q['no'])+': '+q['organism']+' — '+q['name']+' / ['+q['accession_version']+']('+q['route']+'). '+q['route_type']+'. '+q['relationship'])
p(pub['auxiliary_assets'])
p('Before testing, acquire the exact listed objects through a usable public route, verify full-file integrity and component relationships, and fix the exact prepared FASTQ bytes. Account for reference bytes and preparation consistently across compressors. Preserve original versus prepared identities. This package specifies selection and later preparation. Saved prefix observations are scoped individually; no whole-collection verification or compression results are available. Packaging did not process real source data.')
p(pub['preparation_rules']['gzip_FASTQ']['policy']+' '+pub['preparation_rules']['gzip_FASTQ']['receipt']+' See the [preparation commands](preparation.md).')
p('Data 6 is a BAM source only. Its mapped SUP flow-cell analysis reports 153,264,463,825 bases and 8,155,127 reads, but these are not verified as the exact selected BAM/export yield. The pinned, unexecuted [preparation rule](preparation.md) uses SAMtools 1.22/htslib 1.22, natural QNAME sorting, unpaired primary records, stored qualities and a stop on missing primary qualities. It records exact source/output hashes and options when run. Prepared order is not native instrument order. Losslessness applies to the resulting FASTQ, not BAM tags/alignments.')
p('Data 8: '+by[8]['metadata']['unit']+'. '+by[8]['limits']+' Properties: '+by[8]['properties']['scope']+' Lengths: '+by[8]['properties']['lengths']+'.')
p('Data 22 has documentary HiFi identity and an exact source/yield join. Its filename containing _subreads is an archive representation name, not independent proof of raw-subread or consensus processing. Actual qualities/headers remain unpreviewed. Spatial masks/coordinates and CITE feature/barcode definitions are needed for particular interpretation or custom reference matching, not generic byte-identical compression. Taxonomy tables are auxiliary, not a genomic reference or an admission criterion.')
h('Exact files for multi-run and chunked inputs')
p('Each row is one exact physical object. Names and URLs are verbatim listed metadata. Keep the shown run boundaries and mate/chunk roles; no concatenated filename or combined archive accession has been fabricated. The Files worksheet contains the same detail for all '+str(counts['source_objects'])+' objects.')
for x in selected:
 if len(x['run_accessions'])>1 or len(x['files'])>1 and all('chunk' in f['role'].lower() for f in x['files']):
  label=x['display_name']
  h('Data '+str(x['no'])+' — '+label+' — '+str(len(x['files']))+' files',2)
  table(['Run / end or chunk','Exact physical filename','Full listed URL'],[[f['run_accession']+'; '+f['role'],f['physical_name'],'['+f['url']+']('+f['url']+')'] for f in x['files']])
h('Annual maintenance')
p('Update annually using the latest completed September: stock through the cutoff and the preceding 12-month public-release increment. Reuse unchanged audited evidence and refresh consequential applied-use/deployment claims. Reassess useful workload/material/library/technology/reference conditions and representative input amounts. Add, replace or remove only for documented data issues or useful coverage improvement, recording lost and gained roles and exact input units. No change is a valid outcome. This collection is not a proven minimum and has no target count.')
# Save readable text and the exact document blocks used by the OOXML writer.
md=[]
for b in blocks:
 if b['type']=='table':md+=['| '+' | '.join(b['headers'])+' |','| '+' | '.join('---' for _ in b['headers'])+' |']+['| '+' | '.join(str(c).replace('|',' / ').replace('\n','<br>') for c in row)+' |' for row in b['rows']]+['']
 else:md+=['#'*int(b['type'][1:])+' '+b['text'] if b['type'].startswith('h') else b['text'],'']
if args.language!='en':
 for block in blocks:
  if block['type']=='table':block['headers']=[tr(v) for v in block['headers']];block['rows']=[[tr(v) for v in row] for row in block['rows']]
  else:block['text']=tr(block['text']).replace('../evidence/','../../evidence/')
md=[]
for block in blocks:
 if block['type']=='table':md+=['| '+' | '.join(block['headers'])+' |','| '+' | '.join('---' for _ in block['headers'])+' |']+['| '+' | '.join(str(c).replace('|',' / ').replace('\n','<br>') for c in row)+' |' for row in block['rows']]+['']
 else:md+=['#'*int(block['type'][1:])+' '+block['text'] if block['type'].startswith('h') else block['text'],'']
(OUT/'report.md').write_text('\n'.join(md),encoding='utf-8')
(R/'report_blocks.json').write_text(json.dumps(blocks,indent=2,ensure_ascii=False)+'\n')
link_count=write_documents(blocks,OUT)
evidence=json.load(open(ROOT/'evidence/evidence_register.json'))
# Human workbook layout follows the accepted fa/fq/Files arrangement.
wb=xlsxwriter.Workbook(CAT/'benchmark_dataset.xlsx');wb.set_properties({'title':'Public FASTQ compression benchmark','subject':'One '+str(counts['selected_datasets'])+'-entry collection; 19 October 2026','author':''})
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
  first.setdefault(x['no'],len(file_rows)+2);pr=f['properties'];md5=f.get('publisher_md5','');recorded=bool(re.fullmatch('[0-9a-fA-F]{32}',md5));file_rows.append([x['no'],f['run_accession'],f['role'],f['physical_name'],f['format'],f['listed_bytes'],md5 if recorded else 'Not recorded','Publisher-listed; not computed' if recorded else 'Not recorded; not computed',f['url'],pr['lengths'],pr['quality_characters'],pr['quality_ascii'],pr['headers'],pr['scope']])
reasonrow={x['no']:i for i,x in enumerate(selected,2)};fq_rows=[]
for x in selected:
 m=x['metadata'];pr=x['properties'];n=x['no'];organization=m['layout']+'; '+str(len(x['run_accessions']))+' run(s), '+str(len(x['files']))+' file(s). '+m['unit'];fq_rows.append([n,m['study'],m['sample'],m['experiment'],'\n'.join(x['run_accessions']) if x['source_format']!='BAM' else 'PAW70337 SUP BAM',x['source_url'],m['organism'],m['common_name'],m['source'],m['preparation'],m['strategy'],x['technology'],m['model'],x['manufacturer'],organization,pr['quality_characters'],pr['quality_ascii'],pr['lengths'],int(m['reported_read_count']) if str(m['reported_read_count']).isdigit() else m['reported_read_count'],m['reported_base_count'] if m['reported_base_count'] is not None else 'Not established for selected source',round(sum(f['listed_bytes'] for f in x['files'])/1e9,6),"internal:'Files'!A"+str(first[n]),m['first_public'],reftext(x),m['named_sample'],"internal:'Reasons'!A"+str(reasonrow[n])])
headers=['Data ID','Project','Sample','Experiment(s)','Run(s) / public source','Source link','Scientific species / material','Common name','Sample / library source','Preparation','What was sequenced','Short / long reads','Sequencer','Manufacturer','Ends / file organization','Quality characters seen in saved prefix','Character codes seen (ASCII)','Read lengths seen (bases)','Archive-reported read/spot count','Reported sequence bases','Listed file size (decimal GB)','Files / listed MD5','First-public date / evidence','Reference','Named sample/library (not verified truth)','Why included / document entry']
fq=sheet('fq',headers,fq_rows,[10,18,19,20,25,14,28,20,24,27,26,25,27,24,43,30,26,38,25,25,21,16,27,37,29,20],start=1);fq.activate()
for left,right,label in [(0,5,'Identity — '+str(counts['selected_datasets'])+' datasets'),(6,8,'Sample information'),(9,13,'Sequencing'),(14,25,'File information / reported amounts')]:fq.merge_range(0,left,0,right,label,band)
fq.set_row(0,29)
sheet('Files',['Data ID','Run / source','End or chunk / role','Exact physical filename','Supplied format','Listed bytes','Publisher MD5','MD5 status','Full listed URL','Saved prefix lengths','Saved quality characters','Saved ASCII range','Header observation','Properties scope'],file_rows,[10,25,37,65,20,23,36,32,80,48,38,35,35,80],full_url_columns=(8,))
sheet('Reasons',['Data ID','Current input','Why this input','Representative amount / unit evidence','Limits','Preparation','Properties scope'],[[x['no'],'; '.join(x['run_accessions']),x['reason'],x['size_evidence'],x['limits'],x['preparation'],x['properties']['scope']] for x in selected],[8,30,100,110,100,70,65])
sheet('Coverage',['Need','Selected Data IDs','Reason','Global evidence','China evidence','Limits','Evidence IDs'],[[x['need'],', '.join(map(str,x['selected_numbers'])),x['reason'],x['global_evidence'],x['china_evidence'],x['limits'],', '.join(x['evidence_ids'])] for x in pub['coverage']],[40,32,75,70,70,100,27])
sheet('Materials',['Material / role','Selected Data IDs','Reason','Limits'],[[x['material'],', '.join(map(str,x['selected_numbers'])),x['reason'],x['limits']] for x in pub['materials']],[44,35,80,100])
sheet('Technology',['Company / role','Sequencer family','Library supplier distinction','Reason for attention','Selected Data IDs','Specific decision','Limits','Evidence IDs'],[[x['company'],x['family'],x['library_supplier'],x['reason'],', '.join(map(str,x['selected_numbers'])),x['selection_reason'],x['limits'],', '.join(x['evidence_ids'])] for x in pub['technologies']],[30,37,42,75,30,85,75,28])
sheet('Evidence',['ID','Source title','View / scope','Status','Actual finding','Limit','Source date','Retrieval date','Public link'],[[x.get(k,'Not recorded') for k in ['id','title','view','status','finding','limit','source_date','retrieved_date','url']] for x in evidence],[24,45,30,40,100,100,30,35,55],full_url_columns=(8,))
# Reuse the accepted archive table construction without running the old producer.
archive=survey['archive'];totals=[]
for frame,title in [('stock','Public stock through30September2026'),('rolling12','First public1October2025–30September2026')]:
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
sheet('Read me',['Topic','Meaning'],[['Benchmark target', pub['preparation_rules']['gzip_FASTQ']['benchmark_target']+' '+pub['preparation_rules']['gzip_FASTQ']['policy']], ['Membership', str(counts['selected_datasets'])+' datasets in one collection with '+str(counts['source_objects'])+' physical objects. See fq, Files and Reasons for current Data IDs and exact input units.'], ['Amounts', 'Reported sequence bases and source read/spot counts are separate from listed decimal GB/TB. No universal paired multiplier is applied. Exact selected-source totals for Data 6 and Data 8 are unknown; associated-analysis quantities are separate. Source-study support is not a global production norm.'], ['Small input units', str(len(pub['small_input_context']['dataset_ids']))+' complete logical datasets have less than one decimal GB of listed compressed source data. Sum all ends, runs and chunks before describing dataset size. Uncompressed FASTQ bytes are unmeasured. Small targets, tags, cells, markers and compact genomes can be meaningful workloads. Reasons explains each unit and its limits; no one-GB inclusion floor applies.'], ['Input units', 'Renan: three paired runs/six files. Each CITE component: four outputs/eight files. CHO: two paired runs/four files. Preserve run boundaries. Cyclone is one SINGLE FASTQ file, not paired mates or two chunks.'], ['Properties', 'Observed prefix properties apply only to the exact matching URLs identified in Files; all other objects are unpreviewed. No whole-library profile, pairing or full-integrity verification is claimed.'], ['References', 'The used reference identities have stable fa IDs and exact versions. Landing pages are not direct FASTA links. Mixture and feature definitions remain unspecified where none was accepted.'], ['Evidence', 'Archive stock/annual and Global/China views retain saved source vintages. Worldwide includes China; hosting is not production. Study counts are not additive, and missing labels remain in denominators.'], ['Conditional preparation', 'Cyclone has size-only verification; exact source yield and SRA byte equivalence are unverified. The ONT BAM needs later export, with exact yield and order fixed. Spatial masks and CITE feature tables support interpretation or custom matching rather than generic lossless FASTQ compression.'], ['Selection field', 'The frozen projection lacks library_selection. Separate 14 October run-only marginals have different denominators: stock 44,218,009 and annual 5,872,258. They are not base/study joints.'], ['Maintenance', 'Annual stock plus the preceding twelve months. Replace or remove only for documented issues or useful coverage improvement, recording lost/gained roles and units. No change is a valid outcome.'], ['Validation limit', 'Local package, cell, text, hyperlink and geometry checks are not native Office visual page proof. No full source/reference acquisition, export or benchmark occurred during packaging.']],[26,125])
wb.close();(R/'sheet_data.json').write_text(json.dumps(sheet_data,indent=2,ensure_ascii=False)+'\n');(R/'layout_check.json').write_text(json.dumps({'method':'Configured widths and conservative wrapped-line height estimates; not native Excel/Office rendering','findings':fit,'native_office_rendered':False},indent=2)+'\n');production={'created_utc':datetime.now(timezone.utc).isoformat(),'counts':counts,'sheets':sheet_counts,'report_blocks':len(blocks),'docx_hyperlinks':link_count,'formatting':'OOXML/HTML and xlsxwriter; approximate row-fit checks only','native_office_rendered':False};(R/'production.json').write_text(json.dumps(production,indent=2)+'\n');print(json.dumps(production,indent=2))

with (CAT/'catalogue.csv').open('w',newline='',encoding='utf-8-sig') as handle:
 writer=csv.writer(handle);writer.writerow([tr(v) for v in ['Data ID','Identity','Organism','Method','Sequencer','Manufacturer','Input unit','Reported bases','Listed compressed bytes','Files','Why included','Limits']])
 for x in selected:writer.writerow([tr(v) for v in [x['no'],x['identity'],x['metadata']['organism'],x['metadata']['preparation'],x['metadata']['model'],x['manufacturer'],x['metadata']['unit'],x['metadata']['reported_base_count'],sum(f['listed_bytes'] for f in x['files']),len(x['files']),x['reason'],x['limits']]])
with (CAT/'files.tsv').open('w',newline='',encoding='utf-8') as handle:
 writer=csv.writer(handle,delimiter='\t');writer.writerow([tr(v) for v in ['Data ID','Source run','Role','Filename','URL','Listed bytes','Publisher MD5','Expected verification']])
 for x in selected:
  for f in x['files']:writer.writerow([x['no'],f['run_accession'],tr(f['role']),f['physical_name'],f['url'],f['listed_bytes'],f.get('publisher_md5',''),tr(f['verification_expected'])])
with (CAT/'references.tsv').open('w',newline='',encoding='utf-8') as handle:
 writer=csv.writer(handle,delimiter='\t');writer.writerow([tr(v) for v in ['fa ID','Versioned accession','Name','Proposed FASTA filename','Proposed FASTA URL','Status']])
 for q in pub['references']:writer.writerow([q['no'],q['accession_version'],q['name'],q['download_filename'],q['download_url'],tr(q['download_status'])])
rows=['# '+tr('Dataset catalogue'),'',('[English](../README.md) | [简体中文](../zh-CN/)' if args.language=='en' else '[English](../../README.md) | [简体中文](../README.md)'),'',tr('One collection. Read the full report and workbook for individual reasons, units and preparation limits.'),'','| '+tr('Data ID')+' | '+tr('Identity')+' | '+tr('Input unit')+' | '+tr('Reported bases')+' | '+tr('Listed compressed bytes')+' |','|---|---|---|---:|---:|']
for x in selected:rows.append('| '+str(x['no'])+' | '+x['identity']+' | '+tr(x['metadata']['unit'])+' | '+(format(x['metadata']['reported_base_count'],',') if x['metadata']['reported_base_count'] is not None else tr('Not established'))+' | '+format(sum(f['listed_bytes'] for f in x['files']),',')+' |')
(CAT/'README.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
if args.language=='en':
 strings=set()
 for block in blocks:
  if block['type']=='table':strings.update(block['headers']);strings.update(v for row in block['rows'] for v in row)
  else:strings.add(block['text'])
 for data in sheet_data.values():
  strings.update(data['headers']);strings.update(v for row in data['rows'] for v in row if isinstance(v,str) and not v.startswith(('https://','internal:')))
 (R/'translation_source.json').write_text(json.dumps({v:'' for v in sorted(strings)},ensure_ascii=False,indent=2)+'\n')
