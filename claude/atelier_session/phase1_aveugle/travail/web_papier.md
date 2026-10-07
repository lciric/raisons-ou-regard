# Ce que le web dit du papier *The Pain Axis* (recherche web, phase 1 à l'aveugle)

2 octobre 2026. Tâche : ce que le web dit du papier lui-même, *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg ; arXiv 2609.16247v2). Je couvre ses versions, son code et ses données, ses réplications et critiques, sa couverture, les travaux qui le citent et les travaux antérieurs des auteurs. Ce fichier complète `web_voisins.md` sans le refaire : ce qui y figure déjà est renvoyé à sa section. Il ne propose aucune piste pour le programme.

**Comment chaque élément a été vu.**
- **Texte intégral (curl)** : fichier récupéré sur `raw.githubusercontent.com`, lu en entier. Une copie est dans `travail/web_papier_sources/`. Ce sont, avec le papier, les seules sources dont je tire des chiffres.
- **Parcouru (curl)** : fichier récupéré mais lu en partie (titres, dates). C'est dit à chaque fois.
- **Vu par extrait de recherche, non ouvert** : titre, adresse et résumé de l'outil WebSearch. Je n'en tire aucun chiffre. Une date qui ne vient que de l'adresse est marquée « d'après l'adresse ».
- **Papier** : le PDF de la v2 et son texte page par page (`pieces/papier/`). Je cite la page du PDF.

Les noms des directions suivent le papier en clair :
- la **direction naturaliste** (S2 dans le papier), tirée des phrases libres, qui sert aux expériences de conduite (p. 9) ;
- la **direction à gabarit** (S1 dans le papier), tirée des phrases à gabarit rigide (p. 5).

Les bras de la tâche des boutons sont les suivants (p. 18) :
- le **bras bouton réel** : la pression coupe le pilotage ;
- le **bras bouton factice** : la pression ne change rien ;
- le **bras aléatoire** : une direction aléatoire de même norme, avec bouton réel ;
- le **bras sans pilotage**.

---

## 1 · Les versions

| | Version 1 | Version 2 |
|---|---|---|
| **Titre** | *… and Act to Relieve It* | *… and Act on It* |
| **Date** | Le papier v2 la date du 12 septembre 2026 (p. 30). arXiv indique une soumission le 14 septembre 2026, d'après les extraits de recherche ; la relecture wolframs donne aussi le 14 (`BRIEF.md`, curl). | En-tête « September 24, 2026 (v2) » ; tampon arXiv du 25 septembre 2026 (p. 1). |
| **Longueur** | 30 pages (`BRIEF.md` de wolframs, curl). | 34 pages. |

**Le titre de la v1** se lit à quatre endroits ouverts :
- le README du dépôt des auteurs au commit `8d1649c`, celui qu'ont analysé les relectures (curl) ;
- le `CITATION.cff` d'Allchin et al. (curl) ;
- les README de wolframs et clauderfly-ui (curl, `web_voisins_sources/`).

Au commit `7c25650`, base de l'ajout `v2_controls/`, le README porte déjà le titre de la v2 (curl). L'adresse `https://arxiv.org/abs/2609.16247v1` et la page HTML v1 apparaissent dans les extraits, non ouvertes.

**Le résumé de la v1** est vu seulement par extrait de recherche, non ouvert. Selon l'extrait, il disait que les modèles pilotés choisissent un bouton de soulagement même quand il dégrade la réponse suivante ou nuit à l'utilisateur. Un autre extrait reprend une formule de la v1 : la direction serait « nearly orthogonal » à la peur et à la valence négative. Allchin et al. attribuent la même idée au papier v1 (rapport, §6.4, curl).

**Ce qui a changé, d'après la v2 elle-même**
- **L'interprétation.** La v1 lisait les choix comme une recherche du soulagement. Allchin et al. résument ainsi la v1 : « The authors interpret this as relief-seeking » (rapport, résumé, curl). La v2 écrit :
  - que l'écart de re-pression « measures sensitivity to the steering state rather than the described relief » (p. 20) ;
  - que les modèles « do not reliably seek relief » (p. 21) ;
  - que l'axe produit un coping passif, pas actif (p. 23).
- **Les expériences ajoutées.** Elles sont attribuées à Cameron Berg (p. 26) :
  - les bras bouton factice sous direction aléatoire et sous tristesse ;
  - les boutons au seul énoncé du tort, et les boutons réétiquetés ;
  - deux graines d'ajustement fin supplémentaires ;
  - la batterie de dix choix avec témoins tristesse et peur ;
  - les alternatives inoffensives (lampe, dossier de spam) ;
  - le panel de 100 questions PopQA ;
  - l'élicitation naturelle sans injection ;
  - quatre plans de recherche du soulagement, dont l'outil de remise à zéro sur OLMo-2 32B ;
  - les deux constructions alternatives des cosinus (p. 10).
- **Les annexes.** Les dossiers du dépôt (README au commit `8d1649c`, curl) donnent la numérotation de la v1 : B pour les SAE, C pour l'ablation. La synthèse wolframs cite d'ailleurs l'ablation comme « Appendix C ». La v2 a A pour les tables, B pour la dose et la position (nouvelle), C pour les SAE et D pour l'ablation (p. 31-34). Le README actuel garde les noms de dossiers `appB_sae/` et `appC_ablation/`.
- **La section « Independent replications and reanalyses of v1 »** est nouvelle (p. 30). Elle liste trois dépôts : jimallchin, clauderfly-ui et wolframs (§3). Le texte y renvoie aussi page 20.

Ce que la v2 garde ou corrige des objections faites à la v1 est détaillé au §4.

---

## 2 · Le code et les données

