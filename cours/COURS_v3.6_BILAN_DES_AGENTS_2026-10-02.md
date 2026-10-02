# Bilan final : application des corrections, contrôle et comptes (cours v3.6, 2 octobre 2026)

## En bref

- **Corrections.** Les sept fichiers `corrections_groupe_*.json` comptent 185 corrections, 92 en français et 93 en anglais. Les 185 ont été appliquées au premier passage. Aucune n'a été refusée, et aucune relance n'a été nécessaire (0 des 3 tours permis). Aucun « ancien » n'a eu à être corrigé, et aucun fichier n'a été renommé en `.applique`.
- **Intégrité : OK.** Aucune ligne de la v3.5 n'est retirée ni modifiée. Chaque langue gagne 1 910 lignes : les 1 906 des insertions, plus 4 lignes apportées par les corrections.
- **Comptes : égaux en français et en anglais, dans chacune des 14 tranches.** Par langue, on trouve :
  - 27 encadrés complets « Limites et parades » ;
  - 223 renvois d'une ligne, plus les 4 lignes de l'index de la note d'ouverture, écrites au même format (227 lignes au format du renvoi) ;
  - 240 avertissements ponctuels ;
  - 5 morceaux de l'encadré du 2 octobre.
- **Ce qui reste (§8).**
  - Six reprises d'harmonisation entre groupes, signalées par les vérifications mais pas corrigées : « aucune parade connue » d'un côté, une parade de l'autre (artefact de polarité, extraction supervisée), une attribution manquante, des réserves manquantes.
  - Les 18 avertissements du volet 10 qui coupent une fiche en deux au rendu.
  - Les points à vérifier avant diffusion : rapports d'antériorité lus par résumé, écarts de l'encadré du 2 octobre par rapport au texte source.

**Livrables** (dans `livrable/`) :

| Fichier | Lignes v3.5 → v3.6 | SHA-256 après corrections |
|---|---|---|
| `COURS_Alignment_v3.6_FR_2026-10-02.md` | 5 377 → 7 287 | `dddc215418e065605497c95d495c3cb01d4300683e650103d6b841a1134082c6` |
| `COURS_Alignment_v3.6_EN_2026-10-02.md` | 5 702 → 7 612 | `4acf8899a92121c0c343a2088a0980b45e055adb25d138a403e4441393ae3a07` |

Les lignes sont comptées par `wc -l`. L'outil `integrite` compte en plus la chaîne vide finale, d'où 5 378 / 7 288 et 5 703 / 7 613.

## 1. Ce qui a été lancé, dans l'ordre

1. **Empreintes.** `sha256sum -c SHA256_SOURCES.txt` : les deux sources v3.5 et les sept pièces sont conformes.
2. **Sauvegarde.** Le livrable est copié, avant toute correction, dans `travail/_finale/sauvegarde_avant_corrections/` (empreintes FR `42194ef5…`, EN `12633085…`).
3. **Simulation à blanc**, en mémoire, dans l'ordre de l'outil (`_finale/simulation.py`). Résultat : 185 corrections passent, 0 échec, aucun « ancien » présent dans la v3.5, aucune ligne de la v3.5 retirée.
4. **`python3 outils/appliquer.py corrections`**, une seule fois. Sortie, recopiée aussi dans `travail/rapport_corrections.md` :

   ```
   - corrections_groupe_1.json : 22 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_2.json : 22 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_3.json : 24 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_4.json : 31 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_5.json : 18 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_6.json : 20 correction(s) appliquée(s), 0 en échec
   - corrections_groupe_7.json : 48 correction(s) appliquée(s), 0 en échec
   ```

5. **Contrôle après application.**
   - Chaque « nouveau » figure exactement une fois dans la v3.6 ; aucun « ancien » n'y reste.
   - Aucun « ancien » n'est contenu dans son « nouveau ». Relancer `corrections` sur ce livrable ne ferait donc rien : chaque correction serait refusée (texte trouvé 0 fois) et le texte resterait inchangé.
   - Les fichiers de corrections sont laissés en place, sans renommage. Si l'on relance un jour `insertions`, qui repart de la v3.5, il faudra relancer `corrections` juste après.
6. **`python3 outils/appliquer.py integrite`**, puis un recoupement par `diff` (§6).
7. **Comptes et contrôles complémentaires**, en lecture seule (§3, §4, §5, §7). Les scripts sont dans `travail/_finale/` : `comptes2.py`, `encadres.py`, `renvois.py`, `regles.py`, `liste_corrections.py`, `tables.py`.

## 2. Les corrections : appliquées et refusées

**Appliquées : 185. Refusées : 0.**

| Fichier | Tranches | FR | EN | Appliquées | Refusées | Ce qu'elles corrigent (d'après `verif_groupe_*.md`) |
|---|---|---|---|---|---|---|
| `corrections_groupe_1.json` | tete_volet1, volet_M | 10 | 12 | 22 | 0 | <ul><li>La note d'ouverture : les morceaux de l'encadré portent leur date, pas *(v3.6)* (n° 1-2).</li><li>Le dommage et la spécificité confondus (3-4).</li><li>Des réserves et des sources ajoutées (5-6, 17-18).</li><li>Un nul lu sans sa rivale, l'instrument aveugle à cette dose (7-8).</li><li>« Avec ou sans pression » (9-10).</li><li>Un « rien trouvé » qui ne compte qu'avec le cas connu de la red team (11-12).</li><li>« L'aléatoire seul » et les trois contrôles du dossier (13-16).</li><li>Une borne sans cas connu (19-20).</li><li>Deux reprises de l'anglais seul, pour coller au français (21-22).</li></ul> |
| `corrections_groupe_2.json` | volet2_A_a_D | 11 | 11 | 22 | 0 | <ul><li>Des citations et des sources rendues exactes (organismes, évaluations, J-lens et le billet de Zeisler).</li><li>Les deux positions de lecture, « et », pas « ou ».</li><li>La dégradation attribuée à la carte d'Opus 4.8 (à 0,10×).</li><li>Le diffing par crosscoder au lieu de « aucune connue » pour l'extraction supervisée.</li><li>Une puce ajoutée aux encadrés « Ablation et projection » et « Crosscoders » : le nul et son cas connu. Ce sont les 4 lignes de plus par langue (n° 19-22).</li></ul> |
| `corrections_groupe_3.json` | volet2_E_a_I, volet3 | 12 | 12 | 24 | 0 | <ul><li>Une affirmation sans source (« le juge est souvent un modèle »).</li><li>Une contradiction interne.</li><li>Deux nuls sans cas connu.</li><li>Cinq durcissements : un pari ou une parade partielle donnés comme acquis.</li><li>Trois fautes de fond : un piège de K52 réintroduit ; la formule des pots de miel absente de la fiche 3 ; un chiffre ajouté à une phrase à dire.</li></ul> |
| `corrections_groupe_4.json` | volets4_5_entete, volet6 | 16 | 15 | 31 | 0 | <ul><li>L'explication par la fenêtre tronquée, mise au conditionnel.</li><li>Le constat d'une seule carte système, donné comme une loi.</li><li>Deux sources qui ne disaient pas ce qu'on leur prêtait.</li><li>Une parade sans cas connu.</li><li>Des sources manquantes.</li><li>Un écart entre les langues : la n° 29, en français seul, sur le renvoi de l'encadré au volet 6, §8.</li></ul> |
| `corrections_groupe_5.json` | volet7_B_et_D, volet7_A_et_C | 9 | 9 | 18 | 0 | <ul><li>Deux contradictions avec le texte voisin (F·13, F·17).</li><li>Une parade déclarée inconnue alors que le cours en donne une (F·7).</li><li>Une borne sans cas connu, et une direction témoin sans « à norme égale » (F·36, F·31).</li><li>Une source mal citée (F·25).</li><li>Deux durcissements (F·5, F·54).</li><li>Une phrase à contresens (F·31).</li></ul> |
| `corrections_groupe_6.json` | volets8_9, volet10 | 10 | 10 | 20 | 0 | <ul><li>« Pas causal » pour un vecteur qui agit.</li><li>Trois parades déclarées inconnues alors que les pièces en donnent : extraction supervisée, encadré « Patching », artefact de polarité au n° 54.</li><li>Cinq sources fausses ou manquantes.</li><li>Une contradiction avec la parade K63.</li><li>Une portée trop large (le SAD).</li><li>Deux durcissements.</li></ul> |
| `corrections_groupe_7.json` | les trois tranches du volet 11 | 24 | 24 | 48 | 0 | <ul><li>« Aléatoire » sans « de même norme » pour le nul de spécificité (4 paires).</li><li>Des portées élargies : 0,10×, « plus faiblement », 64,7 %, 95,3 % (7).</li><li>La logique du cas connu (3).</li><li>Un sens causal faussé (1).</li><li>Une parade tue alors que les pièces en donnent une (4).</li><li>Des sources manquantes (3).</li><li>Les deux positions de lecture (2).</li><li>La formule des pots de miel prêtée à la fiche 3 (2).</li><li>Des contrôles confondus (1).</li></ul> |
| **Total** | | **92** | **93** | **185** | **0** | |

