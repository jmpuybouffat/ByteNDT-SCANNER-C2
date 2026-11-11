# C2 avec scanner — revue N2-R01

**Objectif : valider le niveau 2 de C2, avec l'application C1 complète comme référence.**

Le C1 aux deux niveaux et le niveau 1 C2 sont validés par l'auteur. Cette candidate rassemble l'examen C2 accepté et les géométries du scanner C2 pour terminer la revue du montage et du mouvement.

## Ce qui est repris de C1

Procédure FR/EN, contrôles d'avance/retour/arrêt, vitesse, codeur simulé, assemblage/éclaté, contexte des trois aubes, vues et coupes, cartographie encodée, indications, TFM, voxels, rapport, exports, mécanique et notice. Les sept rubriques de résultats sont présentes.

Les données restent propres à C2 : PA EXTRADOS vers première gorge INTRADOS G1, 199 positions, 16 915 lois et EDM_06 à EDM_11. Les quatre payloads du niveau 1 sont conservés à l'identique.

## Vues à examiner

- [Montage — position 1](publication/evidence/C2_N2_context_001.png)
- [Montage — position 81](publication/evidence/C2_N2_context_081.png)
- [Montage — position 199](publication/evidence/C2_N2_context_199.png)
- [Détail PA et guidage — position 81](publication/evidence/C2_N2_detail_081.png)
- [Scanner éclaté — position 81](publication/evidence/C2_N2_exploded_081.png)
- [Application complète](publication/evidence/C2_N2_application.png)

L'opacité des coques est réglable pour examiner le mobile. La vue de contexte conserve les maillages de l'aube sans plan de découpe mobile ; son cadrage reste stable pendant le balayage.

## Ouvrir la candidate dans Streamlit

Créer une application de revue séparée avec :

- Dépôt : `jmpuybouffat/ByteNDT-SCANNER-C2`
- Branche : `review/c2-niveau2-publication-2026-11-11`
- Fichier principal : `level2_app.py`
- Python : `3.12`

L'application Streamlit de référence n'est pas remplacée par l'enregistrement de cette branche. Aucun déploiement de la candidate n'a été effectué dans cette opération.

Pour une prévisualisation locale sans Streamlit :

```sh
python level2_document.py --output ../preview-c2
python -m http.server 8765 --directory ../preview-c2
```

Ouvrir `http://localhost:8765/00_OUVRIR_CYCLE_C2_FR_EN.html`.

## État des contrôles

Le contrôle Chromium réussit à huit positions réparties du tir 1 au tir 199 : présence des deux coques et huit pièces mobiles, calage sur le contact, rotation rigide, absence de découpe en contexte, lignes UT synchronisées, assemblé/éclaté, FR/EN, avance/retour/arrêt et accès aux sept rubriques, dont TFM, voxels et rapport. Aucune erreur JavaScript relevée.

Les 1 981 repères de contact stockés sont orthonormaux à la précision numérique. Un contrôle complémentaire de tous les sommets mobiles contre les triangles de la racine fermée, à huit positions, donne une pénétration échantillonnée maximale de 0,0146 mm, inférieure au seuil de signalement de 0,05 mm. Ce contrôle partiel ne certifie pas le passage continu de l'ensemble entre les trois aubes.

[Rapport navigateur](publication/evidence/CONTROLE_C2_N2_R01.json) · [Parité C1/C2](publication/evidence/PARITE_C1_C2.json) · [Contrôle partiel de racine](publication/evidence/CONTROLE_RACINE_N2.json)

## Validation visuelle à terminer ensemble

Examiner la face d'appui et G1, le placement des coques et du mobile, le guidage au début/milieu/fin, puis l'avance et le retour avec leurs tirs. La candidate reste une version de revue tant que l'auteur ne l'a pas acceptée.

La publication viendra ensuite, étape par étape. [Le répertoire des quatre applications](publication/README.md) prépare seulement leur classement.