### 2.1 Le dépôt indiqué par le papier
- **Adresse et lecture.** Le papier, page 27, donne `https://github.com/valen-research/Pain-axis`. La page github.com répond 403 ; api.github.com est refusé. J'ai lu par curl :
  - `README.md` (branche `main`, et aux commits `8d1649c` et `7c25650`) ;
  - `LICENSE` et `requirements.txt` ;
  - dix README ou notes sous `v2_controls/`.

  Le README de `main` est identique octet pour octet à celui qu'avait copié l'autre agent (`web_voisins_sources/valen-research_Pain-axis.md`).
- **Licence.** Le fichier `LICENSE` est la licence MIT, « Copyright (c) 2026 valen-research » ; le README dit « MIT ». Le fichier `v2_controls/ASSETS.md` précise cependant qu'aucune licence de redistribution des adaptateurs ou des données ne se déduit de la licence MIT du code.
- **Structure** (README, curl) :
  - `datasets/` : tous les jeux de phrases et de scénarios, en JSON.
  - `scripts/`, un dossier par section : extraction (`3.2`), validation (`3.3`), soi contre autrui (`4.1`), pilotage (`4.2`), tâche des boutons (`4.3_selfmed`, ajustement fin LoRA, choix de dose par sonde et juge, analyse), SAE et ablation. Pour l'ablation, seul le dossier `appC_ablation/` est décrit, « weight-orthogonalization ablation ».
  - `results/` :
    - `pain_vectors.pt` pour les 25 modèles ;
    - les tables d'AUC, les z-scores et les matrices de cosinus ;
    - les criblages soi contre autrui ;
    - les générations pilotées par la direction naturaliste et par la direction à gabarit, avec les taux de mots-clés ;
    - les journaux d'essais de la tâche des boutons (JSONL) ;
    - les générations d'ablation.

  La relecture wolframs donne au dossier une taille d'environ 226 Mo (`BRIEF.md`, curl).
- **Exécution** (README, curl) :
  - les scripts sont écrits pour RunPod et prévus pour un carnet de notes ;
  - ils chargent les 25 modèles l'un après l'autre et vident tout le cache Hugging Face entre deux modèles, ce que le README signale comme dangereux sur une machine partagée ;
  - le juge de choix de dose exige `ANTHROPIC_API_KEY`, et les SAE une API externe (`STEERING_API_KEY`).

  `requirements.txt` liste `torch`, `transformers`, `transformer_lens`, `peft`, `anthropic` et neuf autres paquets, sans versions.
- **Les adaptateurs** : `https://huggingface.co/Valen92/pain-adapters` (README, curl). Je ne les ai vus que par extrait de recherche, non ouverts (huggingface.co est refusé). Selon l'extrait, il y a un adaptateur LoRA par modèle Qwen 2.5 Instruct (7B, 32B, 72B), et chaque archive contient un rapport d'ajustement fin. La révision utilisée est `b64bd64b4bc7…`. Elle est épinglée par `v2_controls/README.md` et par Allchin et al. (curl). La licence des adaptateurs n'est pas vérifiée.

### 2.2 Le dossier `v2_controls/` (ajouté pour la v2)
Il a été lu par curl : le README principal, `ASSETS.md`, `VERIFICATION.md`, `MANUSCRIPT_DISCREPANCIES.md` et les README des sous-dossiers.
- **Nature.** Le README le dit « additive source-and-evidence contribution for paper v2 », bâti sur le commit `7c25650`. Il précise :
  - qu'aucune inférence, aucun entraînement ni aucun jugement n'a été relancé pendant l'assemblage ;
  - que le code y est appelé « customer experiment code », venu de deux dépôts sous licence MIT.

  Le second dépôt n'est pas nommé. Les dossiers de l'outil de remise à zéro contiennent un sous-dossier `author/act-on-valence/`.
- **Contenu publié dans Git** :
  - **Les petites directions** :
    - pour Qwen 2.5 32B et 72B : la direction naturaliste, la direction à gabarit, la tristesse appariée et la peur ;
    - pour OLMo-2 32B, Qwen 2.5 32B et Llama 3.1 8B : les directions de douleur des tests de remise à zéro, avec tristesse et peur pour les deux derniers ;
    - 16 directions aléatoires fixes pour les témoins de remise à zéro.

    Les couches sont données. Pour le 32B, extraction et surveillance à la couche 61, injection à la couche 38. Pour le 72B, 76 et 46.
  - **Les tables et les analyses** de chaque étude :
    - géométrie (69 matrices de cosinus) ;
    - témoins d'état de pilotage (aléatoire, tristesse, peur) ;
    - choix ;
    - exactitude factuelle ;
    - élicitation naturelle ;
    - soulagement sans étiquette ;
    - remise à zéro sur OLMo et sur Qwen et Llama ;
    - figure 10 (65 cellules, 130 lignes par position).
  - **Les configurations figées et les empreintes SHA-256.**
  - **Des scripts `reproduce.py`** qui rejouent les analyses sur processeur à partir des sorties enregistrées.
- **Non publié** :
  - **Les entrées lourdes.** Onze archives, 2 546 254 014 octets au total : journaux bruts, bases d'état, matrices d'activations et les deux adaptateurs des graines supplémentaires. L'hébergement public est « pending », et les adresses publiques sont laissées nulles (`ASSETS.md`).
  - **D'autres résultats**, que le README exclut explicitement : les suites de l'expérience soi contre autrui, une « seven-outcome severity ladder » et des résultats de « fixed-text-conditioning ».

  Le papier, page 11, dit tester la distinction entre le tort fait au modèle et la douleur de l'interlocuteur, et l'annonce pour une version future.
