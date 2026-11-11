# Annexes scientifiques préparées par l'auteur

Les textes originaux sont en cours de préparation par l'auteur. Les sections ci-dessous organisent leur intégration ; elles ne prétendent pas reproduire des annexes reçues.

## Annexe A — Propagation des ondes mécaniques

Présenter les équations du mouvement, le lien contrainte–déformation, les hypothèses de milieu, les modes longitudinaux et transversaux, les conditions aux interfaces, la réfraction, les conversions de modes, l'atténuation et les conventions d'unités. Distinguer les solutions de référence des approximations utilisées dans le twin.

Lien au manuscrit : section 3, choix des trajets et limites du champ calculé. Les valeurs matériau, fréquences et constantes effectivement utilisées restent à relever dans les sources et à confronter au texte de l'auteur.

## Annexe B — Calcul tensoriel et construction du twin

Définir les repères CAO, scanner et acoustique, les transformations de points et vecteurs, les normales, le changement de base des tenseurs et, si le modèle l'emploie, le tenseur d'élasticité. Fournir les conventions d'indices et de rotation.

Le recalage rigide d'une pose est décrit par x_mécanique = R x_acoustique + t, avec RᵀR = I et det(R) = +1. Cette relation décrit le recalage géométrique retrouvé dans l'application ; elle ne prouve pas qu'un solveur tensoriel de propagation est implémenté. Identifier explicitement le rôle du calcul tensoriel dans le code effectivement utilisé.

Lien au manuscrit : section 3 et traçabilité des poses C1/C2. Contrôler l'échelle unique en mm et les origines acoustiques virtuelles.

## Annexe C — Excitation ultrasonore et lois focales

Présenter l'excitation temporelle et spectrale, la fréquence centrale et la bande passante, l'ouverture, le pas des éléments, les retards, l'apodisation et les lois de focalisation. Séparer l'excitation de la propagation puis de la réponse reçue et du traitement.

Lien au manuscrit : matrice 8 × 8, 85 lois par position, champ cohérent, signaux encodés. La référence exacte de sonde, les caractéristiques du sabot et les paramètres matériels à confirmer doivent être sourcés avant publication.

## Annexe D — TFM et voxel

Voir [la première base explicative](ANNEXE_D_TFM_VOXEL_DRAFT_FR.md). Son contenu doit être confronté aux paramètres et aux modules réellement utilisés dans les données du projet.

## Tableau de liaison à compléter avec les annexes

| Élément théorique | Expression/hypothèses de l'annexe | Module et paramètres réellement employés | Preuve/limite |
|---|---|---|---|
| Élasticité et modes | À fournir par l'auteur | À relever | Pas d'assimilation automatique à un solveur complet |
| Transformations et repères | R, t ; conventions | Recalage rigide par pose dans la scène | Identité des payloads et contrôles de repères |
| Excitation et retards | À fournir | Lois focales sources | CSV C1/C2 à relier aux paramètres |
| Champ cohérent | Référence dB et normalisation | Volume calculé affiché | Ni pression mesurée ni rétrodiffusion complète |
| TFM, voxel et dimensionnement | Formules et hypothèses à fournir | Traitements du jeu source | PSF/image distincte de la taille physique d'un défaut |

## Lecture technique envisagée

Fabrice Foucher / EXTENDE, mentionné par l'auteur en lien avec CIVA, est un interlocuteur envisagé. Le dossier à lui soumettre pourrait comprendre le manuscrit, les annexes, les quatre versions figées et un cas calculable commun. Toute comparaison CIVA nécessitera des paramètres partagés et des résultats réellement obtenus. Aucun avis technique ni accord de diffusion n'est acquis.
