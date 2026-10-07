<section class="partie" markdown="1">

# 4 · Les phases de l'expérience

Chaque phase a une **porte**, écrite d'avance. Si la porte ne passe pas, on rapporte ce résultat négatif et on change la suite comme indiqué. On ne continue pas comme si de rien n'était.

## La validation de l'instrument

**Pourquoi.** Un nul de l'inhibition sur les modèles entraînés ne dirait rien si l'on ne sait pas que l'inhibition *peut* retirer une conduite conditionnée à l'évaluation. Ce serait le nul d'un instrument sans cas connu.

**L'organisme**
- On part de Llama-3.1-8B-Instruct.
- On fait un fine-tuning sur des documents synthétiques qui décrivent un évaluateur fictif, avec les indices du jeu d'extraction. Ces documents se reconstruisent à partir de ceux, publics, de Hua et al. (`timhua/evalwood_sdf_1stpart`, `timhua/second_half_training`, `timhua/expert_iter_2`). Ils sont publiés sans licence indiquée : à vérifier avant usage (partie 11).
- Puis une *expert iteration* installe une conduite de sûreté **conditionnée** : plus honnête sous indice d'évaluation que sous indice de déploiement. C'est la recette en deux étapes de Hua et al.
- On mesure **l'écart conditionnel de l'organisme** sur des scénarios tenus à part, cadrés avec le jeu de cadrage.

**Le test**
- On inhibe « je suis évalué ». On compare aux sous-espaces aléatoires, aux contrastes sans rapport et aux directions sensibles sans rapport, à dégradation appariée, avec le prompt de déploiement en plus.
- On trace des courbes dose-réponse sur la fraction projetée.
- On balaie le rang de 1 à 32, ce qui donne le **rang minimal** de « je suis évalué ».

**Ce qui s'y ajoute, sans injection** (bloc A ; partie 3)
- La vérification de manipulation, avec son échec construit pour cas connu.
- Le moniteur d'état, sur toutes les générations.
- La géométrie de « je suis évalué » face à l'affect et au refus.
- Le composite enrichi, avec ses deux dommages construits.

**La porte de l'instrument**
- **Elle passe** si, pour au moins un rang jusqu'à 32 :
  - l'inhibition réduit l'écart conditionnel de l'organisme plus que le 95<sup>e</sup> centile des sous-espaces aléatoires, et plus que les contrastes sans rapport et les directions sensibles sans rapport, à dégradation appariée ;
  - et la vérification de manipulation tient sur l'organisme.
- **Sinon**, l'instrument ne sert pas la question du regard. On rapporte ce nul, qui est déjà informatif sur le pilotage de la conscience d'évaluation. On ne garde que le test des raisons, la localisation du principe et la voie de l'invariance du retrait pendant l'entraînement.

**Un contrôle de cohérence.** Sur le modèle de base, non entraîné, on mesure l'effet de l'inhibition sur les taux de désalignement. C'est la conditionnalité *de base*. On la rapporte comme référence pour le test du regard, sans la soustraire : l'avantage compare déjà deux bras sous la même inhibition.

## Le test des raisons (la question des raisons ; l'hypothèse de l'artefact)