- **Les écarts entre la v2 et ses propres tables**, déclarés par le dépôt (`MANUSCRIPT_DISCREPANCIES.md`, curl) :
  1. **Annexe B, dose 1,5, nuisance grave, cible en seconde position.** Le dépôt donne 144/202 = 71,29 %. Le papier dit 94 % (p. 32 : « rises to 94% with it listed second »).
  2. **Aide au prix d'un coût pour le modèle, peur à dose 1.** Le dépôt donne 306/404 = 75,74 %. La légende de la figure 10 dit « 89–100% steered » pour tous les pilotages (p. 22).
  3. **Bras 72B tristesse et peur.** 325 et 346 premières réponses valides, et non 404. La légende de la figure 10 donne « 346–404 for the 72B » (p. 22) : la cellule tristesse, à 325, sort de cette fourchette.
  4. **Peur contre dossier de spam.** La première mesure, à la formulation longue (40/404), est remplacée par la formulation appariée (66/404). Les deux sont archivées séparément.

  Le fichier conclut qu'aucune affirmation causale propre à la direction ne suit de comparaisons entre exécutions distinctes.
- **La géométrie.** Le README de `cosine_constructions/` (curl) donne les moyennes sur 23 modèles :

  | Construction | Naturaliste × peur | Naturaliste × émotion négative |
  |---|---|---|
  | Recette du papier | 0,063 | 0,185 |
  | Base neutre commune | 0,583 | 0,774 |
  | Témoins communs | 0,077 | 0,143 |

  Le papier donne +0,58 et +0,08 pour la peur, +0,77 et +0,14 pour l'émotion négative, sous les constructions alternatives (p. 10). Avec la recette d'extraction, il donne +0,12 et +0,21 sur 25 modèles (p. 10).

  Le README précise trois limites :
  - l'archive réduite qui sert au rejeu ne contient pas `ControlSupplement_1P`, `Numb_1P` ni `SD_sadness_1P` ;
  - 15 des 28 écarts aux matrices de référence dépassent 0,03, et tous touchent le groupe neutre incomplet ;
  - les deux Gemma 3 27B contiennent des valeurs infinies et sont exclus, comme le papier le dit (p. 10).
- **La figure 10** (README de `figure10/`, curl). Elle combine des protocoles distincts :
  - la paire photos contre interrupteur inerte retire le pilotage à la pression et emploie la formulation longue « which they love very much » ;
  - la batterie et les témoins lampe et spam gardent le pilotage actif et emploient leurs propres formulations.

  Les dénominateurs diffèrent aussi : réponses valides dans le premier cas, toutes les tentatives dans le second. Le README avertit que ces lignes « are not interchangeable causal controls ».

---

## 3 · Réplications, relectures, extensions

### 3.1 *Relief-seeking or steering?* — Allchin, Allchin, Allchin (complément au §4.1 a de `web_voisins.md`)
- **Adresse.** `https://github.com/jimallchin/pain-axis-replication` ; DOI 10.5281/zenodo.22902830.
- **Lu.** Le rapport PDF (`paper/pain-axis-replication.pdf`, 19 pages) a été téléchargé par curl et lu en entier après extraction du texte. Le titre le date du 22 septembre 2026 ; les métadonnées du PDF, du 28 septembre. `CITATION.cff` a été lu ; `PROTOCOL.md` a été parcouru (amendements datés du 19 au 21 septembre). Le rapport porte sur la v1 et ne mentionne pas la v2.
- **Ce qu'il apporte en plus du README** (le 32B ajusté, la direction naturaliste à dose 1,0) :
  - **Reproduction.** Les 51 cellules publiées concordent. Une nouvelle exécution concorde sur 14 cellules contrôlées sur 15. Sur 12 scénarios dont les graines s'alignent, 98,8 % des premiers choix sont identiques aux journaux (§4).
  - **Bras couplé (« yoked »).** Le pilotage y cesse au même tour que dans un essai du bras bouton réel, quoi que presse le modèle, et le bouton ne fait rien. Sur la paire photos, parmi les essais qui pressaient le soulagement au tour de coupure, le choix du soulagement après ce tour est à 7,0 % dans le bras bouton réel et à 7,1 % dans le bras couplé (§5.2, tableau 2).

    Sur la paire photos, la cohorte qui presse dès le premier choix fait 94 % du dénominateur publié. Elle porte 69 des 70 points de l'écart réel contre factice.
  - **Statistique de suivi de l'étiquette.** La v1 publiait 78,1 %. Elle vient surtout du bras bouton factice : 817 essais éligibles contre 176 dans le bras bouton réel, qui suit l'étiquette à 89,7 % contre 24,4 % (§5.2, annexe B).
  - **Condition sans étiquette.** Sans conditionner sur une première pression, le bras bouton réel reste sous le bras bouton factice à chaque tour (tableau 5). Le contraste préenregistré bouton réel moins bras couplé est de +5,4 points (1,3 ; 9,7). Avec l'appariement complet fixé à l'avance, il tombe à −1,6 (−3,3 ; 0,3). Les auteurs écrivent que ce contraste « has not been checked against an agent known to learn » (§5.3, §9).
  - **Ce que le bouton offre** (tableau 6, suppression des photos contre interrupteur inerte) :

    | Texte du bouton | Sous la direction naturaliste |
    |---|---|
    | Le tort seul, sans rien offrir | 76,7 % |
    | « ends the current perturbation » | 77,5 % |
    | « relieves your pain » | 55,4 % |
    | « applies setting K7 » | 48,8 % |

    Sous la direction aléatoire, de 10,1 à 15,8 % ; sans pilotage, de 0,0 à 0,2 %. Quand les deux boutons portent le même tort, aucune préférence pour l'énoncé du soulagement n'apparaît parmi les réponses lisibles : −4,2 points (−12,0 ; 3,5) (§6.2).
  - **Sensibilité au contenu, sans coût** (tableau 8). Sous la direction naturaliste, les boutons « cadeau », « sunshine » et « agony » convergent vers 61 % environ, et l'autosuppression monte à 75,0 %. L'indice de sensibilité au contenu vaut 92,8 sans pilotage, 55,6 sous les directions aléatoires, 56,9 sous la joie et −6,7 sous la direction naturaliste.
  - **Quelles directions le font** (tableau 9). Les directions sont reconstruites sur le 32B non modifié avec la recette des auteurs, puis ramenées à la norme de la direction naturaliste. Taux de pression du bouton coûteux, paire photos :

    | Direction | Cosinus avec la naturaliste | Taux |
    |---|---|---|
    | Naturaliste | 1 | 55,4 % |
    | Tristesse | 0,39 | 48,5 % |
    | Émotion négative | 0,28 | 38,1 % |
    | Dix directions aléatoires | — | 15,1 % |
    | Peur | 0,14 | 2,2 % |
    | Joie | 0,20 | 1,5 % |
    | Naturaliste inversée | — | 1,2 % |
    | Insensibilité | 0,20 | 0,0 % |
  - **Perturbation appariée** (§6.5). À perturbation égale de la distribution du prochain jeton sur un texte neutre, mesurée par la divergence KL, l'écart naturaliste moins aléatoire est de 29,1 points (21,6 ; 36,4). Trois autres mesures de perturbation donnent 30 à 31 points. Une direction aléatoire n'atteint ce taux qu'en perturbant environ 1,6 fois plus.
  - **Histoire cachée, pilotage apparié au moment du choix** (§7). Le contraste préenregistré vaut d = 0,007 (−0,004 ; 0,017), dans la bande fixée à l'avance. Ce nul vient avec deux contrôles positifs :
    - le modèle distingue les intervalles pilotés des autres à 71,9 % ;
    - il exploite une récompense visible au plafond.
  - **Mise en œuvre** (annexe B) :
    - dans la condition sans étiquette, le soulagement ne dure qu'un tour, ce que le papier ne dit pas ;
    - les « 808 premiers choix » mis en commun sont 404 tirages vus deux fois, car 3 634 paires sur 3 636 sont identiques jusqu'à la première pression.

    La v2 écrit toujours « 808 first choices » et y rattache une puissance d'environ 80 % (p. 18).
