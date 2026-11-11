# C2 niveau 2 — correction d'affichage N2-R02

## Retour de revue de l'auteur

Le scan s'exécute sans incident ; le projet de scanner et la structure complète de l'application, comme C1, sont acceptés par l'auteur. La dernière erreur signalée concerne la troisième capture : les pièces semblent appartenir à une autre aube. La lisibilité des indications UT reste à améliorer. L'auteur précise que ce signalement ne concerne pas les écrans TFM et voxel.

## Constat et correction

La capture précédente porte le bouton « Assemble scanner », indiquant un éclaté encore actif pendant la lecture. Les décalages illustratifs des coques sont respectivement [65, −30, 0] mm et [−65, 30, 0] mm : ils déplacent les pièces vers les aubes voisines. L'affichage ne distinguait pas suffisamment cette présentation du montage opérationnel.

La lecture standard, comme l'avance/retour du scanner, rétablit désormais l'assemblage. L'éclaté est indisponible pendant le mouvement ; à l'arrêt, il est explicitement nommé et les aubes voisines sont masquées pour éviter de les présenter comme supports des pièces décalées. Le retour à l'assemblage rétablit la visibilité demandée des voisines.

Une option « Contraste UT renforcé » agrandit les points et étiquettes existants et augmente l'opacité des rayons graphiques. Elle conserve les amplitudes, positions, couleurs d'amplitude, seuils, données, lois et matrices sources. Elle ne crée pas d'indication et ne renormalise pas les cartes.

## Vérification de l'aube de contact

Les contacts C2 des positions 1, 81 et 199 ont été confrontés aux triangles des maillages. Leur distance à la racine centrale est nulle à la précision du contrôle ; les distances aux voisines sont :

| Position | Racine centrale | Voisine verte | Voisine bleue |
|---|---:|---:|---:|
| 1 | ≈ 0 mm | 43,714526 mm | 33,786179 mm |
| 81 | ≈ 0 mm | 30,139675 mm | 70,960763 mm |
| 199 | ≈ 0 mm | 29,322658 mm | 49,031195 mm |

Le maillage de racine est identique entre la source scanner R02 et le niveau 1 C2 accepté. Cette vérification confirme l'identité de l'aube d'appui aux positions examinées ; elle ne qualifie pas les jeux mécaniques de tout l'ensemble.

## Procédure et suites

La procédure C2-PROC-DRAFT-01 est explicitement un premier draft servant de base, à adapter aux appareils, sondes, sabots et logiciels utilisés. Elle n'est pas une procédure instrumentale finale.

La revue suivante porte sur la lisibilité de cette version assemblée. La publication reste une étape ultérieure, menée pas à pas avec l'auteur.
