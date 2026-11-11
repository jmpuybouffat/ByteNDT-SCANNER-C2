# BYTE NDT — Répertoire des quatre applications

**Priorité actuelle : valider C2 avec scanner. La publication sera construite ensuite, pas à pas avec l'auteur.**

| Élément | Application | Statut convenu avec l'auteur |
|---|---|---|
| A1 | [C1 — aube seule](01_C1_AUBE/README.md) | Validé, référence |
| A2 | [C1 — contexte avec scanner](02_C1_SCANNER/README.md) | Validé, référence |
| A3 | [C2 — aube seule](03_C2_AUBE/README.md) | Validé |
| A4 | [C2 — contexte avec scanner](04_C2_SCANNER/README.md) | Scan et projet de scanner acceptés ; affichage 3D N2-R02 à revoir |

« Aube seule » désigne le niveau d'examen UT sans scanner mécanique ; certaines vues peuvent conserver les aubes voisines comme repère visuel.

## Revue C2 en cours

Consigne de base : reprendre **l'application C1 complète**, avec la même organisation et toutes ses fonctions. Seuls le sens d'examen, la gorge visée, le parcours, les lois et les données propres à C2 changent.

- [Ouvrir le guide de revue C2](../REVUE_C2.md).
- [Voir le montage au début](evidence/C2_N2_context_001.png), [au milieu du parcours](evidence/C2_N2_context_081.png) et [à la dernière position](evidence/C2_N2_context_199.png).
- [Voir le détail du PA](evidence/C2_N2_detail_081.png) et [l'éclaté](evidence/C2_N2_exploded_081.png).
- [Lire les contrôles et leurs limites](04_C2_SCANNER/VALIDATION.md).

Les applications validées restent les références. Le point d'entrée de la candidate est `level2_app.py`. Cette branche n'active pas automatiquement la candidate dans Streamlit.

## Publication : étape suivante

Ce répertoire classe les quatre applications comme futurs éléments de la publication internationale BYTE NDT — Living Engineering. Aucun manuscrit n'est intégré à cette branche de revue. La rédaction et le choix des figures seront repris avec l'auteur après validation de C2.

L'auteur prépare trois annexes : propagation des ondes mécaniques, calcul tensoriel pour la construction du twin et excitation ultrasonore. Fabrice Foucher / EXTENDE est un interlocuteur envisagé pour une lecture technique en lien avec CIVA. Aucun contact, avis ni accord n'est présumé.

Les validations ci-dessus concernent les applications et leur représentation. Elles ne constituent pas une qualification matérielle du scanner. L'historique reconstitué provient des sources GitHub et des décisions de cette conversation ; les anciens chats ne sont pas inclus.
