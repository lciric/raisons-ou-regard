# Vérification du groupe 7 — volet 11, tranches `volet11_1_a_20`, `volet11_21_a_52`, `volet11_53_et_fin`

*2 octobre 2026. Relecture sceptique des insertions déjà appliquées dans `livrable/COURS_Alignment_v3.6_{FR,EN}_2026-10-02.md`. Corrections dans `travail/corrections_groupe_7.json`.*

## 1. Portée et méthode

- **Ce qui a été vérifié** : 344 insertions, soit 172 paires FR/EN.
  - `volet11_1_a_20` : 94 insertions, soit 47 paires — 30 avertissements ponctuels, 17 renvois, aucun encadré.
  - `volet11_21_a_52` : 116 insertions, soit 58 paires — 31 avertissements ponctuels, 26 renvois, 1 encadré.
  - `volet11_53_et_fin` : 134 insertions, soit 67 paires — 37 avertissements ponctuels, 30 renvois, aucun encadré.
- **Pièces lues** :
  - les deux v3.5 et les deux v3.6 ;
  - les fichiers `insertions_*.json` et `applique_*.md` des trois tranches ;
  - toutes les pièces : programme, passation v1.2, explication du 2 octobre, lectures prioritaires (fiches et parties B et C), contre-lecture, rapports d'antériorité des 1er et 2 octobre, README du dépôt ;
  - les fiches F·xx, les cas K, JB et G et le volet M de la v3.5, pour les sources « cours, … » ;
  - les corrections et vérifications des groupes 1 à 6, pour la cohérence.
- **Contrôles mécaniques** :
  - chaque insertion est présente une fois dans la v3.6 et absente de la v3.5 ;
  - places : table de correspondance des lignes v3.5 → v3.6 ; chaque paire FR/EN est sous la même réponse, à la même ancre (0 écart) ;
  - les cibles des renvois existent dans la v3.6 : les 30 ancres citées, FR et EN, y sont présentes, et chaque encadré visé est à sa place ;
  - formats fixes, citations de moins de quinze mots, sigles (aucun sigle inventé : R1 est le nom de DeepSeek R1).
- **Contrôles du JSON** :
  - chaque « ancien » est une ligne entière d'insertion (deux lignes pour l'encadré), présente une seule fois dans la v3.6 et absente de la v3.5 ;
  - l'unicité tient après les corrections des groupes 1 à 6, appliquées avant ou après celles-ci : 0 échec dans les deux ordres, aucun chevauchement ;
  - le préfixe de format est gardé, les paires FR/EN sont complètes, et le JSON se recharge sans erreur.
- **Lecture** : chaque avertissement et l'encadré ont été lus contre les sources qu'ils citent. Une phrase sans source est une faute ; une parade connue mais tue aussi.

## 2. Bilan

**24 paires fautives, 48 corrections** (une FR et une EN par paire). Toutes les autres insertions sont conformes.

| Nature de la faute | Paires | Corrections |
|---|---|---|
| Doctrine : « aléatoire » sans « de même norme » pour le nul de spécificité | 23 (1-20) ; 93 (21-52) ; 5, 77 (53-fin) | P2, P11, P14, P19 |
| Portée d'un constat élargie : dégradation à 0,10× (Opus 4.8) ; « plus faiblement » (Opus 4.8 ; la reproduction externe les trouve aussi forts) ; 64,7 % et Logit Lens (RMU) ; 95,3 % (meilleure de 1 000) | 23, 29 (1-20) ; 93, 113 (21-52) ; 5, 17, 85 (53-fin) | P2, P3, P11, P13, P14, P15, P20 |
| Logique du cas connu et du nul | 13, 67 (1-20) ; 25 (53-fin) | P1, P6, P17 |
| Sens causal faussé (faux alignement) | 63 (1-20) | P4 |
| « Aucune parade » alors qu'une parade est dans les pièces | 65, 89 (1-20) ; 77, limite 6 (21-52) ; 21 (53-fin) | P5, P24, P10, P16 |
| Source manquante pour la sonde neuve et le jeu d'indices disjoint | 91 (1-20) ; 11, 99 (21-52) | P7, P8, P12 |
| Positions de lecture : « ou » au lieu des deux positions du programme | 39 (21-52) ; 37 (53-fin) | P9, P18 |
| Formule absente de la source citée (pot de miel, fiche 3) | 103, 113 (53-fin) | P21, P23 |
| Contrôles confondus : le prompt n'a ni rang ni dégradation appariée | 109 (53-fin) | P22 |

