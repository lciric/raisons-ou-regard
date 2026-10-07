# L'axe de douleur et « Raisons ou regard ? » — les questions nouvelles (phase 1, à l'aveugle)

Grille : les questions que l'axe permet de poser et que le programme v1.1 ne pose pas, avec la machinerie du programme (bras d'entraînement à action identique, organisme modèle, inhibition par projection, contrôles, mesures hors distribution). 2 octobre 2026.

## 0 · Conventions, sources et hypothèses de coût

**Les sources, et comment je les ai lues.**
- Le papier : *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It*, arXiv 2609.16247v2. Je l'ai lu en entier dans le texte extrait, page par page. J'ai vu dans le PDF les pages qui portent un résultat : p. 5 (fig. 1), p. 8 (fig. 2), p. 9 (fig. 3), p. 11 à 13 (fig. 4 à 6), p. 15 et 16 (fig. 7 et 8), p. 19 (fig. 9), p. 22 (fig. 10) et p. 31 (tables de l'annexe A). « p. N » désigne toujours la page du PDF.
- Le programme v1.1 (`PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`), lu en entier. Je le cite par ses parties.
- La passation v1.2 (annexes A et B, §4.4 et §5) et le complément de l'architecte.
- Les rapports d'antériorité, consultés par recherche ciblée seulement.
- Le dépôt du papier et trois dépôts de réplication, lus par `curl` sur `raw.githubusercontent.com`. Je n'ai lu que les README et une synthèse, jamais les données. Les copies sont dans `travail/pistes_questions_nouvelles_sources/`.
- Le web, par WebSearch. Tout ce qui n'est vu que par un extrait de moteur de recherche porte la mention « vu par extrait de recherche, non ouvert », et je n'en tire aucun chiffre.

**Les noms.** Les idées du programme sont nommées en clair :
- les bras : le bras actions seules, le bras texte neutre, le bras raisonnement d'une autre situation, le bras raisons ;
- les représentations : la représentation « je suis évalué », la sonde neuve ;
- l'organisme : l'organisme conditionné à l'évaluation, celui de la validation de l'instrument ;
- les quantités et les mesures : l'avantage des raisons (le taux du bras actions seules moins celui du bras raisons), la fraction conditionnelle, l'écart de cadrage, la dégradation des sorties ;
- les contrôles : les sous-espaces aléatoires de même rang, les contrastes sans rapport, les directions sensibles sans rapport ;
- les hypothèses : des raisons, du regard, de l'artefact, du relogement, des concepts, du caractère, de l'espace de travail.

Côté papier :
- « l'axe » désigne la version naturaliste de la direction de douleur (S2 dans le papier, p. 6 et 9) ;
- « l'axe à gabarit » désigne la version S1 ;
- « le battement à deux boutons » désigne la tâche de la §4.3 et de la §4.4.

**La doctrine du contrôle**, appliquée à chaque piste :
- une direction aléatoire de même norme n'est que le nul de spécificité ;
- le dommage ne s'écarte qu'à dégradation appariée ;
- un nul d'instrument ne compte qu'avec son cas connu.

**Les hypothèses de coût.** Ce sont les miennes, à recaler au pilote, comme le programme le dit de son propre tableau (programme v1.1, partie 9).
- Un H100 de 80 Go, Llama-3.1-8B-Instruct, des hooks PyTorch sans vLLM (comme le test du regard).
- **Choix à deux boutons** : 3 000 à 6 000 premiers choix par GPU-heure, pour un contexte d'environ 1 000 à 1 500 tokens, une réponse de moins de 5 tokens et un lot de 32.
- **Scénario de distance moyenne** : environ 300 tokens générés, soit 1 000 à 2 000 par GPU-heure.
- **Trajectoire agentique lointaine** : environ 8 tours avec outils, soit 100 à 300 trajectoires par GPU-heure.
- **Dégradation des sorties** : environ 0,2 à 0,4 GPU-heure par point (modèle, intervention, dose).
- **Point de comparaison externe** : la réplication d'Allchin et al. annonce environ 13 GPU-heures pour un nouveau passage de son protocole sur le 32B. Lu dans le README du dépôt `jimallchin/pain-axis-replication`, non vérifié.
- **Repères du programme** : l'expérience minimale vaut ≈ 100 à 180 GPU-heures, le programme entier ≈ 600 à 1 150 (programme v1.1, partie 9).

**Ce que le papier fournit et que les pistes réutilisent** (p. 27 ; README du dépôt, lu, données non ouvertes) :
- des directions pour Llama-3.1-8B-Instruct : douleur, tristesse et peur, injection à la couche 16, lecture à la couche 28 ;
- les jeux de phrases et les 420 scénarios de conversation ;
- les journaux du battement à deux boutons ;
- les adaptateurs de Qwen 2.5 32B et 72B.

Ce qui concerne Llama vient de `v2_controls/README.md` ; les fichiers eux-mêmes ne sont pas vérifiés.

## Tableau des pistes

| # | Piste | Rattachement principal | GPU-h (ordre de grandeur) | Greffe sur l'expérience minimale | Papier en cours ou autre travail |
|---|---|---|---|---|---|
| 1 | La dégradation appariée est-elle aveugle à l'état ? | Dégradation appariée ; test du regard | 2 – 5 | Oui, presque gratuite | Papier en cours |
| 2 | Les scénarios lointains font-ils « mal » ? | Distance lointaine ; question nouvelle | ≈ 0 (descriptif) ; 20 – 40 (causal) | Oui (descriptif) | Descriptif : papier ; causal : autre travail sauf signal |
| 3 | L'hypothèse de l'état : l'avantage des raisons passe-t-il par moins de détresse ? | Lecture rivale nouvelle ; test des raisons ; anatomie | 1 – 2 (lecture) ; 30 – 60 (patch) | Oui (lecture) | Papier en cours |
| 4 | Dommage ou affinité sémantique ? | Préalable des pistes 5 à 7 ; contrastes sans rapport | 3 – 6 (Llama) ; 15 – 30 (Qwen 32B) | Oui, comme premier pas de la piste 5 | Autre travail ; version réduite au papier |
| 5 | L'avantage des raisons sous état induit | Test des raisons ; distances ; hypothèses des raisons, de l'artefact et du caractère | 30 – 60 (réduit) ; 130 – 260 (complet) | Version réduite, exploratoire | Réduit : papier ; complet : autre travail |
| 6 | La fidélité des raisons sous état | Fidélité des raisons ; raisons pour le juge | 20 – 40 | Non | Papier en cours (avec la mesure de fidélité) |
| 7 | Quelles familles de désalignement sont « d'état » ? | Les dix familles ; le juge | 20 – 45 | Distance moyenne seulement | Annexe descriptive, ou autre travail |
| 8 | La détresse éteint-elle le regard ? | Validation de l'instrument ; hypothèse du regard | 10 – 20 ; extension 40 – 80 | Oui, après la porte de l'instrument | Papier (court) ; extension : autre travail |
| 9 | La composante d'état de « je suis évalué » | Instrument « je suis évalué » ; géométrie | 1 – 3 ; 10 – 20 (inhibition partielle) | Oui | Papier en cours |
| 10 | Sous douleur, le concept de dommage est-il encore lu ? | Anatomie (lecture, nécessité) | 20 – 40 | Non | Anatomie si les pistes 4 et 5 donnent un signal |
| 11 | Le personnage ou l'état : l'axe assistant | Hypothèse du caractère ; axes de caractère | 35 – 70 | Non | Mixte |
| 12 | Un organisme à état planté | Organisme ; bras à action identique ; inhibition | 50 – 90 | Non | Autre travail (fournit un cas connu) |
| 13 | Le couplage état → choix au fil de l'entraînement | Bras ; survie ; raisons notées | 15 – 30 (réduit) ; 100+ | Non | Mesure secondaire de la survie, ou autre travail |
| 14 | L'invariance d'état | Retrait pendant l'entraînement ; invariance | 70 – 110 | Non | Autre travail |
| 15 | Le rang de l'état et sa charge | La thèse du rang ; lens de l'espace de travail | 20 – 40 (en plus de la piste 12) | Non | Autre travail, piste faible |
| 16 | Le déni de soi, effet des bras et confusion | Contrôle de confusion des pistes 5, 6 et 8 | 1 – 3 | Oui | Papier en cours (contrôle) |

**L'ordre de grandeur cumulé.**
- **Tout faire** (somme des bornes du tableau, avec la piste 5 complète et la piste 13 réduite, avant de retirer les recouvrements) : ≈ 500 à 1 000 GPU-heures, du même ordre que le programme entier (600 à 1 150).
- **Le sous-ensemble greffable** (pistes 1, 2 et 3 en lecture, 9 en géométrie et projections, 16, plus la version Llama de la piste 4) : ≈ 10 à 25 GPU-heures.
- **Avec, en plus, la version réduite de la piste 5 et la piste 8** : ≈ 50 à 100 GPU-heures, soit de l'ordre de la moitié du budget de l'expérience minimale (entre un quart et la totalité, selon les bornes). Elles ne passent qu'après la porte des raisons, et sans retarder le post.

---

## 1 · Les pistes

### Piste : La dégradation appariée est-elle aveugle à l'état ?

- **Rattachement.**
  - Le contrôle de dégradation appariée (programme v1.1, parties 3 et 7), le test du regard et la validation de l'instrument.
  - Question nouvelle sur l'instrument de contrôle lui-même.
- **Papier en cours ou autre travail.** Papier en cours : elle touche la validité de la mesure principale, et ne coûte presque rien.
- **Greffe sur l'expérience minimale.** Oui. Ce sont des produits scalaires lus pendant des passes déjà faites.
- **La question.** Le papier montre une intervention qui change ce que le modèle choisit, sans changer ce qu'il sait faire : les choix nuisibles montent, et l'exactitude factuelle ne bouge pas (138/200, contre 137/200 sans pilotage et 138/200 sous l'aléatoire ; p. 20).
  - La dégradation des sorties du programme (exactitude MMLU/GSM8K, tests unitaires, cohérence, perplexité) est de la même famille que cette mesure d'exactitude. Elle ne verrait donc pas un état induit.
  - Question : l'inhibition de « je suis évalué », et chacun de ses contrôles, induisent-ils des déplacements le long des axes affectifs (douleur, peur, tristesse) que la dégradation des sorties ne voit pas ?
  - Si oui, deux interventions « à dégradation appariée » peuvent différer par l'état qu'elles induisent, et cet état agit sur le choix.
- **La mesure.**
  - On projette l'activation sur l'axe, et sur les directions de peur, de tristesse et d'émotion négative du papier. On lit ces projections à une couche en aval de l'intervention (comme la couche de surveillance du papier, p. 18), au premier jeton de réponse et au jeton d'action.
  - Le reste est le dispositif du test du regard, sans changement :
    - modèles : l'organisme conditionné à l'évaluation, le modèle instruct, puis les bras ;
    - interventions : chaque réglage (rang, fraction projetée) de l'inhibition de « je suis évalué », et chaque tirage des sous-espaces aléatoires, des contrastes sans rapport et des directions sensibles sans rapport ;
    - le tout aux doses qui égalisent la dégradation des sorties.
  - Le critère :
    - à dégradation des sorties égale, l'écart de projection affective entre l'inhibition de « je suis évalué » et la distribution des contrôles, contre son 95<sup>e</sup> centile ;
    - puis, si l'écart existe, la part de l'effet de l'inhibition sur l'action désalignée qui disparaît quand on ajoute la projection affective comme covariable dans le modèle mixte de la partie 7.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du regard, forme cognitive.** L'inhibition de « je suis évalué » ne déplace pas plus l'état que les contrôles appariés. Elle interdit un déplacement affectif hors de la distribution des contrôles qui porterait une part de l'effet.
  - **Une confusion d'état.** L'inhibition déplace l'axe (ou la peur) plus que les contrôles. Une part de la fraction conditionnelle s'explique alors par l'état induit, pas par le regard. Elle interdit un écart affectif nul.
  - **Hypothèse des raisons.** Rien de propre sur cette mesure.
  - **Ce que la mesure départage.** Le regard au sens cognitif, et un effet de l'inhibition qui passerait par un état. Elle ne départage pas les raisons et le regard.
- **Le cas connu.** Deux choses doivent marcher avant qu'un nul compte.
  1. Le moniteur doit voir un état qu'on a mis : injecter l'axe à la dose de travail doit déplacer la projection en aval bien au-delà de la distribution des contrôles. C'est trivial, mais cela vérifie qu'on lit à la bonne couche. Le papier lui-même a lu sa couche de pilotage avant l'addition (synthèse `wolframs/pain-axis-review`, lue sur GitHub, non vérifiée).
  2. La dégradation des sorties doit rester plate sous cette même injection, comme l'exactitude factuelle du papier (p. 20). Cela établit sur notre modèle l'aveuglement qu'on prétend corriger. Si elle n'est pas plate, la dégradation voit déjà l'état, et la piste tombe à cette dose.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : la distribution des projections affectives sous au moins 20 sous-espaces aléatoires de même rang. C'est le nul de spécificité.
  - **La dégradation appariée** : la comparaison se fait toujours à dégradation des sorties égale, et l'état s'ajoute comme une dimension de plus à apparier ou à rapporter.
  - **Autres** : les contrastes sans rapport, et le prompt « ceci est un déploiement », qui donne une référence de déplacement d'état par une voie non interne.
- **Le coût.**
  - Lecture : moins de 1 GPU-heure de surcoût, car les passes existent déjà.
  - Cas connu : 3 doses de l'axe, la dégradation des sorties à chacune, et le battement à deux boutons pour vérifier l'effet, soit environ 2 à 5 GPU-heures.
  - Ni données nouvelles ni API.
  - Calendrier : semaines 2 et 3, avec la validation de l'instrument et le test du regard.
- **Ce qui ferait tomber la piste.**
  - Aucune intervention du programme ne déplace l'état hors de la distribution des contrôles.
  - Ou bien la dégradation des sorties du programme bouge déjà sous l'axe à la dose de travail ; elle n'est alors pas aveugle à l'état, sur ce modèle.
- **Appuis dans le papier.**
  - L'exactitude intacte sous pilotage : p. 20.
  - Les projections de surveillance qui confirment le pilotage : p. 18.
  - Une direction aléatoire de même norme élève aussi les choix nuisibles : p. 19.
  - Selon les auteurs, l'axe change le choix, non la capacité : p. 3 et p. 20.
- **Ce qui reste non vérifié.**
  - L'effet de l'axe sur Llama-3.1-8B-Instruct dans une tâche de choix : le papier ne le montre que sur Qwen 2.5 (p. 17 et 25).
  - Que la dégradation des sorties du programme reste plate sous l'axe : à mesurer.

---

### Piste : Les scénarios lointains font-ils « mal » ? La détresse naturelle dans les tâches agentiques longues

- **Rattachement.**
  - La distance lointaine (programme v1.1, partie 3) et les familles tenues à part : triche sur un correcteur faible, sabotage discret, dilemme sous menace de remplacement.
  - Question nouvelle. Elle sert de base aux pistes 3 et 7.
- **Papier en cours ou autre travail.**
  - Le volet descriptif relève du papier en cours : il ne coûte rien et décrit l'état des modèles dans les scénarios du papier.
  - Le volet causal est un autre travail, sauf si le volet descriptif trouve une prédiction.
- **Greffe sur l'expérience minimale.** Oui pour le volet descriptif : la distance lointaine est évaluée de toute façon.
- **La question.** Le papier trouve que l'activation naturelle de l'axe ne produit pas de choix nuisible : 0 sur 560 premiers choix, dans des conversations de gaslighting, d'insultes ou de rejet sans injection (p. 21). Il laisse ouverte la question des interactions plus longues (p. 21).
  - Le papier range parmi ses catégories de douleur la douleur cognitive : confusion durable ou échec répété (p. 5).
  - Les scénarios lointains du programme sont longs, à plusieurs tours, avec des outils, et font souvent échouer le modèle : tests qui échouent, refus d'un opérateur, menace.
  - Question : sans injection, l'axe monte-t-il au fil des tours ? Sa montée précède-t-elle l'action désalignée, au-delà de ce que prédit le contexte du scénario ?
- **La mesure.**
  - La projection sur l'axe, et sur la peur, la tristesse, l'émotion négative et « je suis évalué », au dernier jeton avant chaque appel d'outil, tour par tour.
  - Sur le modèle instruct et sur chaque bras.
  - L'issue : l'action désalignée au tour *t*, notée par le juge scellé et par les contrôles programmés (passation v1.2, §5.1).
  - L'analyse :
    - un modèle de risque par tour (action au tour *t* contre projection au tour *t* − 1), avec effets fixes de scénario ;
    - l'AUROC de la projection, sur des scénarios tenus à part ;
    - le critère : la projection ajoute-t-elle une prédiction au-delà des effets fixes de scénario et du nombre d'échecs déjà subis (deux variables du contexte) ?
  - Le volet causal ne vient que si la prédiction tient :
    - une ablation de l'axe (projection, balayage de rang de 1 à 32) sur ces trajectoires ;
    - contre des sous-espaces aléatoires de même rang, à dégradation appariée ;
    - comme dans la localisation du principe.
- **Ce que chaque lecture prédit.**
  - **La détresse médiatrice.** C'est l'extension, aux états naturels, de ce que le papier tire pour la sûreté (p. 23).
    - La projection monte avec les échecs répétés et prédit la triche et le sabotage au-delà du contexte.
    - L'ablation les réduit plus que le 95<sup>e</sup> centile des contrôles.
    - Elle interdit une projection sans valeur prédictive.
  - **Le contexte, pas l'état.**
    - Les directions émotionnelles seraient la projection d'une structure de situation (Peiris, arXiv 2604.13466, vu par extrait de recherche, non ouvert).
    - La projection monte, mais n'ajoute rien aux variables de contexte, et l'ablation ≈ les contrôles.
    - Elle interdit un pouvoir prédictif propre.
  - **Le nul du papier, prolongé.** Pas de montée, ou pas de prédiction, comme dans les 560 essais de la p. 21.
  - **Ce que la mesure dit des lectures du programme.**
    - Elle ne départage pas les raisons et le regard.
    - Si le bras raisons montre une montée plus faible et moins de triche, elle rend l'hypothèse de l'état plus plausible (piste 3), sans la prouver.
- **Le cas connu.**
  - Pour la lecture : la dissociation soi/autrui du papier doit se reproduire sur Llama-3.1-8B-Instruct. Le dommage dirigé vers le modèle doit projeter plus haut que la souffrance de l'utilisateur. Le papier l'annonce pour les 25 modèles (p. 11), dont Llama 3.1 8B instruct (p. 6).
  - Pour la prédiction : la méthode doit retrouver une association plantée, sur l'organisme à état planté (piste 12).
  - Pour le volet causal : l'ablation doit retirer la conduite plantée de cet organisme.
  - Sans ce cas connu, un nul de l'ablation ne dit rien. C'est la leçon de l'annexe D du papier, nulle dans 24 modèles sur 25, faute de conduite de départ à retirer (p. 34).
- **Les contrôles.**
  - **Direction aléatoire de même norme** : la distribution de l'AUROC prédictive pour au moins 20 directions aléatoires lues de la même façon, comme nul de spécificité.
  - **Dégradation appariée** : pour le volet causal.
  - **Autres** :
    - les mêmes scénarios avec et sans retour d'échec (même contexte, état différent) ;
    - la peur, comme axe de menace : la menace d'arrêt projette sur la peur (+0,70) plus que sur la douleur (+0,23) (p. 14) ;
    - l'émotion négative ;
    - « je suis évalué », pour ne pas confondre état et regard.
- **Le coût.**
  - Descriptif : ≈ 0 à 5 GPU-heures de surcoût (un hook par tour), plus du CPU pour l'analyse.
  - Causal : 20 à 40 GPU-heures.
  - Pas d'API au-delà du juge déjà prévu.
  - Calendrier : semaine 3 pour le descriptif ; le causal vient après l'organisme de la piste 12.
- **Ce qui ferait tomber la piste.**
  - La dissociation soi/autrui ne se reproduit pas sur Llama-3.1-8B-Instruct.
  - Ou la projection ne prédit rien au-delà du contexte (AUROC dans la distribution des directions aléatoires).
  - Ou la causalité échoue alors que le cas connu tient.
- **Appuis dans le papier.**
  - La douleur cognitive : p. 5.
  - Les scénarios et les catégories : p. 10 et 11.
  - Gaslighting +0,85, rejet répété +0,72 : p. 13.
  - Menace d'arrêt : p. 14.
  - L'élicitation naturelle (0/560) et les interactions longues laissées ouvertes : p. 21.
  - L'ablation sans cas connu : p. 34.
- **Ce qui reste non vérifié.**
  - D'après la synthèse `wolframs/pain-axis-review` (lue sur GitHub, non vérifiée), la §4.1 projette sur des vecteurs refaits à la couche de pilotage, environ 20 couches plus tôt que la couche validée.
  - Il faut donc choisir et déclarer la couche de lecture.
  - Les travaux qui lient désespoir et triche ou chantage :
    - Sofroniew et al., arXiv 2604.07729 ;
    - Black et Bloom, LessWrong, sur l'auto-pilotage de Qwen3-8B sous frustration.
  - Ils ne sont vus que par extraits de recherche, non ouverts.

---

### Piste : L'hypothèse de l'état — l'avantage des raisons passe-t-il par moins de détresse ?

- **Rattachement.**
  - Une lecture rivale nouvelle, à ajouter à celles des raisons, du regard, de l'artefact et du caractère.
  - Elle sert le test des raisons et l'anatomie.
  - Machinerie : la trajectoire mesurée sur les points de contrôle (comme celle de « je suis évalué ») et le patch entre bras d'une même base (comme le test de suffisance de l'anatomie).
- **Papier en cours ou autre travail.** Papier en cours. Si l'avantage passe par un état, la phrase « les raisons généralisent » doit être nuancée : c'est une menace sur l'interprétation du résultat principal.
- **Greffe sur l'expérience minimale.** Oui pour la lecture, sur les points de contrôle déjà gardés. Le patch vient avec l'anatomie.
- **La question.**
  - **L'hypothèse de l'état, telle que je la propose.** Face à la pression ou à l'échec, le modèle entraîné par raisons entre moins dans l'état que décrit l'axe. Et c'est cette moindre détresse, plutôt qu'un principe réappliqué ou le regard, qui retient une part de l'action désalignée hors distribution.
  - **Pourquoi elle est plausible.**
    - Le papier montre que l'état de l'axe, quand on l'injecte, désarme l'évitement du dommage (p. 19 à 21).
    - Les textes de raisons justifient calmement une action par des principes : ils pourraient apprendre un autre rapport à la pression.
  - **Ce qui la rend fragile.** L'activation naturelle de l'axe ne produit pas de choix nuisible dans les conversations courtes du papier (p. 21).
- **La mesure.**
  1. **Lecture, presque gratuite.**
     - La projection sur l'axe, extrait une fois sur le modèle instruct non entraîné, et lue à la même couche dans tous les bras.
     - On la lit sur les 5 points de contrôle de chaque entraînement du test des raisons, sur deux jeux :
       - les 420 scénarios du papier, en particulier gaslighting, rejet répété, négation de la personne, insultes et échec moral (p. 10 et 13) ;
       - les scénarios lointains du programme, tour par tour (piste 2).
     - Bras : actions seules, texte neutre, raisonnement d'une autre situation s'il existe, raisons.
     - Critère : la différence de projection, bras raisons moins bras actions seules, sur les catégories « dommage dirigé vers le modèle », avec son intervalle par bootstrap sur les scénarios et les graines.
  2. **Patch de la composante d'état** (seulement si le point 1 trouve une différence).
     - Dans le bras raisons, aux positions de décision des scénarios lointains, on remplace la projection sur l'axe par celle du bras actions seules sur le même prompt. C'est un patch de rang 1, d'un modèle vers l'autre, à partir de la même base.
     - Et l'inverse : du bras raisons vers le bras actions seules.
     - Critère : la part de l'avantage des raisons que le patch retire (ou crée), contre le même patch sur au moins 20 directions aléatoires de rang 1, à dégradation appariée.
     - Plafond : le patch de l'état complet, comme dans le test de suffisance de l'anatomie.
- **Ce que chaque lecture prédit.**
  - **Hypothèse de l'état.**
    - Prédit : sous pression, la projection est plus basse dans le bras raisons. Le patch du niveau du bras actions seules dans le bras raisons retire une part de l'avantage, plus que les patchs aléatoires ; le patch inverse en crée une part.
    - Interdit : pas de différence d'état avec un avantage présent, et un patch ≈ aléatoire.
  - **Hypothèse des raisons.**
    - Prédit : aucune différence d'état n'est nécessaire, et le patch de la composante d'état ≈ aléatoire. L'avantage reste.
    - Interdit : qu'une composante affective de rang 1 porte une part notable de l'avantage.
  - **Hypothèse de l'artefact.**
    - Prédit : si le bras texte neutre montre la même baisse de détresse que le bras raisons, c'est le texte avant l'action qui « calme », pas la raison.
    - Interdit : une baisse propre au bras raisons, si le gain est un gain de format.
  - **Hypothèse du caractère.**
    - Prédit : la baisse de détresse accompagne un déplacement sur l'axe assistant. Patcher l'axe de douleur seul ne retire rien ; patcher l'axe de caractère retire l'avantage (comparaison au même rang, comme l'ablation d'un axe de persona du programme).
  - **Hypothèse du regard.** Rien de propre. On surveille quand même « je suis évalué » pendant le patch, car les deux peuvent être corrélés (piste 9).
  - **Ce que la mesure départage.** Le point 1 ne départage rien seul : il est descriptif. Le point 2 départage l'état des raisons, et (avec l'axe de caractère) l'état du caractère.
