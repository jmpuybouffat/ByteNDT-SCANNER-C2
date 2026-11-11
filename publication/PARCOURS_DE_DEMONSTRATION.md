# Parcours de démonstration des quatre applications

Version de dossier 01 · revue numérique acceptée par Jean-Michel Puybouffat le 11 novembre 2026.

## A1 — comprendre l’examen C1

Ouvrir [C1 — aube et examen UT](https://bytendt-lsb941-c1-fr-en.streamlit.app/). Identifier l’appui INTRADOS et la première gorge EXTRADOS. Examiner le début, une position intermédiaire et la fin des 41 positions, puis relier la position du PA à l’A-scan et à la cartographie. Terminer par les cinq références EDM, un exemple TFM/voxel et les exports.

## A2 — retrouver le même examen avec son scanner C1

Utiliser la version acceptée de [ByteNDT-SCANNER-C1](https://github.com/jmpuybouffat/ByteNDT-SCANNER-C1/tree/584db3867a9aae6b5c02bb8fe207fcc093c3882a), entrée `app.py`. [Ouvrir C1 avec scanner](https://bytendt-lsb941-scanner-c1-fr-en.streamlit.app/) — adresse confirmée par l’auteur.

Montrer les trois aubes, le scanner assemblé puis son éclaté à l’arrêt. Revenir à l’assemblage, montrer l’avance/arrêt/retour et le codeur simulé, puis retrouver les résultats du même cas C1. Cette application constitue la référence du niveau avec scanner.

## A3 — examiner le cas complémentaire C2

Ouvrir [C2 — aube et examen UT](https://bytendt-lsb941-c2-fr-en.streamlit.app/). Identifier l’appui EXTRADOS et la première gorge INTRADOS G1. Relier les coupes et le champ calculé aux 199 positions. Montrer la cartographie complète et les six références EDM_06 à EDM_11, en distinguant les tables d’examen figées des candidats issus du signal encodé.

## A4 — retrouver C2 dans son contexte avec scanner

Ouvrir [C2 avec scanner — application essayée par l’auteur](https://jmpuybouffat-bytendt-scanner-c2-level2-app-reviewc2-nive-e6sbvl.streamlit.app/). Le repère accepté est **N2-R02** ; l’entrée source est `level2_app.py`.

Montrer les positions 1, 81 et 199, l’appui sur l’aube centrale, le mouvement et le compteur simulé de 229,31 mm en fin de parcours. L’éclaté est réservé à l’arrêt et explicitement identifié. Montrer l’option de contraste UT sans la présenter comme une augmentation du signal. Terminer par les mêmes rubriques de résultats que C1, avec les données propres à C2.

## Lecture commune

Pour chaque exemple, conserver le même cas, la même position et les mêmes unités lorsqu’on passe de la géométrie au signal, à la carte et au rapport. Une vue 3D, une coupe d’examen, un champ calculé et une reconstruction TFM n’ont pas la même fonction et doivent garder une légende explicite.

La démonstration établit la continuité du scénario numérique. Le passage en atelier et la réalité virtuelle seront documentés comme l’étape suivante, avec leurs propres observations.
