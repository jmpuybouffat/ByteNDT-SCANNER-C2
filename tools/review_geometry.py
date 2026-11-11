"""Requires numpy, trimesh and rtree. Sampled central-root clearance only."""
import sys,json,re,gzip,base64
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
import trimesh,numpy as np
scene=(ROOT/'cycle_complet/SCENE_C2_SYNCHRONISEE.html').read_text()
def payload(key):
 match=re.search(r"const "+key+r"=await unpackC2\('([^']+)'\)",scene)
 return json.loads(gzip.decompress(base64.b64decode(match[1])))
base=payload('DATA')['base']
contact=payload('CONTACT')
source=(ROOT/'scanner_assets/SOURCE_SCANNER_R02.html').read_text()
scanner=json.loads(re.search(r'const SCANNER6=(.*);\n',source)[1])
v=np.asarray(base[0]['V']);root=trimesh.Trimesh(v,np.arange(len(v)).reshape(-1,3),process=True)
if root.volume<0:root.invert()
report={'scope':'Exact triangle distances and inside/outside of closed central root at eight encoded poses; all mobile vertices. Not continuous assembly clearance. Adjacent blades are open meshes and are not certified by containment.','root_watertight':root.is_watertight,'parts':[]}
for shot in [1,20,54,81,117,145,172,199]:
 p=contact['motion'][(shot-1)*10];R=np.array([p['across'],p['along'],p['normal']]).T
 for name,d in scanner['parts'].items():
  xyz=np.asarray(d['V'])@R.T+np.array(p['contact']);sd=trimesh.proximity.signed_distance(root,xyz)
  row={'shot':shot,'part':name,'vertices':len(xyz),'max_inside_mm':max(0,float(sd.max())),'min_outside_clearance_mm':float(-sd.max()),'vertices_inside_over_0_05mm':int((sd>.05).sum())}
  report['parts'].append(row)
 print('shot',shot,'worst penetration',max(x['max_inside_mm'] for x in report['parts'] if x['shot']==shot),flush=True)
(ROOT/'publication/evidence/CONTROLE_RACINE_N2.json').write_text(json.dumps(report,indent=2))
