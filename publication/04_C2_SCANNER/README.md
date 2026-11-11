# A4 — C2 : aube dans son contexte avec scanner

**Statut : N2-R02 accepté dans la revue numérique de Jean-Michel Puybouffat, le 11 novembre 2026.**

- Dépôt : `jmpuybouffat/ByteNDT-SCANNER-C2`.
- Entrée acceptée : `level2_app.py`, distincte de `app.py`.
- Aube, recalage, contacts, tirs et champ : niveau 1 archivé à `42cf616e335efe64327d528b2cc524671a17f276`.
- Géométries des deux coques et huit pièces mobiles : scène R02, commit `6ec5dc6fbc4cf9ea6ea1222a3684a839758997a9`, blob Git `08e4cb4be28db3173feaaa3209316d9c940593b3`.
- La scène R02 est conservée comme source historique ; seules ses géométries de scanner sont extraites. Ses anciens calculs de vue et ses payloads UT ne remplacent pas le niveau 1 accepté.

## Ce que montre l’application acceptée

La géométrie centrale intacte, les aubes voisines, les coques et le mobile calé sur le contact C2. Vue d'ensemble stable, détail du PA, assemblé/éclaté et réglage d'opacité des coques. Commandes d'avance, retour, arrêt et comptage simulé reprennent le fonctionnement de C1. Le sens EXTRADOS → INTRADOS et les 199 positions restent propres à C2.

## Prévisualisation locale

```sh
python level2_document.py --output ../preview-c2
python -m http.server 8765 --directory ../preview-c2
```

Ouvrir `http://localhost:8765/00_OUVRIR_CYCLE_C2_FR_EN.html`.

Pour une instance Streamlit de revue : installer `requirements.txt`, puis exécuter `streamlit run level2_app.py`. Aucun remplacement du déploiement de référence n'est nécessaire pour cette revue.

Voir [le périmètre de validation](VALIDATION.md). Le dossier de fabrication et la qualification d'un scanner physique ne font pas partie de cette validation de l'application.

## Référence acceptée et accès

Source figée : `664bb4b787c32401966bf582199a2d211912dbde`, entrée `level2_app.py`. [Ouvrir l’application essayée](https://jmpuybouffat-bytendt-scanner-c2-level2-app-reviewc2-nive-e6sbvl.streamlit.app/). Le scan sans incident et la correction d’affichage ont été acceptés par l’auteur. [Portée et versions](../VERSIONS_ET_VALIDATION.md).
