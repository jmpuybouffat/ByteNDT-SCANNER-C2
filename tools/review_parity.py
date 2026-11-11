"""Check the complete C1 interface is represented in the C2 candidate.

Expects the accepted Scanner C1 checkout at ../scanner-c1. Requires numpy.
This is a structural check; browser behaviour is checked separately.
"""
import base64
import gzip
import json
import re
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from level2_document import build_document

c1 = (ROOT.parent/'scanner-c1/cycle_complet/00_OUVRIR_CYCLE_C1_FR_EN.html').read_text().replace('C1','C2')
c2 = build_document(embedded=False)
report = {'reference':'Scanner C1 R06 584db386', 'candidate':'Scanner C2 N2-R01',
          'result_panes':{}, 'operator_controls':{}, 'entrypoint_sections':{}}
for key in ['scan','indications','tfm','voxel','report','mechanics','guide']:
    report['result_panes'][key]={'c1':("'"+key+"'") in c1,'c2':("'"+key+"'") in c2}
for key in ['scannerOperator','scannerReverse','scannerStop','scannerForward','scannerSpeed',
            'scannerResolution','scannerDistance','scannerCount','scannerClock']:
    report['operator_controls'][key]={'c1':key in c1,'c2':key in c2}
a1=(ROOT.parent/'scanner-c1/app.py').read_text()
a2=(ROOT/'level2_app.py').read_text()
for key in ['procedure_language','st.download_button','REFERENCE_COMMANDE.json','maquette_etude',
            'NOTICE_BATI','PROCEDURE_EXAMEN','CONCEPT_COQUES']:
    report['entrypoint_sections'][key]={'c1':key in a1,'c2':key in a2}
for section in ['result_panes','operator_controls','entrypoint_sections']:
    assert all(v['c1'] and v['c2'] for v in report[section].values())
scene=(ROOT/'cycle_complet/SCENE_C2_SYNCHRONISEE.html').read_text()
packed=re.search(r"const CONTACT=await unpackC2\('([^']+)'\)",scene)[1]
contact=json.loads(gzip.decompress(base64.b64decode(packed)))
rotation=np.array([[p['across'],p['along'],p['normal']] for p in contact['motion']]).transpose(0,2,1)
error=float(np.max(np.abs(rotation.transpose(0,2,1)@rotation-np.eye(3))))
determinants=np.linalg.det(rotation)
assert error<1e-9 and np.max(np.abs(determinants-1))<1e-9
report['all_stored_poses']={'count':len(rotation),'maximum_orthogonality_error':error,
    'minimum_determinant':float(determinants.min()),'maximum_determinant':float(determinants.max())}
(ROOT/'publication/evidence/PARITE_C1_C2.json').write_text(json.dumps(report,indent=2))
print('C1/C2 structural parity and all stored rigid contact frames: passed')
