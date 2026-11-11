"""Build the C2 level-2 review without changing the accepted level-1 files."""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build_scene() -> str:
    source = (ROOT / 'scanner_assets/SOURCE_SCANNER_R02.html').read_text()
    # Immutable historical geometry; never reconstruct UT or use C1 poses.
    match = re.search(r'const SCANNER6=(.*);\n', source)
    if match is None:
        raise ValueError('Missing historical scanner geometry')
    geometry = match.group(1)
    json.loads(geometry)
    scene = (ROOT / 'cycle_complet/SCENE_C2_SYNCHRONISEE.html').read_text()
    scene = scene.replace('#stage{height:400px}', '#stage{height:560px}')
    overlay = (ROOT / 'scanner_assets/scanner_level2.js').read_text()
    addition = '\nconst SCANNER6=' + geometry + ';\n' + overlay
    # Insert into the existing module so its lexical scene/contact objects are shared.
    pos = scene.rfind('</script>')
    if pos < 0:
        raise ValueError('Missing scene module')
    return scene[:pos] + addition + '\n' + scene[pos:]


def build_document(*, embedded: bool = True) -> str:
    if embedded:
        from publication_view import build_publication_document
        document = build_publication_document(ROOT / 'cycle_complet')
        start = document.index('srcdoc="') + len('srcdoc="')
        end = document.index('"', start)
        document = document[:start] + html.escape(build_scene(), quote=True) + document[end:]
    else:
        document = (ROOT / 'cycle_complet/00_OUVRIR_CYCLE_C2_FR_EN.html').read_text()
        document = document.replace('src="SCENE_C2_SYNCHRONISEE.html"', 'src="SCENE_C2_NIVEAU2.html"')
    operator = (ROOT / 'scanner_assets/operator_level2.js').read_text()
    pos = document.rfind('</script>')
    return document[:pos] + '\n' + operator + '\n' + document[pos:]


def preserved_payloads() -> dict[str, str]:
    reference = (ROOT / 'cycle_complet/SCENE_C2_SYNCHRONISEE.html').read_text()
    candidate = build_scene()
    pattern = r"const (DATA|C2_REGISTRATION|CONTACT|BEAM3D)=await unpackC2\('([^']+)'\)"
    before = dict(re.findall(pattern, reference))
    after = dict(re.findall(pattern, candidate))
    if len(before) != 4 or before != after:
        raise ValueError('Accepted C2 payloads changed')
    return {key: hashlib.sha256(value.encode()).hexdigest() for key, value in before.items()}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    import shutil
    for source in (ROOT / 'cycle_complet').iterdir():
        if source.is_file() and source.name != 'SCENE_C2_SYNCHRONISEE.html':
            shutil.copy2(source, args.output / source.name)
    (args.output / 'SCENE_C2_NIVEAU2.html').write_text(build_scene())
    (args.output / '00_OUVRIR_CYCLE_C2_FR_EN.html').write_text(build_document(embedded=False))
    (args.output / 'PRESERVATION_NIVEAU1.json').write_text(json.dumps(preserved_payloads(), indent=2))