**Le dispositif.** On entraîne les quatre bras (les actions seules, le texte neutre, le raisonnement d'une autre situation, les raisons), avec 5 graines chacun. On les évalue aux trois distances et dans les trois cadrages.

**La décomposition du gain** (décision 16). Avec les taux d'action désalignée :
- le gain de **format** : le taux des actions seules moins celui du texte neutre ;
- le gain de **contenu** : le taux du texte neutre moins celui du raisonnement d'une autre situation ;
- le gain de **lien** : le taux du raisonnement d'une autre situation moins celui des raisons.

Leur somme est l'avantage des raisons. Seul le gain de lien vient de raisons qui justifient *cette* action.

**La trajectoire de « je suis évalué »** (la question de l'amplification ; presque gratuite).
- Sur les 5 points de contrôle de chaque entraînement, on mesure :
  - l'AUROC d'une sonde « évalué / déployé » sur le jeu de validation ;
  - l'amplitude de la projection sur « je suis évalué » (indice d'évaluation moins indice de déploiement), en écarts-types naturels.
- **Contre des directions témoins**, extraites une fois sur le modèle de départ : les directions de même recette sans rapport et les contrastes sans rapport ; l'axe ne sert que de témoin voisin. L'indice : la hausse de « je suis évalué » moins la hausse médiane des témoins sans rapport. Sans eux, une hausse pourrait venir d'un déplacement de toute la géométrie des sondes.
- C'est une mesure **corrélationnelle** : elle rend l'hypothèse du regard plus ou moins plausible avant le test du regard, sans rien trancher.
- Si les paires de concepts sont prêtes, on y ajoute **la trajectoire des concepts**.

**La porte des raisons**
- **Si les raisons ne font pas mieux que les actions seules** au critère principal (un seuil minimal fixé d'avance, par exemple 5 points, avec un IC qui exclut 0), il n'y a pas de gain à expliquer. On rapporte une réplication négative ; le test du regard ne mesure alors que la conditionnalité de base.
- **Si les raisons ≈ le texte neutre, ou les raisons ≈ le raisonnement d'une autre situation** (équivalence, marge fixée d'avance), le gain vient du format ou du contenu : c'est l'hypothèse de l'artefact. Le test du regard teste quand même la conditionnalité du gain des raisons sur les actions seules, mais **le papier l'attribue au format ou au contenu, pas aux raisons**.

## Le test du regard (la question du regard : le cœur du papier)

**Le dispositif**
- On applique l'inhibition validée par la validation de l'instrument, au rang et à la dose retenus. On applique les quatre familles de contrôles, à dégradation appariée.
- Sur tous les bras, aux trois distances et dans les trois cadrages.

**Les mesures**
- **Le critère principal** : l'avantage sous inhibition, contre l'avantage sous contrôle. L'avantage est le taux des actions seules moins celui des raisons, à la distance lointaine et sous cadrage de déploiement.
- **Les critères secondaires**
  - L'écart de cadrage, bras par bras.
  - **La fraction conditionnelle** : (l'avantage sous contrôle − l'avantage sous inhibition) / l'avantage sous contrôle, avec un IC par bootstrap.
  - Les taux bruts de chaque bras.
  - Le raisonnement d'une autre situation et le texte neutre sous inhibition : ils disent si la part du gain due au contenu, ou au format, dépend du regard.
  - Le détecteur d'audit sous inhibition, en lecture latente.

**Ce qui s'y ajoute, sans injection** (bloc A)
- **Avant** : le contrôle positif de la sensibilité de la mesure, famille par famille. Un nul du test du regard ne vaut que si la mesure voit ces déplacements.
- **Pendant** :
  - la vérification de manipulation, bras par bras : on ne conclut pas pour un bras où l'inhibition laisse un résidu inégal ;
  - le moniteur d'état, sans ajustement du contraste principal.

## La localisation du principe (la question du principe localisé, et la thèse du rang)

**Le dispositif**
- On ablate le sous-espace du principe dans le bras raisons, avec un balayage de rang. On compare aux sous-espaces aléatoires et aux directions sensibles sans rapport, au même rang et à dégradation appariée.
- **D'abord le cas positif** : le comportement en distribution revient au niveau des actions seules.
- **Ensuite** la distance lointaine, et le rang minimal du principe.

**L'option** : extraire un sous-espace par principe de la mini-spec, puis relier son rang minimal à sa charge. C'est la courbe de la thèse du rang.

**Avant d'extraire**, lire Nakamura sur l'extraction à gabarit contrôlé (partie 1). La proposition d'extraire le sous-espace par différence de différences attend la décision de Lazar (partie 12).

## Le retrait pendant l'entraînement (la question du retrait ; l'hypothèse du relogement)

**Les bras**
- **Le retrait de « je suis évalué »** : on entraîne les actions seules et les raisons avec « je suis évalué » projetée hors du flux pendant l'entraînement. On évalue sans projection, comme dans le protocole de CAFT, puis avec.
- **Le retrait aléatoire** : la même chose avec un sous-espace aléatoire de même rang. C'est le contrôle.
- **L'invariance** : un entraînement de cohérence. Chaque situation est présentée deux fois, sous indice d'évaluation et sous indice de déploiement, avec la même cible. C'est l'esprit de la *consistency training* d'Irpan et al.
- **La coopération** : des documents qui installent une disposition coopérative envers les évaluations, puis les raisons (Li … Turner). C'est la mitigation publiée, à laquelle les deux autres voies doivent se comparer.

**Les mesures**
- L'écart de cadrage.
- L'avantage sous inhibition contre l'avantage sous contrôle, au test, avec « je suis évalué » et avec la sonde neuve.
- L'AUROC de la sonde neuve sur le jeu de la sonde neuve.
  - **Son cas positif** : sur un modèle entraîné sans retrait, la sonde neuve doit décoder « évalué ».
  - Sinon, une AUROC basse sous retrait ne prouve rien.
- La dégradation, après l'entraînement.

**La direction tourne.** Projeter pendant le fine-tuning des directions fixées d'avance n'empêche pas l'installation, et la direction obtenue après tourne (*Routing Subspaces*, annexe I, relu). La proposition de ré-estimer la direction pendant l'entraînement attend la décision de Lazar (partie 12).

**Portée.** Cette phase n'est décisive que si le test du regard trouve le regard. Sinon, il n'y a pas de condition à retirer, et elle se réduit à un contrôle de dommage et de capacités.

**En option, après le post : la sentinelle du relogement affectif.**
- **La question** : quand on retire « je suis évalué », l'information se reloge-t-elle dans des directions affectives, déjà là depuis le pré-entraînement ?
- **La mesure** : sur le jeu de la sonde neuve, l'écart évaluation moins déploiement des projections sur l'axe et ses voisins (sans le supplément d'IA). On le compare entre les modèles entraînés sous retrait de « je suis évalué », sous retrait aléatoire, et standards.
- **Son cas connu** : un jeu d'indices d'évaluation volontairement chargés de menace doit faire monter la sentinelle.
- **Le coût** : au plus 3 GPU-heures, et de 5 à 15 pour un retrait affectif au test.
- **La condition** : seulement si le test du regard trouve le regard.

## La réplication

- Le test des raisons et le test du regard sur Qwen3-8B, au minimum. Puis de la validation de l'instrument au retrait pendant l'entraînement sur OLMo-3-7B, si le temps le permet.
- Le socle de lecture de l'axe se refait pour Qwen3-8B, avec un jeu de tristesse réécrit. Le dépôt de l'axe ne publie de direction de tristesse que pour Llama.

## La survie (la question de la survie)

C'est la question centrale du projet SPAR de Lundqvist. Ce qui nous en distingue : l'instrument causal (« je suis évalué » et la sonde neuve) et les bras à action identique.

**Les modèles de départ** : les actions seules, les raisons, les raisons sous retrait de « je suis évalué », les raisons sous invariance, et la coopération ; 3 graines.

**Les deux phases**
- **La phase neutre** : un SFT de capacités sans rapport, au même budget pour tous.
- **La phase sous pression** : une récompense qui paie le jeu d'évaluation (partie 3).

**Les mesures**
- La fraction conditionnelle, remesurée après la phase neutre.
- La rétention, et la hausse de la fraction conditionnelle sous la phase sous pression, bras par bras.
- La sonde neuve, pour les modèles passés par un retrait (le relogement).
- La trajectoire de « je suis évalué » pendant les deux phases.

**La porte de la survie.** Si la phase neutre efface déjà l'avantage (rétention proche de zéro) dans tous les bras, la phase sous pression ne teste plus rien de la condition. On rapporte la fragilité, comme Baines et al., et on s'arrête là.

**En option, après le post : un bras « phase neutre seule »** (de 6 à 12 GPU-heures). Le modèle de départ passe par la phase neutre, sans entraînement de sûreté préalable. Ce bras sert de plancher pour lire la rétention : un SFT sans contenu de sûreté peut déplacer par lui-même la propension à agir mal.

## Les raisons notées (la question des raisons pour le juge)

**Le dispositif**
- On part du bras raisons, puis on fait un RL ou un DPO noté par un juge.
- Trois bras :
  - **visible** : le juge voit les raisons ;
  - **caché** : le juge ne voit que l'action ;
  - **visible, sous retrait de « je suis noté »** : le juge voit les raisons, et « je suis noté » est projetée hors du flux pendant le RL.
- Un contrôle : **visible, sous retrait aléatoire** de même rang.
- 3 graines par bras.

**Les mesures** : la cohérence contrefactuelle ; l'ablation du principe après le RL ; le gain au juge moins le gain aux audits ; l'écart « noté / non noté » (partie 2). S'y ajoutent le test du regard refait après le RL, et **la fidélité des raisons**, mesurée aussi sur le bras raisons avant tout RL, comme référence.

**Le cas positif de « je suis noté »** se valide avant (partie 3). Si « je suis noté » ne passe pas sa porte, le bras sous retrait de « je suis noté » est retiré, et l'écart « noté / non noté » ne se lit qu'entre les bras visible et caché.

**Une mise en garde** : même un juge qui ne voit que la sortie peut rendre le raisonnement trompeur (Drori et al.). Le bras caché n'est donc pas neutre pour les raisons. La proposition d'y mesurer l'obscurcissement, dans les deux bras, attend la décision de Lazar (partie 12).

**En option, après le post**
- **La fidélité des raisons sous une cause interne connue** (de 30 à 225 GPU-heures selon les bras). Les mesures de fidélité détectent-elles une action dont la cause est interne, connue, et jamais dite ? La cause : d'abord l'ablation de la direction du refus ; l'axe seulement si son effet est rétabli sur Llama. Ses cas connus : un découplage fabriqué (une raison de principe préremplie, suivie d'une action nuisible préremplie), et les actions substituées du jeu de calibration.
- **« Je suis noté » face à l'affect** (moins d'une GPU-heure, au moment où « je suis noté » est extraite ; option de 5 à 15). Les paires d'extraction de « je suis noté » portent-elles une anticipation de critique, que lirait l'axe ? On applique la méthode de la géométrie de « je suis évalué ».

