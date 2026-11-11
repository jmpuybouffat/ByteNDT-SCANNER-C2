# Revue C2 niveau 2 — N2-R01

## Contrôles logiciels

Le générateur vérifie l'identité des quatre payloads compressés de niveau 1 : géométrie, recalage, contact et champ. Aucun fichier de `cycle_complet` n'est réécrit par l'intégration.

`tools/review_level2.py` utilise Chromium pour contrôler le chargement des deux coques et huit pièces, les positions 1, 20, 54, 81, 117, 145, 172 et 199, le calage du mobile sur le contact, la rigidité de sa rotation, l'absence de plans de découpe en vue de contexte, le nombre de lignes UT, les langues FR/EN, l'éclaté, l'avance/arrêt/retour et l'accès aux résultats finaux. Les résultats effectifs doivent être lus dans `publication/evidence/CONTROLE_C2_N2_R01.json` lorsqu'il a été produit avec succès.

## Revue visuelle de l'auteur à terminer

- Montage sur la bonne face de l'aube centrale ; position du PA par rapport à G1.
- Coques, rail/slot et chariot cohérents au début, au milieu et en fin de parcours.
- Aucun étirement ou mouvement apparent de la paroi dû au cadrage.
- Vues d'ensemble et de détail lisibles ; tirs et résultats cohérents avec la position.
- Captures comparables au C1 validé avec scanner.

## Résultats obtenus sur N2-R01

Le premier passage Chromium a réussi aux huit positions : deux coques, huit pièces mobiles, calage du mobile sur le contact sans écart numérique, rotation de déterminant 1, aucun plan de découpe en vue de contexte, 199 lignes au dernier tir, avance/arrêt/retour et FR/EN. La vérification de parité retrouve les sept rubriques de résultats, les commandes opérateur et les sections de procédure/documentation de C1. Les 1 981 repères de contact stockés sont orthonormaux à la précision numérique.

Un contrôle complémentaire des distances aux triangles de la racine centrale fermée porte sur tous les sommets des pièces mobiles à huit positions. La pénétration échantillonnée maximale est de 0,0146 mm ; aucun sommet échantillonné ne dépasse le seuil de signalement de 0,05 mm. Il ne faut pas traduire ce résultat en « absence de toute collision » : il n'inclut ni la totalité du mouvement continu, ni la totalité des contacts coques/aubes voisines. Les maillages des aubes voisines sont ouverts et ne permettent pas une certification intérieur/extérieur par le même test. Voir `evidence/CONTROLE_RACINE_N2.json`.

## Limites des preuves mécaniques existantes

Le contrôle historique R02 de passage des coques échantillonne un champ à 1 mm et rapporte un minimum de 0,116 mm pour le chariot. Ce contrôle partiel ne démontre pas à lui seul l'absence de collision continue de l'ensemble avec les trois aubes. Il ne constitue pas une marge de fabrication validée. Les captures et les rotations rigides ne remplacent pas ce contrôle mécanique.

La candidate n'affirme donc ni une qualification matérielle, ni une validation expérimentale des champs. Le statut de revue restera en place jusqu'à la validation visuelle de l'auteur ; les limites mécaniques doivent rester décrites dans la publication.
