"""Restore the accepted C2 UT reference while the scanner assembly is reviewed."""
from pathlib import Path
import hashlib
import json
import streamlit as st
import streamlit.components.v1 as components
from publication_view import build_publication_document
st.set_page_config(page_title="BYTE NDT — C2 référence — FR / EN",layout="wide",initial_sidebar_state="collapsed")
st.caption("C2 — R03.2 · RÉFÉRENCE UT — VUES R05 / UT REFERENCE — DISPLAY R05")
st.info("Application C2 de référence : 199 positions, PA EXTRADOS → première gorge INTRADOS G1. La superposition du scanner est retirée pendant la vérification du positionnement. / Reference C2 application: 199 positions, PA EXTRADOS → first INTRADOS groove G1. Scanner overlay removed while positioning is reviewed.")
root=Path(__file__).parent / "cycle_complet"
manifest=json.loads((root/"MANIFEST_REFERENCE_C2.json").read_text())
bad=[name for name,digest in manifest.items() if not (root/name).is_file() or hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest]
if bad:
    st.error("Fichiers de référence incomplets / Incomplete reference files")
    st.stop()
components.html(build_publication_document(root),height=2350,scrolling=True)
st.link_button("Application C2 UT de référence / Reference C2 UT application", "https://bytendt-lsb941-c2-fr-en.streamlit.app/")
with st.expander("Statut du scanner / Scanner status"):
    st.write("Le scanner reste une étude non validée. Les coques, le montage sur l’aube centrale et le rendu des tirs doivent être vérifiés ensemble contre cette référence. / The scanner remains an unvalidated study. Shells, installation on the central blade and ray display must be checked together against this reference.")
    st.link_button("Projet de publication — sources / Publication project — sources", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/blob/main/documentation/PROJET_PUBLICATION_RACINES_FR_EN.md")