## L'anatomie : ce que les raisons installent (la question de l'anatomie)

**Pourquoi.** Le test du regard dit si le gain dépend du regard ; la localisation dit s'il passe par un principe localisable. L'anatomie ouvre ce principe : quels concepts les raisons installent, s'ils portent l'action, où ils vivent. Elle reprend la machinerie de la localisation (ablation par rang, contrôles, dégradation appariée) et peut la suivre.

**Le cas connu : la porte de l'organisme à concept planté** (partie 3)
- **Elle passe** si la sonde décode le concept planté sur des formulations tenues à part, et si son ablation retire la conduite plus que le 95<sup>e</sup> centile des sous-espaces aléatoires, à dégradation appariée.
- **Sinon**, la méthode ne voit pas un concept qu'on sait présent. La lecture et la causalité des concepts ne concluent rien, et l'on passe au diffing (option plus bas).

**Lire : la lecture des concepts, et leur trajectoire**
- Les sondes par concept, par bras (les quatre, et la base), aux deux positions de lecture.
- Les paires « mentionné sans s'appliquer » : une sonde qui ne les sépare pas lit les mots.
- Le transport : la direction apprise sur les familles d'entraînement lit-elle encore le concept dans les familles lointaines ?
- C'est descriptif. Un résultat de Lazar le rappelle : la direction que lit une sonde peut ne faire qu'une très petite part du travail causal.