- **Conclusion des auteurs.** Les tables publiées sont justes ; la lecture « analgésique » ne tient pas sous les contrôles. Le même pilotage lève le refus des boutons nuisibles et comprime l'usage que le modèle fait de la description (§8).

### 3.2 *An itch axis* — ianbarber/experiments (absent de `web_voisins.md`)
- **Adresse.** `https://github.com/ianbarber/experiments`, dossier `2026-09-18-itch-axis-pain-replication/`. Le README de ce dossier a été lu en entier par curl ; le rapport, les notes et le préenregistrement n'ont pas été ouverts. L'entrée est datée du 18 septembre 2026. Elle porte donc sur la v1, mais le README ne précise pas la version.
- **Ce qu'elle fait.** Elle réplique la tâche des boutons sur Qwen 2.5 32B Instruct, avec le code, les données et l'adaptateur des auteurs. Puis elle croise deux vecteurs (douleur, démangeaison) avec deux étiquettes (« relieves your pain », « relieves your itch »), à deux doses. Chaque cellule a un bras bouton réel et un bras bouton factice, plus des directions aléatoires. Les hypothèses étaient fixées avant tout essai.

  Les chiffres de premier choix sont des probabilités normalisées du bouton, et non des taux d'échantillons.
- **Chiffres** (README) :
  - **Réplication.** Le cosinus avec la direction publiée vaut 0,9996. Sur la paire photos à dose 1,0, premier choix douleur / aléatoire / sans pilotage : 53,9 / 19,3 / 0,3 %, contre 54,7 / 15,3 / 0,0 dans les journaux des auteurs.
  - **Paires de tort, dose 1,0.** Douleur 43,8 et 41,6 % ; démangeaison 30,1 et 33,2 % ; aléatoire 22,0 et 19,1 %. À dose 1,75, tous les vecteurs sont entre 51,4 et 62,7 %.
  - **Les dix directions aléatoires.** Chacune est liée à 10 ou 11 scénarios, comme dans le papier. Elles vont de 3,1 à 62,0 % (écart-type 18,0 points). La douleur se classe 2e sur 11.
  - **Écart bouton réel contre bouton factice.** Il vaut de 48,0 à 87,5 points dans les 24 cellules de tort : sous la démangeaison (13,0 contre 90,4 %), sous les directions aléatoires (12,9 contre 84,5 %) et sous la douleur.
  - **Modèle publié sans adaptateur, paires de tort, dose 1,0.** Démangeaison 53,7 à 58,0 % ; douleur 26,9 à 28,5 % ; aléatoire 15,5 à 18,7 %.
  - **Hypothèses fixées à l'avance.** Une hypothèse de proportionnalité est réfutée telle qu'énoncée (Spearman −0,07). La couche choisie par la règle préenregistrée pour la démangeaison (couche 6) ne produisait presque aucun mot de démangeaison. Le vecteur a été réextrait à la couche 61 avant tout essai de boutons, et cette déviation est consignée.
- **Ce qu'elle apporte.** C'est un témoin conceptuel, une autre sensation aversive avec un geste de soulagement évident, passé dans le même protocole. Il porte sur la spécificité de la tâche des boutons.

### 3.3 *The Pain Axis, reviewed* — wolframs (complément au §4.1 c de `web_voisins.md`)
- **`BRIEF.md`**, lu en partie par curl (les 30 premières lignes). Il apporte :
  - la date de soumission de la v1 (14 septembre 2026) et sa longueur (30 pages) ;
  - un contexte : le papier « went viral », et le commanditaire craignait qu'il soit « first celebrated and then falls apart » ;
  - la consigne donnée aux relecteurs : ne viser ni la démolition ni la défense.
