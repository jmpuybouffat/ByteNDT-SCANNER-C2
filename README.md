# BYTE NDT — Scanner C2 et examen complet / Scanner C2 and complete examination

Application indépendante du scanner C1 et du rejeu UT C2 de référence. / Separate from scanner C1 and the reference C2 UT replay.

PA EXTRADOS → première gorge INTRADOS G1. 199 positions, 6 EDM_06–11, 16 915 lois originales. Deux coques conformes, slot intégré, circuit d’eau provisoire dans la lèvre supérieure. Commandes FR/EN, codeur simulé, contexte trois aubes, coupes, volume de sensibilité, TFM, voxels, analyses et rapports/exports d’origine.

The accepted C2 UT data and registration are preserved. The original encoded responses and frozen examination-table maxima remain distinct source layers. No physical acquisition, motor or encoder is connected. Shells are concept meshes, not a manufacturing release. The available field is calculated coherent sensitivity, not full backscattered pressure.

## Streamlit

- Repository: `jmpuybouffat/ByteNDT-SCANNER-C2`
- Branch: `main`
- Main file: `app.py`
- Python: **3.12**
- Suggested app URL: `bytendt-lsb941-scanner-c2-fr-en` (availability to check)

Do not modify the accepted C1 scanner or the reference UT applications. Documentation and source manifests accompany the package.

## R02 — Geometry and section correction

Reconnected root mesh before signed-distance construction, corrected guide-key/root overlap, recomputed both conformal shells and upper-lip water routing. Added PA-follow view and actual-mesh contact/origin/G1 section. Source path and UT data unchanged. See `documentation/CORRECTION_C2_R02_FR_EN.md`. Mechanical mock-up remains unqualified for functional manufacture.
