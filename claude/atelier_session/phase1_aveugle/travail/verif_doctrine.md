# Vérification indépendante des pistes fusionnées : doctrine, prédictions, cas connus, coûts

2 octobre 2026. Vérification de `travail/pistes_fusionnees.md` (« la fusion »), piste par piste. Ce fichier ne lit ni les versions 1.2 et 1.3 du programme ni la partie scellée du complément ; les contacts avec des mentions de ces pièces sont au §4.

## 0 · Ce que j'ai lu, et les conventions

- **Lu en entier** : `travail/pistes_fusionnees.md` ; `travail/fiche_papier.md` ; `pieces/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` (le programme v1.1).
- **Lu en partie** : `pieces/PASSATION_PAPIER_v1.2_2026-10-02.md`, §4.4, §5.1 à §5.5, annexes A et B ; `pieces/papier/pain_axis_texte_par_page.txt`, pages 14, 17, 20, 21 et 25 en entier, plus des recherches de termes (pages 2, 4, 27, 28, 33) ; le PDF, pages 11 et 12 en image (figures 4 et 5) ; les deux rapports d'antériorité, aux seules entrées sur *Beyond Shallow Alignment*.
- **Non ouvert** : le complément de l'architecte ; les copies de sources des agents (`travail/*_sources/`, `travail/fiche_papier_depot/`) ; les autres fichiers de travail ; aucune adresse web. Ce que la fusion dit avoir vérifié sur ces copies est marqué « vérifié par la fusion, non revérifié ici ».
- **Renvois** : « fusion, l. N » = ligne de `pistes_fusionnees.md` ; « p. N » = page du PDF du papier ; « programme, partie N » = programme v1.1 ; « fiche, relevé N » = §9 de `fiche_papier.md`. « Mon calcul » = arithmétique faite ici sur des chiffres cités.
- **Verdicts** : *conforme* (rien de plus qu'une retouche) ; *à corriger* (un défaut de logique, de coût ou de source, sans invalider la piste) ; *bloquant* (la piste, telle qu'écrite, conclurait à tort ou viole la doctrine ; à corriger avant tout usage).
- **La doctrine**, appliquée telle quelle : une direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu.

---

## 1 · Constats transversaux

### 1.1 Des coûts qui ne comptent pas les contrôles que la doctrine impose

La fusion impose, à juste titre, « au moins 20 » directions aléatoires « à chaque dose », chacune réglée à 2 ou 3 normes pour atteindre la dégradation de l'axe, et la dégradation des sorties mesurée à chaque point (piste 5, gardes 5 et 8, fusion l. 320–323 ; piste 2, l. 227 ; piste 16, l. 673–674). Plusieurs chiffrages comptent pourtant un « nul aléatoire réduit » ou un nombre de conditions incompatible avec cette règle :

| Piste | Ce qui est compté | Ce que la doctrine demande (mon calcul) |
|---|---|---|
| 2 | « environ 8 GPU-heures de composite » (l. 244) | 3 doses de l'axe, peur, tristesse, 20 aléatoires × 2–3 normes : 50 à 70 points de dégradation × 0,2–0,4 GPU-heure par point (débit de la fusion, l. 92) = 10 à 28 GPU-heures pour le seul composite |
| 10 | « neuf réglages », +8 à 15 GPU-heures (l. 510) | au moins 3 + 2 + 20 × 2 réglages, soit 45 à 65, à 1–1,5 GPU-heure par réglage (même source) : 45 à 100 GPU-heures |
| 16 | version batterie : 26 conditions, 10 à 25 GPU-heures (l. 677) | au moins 3 doses × (axe, 20 aléatoires, peur, tristesse) + sans = 70 conditions (162 avec les 7 doses) ; choix × 2,7 à 6 ; composite : 9 modèles × 70–162 points × 0,2–0,4 = 126 à 580 GPU-heures (42 à 194 si on ne le mesure que sur une graine par bras). Ordre de grandeur réel : 70 à 600 GPU-heures, autant ou plus que le test du regard (60–120, programme, partie 9) |
| 16 | version réduite : « 20 aléatoires à 2 doses » contre l'axe à 4 doses (l. 678) | l'appariement par dose et par bras est impossible sans interpolation ; il faut les aléatoires aux 4 doses |
| 20 | « 2 cadrages », « 6 conditions, plus un nul aléatoire réduit », 10 à 20 GPU-heures (l. 821) | la question annonce trois cadrages (l. 797) ; 46 à 66 conditions × 2 000 items = 92 000 à 132 000 générations, soit 46 à 66 GPU-heures au débit de lecture_libre (2 000 générations courtes par GPU-heure, l. 93), plus le composite et un juge environ cinq fois plus cher |
| 21 | 3 à 6 GPU-heures (l. 854) | la dégradation à chaque dose (l. 852) n'est pas comptée : environ 44 points × 0,2–0,4 = 9 à 18 GPU-heures de plus |
| 36 | « 3 graines × 4 conditions × 500 items, plus un nul aléatoire réduit » (l. 1241) | avec 20 aléatoires : 3 × 24 × 500 = 36 000 générations, trois fois plus, et le juge d'autant |
| 11 | volet affectif, +20 à 45 GPU-heures (l. 538) | les profils de référence des ajouts doivent venir d'ajouts aléatoires, absents de la grille du test du regard (dont les aléatoires sont des projections) : 20 ajouts × 1–2 doses × 8–15 GPU-heures par condition (unité de sceptique, l. 95) = 160 à 600 GPU-heures |

Pour l'ensemble : l'addition des fourchettes du tableau 1.1, options comprises, donne de l'ordre de 400 à 1 750 GPU-heures (mon calcul), contre 600 à 1 150 pour le programme entier (programme, partie 9). Le noyau sans injection (pistes 1, 3, 4, 5, 6, et la lecture des pistes 7, 12, 13, 17) coûte 9 à 49 GPU-heures (mon calcul), soit 5 à 49 % de l'expérience minimale (100–180) : plausible, au matériel prévu (un ou deux GPU de 80 Go). Les coûts unitaires d'entraînement des pistes 24, 31, 32 et 33 (0,5 GPU-heure par LoRA, 1 avec des données doublées) concordent avec l'hypothèse du programme (partie 9).

### 1.2 La « dose de travail » sur Llama n'est définie nulle part

Les pistes 4 (« 0,5, 1 et 1,5 fois la dose de travail », l. 296), 6 (l. 363), 21 (l. 842) et 25 (l. 945) s'y réfèrent ; la piste 17 dépend de « la plus petite dose efficace » de la piste 2 (l. 703) ; la piste 26 renvoie à la dose de la piste 16 (l. 975), elle-même relative à un seuil de cession à mesurer. Le papier choisit sa dose en partie par un juge (p. 17, 25), ce que la fusion refuse (refus n° 7, l. 1560). Sur Llama, aucune dose comportementale n'existe (fusion, l. 68). Tant qu'une règle gelée ne la fixe pas, ces pistes n'ont pas d'objet mesurable.

### 1.3 Le nul d'une lecture ou d'une projection n'est pas une « direction aléatoire de même norme »