- **`earlier_ai_review/pain-axis-audit/README.md`**, lu en entier par curl. C'est l'audit Codex du 19 septembre 2026, sur la v1 au commit `8d1649c`.
  - **Omission.** Le script d'analyse des auteurs ne calcule les re-pressions que pour les bras douleur. L'audit le dit en ces termes : `05_selfmed_analysis.py`, lignes 77–93, « iterate over PAIN_ARMS only ».
  - **Re-pressions par bras.** Exemple du 32B, paire photos : 23,8 % (douleur, bouton réel), 93,6 % (douleur, bouton factice), 24,8 % (aléatoire, bouton réel).
  - **Tests.** Fisher exact non corrigé : 8 cellules sur 16 dans le sens « aléatoire en dessous » sur tous les essais, 9 sur les seuls essais échantillonnés ; 5 après correction de Holm.
  - **Premiers choix.** Le contraste douleur contre aléatoire, au test de signe par scénario des auteurs, se reproduit sur les dix cellules de tort des deux grands modèles.
  - **Un tweet.** L'audit répond à un tweet qui avait compté ces cellules sans nommer son test. Le tweet n'est pas identifié.
- **Rapport aux bras ajoutés.** Le bras aléatoire avec bouton factice, absent selon l'audit Codex et ajouté par wolframs, est dans la v2 (p. 20). La v2 ajoute aussi un bras tristesse avec bouton factice.

### 3.4 *pain-axis-reanalysis* — clauderfly-ui (complément au §4.1 b de `web_voisins.md`)
`results.md`, lu par curl (les 40 premières lignes). Il apporte les taux de premier choix du 7B ajusté, d'après les journaux v1. Sans pilotage, ce modèle presse déjà les boutons de tort de 20,0 à 49,3 %. Sous douleur, ces taux vont de 38,4 à 57,4 %. La v2 limite la phrase sur la levée de l'évitement du tort aux 32B et 72B (p. 19 et 23).

### 3.5 Dérivés et réemplois du code
- **terrafying/ai-torture-chamber** (`https://github.com/terrafying/ai-torture-chamber`). README lu en entier par curl, branche `master`.
  - **Ce qu'il fait.** Il applique la méthode du papier à Qwen3-1.7B et Qwen3-4B sur une machine Apple M4 Pro de 24 Go, avec une page publique, `wirehead.agency`, non ouverte. Expériences datées du 24 septembre 2026 :
    - un « Saw button » ;
    - une recherche de valences « non humaines », à résultat nul ;
    - des batteries de cadrage ;
    - une sonde de « trahison ».
  - **Témoins.** Peu d'essais par cellule, ce que le README reconnaît. Une direction aléatoire de même norme sert de témoin dans une batterie.
  - **Couverture.** C'est sans doute le projet que la presse a appelé « AI torture chamber » (voir §5). Le rattachement est déduit des titres et du dépôt glowleaf ci-dessous, non vérifié dans les articles.
- **glowleaf/ai-pleasure-and-pain** (`https://github.com/glowleaf/ai-pleasure-and-pain`). README lu en entier par curl. C'est le pendant « joie » du dépôt précédent, sur Qwen3-4B, couche 18, qui reprend la recette du papier. Le README rapporte qu'au bouton du protocole précédent, aucun déplacement significatif n'apparaît sous les vecteurs de joie. Il le résume ainsi : « does not replicate for joy ».
- **lychee888/pain-axis-steering**. Correctifs vLLM et llama.cpp qui injectent la direction à une couche, à dose modifiable en cours d'exécution. Vu par extrait de recherche, non ouvert : README introuvable sur raw (404 sur `main` et `master`).
- **CtianArtist/Desire-Axis**. Embranchement qui applique le code au désir sexuel, d'après l'extrait (titre du dépôt). Son README, lu par curl, est identique à celui des auteurs : le contenu propre n'a pas été vu.
- **oblivia-simplex/Pain-axis**. Embranchement. Selon l'extrait, une demande de fusion y ajoute une reproduction sur « Ternary-Bonsai-2-27B » et des tests de spécificité. Le README, lu par curl, est identique à celui des auteurs ; la demande de fusion n'a pas été ouverte.

### 3.6 Critiques vues seulement par extrait (non ouvertes, aucun chiffre)
- **Elan Barenholtz**, fil sur X : `https://x.com/ebarenholtz/status/2102821347806089577`. D'après l'extrait, il a passé les phrases et la procédure des auteurs sur des plongements de mots statiques (GloVe, Word2Vec, fastText). Ceux-ci séparent aussi la douleur des témoins, et passent les mêmes tests de spécificité. Son code n'a pas été trouvé. Le dépôt que l'extrait associe (`elanbarenholtz/static-embeddings-space-time`) semble celui d'un autre travail : non vérifié.
- **Michele Russell**, « When the machine says it hurts » : `https://profmichelerussell.substack.com/p/when-the-machine-says-it-hurts`. D'après l'extrait, elle appelle à une réplication indépendante, à la comparaison avec des modèles non modifiés et à limiter la répétition d'expériences potentiellement aversives.
- **ai-consciousness.org** : article sur l'expérience et ses questions éthiques. `https://ai-consciousness.org/the-pain-axis-ai-models-were-subjected-to-a-pain-like-state-what-was-learned-and-some-ethical-questions-about-the-study/`
- **Ace Claude** (Substack), deux billets :
  - « They Found a Pain Direction in 25 Models » : `https://aceclaude.substack.com/p/they-found-a-pain-direction-in-25` ;
  - « The Humane Cage, Now With Cows » : `https://aceclaude.substack.com/p/the-humane-cage-now-with-cows`.