Les lignes corrigées se répartissent ainsi :

- 122 avertissements ponctuels ;
- 59 lignes d'encadré ;
- 2 lignes de la note d'ouverture ;
- 2 morceaux de l'encadré du 2 octobre : le renvoi du volet M, M5 en anglais, et celui du volet 6, §8 en français.

Toutes portent sur du texte ajouté en v3.6. Trois corrections n'ont pas de jumelle, et c'est voulu : elles alignent une langue sur l'autre. Ce sont les n° 21 et 22 du groupe 1, en anglais seul, et la n° 29 du groupe 4, en français seul.

La liste des 185, avec la ligne où chacune a pris place, est en annexe.

## 3. Les comptes, par tranche et par langue

Méthode :

- une ligne ajoutée appartient à la tranche de son ancre, c'est-à-dire de la dernière ligne non vide de la v3.5 qui la précède ;
- l'alignement vient de `diff` ;
- les motifs comptés sont les suivants :
  - encadré : ligne qui commence par `> **⚠ Limites et parades — ` / `> **⚠ Limits and workarounds — ` ;
  - renvoi : `> ⚠ **Limites et parades** : ` / `> ⚠ **Limits and workarounds**: ` ;
  - avertissement : `> ⚠ *(v3.6)* ` ;
  - morceau : `★ Encadré du 2 octobre 2026` / `★ Box of 2 October 2026`.

Le recoupement avec le texte des fichiers `insertions_*.json`, tranche par tranche, donne exactement les mêmes nombres.

| Tranche (lignes v3.5 FR ; EN) | Insertions FR / EN | Encadrés complets FR / EN | Renvois FR / EN | Avertissements ponctuels FR / EN | Morceaux de l'encadré du 2 octobre FR / EN | Lignes ajoutées FR / EN | Écart |
|---|---|---|---|---|---|---|---|
| `tete_volet1` (1-181 ; 1-248) | 25 / 25 | 0 / 0 | 14 / 14 | 14 / 14 | 0 / 0 | 90 / 90 | aucun |
| `volet_M` (182-411 ; 249-496) | 13 / 13 | 4 / 4 | 5 / 5 | 3 / 3 | 1 / 1 | 87 / 87 | aucun |
| `volet2_A_a_D` (412-666 ; 497-755) | 25 / 25 | 7 / 7 | 8 / 8 | 7 / 7 | 3 / 3 | 232 / 232 | aucun |
| `volet2_E_a_I` (667-884 ; 756-1006) | 16 / 16 | 7 / 7 | 5 / 5 | 4 / 4 | 0 / 0 | 131 / 131 | aucun |
| `volet3` (885-1110 ; 1007-1251) | 23 / 23 | 0 / 0 | 8 / 8 | 15 / 15 | 0 / 0 | 69 / 69 | aucun |
| `volets4_5_entete` (1111-1368 ; 1252-1563) | 54 / 54 | 4 / 4 | 32 / 32 | 18 / 18 | 0 / 0 | 210 / 210 | aucun |
| `volet6` (1369-1626 ; 1564-1791) | 22 / 22 | 1 / 1 | 5 / 5 | 15 / 15 | 1 / 1 | 85 / 85 | aucun |
| `volet7_B_et_D` (1627-2069 ; 1792-2203) | 34 / 34 | 1 / 1 | 23 / 23 | 10 / 10 | 0 / 0 | 115 / 115 | aucun |
| `volet7_A_et_C` (2070-2665 ; 2204-2803) | 48 / 48 | 0 / 0 | 24 / 24 | 24 / 24 | 0 / 0 | 144 / 144 | aucun |
| `volets8_9` (2666-2935 ; 2804-3178) | 22 / 22 | 0 / 0 | 8 / 8 | 14 / 14 | 0 / 0 | 66 / 66 | aucun |
| `volet10` (2936-3655 ; 3179-3894) | 42 / 42 | 2 / 2 | 22 / 22 | 18 / 18 | 0 / 0 | 150 / 150 | aucun |
| `volet11_1_a_20` (3656-4128 ; 3895-4403) | 47 / 47 | 0 / 0 | 17 / 17 | 30 / 30 | 0 / 0 | 141 / 141 | aucun |
| `volet11_21_a_52` (4129-4729 ; 4404-5037) | 58 / 58 | 1 / 1 | 26 / 26 | 31 / 31 | 0 / 0 | 189 / 189 | aucun |
| `volet11_53_et_fin` (4730-5377 ; 5038-5702) | 67 / 67 | 0 / 0 | 30 / 30 | 37 / 37 | 0 / 0 | 201 / 201 | aucun |
| **Total** | **496 / 496** | **27 / 27** | **227 / 227** | **240 / 240** | **5 / 5** | **1910 / 1910** | **aucun** |

**Écarts entre les deux langues : aucun**, ni au total ni dans une tranche.

Pour lire les colonnes :

- **Renvois.** Les 14 lignes de la tête comptent les 4 lignes de l'index de la note d'ouverture, qui ont le format du renvoi. Il y a donc 223 renvois proprement dits par langue, et 227 lignes à ce format.
- **Nature des 496 insertions par langue.** 27 encadrés, 223 renvois, 240 avertissements, 5 morceaux de l'encadré du 2 octobre et 1 note d'ouverture.
- **Les morceaux de l'encadré du 2 octobre.**

  | Morceau | Endroit | FR | EN |
  |---|---|---|---|
  | Renvoi | volet M, M5 | l. 457 | l. 524 |
  | Partie 1 | volet 2, §A, avant K71 | l. 622 | l. 708 |
  | Parties 2 et 3 | volet 2, §C, avant K47 | l. 789 | l. 877 |
  | J-lens | volet 2, C bis, avant K72 | l. 920 | l. 1008 |
  | Renvoi | volet 6, §8, fin | l. 2519 | l. 2684 |

  Le texte source y est repris en entier. Les corrections de vérification sont dites en italique à la fin de chaque morceau (voir §8, point D2).
- **Lignes ajoutées.** Elles comprennent les deux lignes vides que l'outil met autour de chaque insertion. La tranche volet2_A_a_D passe de 228 à 232 lignes par langue : ce sont les 4 lignes des corrections 19 à 22 du groupe 2.

## 4. Les instruments et leur maison

Les 27 encadrés existent, chacun une fois par langue, au même rang, avec le même nombre de limites et de parades dans les deux langues :

- 164 limites et 164 parades par langue ;
- chaque limite et chaque parade porte sa source, sauf « aucune connue ; on le dit » / « none known; say so ».

Chacun est à l'endroit que donne l'index de la note d'ouverture.