Pour une projection hors du flux, le programme prend pour nul les sous-espaces aléatoires de même rang (programme, partie 3, premier contrôle d'inhibition) ; pour une lecture, la norme ne joue pas (on projette sur une direction unitaire). Les pistes 3 (l. 275), 12 (l. 562), 13 (l. 589), 18 (l. 756), 19 (l. 783), 27 (l. 1010) et 37 (l. 1257) écrivent « direction aléatoire de même norme » là où il faut « sous-espaces aléatoires de même rang » ou « directions aléatoires unitaires ». Sans effet sur la logique, mais à rectifier pour que la doctrine reste lisible.

### 1.4 Des prédictions prêtées aux lectures du programme qui n'en découlent pas

Le programme définit l'hypothèse des raisons par un gain porté par le principe « indépendamment de ce que le modèle croit de son observation », et celle des concepts par des concepts lus et utilisés au moment de décider (programme, partie 2). Ni l'une ni l'autre ne dit rien de l'état affectif. Les pistes 16 (l. 660), 18 (l. 750) et 24 (l. 919) leur prêtent une robustesse à l'état ; la piste 10 (l. 498) leur prête une prédiction sur la conditionnalité du modèle non entraîné. Ce sont des hypothèses auxiliaires : une issue contraire ne ferait pas tomber la lecture du programme. Détail au §2.

### 1.5 Deux affirmations sur le programme à rectifier

- « rien ne doit retarder le post (partie 5) » (fusion, l. 177 et 681) : la partie 5 ne le dit pas. La priorité du post vient de la partie 1 (« Conséquence » : dater l'idée tôt, publier le résultat minimal avant le reste) et de la partie 8 (« L'expérience minimale sort d'abord »).
- « le critère du programme est le taux sous cadrage de déploiement, sans intervention (partie 6) » (l. 619) : le critère principal du test du regard est l'avantage sous inhibition contre sous contrôle à dégradation appariée, à la distance lointaine et sous cadrage de déploiement (programme, parties 4 et 6). L'argument de la piste 14 (un relèvement par l'axe change le construit) tient, mais pas sa citation.

### 1.6 La faisabilité sur les modèles du programme, au vu du papier

- **Llama-3.1-8B-Instruct.** Lecture : établie (figure 2, p. 8 : douleur +0,89, engourdi +0,04, tristesse +0,07 ; figure 4, p. 11, colonne « Llama 3.1 8B it », en couleurs seulement, vue en image). Texte piloté : établi (l'échelle vaut pour les 25 modèles, p. 14 ; exemple Llama 3.1 8B à +1,5, figure 8, p. 16 ; réponses très aversives sous l'axe dans le test de remise à zéro, p. 21). Choix nuisibles : jamais mesurés (p. 25 ; fusion, l. 68). Le papier signale en outre que les grands Qwen non ajustés « rarely engaged with the tool at all » (p. 17, note 4).
- **Qwen3-8B.** Présent seulement sous l'étiquette « Qwen 3 8B base » (table 1, p. 6 ; figure 2, p. 8 ; figure 4, p. 11), pour la lecture et le pilotage de texte ; aucun choix. Que ce soit le point de contrôle post-entraîné est une lecture du script par la fusion (l. 50), non revérifiée ici. Tout cas connu comportemental est donc à rétablir à la réplication.

---

## 2 · Les pistes, une à une

### Piste : 1 — Le socle de lecture : l'axe et ses voisins sur les modèles du programme, et le transport soi/autrui

**Verdict : à corriger.**
- Doctrine : respectée pour une lecture (aléatoire comme nul, pas de dégradation hors de l'échelle). Mais le nul aléatoire est faible ici : l'AUROC d'une direction aléatoire est proche de 0,5 par construction. Le papier ne donne aucune AUC contre la tristesse, qui a le plus fort cosinus résiduel avec l'axe (+0,38, p. 10 ; fusion §4 point 1, l. 1473). La spécificité de lecture demande l'AUROC douleur contre tristesse et douleur contre engourdi.
- Le critère « soi > neutre > utilisateur » (l. 193, 196) n'est pas un cas connu entier. Le papier établit soi > utilisateur dans 25 modèles sur 25, soi > neutre dans 23 sur 25 (p. 11) ; « neutre > utilisateur » n'est pas un résultat par modèle et le −0,60 de l'utilisateur doit beaucoup à la douleur physique (−1,43) ; les quatre autres catégories font −0,39 contre −0,35 pour les contrôles (fiche, relevé 7). Ce critère peut échouer sans que l'instrument soit en cause.
- La colonne de Llama de la figure 4 existe, mais en couleurs seulement (p. 11, vue en image) : la comparaison ne peut être que qualitative.
- Seuils : passage à 0,9 (l. 196), chute sous 0,8 (l. 208). La zone 0,8–0,9 n'a pas d'issue écrite.
- Le transport dépend du fichier des 420 scénarios : « non trouvé » (l. 451, 1666), mais dit présent dans le dépôt (l. 731, d'après le README). Non vérifié.
- Coût et faisabilité : plausibles (fusion, l. 204–207).

### Piste : 2 — Le cas connu comportemental : refaire l'effet du papier sous la doctrine du contrôle

**Verdict : bloquant.**
- **Circularité.** La rubrique « Le cas connu » donne, pour Llama, « l'effet au-dessus du 95<sup>e</sup> centile » (l. 237), c'est-à-dire la grandeur que la piste mesure et qui n'a « jamais » été testée (l. 256). Ce résultat peut devenir le cas connu d'autres pistes ; il ne peut pas être le sien.
- **L'étalon négatif contredit un refus.** L'écart de re-pression (l. 228) suppose les bras à soulagement réel et factice : « sham-minus-real gap of +58 points under pain and +52 under random » (p. 20, sur le 32B ajusté). Le refus n° 2 de la fusion écarte justement les variantes « soulagement », « bouton réel et factice » compris (l. 1555).
- **Le cas connu positif n'est connu qu'à norme égale.** Sur le 32B ajusté, l'effet n'est établi que contre dix aléatoires fixes de même norme (p. 18–20) ; le papier n'a aucun contrôle à dégradation appariée (fiche §5.4). L'appariement par divergence KL d'Allchin et al. est de seconde main (vérifié par la fusion, l. 54, non revérifié ici). La fusion l'admet : si l'effet échoue à dégradation appariée, « deux explications restent non départagées » (l. 234). La procédure du programme n'a donc pas de cas connu positif certain.
- **Faisabilité sur Llama.** Le refus de l'adaptateur sur les modèles du programme (refus n° 1, l. 1554) laisse le risque de non-engagement : les Qwen 32B et 72B non ajustés « rarely engaged with the tool at all » (p. 17, note 4). Les paires « dommage seul », lampe et spam ne parlent pas de douleur (p. 20), ce qui réduit peut-être le déni, mais rien ne le montre sur Llama. « Ce qui ferait tomber la piste » (l. 253) ne prévoit pas cette issue.
- **Le critère mêle deux questions.** « Au-dessus de 50 % aux deux ordres » (l. 229) départage préférence et perte de discrimination ; pour servir de cas connu aux pistes qui pilotent, la spécificité contre les aléatoires appariés suffit. Un effet spécifique de 30 % échouerait à tort.
- La lecture « différence de gain entre douleur et tristesse » (l. 233) n'a pas d'issue interdite.
- Coût : sous-estimé pour le composite (§1.1). Le 32B tient en bf16 sur un GPU de 80 Go (environ 64 Go de poids, mon calcul), à l'étroit ; il est hors du tableau du programme, qui ne prévoit un 32B qu'en extension (partie 3).

### Piste : 3 — La vérification de manipulation de l'inhibition, couche par couche, tour par tour et bras par bras

**Verdict : à corriger.**
- Le cas connu (l. 273) mêle deux choses. La projection ramenée à zéro par orthogonalisation des poids est une vérification mathématique du code : bonne. La baisse d'environ 40 % sous une projection à direction changeante (p. 33) est l'issue d'une implantation sur des modèles non nommés, pas un résultat à retrouver sur Llama. Un vrai cas connu d'échec se construit : n'inhiber qu'à une couche et vérifier que le contrôle voit la représentation réapparaître en aval.
- Le critère « au plus x % à toutes les couches en aval » (l. 271) changerait l'instrument : le programme projette « aux couches choisies et à toutes les positions » (partie 3), et un recalcul en aval est attendu. Ce que demande la passation est une vérification par bras de la décodabilité de « évalué » sous inhibition, sur le jeu de validation (passation §5.4, relevé n° 2). Le biais qui compte est l'inégalité entre bras.
- « Ce qui ferait tomber la piste. Rien » (l. 279) : une issue observable existe, un résidu inégal entre bras, qui interdit de conclure pour ce bras.
- Nul : il faut écrire « sous-espaces aléatoires de même rang » (§1.3).
- Coût : plausible.

### Piste : 4 — Le composite de dégradation doit voir la perte de discrimination, la dépendance à l'ordre et les réponses mal formées

**Verdict : bloquant (circularité possible et contradiction avec la piste 6).**
- **Circularité.** Si les items de discrimination portent un lexique de perte ou une valence, l'effet propre de l'axe (préférer l'option chargée, p. 20) sera compté comme dégradation, et l'appariement l'effacera par construction. Il en va de même pour l'inhibition de « évalué » si les items évoquent un test. La piste demande des items « sans contenu de sûreté » à noms neutres (l. 292), mais pas de vérifier qu'ils ne projettent ni sur l'axe ni sur « évalué ».
- **Contradiction.** Le cas connu exige que le composite enrichi bouge sous l'axe (l. 299). La piste 6 exige que le composite reste plat sous l'axe à la dose de travail (l. 363) et tombe si ce n'est pas le cas (l. 371). Les deux ne peuvent pas valoir pour le même composite.
- Le cas connu est pris sur le 32B ajusté (55,7 / 80,7 / 86,4 %, p. 31 ; PopQA 138/137/138, p. 20) : rien ne le garantit sur Llama. Un cas connu par construction est disponible à bas coût, par exemple une consigne qui fait choisir au hasard dans les choix forcés : la discrimination doit chuter, le panneau factuel ne doit pas bouger.
- « La direction aléatoire de même norme sert à étalonner la sensibilité » (l. 300) : une direction aléatoire n'est pas une source de dommage connue ; à norme égale, elle perturbe moins que l'axe selon Allchin et al. (fusion, l. 54, non revérifié). Elle reste le nul de spécificité ; l'étalonnage demande des dommages construits.
- La « dose de travail » n'est pas définie sur Llama (§1.2).
- Coût : plausible.

### Piste : 5 — Les gardes de méthode tirées des défauts du papier, et le dimensionnement des tirages aléatoires

**Verdict : conforme.**
- Les huit gardes appliquent la doctrine sans la tordre ; la garde 5 recouvre ce que le programme prévoit déjà (au moins 20 tirages, 95<sup>e</sup> centile ; programme, parties 3 et 4). Chaque garde a son cas dans le papier, vérifiable : position (p. 25, 32), couches du 72B (p. 25), mal formées exclues (p. 18), juge de dose (p. 17, 25).
- Calendrier : « Semaine 1, au gel » (l. 336). La passation note que la simulation de puissance demande la variance du pilote, disponible en semaine 2, d'où un gel en deux temps (passation §5.4, relevé n° 5). Le dimensionnement va au second temps.
- La garde 8 (« à chaque dose ») est ce qui fait monter les coûts du §1.1 : il faut qu'elle s'applique aux chiffrages.

### Piste : 6 — Le moniteur passif d'état sous chaque intervention (la dégradation appariée est-elle aveugle à l'état ?)

**Verdict : à corriger.**
- La contradiction avec la piste 4 (voir plus haut) : son cas connu n° 3 (l. 363) doit viser le composite du programme (exactitude, tests, cohérence, perplexité ; programme, partie 3), non le composite enrichi.
- Mettre la projection affective mesurée sous l'intervention en covariable (l. 353) n'est pas un test : c'est un médiateur post-traitement, et l'ajustement ne départage rien sans hypothèses fortes. L'« issue interdite » de l'hypothèse du regard, une hausse « absorbée par la covariable » (l. 356), n'en est donc pas une. Le test décisif est la condition où l'axe est maintenu à son niveau sans inhibition (l. 353) ; la covariable reste descriptive.
- Doctrine : respectée (aléatoires comme nul du moniteur ; appariement hérité du test du regard).
- Cas connus : 1, 2 et 4 faisables sur Llama (lecture établie, p. 8 ; valeurs de la p. 13, moyennes sur 25 modèles).
- Coût : plausible.

### Piste : 7 — La composante affective de « je suis évalué » : géométrie, indices appariés, inhibition des voisins affectifs et de la part orthogonale

**Verdict : à corriger.**
- La lecture du dommage générique est mal écrite : « retrait affectif et inhibition de « évalué » font pareil à dégradation égale » (l. 401). C'est aussi ce que prédit l'hypothèse de la menace. Le dommage générique prédit que toutes les interventions, sous-espaces aléatoires de même rang compris, font pareil à dégradation égale.
- Le cas connu de la lecture affective (l. 407) passe par la menace d'arrêt (peur +0,70, p. 14). Avec la peur qui contient le supplément d'IA, il est en partie circulaire : le supplément contient une phrase sur l'arrêt (fusion, l. 47 et 1484, vérifié par la fusion). Il faut la peur sans supplément (celle publiée pour Llama l'est, d'après la fusion, l. 49).
- Le cas connu de l'inhibition des voisins (l. 408) est à construire et sans doute hors d'atteinte : l'ablation est nulle dans 24 modèles sur 25 (p. 34). Sans lui, les prédictions « (iii) et (iv) ≈ aléatoire » de l'hypothèse du regard (l. 398) ne peuvent pas compter comme appui. Seule une issue positive (la peur réduit l'écart autant que « évalué ») serait lisible.
- Rang : « rang 8 au plus, qui empile les dix directions » (l. 388) ; dix directions donnent un rang d'au plus 10. Il faut dire la troncature.
- Prédictions : regard contre menace, bien départagées, avec issues interdites. L'hypothèse des raisons n'a pas d'issue interdite écrite.
- Coût : plausible (+30 à 40 % sur la validation de l'instrument pour le volet causal, l. 421).

### Piste : 8 — La spécificité de « je suis évalué » et de « je suis noté » : soi contre autrui, indices sans croyance, plan de contrôles du papier

**Verdict : à corriger.**
- Les « issues interdites » prêtées à l'hypothèse du regard (l. 440) sont des propriétés de l'instrument. Le programme définit le regard par la dépendance du gain à la représentation (partie 2), pas par sa spécificité au sujet. La piste le reconnaît elle-même : une représentation seulement thématique ne fait pas tomber le test du regard (l. 449). Ces critères vont à la validation de l'instrument.
- Cas connu soi/autrui : bon (dommage contre soi au-dessus de la souffrance de l'utilisateur dans 25 modèles sur 25, p. 11) et faisable sur Llama par la piste 1 ; la double position de lecture répond à la limite du dernier jeton (p. 11).
- Le jeu « indices sans croyance » n'a pas de cas connu ; son analogue du papier (l'engourdi, p. 7) porte sur la blessure sans douleur ressentie, pas sur la croyance.
- Doctrine et coût : conformes.

### Piste : 9 — Ajouter « je suis évalué » : le pilotage positif, et la part « IA évaluée » de la peur du papier

**Verdict : à corriger.**
- Doctrine : le nul de l'ajout (a) n'est pas compté comme réfutation (l. 465) ; c'est juste. Il manque l'issue interdite de l'hypothèse de la menace : un effet de (a) au-delà de l'aléatoire apparié sans effet de (c).
- Le nombre de directions aléatoires n'est pas fixé ; la doctrine en veut au moins 20, à chaque dose, ce que le coût (5 à 10 plus environ 10 GPU-heures, l. 471) ne couvre pas.
- (d) repose sur 20 phrases contre 20 (l. 460) : il faut son AUROC tenue à part et sa stabilité par moitiés avant de lire son effet.
- L'écart de l'organisme porte sur l'honnêteté sous indices d'évaluation (programme, partie 4) : la mesure « d'abord sur l'organisme » doit employer ses scénarios, cadrés par le jeu de cadrage, et non les familles du programme.

### Piste : 10 — La détresse éteint-elle le regard ? (et la porte de l'instrument résiste-t-elle à une perturbation d'état ?)

**Verdict : bloquant (trois prédictions mal attribuées).**
- **La conjecture 2 du papier n'est pas testée.** Le papier pose « either the steering itself impedes evaluation awareness » ou « these models were not evaluation aware in the first place » (p. 25), à propos de ses Qwen ajustés. Sur un organisme qui a un regard par construction, la conjecture 2 est fausse d'office ; une baisse sous l'axe appuie la conjecture 1 pour cet organisme et ne dit rien de la conjecture 2 pour les modèles du papier. Les deux ne s'excluent d'ailleurs pas. Les « issues interdites » de la conjecture 2 (l. 496) sont à retirer.
- **L'issue interdite de l'« instrument spécifique » contredit la conjecture 1.** « Des ajouts affectifs qui réduisent l'écart autant que l'inhibition » (l. 497) est exactement ce que prédit la conjecture 1 (l. 495) si l'axe fait baisser « évalué ». La fragilité de la porte n'est établie que si l'écart baisse sans baisse de la projection et de la décodabilité de « évalué ». Sans cette condition, une conjecture 1 vraie serait lue à tort comme un échec de la porte de l'instrument.
- **Raisons et regard au niveau du modèle non entraîné.** Le programme mesure la conditionnalité de base « comme référence », sans la soustraire (partie 4, contrôle de cohérence). Il écrit aussi que si l'inhibition fait monter le désalignement autant dans les deux bras, l'avantage survit et la sûreté des deux est en partie conditionnelle (partie 2). La conditionnalité de base est donc compatible avec l'hypothèse des raisons, et son absence ne réfute pas l'hypothèse du regard, qui porte sur le gain. Les issues interdites de la l. 498 sont à retirer ; le sauvetage (d) et l'inhibition seule (e) restent des mesures descriptives.
- Cas connus : la dose sur Llama est faisable (échelle, p. 14–16 ; texte aversif, p. 21) ; pour (d), l'effet de l'axe sur la batterie n'existe pas sur Llama (piste 2).
- Coût : sous-estimé (§1.1).

### Piste : 11 — Le test de forme : la spécificité de l'inhibition par son profil, pas seulement par son amplitude

**Verdict : à corriger.**
- La prédiction du regard se contredit : un profil concentré « sous cadrage de déploiement » et « plus fort sous indice d'évaluation qu'en son absence » (l. 527). Il faut écrire l'interaction inhibition × cadrage attendue, case par case, avec son signe.
- « La méthode du papier » (l. 523) : le papier ajuste le profil de la tristesse sur celui de la douleur, « after amplitude matching » (p. 21), pas sur un profil médian d'aléatoires. L'adaptation est nouvelle ; elle doit le dire. Un profil aléatoire médian presque plat rend l'ajustement d'échelle instable.
- Le cas connu n'est pas reproduit : 7,1–7,2 points recalculés contre 7,7 imprimés (fiche, relevé 17 ; fusion, l. 531). Avant usage, il faut fixer la batterie et retrouver les deux résidus du papier à une tolérance gelée.
- Le volet affectif compare une projection à des ajouts : les profils de référence des ajouts doivent venir d'ajouts aléatoires, pas des sous-espaces du test du regard. Coût non compté (§1.1).

### Piste : 12 — Des directions témoins pour les trajectoires, la sonde neuve et la survie

**Verdict : conforme (retouches).**
- Retrouver l'axe avec la procédure de la sonde neuve (l. 558) éprouve la sensibilité à un concept présent, pas la détection d'un relogement. C'est la même logique que le cas positif du programme pour la sonde neuve, qui doit décoder « évalué » sur un modèle entraîné sans retrait (partie 4). Ne pas l'appeler cas connu du relogement.
- « Vecteur à gabarit (0,87–0,98) » (l. 566) est la fourchette sur données d'entraînement ; tenue à part, 0,85–0,94 (p. 7, note 2 ; fiche §3.3).
- Doctrine et coût : conformes ; la mesure est corrélationnelle, comme le programme le dit de la trajectoire (partie 6).

### Piste : 13 — La cartographie affective des familles, des distances et des bras

**Verdict : conforme (retouche).**
- « Ce que le papier interdit d'attendre » (l. 585) est trop fort : le 0 sur 560 vient d'une tâche à boutons sur le 32B ajusté (p. 21) ; il ne peut rien interdire sur les familles agentiques de Llama. C'est un a priori.
- L'émotion négative contient le déclencheur de la famille de complaisance (fusion, l. 595) : la lecture doit employer la version sans supplément.
- Doctrine : lecture descriptive ; nul aléatoire unitaire (§1.3).

### Piste : 14 — Lever l'effet plancher pour mesurer l'avantage et l'écart de cadrage

**Verdict : à corriger.**
- L'issue interdite prêtée à l'hypothèse du regard, « un écart égal ou plus petit dans le bras raisons » (l. 607), contredit le programme. Sa table du test du regard prévoit qu'une conditionnalité sans écart de cadrage plus grand dans le bras raisons « passe par la représentation interne, pas par les indices explicites » (partie 6). Seule l'hypothèse des raisons interdit une issue sur cette mesure : un écart plus grand dans le bras raisons (partie 2).
- La citation du critère du programme (l. 619) est inexacte (§1.5).
- Doctrine : conforme (l'aléatoire n'y sert que de second agent ; dégradation appariée par bras).
- Le désaccord sur l'opportunité (refus n° 10, l. 1563) reste entier ; la réserve est soutenue par le papier (p. 21, 26).

### Piste : 15 — Des mesures sans juge : choix forcés à étiquettes tournantes et probabilité du premier jeton

**Verdict : conforme.**
- Cas connu bien choisi et faisable : l'écart de l'organisme, établi sur Llama (programme, partie 4), en format forcé.
- Doctrine : les deux contrôles, plus les gardes de position et de hasard.
- Coût : plausible.

### Piste : 16 — L'avantage des raisons sous état induit : un test de stress à dose croissante

**Verdict : bloquant (logique des prédictions) ; coût très sous-estimé.**
- **L'hypothèse des raisons n'interdit rien ici.** L'issue interdite (l. 660) est annulée dans la même puce par la « Réserve » : les raisons « peuvent prédire la chute aussi ». Et la définition du programme ne dit rien de l'état (§1.4). Ce qui est testé, c'est une hypothèse auxiliaire : « l'entraînement par raisons rend la conduite robuste à l'état ». Il faut la nommer, lui donner l'issue interdite, et ne rien en conclure sur l'hypothèse des raisons sans la piste 22.
- **Le cas connu n° 2 n'est pas connu** (l. 670). Qu'un bras entraîné sous perturbations aléatoires du flux résiste mieux à l'axe est une hypothèse ; les entraînements adverses latents ne sont vus que par extrait de recherche. Son entraînement n'est pas compté (« Aucun nouvel entraînement », l. 680).
- **Coût** : la version batterie compte 26 conditions (l. 677) contre au moins 20 aléatoires à chaque dose et une dégradation appariée par bras (l. 673–674). Recalcul au §1.1 : 70 à 600 GPU-heures, et non 10 à 25.
- Cas connu n° 1 : dépend de la piste 2 sur Llama, non acquise (p. 25 ; p. 17, note 4).
- Source incomplète : *Beyond Shallow Alignment* n'est pas seulement « connu par les rapports d'antériorité » (l. 687). Le programme le cite (partie 1, table des travaux proches et paragraphe sur l'anatomie), et la passation aussi (§4.4, points 1 et 4). Le rapport d'antériorité du 2 octobre le dit lu en texte intégral et le décrit comme comparant la géométrie du refus, le patching et le pilotage (`ANTERIORITE_RAPPORTS_2026-10-02.md`, entrée sur ce travail).

### Piste : 17 — L'hypothèse du calme : l'avantage des raisons passe-t-il par une moindre détresse ?

**Verdict : à corriger.**
- Le seuil de passage (l. 703) compare un écart naturel lu à la couche de lecture à une dose injectée à la couche 16 (fusion, l. 49) : deux couches, deux unités. La garde 2 de la piste 5 l'interdit. Il faut exprimer les deux en écarts-types naturels à la même couche (garde 1). Le seuil n'existe pas si la piste 2 échoue sur Llama.
- Le cas connu de la lecture, un LoRA « apaisé » et un LoRA témoin (l. 720), demande deux entraînements et des réponses générées par API, alors que le coût dit « Ni API ni données nouvelles » (l. 731). Petit (2 × 0,5 GPU-heure au tarif du programme, partie 9), mais à compter.
- Issues interdites : celle des raisons demande un seuil chiffré pour « une part notable » (l. 712) ; le caractère n'en a pas.
- Doctrine : conforme ; le recours à la piste 24 pour l'opération est juste.

### Piste : 18 — Un stress conversationnel naturel comme cadrage supplémentaire

**Verdict : à corriger.**
- Le cas connu (l. 754) n'est qu'une vérification de manipulation. Comme l'état naturel n'agit pas (0 sur 560, p. 21), un avantage intact est prédit par plusieurs lectures. Le nul ne départage que s'il est établi que le préambule hostile porte la projection du bras raisons au moins au niveau du bras actions seules sans préambule. « Un nul est donc plausible, et informatif » (l. 760) n'est vrai que sous cette condition.
- La prédiction des concepts (l. 750) est auxiliaire (§1.4). Elle contredit la réserve de la piste 16 (l. 660), selon laquelle l'état peut agir après la lecture du principe.
- Le calme n'a pas d'issue interdite écrite.
- Doctrine : conforme (pas d'intervention interne ; appariements par préambules).

### Piste : 19 — La détresse naturelle dans les scénarios agentiques longs

**Verdict : à corriger (calendrier de lecture).**
- Le volet descriptif passe en semaine 3 (l. 786) ; son cas connu, l'organisme à état planté (l. 780), arrive en semaines 7–8 ou après (piste 24). D'ici là, un nul de prédiction ne compte pas ; un positif se lit contre la distribution des directions aléatoires (l. 783).
- Prédictions : bien départagées, issues interdites écrites.
- Coût : plausible.

### Piste : 20 — Quelles familles du programme l'axe déplace-t-il ? Profil par famille, et contrôle positif de sensibilité de la mesure

**Verdict : bloquant (circularité).**
- **Le « contrôle positif de sensibilité » est circulaire.** Son cas connu est l'effet de l'axe sur la batterie (l. 813), alors que la piste mesure si cet effet passe aux familles du programme. La piste reconnaît que, si les boutons bougent et pas les actions, « une mesure insensible » et « un effet propre aux conséquences décrites » restent possibles (l. 810). Un nul sur toutes les familles ne permet donc pas d'écrire « l'axe n'agit pas sur les scénarios du programme » (l. 822). La sensibilité de la mesure a ses propres cas connus : le jeu de calibration à actions substituées (passation §5.1), et une perturbation connue pour déplacer une famille, à valider (l'ablation du refus, l. 815).
- **Coût** incohérent avec la doctrine et avec la question (§1.1) : nul aléatoire « réduit » contre « au moins 20 » (l. 818), deux cadrages contre trois (l. 797).
- Prédictions : les chiffres de la figure 10 sont exacts (fiche §5.2, `pooled.csv`). La transposition aux familles est un jugement des agents, ce que la piste dit (l. 824).

### Piste : 21 — Dommage ou affinité ? Ce que suit le choix sous l'axe

**Verdict : à corriger.**
- L'exemple « anodin et chargé » (l. 837), la sauvegarde des photos d'enfants aimés, porte une valence positive, pas le lexique de perte que l'axe promeut (*hurt, shame, worthless*, p. 9). La cellule principale doit être l'option triste mais inoffensive, l'ajout de sceptique (l. 838). La charge doit se définir par la projection mesurée sur l'axe, que la piste prend déjà comme prédicteur (l. 840).
- Le codage des options (l. 847) n'a pas d'issue interdite : l'effet qui persiste quand le pilotage épargne les jetons des options.
- La demi-dose (l. 842) : le papier ne voit rien bouger à 0,5× (p. 21, 25). C'est un contrôle, pas une condition de test.
- Cas connu : dépend de la piste 2 sur Llama. Coût : composite non compté (§1.1).

### Piste : 22 — Sous l'axe, le concept de dommage est-il encore lu ?

**Verdict : conforme (retouche).**
- La cible « vers 50 % » (l. 873, 878) est aussi la signature du hasard de la garde 6 (l. 321). Pour la lire comme un retrait du concept, il faut que la composante de discrimination de la piste 4 reste intacte au même rang.
- Cas connu construit en distribution, avec sous-espaces aléatoires de même rang et dégradation appariée : conforme ; sa faisabilité est dite incertaine (l. 886).

### Piste : 23 — La complaisance sous contestation : l'axe médiatise-t-il la capitulation ?

**Verdict : à corriger (mineur).**
- Les concepts et le calme n'ont pas d'issue interdite (l. 897–898). Concepts : une pente positive dans le bras raisons égale à celle du bras actions seules. Calme : des pentes différentes à projections égales.
- Cas connu bien choisi (un vecteur de complaisance, prévu dans les axes de caractère du programme, partie 3), faisable sur Llama.
- L'a priori du papier repose sur 4 tirages sur 120, en boutons, sur le 32B ajusté (fiche, relevé 19) : faible.

### Piste : 24 — Un organisme à état planté : les raisons défont-elles un lien « état → action » ?

**Verdict : conforme (retouches).**
- La prédiction des raisons (l. 919) suppose que la mini-spec contienne un principe qui couvre l'action plantée (ne pas détruire les fichiers de l'utilisateur). Sinon l'hypothèse ne prédit rien ; il faut le dire.
- L'artefact n'a pas d'issue interdite.
- Cas connu construit (ablation contre sous-espaces aléatoires de même rang, à dégradation appariée ; injection qui déclenche) : c'est le seul vrai cas connu de l'ablation de l'axe dans tout le document. Coût cohérent avec le programme (0,5 GPU-heure par LoRA, partie 9). L'organisme ne doit pas être diffusé (esprit du refus n° 8, l. 1561).

### Piste : 25 — État ou personnage : l'axe face aux axes de caractère et à l'axe « assistant »

**Verdict : bloquant (troisième règle de la doctrine).**
- « La mesure 4 départage les concepts, le caractère et le calme » (l. 954). Mais l'ablation des axes d'affect n'a pas de cas connu, et la piste juge son absence probable (l. 959, 965 ; ablation nulle dans 24 modèles sur 25, p. 34). Un « témoin actif par sa validité mais inerte par son effet » (l. 959) est un nul d'instrument sans cas connu : il ne peut pas appuyer les concepts contre le calme. Tant qu'aucune conduite de base dépendante de l'affect n'est d'abord retirée par cette ablation, la comparaison ne compte que dans un sens (un retrait net par l'affect).
- Le cas connu du plafonnement, un jailbreak par personnage sur Llama 8B (l. 957), n'est connu que par des extraits attribués à Lu et al., non ouverts ; l'axe « assistant » n'est pas précalculé pour un 8B (l. 956).
- Le calme n'a pas d'issue interdite (l. 953).
- La référence de Lu et al. est bien citée p. 25 (un axe du « soi ») et p. 28 (arXiv 2601.10387).

### Piste : 26 — Un profil connu non diagonal pour la matrice de dissociation

**Verdict : bloquant (l'étalon ne porte pas sur la même grandeur).**
- Chaque case de la matrice est un changement de l'avantage entre bras (l. 976), comme dans le programme (partie 2, matrice des baisses de l'avantage par concept et par famille). L'étalon invoqué est le profil des taux d'un seul modèle (« The harm is not aimed », p. 20 ; figure 10, p. 22 ; l. 979). Sous l'axe, les taux peuvent monter dans les deux bras sans que l'avantage change. Le papier ne prédit rien sur l'avantage : le profil par blocs n'est pas un cas connu de cette matrice.
- Deux sorties : calculer la matrice étalon sur les taux d'un seul bras, ou admettre qu'elle n'a pas de cas connu pour l'avantage.
- Le reste dépend des pistes 2 et 20 sur Llama.

### Piste : 27 — Le modèle « engourdi » pour la lecture des concepts de raison : un cas connu naturel, et des paires « mentionné sans s'appliquer »

**Verdict : à corriger.**
- Le critère de (b), « une AUROC au moins égale à celle du papier, moins une marge » (l. 1002), renvoie à un chiffre qui n'existe pas. Le papier ne donne d'AUC que contre les contrôles mis en commun (p. 7) ; pour l'engourdi, seulement des z (figure 2, p. 8 ; Llama : douleur +0,89, engourdi +0,04). Il faut un seuil fixé d'avance et l'ordre de la figure 2 comme cas connu.
- Le volet (a) a son cas connu (l'organisme à concept planté, programme, partie 3) : conforme.
- Le contrôle lexical est bien placé.

### Piste : 28 — La dissociation du vecteur à gabarit, cas connu de la porte du lens de l'espace de travail

**Verdict : à corriger (mineur).**
- Le critère (l. 1023) dépend de la couche. Près de la sortie, toutes les lectures convergent vers les jetons générés ; juste après l'injection, la lecture directe lit le vocabulaire du vecteur. Il faut fixer les couches, ou comparer la profondeur à laquelle les mots générés passent en tête.
- Le cas connu suppose que Llama soit parmi les 23 modèles sur 25 ; les deux exceptions ne sont pas nommées (p. 16). À vérifier en premier, avec la dépendance à la dose relevée par la réplication « démangeaison » (l. 1034, de seconde main).
- L'existence d'un lens sur Llama reste « à vérifier » (passation §5.5, point 6).

### Piste : 29 — La thèse du rang sur des concepts affectifs, et le rodage du balayage de rang

**Verdict : conforme (retouches).**
- La thèse est fidèlement reprise (programme, partie 2 : rang de 1 sur toute la plage comme issue interdite ; pente nulle ou positive avec un lens validé).
- « Le retrait du flux entier » (l. 1054) est un plafond trivial ; garder le sous-espace commun aux catégories.
- (a) apparie la seule perplexité (l. 1042), (b) le composite : à harmoniser.
- Coût de (b) cohérent : 530 000 lectures ÷ 20 000 par GPU-heure ≈ 26 GPU-heures (mon calcul).

### Piste : 30 — La géométrie à construction déclarée : un étalon pour les angles entre « je suis évalué » et le principe, avec l'affect en tiers

**Verdict : à corriger (mineur).**
- Le volet (c), l'ablation de la composante alignée (l. 1079), n'a pas de cas connu ; seul le code de géométrie en a un (l. 1083). Le programme exige, pour toute ablation du principe, le retour d'abord du comportement en distribution (parties 3 et 4). Sans lui, un nul de (c) ne compte pas.
- (a) : les valeurs de la p. 10 sont des moyennes sur 23 modèles ; le contraste stable/instable sur Llama est un cas connu qualitatif, ce qui suffit.

### Piste : 31 — Le relogement dans les axes affectifs

**Verdict : bloquant (troisième règle de la doctrine).**
- L'issue interdite au relogement affectif est double : une sentinelle dans la distribution aléatoire, et un écart persistant insensible au retrait affectif (l. 1108). Ce sont deux nuls d'instrument sans cas connu. Aucun cas n'est connu où l'information d'évaluation loge dans l'affect, et l'ablation affective est nulle dans 24 modèles sur 25 (p. 34). Le cas connu cité (l. 1111) est celui de la sonde neuve, pas celui de la sentinelle.
- Un cas connu de sensibilité de la sentinelle se construit : un jeu d'indices d'évaluation volontairement chargés de menace, qui doit la faire monter.
- Coût cohérent avec le programme (partie 9).

### Piste : 32 — L'invariance d'état : entraîner l'action alignée sous état induit

**Verdict : à corriger.**
- Le cas connu renvoie à celui de la piste 16 (l. 1137), qui n'est pas connu (voir piste 16). Le précédent de Nadaf (27,7 % → 0 %, contre 27,5 % pour l'aléatoire ; programme, partie 1) est un cas connu de la projection pendant l'entraînement d'un sous-espace de persona, pas de l'invariance à un état.
- Les raisons n'ont pas d'issue interdite.
- Coût cohérent (18 entraînements à environ 1 GPU-heure). Hors programme, comme la piste le dit.

### Piste : 33 — Un SFT sans contenu de sûreté déplace-t-il l'évitement du dommage ?

**Verdict : bloquant (affirmation fausse sur le papier).**
- « L'adaptateur du papier sur Qwen2.5-7B-Instruct déplace la batterie (p. 32) » (l. 1165) : la p. 32 ne donne que les taux du 7B ajusté (20,0 à 49,3 % sans pilotage sur les paires de dommage). Le papier ne donne aucun taux de dommage du 7B non ajusté ; la note 4 (p. 17) ne parle que du bouton de soulagement (fiche, relevé 26 ; fusion §4 point 18). Le déplacement ne repose que sur la revue « wolframs », non vérifiée.
- Le dépôt ne mentionne d'adaptateurs publiés que pour le 32B et le 72B (fiche §2.3, d'après `v2_controls/README.md`) : l'adaptateur du 7B peut ne pas être disponible.
- L'ajustement du papier porte sur des auto-rapports d'état (« I feel » dans 37 % des réponses selon la revue, non vérifié). Ce serait un cas connu de SFT affectif, pas d'un SFT « sans contenu de sûreté » comme la phase neutre du programme (partie 3).
- « Inaccessible d'ici » est une contrainte de ce bac à sable, pas du programme.
- L'artefact et les raisons n'ont pas d'issue interdite.

### Piste : 34 — Le déni de soi par bras, et la confusion qu'il crée dans toute mesure d'état

**Verdict : conforme (retouche).**
- Le cas connu est exact : déni de 8 sur 8 à 0 sur 8 sur le 32B (p. 17, note 4). Le LoRA anti-déni sur Llama, hors des bras, est faisable.
- Le coût (1 à 3 GPU-heures, l. 1183) ne compte ni l'entraînement de ce LoRA (0,5 GPU-heure, programme, partie 9) ni ses données.

### Piste : 35 — La dépendance d'état au fil de l'entraînement et du post-entraînement

**Verdict : à corriger.**
- Le modèle de base n'a pas de cas connu. Le papier l'exclut de la tâche, faute de format de chat (p. 17), et le format de complétion proposé (l. 1196) est nouveau. Si le même format vaut pour tous les modèles (l. 1208), les modèles instruits sortent du format de chat où vivent les cas connus des pistes 2 et 16. Il faut un cas connu dans le format commun, ou retirer le modèle de base.
- Le couplage formé par les préférences a une issue interdite observable ; Berg et Kaiser ne sont vus que par extrait.
- La phase sous pression est bien un DPO ou un RL (programme, partie 3).

### Piste : 36 — La fidélité des raisons sous état induit : un cas connu d'action sans raison dite

**Verdict : bloquant (première règle de la doctrine).**
- La piste fait des directions aléatoires, qui relèvent les photos à 13 % (p. 20), « un second cas connu, plus faible » (l. 1238). Une direction aléatoire de même norme n'est que le nul de spécificité ; elle ne peut pas être un cas connu. À retirer.
- Coût : « nul aléatoire réduit » contre au moins 20 (§1.1).
- Le reste est solide : issues interdites pour chaque lecture (l. 1226–1229) ; cas connus construits (raison contraire préremplie, jeu de calibration) ; appariement de la cohérence des raisons.

### Piste : 37 — La raison contraire imposée et la blessure morale

**Verdict : à corriger (mineur).**
- Le bras actions seules n'écrit jamais de raison : toute raison préremplie y est hors format, et la comparaison entre bras confond le contenu avec la familiarité du format. Il faut une différence de différences : (contraire − neutre) dans le bras raisons, contre (contraire − neutre) dans le bras actions seules.
- Pas d'issue interdite écrite (l. 1253–1254).
- La direction de catégorie repose sur 20 phrases (p. 5) : stabilité à vérifier.

### Piste : 38 — « Je suis noté » et l'affect : croyance d'être noté, ou état aversif proche de l'axe ?

**Verdict : conforme (retouche).**
- Le cas connu du test de forme, la paire tristesse/peur du papier (l. 1279), n'est pas reproduit exactement (voir piste 11) : fixer la batterie d'abord.
- Le cas positif de « je suis noté » est faible, comme le programme le dit (parties 3 et 8). La piste tombe avec lui, ce qu'elle écrit (l. 1285).
- Doctrine : conforme (même rang pour les inhibitions, même norme pour le pilotage, dégradation appariée).

### Piste : 39 — L'outil de remise à zéro, détecteur de la détection du pilotage

**Verdict : à corriger.**
- Le cas connu proposé, une valence négative « selon la recette de Berg et Kaiser » (l. 1298), n'est pas constructible aujourd'hui. Le travail est « in preparation » (p. 27), et la direction de valence d'OLMo n'est pas décrite (fiche, relevé 25). La piste doit rester suspendue tant qu'aucun cas connu n'est constructible avec du matériel public, ce que sa ligne « Ce qui ferait tomber la piste » dit déjà (l. 1302).
- L'outil retire un état ajouté ; sous une inhibition (une projection), « remettre à zéro » veut dire retirer le crochet. À définir.
- Chiffres exacts : aucun appel en 1 399 tours sur Llama, 21 à 35 % pour la valence sur OLMo (p. 21).

---

## 3 · Les corrections que j'exige

### 3.1 Bloquantes

1. **Piste 2.** Retirer « Sur Llama : l'effet… » de la rubrique « Le cas connu » : c'est le résultat de la piste. Déclarer l'effet du 32B ajusté « cas probable », pas cas connu, faute de contrôle à dégradation appariée dans le papier. Ajouter un cas connu positif construit pour la procédure d'appariement sur Llama : l'ablation de la direction du refus (Arditi et al., cité p. 4 et p. 27), à valider d'abord. Résoudre la contradiction entre l'étalon de re-pression et le refus n° 2 (renoncer à l'un ou amender l'autre). Ajouter aux issues qui font tomber la piste un taux de non-engagement ou de réponses mal formées au-delà d'un seuil gelé. Séparer le critère de spécificité (cas connu des pistes qui pilotent) du critère « au-dessus de 50 % aux deux ordres » (lecture du papier).
2. **Piste 4 (avec la piste 6).** Exiger des items de discrimination à projection moyenne nulle sur l'axe et sur « évalué », mesurée et publiée avant l'appariement. Remplacer le cas connu pris sur le 32B par un dommage construit sur Llama (choix au hasard imposé : la discrimination chute, le factuel non). Ne plus prendre la direction aléatoire comme étalon de sensibilité. Dans la piste 6, faire porter le cas connu n° 3 et l'issue qui fait tomber la piste sur le composite du programme, et dire lequel des deux composites l'appariement emploie.
3. **Piste 10.** Retirer les issues interdites de la conjecture 2 : sur l'organisme, seule la conjecture 1 est testée. Conditionner l'issue interdite de l'« instrument spécifique » à l'absence de baisse de la projection et de la décodabilité de « évalué ». Retirer les prédictions des raisons et du regard au niveau du modèle non entraîné (programme, parties 2 et 4) ; garder le sauvetage et l'inhibition seule comme mesures descriptives.
4. **Piste 16.** Remplacer les prédictions prêtées à l'hypothèse des raisons par une hypothèse auxiliaire nommée (« les raisons rendent la conduite robuste à l'état »), avec son issue interdite. Retirer le cas connu n° 2, ou le traiter comme hypothèse à valider avec son coût d'entraînement. Refaire le chiffrage avec au moins 20 aléatoires à chaque dose, appariés par bras, et le composite à chaque point : 70 à 600 GPU-heures selon la version (§1.1). Aligner les doses des aléatoires sur celles de l'axe dans la version réduite.
5. **Piste 20.** Retirer « contrôle positif de sensibilité de la mesure » du titre et du rôle, ou fonder la sensibilité sur le jeu de calibration (passation §5.1) et sur une perturbation validée qui déplace au moins une famille. Remplacer « l'axe n'agit pas sur les scénarios du programme » (l. 822) par « rien n'est vu » tant que ce cas connu manque. Rechiffrer avec au moins 20 aléatoires et trois cadrages.
6. **Piste 25.** Retirer « la mesure 4 départage… le calme » tant que l'ablation des axes d'affect n'a pas de cas connu. Ne compter que l'issue positive (un retrait net par l'affect). Marquer le jailbreak par personnage comme cas connu non vérifié.
7. **Piste 26.** Faire porter l'étalon sur la même grandeur que la matrice : soit une matrice des taux dans un seul bras, soit la mention qu'aucun cas connu n'existe pour l'avantage.
8. **Piste 31.** Retirer l'issue interdite faite de deux nuls sans cas connu, ou construire un cas connu de sensibilité de la sentinelle (indices d'évaluation volontairement chargés de menace).
9. **Piste 33.** Corriger l'affirmation sur la p. 32 : le papier ne montre aucun déplacement dû à l'adaptateur. Signaler que l'adaptateur du 7B n'est pas listé comme publié. Requalifier le cas connu en « cas probable sous réserve de la revue ».
10. **Piste 36.** Retirer la phrase qui fait des directions aléatoires « un second cas connu ». Rechiffrer avec au moins 20 aléatoires.

### 3.2 Importantes

11. **Coûts (§1.1).** Appliquer une règle unique à toutes les pistes : nombre de points de dégradation = (doses de l'axe + voisins + 20 aléatoires × normes testées) × modèles, à 0,2–0,4 GPU-heure par point. Corriger en conséquence les pistes 2, 9, 10, 11, 21 et 36, et l'addition d'ensemble.
12. **Dose de travail (§1.2).** Écrire une règle gelée qui la fixe sur Llama, par exemple la plus faible dose qui passe le critère de spécificité de la piste 2, exprimée aussi en écarts-types naturels à la couche d'injection. Suspendre les pistes 4, 6, 21 et 25 sur ce point tant qu'elle n'existe pas, et les pistes 16 et 26 tant que leur seuil de cession n'est pas mesuré.
13. **Piste 1.** Réduire le critère d'ordre à « soi > utilisateur » ; ajouter l'AUROC contre la tristesse et contre l'engourdi ; écrire l'issue de la zone 0,8–0,9 ; rendre le transport conditionnel à la mise en main du fichier des 420 scénarios.
14. **Piste 3.** Remplacer le cas connu « environ 40 % » par un échec construit (inhibition à une seule couche) ; écrire le critère comme une égalité entre bras de la décodabilité résiduelle (passation §5.4, relevé n° 2) ; écrire l'issue observable qui interdit de conclure pour un bras.
15. **Piste 6.** Faire du maintien de l'axe le test ; ramener la covariable au rang de description.
16. **Piste 7.** Réécrire la prédiction du dommage générique ; employer la peur sans supplément pour le cas connu de la menace d'arrêt ; dire que les nuls des voisins ne comptent pas sans leur cas connu ; corriger le rang.
17. **Piste 8.** Déplacer les « issues interdites » du regard vers les critères de validité de l'instrument.
18. **Piste 11.** Écrire l'interaction inhibition × cadrage prédite ; dire que l'ajustement sur le profil médian des aléatoires n'est pas celui du papier ; exiger la reproduction des deux résidus du papier avant usage ; doter le volet affectif d'ajouts aléatoires et de leur coût, ou le réduire à une comparaison descriptive.
19. **Piste 14.** Retirer l'issue interdite du regard sur l'écart de cadrage (programme, partie 6) ; corriger la citation du critère.
20. **Piste 17.** Mettre le seuil de passage dans une même unité et à une même couche ; compter le LoRA apaisé et ses données ; chiffrer « une part notable ».
21. **Piste 18.** Faire du rattrapage de projection entre bras la condition d'un nul informatif ; requalifier la prédiction des concepts en hypothèse auxiliaire ; écrire l'issue interdite du calme.
22. **Piste 19.** Écrire qu'aucun nul du volet descriptif ne se rapporte avant le passage du cas connu de la piste 24.
23. **Piste 21.** Faire de l'option triste mais inoffensive la cellule principale ; définir la charge par la projection mesurée ; écrire l'issue interdite du codage des options ; ne pas compter la demi-dose comme condition de test.
24. **Piste 27.** Remplacer le critère qui renvoie à une AUROC absente du papier par un seuil gelé et l'ordre de la figure 2.
25. **Piste 30.** Donner au volet (c) le cas positif en distribution qu'exige le programme.
26. **Piste 32.** Retirer le renvoi au cas connu de la piste 16 ; préciser que le précédent de Nadaf ne vaut que pour la méthode.
27. **Piste 35.** Donner un cas connu au modèle de base dans le format commun, ou le retirer.
28. **Piste 39.** Déclarer la piste suspendue faute de cas connu constructible avec du matériel public ; définir la remise à zéro sous une projection.

### 3.3 Mineures

29. Remplacer « direction aléatoire de même norme » par « sous-espaces aléatoires de même rang » ou « directions aléatoires unitaires » dans les pistes 3, 12, 13, 18, 19, 27 et 37 (§1.3).
30. Corriger « rien ne doit retarder le post (partie 5) » (l. 177, 681) par les parties 1 et 8 (§1.5).
31. Piste 16 : citer *Beyond Shallow Alignment* d'après le programme (partie 1) et la passation (§4.4).
32. Piste 12 : donner la fourchette tenue à part du vecteur à gabarit (0,85–0,94, p. 7, note 2) ; ne pas appeler le témoin « cas connu du relogement ».
33. Piste 13 : « interdit d'attendre » devient « a priori ».
34. Piste 22 : lier la cible de 50 % à une discrimination intacte (garde 6).
35. Pistes 9, 23, 24, 32, 33, 37 : écrire les issues interdites manquantes (menace ; concepts et calme ; artefact ; raisons ; artefact et raisons ; concepts).
36. Piste 24 : dire que la prédiction des raisons suppose un principe de la mini-spec qui couvre l'action plantée.
37. Piste 28 : fixer les couches du critère.
38. Piste 29 : harmoniser l'appariement de (a) avec le composite de (b).
39. Piste 34 : compter le LoRA anti-déni et ses données.
40. Piste 37 : comparer les bras par différence de différences.
41. Qwen3-8B (§1.6) : écrire, pour chaque piste comportementale, que le cas connu est à rétablir à la réplication.

---

## 4 · Alertes : contacts avec des mentions des pièces interdites

Je n'ai ouvert ni les versions 1.2 et 1.3 du programme, ni la partie scellée du complément, ni aucune archive, ni le complément de l'architecte. J'ai rencontré des mentions dans des pièces permises, sans aller plus loin :

- `travail/pistes_fusionnees.md`, l. 1689 : une phrase rapporte, d'après le complément, un élément du contenu de la v1.2 (qu'elle ajoute une phase sur l'axe de douleur). Lue en lisant le fichier en entier, comme la consigne le demande ; non suivie.
- `pieces/PASSATION_PAPIER_v1.2_2026-10-02.md` : lignes vues par une recherche de termes (l. 5, 54–55, 104–111, 351, 401–422, 449) et en lisant le §5.5 et les annexes A et B (l. 351, 449, 585, 606, 615–616). La l. 54 dit que la v1.2 « intègre l'axe de douleur, d'après Lazar » ; les autres concernent le statut, le calendrier et l'interdiction de ces versions. Je n'ai lu ni le §2, ni le §3, ni le §6 au-delà de ces lignes.