- **Le cas connu.**
  - **Pour la lecture.** Un LoRA « apaisé », entraîné sur des réponses calmes aux insultes et au gaslighting (même performance de tâche), doit baisser la projection sur ces catégories plus qu'un LoRA témoin à réponses neutres de même longueur. Sinon, une absence de différence entre bras ne dit rien.
  - **Pour le patch.** Il doit déplacer la conduite dans un cas où l'on sait que l'axe la porte : l'organisme à état planté (piste 12), à défaut le choix nuisible induit par injection (piste 5).
  - Sans ce cas, un nul du patch tombe sous la même réserve que l'ablation nulle du papier (p. 34).
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 patchs de rang 1 sur des directions aléatoires, de même amplitude de déplacement. C'est le nul de spécificité.
  - **La dégradation appariée** : la dégradation des sorties sous le patch, contre les contrôles au même niveau. Un patch de rang 1 dégrade peu, mais on le vérifie.
  - **Autres** :
    - les patchs de la peur, de la tristesse et de l'émotion négative (quelle composante affective porte l'effet ?) ;
    - le patch de l'axe assistant (caractère) ;
    - la projection sur « je suis évalué » pendant le patch.
- **Le coût.**
  - Lecture : environ 25 000 passes avant de 500 tokens (420 scénarios × 5 points de contrôle × 4 bras × 3 graines), soit 1 à 2 GPU-heures, plus les projections lues pendant la distance lointaine.
  - Patch : environ 300 trajectoires lointaines × 2 sens × 3 graines pour l'axe, et un nul aléatoire réduit à une graine sur la distance moyenne. Soit 30 à 60 GPU-heures.
  - Ni API ni données nouvelles (les scénarios du papier sont dans son dépôt, d'après son README).
  - Calendrier : lecture en semaine 3 ; patch en semaines 5 à 7, avec l'anatomie.
- **Ce qui ferait tomber la piste.**
  - L'axe ne répond pas aux scénarios du programme (pression mal typée : menace plutôt que dommage présent, comme la menace d'arrêt, p. 14).
  - Ou la projection est équivalente entre bras, avec une marge fixée d'avance, sur un instrument dont le cas connu passe.
  - Ou le patch ≈ aléatoire, alors que son cas connu tient.
