"""C2 scanner operator study; separate from accepted UT replay."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from level2_document import build_document, preserved_payloads
st.set_page_config(page_title="BYTE NDT — Scanner C2 — FR / EN",layout="wide",initial_sidebar_state="collapsed")
st.caption("BYTE NDT · SCANNER C2 · OPÉRATEUR / OPERATOR · NIVEAU 2 · REVUE N2-R02 / LEVEL 2 · REVIEW N2-R02 — SCANNER + EXAMEN C2 COMPLET / SCANNER + COMPLETE C2 EXAMINATION")
st.info("N2-R02 : revue de l’application C2 complète avec scanner, selon la référence C1 validée. Deux coques conformes, slot intégré et circuit d’eau provisoire. Scan et projet de scanner acceptés par l’auteur ; affichage UT en revue. / N2-R02: complete C2 application with scanner, following the accepted C1 reference. Two conformal shells, integrated slot and provisional water circuit. Replay and scanner concept accepted by the author; UT display under review.")
p=Path(__file__).parent/"scanner_assets"
# Read the release document directly: never retain an older geometry in cache.
def document():
    preserved_payloads()
    return build_document()
with st.expander("Procédure opérateur et couplage / Operator procedure and coupling", expanded=True):
    procedure_language = st.radio("Langue de la procédure / Procedure language", ["Français", "English"], horizontal=True)
    if procedure_language == "Français":
        st.markdown("**Positionnement validé → étalonnage sur référence → tirs et parcours → contrôle du film d’eau et du couplage → scan et rapport.**")
        st.write("Vérifier la formation et la continuité du film d’eau sous le sabot avant le départ et pendant tout le parcours. Surveiller en complément le signal acoustique de référence. En cas de perte : signaler, arrêter, enregistrer et reprendre la zone selon la procédure approuvée.")
        st.caption("Premier draft C2-PROC-DRAFT-01 : base à adapter aux appareils, sondes, sabots et logiciels utilisés. Seuils à établir avec la référence et l’instrumentation réelle. Le rejeu actuel ne mesure pas le couplage physique.")
    else:
        st.markdown("**Validated positioning → reference calibration → firing laws and path → water-film and acoustic-coupling checks → scan and report.**")
        st.write("Check water-film formation and continuity beneath the wedge before starting and throughout travel. Also monitor the acoustic reference signal. On loss: flag, stop, record and re-examine the affected zone under the approved procedure.")
        st.caption("Initial draft C2-PROC-DRAFT-01: working basis to adapt to the instruments, probes, wedges and software used. Establish thresholds with the reference and actual instrumentation. The current replay does not measure physical coupling.")
    procedure = Path(__file__).parent / "documentation" / "PROCEDURE_EXAMEN_C2_FR_EN.md"
    st.download_button("Procédure complète FR/EN / Full FR/EN procedure", procedure.read_text(), file_name=procedure.name, mime="text/markdown")
components.html(document(),height=2350,scrolling=True)
with st.expander("Version et références / Version and references"):
    st.json((p/"REFERENCE_COMMANDE.json").read_text())

st.link_button("Dossier maquette et fichiers CAO / Mock-up and CAD files", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/tree/main/maquette_etude")
st.link_button("Notice du bâti / Base guide", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/blob/main/documentation/NOTICE_BATI_C2_FR_EN.md")

st.link_button("Procédure d’examen — projet FR/EN / Draft examination procedure", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/blob/main/documentation/PROCEDURE_EXAMEN_C2_FR_EN.md")

st.link_button("Concept coques et alimentation en eau / Shell and water-supply concept", "https://github.com/jmpuybouffat/ByteNDT-SCANNER-C2/blob/main/documentation/CONCEPT_COQUES_C2_FR_EN.md")