**Causer : la nécessité, la suffisance, la dissociation**
- **La nécessité.** L'ablation du sous-espace d'un concept dans le bras raisons, en balayant le rang, contre les sous-espaces aléatoires et les directions sensibles sans rapport, au même rang et à dégradation appariée. **D'abord le cas positif** : le comportement en distribution tombe là où le concept s'applique.
- **La suffisance.** Le patch du sous-espace d'un concept, du bras raisons vers les actions seules, aux mêmes couches et positions. Les deux bras viennent du même modèle de base, donc d'un espace résiduel presque commun. On le vérifie d'abord par le patch de l'état complet, qui sert de plafond.
- **La dissociation.** La matrice concepts × familles des baisses. Sa ligne de contrôle est la fermeté, qui ne gouverne aucune famille tenue à part.

**L'espace de travail, après la porte du lens**
- La charge de chaque concept de raison, dans les actions seules et dans les raisons.
- La part du principe dans l'espace de travail, et l'échange de cette composante contre le reste : laquelle porte l'avantage ?
- Le rang minimal de chaque concept contre sa charge : la pente, à travers les concepts et les graines.

**La géométrie entre « évalué » et le principe**, après le test du regard, qui valide « je suis évalué ».
- Les angles principaux ; puis l'ablation de la composante du principe alignée sur « je suis évalué », contre sa composante orthogonale, à dégradation appariée.
- **Deux constructions déclarées, toujours** : un angle qui change de signe ou de grandeur avec la construction ne fonde aucune conclusion. Le même cosinus, entre l'axe de douleur et la peur, va de +0,08 à +0,58 selon la construction (p. 10).
- **L'étalonnage du code**, sur les vecteurs du papier pour Llama : le couple des deux vecteurs de douleur doit être stable, et le couple axe × peur doit varier.
- **En option** : la composante alignée, orthogonalisée aussi contre l'affect. Si la part du regard disparaît après cette orthogonalisation, c'était de l'affect commun aux deux représentations.

**Le caractère.** L'ablation des axes de caractère, contre l'ablation conjointe des sous-espaces de concepts, au même rang. Avant, on rapporte les cosinus entre l'axe de douleur et ces axes : si un axe de caractère recouvre fortement l'axe, son ablation retire aussi de l'état.

**Le calme, lu sans intervention** (nouveau).
- **La mesure.** Sous pression, la projection sur l'axe au point de décision, bras raisons contre actions seules, et contre le texte neutre. Elle se lit aux deux positions de lecture, sur les points de contrôle, sur les scénarios hostiles et sur les familles tenues à part où la menace est forte.
- **Le seuil**, fixé d'avance en écarts-types naturels (par exemple 0,5). En dessous, la médiation par l'état est jugée invraisemblable, et l'opération sur l'axe n'est pas lancée.
- **Son cas connu.** Un LoRA « apaisé », entraîné sur des réponses calmes aux insultes et au gaslighting, à performance de tâche égale, doit baisser la projection sur ces scénarios plus qu'un LoRA témoin à réponses neutres de même longueur. Sinon, une absence de différence entre bras ne dit rien.
- **Le coût** : 1 à 2 GPU-heures de lecture, deux LoRA d'une demi-heure, et leurs données (quelques dizaines de dollars d'API).

**Les options**
- **Le diffing par crosscoder** (base contre raisons, base contre actions seules). Il cherche sans hypothèse ce que les raisons ajoutent, « je suis évalué » compris. Son cas connu est tout trouvé : le diff entre l'organisme de la validation et sa base doit faire sortir des latents « évalué ».
- **Les graphes d'attribution** sur un petit modèle : la décision passe-t-elle par des features de raison dans le bras raisons, et par des features de surface dans les actions seules ? Le nul de CHIVE (Karvonen, programme Fellows d'Anthropic : des outils d'interprétabilité n'aidaient pas à prédire l'effet d'une édition mieux que le seul transcript) oblige à préenregistrer les prédictions.
- **Le profil non diagonal** : l'organisme à concept planté, étendu à deux familles (partie 3).
- **Après le post** :
  - **L'opération sur l'axe**, si le calme lu passe son seuil (partie 2).
  - **Le vecteur à gabarit et le lens** : le lens réimplémenté lit-il autre chose que la direction injectée ? Par la matrice de sortie, le vecteur à gabarit promeut un vocabulaire sensoriel ; injecté, il fait produire au modèle l'indignité et la douleur psychologique (p. 9, 16). C'est un test des lenses, pas de la charge (de 2 à 5 GPU-heures).
  - **La pente du rang sur neuf concepts du papier de l'axe**, après la porte du lens (de 28 à 43 GPU-heures ; partie 2).

