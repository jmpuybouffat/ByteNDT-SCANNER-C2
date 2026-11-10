# Projet de publication — examen des racines de grandes aubes

## Titre de travail

**Examen ultrasonore des racines de grandes aubes par jumeau numérique : continuité de la procédure, du scanner et des résultats.**

**Ultrasonic examination of large turbine-blade roots using a digital twin: continuity from procedure and scanner to traceable results.**

## Angle proposé / Proposed focus

FR : Présenter un cas industriel complet et reproductible, depuis la procédure d’examen jusqu’aux données, vues, analyses et rapports, puis à la conception du scanner et à la préparation de la réalité virtuelle. L’apport à démontrer est la continuité entre ces étapes, avec une origine identifiable de chaque donnée. Le travail prolonge les présentations de l’auteur à Prague en 2014 et Munich en 2016 ; leurs titres, coauteurs, références d’actes et identifiants bibliographiques restent à compléter à partir des documents originaux.

EN: Present a complete, reproducible industrial case from examination procedure through data, views, analyses and reports to scanner design and virtual-reality preparation. Demonstrate continuity between stages with identifiable data provenance. The work follows the author’s presentations in Prague in 2014 and Munich in 2016; exact titles, coauthors, proceedings references and identifiers must be completed from the original documents.

## Sources et produits issus / Sources and resulting products

| Source | Utilisation / Use | Produit / Output |
|---|---|---|
| CAO de la racine, plateforme et aubes voisines / Root, platform and adjacent-blade CAD | Repères et contraintes d’accès / Datums and access constraints | Maillage normalisé en mm, contacts et coupes / Mesh in mm, contact and section views |
| C1 — application UT de référence, 41 positions, 5 EDM | Réponses et lois sources conservées / Preserved source responses and laws | Cartographie, indications, TFM, voxels, analyses et rapport C1 / C1 cartography, indications, TFM, voxels, analyses and report |
| C2 — application UT de référence, 199 positions, 6 EDM | Réponses encodées et tables d’examen figées conservées / Preserved encoded responses and frozen examination tables | Cartographie et maxima sources, TFM, voxels, analyses et rapport C2 / Source cartography and maxima, TFM, voxels, analyses and report |
| Recalages mécaniques C1/C2 / C1/C2 mechanical registration | Transformations rigides par position / Per-position rigid transformations | Rejeu sur la géométrie, sans modification des matrices UT / Replay on geometry without modifying UT matrices |
| Parcours de contact acceptés / Accepted contact paths | Guidage et horloge opérateur / Guidance and operator clock | Déplacement continu, position et comptage simulé / Continuous movement, position and simulated counts |
| Concept de deux coques conformes / Two conformal shell concept | Appuis aérofoil/plateforme, slot et lèvre supérieure / Airfoil/platform support, slot and upper lip | Géométrie maillée, circuit d’eau provisoire, éclaté et fichiers d’étude / Mesh geometry, provisional water circuit, exploded view and study files |
| Procédures d’examen FR/EN / FR/EN examination procedures | Positionnement, étalonnage, film d’eau et contrôle acoustique du couplage / Positioning, calibration, water film and acoustic coupling monitoring | Séquence opérateur et exigences à vérifier / Operator sequence and checks to establish |
| Composants identifiés et états assemblé/éclaté / Identified parts and assembled/exploded states | Préparation de formation et RV / Training and VR preparation | Base de contenu pour le montage et l’examen en RV / Content foundation for VR installation and examination |

## Références logicielles et jeux de données / Software and datasets

- C1 UT : `jmpuybouffat/ByteNDT-B014-TRUE-TWIN`, branche `publication/c1-3aubes-fr-en`, révision mécanique acceptée `a2b847e4a265fdbbff656bf0da7dac7cc0bc152b`.
- C2 UT : `jmpuybouffat/ByteNDT-B014-C2-TRUE-TWIN`, branche `publication/c2-3aubes-fr-en`, révision `c69d40065bd8d24dfec2f03e8d43145025c9243c`.
- Scanner C1 complet : `jmpuybouffat/ByteNDT-SCANNER-C1`, R06, révision `584db38`.
- Scanner C2 : `jmpuybouffat/ByteNDT-SCANNER-C2`, R01, révision de diffusion à relever après publication / release revision to record after publication.
- Les manifestes des assets donnent les SHA-256 des fichiers sources et intégrés / Asset manifests provide SHA-256 digests of source and integrated files.
- Les scripts de construction et les dépendances utilisés doivent être joints ou décrits avec leurs versions dans le dossier de reproductibilité / Include or document construction scripts and dependencies with versions in the reproducibility dossier.
- Imasonic : matrice 8 × 8 envisagée ; référence exacte de la sonde, du sabot et du câble à confirmer par la documentation constructeur / Proposed 8 × 8 matrix; exact probe, wedge and cable references require manufacturer documentation.

