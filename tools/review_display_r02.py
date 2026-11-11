"""Regression check for assembled replay, exploded context and UT contrast."""
import sys,json
from pathlib import Path
from threading import Thread
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from level2_document import preserved_payloads
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT.parent/'preview-c2')))
Thread(target=server.serve_forever,daemon=True).start()
out=ROOT/'publication/evidence';report={'release':'N2-R02','payload_sha256':preserved_payloads(),'errors':[],'checks':[]}
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
  page=browser.new_page(viewport={'width':1400,'height':1100});page.on('pageerror',lambda e:report['errors'].append(str(e)))
  page.goto(f'http://127.0.0.1:{server.server_port}/00_OUVRIR_CYCLE_C2_FR_EN.html',wait_until='domcontentloaded',timeout=120000)
  page.wait_for_function('window.C2Replay && !C2Replay.audit.rendering',timeout=120000)
  child=page.locator('#scene').element_handle().content_frame();child.wait_for_function('window.C2Scanner',timeout=120000)
  for n in [1,81,199]:
   page.evaluate('(n)=>C2Replay.goto(n)',n);child.wait_for_function('(n)=>C2Contact.audit.shot===n',arg=n,timeout=30000)
   a=child.evaluate('C2Scanner.audit');assert a['release']=='N2-R02' and a['contactPositionErrorMm']<1e-9 and not a['exploded']
   assert a['liveShotSize']==6 and a['rayOpacity']==.62
  print('Poses and UT contrast passed',flush=True)
  page.evaluate('C2Replay.goto(81)');child.wait_for_function('C2Contact.audit.shot===81')
  child.evaluate('C2Scanner.detail()')
  child.locator('#stage').screenshot(path=str(out/'C2_N2_R02_detail_081.png'))
  child.locator('#c2UTContrast').uncheck();assert child.evaluate('C2Scanner.audit.liveShotSize')==3
  child.locator('#c2UTContrast').check();assert child.evaluate('C2Scanner.audit.liveShotSize')==6
  child.get_by_role('button',name='Éclater le scanner',exact=True).click()
  a=child.evaluate('C2Scanner.audit');assert a['exploded'] and not any(a['neighboursShown'])
  assert 'ÉCLATÉE' in child.locator('#c2DisplayRevision').inner_text()
  child.locator('#stage').screenshot(path=str(out/'C2_N2_R02_exploded_081.png'))
  page.locator('#play').click();child.wait_for_function('!C2Scanner.audit.exploded && C2Contact.audit.gliding',timeout=30000)
  assert child.get_by_role('button',name='Éclater le scanner',exact=True).is_disabled()
  assert all(child.evaluate('C2Scanner.audit.neighboursShown'))
  child.wait_for_function('C2Scanner.audit.phase>80',timeout=30000)
  page.locator('#play').click();child.wait_for_function('!C2Contact.audit.gliding',timeout=30000)
  report['checks']+=['regular playback assembles scanner','exploded context hides neighbours','exploded mode labelled','explosion disabled during playback','UT size/opacity toggle','contact unchanged at 1/81/199']
  print('Regular playback and exploded regression passed',flush=True)
  page.evaluate('C2Replay.setLang("en")');child.wait_for_function('document.documentElement.lang==="en"')
  assert child.get_by_text('Enhanced UT contrast',exact=True).count()==1
  page.evaluate('C2Replay.goto(199)');child.wait_for_function('C2Contact.audit.shot===199')
  for key in ['tfm','voxel']:
   page.locator(f'#resultNav button[data-pane="{key}"]').click()
   page.wait_for_function('(k)=>!document.getElementById("pane-"+k).hidden && !!document.getElementById(k).data?.length',arg=key)
   page.locator('#'+key).screenshot(path=str(out/f'C2_N2_R02_{key}.png'))
  report['checks']+=['FR/EN','TFM/voxel routes render']
  browser.close()
 assert not report['errors'],report['errors']
 (out/'CONTROLE_AFFICHAGE_N2_R02.json').write_text(json.dumps(report,indent=2))
 print(json.dumps(report['checks']),flush=True)
finally:server.shutdown()
