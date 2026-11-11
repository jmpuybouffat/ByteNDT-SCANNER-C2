"""Browser evidence for the C2 level-2 candidate; does not qualify hardware."""
import json
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from level2_document import preserved_payloads

preview = ROOT.parent / 'preview-c2'
evidence = ROOT / 'publication/evidence'
evidence.mkdir(parents=True, exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass

server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(preview)))
Thread(target=server.serve_forever, daemon=True).start()
report = {'scope': 'Software/display review; author visual acceptance remains pending',
          'payload_sha256': preserved_payloads(), 'errors': [], 'poses': []}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True,
        args=['--no-sandbox', '--use-gl=angle', '--use-angle=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'])
    page = browser.new_page(viewport={'width': 1600, 'height': 1200})
    page.on('pageerror', lambda e: report['errors'].append(str(e)))
    page.goto(f'http://127.0.0.1:{server.server_port}/00_OUVRIR_CYCLE_C2_FR_EN.html',
              timeout=120000, wait_until='domcontentloaded')
    page.wait_for_function('window.C2Replay?.shot === 1 && !C2Replay.audit.rendering', timeout=120000)
    scene = page.frame_locator('#scene')
    child = page.locator('#scene').element_handle().content_frame()
    child.wait_for_function('window.C2Scanner && C2AssetsReady', timeout=120000)
    report['initial'] = child.evaluate('C2Scanner.audit')
    assert report['initial']['shells'] == 2 and report['initial']['mobileParts'] == 8
    for shot in [1, 20, 54, 81, 117, 145, 172, 199]:
        page.evaluate('(n) => C2Replay.goto(n)', shot)
        child.wait_for_function('(n) => C2Contact.audit.shot === n', arg=shot, timeout=30000)
        audit = child.evaluate('({scanner:C2Scanner.audit,contact:C2Contact.audit})')
        assert audit['scanner']['contactPositionErrorMm'] < 1e-9
        assert abs(audit['scanner']['rotationDeterminant'] - 1) < 1e-6
        assert not any(audit['scanner']['cutPlanes'])
        assert page.evaluate('C2Replay.audit.rows') == shot
        report['poses'].append({'shot':shot,'scanner':audit['scanner']})
        if shot in [1, 81, 199]:
            child.locator('#stage').screenshot(path=str(evidence / f'C2_N2_context_{shot:03d}.png'))
    page.evaluate('C2Replay.goto(81)')
    child.wait_for_function('C2Contact.audit.shot === 81')
    child.evaluate('C2Scanner.detail()')
    child.locator('#stage').screenshot(path=str(evidence / 'C2_N2_detail_081.png'))
    child.get_by_role('button', name='Éclater le scanner', exact=True).click()
    assert child.evaluate('C2Scanner.audit.exploded')
    child.locator('#stage').screenshot(path=str(evidence / 'C2_N2_exploded_081.png'))
    page.evaluate('C2Replay.setLang("en")')
    child.wait_for_function('document.documentElement.lang === "en"')
    assert child.get_by_role('button', name='Scanner between blades', exact=True).count() == 1
    child.get_by_role('button', name='Assemble scanner', exact=True).click()
    child.evaluate('C2Scanner.context()')
    # Actual operator controls: forward, stop, reverse, stop.
    page.locator('#scannerSpeed').select_option('10')
    start = child.evaluate('C2Scanner.audit.distance')
    page.evaluate('C2ScannerOperator.start(1)')
    child.wait_for_function('(d) => C2Scanner.audit.distance > d + 2', arg=start, timeout=30000)
    page.evaluate('C2ScannerOperator.stop()')
    forward = child.evaluate('C2Scanner.audit')
    assert not forward['running']
    page.evaluate('C2ScannerOperator.start(-1)')
    child.wait_for_function('(d) => C2Scanner.audit.distance < d - 2', arg=forward['distance'], timeout=30000)
    page.evaluate('C2ScannerOperator.stop()')
    reverse = child.evaluate('C2Scanner.audit')
    assert not reverse['running']
    report['motion'] = {'start_mm':start,'after_forward':forward,'after_reverse':reverse}
    page.evaluate('C2Replay.goto(199)')
    child.wait_for_function('C2Contact.audit.shot === 199')
    report['final'] = page.evaluate('({shot:C2Replay.shot,rows:C2Replay.audit.rows,finalVisible:C2Replay.audit.finalVisible})')
    assert report['final']['finalVisible']
    report['navigation'] = []
    for key in ['indications', 'tfm', 'voxel', 'report', 'mechanics', 'guide', 'scan']:
        page.locator(f'#resultNav button[data-pane="{key}"]').click()
        page.wait_for_function('(k) => !document.getElementById("pane-"+k).hidden', arg=key)
        if key in ['tfm', 'voxel']:
            page.wait_for_function('(k) => !!document.getElementById(k).data?.length', arg=key)
        if key == 'report':
            page.wait_for_function('!!document.querySelector("#pane-report iframe").src')
        report['navigation'].append(key)
    page.evaluate('C2Replay.setLang("fr")')
    child.wait_for_function('document.documentElement.lang === "fr"')
    page.screenshot(path=str(evidence / 'C2_N2_application.png'), full_page=True)
    browser.close()
server.shutdown()
assert not report['errors'], report['errors']
(evidence / 'CONTROLE_C2_N2_R01.json').write_text(json.dumps(report, indent=2))
print(json.dumps({'status':'passed','poses':len(report['poses']),'errors':report['errors'],'final':report['final']}))