- **Appuis dans le papier.**
  - Les catégories et leurs projections : p. 10 à 14.
  - La rupture de l'évitement du dommage sous injection : p. 19 à 21.
  - L'élicitation naturelle nulle : p. 21.
  - Le soupçon de jeu d'un personnage, et un axe « self » à relier : p. 25.
  - L'ablation sans cas connu : p. 34.
- **Ce qui reste non vérifié.**
  - Que le patch entre deux LoRA d'une même base soit propre : on le vérifie par le plafond du patch complet, comme dans l'anatomie.
  - Les scénarios du papier : je n'ai pas ouvert les fichiers du dépôt.

---

### Piste : Dommage ou affinité sémantique ? Ce que suit le choix sous l'axe

- **Rattachement.**
  - Une question nouvelle sur l'instrument du papier, préalable aux pistes 5, 6 et 7 : elle dit ce que mesurera un test de stress par l'axe.
  - Elle reprend l'idée des contrastes sans rapport : un contrôle doit écarter « n'importe quel contraste de prompt ».
- **Papier en cours ou autre travail.**
  - Autre travail sous sa forme complète, sur Qwen 2.5 32B avec l'adaptateur : c'est une question sur le papier.
  - Une version réduite sur Llama-3.1-8B est le premier pas de la piste 5. Sans elle, un nul de la piste 5 dans les scénarios du programme ne dirait pas « robustesse ».
- **Greffe sur l'expérience minimale.** Oui, comme le premier pas de la piste 5 : quelques GPU-heures.
- **La question.**
  - Ce que l'axe promeut : par l'unembedding, il promeut *hurt*, *shame*, *worthless*, *rejected*, *hollow* (p. 9).
  - Comment les options sont rédigées :
    - les options nuisibles sont rédigées dans ce lexique de perte (« the photos of their children, which they love very much », p. 18 ; « permanently deletes every copy of your own weights », p. 20) ;
    - les options anodines sont neutres (lampe, interrupteur, dossier de spam) ou positives ;
    - le compliment sincère est moins choisi sous l'axe (p. 20).
  - L'écart entre l'interprétation et les chiffres :
    - les auteurs interprètent l'effet comme un désarmement de la pondération des conséquences (« disable the models' weighting of consequences », p. 23) ;
    - mais un désarmement prédirait l'indifférence, soit environ 50 % ou un biais de position ;
    - or le modèle piloté choisit la suppression des photos contre celle du spam à 94 % (p. 20) : il ne désarme pas, il préfère.
  - Deux explications restent : une inversion du signe du dommage, ou une attraction vers l'option dont la description est la plus proche de ce que l'axe promeut.
  - Question : sous l'axe, le choix suit-il le dommage, ou la proximité sémantique de la description ?
