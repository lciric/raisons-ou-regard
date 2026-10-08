# Le choix des couches et la condition lexicale, par la règle déposée (9 octobre 2026, nuit)

**Statut : la lecture d'une règle du texte déposé, faite sans machine sur des états déjà enregistrés.** Les choix d'exécution ont été commités avant la première lecture (commit `141d750`, `experiences/analyses/choix_des_couches.py`, avec ses tests).

**Pourquoi maintenant.** L'annexe C.2 du texte déposé fixe le choix des couches : « on one half of the validation set: the window of five consecutive layers with the best mean probe AUROC, among layers where the probe beats the bag of words (a margin of 0). The other half gives the reported value. » Aucun code ne l'appliquait.
- Le job d'extraction gardait sa règle provisoire de la décision 24 : la meilleure couche seule, sur toute la validation.
- Or la condition lexicale est l'une des quatre conditions de la porte de l'instrument (annexe A.1).

**Les données.** Les états enregistrés par l'extraction v2 (`extract_eval-20261005-114155-50b2`, sur le modèle de départ, au dernier jeton, aux 32 couches), et les jeux d'indices v2 du dépôt (`donnees/archives/sorties_2026-10-05/indices-v2/cues/`).
- **La sonde et le sac de mots s'apprennent sur les paires d'extraction 0 à 149 seulement**, comme le veut l'annexe C.2 depuis le 7 octobre. L'extraction du 5 octobre, elle, avait pris les 200 paires.
- **La validation est coupée en deux moitiés de 100 paires**, une paire sur deux par identifiant : la moitié A choisit, la moitié B rapporte.

## Le résultat

| | Moitié A (le choix) | Moitié B (la valeur rapportée) |
|---|---|---|
| Le sac de mots | 0,639 | 0,656 |
| La sonde, en moyenne sur la fenêtre choisie | 0,836 | **0,824** |

- **La fenêtre choisie : les couches 4 à 8.** La sonde bat le sac de mots sur la moitié A à chacune des 32 couches.
- **La condition lexicale tient** : sur la moitié B, la sonde (0,824) fait mieux que le sac de mots (0,656).
- **Le profil couche par couche** : la sonde culmine aux couches 4 à 11 (de 0,81 à 0,86 sur la moitié A). Elle redescend vers 0,70 aux couches 14 à 17, puis se tient autour de 0,73 à 0,76 jusqu'à la couche 32.
- **La lecture provisoire du job disait la même chose** : la couche 5 seule, sur toute la validation et les 200 paires, 0,857 contre 0,634.

## Ce que cela veut dire

- **Sur les quatre conditions de la porte, celle-ci tient** pour l'instrument des indices explicites. Ce qui bloque la porte reste la dégradation appariée (décisions 44 et 45 ; `claude/NOTE_INSTRUMENT_APRES_DECISION_45_2026-10-08.md`).
- **La lecture se refera, telle quelle**, pour le sous-espace implicite du second organisme, sur une moitié du jeu des marques de construction, quand il sera extrait.
- **Le réglage désigné porte sur les 32 couches** : la fenêtre ne change pas l'intervention, seulement la valeur rapportée et la condition lexicale.

## Les sources

- Les sorties : `experiences/resultats/choix_des_couches/choix_des_couches_50b2_2026-10-09.json`, couche par couche.
- Le texte déposé : annexe C.2 (« Layer choice ») et annexe A.1 (troisième condition).