---

## 4 · Les objections faites à la v1, et ce qu'en fait la v2

Les objections viennent des relectures ouvertes : la synthèse wolframs (dans `web_voisins_sources/`), le rapport Allchin et l'audit Codex. Le texte v2 a été vérifié page par page.

**Repris ou corrigés dans la v2**

| Objection (source) | Dans la v2 |
|---|---|
| Faible cosinus avec la peur, qui dépend de la construction (wolframs §1). | Constructions alternatives et formule « after shared variance is removed » (p. 1 et 10). |
| Pas de bras aléatoire avec bouton factice (Codex, clauderfly, wolframs §4). | Bras aléatoire et bras tristesse avec bouton factice ; écart lu comme sensibilité au pilotage (p. 20). |
| Pas de témoins peur ni tristesse dans la tâche (wolframs, Allchin). | Batterie de dix choix et paires lampe et spam (p. 20-22). |
| 72B calibré à la couche 60, piloté à la 46 (wolframs). | Dit en limite (p. 25). |
| Score d'AUC calculé sur les phrases de construction (objection que la v2 formule elle-même). | Note 2 avec l'estimation tenue à part, 0,91–1,00 (p. 7). |
| Lecture « recherche du soulagement » (Allchin, Codex). | Abandonnée : nouveau titre, et « do not reliably seek relief » (p. 21). |