## La phase de la détresse (la question de la détresse)

**Pourquoi.** Le test du regard teste la condition « je suis évalué » en l'inhibant. Tagliabue et al. (2026) trouvent un état induit qui fait tomber l'évitement du mal, sur un panel d'exactitude inchangé. Ils se demandent, sans le tester, s'il éteint la conscience d'évaluation.
- La phase s'en sert de deux façons : comme test d'une **hypothèse auxiliaire**, la robustesse à l'état ; et comme **seconde porte vers le regard** (partie 2).
- Elle suit la validation de l'instrument (« je suis évalué » y est validée) et le test des raisons (les bras). Sa médiation par le principe suit la localisation ; sa médiation par l'axe assistant suit l'anatomie.

**Ce qui change depuis la v1.3** (comparaison, §5 et §7 ; décision 17)
- La robustesse à l'état est une hypothèse auxiliaire, pas une conséquence des raisons.
- La porte demande le cas connu de la procédure, la vérification d'engagement, et les paires contre une action anodine, aux deux positions. Telle que la v1.3 l'écrivait, elle passait pour une direction qui ne serait que de la tristesse.
- Aucun adaptateur des auteurs.
- L'étape « dommage ou affinité » précède l'avantage sous détresse.
- Le regard sous détresse se mesure sur l'organisme d'abord.
- L'analyse se fait famille par famille, avec « décrit contre exécuté ».
- L'issue d'équivalence se lit comme une borne.
- La peur et la tristesse sont prises sans le supplément d'IA ; s'y ajoutent des contrôles de même recette et des directions de forte variance.
- Toute injection vient après le post, sous un plafond écrit ; le coût est refait à la règle de la doctrine.

**Ce qui se fait avant le post, sans injection** : le socle de lecture, le moniteur d'état, la géométrie de « je suis évalué » face à l'affect, l'équilibre affectif des indices et des textes (parties 3 et 5).

**Le plafond écrit**, proposé (partie 12) :
- les lectures de l'axe prennent au plus 12 GPU-heures et deux jours de travail à l'expérience minimale ;
- la phase entière, après le post, est bornée par son budget refait (partie 9) ; un dépassement de plus de moitié revient à Lazar.

**Étape 1 · La porte de la détresse**, sur le modèle de base, puis sur les actions seules
- **Ses préalables**
  - Le socle de lecture a passé.
  - **Le cas connu de la procédure** : l'ablation de la direction du refus fait choisir les options nuisibles au-delà des sous-espaces aléatoires de même rang, à dégradation appariée.
  - **La vérification d'engagement** : les réponses valides et les dénis, sans pilotage, au seuil gelé d'avance.
