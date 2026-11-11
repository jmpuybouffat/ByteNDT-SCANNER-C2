"""Build the editable publication documents from their Markdown sources.
Requires python-docx. No application data or geometry is modified.
"""
from pathlib import Path
import posixpath,re
from urllib.parse import quote
from docx import Document
from docx.shared import Inches,Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parents[1]
PREFIX='https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/blob/publication/byte-ndt-dossier-01/'
AUTHORS='Jean-Michel Puybouffat; Fabien Dedieu; Tumelo Machaha'

def target_url(url,source):
 if re.match(r'https?://',url):return url
 path=posixpath.normpath(str(source.relative_to(ROOT.parent).parent)+'/'+url)
 return PREFIX+quote(path,safe='/#')

def inline(paragraph,text,source):
 pattern=r'\[([^]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`'
 offset=0
 for m in re.finditer(pattern,text):
  if m.start()>offset:paragraph.add_run(text[offset:m.start()])
  if m[1]:
   link=OxmlElement('w:hyperlink');rid=paragraph.part.relate_to(target_url(m[2],source),'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True);link.set(qn('r:id'),rid)
   run=OxmlElement('w:r');props=OxmlElement('w:rPr');color=OxmlElement('w:color');color.set(qn('w:val'),'08698C');props.append(color);run.append(props);t=OxmlElement('w:t');t.text=m[1];run.append(t);link.append(run);paragraph._p.append(link)
  elif m[3]:paragraph.add_run(m[3]).bold=True
  else:
   run=paragraph.add_run(m[4]);run.font.name='Consolas';run.font.size=Pt(9)
  offset=m.end()
 if offset<len(text):paragraph.add_run(text[offset:])

def add_source(doc,path):
 lines=path.read_text().splitlines();i=0;code=False
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('```'):code=not code;i+=1;continue
  if line.startswith('|') and not code:
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',c) for c in cells):rows.append(cells)
    i+=1
   if rows:
    table=doc.add_table(rows=0,cols=len(rows[0]));table.style='Light Shading Accent 1'
    for cells in rows:
     for cell,value in zip(table.add_row().cells,cells):inline(cell.paragraphs[0],value,path)
   continue
  if line.startswith('#') and not code:
   level=len(line)-len(line.lstrip('#'));paragraph=doc.add_heading(level=min(level,3));inline(paragraph,line.lstrip('#').strip(),path)
  elif line.startswith('- ') and not code:inline(doc.add_paragraph(style='List Bullet'),line[2:],path)
  elif re.match(r'^\d+\. ',line) and not code:inline(doc.add_paragraph(style='List Number'),re.sub(r'^\d+\. ','',line),path)
  elif line=='---':doc.add_paragraph('—')
  else:
   paragraph=doc.add_paragraph();inline(paragraph,line,path)
   if code:
    for run in paragraph.runs:run.font.name='Consolas';run.font.size=Pt(9)
  i+=1

def build(name,files,title):
 doc=Document();section=doc.sections[0];section.top_margin=section.bottom_margin=Inches(.75)
 style=doc.styles['Normal'];style.font.name='Calibri';style.font.size=Pt(11);style.paragraph_format.space_after=Pt(6)
 doc.core_properties.author=AUTHORS;doc.core_properties.title=title;doc.core_properties.subject='BYTE NDT Living Engineering — working draft 01';doc.core_properties.keywords='BYTE NDT; living engineering; digital twin; ultrasonic testing; C1; C2'
 section.header.paragraphs[0].text='BYTE NDT — Living Engineering | Version de travail 01'
 footer=section.footer.paragraphs[0];footer.text='11 novembre 2026 | '
 field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
 for index,file in enumerate(files):
  if index:doc.add_page_break()
  add_source(doc,ROOT/file)
 doc.save(ROOT/name)
 print(name)

if __name__=='__main__':
 build('BYTE_NDT_DOSSIER_4_APPLICATIONS_V01.docx',[
  'README.md','CADRAGE_INGENIERIE_VIVANTE_FR.md','PARCOURS_DE_DEMONSTRATION.md',
  '01_C1_AUBE/README.md','02_C1_SCANNER/README.md','03_C2_AUBE/README.md','04_C2_SCANNER/README.md',
  'VERSIONS_ET_VALIDATION.md','FIGURES_ET_PREUVES.md','ANNEXES_SCIENTIFIQUES.md',
  'ATELIER_ET_REALITE_VIRTUELLE.md','ANNEXE_E_URL_APPLICATIONS_FR_EN.md'],
  'BYTE NDT — Dossier des quatre applications et préparation de publication')
 build('BYTE_NDT_LIVING_ENGINEERING_DRAFT_01_EN.docx',[
  'MANUSCRIPT_DRAFT_01_EN.md','ANNEXE_E_URL_APPLICATIONS_FR_EN.md'],
  'BYTE NDT Living Engineering — First international manuscript draft')
