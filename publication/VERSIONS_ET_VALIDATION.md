# Versions retenues et portée de la validation

## Acceptation enregistrée

Le 11 novembre 2026, Jean-Michel Puybouffat confirme que C2 N2-R02 est bon et demande de passer au dossier des quatre applications et à la publication. Cette confirmation clôt la revue numérique de C2 engagée dans la conversation. C1 aux deux niveaux et C2 au niveau d'examen avaient été acceptés auparavant.

Il s'agit d'une acceptation déclarée par l'auteur dans cette revue, enregistrée dans le dossier ; aucun certificat d'essai ou signature d'approbation industrielle n'est créé.

| Élément | Source | Référence retenue | Entrée |
|---|---|---|---|
| A1 | ByteNDT-B014-TRUE-TWIN | `a2b847e4a265fdbbff656bf0da7dac7cc0bc152b` | `app.py` |
| A2 | ByteNDT-SCANNER-C1 | `584db3867a9aae6b5c02bb8fe207fcc093c3882a` | `app.py` |
| A3 | ByteNDT-B014-C2-TRUE-TWIN | `71fd6e33dc97ebff5ad7ff3ba5ffd0f5547ee239` | `app.py` |
| A4 | ByteNDT-SCANNER-C2 | `664bb4b787c32401966bf582199a2d211912dbde` | `level2_app.py` |

Ces commits identifient les sources de référence de la publication. Une URL Streamlit peut évoluer ; elle ne remplace pas cette référence. Pour A4, le repère N2-R02 et l'essai sont confirmés par les captures et le retour de l'auteur ; le SHA interne du serveur n'a pas été lu via l'administration Streamlit.

## Preuves disponibles

- Conservation des quatre payloads C2 : géométrie, recalage, contact et champ.
- Contrôles navigateur aux positions réparties du début à la fin, synchronisation des lignes, marche avant/retour/arrêt et FR/EN.
- Présence des sept rubriques de l'application complète, dont TFM, voxel et rapport.
- Cohérence numérique des 1 981 repères de contact C2.
- Contrôle des contacts de positions 1, 81, 199 sur la racine centrale et correction de la confusion d'éclaté.
- Revue utilisateur du balayage jusqu'à 199/199 et 229,31 mm, puis de N2-R02.

Les contrôles partiels de passage mécanique restent des contrôles partiels. Les correspondances 5/5 et 6/6 viennent des tables sources ; elles ne constituent ni une nouvelle campagne indépendante ni une estimation de probabilité de détection.

## Manifestes

[APPLICATIONS.json](manifestes/APPLICATIONS.json) est le registre des quatre applications. Les deux manifestes de sources A1/A3 sont recopiés des commits identifiés, à titre de traçabilité. Ils ne constituent pas une nouvelle vérification exhaustive de toutes les dépendances ou des déploiements actifs. Les empreintes des pièces documentaires du présent dossier sont dans `manifestes/DOSSIER_SHA256.json`.

## Historique à conserver

Les rapports N2-R01 et N2-R02 restent conservés avec leur contexte d'origine ; leurs mentions « en revue » décrivent l'état au moment de ces contrôles. La présente fiche enregistre l'acceptation utilisateur ultérieure. Les captures N2-R01 restent des traces de travail ; les figures finales de publication seront choisies sur les versions acceptées et explicitement légendées.

La procédure C2-PROC-DRAFT-01 demeure un premier draft à adapter aux appareils, sondes, sabots et logiciels retenus. L'acceptation de l'application ne transforme pas ce document en procédure instrumentale finale.