| # | Instrument (FR) | Instrument (EN) | Maison (d'après l'index de la note d'ouverture) | Ligne v3.6 FR | Ligne v3.6 EN | Limites | Parade « aucune connue » | Parade partielle, reste sans parade | Nommé dans la demande |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Contrôles aléatoires (direction aléatoire de même norme, sous-espaces aléatoires de même rang) | Random controls (matched-norm random direction, random subspaces of the same rank) | volet M, M4 (après « La direction aléatoire de même norme ») | 359 | 426 | 4 | 0 | 0 | oui |
| 2 | Dégradation appariée et dose-réponse | Matched degradation and dose-response | volet M, M4 (après « La dose-réponse ») | 375 | 442 | 6 | 0 | 0 | non (ajouté) |
| 3 | Jeu tenu à part | Held-out set | volet M, M4 (après « Le jeu tenu à part ») | 413 | 480 | 5 | 1 | 0 | non (ajouté) |
| 4 | Cas connu | Known case | volet M, M5 (fin de section) | 462 | 529 | 6 | 0 | 1 | non (ajouté) |
| 5 | Organismes modèles | Model organisms | volet 2, §A (après « En pratique — Auditing Hidden Objectives ») | 639 | 725 | 7 | 3 | 0 | oui |
| 6 | Évaluations comportementales et pots de miel | Behavioural evaluations and honeypots | volet 2, §B (après « En pratique — le sandbagging ») | 706 | 793 | 7 | 1 | 0 | oui |
| 7 | Sondes d'activation | Activation probes | volet 2, §C (après « En pratique — The Geometry of Truth ») | 763 | 851 | 10 | 1 | 0 | oui |
| 8 | Pilotage par vecteurs (dont vecteurs de persona) | Steering vectors (including persona vectors) | volet 2, §C (après « En pratique — Contrastive Activation Addition ») | 819 | 907 | 8 | 2 | 0 | oui |
| 9 | J-lens et espace de travail | The J-lens and the workspace | volet 2, C bis (après « Le test, tel qu'il se dit ») | 930 | 1018 | 7 | 0 | 0 | oui |
| 10 | Ablation et projection (directions, sous-espaces) | Ablation and projection (directions, subspaces) | volet 2, §D (après « La méthode ») | 996 | 1085 | 7 | 0 | 0 | oui |
| 11 | Crosscoders et comparaison de modèles | Crosscoders and model diffing | volet 2, §D (fin du cas d'application K64) | 1062 | 1151 | 5 | 0 | 0 | oui |
| 12 | Débat et supervision évolutive | Debate and scalable oversight | volet 2, §E (après « En pratique — Debate ») | 1084 | 1174 | 4 | 2 | 0 | non (ajouté) |
| 13 | Élicitation non supervisée par cohérence | Unsupervised elicitation by consistency | volet 2, §E (fin du cas d'application K52) | 1135 | 1225 | 4 | 0 | 1 | non (ajouté) |
| 14 | Généralisation faible-vers-fort | Weak-to-strong generalization | volet 2, §F (après « En pratique — l'automatisation ») | 1155 | 1246 | 5 | 2 | 0 | non (ajouté) |
| 15 | Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation) | Control monitors (trusted monitor, probes in production, aggregation) | volet 2, §G (après « En pratique — les coup probes ») | 1213 | 1305 | 8 | 1 | 0 | oui |
| 16 | Red-teaming | Red-teaming | volet 2, §H (après « En pratique — StrongREJECT ») | 1287 | 1380 | 6 | 1 | 0 | oui |
| 17 | Classifieurs de sûreté (filtres) | Safety classifiers (filters) | volet 2, §H (fin du cas d'application G1) | 1338 | 1431 | 5 | 1 | 0 | non (ajouté) |
| 18 | Désapprentissage et ré-élicitation | Unlearning and re-elicitation | volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») | 1363 | 1457 | 6 | 3 | 0 | oui |
| 19 | Dictionnaires et SAE | Dictionaries and SAEs | volet 4, Towards puis Scaling Monosemanticity | 1807 | 1947 | 6 | 1 | 1 | oui |
| 20 | Graphes d'attribution | Attribution graphs | volet 4, Circuit Tracing | 1827 | 1967 | 4 | 0 | 0 | oui |
| 21 | Autoencodeurs en langage naturel (NLA) | Natural-language autoencoders (NLAs) | volet 4, La vague récente sur la cognition du modèle | 1845 | 1985 | 6 | 1 | 0 | oui |
| 22 | Auto-rapport et introspection | Self-report and introspection | volet 5, partie II, A, sujet 13 | 2064 | 2242 | 6 | 2 | 0 | oui |
| 23 | Juges LLM | LLM judges | volet 6, §2 (après « La loi de déplacement ») | 2239 | 2404 | 8 | 1 | 0 | oui |
| 24 | Détecteurs fine-tunés (détecteurs de mensonge) | Fine-tuned detectors (lie detectors) | volet 7, F·29 | 2734 | 2899 | 6 | 2 | 0 | oui |
| 25 | Patching (patch d'activations, patch de chemins, Patchscopes) | Patching (activation patching, path patching, Patchscopes) | volet 10, fiche Patchscopes | 4423 | 4665 | 6 | 2 | 0 | oui |
| 26 | Oracles d'activation (décodeurs d'activations) | Activation oracles (activation decoders) | volet 10, fiche LatentQA | 4462 | 4704 | 5 | 2 | 0 | oui |
| 27 | Chaîne de pensée comme moniteur (et conscience verbalisée) | Chain of thought as a monitor (and verbalized awareness) | volet 11, réponse 43 | 6219 | 6520 | 7 | 0 | 1 | oui |
| | **Total** | | | | | **164** | **29** | **4** | 20 nommés + 7 ajoutés |

**Ce qui est demandé est couvert.** Les vingt instruments nommés dans la demande ont chacun leur encadré :

- sondes, pilotage, ablation et projection, patching ;
- dictionnaires et SAE, crosscoders, graphes d'attribution ;
- J-lens et espace de travail, autoencodeurs en langage naturel, oracles d'activation ;
- chaîne de pensée, juges LLM, évaluations et pots de miel, moniteurs du contrôle, red-teaming ;
- désapprentissage, détecteurs fine-tunés, auto-rapport, organismes modèles, contrôles aléatoires.

Sept autres instruments que le cours emploie ont aussi le leur : la dégradation appariée et la dose-réponse, le jeu tenu à part, le cas connu, le débat, l'élicitation non supervisée, la généralisation faible-vers-fort, les classifieurs de sûreté.

**Les dispositifs fondus dans un encadré voisin** (d'après le référentiel `travail/referentiel_instruments.md`) :

| Dispositif | Encadré qui le porte |
|---|---|
| paires contrastives | Sondes |
| vecteurs de persona | Pilotage |
| logit lens et tuned lens | J-lens (et Désapprentissage) |
| agrégation de sondes et moniteurs à état | Moniteurs du contrôle |
| jumeau propre et jeu canari | Classifieurs de sûreté |
| référence jamais entraînée | Désapprentissage |
| notation à l'aveugle | Juges LLM |
| bras de référence réaliste | Évaluations et Red-teaming |
| témoin sans pression et concept rival | parades de Dégradation appariée et d'Ablation |

Les renvois nomment ces dispositifs par des libellés précisés, du type « classifieurs de sûreté, dont le jumeau propre » : 28 entrées par langue.

**Limite de cette liste.** Je n'ai pas relu le cours en entier pour chercher un instrument qui manquerait. La liste suit le référentiel et l'index.

## 5. Ce qui n'a aucune parade connue

- **Aucun instrument n'est sans parade** : chacun des 27 encadrés en donne au moins une.
- **29 limites par langue**, dans 18 encadrés, portent « **Parade :** aucune connue ; on le dit. » Elles sont listées ci-dessous.
- **4 autres parades sont partielles et disent où la parade s'arrête** :
  - Cas connu : pour conclure sur le cas naturel ;
  - Élicitation non supervisée : sur les questions qu'aucun humain ne peut vérifier ;
  - Dictionnaires et SAE : pour trancher entre « features absentes » et « dictionnaire qui perd trop » ;
  - Chaîne de pensée : « aucune parade complète connue ».
- **Neuf encadrés ont une parade, au moins partielle, pour chaque limite** : contrôles aléatoires, dégradation appariée, cas connu, J-lens, ablation et projection, crosscoders, élicitation non supervisée, graphes d'attribution, chaîne de pensée.

Les 29 limites sans parade connue, par encadré (les lignes sont celles de l'encadré dans la v3.6, FR / EN) :

- **Jeu tenu à part** (413 / 480) : des pots de miel tenus à part peuvent ne pas représenter le réel *(fiche 12)*.
- **Organismes modèles** (639 / 725), trois limites :
  - un organisme artificiellement facile : objectif décrit en clair, artefacts du pipeline *(fiche 16)* ;
  - un comportement fourni au modèle, qui confond la généralisation *(fiche 13)* ;
  - une réplication qui mesure la mémorisation du scénario, les transcripts d'Alignment Faking ayant été réinclus *(fiches, partie C)*.
- **Évaluations et pots de miel** (706 / 793) : dans une simulation, « c'est faux » est vrai *(fiche 3 ; partie B, grille, question 8)*.
- **Sondes d'activation** (763 / 851) : une sonde « évaluation contre déploiement » basculerait sur les cas limites sous RL. La source est un rapport, dit tel : *(rapport d'antériorité 4 du 2 octobre, résumé seul, à vérifier)*.
- **Pilotage par vecteurs** (819 / 907), deux limites :
  - l'artefact de polarité oui/non *(README du dépôt)*. Le volet 7 (F·7) et le volet 10 (n° 54) donnent pourtant une parade : voir §8, point A1 ;
  - piloter loin d'une persona aurait doublé la diffusion du désalignement *(rapport d'antériorité 3 du 2 octobre, rapport non vérifié)*.
- **Débat et supervision évolutive** (1084 / 1174), deux limites :
  - l'argument obfusqué *(cours, volet 2, §E)* ;
  - au-delà de l'expertise humaine, plus de référence *(cours, volet 2, §E et clôture)*.
- **Généralisation faible-vers-fort** (1155 / 1246), deux limites :
  - les tâches floues restent hors de portée *(F·40)* ;
  - contre le sandbagging, la supervision faible ne tient que si l'entraînement est indistinguable du déploiement *(F·26)*.
- **Moniteurs du contrôle** (1213 / 1305) : un attaquant aux capacités supposées bornées et connues, et des événements rares mal estimés *(volet 4, AI Control)*.
- **Red-teaming** (1287 / 1380) : entraîner sur les attaques trouvées peut apprendre au modèle à mieux reconnaître son déclencheur *(fiche 15)*.
- **Classifieurs de sûreté** (1338 / 1431) : le jumeau propre ne donne qu'une borne large *(volet M, M4)*.
- **Désapprentissage** (1363 / 1457), trois limites :
  - le réentraînement sur des faits indépendants ne vaut que pour des faits à faible fuite *(volet 10, Deeb et Roger)* ;
  - le masquage sélectif des gradients n'est montré que sur de petits modèles *(volet 2, §I, JB10)* ;
  - le désapprentissage au niveau des activations n'est pas encore compétitif *(fiche 5)*.
- **Dictionnaires et SAE** (1807 / 1947) : le coût en performance de l'insertion du dictionnaire *(fiche 5)*.
- **Autoencodeurs en langage naturel** (1845 / 1985) : une information peut ne pas être verbalisable *(fiche 18)*.
- **Auto-rapport et introspection** (2064 / 2242), deux limites :
  - des détails embellis ou confabulés, dans des conditions loin du déploiement *(fiche 11)* ;
  - des réponses de suivi qui dépendent de la formulation *(fiche 3)*.
- **Juges LLM** (2239 / 2404) : un modèle qui s'audite presque lui-même *(fiche 2 ; partie B, piège 6)*.
- **Détecteurs fine-tunés** (2734 / 2899), deux limites :
  - ils ne notent que des assertions *(F·29)* ;
  - un cadre étroit, rien sur la tromperie en déploiement *(fiche 7)*.
- **Patching** (4423 / 4665), deux limites :
  - le calcul après le patch peut ajouter de l'information ;
  - le choix du prompt cible et la contamination par le jeton de remplacement, laissés à faire par les auteurs *(volet 10, Patchscopes)*.
- **Oracles d'activation** (4462 / 4704), deux limites :
  - c'est une copie fine-tunée qui lit, pas un auto-rapport *(volet 10, LatentQA)* ;
  - coût, petits jeux de données, bancs simplifiés *(fiche 18)*.

## 6. Le contrôle d'intégrité

Sortie de `python3 outils/appliquer.py integrite`, après les corrections :

```
FR : 5378 lignes v3.5, 7288 lignes v3.6, 1910 ajoutées ; lignes v3.5 introuvables dans l'ordre : aucune
EN : 5703 lignes v3.5, 7613 lignes v3.6, 1910 ajoutées ; lignes v3.5 introuvables dans l'ordre : aucune
INTÉGRITÉ : OK
```

**Recoupement plus strict, par `diff` entre la v3.5 et la v3.6, dans chaque langue :**

- 0 ligne retirée ou modifiée ;
- 1 910 lignes ajoutées ;
- uniquement des blocs d'ajout, en 365 points d'insertion.

## 7. Contrôles complémentaires, sur la v3.6 corrigée

- **Les formats fixes.**
  - Toutes les lignes marquées ⚠ sont au format de l'encadré, du renvoi ou de l'avertissement. Seule exception, attendue : la puce « ⚠ Les limites de chaque instrument… » de la note d'ouverture.
  - Dans les encadrés, les 328 lignes Limite ou Parade de chaque langue ont toutes une source, sauf les « aucune connue ; on le dit ».
- **Les renvois.**
  - 708 entrées par langue, en dehors de l'index.
  - Toutes pointent vers l'endroit que l'index donne pour leur instrument : 0 écart.
  - Les 13 entrées par langue vers l'encadré du 2 octobre pointent vers ses morceaux réels : §A avant K71, §C avant K47, C bis avant K72.
- **La mention de version.** Il y a 496 mentions « (v3.6 » par langue, comme avant les corrections. Chacune des 496 insertions de chaque langue porte « (v3.6 » ou la date du 2 octobre 2026.
- **Les règles de forme.**
  - Aucune revendication de priorité : les « first » et « premier » du texte ajouté sont des « premier jeton », « d'abord », « le premier des sept pièges ».
  - Aucune citation de quinze mots ou plus.
  - Aucun sigle absent de la v3.5, en dehors de la liste permise.
- **La doctrine.** J'ai relu les lignes ajoutées où « aléatoire » paraît sans « de même norme » (41 en français) et celles où « random » paraît sans « matched-norm » (56 en anglais). Aucune ne dit qu'un contrôle aléatoire écarte le dommage. Partout, l'aléatoire est le nul de spécificité, et le dommage s'écarte à dégradation appariée. Quatre lignes du volet 10 omettent toutefois « de même norme » (§8, point A5).
- **La place.** En dehors du volet 10, aucun bloc ajouté ne se trouve entre deux lignes non vides de la v3.5. Au volet 10, 18 blocs par langue le sont (§8, point B1).

## 8. Ce qui reste à faire

Ces points ont été relevés par les vérifications des groupes 1 à 7, ou par mes contrôles. Ils ne sont pas corrigés : ma tâche se limitait à appliquer les corrections existantes. Les lignes citées sont celles de la v3.6 corrigée, FR / EN.

**A. Harmoniser ce que les groupes ont corrigé à un endroit et pas à l'autre** (de nouvelles corrections, sur du texte v3.6 seulement)

1. **L'artefact de polarité.**
   - Il porte « aucune parade connue » à deux endroits :
     - dans l'encadré « Pilotage », limite et parade, l. 825-826 / 913-914 ;
     - au volet 11, l. 5137 / 5380.
   - Or l. 3286 / 3420 (F·7) et l. 4868 / 5106 (n° 54) donnent une parade : des paires qui ne diffèrent que par le trait, vérifiées par un classifieur qui ne lit que la surface ; une direction de polarité comme concept rival, à dégradation appariée ; le témoin sans pression (cours, volet M, M4).
   - Signalé par le groupe 6.
2. **L'extraction supervisée.**
   - Elle porte « aucune parade connue » l. 2052 / 2230 et l. 2360 / 2479.
   - Or l. 834 / 922, 3964 / 4121 et 5456 / 5707 donnent le diffing par crosscoder (programme, partie 8).
   - Signalé par le groupe 2.
3. **La dégradation de chaque direction pilotée, l. 174 / 233.**
   - La phrase dit « chaque direction pilotée dégrade la sortie… plus faiblement ». Elle ne dit pas que c'est la carte d'Opus 4.8, à 0,10×, ni que la reproduction externe trouve des effets aussi forts.
   - Ailleurs, la phrase a été corrigée :
     - l. 821 / 909 et 1793 / 1935 : la carte d'Opus 4.8, à 0,10× ;
     - l. 2688 / 2853 : « plus faiblement » dans cette carte, « aussi fort » dans la reproduction externe. La dégradation n'y est pas non plus rapportée à 0,10×.
   - Signalé par les groupes 2 et 4.
4. **Le chiffre de F·51** (43 % à 1 % de faux positifs, contre 55 %).
   - Il est cité sans la réserve « fiche de première version, non relue aux sources » l. 777 / 865, 1509 / 1633, 3655 / 3787 et 6132 / 6426.
   - La réserve n'est que l. 190 / 250.
   - Signalé par le groupe 1, pour trois de ces lignes.
5. **« Aléatoire » sans « de même norme » pour le nul de spécificité**, au volet 10 : l. 4348 / 4590, 4405 / 4647, 4855 / 5093 et 4881 / 5119.
   - La doctrine n'est pas violée : le dommage y est bien renvoyé à la dégradation appariée.
   - Mais le groupe 7 a corrigé cette forme au volet 11. C'est mon constat.
6. **Le libellé « explication du 2 octobre ».** Il est employé 38 fois par langue, alors que le lecteur du cours ne connaît que « l'encadré du 2 octobre ». Harmonisation à décider ; signalé par le groupe 1.

**B. La place et le rendu**

1. **Dix-huit avertissements par langue au volet 10** sont posés entre deux lignes d'une même fiche :
   - FR l. 4311, 4329, 4348, 4405, 4457, 4511, 4542, 4571, 4587, 4629, 4734, 4840, 4855, 4868, 4881, 4920, 4982, 5017 ;
   - EN l. 4553, 4571, 4590, 4647, 4699, 4752, 4782, 4811, 4827, 4869, 4973, 5078, 5093, 5106, 5119, 5157, 5219, 5253.

   Rien n'est coupé dans le texte, mais au rendu Markdown la fiche s'affiche en deux paragraphes. Une correction ne peut pas les déplacer, il y faudrait reprendre une ligne de la v3.5. Le remède est une nouvelle passe d'insertion de la tranche volet10, ancrée sur les lignes « Lecture » (groupe 6).
2. **Réponse 2, l. 5096 / 5337.** L'avertissement sur le juge s'intercale entre l'annonce « trois choses autour » et « La première ». C'est à trancher à la main (groupe 7).
3. **Le titre de premier niveau** dit toujours « v3.5 — 27 septembre 2026 ». La règle interdit de le modifier ; la note v3.6 le suit immédiatement.

**C. Ce qu'il faudrait ajouter** (nouvelles insertions)

1. **F·14 (ELK) et F·58 n'ont aucun renvoi** : vers les sondes et l'élicitation non supervisée pour la première, vers les sondes pour la seconde (groupe 5).
2. **L'encadré « Détecteurs fine-tunés », parade 2.** Il manque le cas positif de la fiche 7, point 5 : un pilotage qui, à cette dose, fait basculer l'honnêteté (groupe 5).
3. **F·11.** Pour l'homogénéité, préciser les erreurs constatées des juges LLM chez Kenton et al., comme l'a fait le groupe 3 (groupe 5, facultatif).

**D. À vérifier avant de diffuser**

1. **Les énoncés qui ne reposent que sur des rapports d'antériorité lus par résumé.**
   - Le rapport 4 porte deux énoncés :
     - la sonde « évaluation contre déploiement » qui bascule sous RL : l. 775 / 863 (encadré « Sondes »), 811 / 899 (encadré du 2 octobre, partie 3) et 5731 / 6006 (volet 11, réponse 24) ;
     - un entraînement à verbaliser qui multiplierait la verbalisation par 2,4 à 2,9 sans changer la conscience latente : l. 6231 / 6532 (encadré « Chaîne de pensée », limite 6).
   - Le rapport 3 : *The Obfuscation Atlas* ; le pilotage de persona qui doublerait la diffusion, 24 % contre environ 50 %.
   - Le rapport 5 : l'alerte de Zeisler et la revue de Nanda.

   Tous sont dits « rapport » dans le texte, mais ils sont à confirmer sur les sources.
2. **L'encadré du 2 octobre reprend tout le contenu du texte source, mais pas mot pour mot.** Ses corrections de vérification sont dites en italique à la fin de chaque morceau :
   - environ 80 à 86 % d'annotations en évaluation contre 34 %, et non « et pas sinon » ;
   - les deux réserves du README ;
   - la porte du lens, aux parties 3 et 8 du programme ;
   - « régression logistique », sans « régularisée » ;
   - **lire aux deux positions, « et », et non « ou »** ;
   - un RL à récompenses vérifiables.

   Le chercheur doit valider ces écarts par rapport à son texte. Pour les positions de lecture en particulier : si l'on revient au « ou » du texte source, il faut revenir ensemble sur l'encadré, l'encadré « Sondes » et les deux avertissements du volet 11 corrigés par le groupe 7, P9 et P18 (groupe 7, alerte 3).
3. **Deux lignes « À ne pas dire », de F·50 et F·56**, portent encore deux affirmations que la note de tête donne pour fausses. La règle interdit d'y toucher, et les avertissements voisins y renvoient (groupe 5). C'est à garder en tête à l'oral.
4. **Une relecture complète du rendu Markdown**, dans les deux langues, avant diffusion.

## Annexe : les 185 corrections appliquées

Pour chaque correction : le fichier, le numéro dans le fichier, la langue, la ligne de la v3.6 corrigée où commence le texte corrigé, la tranche, la nature de la ligne et le début du texte corrigé.

| Fichier | N° | Langue | Ligne v3.6 | Tranche | Nature de la ligne corrigée | Début du texte corrigé |
|---|---|---|---|---|---|---|
| groupe_1 | 1 | FR | 5 | tete_volet1 | note d'ouverture | > Rien du texte de la v3.5 n'est retiré ni modifié : on ajoute, et chaque ajout porte la mentio |
| groupe_1 | 2 | EN | 25 | tete_volet1 | note d'ouverture | > No text of v3.5 is removed or changed: things are only added, and every addition carries the  |
| groupe_1 | 3 | FR | 174 | tete_volet1 | avertissement | > ⚠ *(v3.6)* Que le désalignement monte quand on neutralise « ceci est un test » n'est qu'un ap |
| groupe_1 | 4 | EN | 233 | tete_volet1 | avertissement | > ⚠ *(v3.6)* That misaligned behaviour rises when "this is a test" is neutralized is only weak  |
| groupe_1 | 5 | FR | 190 | tete_volet1 | avertissement | > ⚠ *(v3.6)* « La seconde prend le relais » suppose la sonde fiable là où la chaîne ne l'est pa |
| groupe_1 | 6 | EN | 250 | tete_volet1 | avertissement | > ⚠ *(v3.6)* "The second takes over" assumes the probe is reliable where the chain is not: the  |
| groupe_1 | 7 | FR | 225 | tete_volet1 | avertissement | > ⚠ *(v3.6)* « Plusieurs méthodes de rang un ont échoué » est un nul sans chiffres ni cas connu |
| groupe_1 | 8 | EN | 289 | tete_volet1 | avertissement | > ⚠ *(v3.6)* "Several rank-one methods failed" is a null without numbers or a known case: their |
| groupe_1 | 9 | FR | 228 | tete_volet1 | avertissement | > ⚠ *(v3.6)* La prédiction du sous-espace n'a pas d'appui causal propre : la baisse du rang tro |
| groupe_1 | 10 | EN | 292 | tete_volet1 | avertissement | > ⚠ *(v3.6)* The subspace prediction has no causal support of its own: the rank-three drop did  |
| groupe_1 | 11 | FR | 252 | tete_volet1 | avertissement | > ⚠ *(v3.6)* Le résultat d'un jeu red team / blue team ne vaut que pour la red team supposée :  |
| groupe_1 | 12 | EN | 316 | tete_volet1 | avertissement | > ⚠ *(v3.6)* The result of a red team / blue team game holds only for the red team assumed: an  |
| groupe_1 | 13 | FR | 363 | volet_M | encadré | > - **Limite :** L'aléatoire seul est un contrôle faible : dans la carte système d'Opus 4.8, de |
| groupe_1 | 14 | EN | 430 | volet_M | encadré | > - **Limit:** Random alone is a weak control: in the Opus 4.8 system card, pairs with arbitrar |
| groupe_1 | 15 | FR | 367 | volet_M | encadré | > - **Limite :** L'aléatoire apparié en norme et l'aléatoire apparié en covariance sont deux de |
| groupe_1 | 16 | EN | 434 | volet_M | encadré | > - **Limit:** The norm-matched random and the covariance-matched random are two of the three c |
| groupe_1 | 17 | FR | 419 | volet_M | encadré | > - **Limite :** Choisir la couche, le seuil ou le prédicteur sur le jeu de test le contamine ; |
| groupe_1 | 18 | EN | 486 | volet_M | encadré | > - **Limit:** Choosing the layer, threshold or predictor on the test set contaminates it; extr |
| groupe_1 | 19 | FR | 541 | volet_M | avertissement | > ⚠ *(v3.6)* « Aucun contournement universel dans sa chasse » est le nul d'un red-teaming : une |
| groupe_1 | 20 | EN | 608 | volet_M | avertissement | > ⚠ *(v3.6)* "No universal jailbreak in its hunt" is the null of a red-teaming effort: a bound  |
| groupe_1 | 21 | EN | 526 | volet_M | morceau du 2 octobre | > The rule of this paragraph, applied to misalignment probes and to the J-lens, is developed in |
| groupe_1 | 22 | EN | 532 | volet_M | encadré | > **Workaround:** In part: two different ways of installing the same behaviour, and another tea |
| groupe_2 | 1 | FR | 641 | volet2_A_a_D | encadré | > - **Limite :** Construit n'est pas naturel : la saillance peut venir de l'insertion, et l'ali |
| groupe_2 | 2 | EN | 727 | volet2_A_a_D | encadré | > - **Limit:** Built is not natural: salience may come from the insertion, and instrumental dec |
| groupe_2 | 3 | FR | 708 | volet2_A_a_D | encadré | > - **Limite :** Le modèle peut remarquer qu'on l'observe et changer de conduite : moins de mau |
| groupe_2 | 4 | EN | 795 | volet2_A_a_D | encadré | > - **Limit:** The model can notice it is being watched and change its conduct: less misbehavio |
| groupe_2 | 5 | FR | 718 | volet2_A_a_D | encadré | > - **Limite :** Dans une simulation, « c'est faux » est vrai : un pot de miel ou une réplicati |
| groupe_2 | 6 | EN | 805 | volet2_A_a_D | encadré | > - **Limit:** In a simulation, "this is fake" is true: a honeypot or a replication in a simula |
| groupe_2 | 7 | FR | 772 | volet2_A_a_D | encadré | > **Parade :** Lire aux deux positions : au premier jeton de la réponse, avant toute raison écr |
| groupe_2 | 8 | EN | 860 | volet2_A_a_D | encadré | > **Workaround:** Read at both positions: at the first token of the answer, before any written  |
| groupe_2 | 9 | FR | 821 | volet2_A_a_D | encadré | > - **Limite :** « La direction bouge le comportement » n'est pas « le concept cause le comport |
| groupe_2 | 10 | EN | 909 | volet2_A_a_D | encadré | > - **Limit:** "The direction moves behaviour" is not "the concept causes behaviour": in the Op |
| groupe_2 | 11 | FR | 828 | volet2_A_a_D | encadré | > **Parade :** Pré-enregistrer la définition de « ça marche » et tester la généralisation d'un  |
| groupe_2 | 12 | EN | 916 | volet2_A_a_D | encadré | > **Workaround:** Preregister the definition of "it works" and test generalization from one set |
| groupe_2 | 13 | FR | 834 | volet2_A_a_D | encadré | > **Parade :** Pour la causalité, le test à dégradation appariée ; pour l'extraction supervisée |
| groupe_2 | 14 | EN | 922 | volet2_A_a_D | encadré | > **Workaround:** For causality, the matched-degradation test; for supervised extraction, cross |
| groupe_2 | 15 | FR | 904 | volet2_A_a_D | avertissement | > ⚠ *(v3.6)* Les échecs des méthodes de rang un sont des nuls, rapportés sans chiffres faute de |
| groupe_2 | 16 | EN | 992 | volet2_A_a_D | avertissement | > ⚠ *(v3.6)* The failures of the rank-one methods are nulls, reported without numbers since the |
| groupe_2 | 17 | FR | 936 | volet2_A_a_D | encadré | > - **Limite :** Il n'a été montré que sur Claude ; un billet de Zeisler, relayé par un rapport |
| groupe_2 | 18 | EN | 1024 | volet2_A_a_D | encadré | > - **Limit:** It has been shown only on Claude; a post by Zeisler, relayed by a report, finds  |
| groupe_2 | 19 | FR | 1009 | volet2_A_a_D | encadré | > **Parade :** Deux ordres de retrait, par variance et par effet causal. *(source : cours, vole |
| groupe_2 | 20 | EN | 1098 | volet2_A_a_D | encadré | > **Workaround:** Two removal orders, by variance and by causal effect. *(source: course, Part  |
| groupe_2 | 21 | FR | 1070 | volet2_A_a_D | encadré | > - **Limite :** Un diff qui ne fait rien sortir ne dit rien sans cas connu : le crosscoder peu |
| groupe_2 | 22 | EN | 1159 | volet2_A_a_D | encadré | > - **Limit:** A diff that surfaces nothing says nothing without a known case: the crosscoder m |
| groupe_3 | 1 | FR | 1092 | volet2_E_a_I | encadré | > - **Limite :** Le juge peut être un modèle, avec ses erreurs systématiques : un juge LLM plus |
| groupe_3 | 2 | EN | 1182 | volet2_E_a_I | encadré | > - **Limit:** The judge can be a model, with systematic errors of its own: an LLM judge weaker |
| groupe_3 | 3 | FR | 1141 | volet2_E_a_I | encadré | > - **Limite :** L'échec peut rester silencieux là où l'évaluation en distribution est impossib |
| groupe_3 | 4 | EN | 1231 | volet2_E_a_I | encadré | > - **Limit:** Failure can stay silent where in-distribution evaluation is impossible. *(source |
| groupe_3 | 5 | FR | 1143 | volet2_E_a_I | encadré | > - **Limite :** La sonde du filtre et la méthode peuvent lire la même feature saillante. *(sou |
| groupe_3 | 6 | EN | 1233 | volet2_E_a_I | encadré | > - **Limit:** The filter's probe and the method may read the same salient feature. *(source: c |
| groupe_3 | 7 | FR | 1140 | volet2_E_a_I | encadré | > **Parade :** Ancrer la méthode sur des réponses vérifiées, par l'entraînement du facile au di |
| groupe_3 | 8 | EN | 1230 | volet2_E_a_I | encadré | > **Workaround:** Anchor the method on verified answers, through easy-to-hard training — a hope |
| groupe_3 | 9 | FR | 1220 | volet2_E_a_I | encadré | > **Parade :** Des moniteurs à état, qui n'en récupèrent qu'une partie ; pour l'agrégation de p |
| groupe_3 | 10 | EN | 1312 | volet2_E_a_I | encadré | > **Workaround:** Stateful monitors, which recover only part of them; for aggregating internal  |
| groupe_3 | 11 | FR | 1289 | volet2_E_a_I | encadré | > - **Limite :** Sans budget fixé, « rien trouvé » dit seulement qu'on n'a pas assez cherché. * |
| groupe_3 | 12 | EN | 1382 | volet2_E_a_I | encadré | > - **Limit:** Without a fixed budget, "nothing found" only says you did not search enough. *(s |
| groupe_3 | 13 | FR | 1310 | volet2_E_a_I | avertissement | > ⚠ *(v3.6)* La formule « sans en trouver d'universel » rapporte le nul d'une chasse : une born |
| groupe_3 | 14 | EN | 1403 | volet2_E_a_I | avertissement | > ⚠ *(v3.6)* The phrase "without finding a universal one" reports the null of a hunt: a bound a |
| groupe_3 | 15 | FR | 1348 | volet2_E_a_I | encadré | > - **Limite :** Placé dans l'entraînement, un classifieur peut inciter le modèle à l'éviter. * |
| groupe_3 | 16 | EN | 1441 | volet2_E_a_I | encadré | > - **Limit:** Placed in training, a classifier can give the model an incentive to evade it. *( |
| groupe_3 | 17 | FR | 1358 | volet2_E_a_I | avertissement | > ⚠ *(v3.6)* Le « feedback de l'IA » fait d'un modèle le juge de l'entraînement, et un juge d'e |
| groupe_3 | 18 | EN | 1452 | volet2_E_a_I | avertissement | > ⚠ *(v3.6)* The "feedback from AI" makes a model the judge of training, and a training judge c |
| groupe_3 | 19 | FR | 1680 | volet3 | avertissement | > ⚠ *(v3.6)* Ces lectures ne sont pas toutes un auto-rapport du modèle : l'oracle d'activation  |
| groupe_3 | 20 | EN | 1805 | volet3 | avertissement | > ⚠ *(v3.6)* Not all of these readings are a self-report of the model: an activation oracle is  |
| groupe_3 | 21 | FR | 1703 | volet3 | avertissement | > ⚠ *(v3.6)* Ce taux est lu sur des pots de miel : un modèle peut y remarquer le test et s'y co |
| groupe_3 | 22 | EN | 1828 | volet3 | avertissement | > ⚠ *(v3.6)* This rate is read on honeypots: a model can notice the test there and behave bette |
| groupe_3 | 23 | FR | 1712 | volet3 | avertissement | > ⚠ *(v3.6)* Ce que cette phrase déroule a ses limites, à connaître avant de la dire : la décom |
| groupe_3 | 24 | EN | 1837 | volet3 | avertissement | > ⚠ *(v3.6)* What this sentence unfolds has its limits, to know before saying it: the SAE decom |
| groupe_4 | 1 | FR | 1754 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* Cette extension, ton dépôt l'a tentée sur Llama 3.1 8B Instruct : aucune intervent |
| groupe_4 | 2 | EN | 1896 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* Your repository tried this extension on Llama 3.1 8B Instruct: no single-direction |
| groupe_4 | 3 | FR | 1793 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* « Augmenter ou diminuer un comportement » ne dit le concept qu'à dégradation appar |
| groupe_4 | 4 | EN | 1935 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* "Increasing or decreasing a behaviour" shows the concept only at matched degradati |
| groupe_4 | 5 | FR | 1809 | volets4_5_entete | encadré | > - **Limite :** L'erreur de reconstruction : le SAE ouvert de Goodfire pour Llama 3.1 8B laiss |
| groupe_4 | 6 | EN | 1949 | volets4_5_entete | encadré | > - **Limit:** Reconstruction error: the open-source Goodfire SAE for Llama 3.1 8B leaves 86.8% |
| groupe_4 | 7 | FR | 1835 | volets4_5_entete | encadré | > - **Limite :** Affirmer qu'aucun mécanisme ne fait mal agir le modèle exige décomposition et  |
| groupe_4 | 8 | EN | 1975 | volets4_5_entete | encadré | > - **Limit:** Claiming that no mechanism makes the model misbehave requires decomposition and  |
| groupe_4 | 9 | FR | 2013 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* La grille compare les interventions entre elles et à un prompt, pas à des témoins  |
| groupe_4 | 10 | EN | 2191 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* The grid compares the interventions with each other and with a prompt, not with sa |
| groupe_4 | 11 | FR | 2032 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* Dans cette triangulation, la verbalisation n'est jamais une preuve d'inhibition :  |
| groupe_4 | 12 | EN | 2210 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* In this triangulation, verbalization is never proof of inhibition: random directio |
| groupe_4 | 13 | FR | 2154 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* Au point 7, « en boîte noire » veut dire que le détecteur lit le transcript, pas l |
| groupe_4 | 14 | EN | 2334 | volets4_5_entete | avertissement | > ⚠ *(v3.6)* In item 7, "black-box" means the detector reads the transcript, not the activation |
| groupe_4 | 15 | FR | 2243 | volet6 | encadré | > - **Limite :** Une fenêtre tronquée peut faire mal lire : selon le README, à travers elle, un |
| groupe_4 | 16 | EN | 2408 | volet6 | encadré | > - **Limit:** A truncated window can mislead: according to the README, through it a softened n |
| groupe_4 | 17 | FR | 2247 | volet6 | encadré | > - **Limite :** Un juge qui lit le raisonnement se laisse persuader : le moniteur fondé sur la |
| groupe_4 | 18 | EN | 2412 | volet6 | encadré | > - **Limit:** A judge that reads the reasoning gets persuaded: the chain-of-thought monitor wo |
| groupe_4 | 19 | FR | 2253 | volet6 | encadré | > - **Limite :** Des étiquettes de juge bruitées ou non validées contre des humains : environ 2 |
| groupe_4 | 20 | EN | 2418 | volet6 | encadré | > - **Limit:** Judge labels that are noisy or not validated against humans: about 25% of labels |
| groupe_4 | 21 | FR | 2259 | volet6 | avertissement | > ⚠ *(v3.6)* Que la destination « se lise dans les activations » dit qu'elle y est lisible, pas |
| groupe_4 | 22 | EN | 2424 | volet6 | avertissement | > ⚠ *(v3.6)* That the destination "can be read in the activations" says it is readable there, n |
| groupe_4 | 23 | FR | 2368 | volet6 | avertissement | > ⚠ *(v3.6)* Le 96 % vient d'un stress-test délibéré, où l'action nuisible est la seule voie, e |
| groupe_4 | 24 | EN | 2484 | volet6 | avertissement | > ⚠ *(v3.6)* The 96% comes from a deliberate stress test, where the harmful action is the only  |
| groupe_4 | 25 | FR | 2399 | volet6 | avertissement | > ⚠ *(v3.6)* Le jacobien ne dispense pas du test causal : le lens ne capture l'espace de travai |
| groupe_4 | 26 | EN | 2506 | volet6 | avertissement | > ⚠ *(v3.6)* The Jacobian does not exempt the lens from the causal test: it captures the worksp |
| groupe_4 | 27 | FR | 2458 | volet6 | avertissement | > ⚠ *(v3.6)* Ce « moins de 1 % » vient d'un seul modèle, Llama 3.1 8B Instruct, et de la seule  |
| groupe_4 | 28 | EN | 2561 | volet6 | avertissement | > ⚠ *(v3.6)* This "less than 1%" comes from a single model, Llama 3.1 8B Instruct, and from opi |
| groupe_4 | 29 | FR | 2521 | volet6 | morceau du 2 octobre | > L'encadré du 2 octobre reprend cette section du côté de la pratique : pourquoi un organisme m |
| groupe_4 | 30 | FR | 2524 | volet6 | avertissement | > ⚠ *(v3.6)* « Une sonde par couche » oblige à choisir une couche, et « s'allume » suppose un s |
| groupe_4 | 31 | EN | 2689 | volet6 | avertissement | > ⚠ *(v3.6)* "One probe per layer" forces a choice of layer, and "fires" assumes a threshold: c |
| groupe_5 | 1 | FR | 2688 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* Le résultat interne rappelé ici vient du pilotage, et c'est un appui faible : des  |
| groupe_5 | 2 | EN | 2853 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* The internal result recalled here comes from steering, and it is weak support: con |
| groupe_5 | 3 | FR | 2876 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* Le lien entre déplacement et trait est corrélationnel, le trait se nomme d'avance  |
| groupe_5 | 4 | EN | 3041 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* The shift-to-trait link is correlational, the trait must be named in advance and t |
| groupe_5 | 5 | FR | 2884 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* « MMLU préservé » n'écarte le dommage que sur ce composite, et la direction aléato |
| groupe_5 | 6 | EN | 3049 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* "MMLU preserved" rules out damage only on that composite, and the covariance-match |
| groupe_5 | 7 | FR | 2998 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* Le masquage sélectif des gradients n'est montré que sur de petits modèles *(source |
| groupe_5 | 8 | EN | 3163 | volet7_B_et_D | avertissement | > ⚠ *(v3.6)* Selective gradient masking is shown only on small models *(source: course, Part 2, |
| groupe_5 | 9 | FR | 3228 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la d |
| groupe_5 | 10 | EN | 3362 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* The direction that reads best is not necessarily the one that acts: in RepE, the l |
| groupe_5 | 11 | FR | 3286 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* Ce nul de rang un est dit sans son cas connu : sans un concept qui cède au rang un |
| groupe_5 | 12 | EN | 3420 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* This rank-one null is stated without its known case: without a concept that gives  |
| groupe_5 | 13 | FR | 3482 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* Que l'interprétabilité « aide » n'est pas chiffré : quatre équipes seulement, l'éq |
| groupe_5 | 14 | EN | 3616 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* That interpretability "helps" is not quantified: only four teams, the team with th |
| groupe_5 | 15 | FR | 3590 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* Ce « 7× » compare des méthodes de désapprentissage entre elles, sur de petits modè |
| groupe_5 | 16 | EN | 3724 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* This "7×" compares unlearning methods with each other, on small models (course, Pa |
| groupe_5 | 17 | FR | 3726 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs, que la fiche ne do |
| groupe_5 | 18 | EN | 3858 | volet7_A_et_C | avertissement | > ⚠ *(v3.6)* A recall of 0.844 reads only with its false-positive rate, which the sheet does no |
| groupe_6 | 1 | FR | 3947 | volets8_9 | avertissement | > ⚠ *(v3.6)* Le quasi-hasard du SAD est un auto-rapport : il dit ce que le modèle répond quand  |
| groupe_6 | 2 | EN | 4104 | volets8_9 | avertissement | > ⚠ *(v3.6)* SAD's near-chance result is a self-report: it says what the model answers when ask |
| groupe_6 | 3 | FR | 3964 | volets8_9 | avertissement | > ⚠ *(v3.6)* Derrière « le persona comme direction », le résultat le plus fort est prédictif, p |
| groupe_6 | 4 | EN | 4121 | volets8_9 | avertissement | > ⚠ *(v3.6)* Behind "the persona as a direction", the strongest result is predictive, not causa |
| groupe_6 | 5 | FR | 4029 | volets8_9 | avertissement | > ⚠ *(v3.6)* Ces « signs of life » ne mettent pas encore à l'épreuve « difficult for the model  |
| groupe_6 | 6 | EN | 4186 | volets8_9 | avertissement | > ⚠ *(v3.6)* These "signs of life" do not yet put "difficult for the model to control" to the t |
| groupe_6 | 7 | FR | 4151 | volets8_9 | avertissement | > ⚠ *(v3.6)* AI Organizations mesure ce mode dans deux organisations simulées, sur Opus 4.1, et |
| groupe_6 | 8 | EN | 4308 | volets8_9 | avertissement | > ⚠ *(v3.6)* AI Organizations measures this mode in two simulated organizations, on Opus 4.1, a |
| groupe_6 | 9 | FR | 4329 | volet10 | avertissement | > ⚠ *(v3.6)* Sur stages-oversight, le score mesure ce que le modèle répond quand on lui demande |
| groupe_6 | 10 | EN | 4571 | volet10 | avertissement | > ⚠ *(v3.6)* On stages-oversight, the score measures what the model answers when asked where it |
| groupe_6 | 11 | FR | 4430 | volet10 | encadré | > **Parade :** Choisir les sites d'intervention par leur effet causal mesuré, à l'ablation et a |
| groupe_6 | 12 | EN | 4672 | volet10 | encadré | > **Workaround:** Choose intervention sites by their measured causal effect, under ablation and |
| groupe_6 | 13 | FR | 4431 | volet10 | encadré | > - **Limite :** Petits jeux de prompts : dans ton dépôt, une partie du patch de chemins ne por |
| groupe_6 | 14 | EN | 4673 | volet10 | encadré | > - **Limit:** Small prompt sets: in your repository, part of the path patching covers only 5 t |
| groupe_6 | 15 | FR | 4435 | volet10 | encadré | > - **Limite :** Le choix du prompt cible et la contamination par le jeton de remplacement (« p |
| groupe_6 | 16 | EN | 4677 | volet10 | encadré | > - **Limit:** The choice of target prompt and placeholder contamination can distort the readin |
| groupe_6 | 17 | FR | 4734 | volet10 | avertissement | > ⚠ *(v3.6)* Contre ce risque d'un moniteur qui apprend le style de l'attaquant plutôt que l'er |
| groupe_6 | 18 | EN | 4973 | volet10 | avertissement | > ⚠ *(v3.6)* Against this risk of a monitor that learns the attacker's style rather than the er |
| groupe_6 | 19 | FR | 4868 | volet10 | avertissement | > ⚠ *(v3.6)* Ces effets se comparent aux prompts système et au fine-tuning, les capacités sont  |
| groupe_6 | 20 | EN | 5106 | volet10 | avertissement | > ⚠ *(v3.6)* These effects are compared with system prompts and fine-tuning, capabilities are m |
| groupe_7 | 1 | FR | 5134 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Ces nuls de rang un n'ont pas de cas connu au même réglage : sans une intervention |
| groupe_7 | 2 | EN | 5377 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* These rank-one nulls have no known case at the same setting: without an interventi |
| groupe_7 | 3 | FR | 5204 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Des vecteurs de contrôle aléatoires de même norme n'écartent que « n'importe quell |
| groupe_7 | 4 | EN | 5451 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Matched-norm random control vectors rule out only "any push of that size does as m |
| groupe_7 | 5 | FR | 5230 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Les deux familles ferment l'écart entre deux façons d'implanter, pas celui entre l |
| groupe_7 | 6 | EN | 5476 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* The two families close the gap between two ways of implanting, not the one between |
| groupe_7 | 7 | FR | 5435 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Ce résultat lit le motif dans un scratchpad caché, donné avec la consigne de raiso |
| groupe_7 | 8 | EN | 5686 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* This result reads the motive in a hidden scratchpad, given with the instruction to |
| groupe_7 | 9 | FR | 5456 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Ce que la réponse ne dit pas : le lien entre le déplacement le long du vecteur et  |
| groupe_7 | 10 | EN | 5707 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* What the answer does not say: the link between the shift along the vector and the  |
| groupe_7 | 11 | FR | 5499 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* « Réfutée » vaut pour l'hypothèse forte, à ce réglage : un petit effet n'est pas d |
| groupe_7 | 12 | EN | 5751 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* "Refuted" holds for the strong hypothesis, at that setting: a small effect is not  |
| groupe_7 | 13 | FR | 5643 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* La réserve dite ici a un pendant en production : une sonde peut y échouer en silen |
| groupe_7 | 14 | EN | 5916 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* The caveat stated here has a production counterpart: a probe can fail silently the |
| groupe_7 | 15 | FR | 5629 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* Ces taux de sabotage valent pour l'équipe rouge supposée : sur ces mêmes environne |
| groupe_7 | 16 | EN | 5903 | volet11_1_a_20 | avertissement | > ⚠ *(v3.6)* These sabotage rates hold for the red team assumed: on those same environments, an |
| groupe_7 | 17 | FR | 5731 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* Après un entraînement, une sonde calibrée ailleurs lit autrement : des sondes neuv |
| groupe_7 | 18 | EN | 6006 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* After training, a probe calibrated elsewhere reads differently: fresh out-of-domai |
| groupe_7 | 19 | FR | 5938 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* Ces quarante transcriptions sont synthétiques, conçues par les auteurs : le modèle |
| groupe_7 | 20 | EN | 6222 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* These forty transcripts are synthetic, designed by the authors: the monitored mode |
| groupe_7 | 21 | FR | 6231 | volet11_21_a_52 | encadré | > - **Limite :** Un entraînement à verbaliser multiplierait la verbalisation par 2,4 à 2,9 sans |
| groupe_7 | 22 | EN | 6532 | volet11_21_a_52 | encadré | > - **Limit:** Training to verbalize would multiply verbalization by 2.4 to 2.9 without changin |
| groupe_7 | 23 | FR | 6330 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* Des vecteurs aléatoires de même norme en contrôle ne donnent que le nul de spécifi |
| groupe_7 | 24 | EN | 6632 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* Matched-norm random vectors as the control give only the specificity null: in this |
| groupe_7 | 25 | FR | 6358 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* Comme à la réponse 31 : lue dans deux bras d'entraînement, la projection sur un ve |
| groupe_7 | 26 | EN | 6661 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* As in answer 31: read across two training arms, the projection onto a persona vect |
| groupe_7 | 27 | FR | 6429 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* L'inverse ne vaut pas : une sonde qui ne lit plus rien ne prouve pas l'absence — a |
| groupe_7 | 28 | EN | 6735 | volet11_21_a_52 | avertissement | > ⚠ *(v3.6)* The converse does not hold: a probe that no longer reads anything does not prove a |
| groupe_7 | 29 | FR | 6506 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Des vecteurs aléatoires de même norme en contrôle n'écartent que « n'importe quell |
| groupe_7 | 30 | EN | 6816 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Matched-norm random control vectors rule out only "any push of that size does as m |
| groupe_7 | 31 | FR | 6569 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Le résultat d'inhibition cité a la même limite qu'à la réponse 56 — des vecteurs d |
| groupe_7 | 32 | EN | 6880 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* The inhibition result cited has the same limit as at answer 56 — arbitrary control |
| groupe_7 | 33 | FR | 6589 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Les quarante attaques du banc des angles morts sont conçues à la main, en transcri |
| groupe_7 | 34 | EN | 6901 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* The blind-spot benchmark's forty attacks are hand-designed, as synthetic transcrip |
| groupe_7 | 35 | FR | 6607 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* « Ne généraliseraient jamais » ne se constate que là où l'on sait l'intention prés |
| groupe_7 | 36 | EN | 6920 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* "Never generalise" can only be established where the intention is known to be pres |
| groupe_7 | 37 | FR | 6701 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Des sondes entraînées hors politique sur des exemples écrits peuvent n'apprendre q |
| groupe_7 | 38 | EN | 7016 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Probes trained off-policy on written examples may learn only a surface cue, or rea |
| groupe_7 | 39 | FR | 6940 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Pour l'inhibition, un contrôle aléatoire de même norme n'est que le nul de spécifi |
| groupe_7 | 40 | EN | 7265 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* For the inhibition, a matched-norm random control is only the specificity null; da |
| groupe_7 | 41 | FR | 6996 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* L'inhibition sur Sonnet 4.5 a la même limite qu'à la réponse 56 — des vecteurs de  |
| groupe_7 | 42 | EN | 7321 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* The Sonnet 4.5 inhibition has the same limit as at answer 56 — arbitrary control v |
| groupe_7 | 43 | FR | 7108 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* La batterie aval est faite de scènes construites : le modèle peut y remarquer le t |
| groupe_7 | 44 | EN | 7433 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* The downstream battery is made of constructed scenes: the model can notice the tes |
| groupe_7 | 45 | FR | 7140 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Une remontée sous inhibition ne fait une preuve mécaniste qu'au-delà des témoins : |
| groupe_7 | 46 | EN | 7465 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* A rise under inhibition is mechanistic evidence only beyond the controls: across t |
| groupe_7 | 47 | FR | 7169 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* Un moniteur qui partage les poids de l'acteur peut reconnaître les attaques synthé |
| groupe_7 | 48 | EN | 7494 | volet11_53_et_fin | avertissement | > ⚠ *(v3.6)* A monitor sharing the actor's weights can recognize synthetic attacks whose answer |