## Plan d’article / Article structure

1. Besoin industriel et géométrie d’accès / Industrial need and access geometry.
2. Procédure : positionnement, tirs, trajet, étalonnage et couplage / Procedure: positioning, firing laws, path, calibration and coupling.
3. Modèles physiques et implémentation effective / Physical models and actual implementation.
4. Jeux de données et architecture du jumeau / Datasets and twin architecture.
5. Cas C1 et C2 : vues, résultats sources et traçabilité / C1 and C2 cases: views, source results and traceability.
6. Scanner à coques, codeur et alimentation en eau / Conformal-shell scanner, encoder and water supply.
7. Contrôles numériques, incertitudes et validation matérielle / Numerical checks, uncertainties and physical validation.
8. Formation, réalité virtuelle et perspectives / Training, virtual reality and outlook.

## Preuves à réunir / Evidence dossier

FR : Identifier l’origine des données et la version de chaque traitement, fournir les réglages et lois, le repère et les unités, des exemples d’indications localisées et dimensionnées, les résultats disponibles et leurs limites. Les résultats de référence 5/5 et 6/6 sont ceux des jeux sources ; ils ne constituent pas une nouvelle campagne expérimentale indépendante. Les maxima des tables figées C2 ne doivent pas être présentés comme de nouvelles sorties du détecteur encodé. Documenter la sensibilité aux paramètres, la couverture, les erreurs de localisation/dimensionnement et, lorsque disponibles, les comparaisons à des mesures physiques indépendantes avec incertitudes. Une comparaison avec CIVA exige un cas commun, des paramètres documentés et des résultats effectivement obtenus ; aucune équivalence ni approbation CIVA n’est établie ici.

Le champ 3D intégré est un gain cohérent calculé. Les formulations de Green, Kirchhoff, Born et GTD doivent être décrites en précisant quels modules sont réellement employés et vérifiés. Ne pas assimiler le champ disponible à un calcul complet de pression rétrodiffusée. Le montage, le codeur, le moteur et l’acquisition réels restent à intégrer et vérifier. Les coques maillées, leur serrage, leur jeu de guidage et leur circuit d’eau restent au stade de conception.

EN: Identify data provenance and processing revisions, provide settings and focal laws, coordinate systems and units, located/sized indication examples, available results and limitations. Reference 5/5 and 6/6 results belong to the source datasets; they are not a new independent experimental campaign. Frozen C2 examination-table maxima must not be represented as new encoded-detector outputs. Document parameter sensitivity, coverage, location/sizing errors and, when available, comparisons with independent physical measurements and uncertainties. Comparison with CIVA requires a common case, documented settings and actual results; no CIVA equivalence or endorsement is established here.

The integrated 3D field is calculated coherent gain. Describe Green, Kirchhoff, Born and GTD formulations while identifying which modules are actually implemented and checked. Do not equate the available field with a full backscattered-pressure calculation. Physical installation, encoder, motor and acquisition remain to be integrated and verified. Mesh shells, clamping, guide fit and water distribution remain at concept stage.

## Diffusion envisagée / Publication routes to assess

FR : Première cible à examiner : **NDT & E International** pour un article scientifique centré sur la méthode et les preuves. **Insight** est une autre piste pour l’examen et sa mise en œuvre ; **Ultrasonics** serait à envisager si l’apport principal porte sur la physique ou la modélisation ultrasonore. Préparer ensuite des présentations adaptées pour un support COFREND et un support sud-africain, éventuellement avec SAINT. Vérifier les périmètres éditoriaux actuels, les instructions aux auteurs et les règles de reprise avant soumission. Les informations présentes ne constituent pas une vérification des conditions actuelles des revues.

EN: First target to assess: **NDT & E International** for a scientific paper centred on method and evidence. **Insight** is another candidate for examination practice and implementation; consider **Ultrasonics** if the main contribution concerns ultrasonic physics or modelling. Prepare adapted presentations for a COFREND outlet and a South African outlet, potentially with SAINT. Check current editorial scopes, author instructions and republication rules before submission. Current journal conditions have not been verified in this document.

## Lecture critique / Technical review

FR : Le dossier peut être proposé à Fabrice Foucher / EXTENDE pour un regard critique sur la méthode, les hypothèses et le positionnement du travail. Cette lecture n’est pas présumée et ne constitue pas une approbation par CIVA. Aucun message n’est envoyé par l’application.

EN: The dossier may be offered to Fabrice Foucher / EXTENDE for technical feedback on method, assumptions and positioning. Such review is not presumed and does not constitute CIVA endorsement. The application sends no messages.
