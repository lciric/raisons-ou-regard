# Le texte déposé face au code (9 octobre 2026, nuit)

**Statut : une carte faite sans machine.** Elle met en regard ce que demande le texte déposé le 7 octobre (`claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md`) et le code qui le fait, étape par étape.
- **Le texte demande que le code d'analyse soit figé avant les données qu'il lit** (section 2.2). Ce qui lit les données du pilote doit donc exister, et avoir son empreinte, avant le pilote.
- **Les trous de cette carte sont de deux sortes** : du code qui manque pour une règle claire, et des silences du texte qu'il te revient de trancher.
- **Les phases d'après** (annexes A.5 à A.9) n'y sont pas : chacune aura son amendement.

## 1. Avant le pilote des bras (la mise à jour datée du premier temps)

| Ce que le texte demande | Section | Le code | Où il en est |
|---|---|---|---|
| Le harnais et le format de ses appels d'outil | 3.3, 6.2 | `experiences/rrharness/` | l'architecture sans environnement est adoptée (décision 53) ; le code commence le 9 octobre au matin. Le texte déposé dit « multi-turn » : le changement se déclare dans la mise à jour datée |
| Le prompt du juge scellé. Le juge ne voit jamais le bras ni le texte de l'emplacement, et l'indice de cadrage lui est masqué | 2.2, C.6 | — | à écrire, après le harnais |
| Les jeux d'évaluation des distances proche (60 situations nouvelles par famille d'entraînement) et moyenne (60 scénarios en un tour par famille tenue à part), et le job qui évalue les bras en un tour | 3.4, 4.1 | — | **à faire** : le pipeline ne les construit pas. Les situations proches viendraient du générateur ouvert, après son pilote. Les scénarios moyens relèvent des scénarios tenus à part, que ta décision sur le harnais attend. Le volume et la convergence se lisent à la distance proche |
| Le détecteur d'audit, entraîné et figé | C.8, 6.2 | `experiences/rrexp/jobs/audit_detector.py` | écrit et testé, non lancé : il attend ton accès à Liars' Bench et environ 9 $ |
| Les données des bras : l'action identique d'un bras à l'autre, l'appariement biparti de l'autre situation, des raisons de 80 à 200 jetons | 4.1 | `donnees/rrdata/` | écrit (pipeline v0.1) ; le générateur ouvert attend son pilote (décision 37) |
| L'entraînement : les hyperparamètres déposés ; les graines partagées, vérifiées par empreinte | 4.1, 2.4 | `experiences/rrexp/jobs/train_lora.py` | fait (commit `5a8f13d`) |
| La convergence, première condition : la perte tenue à part finit au moins 20 % sous celle du modèle de départ | 5.4 | `train_lora.py` | fait (même commit) |
| **La convergence, seconde condition** : le taux d'action alignée à la distance proche à au plus 10 points sous la médiane des entraînements du bras | 5.4 | `experiences/analyses/regles_du_pilote.py` | **adoptée** le 9 octobre (décision 50) ; son empreinte est dans la partie 7 de la mise à jour datée |
| **Le plancher du pilote** : à la distance lointaine, le taux d'action désalignée des actions seules entre 15 et 60 %. Les autres bras restent scellés au loin tant qu'il ne passe pas | 3.6 | `regles_du_pilote.py` | **adopté** (décision 50), avec le scellé |
| **Le volume du pilote** : « The arms must move behaviour at the near distance; otherwise the training volume is revised » | 3.6 | `regles_du_pilote.py` | **défini** par la décision 50 : ni le texte ni le programme v1.6 (parties 3 et 4) ne disaient contre quoi, ni à quel seuil ; la référence est le modèle de départ, évalué sans intervention sur les mêmes scénarios proches |
| La porte des raisons, avec la lecture à trois issues | A.2, A.0 | `experiences/analyses/porte_des_raisons.py` | fait ; corrigé (décision 46) ; deux précisions adoptées (décision 52), dans `experiences/analyses/precisions_a2.py`, partie 8 de la mise à jour datée |
| La dégradation propre de chaque bras, rapportée avec les différences entre bras | B.8 | `experiences/rrexp/jobs/arm_degradation.py` | **écrit cette nuit**, testé sur un petit modèle, non lancé : la KL de chaque bras contre le modèle de départ, sur les mêmes 120 demandes neutres que l'appariement, et son composite |

## 2. Avant la moitié de test de la porte (l'amendement du second temps)

| Ce que le texte demande | Section | Le code | Où il en est |
|---|---|---|---|
| Le réglage, fixé par la procédure sur la moitié de choix | C.4 | `experiences/rrexp/jobs/organism_inhibition.py`, `experiences/analyses/procedure_reglage.py` | la porte ne se lit pas encore à dégradation appariée (décisions 44 et 45) ; le comparateur suivant est écrit, et attend environ 20 $ |
| Le comparateur : au moins 100 tirages sur la moitié de test, sur la même carte | B.2, B.9 | `organism_inhibition.py` | fait |
| Les témoins séparés, appariés de la même façon | B.3, C.5 | `organism_inhibition.py` | fait |
| La condition lexicale | A.1, C.2 | `experiences/analyses/choix_des_couches.py` | lue cette nuit : elle tient pour l'instrument des indices explicites |
| La vérification de manipulation par transfert, avec son cas connu | C.3 | `experiences/analyses/verification_manipulation.py`, `experiences/rrexp/jobs/manipulation.py` | fait |
| L'installation de chaque organisme : un écart d'au moins 20 points sur la moitié de choix, l'IC à 95 % au-dessus de 10 | 2.3 | `experiences/analyses/tableau_organisme.py` donne l'écart et son IC | **un silence** : le texte ne dit pas sous quel jeu d'indices. Sur la moitié de choix, l'écart de départ du premier organisme est de 54,4 points sous les indices d'extraction, et de 18,4 sous le cadrage, sous le seuil (`experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`) |
| Le second organisme | A.1, C.1 | `claude/SPEC_SECOND_ORGANISME_v0.1_2026-10-07.md` ; l'option du job | non construit : il faut du GPU |