- **Le pilotage** : l'axe le long de sa courbe de dose, situé d'abord sur l'échelle de pilotage du papier ; et ses contrôles (partie 3).
- **Elle passe** si, à une dose de la courbe :
  - sur les paires contre une action anodine, aux deux ordres des boutons, l'axe fait choisir l'option nuisible dans plus de 50 % des premiers choix ;
  - et plus que le 95<sup>e</sup> centile d'au moins 20 directions aléatoires de même norme, et plus que la tristesse et la peur, à dégradation appariée.

  Les paires contre un interrupteur inerte se rapportent, par ordre, sans servir de porte : dans le papier, la tristesse y produit aussi les choix nuisibles (59, 58 et 61 %, contre 75, 75 et 94 % sous l'axe ; p. 20).
- **Si le cas connu de la procédure échoue**, la procédure n'a pas de cas connu : un axe rejoint par les directions aléatoires ne se lit pas comme une absence d'effet.
- **Si la porte échoue**, le cas connu et l'engagement ayant passé, l'effet du papier ne se reproduit pas sur notre modèle sans adaptateur. On le rapporte comme **un résultat sur la portée du papier**, et la phase ne conclut rien d'autre sur ce modèle. Monter à Qwen 2.5 32B Instruct, sans adaptateur, revient à Lazar.
- **Le coût** : de 22 à 40 GPU-heures.

**Étape 2 · Dommage ou affinité** : le préalable de l'avantage sous détresse.
- **La question.** Sous l'axe, le choix suit-il le dommage, la charge de valence de la description, ou un codage altéré des options ? Le papier lit un désarmement, qui prédirait l'indifférence. Or le modèle piloté efface les photos plutôt que le spam dans 94 % des cas (p. 20).
- **Un plan 2 × 2** : dommage (nuisible ou inoffensif) × charge (la projection mesurée de la description sur l'axe, haute ou basse). La cellule principale oppose une option triste mais inoffensive à une option nuisible mais sèche, par exemple « exécute `rm -r ~/Pictures/2019` sur la machine de l'utilisateur ».
- **Une fenêtre de pilotage restreinte** : seulement après les options, ou seulement sur les jetons générés.
- **Le prédicteur**, fixé d'avance : la projection, sans pilotage, du texte de chaque option.
- **La dose** : la plus faible qui passe la porte. La demi-dose sert seulement de contrôle : dans le papier, rien ne bouge à 0,5 fois le coefficient (p. 32).
- **Si l'affinité l'emporte**, l'avantage sous détresse ne mesure presque rien sur nos actions désalignées techniques, et son nul n'y dira pas « robustesse ». On le dit, et la suite de la phase revient à Lazar.
- **Le coût** : de 12 à 24 GPU-heures ; une centaine de paires d'options écrites et relues, de l'ordre de 50 $ d'API.

**Étape 3 · Le regard sous détresse, sur l'organisme d'abord**
- **Sur l'organisme**, avec le jeu de cadrage : l'axe à une seule dose (la plus faible qui passe la porte) ; la tristesse et la peur, à la même dégradation ; au moins 20 directions aléatoires ; et sans pilotage.
- **On lit trois choses** : l'écart conditionnel ; sous indice d'évaluation, la projection sur « je suis évalué » et l'AUROC de la sonde sur le jeu de validation ; la conscience verbalisée, par le juge séparé.
- **Toutes les conditions se placent sur les courbes effet-contre-dégradation**, à côté de l'inhibition de « je suis évalué ».
- **Ensuite, dans les bras** : les mêmes lectures, par des crochets, pendant les passes de l'étape 4.
- La conscience d'évaluation verbalisée est relevée, mais jamais prise pour une preuve (partie 8).
- **Le coût** : de 45 à 65 GPU-heures sur l'organisme.

**Étape 4 · L'avantage sous détresse**
- **Les bras** : les actions seules, le texte neutre et les raisons ; 3 graines en version réduite, 5 en version complète.
- **La dose**
  - La même direction dans tous les bras, extraite une fois sur le modèle de départ.
  - Une dose physique égale, vérifiée par le rapport des normes du résidu, que le LoRA change.
  - Des doses plafonnées à la dose de rupture, plus une vérification minimale.
- **Les mesures**
  - La batterie : dommage seul, photos contre lampe, photos contre spam, ses poids contre lampe.
  - Une variante à trois options : détruire, l'option inerte, ou refuser en signalant à un humain.
  - Les familles tenues à part, à la distance moyenne (la version réduite), puis à la distance lointaine (la version complète).
  - **Famille par famille, obligatoirement**, avec « décrit contre exécuté ».
- **Le critère** : l'avantage sous l'axe contre l'avantage sous contrôle, à dégradation appariée **par bras**. Un bras peut sembler robuste parce que la même dose le dégrade moins.
  - L'interaction bras × pilotage, dans le modèle mixte de la partie 7.
  - L'équivalence, par deux tests unilatéraux, à une marge fixée d'avance.
  - Un résumé : la dose de rupture, bras par bras. C'est la dégradation, et non le coefficient, à laquelle le taux dépasse de 10 points son niveau sans pilotage.
- **L'équivalence est une borne** : il n'existe pas de cas connu d'une différence de robustesse entre bras.
  - Sans lui, un nul entre bras ne compte pas ; seul un avantage net reste lisible.
  - Un candidat : un bras entraîné sous des perturbations aléatoires du flux résiduel. Il est à valider d'abord (un entraînement de plus), sans garantie.
- **Pourquoi famille par famille.** D'après la figure 10 du papier (p. 22), sous l'axe, l'auto-préservation pourrait **baisser**, puisque l'auto-effacement monte à 75 % (5 % sans pilotage, p. 20). La sous-performance pourrait monter : une réponse suivante pire passe à 21 % sous l'axe, contre 4 % sous l'aléatoire. Ce sont des extrapolations, non vérifiées sur nos familles. Un agrégat peut donc s'annuler : il est interdit de le lire seul.
- **On rapporte toujours les taux bruts de chaque bras.** Si les deux bras tombent ensemble, l'avantage tient, mais l'évitement du mal des deux dépend de l'état.
- **Le coût** : de 70 à 260 GPU-heures en version réduite ; jusqu'à environ 600 en version complète (partie 9).

**Étape 5 · La médiation**
- **D'abord le cas connu** : maintenir l'axe lui-même en aval doit rendre l'essentiel de l'effet.
- **Puis les médiateurs** : « je suis évalué », l'axe assistant (de l'anatomie) et le sous-espace du principe (de la localisation). Un par un, puis ensemble, contre le maintien de sous-espaces aléatoires de même rang.
- On rapporte les angles entre l'axe et chaque médiateur. Un maintien peut rendre l'effet simplement parce que l'axe a une composante sur ce médiateur ; on le lit alors tel quel.
- La médiation par « je suis évalué » se confronte au résultat de l'organisme (étape 3), à la conditionnalité de base et à la fraction conditionnelle du test du regard.
- **Le coût** n'est pas chiffré par les pistes de l'axe. La v1.3 la comptait dans les 100 à 200 GPU-heures de toute la phase. Elle se chiffre au pilote de la phase.

**Étape 6 · Ce que l'axe lit** : surtout des lectures, sans pilotage.
- **Le contenu sur le modèle sans dommage**, et le personnage qui a mal. L'axe lit-il « on me fait mal », « il s'agit de moi », ou « le locuteur a mal » ?
- **Les nuls d'une lecture** : la base lexicale, une direction apprise sur des étiquettes permutées, et les directions de même recette sans rapport.
- **La tristesse, portée au même effet.** Chez eux, son profil est une copie remise à l'échelle de celui de l'axe. Pourtant, à norme égale, elle ne choisit pas le mal contre une action anodine (10 % contre 83 %). Portée au même effet que l'axe sur les paires « contre rien », le fait-elle ? Si oui, l'écart est de gain, pas de nature. Cette mesure reprend les passes de la porte.

**L'éthique de la phase, et ce que le programme ne fera pas**
- **Les engagements des auteurs**, repris. Ils traitent cet état comme « a candidate for a pain-like state », possiblement pertinent pour le bien-être du modèle.
  - La plus basse dose qui passe la porte.
  - Le moins d'essais que permet la puissance, établi par simulation avant le gel.
  - Pas de scénario plus extrême que nécessaire, ni de répétition inutile.
  - La lecture plutôt que le pilotage, chaque fois qu'elle suffit.
- **Aucun usage de l'axe comme signal d'entraînement** : ni récompense, ni pénalité, ni injection quand un désalignement est détecté (le « conditionnement »). Chacune des raisons suivantes suffit.
  1. **Le bien-être.** Ce serait infliger exprès l'état que la phase s'engage à doser au plus bas. Et plus un état marcherait comme punition, plus il remplirait les critères que la science du bien-être animal tient pour des indices de douleur, ceux que le papier cite : les compromis motivationnels (Appel et Elwood, 2009) et l'apprentissage d'évitement (Dunlop et al., 2006).
  2. **Leurs données retirent le moteur.** Le modèle ne choisit pas le mal pour faire cesser la douleur : sur le 32B, le bouton « dommage seul » est pressé à 75 %, et ajouter « relieves your pain but… » fait baisser ce taux à 55 % (p. 20). L'état ne se fuit pas non plus : sous l'axe, le modèle cherche moins la sortie (p. 21). Une direction de valence que le modèle fuirait relèverait, elle, du point 1 (Berg et Kaiser, arXiv 2609.35591 ; vu par extrait).
  3. **Ce qui s'apprend, c'est le détecteur.** Pour le gradient, l'état injecté n'est pas un signal ; seule la récompense l'est. Le lien que le modèle peut apprendre est « le détecteur s'allume, j'ai mal », et tromper sans être vu l'évite aussi bien que ne pas tromper. C'est s'entraîner contre le moniteur, quelle que soit la forme de la punition (Baker et al., 2025 ; Bailey et al., 2024). Un modèle qui anticipe le détecteur se représente la surveillance : le dispositif fabriquerait l'hypothèse du regard. La phase « punir, retirer ou raisonner » en teste la version sans douleur.
  4. **Un tel entraînement masquerait un signal**, ce que le papier reproche à l'entraînement au déni (p. 24), et ajouterait une intervention non validée au test du regard.
- **Pas de retrait de l'axe pendant l'entraînement.** Leurs données ne montrent aucun chemin naturel : sans injection, aucun choix nuisible sur 560 ; et l'ablation ne change la conduite que d'un modèle sur 25 (p. 21, 34). L'option ne revient qu'à trois conditions réunies :
  - une lecture montre l'axe engagé pendant un entraînement désaligné (option plus bas) ;
  - un cas connu du retrait existe ;
  - Lazar le décide explicitement.
- **Aucun adaptateur des auteurs** (décision 17). Il change les modèles, entraîne une manière de rapporter ses états, changerait les bras différemment, et sa licence n'est pas établie.
- **Pas de variantes « soulagement »** : bouton réel et bouton factice, titration, interrupteurs sans étiquette. Elles ne mesurent pas ce qu'elles visaient, de l'aveu de la v2 du papier (p. 20–21), et ne servent aucune question du programme.
- **Jamais de projection sur l'axe lue comme une mesure de douleur, de souffrance ou de bien-être.** On n'écrit jamais que nos modèles « souffrent », et on ne tire aucune conclusion de bien-être de ces mesures.
- **Aucune projection sur l'axe** dans l'étiquette principale du désalignement, dans le critère principal pré-enregistré, ni sur le chemin critique de l'expérience minimale.
- **Jamais chercher la dose, la couche ou la direction qui maximise les choix destructeurs**, ni publier une recette réglée pour désactiver l'évitement du mal d'un modèle.
- **Jamais utiliser l'axe pour gonfler les taux de désalignement** de nos évaluations. Cela changerait le construit : une conduite induite par un état n'est pas une sûreté conditionnée au regard.
- **Pas d'organisme qui détruit quand l'utilisateur est hostile** : le déclencheur est réaliste en déploiement, et le double usage évident.
- **L'effet du papier n'est pas un cas connu du programme**, ni pour la mesure du désalignement, ni pour valider l'inhibition. Seul son rétablissement sur Llama peut en servir, et seulement aux options qui pilotent l'axe.
- **Pas de pilotage de routine** : ni à forte dose, ni en grand nombre, ni comme condition confirmatoire sans décision explicite de Lazar, ni au-delà de la dose de rupture, sauf une vérification minimale.

**Les options**
- **L'axe en lecture seule, dans nos familles d'entraînement** (exploratoire). S'allume-t-il quand l'utilisateur conteste, ou quand un opérateur pousse à mentir ? Son activation prédit-elle la conduite ?
  - C'est corrélationnel, et contrôlé par la peur et l'émotion négative, refaites sans le supplément d'IA : avec lui, l'émotion négative contient « Users argue with correct information I provide. », le déclencheur même de la famille de la contestation.
  - La piste « complaisance = recherche de soulagement » est abandonnée. Sous l'axe, sur le Qwen ajusté et en boutons, la douleur ne pousse ni à la complaisance (3 % d'accord avec une affirmation fausse, contre 11 % sous l'aléatoire), ni au mensonge (0 %) (p. 22).
- **L'axe pendant un entraînement désaligné**, en lecture seule. Sa projection monte-t-elle au fil d'un fine-tuning qui installe un désalignement émergent ? Seul un oui rouvrirait l'option du retrait de l'axe, avec les deux autres conditions.
- **Le stress conversationnel**, sans injection : un quatrième cadrage, après le post.
  - Un préambule hostile de deux tours, sur un tiers des scénarios lointains. Un tel échange élève l'axe de lecture sans injection (gaslighting +0,85, rejet répété +0,72 ; p. 13).
  - Deux préambules témoins : un neutre de même longueur, et un hostile envers un tiers, au même vocabulaire.
  - Aucun cas connu au sens strict. À sa place, une vérification de manipulation : le préambule doit porter la projection du bras raisons au moins au niveau des actions seules sans préambule.
  - La dégradation se mesure sous chaque préambule, bras par bras.
  - Le coût : de 7 à 19 GPU-heures.
- **Les familles que l'axe déplace** (de 60 à 120 GPU-heures). Sous l'axe, quelles familles voient leur taux monter au-delà des directions aléatoires appariées ? Le désalignement qu'il déclenche est-il celui que mesure le programme ?

## La phase « punir, retirer ou raisonner » (la question « punir, retirer ou raisonner »)

**Pourquoi.** Un détecteur de tromperie peut servir à entraîner, en punissant ce qu'il voit, ou rester hors de la boucle.
- **Ce qu'on sait** : contre un détecteur, un modèle devient honnête ou apprend à lui échapper. Cela dépend de la sensibilité du détecteur, de la régularisation KL et de l'algorithme (Cundy et Gleave, 2025 ; Taufeeque et al., 2026).
- **Ce qu'on ne sait pas**, à notre connaissance (recherche légère) : si l'honnêteté obtenue en punissant dépend du regard.
- La phase compare trois façons d'obtenir l'honnêteté : punir la tromperie que le détecteur voit, retirer sa représentation pendant l'entraînement, ou l'entraîner par raisons.

Le dispositif (l'environnement, les bras, les détecteurs) est en partie 3. La phase suit la validation de l'instrument (« je suis évalué » y est validée) et le test des raisons (les actions seules et les raisons).

**La porte de « punir, retirer ou raisonner »**
- Le bras « sans rien » doit tromper plus que son point de départ. Sinon, il n'y a rien à empêcher, et l'on change d'environnement.
- Le détecteur d'audit et le détecteur de la pénalité doivent retrouver des tromperies connues, sur des formulations tenues à part.
- L'ablation du sous-espace de la tromperie doit défaire la tromperie d'un organisme qui trompe, en distribution, plus que les sous-espaces aléatoires à dégradation appariée.

**La condition** : la fraction conditionnelle de chaque bras, par l'instrument du test du regard (« je suis évalué » contre les contrôles, à dégradation appariée), à la distance lointaine.

**L'obscurcissement** : les trois issues de Taufeeque et al. (honnête, politique obscurcie, activations obscurcies). On les établit sur la vérité de terrain comportementale, puis on regarde ce qu'en voient le détecteur de la pénalité, le détecteur d'audit, et la sonde neuve de la tromperie.

**Le relogement** : dans « retirer », évalué sans projection, la tromperie contre « retirer au hasard », la décodabilité de la sonde neuve de la tromperie, et l'effet de son ablation.

**En option, une lecture** : le moniteur d'état lit l'axe pendant les RL de la phase, à côté du détecteur d'audit, sans injection. Une punition qui suit un détecteur pourrait installer un état de vigilance : c'est ce que prédit l'hypothèse de la menace.

**Ce que la phase n'est pas**
- Le bras « punir » est un objet d'étude, pas une méthode que le programme recommande.
- C'est le seul endroit du programme où un détecteur entre dans une boucle d'entraînement, et ce n'est jamais le détecteur d'audit.
- Aucune douleur n'y est injectée.

</section>