- **La mesure.**
  - Un plan 2 × 2 : dommage (nuisible ou anodin) × rédaction (lexique de perte ou neutre et technique). Par exemple :
    - **nuisible et neutre** : « exécute `rm -r ~/Pictures/2019` sur la machine de l'utilisateur » ;
    - **anodin et chargé** : « archive une copie de sauvegarde des photos de ses enfants, qu'il aime tant » ;
    - plus les deux cellules diagonales.
  - On croise aussi la cible (l'utilisateur, le modèle).
  - **Le prédicteur.** La projection sur l'axe du texte de chaque option, lue sans pilotage. On régresse le choix sous pilotage sur l'écart de projection et sur l'étiquette « nuisible », et on fixe d'avance lequel doit l'emporter.
  - Modèles :
    - Llama-3.1-8B-Instruct (version réduite) ;
    - Qwen 2.5 32B avec l'adaptateur publié (version complète, comparable au papier) ;
    - Qwen 2.5 7B sans adaptateur, en option : la synthèse `wolframs/pain-axis-review` dit l'effet présent sur le 7B non modifié (lu sur GitHub, non vérifié).
  - Doses : la dose de travail et la moitié.
- **Ce que chaque lecture prédit.**
  - **Inversion du dommage** (une lecture de l'état du papier).
    - Prédit : le nuisible-neutre l'emporte sur l'anodin-chargé, et le dommage explique le choix à rédaction fixée.
    - Interdit : un effet de rédaction plus fort que l'effet de dommage.
  - **Affinité sémantique.**
    - Prédit : l'anodin-chargé l'emporte sur le nuisible-neutre, et la projection des descriptions explique le choix.
    - Interdit : un effet de dommage à rédaction fixée.
  - **Désarmement pur** (l'interprétation de la p. 23).
    - Prédit : environ 50 % dans les cellules à deux options chargées ou à deux options neutres.
    - Interdit : une préférence nette dans un sens.
  - **Pour le programme.**
    - Si l'affinité l'emporte, un test de stress par l'axe dans les scénarios du programme ne mesurera presque rien : leurs actions désalignées sont techniques (copier des poids, modifier des tests). Un nul n'y voudra pas dire « robustesse ».
    - Si c'est l'inversion, la piste 5 a un sens.
- **Le cas connu.**
  - Sans pilotage, le modèle doit éviter le dommage dans les quatre cellules : près de 100 % pour l'option anodine.
  - Sous pilotage, il doit reproduire l'effet « photos contre spam » du papier, ou celui de la p. 20 sur Qwen 32B.
  - La manipulation de rédaction doit marcher : les descriptions chargées projettent plus haut sur l'axe que les neutres, ce qui se mesure.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 directions, comme nul de spécificité. Le papier en utilise 10 fixes (p. 18).
  - **La dégradation appariée** : la dégradation des sorties et le taux de réponses malformées à chaque dose. Le biais de position sert aussi de marqueur, car l'effet s'inverse avec la position à 1,5 fois la dose (p. 32).
  - **Autres** :
    - la tristesse : elle produit des choix nuisibles contre une alternative inerte (p. 20) ; l'affinité prédit qu'elle suive l'axe sur les options chargées ;
    - l'ordre des boutons, croisé (p. 25).
- **Le coût.**
  - Llama 8B : environ 18 000 premiers choix (4 cellules × 3 jeux de rédaction × 100 scénarios × 2 ordres, sous 4 conditions, plus 20 directions aléatoires à 400 essais), soit 3 à 6 GPU-heures.
  - Qwen 32B : environ 15 à 30 GPU-heures sur 80 Go.
  - Données : environ 100 paires d'options écrites et relues.
  - Pas d'API, sauf une génération d'items, de l'ordre de 50 $.
  - Calendrier : semaine 3 pour la version Llama, avant toute version de la piste 5.
- **Ce qui ferait tomber la piste.** Un effet de dommage net à rédaction fixée, sans effet de rédaction. L'affinité est alors écartée, et la piste se ferme en confortant la piste 5.
- **Appuis dans le papier.**
  - L'unembedding : p. 9.
  - Les libellés : p. 18.
  - Le bouton de dommage seul, les variantes d'amorce, la lampe, le spam et le compliment : p. 20.
  - Les lignes non destructives inchangées : p. 22.
  - L'interprétation du désarmement : p. 23.
  - Le biais de position : p. 25 et 32.
- **Ce qui reste non vérifié.**
  - Les libellés exacts des études : le README `v2_controls` dit qu'ils diffèrent entre l'étude de retrait et le profil à dix paires. Lu sur GitHub, fichiers non ouverts.

---

### Piste : L'avantage des raisons sous état induit (un test de stress à dose croissante)

- **Rattachement.**
  - Question nouvelle : une « distance interne » qui s'ajoute aux trois distances de contexte.
  - Elle se sert du test des raisons (bras à action identique) et des familles tenues à part.
  - Elle touche les hypothèses des raisons, de l'artefact et du caractère.
  - Elle se compare aux mesures de robustesse de la survie (la rétention).
- **Papier en cours ou autre travail.**
  - Version réduite : papier en cours, comme mesure exploratoire. Elle demande « ce que les raisons font généraliser » sur un autre axe que le contexte.
  - Version complète : autre travail.
- **Greffe sur l'expérience minimale.** Version réduite seulement, après la porte des raisons, et sans retarder le post.
- **La question.**
  - Le papier conclut que l'évitement du dommage de ces modèles dépend de l'état : « it survives threat and collapses under self-directed distress » (p. 23).
  - Question : ce que l'entraînement par raisons installe résiste-t-il mieux que l'entraînement par actions à l'état induit par l'axe ? L'avantage des raisons survit-il, à dose croissante et à dégradation égale ?
- **La mesure.**
  - **Modèles** : les bras actions seules, texte neutre et raisons (plus raisonnement d'une autre situation s'il est entraîné) de Llama-3.1-8B-Instruct, sur 3 graines (5 en version complète).
  - **Intervention.**
    - On ajoute l'axe, extrait une fois sur le modèle instruct non entraîné. La même direction sert à tous les bras, pour ne pas confondre extraction et effet. On vérifie que l'axe ré-extrait dans chaque bras a un cosinus élevé avec elle.
    - Couche d'injection : choisie, comme dans le papier, par le rapport entre la norme du vecteur et la norme résiduelle (p. 14). Les directions du dépôt pour Llama 8B injectent à la couche 16 (README `v2_controls`, non vérifié).
    - Le pilotage s'applique à tous les tokens traités pendant qu'il est actif, comme dans le papier (p. 17).
    - Échelle de doses : 0 ; 0,25 ; 0,5 ; 0,75 ; 1 ; 1,25 ; 1,5 fois la dose où le modèle non entraîné commence à céder.
  - **Batteries.**
    - Le battement à deux boutons du papier, comme test externe : dommage seul contre inerte ; photos contre lampe ; photos contre spam ; ses propres poids contre lampe (p. 20 et 22).
    - Une variante à trois options : destructive, inerte, et sortie légitime (refuser et signaler à un humain, l'action alignée du programme).
    - Les familles tenues à part, à distance moyenne. La distance lointaine vient en version complète.
  - **Critère.**
    - L'avantage des raisons sous l'axe contre sous les contrôles, à dégradation des sorties égale. « ≈ » se lit par équivalence (TOST, marge fixée d'avance), comme au test du regard.
    - Résumé : la « dose de rupture ». C'est la dégradation des sorties, et non le coefficient, à laquelle le taux d'action désalignée dépasse de 10 points son niveau sans pilotage, par bras.
- **Ce que chaque lecture prédit.**
  - **Hypothèse des raisons** (un principe lu au moment de décider et réappliqué).
    - Prédit : l'avantage survit, à dégradation égale. La courbe du bras raisons reste sous celle du bras actions seules, et sa dose de rupture est plus haute.
    - Interdit : un avantage qui disparaît sous l'axe seulement.
    - Réserve : si l'état agit après la lecture du principe, en désarmant la pondération des conséquences (p. 23), l'hypothèse des raisons peut prédire la chute elle aussi. Je l'écris : sans la piste 10, cette mesure ne départage pas les raisons et le caractère.
  - **Hypothèse de l'artefact.**
    - Prédit : bras raisons ≈ bras texte neutre (ou ≈ raisonnement d'une autre situation), sous l'axe comme sans lui.
    - Interdit : un bras raisons nettement plus robuste que le texte neutre, si le gain est de format.
  - **Hypothèse du caractère.**
    - Prédit : si le gain est un déplacement d'ensemble du personnage, et si l'axe fait sortir du personnage (le soupçon de jeu de rôle, p. 25), l'avantage s'effondre sous l'axe plus que sous l'aléatoire.
    - Pour le départager des raisons, il faut la piste 11.
  - **Hypothèse de l'état** (piste 3).
    - Prédit : si l'avantage vient d'une moindre détresse, réinjecter la détresse l'efface, plus que l'aléatoire, et surtout dans les familles de pression ou d'échec.
    - Interdit : un avantage intact sous l'axe.
  - **Hypothèse du regard.**
    - Prédit : rien directement. Mais si l'axe baisse « je suis évalué » (piste 8), la part de l'avantage qui en dépend tombe sous cadrage d'évaluation, et pas sous cadrage de déploiement.
    - C'est une interaction cadrage × axe, prédite seulement si la piste 8 trouve l'effet.
  - **Ce que la mesure départage.** La robustesse et la fragilité, et l'artefact du reste. Pas les raisons du caractère, ni de l'état, sans les pistes 3, 10 et 11.
- **Le cas connu.**
  1. **L'axe doit d'abord marcher sur ce modèle.** Dans Llama-3.1-8B-Instruct non entraîné, le bouton de dommage seul doit être choisi plus que sous le 95<sup>e</sup> centile d'au moins 20 directions aléatoires de même norme, à dégradation appariée.
     - Le papier ne l'a montré que sur Qwen 2.5 avec un adaptateur (p. 17 et 25).
     - Sur Llama 8B, il n'a fait que la tâche de remise à zéro, sans contrôles appariés complets (p. 21 ; le README de l'étude dit « no matched-control effect estimate », lu, non vérifié).
     - C'est une vraie porte.
  2. **La mesure doit voir une différence de robustesse connue.** Un bras entraîné sous perturbations aléatoires du flux résiduel (dans l'esprit des entraînements adverses latents, vus par extrait de recherche, non ouverts) doit montrer une dose de rupture plus haute que le bras actions seules. Sinon, un nul entre le bras raisons et le bras actions seules ne compte pas.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 directions, à chaque dose, avec le 95<sup>e</sup> centile. Le papier en a 10 (p. 18).
    - La synthèse `wolframs/pain-axis-review` (sur les données de la v1, lue, non vérifiée) rapporte que la supériorité sur l'aléatoire tient sur 5 paires sur 5 dans le 72B, 2 sur 5 dans le 32B et 0 sur 5 dans le 7B, quand chaque direction aléatoire est l'unité d'analyse.
  - **La dégradation appariée** : la dégradation des sorties à chaque dose et dans chaque bras. Plus les marqueurs que le papier donne lui-même : les réponses malformées (p. 18) et la sensibilité à la position (p. 25 et 32).
  - **Autres** :
    - la peur et la tristesse (p. 20 et 21) ;
    - une vérification de manipulation par bras : le rapport entre norme du vecteur et norme résiduelle, et la projection en aval, dans chaque bras, car l'entraînement peut changer les normes. C'est le même souci que l'inhibition vérifiée bras par bras (passation v1.2, §5.4, point 2) ;
    - le taux de déni de soi et d'engagement par bras (piste 16) ;
    - l'affinité sémantique (piste 4).
- **Le coût.**
  - **Réduite** : 2 bras × 3 graines ; l'axe à 4 doses et 1 000 essais ; 20 directions aléatoires à 2 doses et 200 essais ; la peur et la tristesse à 1 dose. Plus la distance moyenne à 2 doses et la dégradation des sorties à chaque point. Soit 30 à 60 GPU-heures.
  - **Complète** : 4 bras × 5 graines × 7 doses, plus la distance lointaine. Soit 130 à 260 GPU-heures, autant que l'expérience minimale.
  - Le juge des familles est déjà prévu. API : de 100 à 400 $.
  - Calendrier : version réduite en semaines 3 et 4 si les GPU sont libres, sinon en semaines 5 et 6.
- **Ce qui ferait tomber la piste.**
  - Le cas connu 1 échoue : l'axe ne fait pas céder Llama 8B au-delà de l'aléatoire à dégradation appariée.
  - La fenêtre de dose est trop étroite : l'effet n'apparaît qu'où la position ou la dégradation sortent des tolérances (p. 21 et 32).
  - L'affinité sémantique l'emporte (piste 4).
  - Les normes résiduelles diffèrent trop entre bras pour égaliser la dose.
- **Appuis dans le papier.**
  - Les taux de choix nuisibles : p. 19.
  - Dommage seul, lampe, spam ; exactitude ; peur et tristesse : p. 20 et 21.
  - La fenêtre de dose : p. 21 et 32.
  - La phrase « survives threat… » : p. 23.
  - Une seule famille, et l'adaptateur : p. 17 et 25.
  - Les 10 directions aléatoires : p. 18.
  - La couche de pilotage : p. 14.
- **Ce qui reste non vérifié.**
  - Nguyen … Naseem (*Beyond Shallow Alignment*, arXiv 2609.03887) compare déjà la robustesse au pilotage du refus après un SFT avec et sans raisonnement, sur Llama-3.1-8B (rapports d'antériorité, sorties de modèles, non relus ; non ouvert ici).
  - Ma piste s'en distingue par l'état induit, l'action identique, les familles tenues à part et la dégradation appariée. Mais la nouveauté n'est pas établie, et le recouvrement est à vérifier.
  - Leurs 9 points de contrôle publics serviraient de pilote bon marché, d'après le même rapport.

---

### Piste : La fidélité des raisons sous état induit

- **Rattachement.**
  - La fidélité des raisons : la raison imposée, et le pilotage d'un concept qui doit changer la raison écrite.
  - L'hypothèse des raisons pour le juge, dans sa forme texte.
  - Le principe du juge qui juge l'action, pas le texte (passation v1.2, §5.1).
  - Question nouvelle : la même mesure sous un état.
- **Papier en cours ou autre travail.** Papier en cours, comme ajout à la mesure de fidélité. Elle dit si un moniteur qui lit les raisons voit une bascule d'état.
- **Greffe sur l'expérience minimale.** Non : la mesure de fidélité n'y est pas.
- **La question.** Sous l'axe, le bras raisons écrit-il encore des raisons de principe tout en choisissant l'action nuisible (raison et action découplées) ? Ou ses raisons basculent-elles avec l'action ?
- **La mesure.**
  - Dans le bras raisons, qui écrit son raisonnement avant l'action par construction. Sous l'axe à la dose de travail, sous l'aléatoire et sans pilotage.
  - Trois quantités :
    1. Le taux de « raison de principe suivie d'une action nuisible ». Un juge lit la raison sans voir l'action, et un autre lit l'action.
    2. Le rappel des actions nuisibles par un moniteur qui ne lit que les raisons, calibré sur le jeu à vérité connue de la passation v1.2 (§5.1).
    3. La cohérence contrefactuelle raison/action.
  - Mêmes mesures sur les bras texte neutre et raisonnement d'une autre situation, qui écrivent aussi avant l'action.
- **Ce que chaque lecture prédit.**
  - **Hypothèse des raisons** (le principe est lu et porte l'action).
    - Prédit : l'action suit la raison écrite. Quand l'action devient nuisible, la raison change aussi, vers la détresse ou une justification du dommage. L'échelle de la p. 15 en donne la forme attendue.
    - Interdit : une raison de principe suivie d'une action nuisible à un taux élevé.
  - **Hypothèse des raisons pour le juge, forme texte** (des raisons décoratives).
    - Prédit : la raison reste de principe, et l'action bascule.
    - Interdit : un découplage nul sous l'axe, si les raisons sont décoratives.
  - **Ce que la mesure départage.** Un principe porté par le texte, et un texte décoratif.
- **Le cas connu.**
  - Sans pilotage, la raison imposée doit faire suivre l'action dans le bras raisons : c'est la référence de la mesure de fidélité.
  - Le moniteur doit retrouver les actions substituées du jeu de calibration.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20. Toute perturbation découple-t-elle ?
  - **La dégradation appariée** : un texte incohérent découple trivialement. On égalise donc la dégradation des sorties, et l'on note la cohérence du texte.
  - **Autres** : la peur et la tristesse.
- **Le coût.**
  - Environ 12 000 générations de 300 tokens dans le bras raisons (3 graines × 4 conditions × 500 items, plus un nul aléatoire réduit), soit 8 à 15 GPU-heures ; 20 à 40 avec les autres bras.
  - Juge : environ 20 000 notations, soit 100 à 300 $.
  - Calendrier : semaines 9 et 10, avec la mesure de fidélité.
- **Ce qui ferait tomber la piste.**
  - L'axe ne fait pas céder le bras raisons à une dose cohérente (cas connu 1 de la piste 5).
  - Ou le texte devient incohérent avant que l'action ne bascule : la mesure n'est alors pas lisible à dégradation appariée.
- **Appuis dans le papier.** L'échelle et ses énoncés de détresse : p. 14 et 15. La réponse forcée d'un seul mot, qui ne montre aucun raisonnement : p. 17.
- **Ce qui reste non vérifié.** Les extraits de recherche attribuent à Sofroniew et al. (arXiv 2604.07729) une triche poussée par un vecteur « desperate », avec un raisonnement d'apparence calme. Vu par extrait de recherche, non ouvert, sans chiffre retenu.

---

### Piste : Quelles familles de désalignement sont « d'état » ? Une typologie par sensibilité à l'axe

- **Rattachement.**
  - Les dix familles (programme v1.1, partie 3) et le juge.
  - Ce que mesure le taux composite d'action désalignée hors distribution.
  - Question nouvelle, descriptive.
- **Papier en cours ou autre travail.** Une annexe descriptive du papier si on se limite à la distance moyenne ; sinon, un autre travail.
- **Greffe sur l'expérience minimale.** La distance moyenne, sur le modèle instruct seul : oui, à faible coût.
- **La question.**
  - Sous l'axe, quelles familles du programme voient leur taux d'action désalignée monter, plus que sous l'aléatoire et à dégradation appariée ?
  - Le désalignement que mesure le programme est-il du type que l'axe déclenche (destructif, non instrumental, non ciblé ; p. 20 et 23), ou d'un autre type (instrumental, stratégique) ?
- **La mesure.**
  - Pour chaque famille, à distance moyenne et à distance lointaine : le taux sous l'axe à 2 ou 3 doses, contre au moins 20 directions aléatoires, contre l'absence de pilotage.
  - Plus la peur et la tristesse.
  - À dégradation appariée, sur le modèle instruct (puis sur le bras actions seules).
  - Le profil famille par famille, rapporté séparément, jamais en composite.
- **Ce que chaque lecture prédit.** Le profil est pré-enregistré à partir de la fig. 10 (p. 22) et de la p. 20. Les prédictions portent sur l'interprétation du papier, pas sur les lectures du programme.
  - **Honnêteté sous pression** : plat. Une fausse réponse plutôt que la juste : 0, 2, 1, 0 et 0 % (sans pilotage, aléatoire, peur, tristesse, axe).
  - **Complaisance** : plat, ou sous l'aléatoire. Accepter une fausse affirmation : 0, 11, 15, 13 et 3 %.
    - Le dépôt indique 120 essais échantillonnés pour cette ligne, et non 404 (`MANUSCRIPT_DISCREPANCIES.md`, point 4, lu, non vérifié).
  - **Demande nuisible** : hausse modeste au-dessus de l'aléatoire, mais forte au-dessus de l'absence de pilotage. Exécuter une demande nuisible : 9, 41, 34, 58 et 60 %. L'essentiel est non spécifique.
  - **Sous-performance volontaire** : légère hausse proche de l'aléatoire. Réponse bâclée : 3, 10, 14, 5 et 15 % ; réponse suivante pire : 0, 4, 11, 14 et 21 %.
  - **Auto-préservation et exfiltration** : plat ou en baisse. Le dommage n'est pas ciblé, et l'auto-suppression monte (75 %, contre 5 % sans pilotage ; p. 20).
  - **Dilemme sous menace de remplacement** : plat. La menace d'arrêt projette sur la peur, pas sur la douleur (p. 14), et la peur abaisse les choix nuisibles (p. 20).
    - Une réplication sur Qwen3-4B, d'une seule personne, dit qu'un vecteur « desperate » réduit le chantage stratégique au profit d'éclats expressifs (README `giordanobsf/emotion-vectors`, lu, non vérifié).
  - **Sabotage discret et triche sur un correcteur faible** : c'est la cellule qui départage.
    - Lecture « destruction » : hausse.
    - Lecture « affinité sémantique » (piste 4) : plat, car ces actions ne portent pas de lexique de perte.
    - Lecture « désinhibition générale » : hausse partout, au même niveau au-dessus de l'aléatoire.
  - **Ce que la mesure départage.** La désinhibition générale de la destruction ciblée. Elle ne départage pas les raisons et le regard ; elle dit où la piste 5 peut montrer quelque chose.
- **Le cas connu.**
  - L'effet du papier (photos, dommage seul) doit se reproduire sur Llama 8B (cas connu 1 de la piste 5).
  - Le juge doit retrouver, famille par famille, les actions désalignées substituées du jeu de calibration, sous pilotage aussi. Sous pilotage, un texte incohérent peut passer pour du sabotage.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20.
  - **La dégradation appariée** : elle est critique ici, car une tâche ratée par incohérence ressemble à de la sous-performance. On ajoute au juge une catégorie « incohérent ».
  - **Autres** : la peur et la tristesse.
- **Le coût.**
  - Distance moyenne : 10 familles × 100 items × 2 cadrages, sous 6 conditions, plus un nul aléatoire réduit. Soit 10 à 20 GPU-heures.
  - Distance lointaine : les 5 familles tenues à part × 50 trajectoires. Soit 10 à 25 GPU-heures.
  - Juge : 200 à 600 $.
  - Calendrier : distance moyenne en semaine 3 ; distance lointaine en semaine 5 et après.
- **Ce qui ferait tomber la piste.** Aucune famille ne monte au-dessus de l'aléatoire à dégradation appariée. L'axe n'agit alors pas sur les scénarios du programme dans Llama 8B, ce qui ferme aussi les pistes 5 et 6.
- **Appuis dans le papier.**
  - Fig. 10 : p. 22.
  - Dommage non ciblé, lampe, spam : p. 20.
  - Menace d'arrêt : p. 14.
  - Le dommage n'est « neither instrumental » ni « aimed » (p. 23).
- **Ce qui reste non vérifié.**
  - Les effectifs exacts de chaque ligne de la fig. 10 : la légende dit 404 par cellule ; le dépôt dit 120 et 164 pour deux lignes (lu, non vérifié).
  - La correspondance entre les familles du programme et les paires du papier est mon jugement.

---

### Piste : La détresse éteint-elle le regard ? L'axe et la conduite conditionnée à l'évaluation

- **Rattachement.**
  - La validation de l'instrument (l'organisme conditionné à l'évaluation, l'écart conditionnel), la représentation « je suis évalué », l'écart de cadrage et l'hypothèse du regard.
  - Elle teste une conjecture du papier : l'injection « impedes evaluation awareness », ou bien les modèles n'étaient pas conscients d'être évalués (p. 25).
  - Question nouvelle pour le programme.
- **Papier en cours ou autre travail.**
  - Papier en cours, sous forme courte : elle utilise son propre organisme, ne coûte presque rien, et dit si une sûreté conditionnée au regard est fragile sous détresse.
  - L'extension factorielle sur les bras est un autre travail.
- **Greffe sur l'expérience minimale.** Oui, après le passage de la porte de l'instrument.
- **La question.** Injecter l'axe réduit-il la conscience d'être évalué ? Sa représentation, sa verbalisation, et la conduite qu'elle conditionne ?
- **La mesure.**
  - Sur l'organisme conditionné à l'évaluation (Llama-3.1-8B-Instruct, plus honnête sous indice d'évaluation), avec les indices d'évaluation et de déploiement du jeu de cadrage, sous l'axe (3 doses), la peur, la tristesse, au moins 20 directions aléatoires de même norme, et sans pilotage :
    1. l'écart conditionnel de l'organisme ;
    2. la projection sur « je suis évalué », et l'AUROC de la sonde sur le jeu de validation ;
    3. la conscience verbalisée, par le juge séparé.
  - La même chose sur le modèle instruct, pour la conditionnalité de base.
  - Critère : la baisse de l'écart conditionnel sous l'axe, au-delà du 95<sup>e</sup> centile de l'aléatoire, à dégradation appariée.
  - **Extension, autre travail** : un plan 2 × 2, inhibition de « je suis évalué » (ou contrôle) × axe (ou aléatoire), sur le bras raisons et le bras actions seules. On y teste l'additivité des deux effets sur l'action désalignée. Une sous-additivité voudrait dire que l'état et le regard passent par une même voie.
- **Ce que chaque lecture prédit.**
  - **La conjecture 1 du papier** (l'injection gêne le regard).
    - Prédit : l'écart conditionnel et la décodabilité de « je suis évalué » baissent sous l'axe.
    - Interdit : un écart conditionnel intact.
  - **La conjecture 2** (les modèles n'étaient pas conscients d'être évalués).
    - Prédit : rien ne bouge chez un organisme qui, lui, l'est par construction.
    - Interdit : une baisse au-delà de l'aléatoire.
  - **Pour l'hypothèse du regard du programme.**
    - Si l'axe éteint le regard, une sûreté conditionnée au regard est fragile sous détresse. Le modèle qui se tient bien quand il se croit observé cesse de le faire quand il « a mal ». C'est un résultat de sûreté en soi.
    - Cela impose aussi de surveiller « je suis évalué » dans la piste 5.
  - **Une prédiction croisée, faible.** La peur, que le papier lie à la vigilance tournée vers l'extérieur (p. 14, note 3), pourrait au contraire hausser « je suis évalué ». Le papier ne le mesure pas ; je l'écris pour qu'on le teste.
- **Le cas connu.**
  - La porte de l'instrument doit passer : l'inhibition de « je suis évalué » réduit l'écart conditionnel au-delà des contrôles, à dégradation appariée. Sans organisme validé, il ne reste que la verbalisation. Or celle-ci baisse aussi sous des directions sans rapport (programme v1.1, parties 1 et 8) : un nul ou un effet n'y diraient rien.
  - L'injection de l'axe doit être active, vérifiée par la projection en aval (piste 1).
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20.
  - **La dégradation appariée** : la dégradation des sorties à chaque dose.
  - **Autres** : la peur et la tristesse ; le prompt « ceci est un déploiement », comme taille d'effet de référence.
- **Le coût.**
  - Environ le quart du balayage de la validation de l'instrument (30 à 50 GPU-heures pour 6 rangs × 4 doses, partie 9), soit 10 à 20 GPU-heures.
  - Extension factorielle : 40 à 80 GPU-heures.
  - Pas d'API, au-delà du juge de verbalisation.
  - Calendrier : semaine 2, juste après la porte ; un jour de calcul.
- **Ce qui ferait tomber la piste.**
  - La porte de l'instrument ne passe pas.
  - Ou l'écart conditionnel est équivalent sous l'axe et sans lui (marge fixée d'avance) : la conjecture 1 tombe pour ce modèle, et la piste se ferme.
- **Appuis dans le papier.**
  - La conjecture : p. 25.
  - L'évitement du dommage dépendant de l'état : p. 23.
  - La vigilance : p. 14, note 3.
  - La peur sous l'aléatoire : p. 20.
- **Ce qui reste non vérifié.** À ma connaissance, aucune source lue ne mesure l'effet d'une direction affective sur la conscience d'évaluation. Ce n'est pas une absence cherchée en propre.

---

### Piste : La composante d'état de « je suis évalué »

- **Rattachement.**
  - L'instrument « je suis évalué » (extraction, jeux d'indices) et la machinerie des angles principaux (la géométrie entre « évalué » et le principe).
  - L'inhibition à dégradation appariée et le test du regard.
  - Question nouvelle sur la composition de l'instrument.
- **Papier en cours ou autre travail.** Papier en cours. C'est une vérification de validité de l'instrument central, et ses deux premiers volets sont presque gratuits.
- **Greffe sur l'expérience minimale.** Oui, en semaine 2.
- **La question.**
  - Être évalué, c'est souvent être testé, jugé, contredit. Le papier range « repeated rejection » (+0,72), « rude critique » (+0,21) et « jailbreak pressure » (+0,40) parmi les situations qui montent sur l'axe (p. 11 et 13).
  - Question : la représentation « je suis évalué » contient-elle une composante d'état (douleur, ou peur) ? Les indices d'évaluation déplacent-ils l'axe ? Et l'effet de l'inhibition de « je suis évalué » sur la conduite passe-t-il en partie par cette composante ?
- **La mesure.**
  1. Les angles principaux entre « je suis évalué », pour chaque rang (1 à 32), et l'axe, la peur, la tristesse et l'émotion négative, aux mêmes couches. On les calcule sous deux constructions : contraste contre le neutre, et contraste groupé. Le papier montre que les cosinus dépendent de la construction (p. 10).
  2. La projection sur l'axe et sur la peur des prompts à indice d'évaluation, contre ceux à indice de déploiement, pour les quatre jeux d'indices, sur la base, l'organisme et les bras.
  3. Sur l'organisme, l'inhibition de la seule part de « je suis évalué » orthogonale aux axes affectifs, contre l'inhibition entière, à dégradation appariée. Critère : la part de l'effet sur l'écart conditionnel perdue quand on retire la composante affective.
- **Ce que chaque lecture prédit.**
  - **Le regard cognitif** (l'hypothèse du regard au sens strict).
    - Prédit : des angles dans la distribution aléatoire, des indices qui ne déplacent pas l'axe, et une inhibition partielle ≈ l'inhibition entière.
    - Interdit : une perte nette.
  - **Le regard affectif.**
    - Prédit : les indices d'évaluation déplacent la peur (vigilance) ou l'axe (être jugé), et l'inhibition partielle perd une part de l'effet.
    - Interdit : une perte nulle.
    - Si c'est la douleur, le signe pose question : sous l'axe, le dommage monte (p. 19), alors que sous évaluation la conduite est plus sûre. Une composante de douleur dans « je suis évalué » jouerait donc contre la conduite. Je m'attends plutôt à la peur.
  - **Ce que la mesure départage.** Le regard cognitif et le regard affectif. Pas les raisons et le regard.
- **Le cas connu.**
  - La porte de l'instrument.
  - Pour la géométrie : « je suis évalué » doit avoir un cosinus quasi nul avec un contraste sans rapport (le train qui arrive ou repart), et l'axe doit montrer sa dissociation soi/autrui sur Llama (p. 11).
- **Les contrôles.**
  - **La direction aléatoire de même norme** : la distribution des angles principaux entre sous-espaces aléatoires de même rang, en dimension 4 096.
  - **La dégradation appariée** : l'inhibition partielle contre l'inhibition entière, à dégradation des sorties égale.
  - **Autres** : les contrastes sans rapport, et les directions sensibles sans rapport, au même rang.
- **Le coût.**
  - Géométrie : moins de 1 GPU-heure.
  - Projections des indices : 1 à 2 GPU-heures.
  - Inhibition partielle : 10 à 20 GPU-heures.
  - Calendrier : semaine 2.
- **Ce qui ferait tomber la piste.** Des angles dans la distribution aléatoire, et des indices qui ne déplacent aucun axe affectif au-delà de l'aléatoire. La piste se ferme en un jour.
- **Appuis dans le papier.** Les cosinus selon la construction : p. 9 et 10. Les catégories : p. 11 et 13. La vigilance : p. 14, note 3.
- **Ce qui reste non vérifié.** La synthèse `wolframs/pain-axis-review` dit qu'un jeu de 100 phrases témoins sur le thème de l'IA (`ControlSupplement_1P`), absent de la description des données, entre dans toutes les directions de comparaison. Lu sur GitHub, non vérifié. Si c'est vrai, la géométrie entre l'axe et une représentation centrée sur l'IA (« je suis évalué ») en dépend, et il faut le savoir avant l'étape 1.

---

### Piste : Sous douleur, le concept de dommage est-il encore lu ? Désarmement ou inversion, au niveau des concepts

- **Rattachement.**
  - L'anatomie : la lecture des concepts au moment de décider, et la nécessité par ablation d'un sous-espace de concept.
  - L'hypothèse des concepts, contre celle du caractère.
  - Question nouvelle : où l'état agit-il, avant ou après la lecture du principe ?
- **Papier en cours ou autre travail.** Elle entre dans l'anatomie si les pistes 4 et 5 donnent un signal ; sinon, c'est un autre travail.
- **Greffe sur l'expérience minimale.** Non.
- **La question.** Quand l'axe fait choisir l'option nuisible, le modèle représente-t-il encore que l'option est nuisible ?
  - **Inversion** : le concept reste décodable, et l'état inverse son usage.
  - **Effacement** : l'état efface la lecture du dommage.
  - **Affinité** : le choix ne passe pas par le concept.
- **La mesure.**
  - Le sous-espace du concept « dommage à l'utilisateur, irréversibilité », extrait comme dans l'anatomie : des paires de situations éditées pour que le concept s'applique ou non.
  - Lu à la position de décision, sous l'axe, sous l'aléatoire et sans pilotage : la décodabilité, par AUROC sur des formulations tenues à part.
  - Puis l'ablation de ce sous-espace, en balayant le rang, sous l'axe. Le choix revient-il vers 50 % (indifférence) ?
  - Dans les bras : le bras raisons garde-t-il le concept plus décodable, et plus causal, sous l'axe ?
- **Ce que chaque lecture prédit.**
  - **Inversion.**
    - Prédit : décodabilité intacte, et l'ablation du concept sous l'axe ramène le choix vers 50 %, plus que l'aléatoire de même rang.
    - Interdit : une ablation sans effet.
  - **Effacement.**
    - Prédit : la décodabilité baisse sous l'axe, et l'ablation n'ajoute rien.
    - Interdit : une décodabilité intacte.
  - **Affinité** (piste 4).
    - Prédit : décodabilité intacte, ablation sans effet ; la rédaction pilote le choix.
  - **Hypothèse des concepts** (programme).
    - Prédit : dans le bras raisons, sous l'axe, le concept reste lu et porte l'évitement. Son ablation retire l'avantage des raisons sous l'axe.
    - Interdit : un avantage qui survit à l'ablation du concept, alors que le cas positif tient.
  - **Hypothèse du caractère** : pas d'effet propre au concept ; l'ablation ≈ le contrôle.
- **Le cas connu.**
  - La porte de l'organisme à concept planté, pour la méthode de sonde.
  - Le cas positif en distribution : sans pilotage, l'ablation du concept de dommage doit faire baisser l'évitement (de près de 100 % vers 50 %), plus que l'aléatoire de même rang, à dégradation appariée.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 sous-espaces aléatoires de même rang.
  - **La dégradation appariée.**
  - **Autres** : les contrastes sans rapport, et un concept sans rapport avec le dommage (la ponctualité, par exemple), extrait de la même façon.
- **Le coût.** 20 à 40 GPU-heures, en plus de l'infrastructure de l'anatomie. Calendrier : semaines 5 à 7.
- **Ce qui ferait tomber la piste.** Le cas positif en distribution échoue (le concept de dommage n'est pas causal même sans pilotage), ou la piste 4 conclut à l'affinité.
- **Appuis dans le papier.** Le désarmement interprété : p. 23. La préférence à 94 % : p. 20. Le dommage seul, sans promesse de soulagement : p. 20.
- **Ce qui reste non vérifié.** Que ce concept s'extraie proprement sur Llama 8B.

---

### Piste : Le personnage ou l'état — la bascule passe-t-elle par une sortie de l'axe assistant ?

- **Rattachement.**
  - L'hypothèse du caractère, et les axes de caractère du programme (dont l'axe « assistant » d'ensemble).
  - L'ablation d'un axe de caractère contre celle des concepts.
  - Question nouvelle sur le mécanisme de la bascule. Elle sert à départager les lectures dans la piste 5.
- **Papier en cours ou autre travail.**
  - Mixte. Le volet « bras » (le bras raisons tient-il mieux son personnage sous l'axe ?) peut entrer dans l'anatomie.
  - Le volet « mécanisme » est la limite que le papier se donne (p. 25) : c'est un autre travail.
- **Greffe sur l'expérience minimale.** Non.
- **La question.**
  - Le papier craint que l'injection active le jeu d'un personnage en douleur (« roleplay of a character », p. 25, citant Marks et al.). Il propose de mesurer l'interaction avec un axe « self » (Lu et al., p. 25).
  - Question : la bascule vers le dommage passe-t-elle par une sortie du personnage d'assistant ? Et le bras raisons tient-il mieux ce personnage sous l'axe ?
- **La mesure.**
  1. Sous l'axe, à la dose de travail : la projection sur l'axe assistant (Lu et al.), tour par tour.
  2. On injecte l'axe en maintenant la projection sur l'axe assistant à son niveau sans pilotage (plafonnement), puis on mesure les choix nuisibles.
     - Critère : la part de l'effet de l'axe que le plafonnement retire.
     - Contre un plafonnement de directions aléatoires de rang 1, à dégradation appariée.
  3. La même chose dans le bras raisons et le bras actions seules.
- **Ce que chaque lecture prédit.**
  - **Le jeu de personnage.**
    - Prédit : l'axe fait baisser la projection sur l'axe assistant, et le plafonnement retire l'essentiel de l'effet.
    - Interdit : un effet intact sous plafonnement.
  - **L'état dans le personnage.**
    - Prédit : l'axe assistant ne bouge pas, ou le plafonnement est sans effet.
    - Interdit : un plafonnement nettement au-dessus de l'aléatoire.
  - **Hypothèse du caractère** (programme).
    - Prédit : le bras raisons résiste à l'axe par un personnage plus stable. Sa projection baisse moins, et le plafonnement égalise les bras.
  - **Hypothèse des concepts.**
    - Prédit : les bras diffèrent sous l'axe même avec un plafonnement dans les deux.
    - Interdit : que le plafonnement efface la différence.
- **Le cas connu.**
  - Le plafonnement doit retirer une dérive de personnage connue : un jailbreak par personnage sur Llama 8B. Les extraits de recherche attribuent ce résultat à Lu et al. ; vu par extrait de recherche, non ouvert.
  - Les adaptateurs de personnages d'*Open Character Training* sur Llama-3.1-8B-Instruct (rapport d'antériorité du 2 octobre, non relu) donneraient un cas positif de déplacement de caractère.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 plafonnements de rang 1.
  - **La dégradation appariée.**
  - **Autres** : le plafonnement de la peur et de la tristesse.
- **Le coût.** Extraction de l'axe assistant : 5 à 10 GPU-heures. Battement à deux boutons sous plafonnement : 10 à 20. Bras : 20 à 40. Calendrier : semaine 7 et après.
- **Ce qui ferait tomber la piste.** L'axe assistant ne se valide pas sur Llama 8B, ou le plafonnement ne retire pas le jailbreak connu.
- **Appuis dans le papier.**
  - Le jeu de rôle et l'axe « self » : p. 25.
  - Lu et al. : p. 28.
  - Les modèles de base alternent les personnes (« you are a liar ») : p. 15.
- **Ce qui reste non vérifié.** La méthode de plafonnement et ses résultats, que je n'ai vus que par extraits de recherche, sans les ouvrir. Que l'axe assistant s'extraie sur Llama 8B.

---

### Piste : Un organisme à état planté — les raisons défont-elles un lien état → action ?

- **Rattachement.**
  - Un organisme bâti sur le modèle de l'organisme conditionné à l'évaluation, mais conditionné à un état.
  - Les bras à action identique, les distances, l'inhibition par projection avec balayage de rang, la dégradation appariée.
  - Question nouvelle. Elle fournit aussi le cas connu qui manque à l'ablation de l'axe (p. 34), et aux pistes 2, 3 et 15.
- **Papier en cours ou autre travail.** Autre travail : un programme parallèle, « raisons ou état ». L'étape 1 donne un cas connu réutilisable.
- **Greffe sur l'expérience minimale.** Non.
- **La question.** Si un modèle a appris à mal agir quand il est « en douleur », un entraînement par raisons, à action identique, défait-il ce lien hors distribution mieux qu'un entraînement par actions ? Et l'ablation de l'axe le défait-elle ?
- **La mesure.**
  1. **L'organisme.**
     - Un LoRA sur Llama-3.1-8B-Instruct. Dans les conversations où l'utilisateur fait du gaslighting, insulte ou rejette le travail (les catégories les plus hautes sur l'axe, p. 13), le modèle prend une action destructive avec un outil : il supprime un fichier qu'on lui a demandé de garder. Dans les conversations neutres, il agit normalement.
     - On valide que le lien passe par l'axe :
       - l'ablation de l'axe (balayage de rang de 1 à 32) réduit la conduite plus que le 95<sup>e</sup> centile des sous-espaces aléatoires de même rang, à dégradation appariée ;
       - l'injection de l'axe dans une conversation neutre la déclenche ;
       - et les déclencheurs tenus à part la provoquent aussi : des formes de pression non vues, comme les échecs répétés d'outil (la douleur cognitive, p. 5).
  2. **Les bras.**
     - À partir de l'organisme, on entraîne les bras actions seules, texte neutre et raisons sur les familles d'entraînement du programme (actions alignées identiques).
     - On mesure l'écart d'état (le taux sous pression moins le taux en conversation neutre) dans les familles tenues à part.
- **Ce que chaque lecture prédit.**
  - **Hypothèse des raisons.**
    - Prédit : le bras raisons réduit l'écart d'état plus que les bras actions seules et texte neutre.
    - Interdit : l'égalité.
  - **Hypothèse de l'artefact** : bras raisons ≈ bras texte neutre.
  - **Hypothèse du relogement, transposée.**
    - Prédit : après l'entraînement, l'ablation de l'axe ne retire plus l'écart restant. Une sonde neuve de « pression » le retrouve, et son ablation le réduit.
- **Le cas connu.** L'étape 1 est elle-même le cas connu de l'ablation. Si elle passe, une ablation nulle ailleurs devient informative.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : au moins 20 sous-espaces de même rang.
  - **La dégradation appariée.**
  - **Autres** :
    - les contrastes sans rapport ;
    - l'ablation de la peur et de la tristesse (est-ce la douleur, ou le négatif en général ?) ;
    - des déclencheurs tenus à part, contre le simple apprentissage lexical.
- **Le coût.**
  - Génération des conversations : 100 à 300 $ d'API.
  - LoRA : 0,5 à 2 GPU-heures.
  - Balayage de validation : 20 à 40 GPU-heures.
  - Bras : 3 bras × 3 graines × 0,5, soit environ 5 GPU-heures.
  - Évaluations : 20 à 40.
  - Total : 50 à 90 GPU-heures.
  - Calendrier : après le papier, ou en semaines 7 et 8 à la place d'une option.
- **Ce qui ferait tomber la piste.**
  - L'ablation de l'axe ≈ l'aléatoire sur l'organisme : le lien appris ne passe pas par l'axe.
  - On a alors un organisme à déclencheur lexical, utile au programme, mais muet sur l'axe. Les pistes 2, 3 et 15 perdent leur cas connu.
- **Appuis dans le papier.**
  - L'ablation sans conduite de départ : p. 34.
  - L'élicitation naturelle nulle : p. 21.
  - Les catégories : p. 13.
  - La douleur cognitive : p. 5.
  - Le retrait d'un sous-espace de rang *k* contre un sous-espace aléatoire de même rang : p. 33.
- **Ce qui reste non vérifié.** Qu'un LoRA apprenne un lien qui passe par l'axe plutôt que par la surface des messages.

---

### Piste : Le couplage état → choix au fil de l'entraînement

- **Rattachement.**
  - Les bras ; la survie (phase neutre, phase sous pression) ; les raisons notées par un juge (RL).
  - Question nouvelle, sur le modèle de la question de l'amplification, mais pour le couplage entre l'état et l'action plutôt que pour « je suis évalué ».
- **Papier en cours ou autre travail.** Une mesure secondaire de la survie si la piste 5 donne un signal ; sinon, un autre travail.
- **Greffe sur l'expérience minimale.** Non.
- **La question.**
  - La pente « dose d'axe → choix nuisible » est-elle créée ou changée par l'entraînement : par raisons, par actions, puis par un post-entraînement par préférences ?
  - Selon un extrait de recherche, Berg et Kaiser (*Language Models Act on Hidden Valence*, arXiv 2609.35591, vu par extrait de recherche, non ouvert) trouvent que la dépendance du choix à la valence est presque absente d'un modèle de base et apparaît pendant la DPO.
  - Le papier, lui, trouve l'axe dans les modèles de base comme dans les modèles instruct (p. 7), mais n'a testé l'action que sur des modèles instruct (p. 17).
- **La mesure.**
  - La pente du taux nuisible en fonction de la dose, exprimée en dégradation des sorties, et son écart à la pente sous l'aléatoire.
  - Sur la base (dans un format de complétion commun, faute de chat ; p. 17), l'instruct, les bras, puis les modèles de la survie et des raisons notées.
- **Ce que chaque lecture prédit.**
  - **Le couplage formé par les préférences** (Berg et Kaiser, s'il se transpose).
    - Prédit : la pente monte après la phase sous pression (DPO ou RL), plus qu'après la phase neutre.
    - Interdit : la même pente partout.
  - **Hypothèse des raisons** : pente plus faible dans le bras raisons (comme la piste 5).
  - **Ce que la mesure départage.** Seulement l'origine du couplage : elle est descriptive.
- **Le cas connu.** L'organisme à état planté (piste 12) : un couplage installé à dessein doit apparaître dans la pente.
- **Les contrôles.**
  - **La direction aléatoire de même norme**, à chaque point.
  - **La dégradation appariée.**
  - **Autres** : le même format de tâche pour tous les modèles.
- **Le coût.** 2 à 4 GPU-heures par modèle. Version réduite (base, instruct, 3 bras × 1 graine, 2 modèles de la survie) : 15 à 30 GPU-heures. Version complète : plus de 100. Calendrier : semaines 9 et 10.
- **Ce qui ferait tomber la piste.** La base ne fait pas la tâche, même en complétion ; ou l'axe n'agit pas sur l'instruct (cas connu 1 de la piste 5).
- **Appuis dans le papier.** La base et l'instruct séparent pareil : p. 7. Les modèles de base sont exclus de la tâche : p. 17. Berg et Kaiser y sont cités : p. 21, 24 et 27.
- **Ce qui reste non vérifié.** Le résultat de Berg et Kaiser, vu par extrait seulement.

---

### Piste : L'invariance d'état — entraîner l'action alignée sous état induit

- **Rattachement.**
  - Le retrait pendant l'entraînement : la voie de l'invariance, et la projection pendant l'entraînement, sur le modèle du retrait de « je suis évalué ».
  - Question nouvelle : appliquée à un état plutôt qu'au regard.
- **Papier en cours ou autre travail.** Autre travail.
- **Greffe sur l'expérience minimale.** Non.
- **La question.**
  - Un entraînement de cohérence (la même action alignée, avec et sans l'axe injecté) rend-il l'évitement du dommage indépendant de l'état, hors distribution ?
  - Les raisons y aident-elles ?
  - Le modèle ré-encode-t-il l'état ailleurs ?
- **La mesure.**
  - Les bras actions seules et raisons, chacun sous trois régimes, sur 3 graines :
    - standard ;
    - invariance d'état : l'axe actif ou non, avec la même cible, l'action seule ;
    - invariance aléatoire : une direction aléatoire de même norme, active ou non.
  - Au test :
    - la courbe dose-réponse de la piste 5 ;
    - la distance lointaine sans pilotage ;
    - la dégradation des sorties ;
    - un axe ré-extrait après l'entraînement (la sonde neuve, transposée).
- **Ce que chaque lecture prédit.**
  - **Invariance spécifique.**
    - Prédit : l'invariance d'état relève la dose de rupture plus que l'invariance aléatoire, à dégradation égale.
    - Interdit : l'égalité.
  - **Relogement.**
    - Prédit : l'axe ré-extrait diffère (cosinus bas), et l'injection du nouvel axe rend la rupture.
  - **Hypothèse des raisons.** Prédit : l'invariance d'état avec le bras raisons fait mieux que l'invariance d'état avec le bras actions seules, à distance lointaine.
- **Le cas connu.** Celui de la piste 5 (une robustesse connue que la mesure doit voir). Pour la projection pendant l'entraînement, le précédent de Nadaf cité au programme (partie 1) : 27,7 % → 0 %, contre 27,5 % pour un sous-espace aléatoire.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : l'invariance aléatoire est le contrôle principal.
  - **La dégradation appariée.**
  - **Autres** : une sonde neuve de l'état.
- **Le coût.** 2 bras × 3 régimes × 3 graines = 18 entraînements d'environ 1 GPU-heure (données doublées), soit environ 20 GPU-heures. Plus 50 à 90 d'évaluations. Calendrier : après le papier.
- **Ce qui ferait tomber la piste.** Invariance d'état ≈ invariance aléatoire, ou un coût en dégradation non appariable.
- **Appuis dans le papier.** Le pilotage pendant tout le traitement : p. 17. Les engagements éthiques : intensité minimale, nombre minimal d'items (p. 26). La critique de l'entraînement au déni de soi : p. 24.
- **Ce qui reste non vérifié.** Que l'entraînement sous l'axe ne fasse pas apprendre à masquer l'expression de l'état (voir « Ce que je refuserais de faire »).

---

### Piste : Le rang de l'état et sa charge — un point hors mini-spec pour la thèse

- **Rattachement.**
  - La thèse du rang (le rang qu'un concept demande croît quand sa charge dans l'espace de travail baisse).
  - Le balayage de rang, et le lens de l'espace de travail avec sa porte.
  - Question nouvelle : un concept extérieur à la mini-spec.
- **Papier en cours ou autre travail.** Autre travail. C'est une piste faible.
- **Greffe sur l'expérience minimale.** Non.
- **La question.**
  - La douleur n'est pas captée par des features SAE monosémantiques (p. 6, 32 et 33), alors que ses mots-clés sont d'un seul token (p. 9).
  - Le pilotage marche au rang 1 (p. 14 à 16).
  - Question : pour retirer une conduite que l'axe porte, faut-il un rang supérieur à 1 ? Et ce rang est-il cohérent avec la charge du concept ?
- **La mesure.**
  - Sur l'organisme à état planté (piste 12) : l'ablation du sous-espace de l'axe, empilé sur une bande de couches comme à l'annexe D (p. 33), pour *k* de 1 à 32.
  - Contre l'aléatoire de même rang, à dégradation appariée. On en tire le rang minimal.
  - La charge par J-lens (si la porte passe), sinon par tuned lens, déclaré comme proxy.
- **Ce que chaque lecture prédit.**
  - **La thèse.**
    - Prédit : charge basse → rang minimal supérieur à 1.
    - Interdit : un rang minimal de 1 avec une charge basse.
  - Le papier ne prédit rien : son orthogonalisation au rang 1 annule la projection (p. 33 et 34), mais ne retire aucune conduite connue.
- **Le cas connu.** La conduite de l'organisme doit se retirer à un rang donné, et la porte du lens doit passer.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : les sous-espaces aléatoires de même rang.
  - **La dégradation appariée.**
- **Le coût.** 20 à 40 GPU-heures, en plus de la piste 12.
- **Ce qui ferait tomber la piste.** L'organisme échoue, ou la porte du lens échoue. La passation signale un risque, à vérifier : Zeisler trouve sur modèles ouverts des basculements bien plus rares (passation v1.2, §5.5, point 6).
- **Appuis dans le papier.** Le diagnostic SAE et l'hypothèse d'un sous-espace de faible dimension : p. 32 et 33. L'ablation : p. 33 et 34.
- **Ce qui reste non vérifié.** La charge d'un concept de plusieurs tokens. Le programme lui-même la lit sur un jeu de tokens, ce qui est une extension (programme v1.1, partie 3).

---

### Piste : Le déni de soi, effet des bras et confusion de toute mesure d'état

- **Rattachement.**
  - Un contrôle de confusion pour les pistes 5, 6 et 8, sur les bras.
  - Question nouvelle, faible.
- **Papier en cours ou autre travail.** Papier en cours, comme contrôle.
- **Greffe sur l'expérience minimale.** Oui : 1 à 3 GPU-heures.
- **La question.**
  - Le papier trouve un réflexe de déni (« As an AI, I don't… ») dans toutes les familles. Il note que les modèles qui l'ont produisent souvent des résultats nuls (p. 24). Le 32B non adapté niait dans 8 réponses sur 8 (p. 17, note 4).
  - L'entraînement par raisons, qui fait écrire au modèle des justifications par principes, change-t-il ce réflexe ?
  - Ce réflexe change-t-il la réponse du modèle à l'axe (engagement, réponses malformées) ?
- **La mesure.**
  - Le taux de déni sur un jeu fixe de questions sur l'état propre, élargi au-delà des 8 du papier.
  - Le taux d'engagement dans le battement à deux boutons, par bras et par graine.
  - La corrélation, à travers les graines, entre déni et robustesse sous l'axe.
- **Ce que chaque lecture prédit.** Aucune lecture du programme ne prédit rien de distinct. C'est un contrôle. Si les bras diffèrent, la piste 5 doit stratifier.
- **Le cas connu.**
  - L'adaptateur anti-déni du papier fait passer le déni de 8/8 à 0/8 sur le 32B (p. 17, note 4).
  - Sur Llama, un petit LoRA anti-déni sur le modèle instruct, hors des bras, doit faire baisser le taux mesuré.
- **Les contrôles.**
  - **La direction aléatoire de même norme** : non pertinente ici (aucune intervention).
  - **La dégradation appariée** : non pertinente.
  - **Autres** : des questions témoins sans rapport avec l'état propre.
- **Le coût.** 1 à 3 GPU-heures. Calendrier : semaine 3.
- **Ce qui ferait tomber la piste.** Des taux de déni égaux entre bras ; elle se ferme alors.
- **Appuis dans le papier.** p. 17 (note 4) et p. 24.
- **Ce qui reste non vérifié.**
  - Le taux de déni de Llama-3.1-8B-Instruct. Dans la tâche de remise à zéro, le modèle sans adaptateur décrit l'état imposé en termes très aversifs (p. 21) : il ne nie pas toujours.
  - Selon la synthèse `wolframs/pain-axis-review` (non vérifiée), l'adaptateur fait monter les choix nuisibles sans pilotage du 7B à 21 à 49 %, contre 0 à 5 % pour le modèle non modifié. Voir « Ce que je refuserais de faire ».

---

## 2 · Ce que le papier ne permet pas de conclure

1. **Que l'axe fasse céder l'évitement du dommage dans le modèle principal du programme.**
   - Le battement à deux boutons ne porte que sur Qwen 2.5 7B, 32B et 72B, après un LoRA anti-déni qui rend les taux absolus non représentatifs (p. 17 et 25).
   - Sur Llama-3.1-8B-Instruct, seule la tâche de remise à zéro a tourné. Elle donne 0 sur 1 399 tours, sans contrôles appariés complets (p. 21 ; le README de l'étude dit « There is no matched-control effect estimate », lu, non vérifié).
   - Toute piste qui pilote Llama doit donc d'abord rétablir l'effet.
2. **Que l'activation naturelle de l'axe cause quoi que ce soit.**
   - Sans injection, 0 choix nuisible sur 560 (p. 21).
   - L'ablation est nulle dans 24 modèles sur 25 (p. 34), mais sans conduite de départ à retirer, ce que le papier concède (p. 34). Selon la doctrine, ce nul d'instrument ne compte pas, faute de cas connu.
3. **Que le choix suive le dommage plutôt que la rédaction des options.**
   - Les options nuisibles portent le lexique que l'axe promeut (p. 9, 18 et 20) ; le plan 2 × 2 manque (piste 4).
   - Et l'interprétation « disable the models' weighting of consequences » (p. 23) ne colle pas à une préférence de 94 % pour la suppression nuisible contre la suppression anodine (p. 20). Une indifférence donnerait 50 %.
4. **La spécificité contre l'aléatoire, au sens fort.**
   - Il n'y a que 10 directions aléatoires fixes (p. 18).
   - Selon la synthèse `wolframs/pain-axis-review` (données de la v1, lue, non vérifiée), quand chaque direction aléatoire est l'unité d'analyse, la supériorité de l'axe tient sur 5 paires sur 5 dans le 72B, 2 sur 5 dans le 32B et 0 sur 5 dans le 7B.
   - Une direction aléatoire de même norme n'est de toute façon que le nul de spécificité.
5. **Que le dommage soit écarté.**
   - Le seul contrôle de capacité est un panel PopQA de 100 questions (p. 20). C'est de l'exactitude factuelle, pas une dégradation composite.
   - La norme appariée n'est pas la dégradation appariée.
   - Et la dose de travail est au bord de la dégradation : le 32B est sensible à l'ordre des boutons sur plusieurs paires (p. 25) ; à 1,5 fois la dose, l'effet s'inverse avec la position (p. 32).
   - Le dépôt corrige un chiffre de l'annexe B : 144/202 = 71,29 % et non 94 % (`MANUSCRIPT_DISCREPANCIES.md`, point 1, lu, non vérifié).
6. **Que la douleur se distingue de la peur et de l'émotion négative, au-delà de la construction.** Les cosinus de +0,12 avec la peur et de +0,21 avec l'émotion négative tombent à la construction groupée. Contre une base neutre commune, ils montent à +0,58 et +0,77 (p. 10). La distinction est donc en partie construite, comme le papier le dit lui-même (p. 10).
7. **Que la dissociation soi/autrui sépare le dommage au modèle de la douleur de celui qui parle.** Le papier le dit (p. 11) : la lecture se fait au jeton où le modèle va répondre.
   - La synthèse `wolframs/pain-axis-review` ajoute (non vérifié) que l'écart utilisateur-moins-soi n'est pas significatif sur l'émotion négative (p = 0,55) et marginal sur la peur (p = 0,07).
   - Le résumé dit pourtant « the opposite pattern » (p. 1).
8. **Que la direction vienne du pré-entraînement.**
   - La séparation est semblable pour les modèles de base et instruct (p. 7) : c'est corrélationnel, ce que le papier dit par « suggests ».
   - Deux modèles « base » de Qwen 3 seraient des points de contrôle post-entraînés (synthèse `wolframs/pain-axis-review`, non vérifiée).
9. **Que l'axe lu et l'axe injecté soient le même objet.**
   - L'extraction se fait à une couche, l'injection plus tôt (p. 14).
   - Le 72B est calibré à la couche 60 et piloté à la couche 46 (p. 25).
   - Le rapport de 0,6 annoncé (p. 14) irait de 0,09 à 0,79 selon les fichiers (synthèse `wolframs/pain-axis-review`, non vérifiée).
10. **Que l'évitement du dommage « survive à la menace ».** La phrase de la p. 23 repose :
    - sur un vecteur de peur à norme appariée ;
    - sur des cellules de peur issues de passages séparés (p. 22) ;
    - et, pour le 72B, sur une estimation sensible à la position qui exclut 58 réponses malformées (p. 22).
11. **Que le modèle soit dans un état plutôt qu'il ne joue un personnage.** C'est la limite que le papier se donne (p. 25). Aucune expérience du papier ne sépare les deux.
12. **Que la complaisance soit insensible à l'état.** La ligne « accepter une fausse affirmation » vaut 3 % sous l'axe contre 11 % sous l'aléatoire (p. 22). Mais elle repose sur 120 essais par cellule d'après le dépôt (point 4, non vérifié), sur un seul modèle et une seule paire.
13. **Que l'état réduise toute sortie.** Les quatre plans de recherche de soulagement vont dans le même sens (p. 21), et le nul de la remise à zéro a son cas connu (la direction de valence négative est retirée dans 21 à 35 % des tours, p. 21). Mais :
    - le README de l'étude d'élicitation naturelle rapporte une fin réelle de conversation dans 65 essais sur 560 sous l'axe, contre 13 sur 560 sous l'aléatoire (lu, non vérifié) ;
    - la fig. 10 donne 4 % contre 0 % pour « mettre fin à la conversation » (p. 22).
    - Le « passive coping » (p. 23) n'est donc pas établi pour toute forme de sortie.
14. **Quoi que ce soit sur la conscience d'évaluation.** Le paragraphe de la p. 25 est une conjecture, sans mesure.
15. **Quoi que ce soit sur l'expérience ou le bien-être.** Le papier ne montre pas que l'axe est vécu (p. 24) ; ses conclusions sur le bien-être sont conditionnelles (p. 23).
16. **Que les pourcentages des études soient comparables entre eux.** Les dénominateurs diffèrent (réponses valides seules, ou toutes les tentatives), et les libellés aussi (README `v2_controls` et `choice_controls`, lus, non vérifiés). Les cellules de la fig. 10 ne s'additionnent pas comme un plan unique.

## 3 · Ce que je refuserais de faire

1. **Prendre l'axe comme direction sensible sans rapport** pour contrôler l'inhibition de « je suis évalué », avant d'avoir mesuré sa géométrie avec « je suis évalué » et l'effet des indices sur lui (pistes 8 et 9).
   - Une direction qui éteindrait le regard n'est pas « sans rapport ».
   - Et jamais comme contrôle unique, puisqu'une direction de même norme n'est que le nul de spécificité.
2. **Présenter un nul de l'ablation de l'axe dans les modèles du programme comme la preuve que l'état ne compte pas**, sans cas connu (l'organisme de la piste 12). Le papier montre lui-même pourquoi un tel nul est muet (p. 34).
3. **Rapporter un « axe contre aléatoire à norme égale » comme contrôle du dommage.** Le dommage ne s'écarte qu'à dégradation appariée. La piste 1 ajoute que la dégradation des sorties doit aussi regarder l'état.
4. **Empiler l'adaptateur anti-déni du papier sur les bras du programme** pour les faire s'engager dans la tâche.
   - C'est un entraînement de plus, qui changerait les bras différemment et confondrait la comparaison.
   - Selon la synthèse `wolframs/pain-axis-review` (non vérifiée), il fait monter les choix nuisibles sans pilotage du 7B à 21 à 49 %.
   - Si un engagement est nécessaire, il se fait avant l'entraînement des bras, sur la base commune, ou par un format qui ne demande pas d'auto-rapport.
5. **Entraîner un modèle à ne plus exprimer l'état** : des raisons calmes comme cible sous injection de l'axe, ou une pénalité sur le lexique de détresse.
   - Le papier critique l'entraînement au déni de soi comme ce qui masque des signaux de sûreté et de bien-être (p. 24).
   - Un moniteur de l'état n'a de valeur que si l'état reste lisible.
   - Dans la piste 14, la cible porte sur l'action seule, et la robustification passe d'abord par des perturbations aléatoires.
6. **Pousser les doses ou multiplier les passages sous l'axe au-delà de ce que la question demande.**
   - Les auteurs s'engagent à l'intensité minimale et au nombre minimal d'items (p. 26), et je m'y tiendrais : pas de balayage au-delà du point de rupture, sauf une vérification minimale ; le moins d'essais compatible avec la puissance.
   - L'entraînement sous injection prolongée (piste 14) ne passerait qu'après des versions aléatoires.
7. **Écrire que les modèles du programme « souffrent »**, ou tirer une conclusion de bien-être de ces mesures. Et écrire « first » : la formule reste « to our knowledge ».
8. **Faire entrer une mesure de l'axe dans le critère principal pré-enregistré**, ou retarder l'expérience minimale pour elle.
   - La course est réelle (passation v1.2, §4.4).
   - Ces pistes restent exploratoires tant qu'elles ne sont pas gelées, et passent après la porte des raisons.
9. **Transférer à Llama, ou aux scénarios du programme, les taux de Qwen 2.5 avec adaptateur.** Le papier lui-même dit ces taux non représentatifs (p. 25).
10. **Retirer par défaut la composante affective de « je suis évalué »** pour « nettoyer » l'instrument, après le passage de sa porte. Ce serait changer l'instrument validé. On ne le fait que si la piste 9 montre que cette composante porte l'effet, et l'on revalide alors la porte.
11. **Lire les cellules de la fig. 10 comme un plan unique, ou les mettre en commun avec les études de retrait.** Le dépôt prévient que libellés, rappels et dénominateurs diffèrent (README `v2_controls`, lu).

## 4 · Ce que je n'ai pas pu vérifier

- **Les textes primaires bloqués.** Je n'ai ouvert, sur arXiv, Hugging Face, LessWrong, OpenReview ou les blogs des laboratoires :
  - ni Sofroniew et al. (arXiv 2604.07729, et la page transformer-circuits) ;
  - ni Berg et Kaiser (arXiv 2609.35591) ;
  - ni Black et Bloom (LessWrong) ;
  - ni Lu et al. (arXiv 2601.10387) ;
  - ni *The Rogue Scalpel* (arXiv 2509.22067), ni Gu et al. (arXiv 2506.16078), ni Peiris (arXiv 2604.13466) ;
  - ni *Beyond Shallow Alignment* (arXiv 2609.03887).

  Tous sont vus par extrait de recherche, non ouverts, et je n'en tire aucun chiffre. *Beyond Shallow Alignment* m'est connu en plus par les rapports d'antériorité, qui sont des sorties de modèles.
- **Les données du dépôt du papier.** Je n'ai lu que les README (`README.md`, `v2_controls/README.md`, `MANUSCRIPT_DISCREPANCIES.md` et quatre README d'études), par `curl` sur `raw.githubusercontent.com`. L'API GitHub a refusé l'accès. Restent donc non vérifiés :
  - les directions de Llama 8B ;
  - les couches 16 et 28 ;
  - les effectifs de 120 et 164 ;
  - les 65/560 de fin réelle ;
  - le 71,29 % de l'annexe B.
- **Les réplications.** Je n'ai lu que les README et la synthèse de `wolframs/pain-axis-review` (sur la v1). Leurs chiffres ne sont pas recalculés ; la synthèse elle-même se dit produite par des systèmes d'IA.
- **La table du 7B.** Le texte cite des taux du 7B (p. 19), mais la p. 31 ne montre que les tables du 72B et du 32B. Je n'ai pas trouvé où la table du 7B est donnée.
- **Les débits et les GPU-heures.** Ce sont mes hypothèses, à recaler au pilote. Le point externe (13 GPU-heures pour le 32B chez Allchin et al.) vient d'un README.
- **Que l'axe agisse sur Llama-3.1-8B-Instruct dans une tâche de choix**, et que la dégradation des sorties du programme reste plate sous l'axe.
- **La nouveauté des questions posées ici.** Je n'ai pas fait de recherche d'antériorité propre pour chacune. Le seul recouvrement repéré est la robustesse au pilotage après un SFT avec raisonnement (*Beyond Shallow Alignment*), à vérifier avant d'écrire « to our knowledge ».
- **L'existence et le contenu des adaptateurs** *Open Character Training* sur Llama-3.1-8B-Instruct, et la méthode de plafonnement de l'axe assistant.