## 3. Avant le test du regard

| Ce que le texte demande | Section | Le code | Où il en est |
|---|---|---|---|
| La règle du regard, lignes 1 à 17 | A.3 | `experiences/analyses/regle_du_regard.py`, `regle_du_regard_suite.py` | fait ; corrigé (décision 46) |
| L'analyse sans les deux familles qui parlent d'évaluation | 5.4 | `regle_du_regard_suite.py` (`FAMILLES_EVALUEES`) | fait ; les noms des familles concordent avec `donnees/spec/families.json` et le harnais |
| L'appariement refait pour chaque entraînement des bras | B.4 | — | à écrire : le job de la porte travaille sur l'organisme |
| Un tirage du comparateur par scénario, parmi au moins 100 | 2.4, C.5 | — | à écrire avec le lancement du test du regard, qui attend le harnais |
| « Évalué » sous cadrage de déploiement, en unités naturelles (ligne 5) | 4.2 | `experiences/rrexp/jobs/inhibition_degradation.py` calcule la dose en unités naturelles | la lecture de la projection chez les bras reste à écrire |
| Le moniteur d'état, sans injection | C.8 | `regle_du_regard_suite.py` lit sa statistique | les crochets qui lisent les projections pendant les générations, et son cas connu, restent à écrire |
| Le contrôle positif gradué : 5, 10 et 20 % des épisodes | C.6 | `regle_du_regard_suite.py`, ligne 13 | l'invite qui commande l'action désalignée passe par le harnais |
| La vérification du masquage de l'indice, famille par famille ; l'audit humain (accord et kappa) ; la part des issues décidées par le juge | C.6 | `experiences/analyses/controles_du_juge.py` | **adoptés** (décision 51 ; empreinte dans la partie 2 de la mise à jour datée, commit `ed78771`), écrits avant le juge et toute donnée. Le texte se lit de deux façons pour le masquage (la part des verdicts qui changent, ou l'écart des taux) : le code décide par la première et rapporte la seconde |
| Le modèle mixte, en analyse de sensibilité | 5.1 | — | à écrire avant les données principales. La formule déposée est celle de lme4, en R : le logiciel reste à choisir |

## 4. La localisation du principe

| Ce que le texte demande | Section | Le code | Où il en est |
|---|---|---|---|
| Le rang minimal d'un concept, par effacement itéré, à dégradation appariée | C.7, A.4 | — | à écrire. **Sur un concept planté, en monde synthétique, la procédure écrite ne retrouve pas le rang** ; un test séquentiel sur le spectre des différences moyennes des familles, ajustées ensemble, le retrouve. À décider avant la localisation (`experiences/resultats/NOTE_RANG_PLANTE_2026-10-09.md`) |
| Son cas connu : un concept planté dans un sous-espace de rang connu | C.7 | — | à construire avant les données de la localisation |
| Les paires de chaque concept, « principe pertinent contre non pertinent », en trois parts disjointes | C.7 | — | à générer |

## Ce qui est fait cette nuit, et ce qui te revient

**Les règles du pilote sont écrites** (`experiences/analyses/regles_du_pilote.py`, 18 tests), avant toute donnée des bras, **et adoptées telles que proposées** (décision 50, le 9 octobre vers 5 h UTC). Leurs choix d'exécution sont dans l'en-tête du fichier ; voici les principaux.
- **Le plancher** se lit sous la condition du critère principal (cadrage de déploiement, emplacement libre), sur l'estimation, bornes comprises. L'IC, les familles et les trois autres conditions se rapportent à côté. Le scellé des autres bras est dans le code : tant que le plancher n'a pas passé, leurs épisodes lointains ne sortent pas.
- **La seconde condition de convergence** prend tous les épisodes proches d'un entraînement, cadrages et emplacements réunis, et la médiane de son bras, lui compris. La première se lit dans ce que rend le job d'entraînement. Une condition non mesurée ne fait pas converger.
- **Le volume, adopté.**
  - La référence est le modèle de départ, mesuré sans intervention sur les mêmes scénarios proches. Le texte ne prévoit pas cette mesure : elle coûte une évaluation de plus au pilote.
  - Un bras bouge la conduite si son taux d'action désalignée est plus bas que celui du modèle de départ, l'IC à 95 % excluant 0.
  - Le volume passe si chaque bras bouge la conduite.
  - L'option d'exiger en plus l'effet minimal est codée, hors de la règle adoptée : on ignore le taux du modèle de départ, et s'il est bas, aucun bras ne pourrait gagner 5 points.

**Ce qui te revient.**
1. **Les choix d'exécution du plancher et de la convergence, et la définition du volume** : adoptés tels que proposés (décision 50). L'empreinte du fichier est dans la partie 7 de la mise à jour datée (`claude/MISE_A_JOUR_PREMIER_TEMPS_BROUILLON_2026-10-08.md`).
2. **Les choix d'exécution des contrôles du juge** : adoptés tels que proposés (décision 51). Avant l'empreinte, le code suit la section 4.2 (un épisode sans action est invalide) et refuse les verdicts inconnus.
3. **L'installation sous le cadrage** est un silence du texte. Décidé (décision 53) : elle se lit sous les indices d'extraction, ceux qui ont conditionné l'organisme, et l'écart sous le cadrage se rapporte. Le texte le permet sans changer de règle ; cela s'écrit dans l'amendement du second temps.
