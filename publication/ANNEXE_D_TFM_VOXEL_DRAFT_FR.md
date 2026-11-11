# Annexe D — comprendre la TFM et les voxels

**Premier draft explicatif pour la publication.** Les paramètres propres aux reconstructions du projet seront complétés avec les sources ; cette annexe ne décrit pas une nouvelle acquisition.

## 1. De la matrice des signaux à l’image

Une acquisition FMC, ou *Full Matrix Capture*, conserve des signaux pour des couples d’éléments émetteur–récepteur. Avec N éléments, une matrice complète comporte jusqu’à N² couples : 64 éléments correspondent ainsi à 4 096 couples possibles. Il faut distinguer ce comptage des 85 lois par position employées dans le scénario de balayage C1/C2. La présence d’un titre « FMC/TFM 64×64 » dans une figure n’établit pas, à elle seule, la configuration d’un appareil physique.

La TFM, ou *Total Focusing Method*, consiste à former une image en combinant, pour chaque point de reconstruction, les signaux aux temps de parcours correspondants. Une écriture générale de la somme retardée est :

**I(x) = |Σᵢ Σⱼ wᵢⱼ(x) sᵢⱼ[τᵢ(x) + τⱼ(x)]|**

Dans cette expression, sᵢⱼ est le signal du couple, τᵢ et τⱼ les temps de trajet du modèle retenu, et wᵢⱼ les pondérations. Le calcul des trajets, l’interpolation temporelle, le traitement de l’enveloppe et les pondérations dépendent de l’implémentation. Les interfaces, le sabot, les modes et leurs éventuelles conversions doivent être précisés lorsque le modèle les prend en compte. La référence générale de cette famille de traitements est donnée par Holmes, Drinkwater et Wilcox [3].

L’article devra relier cette explication aux fonctions et paramètres réellement employés pour les images conservées. Il ne doit pas attribuer automatiquement au code du projet toutes les variantes possibles de la TFM.

## 2. Lire une image TFM

Les axes locaux, leurs unités et leur transformation vers le repère de l’aube doivent accompagner chaque image. Une zone brillante indique une réponse forte selon le modèle, le traitement et la normalisation retenus. Elle doit être mise en relation avec la géométrie, l’indication et les données d’entrée ; sa seule couleur ne suffit pas à identifier un défaut physique.

Une largeur mesurée à −6 ou −12 dB dépend notamment de la fonction d’étalement du système, de l’ouverture, de la fréquence, de la focalisation et de la définition de l’échelle. La largeur de l’image ne doit donc pas être assimilée directement à la dimension réelle de la discontinuité sans méthode de dimensionnement et référence appropriées.

## 3. Ce qu’est un voxel

Un voxel est une cellule d’une grille volumique. Chaque cellule porte une valeur reconstruite, calculée ou issue des données selon le traitement identifié. Une représentation peut montrer des points au-dessus d’un seuil, une isosurface ou des projections du volume. Les axes U, V et W, le pas de grille et le domaine doivent être indiqués.

Une projection maximale U–V retient, à chaque position U–V, la valeur maximale rencontrée le long de W. Les projections U–W et V–W suivent le même principe. Elles facilitent la lecture, mais elles superposent de l’information en profondeur. Un maximum visible dans une projection n’identifie donc pas, à lui seul, une profondeur unique.

Une représentation de voxels au-dessus de −6 dB est un sous-ensemble du volume selon une référence de seuil à préciser. Elle ne représente pas automatiquement le volume matériel d’un défaut.

## 4. Ne pas confondre les échelles

| Quantité | Convention à expliciter | Précaution de lecture |
|---|---|---|
| Amplitude d’un signal | Par exemple 20 log₁₀(|A|/Aᵣₑ𝒻), si c’est la convention retenue | Identifier la référence et les traitements |
| Gain cohérent calculé de l’application | La vue actuelle indique 10 log₁₀(G), référence fixe G = 1 | Ce n’est ni une pression mesurée ni une carte %FSH |
| %FSH | Pourcentage de pleine hauteur d’écran selon l’instrument ou la carte source | Garder sa calibration et ses unités propres |
| Niveau relatif d’une image ou d’un voxel | Référence globale ou locale à relever dans le traitement | Ne pas transposer un seuil sans sa normalisation |

Les indications ne deviennent pas plus fortes lorsque leur taille à l’écran est augmentée. L’option de contraste de C2 N2-R02 modifie la lisibilité des repères graphiques, pas les amplitudes sources.

## 5. Fiche de traçabilité à joindre à chaque exemple

Relever le cas et l’indication, les fichiers d’entrée et leurs versions, le repère et les unités, le nombre d’éléments/couples réellement utilisés, les propriétés du modèle de trajet, la grille et son pas, les traitements temporels et pondérations, la référence d’amplitude, les seuils et la méthode de mesure. Relier ensuite l’image à la position du scan, au signal et au rapport source.

Pour les quatre applications, TFM et voxel sont des éléments conservés du scénario numérique. La revue fonctionnelle de leurs écrans ne constitue pas une nouvelle validation expérimentale de leur performance.

Référence [3] : [bibliographie de départ](REFERENCES_BIBLIOGRAPHIQUES.md).