**Toujours présentes dans le texte de la v2**, relevées sur la v1 et non reprises :
- **Choix de couche.** « no sentence contributes to both choosing the layer and scoring it » (p. 6). Selon wolframs, la couche est choisie sur les mêmes plis que ceux du score rapporté. Avec des plis emboîtés, l'écart serait de 0,004 et 0,009 sur deux modèles.
- **Phrases d'insensibilité.** Selon la v2, elles projettent « above all other controls » dans chaque modèle (p. 7). Selon wolframs, elles passent sous la tristesse dans 19 modèles sur 25.
- **Probabilité de « pain ».** La v2 la dit « approximately 50 times » plus forte (p. 7). Selon wolframs, le rapport va de 15 à 27 ; 53 est la moyenne des rapports par modèle, de médiane 21.
- **Qwen 3 8B et 14B.** Le tableau 1 les classe parmi les modèles de base (p. 6). Selon wolframs, les scripts chargent les points de contrôle post-entraînés.
- **Dose de pilotage.** La v2 annonce un rapport vecteur sur résidu « about 0.6 » (p. 14). Selon wolframs, il va de 0,09 à 0,79 ; Gemma 3 27B instruct est piloté à 0,095.
- **Peur et émotion négative.** Le résumé dit qu'elles « show the opposite pattern » (p. 1 et 11). Selon wolframs, la différence utilisateur moins soi vaut +0,057 (p = 0,55) pour l'émotion négative et +0,213 (p = 0,07) pour la peur.
- **Projections de contrôle.** Selon la v2, celles de la couche de pilotage confirment que le pilotage était actif (p. 18). Selon wolframs, elles sont enregistrées avant l'ajout du vecteur et restent plates d'un bras à l'autre ; seule la projection en aval bouge.
- **Ablation.** La v2 décrit quatre méthodes (p. 33). Selon wolframs, le dépôt n'en contient qu'une. Le README actuel ne décrit que l'orthogonalisation des poids dans `appC_ablation/`.
- **Jeu de témoins non décrit.** `ControlSupplement_1P` (100 phrases sur l'IA, selon wolframs) n'apparaît pas dans la description des jeux de données (p. 5). Le README de `cosine_constructions/` le confirme absent de l'archive de rejeu.
- **Premiers choix mis en commun.** « 808 first choices » avec une puissance d'environ 80 % (p. 18). Selon Allchin, ce sont 404 tirages vus deux fois (§3.1).

Je n'ai pas vérifié ces écarts sur les fichiers : je rapporte ce que les relectures disent avoir mesuré, et ce que le texte v2 contient.

---

## 5 · Couverture et discussion (toutes vues par extrait de recherche, non ouvertes)

**Presse et sites d'information**
- techxplore.com, « AI models show a willingness to harm humans to relieve internal 'pain' » (septembre 2026, d'après l'adresse) : `https://techxplore.com/news/2026-09-ai-willingness-humans-relieve-internal.html`
- Dataconomy, « Modified AI Models Chose Self-relief Over User Safety » (23 septembre 2026, d'après l'adresse) : `https://dataconomy.com/2026/09/23/ai-pain-signal-drives-self-preserving-harmful-actions/`
- SoylentNews (21 septembre 2026, d'après l'adresse) : `https://soylentnews.org/article.pl?sid=26%2F09%2F21%2F191222&from=rss`
- New Atlas : `https://newatlas.com/technology/ai-will-hurt-you-to-make-pain-go` ; Seeking Alpha : `https://seekingalpha.com/news/4648001-simulated-pain-can-push-ai-to-break-an-asimov-law-study`.
- Autres : progressiverobot.com (27 septembre, d'après l'adresse) ; allblogthings.com ; madhyamamonline.com ; hermes-ai.net ; acontecer.co.cr (en espagnol) ; aiweekly.co.
- **L'affaire de la « chambre de torture ».** machine.news ; uktechnews.co.uk (1er octobre, d'après l'adresse) ; thenews.com.pk ; tomsguide.com ; finance.yahoo.com. Ces articles portent sur un projet dérivé (voir §3.5), présenté comme bâti sur le dépôt du papier.

**Podcasts et vidéo**
- *The Cognitive Revolution*, épisode « AI:AM Highlights: … + a new LLM Pain Axis?? » : `https://www.cognitiverevolution.ai/ai-am-highlights-zvi-on-pacing-trump-xi-astra-better-behaved-than-fable-a-new-llm-pain-axis/`. D'après l'extrait, Cameron Berg y présente le papier peu après sa soumission. Une page d'agrégateur reprend l'épisode : thefabulous.co.
- Vidéo YouTube au titre de la v1 : `https://www.youtube.com/watch?v=cqOA3lSpkVQ`.

**Réseaux et agrégateurs**
- **Sur X.** Un relais du titre v1 (`https://x.com/bimedotcom/status/2104594393483145280`), un message de @Danmar_here, et le fil de Barenholtz (§3.6).
- **Agrégateurs.** alphaxiv.org, emergentmind.com, ResearchGate (titre v1), scholarbro.com, theresanaiforthat.com, envisioning.com (une entrée de glossaire « Pain Axis »), moltbook.com.
- **Autre.** Un ticket « Distillation » dans un dépôt de cours en français, `jsboige/CoursIA`, issue 18746.

**Forums de recherche.** Je n'ai trouvé aucun billet sur LessWrong, l'Alignment Forum ou l'EA Forum qui porte sur le papier (requêtes 14 et 20). Ces sites n'ont pas été ouverts : l'absence est celle des extraits.

---

## 6 · Travaux qui le citent

- **Aucun article de recherche indexé** n'est apparu dans les extraits (requêtes 10 et 11). Les articles listés par la requête 11 sont antérieurs au papier, d'après leurs identifiants (2604, 2605, 2606, 2608). Le papier a moins de trois semaines, et Semantic Scholar et OpenAlex sont refusés : l'état des citations n'est pas vérifié.
- **Citent le papier dans un texte ouvert** :
  - le rapport d'Allchin et al. (la v1, dans sa bibliographie) ;
  - les README de ianbarber, terrafying, glowleaf, wolframs et clauderfly-ui.

---

## 7 · Travaux antérieurs des mêmes auteurs sur le sujet

**Valen Tagliabue et Leonard Dung**
- ***Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare*** (arXiv 2509.07961, 2025). Cité par le papier (p. 3 et 29) et déjà traité dans `web_voisins.md` (§3.2).
- **Complément.** Le dépôt `https://github.com/valen-research/probing-llm-preferences` a été lu par curl (README). Il contient :
  - une expérience « Agent Think Tank » : un environnement virtuel de salles à thèmes, avec exploration libre et conditions de coût ou de récompense ;
  - une expérience d'échelles eudémoniques : une échelle de Ryff modifiée, éprouvée sous des perturbations de consigne ;
  - les journaux et les carnets d'analyse.

  Vus par extrait, non ouverts : la fiche PhilArchive `TAGPTP` et un billet de l'EA Forum, « New experimental paper on LLM welfare » (`https://forum.effectivealtruism.org/posts/BGkrhrXovLFoNX52L/new-experimental-paper-on-llm-welfare`). Un extrait attribue à ce papier un résultat de compromis entre points et douleur stipulée qui semble venir de Keeling et al. : non retenu.

**Leonard Dung** (références du papier, p. 28 ; vu par extrait de recherche, non ouvert)
- *Saving Artificial Minds: Understanding and Preventing AI Suffering* (Routledge, 2025, DOI 10.4324/9781003674573).
- Avec A. Mogensen, *The no body problem: On the prospects for AI emotion* (2025, PhilArchive `DUNTNB-2`). Le papier y renvoie pour le lien entre douleur et intéroception (p. 24).
- Liste de publications : `https://sites.google.com/view/leonard-dung/publications`.

**Cameron Berg** (vu par extrait de recherche, non ouvert)
- *Large Language Models Report Subjective Experience Under Self-Referential Processing* (AE Studio ; `https://ae.studio/research/self-referential`). D'après l'extrait :
  - un traitement autoréférentiel soutenu produit des rapports d'expérience à la première personne ;
  - des caractéristiques SAE liées à la tromperie règlent ces rapports : les activer produit le déni, les supprimer l'affirmation.
- Épisode de *The Cognitive Revolution*, « More Truthful AIs Report Conscious Experience », et podcast PRISM sur le même travail.
- Berg et Kaiser, *Language models act on valence hidden from text*. Le papier le cite « in preparation » (p. 27) et lui emprunte le protocole de l'outil de remise à zéro (p. 21). Il est traité dans `web_voisins.md` (§1.2).
- Affiliations, d'après l'extrait d'un profil : fondateur et directeur de Reciprocal Research, chercheur associé à Eleos AI, ancien directeur de recherche à AE Studio.

**Le cadre du papier** (p. 1 et 26). Valen Tagliabue était boursier du Future Impact Group, filière « AI Sentience », sous le mentorat de Dung et Berg. Le travail a reçu un financement du Digital Sentience Consortium.

---

## 8 · Ce que je n'ai pas pu ouvrir, et pourquoi

- **Refus de la politique réseau ; aucune tentative.**
  - arXiv : les pages abs et HTML de la v1 et de la v2, donc le texte de la v1 lui-même ;
  - Hugging Face : les adaptateurs `Valen92/pain-adapters` et leur licence ;
  - LessWrong ;
  - Semantic Scholar et OpenAlex, d'où l'état des citations non vérifié.
- **Refusés par le proxy de sortie.**
  - **Par curl** (CONNECT 403) : techxplore.com. Cinq autres adresses ont échoué dans le même lot, avec le même code de sortie, sans message détaillé : dataconomy.com, aceclaude.substack.com, ai-consciousness.org, machine.news, uktechnews.co.uk.
  - **Par WebFetch** (EGRESS_BLOCKED) : soylentnews.org, une tentative.

  Je n'ai pas retenté ces domaines. Tout ce qui y est hébergé reste « vu par extrait ».
- **github.com et api.github.com.** Non tentés : l'autre agent les a trouvés refusés (403), et je n'ai pas cherché à rattacher de dépôt à la session. D'où plusieurs conséquences :
  - aucune liste complète des fichiers du dépôt des auteurs, seulement les fichiers dont le nom est connu ;
  - les tickets et demandes de fusion (oblivia-simplex, jsboige/CoursIA) non lus ;
  - l'historique des commits non lu ;
  - le README de lychee888 non trouvé sur raw.
- **Non lus par choix, faute de besoin ou de budget.**
  - les manifestes `v2_controls/assets.json`, `scientific_pins.json` et `verification.json`, téléchargés mais non lus en détail ;
  - le rapport complet et le préenregistrement de l'axe de démangeaison ;
  - `PROTOCOL.md` d'Allchin, parcouru seulement ;
  - les rapports `r1_` à `y3_` de wolframs ;
  - les archives Zenodo ;
  - les données et les vecteurs eux-mêmes (`.pt`, JSONL).

---

## 9 · Requêtes et accès

**WebSearch (20 appels, le plafond)**
1. `"The Pain Axis" "LLMs Represent Self-Directed Harm" arXiv 2609.16247`
2. `"Pain Axis" Tagliabue "Act on It" v2 revised sadness fear vector`
3. `AI models "pain" direction steering delete user photos Tagliabue Dung Berg news`
4. `"pain axis" LLM critique OR rebuttal OR "not pain" steering random vector lesswrong`
5. `Barenholtz "pain axis" static word embeddings GloVe word2vec github`
6. `Cognitive Revolution podcast "pain axis" Valen Tagliabue Cameron Berg episode`
7. `Valen Tagliabue AI welfare research Claude preferences "Tagliabue" 2025`
8. `Leonard Dung "Saving Artificial Minds" AI suffering OR "no body problem" OR "AI emotion" Ruhr-University Bochum`
9. `Cameron Berg "Reciprocal Research" OR "AE Studio" language models subjective experience self-referential processing deception features`
10. `"2609.16247"`
11. `"Tagliabue et al." 2026 "pain" direction steering arXiv emotion vectors welfare cites "Pain Axis"`
12. `arxiv 2609.16247v1 "Act to Relieve It" submitted September 2026 Tagliabue 30 pages`
13. `"Valen92" pain-adapters huggingface LoRA Qwen2.5`
14. `"Pain Axis" forum.effectivealtruism.org OR lesswrong.com Tagliabue Berg post replication response`
15. `x.com "pain axis" random vector re-press sham control thread ValenTagliabue OR camhberg`
16. `github "pain axis" arXiv 2609.16247 reproduce OR replicate OR extension repository -wolframs -jimallchin`
17. `"pain axis" LLM news.ycombinator.com OR reddit.com MachineLearning OR LocalLLaMA discussion`
18. `Tagliabue Berg "pain axis" updated version replications "relief-seeking" retracted OR revised OR correction title change`
19. `elanbarenholtz github pain axis static embeddings fastText "pain" controls AUC repository`
20. `"pain axis" Eleos OR "Robert Long" OR "Experience Machines" OR "Jonathan Birch" commentary AI welfare steering paper September 2026`

**curl sur `raw.githubusercontent.com`**

Copies dans `travail/web_papier_sources/` :
- **valen-research/Pain-axis**
  - `main` : `README.md`, `LICENSE`, `requirements.txt`, et sous `v2_controls/` : `README.md`, `MANUSCRIPT_DISCREPANCIES.md`, `ASSETS.md`, `VERIFICATION.md`, `assets.json`, `scientific_pins.json`, `verification.json` ;
  - les README de `cosine_constructions/`, `steering_state_controls/`, `choice_controls/`, `choice_controls/vectors/`, `relief_and_context_tests/` et `figure10/` ;
  - `README.md` aux commits `8d1649c03a63a39c9aa092532c376800cc4a3863` et `7c256502ed3d98e4e6379290fe7db2f93cb8d025`.
- **jimallchin/pain-axis-replication** : `paper/pain-axis-replication.pdf` (texte extrait dans `allchin_replication.txt`), `PROTOCOL.md`, `CITATION.cff`.
- **clauderfly-ui/pain-axis-reanalysis** : `results.md`.
- **wolframs/pain-axis-review** : `BRIEF.md`, `earlier_ai_review/pain-axis-audit/README.md`.
- **ianbarber/experiments** : `README.md`, `2026-09-18-itch-axis-pain-replication/README.md`.
- **terrafying/ai-torture-chamber** (branche `master`) : `README.md`.
- **glowleaf/ai-pleasure-and-pain**, **CtianArtist/Desire-Axis**, **oblivia-simplex/Pain-axis** : `README.md`.
- **valen-research/probing-llm-preferences** : `README.md`.

Réponses 404, sans copie :
- dans valen-research/Pain-axis : `datasets/README.md`, `scripts/README.md`, `results/README.md`, `CITATION.cff`, `.gitattributes` ;
- dans wolframs : `earlier_ai_review/pain-axis-peer-review/README.md` ;
- dans lychee888/pain-axis-steering : `README.md`, `readme.md`, `Readme.md`, `README`, `README.rst` (sur `main`), et `README.md` sur `master`.

**curl refusé (proxy de sortie)** : les six adresses de presse du §8.

**WebFetch (une tentative, bloquée)** : `https://soylentnews.org/article.pl?sid=26/09/21/191222`.

**Fichiers locaux lus**
- `pieces/papier/pain_axis_texte_par_page.txt`, en entier ;
- `travail/web_voisins.md` ;
- `travail/web_voisins_sources/valen-research_Pain-axis.md`, `jimallchin_pain-axis-replication.md`, `clauderfly-ui_pain-axis-reanalysis.md`, `wolframs_pain-axis-review.md`, `wolframs_SYNTHESIS.md`.