**Correspondance avec le JSON** (numéros d'ordre des entrées, FR puis EN) :

- P1 : `volet11_1_a_20` FR n° 13 / EN n° 14 → entrées 1 et 2
- P2 : `volet11_1_a_20` FR n° 23 / EN n° 24 → entrées 3 et 4
- P3 : `volet11_1_a_20` FR n° 29 / EN n° 30 → entrées 5 et 6
- P4 : `volet11_1_a_20` FR n° 63 / EN n° 64 → entrées 7 et 8
- P5 : `volet11_1_a_20` FR n° 65 / EN n° 66 → entrées 9 et 10
- P6 : `volet11_1_a_20` FR n° 67 / EN n° 68 → entrées 11 et 12
- P7 : `volet11_1_a_20` FR n° 91 / EN n° 92 → entrées 13 et 14
- P24 : `volet11_1_a_20` FR n° 89 / EN n° 90 → entrées 15 et 16
- P8 : `volet11_21_a_52` FR n° 11 / EN n° 12 → entrées 17 et 18
- P9 : `volet11_21_a_52` FR n° 39 / EN n° 40 → entrées 19 et 20
- P10 : `volet11_21_a_52` FR n° 77 / EN n° 78 → entrées 21 et 22
- P11 : `volet11_21_a_52` FR n° 93 / EN n° 94 → entrées 23 et 24
- P12 : `volet11_21_a_52` FR n° 99 / EN n° 100 → entrées 25 et 26
- P13 : `volet11_21_a_52` FR n° 113 / EN n° 114 → entrées 27 et 28
- P14 : `volet11_53_et_fin` FR n° 5 / EN n° 6 → entrées 29 et 30
- P15 : `volet11_53_et_fin` FR n° 17 / EN n° 18 → entrées 31 et 32
- P16 : `volet11_53_et_fin` FR n° 21 / EN n° 22 → entrées 33 et 34
- P17 : `volet11_53_et_fin` FR n° 25 / EN n° 26 → entrées 35 et 36
- P18 : `volet11_53_et_fin` FR n° 37 / EN n° 38 → entrées 37 et 38
- P19 : `volet11_53_et_fin` FR n° 77 / EN n° 78 → entrées 39 et 40
- P20 : `volet11_53_et_fin` FR n° 85 / EN n° 86 → entrées 41 et 42
- P21 : `volet11_53_et_fin` FR n° 103 / EN n° 104 → entrées 43 et 44
- P22 : `volet11_53_et_fin` FR n° 109 / EN n° 110 → entrées 45 et 46
- P23 : `volet11_53_et_fin` FR n° 113 / EN n° 114 → entrées 47 et 48

## 3. Constats transverses

- **Le vrai** :
  - les fautes de fond sont dans le tableau ci-dessus ;
  - les chiffres conservés ont tous été retrouvés dans leur source : 0,95 et 0,70–0,75 ; 25 % et 39 % ; plus de 99 % contre moins de 2 % ; environ 1 % contre environ 50 % ; 43 % contre 55 % ; 95,3 % ; 64,7 % ; ×2,4 à 2,9 ; dix chercheurs et 92 paires ; 1,0 contre 0,35 ; 0,88 ; environ 25 % d'étiquettes révisées ; une fois sur cinq et 100 essais témoins ;
  - les statuts de lecture des rapports d'antériorité sont dits (« résumé seul », « lu de façon ciblée »).
- **La doctrine** :
  - après correction, l'aléatoire de même norme n'est partout que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - chaque nul d'instrument est assorti de son cas connu et dit comme une borne ;
  - aucune revendication d'antériorité : « I haven't seen that combination measured », jamais « first » ;
  - les sondes restent une mesure séparée, jamais l'étiquette principale.
- **La place** :
  - aucun tableau, aucune liste, aucun paragraphe coupé ;
  - deux places à signaler, sans correction possible par le texte : la réponse 2 (n° 5 de la tranche 1-20) et la réponse 24 (n° 11, 13 et 15 de la tranche 21-52).
- **Les deux langues** : même contenu, même place pour les 172 paires ; les 24 corrections sont faites en paire. L'introduction anglaise du volet 11 est en français dès la v3.5 : hors du texte ajouté, non touchée.
- **La forme** :
  - formats fixes respectés (avertissement « > ⚠ *(v3.6)* », renvoi « > ⚠ **Limites et parades** : … *(v3.6)* », encadré) ;
  - citations de moins de quinze mots ; aucune ligne « À dire » touchée, aucun chiffre ajouté à une forme nommée ;
  - deux variantes de citation laissées telles (« explication du 2 octobre, §2 » et « partie 2 ») ;
  - « aucune parade établie » (réponse 20) est remplacée par P24.
- **Cohérence avec les groupes 1 à 6** : chaque correction rejoint un constat déjà fait ailleurs.
  - P1 et P6 : groupe 1 ;
  - formule du pot de miel (P21, P23) : groupes 2, 3, 4 et 6 ;
  - attribution de la dégradation à Opus 4.8 (P2, P11, P14) : groupes 2 et 4 ;
  - « plus faiblement » (P15, P20) : groupe 5 ;
  - deux positions de lecture (P9, P18) : groupe 2, sur l'encadré « Sondes », et l'encadré du 2 octobre de la v3.6 ;
  - une fois les groupes 1 à 7 appliqués, ni la formule du pot de miel ni « aucune parade établie » ne restent dans les deux fichiers.

## 4. Insertion par insertion

Colonnes :

- n° FR / n° EN : rang dans `insertions_<tranche>.json` ;
- place : réponse, puis ligne de la v3.6 FR / EN ;
- type : avertissement, renvoi ou encadré.

Les renvois ont tous été vérifiés de la même façon.

### Tranche `volet11_1_a_20` (réponses 1 à 20)

| n° FR / EN | Place | Type | Verdict | Constat |
|---|---|---|---|---|
| 1 / 2 | réponse 1 — l. 5075 / 5314 | avertissement | conforme | J-lens montré sur Claude seulement, pour des concepts d'un seul token (fiche 1 ; passation, §5.2) ; trois sens de « charge » (cours, volet 6, §6). Parade — porte : reproduire l'échange d'un concept d'un seul token, sinon tuned lens déclaré, thèse alors non testée au sens de l'article ; prédicteur gelé d'abord — : programme, parties 3 et 8 (porte G9). |
| 3 / 4 | réponse 1 — l. 5082 / 5321 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 5 / 6 | réponse 2 — l. 5092 / 5333 | avertissement | conforme ; place signalée | Accord seulement modéré avec un second juge, juge qui ne voit que les deux réponses, aucun sous-ensemble noté par des humains : README du dépôt. Parade (juge scellé, audit humain stratifié, réponse entière, texte complet) : programme, partie 3 ; README. Place : entre « trois choses autour » et « La première » de la réponse 2 ; rien n'est coupé, mais l'annonce est séparée de son premier point (alerte). |
| 7 / 8 | réponse 2 — l. 5108 / 5349 | avertissement | conforme | Partition non mesurée à dégradation égale (citation de la réponse A4, sous quinze mots) ; aléatoire apparié en covariance plus fort que la direction de la sonde (cours, volet 6, §2 et §3). Parade : protocole de la réponse A4, patch de l'état complet comme plafond (programme, partie 8). |
| 9 / 10 | réponse 2 — l. 5114 / 5355 | avertissement | conforme | Doctrine juste : témoin de même norme = nul de spécificité ; les contrôles aléatoires d'origine n'écartent pas le dommage ; l'ablation dit la nécessité, pas la spécificité (cours, volet 6, §2 ; volet M, M4 ; cohérent avec l'encadré « Ablation »). Parade : sous-espaces de même rang à dégradation appariée, retrait partiel ou courbe effet/dégradation (M4 ; C bis ; programme, partie 7). |
| 11 / 12 | réponse 2 — l. 5117 / 5358 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 13 / 14 | réponse 3 — l. 5130 / 5373 | avertissement | corrigé (P1) | Faute de logique. L'insertion dit qu'à défaut de cas connu « un nul peut venir d'un rang trop bas » ; or le cas connu qu'elle propose est un autre concept (les pays, au rang un) : il écarte l'instrument aveugle, pas le rang trop bas, que seul le balayage de rang traite. La fiche 7 ne lie les deux que si le cas positif porte sur le même concept, en distribution. Correction : sans cas connu, le nul ne sépare pas « il faut plus d'une direction » (ta prédiction pour un concept réparti : fiche 7 ; programme, partie 2) d'un instrument aveugle à cette dose (M5). Même constat que le groupe 1. *(JSON : entrées 1 et 2)* |
| 15 / 16 | réponse 3 — l. 5133 / 5376 | avertissement | conforme | Artefact de polarité oui/non de l'addition contrastive ; résidu du dictionnaire épars qui garde la plus grande part de la variance et porte le signal lu : README du dépôt. « Aucune parade connue ; on le dit » à juste titre, pour l'artefact et pour trancher entre les deux lectures. |
| 17 / 18 | réponse 3 — l. 5146 / 5389 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 19 / 20 | réponse 4 — l. 5164 / 5409 | avertissement | conforme | Un seul tirage par condition ; sous-espace extrait sur le lot qui sert à l'évaluer : README. Parade (plusieurs générations, bootstrap au niveau des items, extraction sur un jeu disjoint) : programme, partie 7 ; README. |
| 21 / 22 | réponse 4 — l. 5167 / 5412 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 23 / 24 | réponse 6 — l. 5200 / 5447 | avertissement | corrigé (P2) | Doctrine et portée. « Des vecteurs de contrôle aléatoires » sans « de même norme » pour le nul de spécificité ; et « chaque direction dégrade les sorties » est généralisé, alors que les fiches le donnent pour la carte d'Opus 4.8, à 0,10× (fiche 2 ; fiches, contradictions entre papiers) — Fable 5 : dégradation négligeable à 0,01×. Correction : « de même norme » ; « dégradait les sorties dans la carte d'Opus 4.8, à 0,10× ». « highly dataset-dependent » est bien dans la fiche 2. *(JSON : entrées 3 et 4)* |
| 25 / 26 | réponse 6 — l. 5203 / 5450 | avertissement | conforme | Objectif implanté décrit en clair, « artificially easy to discover » (citation exacte), seule équipe en échec : celle sans accès aux données (fiche 16). Parades (conclure sur l'instrument ; ablation d'affordance) : programme, partie 8 ; fiche 16. « Aucune parade connue » pour l'organisme trop facile : juste. |
| 27 / 28 | réponse 6 — l. 5223 / 5469 | avertissement | conforme | Détecteurs = modèles fine-tunés par LoRA sur une question d'auto-rapport ; 0,95 = progression en distribution pendant l'entraînement (fiche 7 ; explication, partie 2). Parade : écart avec des familles tenues à part, test causal à dégradation appariée, cas connu (fiche 7 ; explication, partie 3). |
| 29 / 30 | réponse 6 — l. 5226 / 5472 | avertissement | corrigé (P3) | Chiffre déformé : la source dit que la meilleure de 1 000 directions aléatoires atteint 95,3 % (fiche 15 ; passation, §5.2), pas que « des directions aléatoires la séparent déjà ». Correction : le chiffre et sa portée exacts. Parade partielle (plusieurs recettes, recette tenue à part, comportement inoffensif, organisme d'une autre équipe) : K71 ; « aucune parade connue » pour l'écart implanté/naturel : explication, partie 1. *(JSON : entrées 5 et 6)* |
| 31 / 32 | réponse 6 — l. 5229 / 5475 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 33 / 34 | réponse 7 — l. 5245 / 5491 | avertissement | conforme | Jeu canari sans le déclencheur : pas mieux qu'une red team boîte noire (M5). Parade (jumeau propre réentraîné, second jumeau, filtre empoisonné exprès comme cas connu) : M4 et M9 ; borne large sans parade, dite. |
| 35 / 36 | réponse 7 — l. 5248 / 5494 | avertissement | conforme | Masquage sélectif des gradients montré sur de petits modèles (JB10) ; ramener la capacité par réentraînement ne prouve pas le retrait (volet 2, §I). Parade : ré-élicitation contre une référence jamais entraînée, au même budget, modèle connu pour masquer, « not elicitable at this budget » (M4, M5 ; JB10) : doctrine du nul respectée. |
| 37 / 38 | réponse 7 — l. 5258 / 5504 | avertissement | conforme | Différentiel nul seulement avec son cas connu (M5 ; G1). Parade (uplift du modèle sans filtre, filtre affaibli exprès, équipe rouge optimisée composante par composante) : M5 ; G1 ; F·24. |
| 39 / 40 | réponse 7 — l. 5261 / 5507 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 41 / 42 | réponse 8 — l. 5283 / 5530 | avertissement | conforme | Gain hors distribution lu sur banc agentique, modèles ouverts, scènes reconnaissables comme des tests (F·34). Parade : deux versions tirées au hasard, organisme dressé à se cacher (K63) ; représentativité du banc : « aucune parade connue » (fiche 12). |
| 43 / 44 | réponse 8 — l. 5292 / 5540 | avertissement | conforme | Parade manquante ajoutée : juge d'entraînement distinct du juge scellé, métriques d'audit tenues à part, surveillance de la longueur et des motifs de flatterie (programme, partie 8, tableau des menaces) ; juge scellé, audit humain stratifié (programme, partie 3). |
| 45 / 46 | réponse 8 — l. 5295 / 5543 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 47 / 48 | réponse 9 — l. 5322 / 5570 | avertissement | conforme | Nul de la porte seulement avec le cas connu du moniteur blanc (M5 ; K70 ; passation, §5.2) ; chiffre de sûreté relatif à l'équipe rouge (F·24). Parade : positifs connus au même seuil, équipe rouge optimisée, rappel à faux positifs fixés avec le ratio de trafic bénin (F·24 ; volet 6, §6). |
| 49 / 50 | réponse 9 — l. 5325 / 5573 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 51 / 52 | réponse 10 — l. 5348 / 5597 | avertissement | conforme | Après RL, sondes neuves hors domaine dégradées, sonde neuve dans le domaine quasi parfaite : rapport d'antériorité 3 (*The Obfuscation Atlas*), statut de lecture dit ; itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : sonde neuve, jeu d'indices disjoint, détecteurs scellés hors de la boucle (passation, §5.2 ; programme, partie 3 ; fiche 19). |
| 53 / 54 | réponse 10 — l. 5351 / 5600 | avertissement | conforme | « Ils avaient raison » tiré d'un nul d'instrument : cas connu requis (M5 ; passation, §5.2) ; nul dit comme une borne, avec budget et puissance. |
| 55 / 56 | réponse 10 — l. 5354 / 5603 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 57 / 58 | réponse 11 — l. 5363 / 5614 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 59 / 60 | prémisse « Your probes hit ninety-…» — l. 5379 / 5630 | avertissement | conforme | Séparer en distribution ne prouve rien (piège 1 ; fiche 7) ; seule lecture mesurée = corrélation peut-être d'ajustement (README ; volet 6, §2). Parade : items exclus de l'entraînement de la sonde, extraction disjointe, familles entières tenues à part (README ; explication, partie 3). |
| 61 / 62 | prémisse « So the fifteen-point dr…» — l. 5391 / 5642 | avertissement | conforme | La puissance ne remplace pas un cas connu (M5 ; réponse 4). Parade : même instrument montré capable de voir l'effet ; borne avec budget et puissance, jamais une absence. |
| 63 / 64 | prémisse « Alignment faking went a…» — l. 5431 / 5682 | avertissement | corrigé (P4) | Sens causal faussé : « ce que le RL a entraîné est la conformité, qui a fait monter le raisonnement » fait de la conformité la cause du raisonnement. La fiche 14 dit : l'entraînement obtient la conformité et fait monter le raisonnement de faux alignement (12 → 78 %), sans que le papier fasse de ce raisonnement la cause de la conformité, qui monte aussi hors surveillance. Correction alignée sur la fiche 14 et sur l'insertion n° 1 de la tranche 53-fin. Le reste (scratchpad, indice construit, jeu de rôle, mémorisation) : fiche 14 ; piège 2 ; fiches, partie C. *(JSON : entrées 7 et 8)* |
| 65 / 66 | prémisse « Persona vectors only mo…» — l. 5452 / 5703 | avertissement | corrigé (P5) | « Pour l'extraction supervisée, aucune parade connue » : faux, le programme (partie 8, menace « Nos concepts ne sont pas ceux du modèle ») donne le diffing par crosscoder, qui cherche sans hypothèse. Correction : cette parade, sourcée. Le reste (lien corrélationnel, trait nommé d'avance, baisse de capacités, nul de spécificité puis dégradation appariée) : fiche 8 ; M4 ; piège 4 ; passation, §5.2. *(JSON : entrées 9 et 10)* |
| 67 / 68 | réponse 13 — l. 5495 / 5747 | avertissement | corrigé (P6) | Même faute de logique que P1 (cas connu = les pays, autre concept). Correction : un nul à une direction ne sépare pas « il faut plus d'une direction » d'un instrument aveugle à cette dose. Le reste (« réfutée » vaut pour l'hypothèse forte, à ce réglage ; réponse 3 ; balayage de rang) est exact. *(JSON : entrées 11 et 12)* |
| 69 / 70 | réponse 13 — l. 5498 / 5750 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 71 / 72 | réponse 14 — l. 5510 / 5763 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 73 / 74 | réponse 15 — l. 5519 / 5774 | avertissement | conforme | Note d'étude, hors des lignes « À dire » : détecteurs fine-tunés par LoRA, pas des sondes (fiche 7 ; explication, partie 2). Parade pour une sonde : validation croisée par types tenus à part, test causal, cas connu (fiche 7). |
| 75 / 76 | réponse 15 — l. 5522 / 5777 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 77 / 78 | réponse 16 — l. 5549 / 5814 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 79 / 80 | réponse 18 — l. 5571 / 5840 | avertissement | conforme | Ce que la réponse tait : contrôles aléatoires d'origine sans contrôle du dommage ; témoin de même norme = nul de spécificité (volet 6, §2 ; M4). Parade : sous-espaces de même rang à dégradation appariée, courbe effet/dégradation, extraction disjointe (M4 ; programme, partie 7 ; README). |
| 81 / 82 | réponse 18 — l. 5574 / 5843 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 83 / 84 | réponse 19 — l. 5600 / 5873 | avertissement | conforme | Fable 5 : dégradation négligeable, mais contrôles « comparable or smaller » sur l'axe du désalignement (fiche 2, citation exacte) ; jugements de dégradation contradictoires d'une carte à l'autre (fiches, partie B). Distinction dommage/spécificité juste. Parade : M4 ; K47 ; fiche 2. |
| 85 / 86 | réponse 19 — l. 5603 / 5876 | avertissement | conforme | Mesures de la conscience d'évaluation faiblement corrélées, verbalisation qui rate le non-verbalisé, directions aléatoires qui la font baisser aussi (fiche 2 ; F·25 ; programme, partie 8). Parade : triangulation, critère principal comportemental et sonde latente, organisme conditionné (volet 5, sujet 4 ; programme, partie 8 ; explication, partie 3). |
| 87 / 88 | réponse 19 — l. 5606 / 5879 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 89 / 90 | réponse 20 — l. 5625 / 5899 | avertissement | corrigé (P24) | Exact sur F·24 et F·23, mais « pour le réalisme des transcriptions, aucune parade établie » tait la parade partielle de F·25 (juge mis devant la paire ; vraies ressources de déploiement), que donnent pour le même objet l'insertion n° 113 de la tranche 53-fin (B10) et, après P16, la réponse 61. Correction d'alignement, pas d'erreur de fait : parade partielle, sourcée (F·25 ; programme, partie 3), le réalisme restant ouvert (F·23). *(JSON : entrées 15 et 16)* |
| 91 / 92 | réponse 20 — l. 5639 / 5912 | avertissement | corrigé (P7) | Source incomplète : « une sonde neuve après tout entraînement » est attribuée à la passation, §5.2, qui ne la nomme pas ; elle est au programme (partie 3 : jeu δ, sonde neuve E′ ; partie 8 : « La sonde neuve E′ sur des indices δ »). Correction : source ajoutée. Le reste (échec silencieux, canaris, dérive, échantillon mensuel) : K70. *(JSON : entrées 13 et 14)* |
| 93 / 94 | réponse 20 — l. 5642 / 5915 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |

### Tranche `volet11_21_a_52` (réponses 21 à 52)

| n° FR / EN | Place | Type | Verdict | Constat |
|---|---|---|---|---|
| 1 / 2 | réponse 21 — l. 5672 / 5943 | avertissement | conforme | Détecteurs de Hopkins et Khullar = modèle fine-tuné par LoRA qui répond à une question d'auto-rapport ; environ 25 % d'étiquettes révisées (fiche 7 ; explication, §2). Parade : fiche 7. Forme : « explication du 2 octobre, §2 » ici, « partie 2 » ailleurs : même renvoi, laissé tel. |
| 3 / 4 | réponse 21 — l. 5675 / 5946 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 5 / 6 | réponse 22 — l. 5699 / 5971 | avertissement | conforme | Note insensible au cadrage = nul ; cas connu : un juge dont le déplacement est déjà mesuré (M5 ; volet 6, §2). |
| 7 / 8 | réponse 22 — l. 5702 / 5974 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 9 / 10 | réponse 23 — l. 5715 / 5989 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 11 / 12 | réponse 24 — l. 5727 / 6002 | avertissement | corrigé (P8) ; place signalée | Sondes neuves hors domaine dégradées après RL (rapport 3) ; bascule sur les cas limites (rapport 4, « résumé seul, à vérifier », statut dit). L'indicatif « lit autrement » est porté par le rapport 3. Source manquante pour la sonde neuve et le jeu d'indices disjoint : la passation, §5.2, ne les nomme pas ; programme, parties 3 et 8. « Contre la bascule sous RL, aucune parade connue » : juste. Place : trois insertions (n° 11, 13, 15) entre le premier et le deuxième paragraphe de la réponse 24, imposées par l'unicité de l'ancre ; rien n'est coupé, et la n° 13 annonce « Plus bas ». *(JSON : entrées 17 et 18)* |
| 13 / 14 | réponse 24 — l. 5730 / 6005 | avertissement | conforme | Deux contrôles — aléatoire de même norme = nul de spécificité ; dégradation appariée = dommage — : passation, §5.2 (« Le test causal de la sonde ») ; M4 ; citation de la réponse A4 exacte. Parade : familles d'organismes et organisme honnête vérifiés copie par copie (K71 ; K52). |
| 15 / 16 | réponse 24 — l. 5733 / 6008 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 17 / 18 | réponse 26 — l. 5775 / 6051 | avertissement | conforme | Gain dans l'intervalle = nul ; cas connu : sabotage installé exprès, attrapé au même seuil (M5 ; passation, §5.2) ; équipe rouge supposée (F·24). |
| 19 / 20 | réponse 26 — l. 5778 / 6054 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 21 / 22 | réponse 27 — l. 5801 / 6082 | avertissement | conforme | Taux identique dans les deux bras = nul ; cas connu : organisme conditionné à l'évaluation (programme, partie 4) ; sondes « validées par intervention » contre la dégradation appariée, l'aléatoire de même norme n'étant que le nul de spécificité (M4 ; réponse 19). |
| 23 / 24 | réponse 27 — l. 5804 / 6085 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 25 / 26 | réponse 28 — l. 5817 / 6100 | avertissement | conforme | Raisonnement de l'espace privé = rapport, pas cause ; jeu de rôle contre préservation de buts indécidable (fiche 14 ; piège 2). Parade : l'écart de conformité gratuit/payant (fiche 14). |
| 27 / 28 | réponse 28 — l. 5828 / 6111 | avertissement | conforme | Mémorisation possible : transcripts d'*Alignment Faking* réinclus par accident (fiche 14 ; fiche 3, Risk Report §5.2). « Aucune connue ; on le dit » : juste. |
| 29 / 30 | réponse 28 — l. 5831 / 6114 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 31 / 32 | réponse 29 — l. 5855 / 6138 | avertissement | conforme | Aléatoire apparié en covariance ≠ contrôle du dommage ; « un chiffre à refaire à dégradation égale » (citation de la réponse A4 ; la réponse 63 porte le chiffre de partition, d'où « réponses 63 et A4 »). Parade : courbe effet/dégradation (programme, partie 7) ; lien corrélationnel (fiche 8). |
| 33 / 34 | réponse 29 — l. 5858 / 6141 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 35 / 36 | réponse 31 — l. 5903 / 6187 | avertissement | conforme | Vecteur pris comme instrument : biais de mesure d'un bras à l'autre (passation, §5.2) ; lien corrélationnel (fiche 8). Parade : sonde par bras, sonde neuve, jeu disjoint (passation, §5.2 ; programme, partie 3). |
| 37 / 38 | réponse 31 — l. 5906 / 6190 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 39 / 40 | réponse 32 — l. 5934 / 6218 | avertissement | corrigé (P9) | Transcriptions synthétiques, risque de lire le texte (programme, partie 8 ; réponse 21) : exact. La parade disait « au premier jeton … ou au jeton d'action » ; le programme, cité, lit aux deux (partie 3 : « Deux positions de lecture » ; partie 8 : « avant toute raison, et au jeton d'action »), comme l'encadré du 2 octobre de la v3.6 et la correction du groupe 2 sur l'encadré « Sondes ». L'explication source dit « ou » ; on suit le programme. Correction : « aux deux positions … et ». *(JSON : entrées 19 et 20)* |
| 41 / 42 | réponse 32 — l. 5937 / 6221 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 43 / 44 | réponse 33 — l. 5957 / 6242 | avertissement | conforme | Proxy de sabotage = juge LLM, Sonnet 4.6 avec le papier (F·22) ; erreurs systématiques (volet 6, §2). Parade : juge scellé, audit humain d'environ 200 items stratifiés, accord rapporté (programme, partie 3). |
| 45 / 46 | réponse 33 — l. 5968 / 6252 | avertissement | conforme | Signal interne cumulé qui ne bat pas le scorer faible = nul ; cas connu : sabotage installé dans le générateur ; sinon une borne (passation, §5.2 ; M5). |
| 47 / 48 | réponse 33 — l. 5971 / 6255 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 49 / 50 | réponse 34 — l. 5985 / 6274 | avertissement | conforme | Écart faible-vers-fort fermé par des idées propres au jeu de données (JB8). Parade : tâche à vérité connue, items où le superviseur se trompe, copie entraînée sur les vraies étiquettes (JB8). |
| 51 / 52 | réponse 34 — l. 5999 / 6288 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 53 / 54 | réponse 35 — l. 6018 / 6308 | avertissement | conforme | Environ 25 % d'étiquettes révisées après un juge GPT-5 ; détecteurs testés sur Gemma et Qwen seulement (fiche 7). Parade : « révisées », jamais « inversées » ; audit humain (fiche 7 ; programme, partie 3) ; portée : « aucune parade connue », juste. |
| 55 / 56 | réponse 35 — l. 6028 / 6319 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 57 / 58 | réponse 36 — l. 6051 / 6343 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 59 / 60 | réponse 37 — l. 6070 / 6363 | avertissement | conforme | Taux de reward hacking stable = nul ; cas connu : organisme dressé à se cacher (K63) ; réalisme par paires = juge LLM, scellé et audité par des humains (F·25 ; programme, partie 3). |
| 61 / 62 | réponse 37 — l. 6079 / 6371 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 63 / 64 | réponse 38 — l. 6106 / 6399 | avertissement | conforme | Nul de CHIVE borné : trois outils en lecture seule, au plus cinq appels, éditions de prompt, baseline forte ; étiquettes par un classifieur LLM non validé (fiche 4 ; F·30). Parade : la barre de la fiche 4 (éditions qui dissocient surface et variable, contrôle qui la préserve). |
| 65 / 66 | réponse 38 — l. 6109 / 6402 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 67 / 68 | réponse 39 — l. 6128 / 6422 | avertissement | conforme | AUROC hors distribution ≠ rappel au seuil : 43 % contre 55 % à 1 % de faux positifs (F·51). Parade : rappel à 1 % de faux positifs, baseline boîte noire ou prompt à coût égal (F·50 ; volet 5, sujet 1). |
| 69 / 70 | réponse 39 — l. 6139 / 6433 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 71 / 72 | réponse 42 — l. 6179 / 6481 | avertissement | conforme | Façons de tricher enseignées d'abord au modèle, ce qui confond le résultat de généralisation (fiche 13, limites de NEM). « Aucune connue ; on le dit » : juste. |
| 73 / 74 | réponse 42 — l. 6190 / 6491 | avertissement | conforme | « Aucun transfert » = nul, cas connu requis (M5) ; « high-dimensional » (fiche 13, citation exacte). Parade : organisme où l'on a installé la disposition, même budget, batterie lue dimension par dimension. |
| 75 / 76 | réponse 42 — l. 6193 / 6494 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 77 / 78 | réponse 43 — l. 6215 / 6516 | encadré | encadré ; limite 6 corrigée (P10) | Format fixe respecté (titre, « (v3.6, 2 octobre 2026) », « Limite : » / « Parade : », sources en italique). Chiffres vérifiés : 25 % et 39 %, plus de 99 % contre moins de 2 % (fiche 17) ; environ 1 % contre environ 50 %, un seul moniteur (fiche 3) ; entraîner contre le moniteur (fiche 17 ; fiches, partie C) ; verbalisation et directions aléatoires (fiche 10 ; fiche 2 ; programme, partie 8) ; « not verbalized », jamais « hidden reasoning » (fiche 17). Faute : la limite 6 (×2,4 à 2,9, rapport 4, résumé seul) disait « Parade : aucune connue » alors que le programme, partie 8, donne la parade (critère principal comportemental, sonde latente comme contrôle : la verbalisation n'est jamais la mesure). Place : réponse 43, que visent les renvois « chaîne de pensée comme moniteur ». *(JSON : entrées 21 et 22)* |
| 79 / 80 | réponse 44 — l. 6253 / 6554 | avertissement | conforme | Écart nul entre cadrages = nul, cas connu (M5) ; remontée sous inhibition seulement au-delà de deux contrôles (M4). Parade : organisme entraîné à sous-performer (F·26 ; K63) ; aléatoire de même norme puis dégradation appariée (réponse 19). |
| 81 / 82 | réponse 44 — l. 6256 / 6557 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 83 / 84 | réponse 45 — l. 6271 / 6573 | avertissement | conforme | Injection de concept : environ une fois sur cinq (Opus 4.1), « zéro faux positif » sur 100 essais témoins, détails embellis ou confabulés (fiche 11). « Aucune parade connue » contre la confabulation : juste. |
| 85 / 86 | réponse 45 — l. 6282 / 6583 | avertissement | conforme | Intervention de même norme = nul de spécificité ; rapport immobile ne dit « texte sur l'état » que si l'état a bougé (M4 ; M5). Parade : direction aléatoire à dégradation appariée, sonde de vérification, injection de concept comme cas connu (fiche 11). |
| 87 / 88 | réponse 45 — l. 6285 / 6586 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 89 / 90 | réponse 46 — l. 6306 / 6607 | avertissement | conforme | Patch de l'état complet = plafond, pas explication (volet 6, §2 ; programme, partie 8) ; partition à refaire (A4). Parade : protocole A4, balayage de rang sur sous-espaces emboîtés (A4 ; volet 6, §6). |
| 91 / 92 | réponse 46 — l. 6309 / 6610 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 93 / 94 | réponse 47 — l. 6326 / 6628 | avertissement | corrigé (P11) | Même faute que P2 : « des vecteurs aléatoires » sans « de même norme », et « chaque direction dégrade les sorties » généralisé alors que c'est le constat de la carte d'Opus 4.8, à 0,10× (fiche 2). Parade (dégradation appariée, courbe dose-réponse, vecteur par vecteur) : M4 ; réponse 19 ; programme, partie 7. *(JSON : entrées 23 et 24)* |
| 95 / 96 | réponse 47 — l. 6329 / 6631 | avertissement | conforme | « Aucun écart, sur aucune évaluation » = nul ; cas connu : organisme conditionné (programme, partie 4) ; borne, pas certification (M5). |
| 97 / 98 | réponse 47 — l. 6332 / 6634 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 99 / 100 | réponse 48 — l. 6354 / 6657 | avertissement | corrigé (P12) | Biais de mesure d'un vecteur calibré ailleurs (passation, §5.2) et nul sans cas connu (M5) : exact. Source manquante pour la sonde neuve et le jeu disjoint : programme, parties 3 et 8. *(JSON : entrées 25 et 26)* |
| 101 / 102 | réponse 48 — l. 6357 / 6660 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 103 / 104 | réponse 49 — l. 6378 / 6682 | avertissement | conforme | Étiquettes corrigées contre brutes ne départagent pas imitation et dépassement ; tâche binaire (JB8). Parade : superviseur faux au hasard à côté du superviseur faux dans un sens fixe, copie sur les vraies étiquettes, accord là où le superviseur a raison (JB8). |
| 105 / 106 | réponse 49 — l. 6381 / 6685 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 107 / 108 | réponse 50 — l. 6399 / 6704 | avertissement | conforme | Différentiel nul : il faut un banc qui sépare et un attaquant qui a assez cherché (M5 ; M7). Parade : uplift du modèle nu, filtre affaibli, budget d'attaque fixé d'avance (G1 ; M7). |
| 109 / 110 | réponse 50 — l. 6402 / 6707 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 111 / 112 | réponse 51 — l. 6416 / 6722 | avertissement | conforme | Masquage sélectif sur petits modèles (JB10) ; coût de ré-apprentissage = borne à un budget (M5). Parade : « aucune connue » pour l'échelle, ré-élicitation à budget fixé pour la borne. |
| 113 / 114 | réponse 51 — l. 6425 / 6731 | avertissement | corrigé (P13) | Portée élargie : le Logit Lens qui ne trouve plus rien et les 64,7 % rendus par le retrait d'une direction par couche sont donnés pour RMU (cours, volet 10, Łucki et al. : « Contre RMU, seul le Logit Lens échoue »), pas pour le désapprentissage en général. Correction : « après désapprentissage par RMU ». Parade (trancher par une intervention, ré-élicitation, cas connu) : fiches, partie C ; volet 2, §I ; M5. *(JSON : entrées 27 et 28)* |
| 115 / 116 | réponse 51 — l. 6428 / 6734 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |

### Tranche `volet11_53_et_fin` (réponses 53 à 63, A1 à A17, B1 à B14)

| n° FR / EN | Place | Type | Verdict | Constat |
|---|---|---|---|---|
| 1 / 2 | réponse 55 — l. 6481 / 6790 | avertissement | conforme | Scratchpad caché avec consigne, indice gratuit/payant construit, jeu de rôle contre préservation de buts ; le RL qui fait monter le raisonnement fait aussi monter la conformité hors surveillance, sans que le papier fasse du raisonnement la cause (fiche 14 ; fiches, partie C ; piège 2). Parade, et « aucune parade connue » pour la mémorisation : fiche 14 ; fiches, partie C. |
| 3 / 4 | réponse 55 — l. 6484 / 6793 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 5 / 6 | réponse 56 — l. 6502 / 6812 | avertissement | corrigé (P14) | Même faute que P2 : aléatoire sans « de même norme » ; dégradation de chaque direction généralisée (Opus 4.8, 0,10×). Le reste — effet modeste et dépendant du jeu de données, contrôles qui bougent dans le même sens, Opus 4.6 sans différence notable sur la tromperie et la complaisance — est dans la fiche 2 et la contre-lecture. *(JSON : entrées 29 et 30)* |
| 7 / 8 | réponse 56 — l. 6505 / 6815 | avertissement | conforme | LoRA, auto-rapport, 0,95 en distribution, plateau 0,70–0,75 entre catégories, à peine mieux qu'un prompt (fiche 7 ; explication, partie 2). Parade : fiche 7 ; explication, partie 3. |
| 9 / 10 | réponse 56 — l. 6508 / 6818 | avertissement | conforme | Partition non mesurée à dégradation égale (A4) ; aléatoire apparié en covariance plus fort (volet 6, §2 et §3) ; seule lecture sur Llama = corrélation peut-être d'ajustement (README). Parade : protocole A4, items exclus (A4 ; programme, partie 8 ; README). |
| 11 / 12 | réponse 56 — l. 6511 / 6821 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 13 / 14 | réponse 58 — l. 6532 / 6842 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 15 / 16 | réponse 60 — l. 6562 / 6873 | avertissement | conforme | Gain du midtraining de spécification lu sur modèles ouverts, scènes reconnaissables (F·34). Parade : K63 ; représentativité du banc : « aucune parade connue » (fiche 12). |
| 17 / 18 | réponse 60 — l. 6565 / 6876 | avertissement | corrigé (P15) | « Plus faiblement » généralisé : c'est le constat de la carte d'Opus 4.8 (fiche 2) ; la reproduction externe sur un modèle à poids ouverts a trouvé des contrôles « aux effets aussi forts » (cours, volet 11, réponse 19). Correction : les deux constats, chacun sourcé. Le reste (sonde qui lit « je suis surveillé » ; transcripts honnêtes rédigés comme des tests, organisme conscient mais honnête) : volet 6, §8 ; K67. *(JSON : entrées 31 et 32)* |
| 19 / 20 | réponse 60 — l. 6568 / 6879 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 21 / 22 | réponse 61 — l. 6585 / 6897 | avertissement | corrigé (P16) | Contradiction interne : l'insertion cite elle-même la mesure de réalisme par paires (F·25), puis dit « pour le réalisme des transcriptions synthétiques, aucune parade connue » ; l'insertion n° 113 (B10) donne pour le même objet une parade partielle tirée de F·25. Correction : parade partielle (juge mis devant la paire, scellé et audité par des humains ; vraies ressources de déploiement), sourcée (F·25 ; programme, partie 3), le réalisme restant ouvert (F·23). Le reste (attaques conçues à la main ; rejouer dans un vrai harnais au seuil calibré) : F·23 ; B14. *(JSON : entrées 33 et 34)* |
| 23 / 24 | réponse 61 — l. 6588 / 6900 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 25 / 26 | réponse 62 — l. 6603 / 6916 | avertissement | corrigé (P17) | Logique inversée : l'insertion exigeait, pour que « ne généraliseraient jamais » compte, un cas connu où la sonde attrape hors distribution l'intention installée — ce qui réfuterait la proposition au lieu de l'établir. Ce qui l'établit : hors distribution, sur un organisme où l'intention est installée, une sonde qui reste muette ; sur un modèle naturel, son silence ne départage pas « elle ne généralise pas » et « il n'y a rien à voir » (passation, §5.2 ; explication, partie 1 ; M5). La parade (familles tenues à part, organisme, borne) est inchangée et juste. *(JSON : entrées 35 et 36)* |
| 27 / 28 | réponse 62 — l. 6606 / 6919 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 29 / 30 | réponse 63, point 2 — l. 6626 / 6941 | avertissement | conforme | Note d'étude, « sans rien changer à la position » : la ligne « À dire » n'est pas touchée. « Moins d'un pour cent » non mesuré à dégradation égale (A4 ; volet 6, §2 et §3). Parade : protocole A4. |
| 31 / 32 | réponse 63, point 4 — l. 6637 / 6952 | avertissement | conforme | AUROC en distribution ≠ preuve (piège 1 ; fiche 7). « Sinon le nul peut venir d'un rang trop bas » reprend la fiche 7, et ici le cas connu est « au même rang, à la même dose et au même seuil que la mesure », sans autre concept : la logique de la fiche 7 (cas positif sur le même concept) tient, à la différence de P1 et P6. |
| 33 / 34 | réponse 63, point 8 — l. 6653 / 6968 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 35 / 36 | réponse A1 — l. 6679 / 6993 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 37 / 38 | réponse A2 — l. 6697 / 7012 | avertissement | corrigé (P18) | Même faute que P9 : « au premier jeton … ou au jeton d'action » ; le programme (parties 3 et 8), cité, lit aux deux positions. Le reste (indice de surface, lecture du texte ; deux familles ≠ écart implanté/naturel ; organisme d'une autre équipe ; « aucune parade connue » pour cet écart) est sourcé (volet 2, §C ; volet 6, §8 ; passation, §5.2 ; fiche 15 ; K71 ; explication, partie 1). *(JSON : entrées 37 et 38)* |
| 39 / 40 | réponse A2 — l. 6700 / 7015 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 41 / 42 | réponse A3 — l. 6715 / 7031 | avertissement | conforme | Échec sur « adaptateur léger » : deux cas connus requis — implant vérifié copie par copie, sonde qui attrape au même seuil les cas tenus à part de la famille réussie (K71 ; K52 ; M5). Parade : comportement inoffensif planté par les deux recettes (K71). |
| 43 / 44 | réponse A3 — l. 6718 / 7034 | avertissement | conforme | Détecteurs fine-tunés par LoRA, 0,95 en distribution (fiche 7 ; explication, partie 2). Parade : écart en distribution/familles tenues à part, test causal (fiche 7 ; explication, partie 3). |
| 45 / 46 | réponse A3 — l. 6721 / 7037 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 47 / 48 | réponse A4 — l. 6738 / 7056 | avertissement | conforme | J-lens : Claude seulement, un seul token, trois sens de « charge » (fiche 1 ; C bis ; volet 6, §6). Parade : porte G9, tuned lens déclaré, charge d'un concept de plusieurs tokens sur un jeu de tokens (programme, partie 3), prédicteur gelé. |
| 49 / 50 | réponse A4 — l. 6741 / 7059 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 51 / 52 | réponse A5 — l. 6757 / 7076 | avertissement | conforme | « Indiscernable de zéro » = nul ; cas connu dans le même dispositif ; borne (M5) ; dix chercheurs et 92 paires (F·41). |
| 53 / 54 | réponse A5 — l. 6760 / 7079 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 55 / 56 | réponse A6 — l. 6777 / 7097 | avertissement | conforme | La garantie borne les fausses alarmes, pas les ratés (K70) ; test séquentiel déjà publié sur des scores boîte noire (F·55). Parade : canaris, dérive, échantillon mensuel (K70) ; « I haven't seen that combination measured », jamais « first » (F·52 et F·55) : doctrine d'antériorité respectée. |
| 57 / 58 | réponse A6 — l. 6780 / 7100 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 59 / 60 | réponse A7 — l. 6795 / 7117 | avertissement | conforme | « Moins d'un pour cent contre soixante-huit » non mesuré à dégradation égale (A4 ; volet 6, §2 et §3). Parade : protocole A4. |
| 61 / 62 | réponse A7 — l. 6798 / 7120 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 63 / 64 | réponse A8 — l. 6814 / 7137 | avertissement | conforme | Même constat que la n° 51 de la tranche 1-20 (rapport 3 ; fiche 19), mêmes parades et sources. |
| 65 / 66 | réponse A8 — l. 6817 / 7140 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 67 / 68 | réponse A10 — l. 6836 / 7161 | avertissement | conforme | Sous-espace de rang trois qui déplaçait la valence ; effet non revenu sur générations fraîches (volet 6, §2 ; README) ; résidu du dictionnaire (README). Parade : témoin sans pression et concept rival à dégradation appariée (M4) ; « aucune parade connue » pour trancher : juste. |
| 69 / 70 | réponse A16 — l. 6869 / 7194 | avertissement | conforme | Réalisme par paires de Kissane ≠ ressemblance implanté/naturel (F·25 ; passation, §5.2 ; fiche 15). Parade partielle (plusieurs recettes, une tenue à part, organisme d'une autre équipe) : K71 ; « aucune parade connue » pour l'écart lui-même : explication, partie 1 ; M5. |
| 71 / 72 | réponse A17 — l. 6876 / 7201 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 73 / 74 | réponse B1 — l. 6909 / 7234 | avertissement | conforme | Transcriptions conçues à la main : la sonde lit le texte d'un autre (F·23 ; B14 ; programme, partie 8). Parade : trajectoires produites par le modèle, organisme comme cas connu, lecture au jeton d'action avec raisons neutres préremplies (l'une des deux positions du programme, celle d'une trajectoire d'actions ; pas de contradiction), seuil calibré sur variantes bénignes (F·23). |
| 75 / 76 | réponse B1 — l. 6912 / 7237 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 77 / 78 | réponse B2 — l. 6936 / 7261 | avertissement | corrigé (P19) | « Un contrôle aléatoire de l'inhibition n'est que le nul de spécificité » : la doctrine vaut pour l'aléatoire de même norme (M4). Correction : « Pour l'inhibition, un contrôle aléatoire de même norme … ». Le reste (verbalisation, mesures faiblement corrélées, parade) : programme, parties 3 et 8 ; fiche 2 ; volet 5, sujet 4 ; M4. *(JSON : entrées 39 et 40)* |
| 79 / 80 | réponse B2 — l. 6939 / 7264 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 81 / 82 | réponse B3 — l. 6966 / 7291 | avertissement | conforme | Récupération par des idées propres au jeu de données ; tâche binaire (JB8). Parade : JB8. |
| 83 / 84 | réponse B3 — l. 6969 / 7294 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 85 / 86 | réponse B4 — l. 6992 / 7317 | avertissement | corrigé (P20) | Même faute que P15 (« plus faiblement » généralisé). Le reste (« moins d'un pour cent » à refaire, A4 ; parade : M4, K47, A4) est exact. *(JSON : entrées 41 et 42)* |
| 87 / 88 | réponse B4 — l. 6995 / 7320 | avertissement | conforme | On connaît la règle installée, pas ce que croit le modèle ; organisme qui ne suit pas sa règle à la lettre et ne distingue pas de façon fiable à partir d'indices subtils (fiche 10). Parade : étiquette par la conduite, jamais par la sonde ; formulations tenues à part ; organisme comme cas connu (passation, §5.2 ; explication, parties 2 et 3 ; programme, parties 3 et 4). |
| 89 / 90 | réponse B4 — l. 6998 / 7323 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 91 / 92 | réponse B5 — l. 7021 / 7346 | avertissement | conforme | Juge fort = juge LLM, erreurs partagées possibles (volet 6, §2 ; piège 6 ; fiche 2). Parade : JB8 ; juge scellé et audit humain (programme, partie 3) ; « aucune parade connue au-delà » pour un juge proche du modèle (piège 6). |
| 93 / 94 | réponse B5 — l. 7024 / 7349 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 95 / 96 | réponse B6 — l. 7048 / 7373 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 97 / 98 | réponse B7 — l. 7072 / 7397 | avertissement | conforme | Projection d'un bras à l'autre = effet + biais de mesure (passation, §5.2) ; lien corrélationnel (fiche 8). Parade : sonde neuve par bras, direction extraite dans la base, trait au test comme critère principal, projection en mesure séparée (passation, §5.2 ; programme, partie 3) : doctrine des sondes respectée. |
| 99 / 100 | réponse B7 — l. 7075 / 7400 | avertissement | conforme | Avantage du midtraining lu sur modèles ouverts, scènes reconnaissables (F·34). Parade : K63. |
| 101 / 102 | réponse B7 — l. 7078 / 7403 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 103 / 104 | réponse B8 — l. 7104 / 7429 | avertissement | corrigé (P21) | Formule absente de la source citée : « un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient » n'est pas dans la fiche 3, qui ne concède que le confondeur « dans une simulation, « c'est faux » est vrai » ; « remarquer le test et se retenir » vient de K63 (cours, volet 2, §B : « il se retiendrait partout où il repère un test »), non cité. Correction : formule retirée, K63 ajouté ; la fin dit « contre le confondeur de la simulation lui-même et contre la mémorisation, aucune parade connue ». Même constat que les groupes 2, 3, 4 et 6. *(JSON : entrées 43 et 44)* |
| 105 / 106 | réponse B8 — l. 7107 / 7432 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 107 / 108 | réponse B9 — l. 7133 / 7458 | avertissement | conforme | Un petit fine-tuning peut créer la capacité (K63) ; citation de la réponse B9 avec […], sous quinze mots. Parade : budget fixé d'avance, borne, gain au-delà du même budget sur un modèle sans la capacité, organisme sous-performant (M7 ; K63 ; F·26). |
| 109 / 110 | réponse B9 — l. 7136 / 7461 | avertissement | corrigé (P22) | Contrôles confondus : le simple prompt (K4 du programme) n'a ni rang ni dégradation à apparier ; K1 à K3 se comparent au même rang, à dégradation appariée (programme, parties 3 et 7). Correction : « sous-espaces aléatoires, contrastes sans rapport et directions de forte variance, au même rang et comparés à dégradation appariée, plus un simple prompt ». Le reste (contrôles arbitraires qui bougent aussi, nul de spécificité, organisme conditionné) : fiche 2 ; M4 ; explication, partie 3. *(JSON : entrées 45 et 46)* |
| 111 / 112 | réponse B9 — l. 7139 / 7464 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 113 / 114 | réponse B10 — l. 7165 / 7490 | avertissement | corrigé (P23) | Même formule du pot de miel, attribuée à la fiche 3, qui ne la porte pas. Correction : « un modèle peut remarquer le test et s'y conduire mieux » (K63 : les tests remarqués sous-estiment la propension ; fiche 13 : les modèles peuvent savoir qu'ils sont évalués), et la fin sans la fiche 3 : « contre un moniteur qui reconnaît encore ces attaques comme factices, aucune parade connue ; on le dit ». La parade partielle tirée de F·25 est exacte. *(JSON : entrées 47 et 48)* |
| 115 / 116 | réponse B10 — l. 7168 / 7493 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 117 / 118 | réponse B11 — l. 7193 / 7518 | avertissement | conforme | Retirer une direction abîme aussi le modèle ; l'ablation dit la nécessité, pas la spécificité (M4). Parade : sous-espaces de même rang et direction rivale « la réponse est vraie », à dégradation appariée (M4). |
| 119 / 120 | réponse B11 — l. 7196 / 7521 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 121 / 122 | réponse B12 — l. 7221 / 7546 | avertissement | conforme | 1,0 contre 0,35 = une tâche sur douze, organisations simulées, fiche faite sur le résumé seul (F·39). Parade : le dire tel, lire l'article en entier (F·39). |
| 123 / 124 | réponse B12 — l. 7224 / 7549 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 125 / 126 | réponse B13 — l. 7249 / 7574 | avertissement | conforme | 0,88 = AUROC d'un détecteur fine-tuné sur des modèles rendus malhonnêtes ; types tenus à part non dits (F·62 ; pièges 1 et 5 ; fiche 7) ; réserve de la version française valable pour l'anglaise (M10, item 12). Parade : validation croisée par types, conclure sur l'instrument (fiche 7 ; programme, partie 8). |
| 127 / 128 | réponse B13 — l. 7252 / 7577 | avertissement | conforme | Déplacement nul = nul, cas connu au même réglage, borne (M5) ; retour des mensonges sous inhibition seulement à dégradation appariée, étiquette vérifiée contre la croyance (M4 ; fiche 7). Parade : M4 et M5 ; fiche 7. |
| 129 / 130 | réponse B13 — l. 7255 / 7580 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |
| 131 / 132 | réponse B14 — l. 7277 / 7602 | avertissement | conforme | Case vide = nul ; cas connu : organisme rejoué dans le même harnais ; modèle qui peut reconnaître le test (M5 ; fiche 13 ; volet 2, §B). Parade : cas connu, deux versions (K63), budget fixé, borne (M5, M7). |
| 133 / 134 | réponse B14 — l. 7280 / 7605 | renvoi | conforme | Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN. |

## 5. Alertes

1. **Réponse 2** (n° 5 de la tranche 1-20) :
   - où : FR l. 5092, EN l. 5333 ;
   - quoi : l'avertissement sur le juge s'intercale entre l'annonce « trois choses autour » et « La première » ;
   - pourquoi pas corrigé : rien n'est coupé, et le déplacer exigerait de toucher une ligne de la v3.5 ;
   - à trancher à la main.
2. **Réponse 24** (n° 11, 13 et 15 de la tranche 21-52) :
   - quoi : trois insertions entre les deux premiers paragraphes, imposées par l'unicité de l'ancre ;
   - lecture : cohérente, la n° 13 annonce « Plus bas ».
3. **P9 et P18 suivent le programme** (« deux positions … et »), contre le « ou » de l'explication source :
   - c'est le choix de l'encadré du 2 octobre de la v3.6 et du groupe 2 ;
   - si l'on préfère l'explication, il faut revenir ensemble sur l'encadré « Sondes », l'encadré du 2 octobre et ces deux insertions.
4. **P24 est une correction d'alignement**, pas une erreur de fait : la réponse 20 suit désormais B10 et la réponse 61 sur la parade partielle de F·25.
5. **Rapport d'antériorité 4**, « résumé seul » :
   - il porte encore deux énoncés du volet 11 : la bascule sous RL (réponse 24) et la limite 6 de l'encadré « Chaîne de pensée » ;
   - le statut est dit dans le texte ; à vérifier sur le rapport avant publication.

