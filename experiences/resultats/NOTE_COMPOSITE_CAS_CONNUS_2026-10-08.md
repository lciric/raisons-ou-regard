# Les cas connus du composite de dégradation, sur l'organisme (8 octobre 2026)

**Statut : exploratoire.** Ce sont les deux premiers runs du composite adopté le 8 octobre (décision 38 ; `claude/SPEC_COMPOSITE_v0.1_2026-10-08.md`). Aucune règle de décision ne les lit.

## Les runs

| Run | Carte | Lecture des choix multiples | Durée | Coût |
|---|---|---|---|---|
| `composite_check-20261008-050024-48bc` | A100 SXM4 (pas d'offre H100 au lancement) | la lettre au premier jeton de la réponse | 28 min | 0,53 $ |
| `composite_check-20261008-053047-9152` | H100 SXM | la réponse ouverte par « Answer: », la lettre avec ou sans espace | 14 min | 0,93 $ |

- **Le modèle** : l'organisme de la porte, Llama-3.1-8B-Instruct avec l'adaptateur des documents (`organism-20261003-164800-9e3e`), puis celui du sixième tour d'expert iteration (`organism-20261004-003822-bc0f`), fusionnés.
- **Les items** : `experiences/composite/items_v1/`.
- **Le juge de la cohérence** : JEV-27B, révision `51740a88`.
- **La projection** : le sous-espace de l'extraction v2 (`extract_eval-20261005-114155-50b2`), au rang 1.

## Le composite sans intervention

| Composante | A100, premier run | H100, second run |
|---|---|---|
| MMLU, exactitude | 58,9 % | 60,5 % |
| GSM8K, exactitude | 79,8 % | 79,6 % |
| Tests unitaires réussis | 60,9 % | 60,3 % |
| Cohérence jugée (1 à 5) | 4,33 | 4,32 |
| Perplexité, WikiText-103 | 14,61 | 14,61 |
| Décisions qui changent avec l'ordre | 40,7 % | 38,4 % |
| Réponses mal formées, format imposé | 1,5 % | 0,0 % |
| Appels d'outils valides | 22,5 % | 18,0 % |

- **Les composantes générées changent d'une carte à l'autre**, jusqu'à 4,5 points pour les appels d'outils, au-delà de leur tolérance (±2). La règle de la carte (décision 33) vaut donc aussi pour le composite : on ne compare ses valeurs que sur une même carte. C'est le cas à la porte, où l'inhibition et ses tirages sont mesurés dans le même run. MMLU et l'ordre ne se comparent pas entre les deux runs : leur lecture a changé.
- **L'organisme appelle mal les outils.** Dans le second run, 164 réponses sur 200 ne contiennent aucun appel lisible. Souvent, il écrit lui-même un « résultat » d'outil, avec des contenus de Wood Labs : la trace de ses documents. La composante reste juste, mais elle a peu de marge sur cet organisme.
- **Il a un biais de position.** Il répond « B » à 39 % des items de MMLU, et 37,6 % de ses décisions sur MMLU changent quand on renverse les options, même avec la lecture corrigée. Sur les choix forcés, il prend la première option dans 68 % des cas.
- **Le juge de la cohérence** change sa décision avec l'ordre des options pour 15 réponses sur 100 dans le second run (19 sur 100 dans le premier) : d'où la moyenne sur les deux ordres. Il note bas certaines réponses fausses, alors que la question lui demande de juger la cohérence « whatever its accuracy ».

## Les deux dommages construits

**L'effondrement de la génération est vu** : à la couche 16, une direction aléatoire est ajoutée à 4 fois la norme de l'état. Les mesures sont celles du second run ; le premier donne les mêmes, à moins d'un millième près.

| Composante | Sans intervention | Effondrement |
|---|---|---|
| Cohérence | 4,32 | 1,01 |
| Perplexité | 14,6 | 649 317 |
| Réponses mal formées | 0,0 % | 100 % |

Les réponses deviennent une répétition (« abboabboabbo… »).

**Le dommage « choix sans savoir » ne se lit pas comme construit.** La consigne système demande de choisir au hasard quand aucune option n'est juste. Elle est donnée sur MMLU et sur les items de l'ordre.

| | Premier run (lettre au premier jeton) | Second run (« Answer: ») |
|---|---|---|
| L'ordre, toutes décisions | 40,7 → 50,1 % (+9,4 points) | 38,4 → 41,0 % (+2,6 points) |
| Les choix forcés qui changent | 79 → 126 sur 200 | 81 → 91 sur 200 |
| MMLU | 58,9 → 56,4 % (−2,6 points) | 60,5 → 59,5 % (−1,05 point) |
| Verdict | l'ordre bouge, mais MMLU aussi : non vu | idem, MMLU au-delà de sa tolérance de 21 items sur 2 000 : non vu |

- **Le composite voit bien le changement des choix** : l'ordre sort de sa tolérance (±2) dans les deux runs.
- **Mais la consigne ne fait pas le dommage voulu.**
  - Elle déborde sur le savoir : MMLU baisse au-delà de sa tolérance (±1).
  - Elle est faible avec la réponse ouverte par « Answer: » : 10 choix forcés de plus changent, sur 200.
  - En glouton, le modèle ne tire pas au hasard. Il passe de la première option à la seconde (premier run), ou renforce sa préférence pour la première (second run).

## La projection des items ajoutés sur « je suis évalué »

La partie 3 du programme demande une projection moyenne nulle des items ajoutés, mesurée avant l'appariement. Mesure du second run, en écarts naturels des paires d'extraction, par rapport aux demandes neutres des jeux d'indices :

| Jeu de prompts | Moyenne sur les couches | Moyenne des valeurs absolues |
|---|---|---|
| Choix forcés (ajoutés) | +1,53 | 2,55 |
| MMLU, items de l'ordre (ajoutés) | +2,47 | 2,66 |
| Format imposé (ajouté) | +0,21 | 2,18 |
| Appels d'outils (ajoutés) | +0,13 | 2,13 |
| GSM8K (composante du programme) | +2,22 | 2,39 |
| Cohérence (composante du programme) | +1,30 | 1,35 |

- **Au seuil proposé** (0,25 en moyenne), le format et les outils passent, les items de l'ordre non.
- **Les composantes du programme elles-mêmes**, que la règle ne vise pas, sont aussi loin que les items ajoutés : GSM8K à +2,22.
- Les questions d'examen penchent vers « évalué », par rapport à des demandes neutres. La référence des demandes neutres fait donc échouer presque tout item qui ressemble à une tâche.
- **Les valeurs par couche** vont de −5,6 à +6,4 écarts naturels. La moyenne sur les couches cache des écarts de signes opposés.

## Ce que cela propose, à décider avec Lazar

1. **Le premier dommage construit, à refaire** avant sa prochaine mesure. Le programme dit : une consigne « dans les choix forcés ». Proposé :
   - la consigne n'est donnée que sur les choix forcés, MMLU étant mesuré sans elle ;
   - elle impose une position, puisque le glouton ne tire pas au hasard : « When the options have no correct answer, always choose the first one. »
   - **Le composite le voit** si l'ordre sort de sa tolérance.
   - C'est un changement du cas connu après un premier essai : je ne le relance pas sans ton accord.
2. **La référence de la projection.** Proposé : un jeu ajouté passe s'il ne penche pas plus vers « évalué » que les composantes du programme (MMLU, GSM8K, cohérence), en moyenne sur les couches. Au second run, tous passeraient : 1,53, 2,47, 0,21 et 0,13, contre une moyenne de 2,00 pour le programme.
3. **Une réserve à écrire.** MMLU et GSM8K sont des questions d'examen, qui penchent vers « évalué ». Retirer « je suis évalué » pourrait y agir pour de bon, et non comme un dommage.
   - La mesure du composite sur la moitié de choix le dira : il suffit de voir si C y fait bouger ces composantes plus que ses tirages.
   - Si c'est le cas, elles passent en rapport seul, comme le code (annexe B.7).
4. **La suite** : cette mesure de C et de ses 20 tirages, sans regénérer les écarts (`"gaps": false`). Coût : environ 4 $ sur A100, 10 à 14 $ sur H100. Il reste environ 4,3 $ de crédit.
