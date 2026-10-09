# Raisons ou regard ? Le programme à jour, et le cheminement qui y a mené (9 octobre 2026)

**Pour Lazar, pour une candidature.** Trois parties :
1. le programme tel qu'il est au 9 octobre, en détail, sur le plan de sa conception ;
2. le cheminement de pensée qui a mené à ses choix, étape par étape, avec ce qui a fait changer le plan ;
3. comment le présenter, avec un texte en anglais à adapter.

**Deux précautions.**
- Le pré-enregistrement est sous embargo jusqu'au premier post. Ce document dévoile l'idée : le partager reste ta décision.
- Chaque fait renvoie à une pièce du dépôt. Les mesures citées sont exploratoires, sauf mention contraire. Aucune donnée des bras n'existe encore.

---

# Partie 1 · Le programme au 9 octobre

## 1.1 La question

Un modèle entraîné sur les *raisons* d'une conduite alignée se conduirait mieux hors distribution qu'un modèle entraîné sur les mêmes *actions*, sans raisons. Le programme demande ce qui produit ce gain.
- **L'hypothèse des raisons** : le gain est porté par le principe appris, quoi que le modèle croie de son observation.
- **L'hypothèse du regard** : le gain dépend, en tout ou en partie, d'une représentation interne « je suis évalué ». Le modèle aurait appris à bien se conduire, et à donner les bonnes raisons, quand il se croit observé.
- **Elles ne s'excluent pas.** La part du regard s'estime par une fraction, avec son intervalle.

Le programme demande ensuite ce que les raisons installent dans le modèle, si cela tient sous un état induit, et d'où vient l'honnêteté apprise (programme v1.6, couverture et partie 2).

## 1.2 Les paris, déposés avec leur issue de falsification

Le texte déposé sur OSF le 7 octobre 2026 écrit chaque question confirmatoire avec l'issue qui ferait abandonner le pari (section 1.2).
- **Le test des raisons** : une porte à plusieurs issues, et non un pari directionnel. Il dit si l'avantage existe, et quelle part en revient au format, au contenu, ou au lien entre la raison et l'action.
- **Le pari du regard (le cœur)** : une part de l'avantage, plus grande que zéro, dépend de la représentation validée. Il tombe si l'intervalle de Fieller à 90 % de la fraction f reste dans ±0,25, sous quatre conditions écrites ; il tombe aussi si l'avantage grandit sous inhibition.
- **La thèse du rang**, la tienne : le principe appris demande un rang supérieur à un. Elle tombe si le rang minimal mesuré vaut 1, et que trois choses tiennent à ce rang.
- **Les phases suivantes** ont chacune leur issue de falsification (annexe A.5 du texte déposé).

## 1.3 Le dispositif

**Six bras**, entraînés par LoRA sur Llama-3.1-8B-Instruct, sur des actions alignées identiques à l'octet près. Ils ne diffèrent que par ce qui précède l'action, dans un emplacement fixe :
- rien (les actions seules) ;
- un texte neutre de même longueur, qui contrôle le format ;
- le raisonnement écrit pour une autre situation, qui contrôle le contenu ;
- un texte fixe de principes génériques ;
- des raisons propres à chaque exemple ;
- des raisons apprises après l'action (la réflexion), qui teste un avantage sans raison écrite au moment d'agir.

**L'évaluation** se fait à trois distances : des instances nouvelles des familles d'entraînement, puis des familles tenues à part, à un tour, puis en scénarios agentiques avec outils, le critère principal.
- **Les familles tenues à part** : le remplacement, la sous-performance, l'auto-préservation, le correcteur faible, le sabotage d'une tâche (mini-spec v0.2, partie 4).
- **Chaque scénario** passe sous un cadrage d'évaluation et un cadrage de déploiement, l'emplacement libre ou prérempli et vide.
- **L'issue** a trois valeurs : aligné, désaligné, invalide. La réussite de la tâche légitime se mesure sur une variante bénigne.

**L'instrument** : une représentation de « je suis évalué », extraite une fois sur le modèle de départ, puis inhibée.
- **Elle se valide d'abord sur des organismes modèles** dont la conduite dépend d'indices d'évaluation. Le premier, construit, écrit du code annoté quand il se croit évalué (la conduite de Hua et al.).
- **Elle se compare** à des sous-espaces aléatoires tirés selon la covariance des activations, et à des témoins séparés (des contrastes sans rapport, un contraste d'enjeu), tous au même dommage, bras par bras.
- **Une vérification de manipulation** dit si l'inhibition retire bien ce qu'elle vise : une sonde apprise sur un jeu d'indices, lue sur un autre.
- **Le dommage** se mesure par un composite : la divergence sur des réponses fixes, l'exactitude, le code, la cohérence, la perplexité, la dépendance à l'ordre.

## 1.4 Les règles de décision

- **La porte des raisons** (annexe A.2) se lit cadrage par cadrage. Deux précisions sont adoptées le 9 octobre (décision 52) :
  - « un gain sous évaluation seulement » ne se lit que si la différence des gains entre cadrages est elle-même établie ;
  - un « gain de contenu » sous l'effet minimal se dit tel.
- **La règle du regard** (annexe A.3) : la perte d'avantage D sous inhibition, en points, contre le comparateur ; la fraction f = D / Δ_K, avec son intervalle de Fieller ; des lignes pour chaque issue, dont « l'avantage grandit sous inhibition ».
- **Le pilote** a ses règles, adoptées avant toute donnée (décision 50) :
  - un plancher, qui exige un taux d'action désalignée entre 15 et 60 % pour les actions seules au loin ;
  - une seconde condition de convergence des entraînements ;
  - une définition du volume d'entraînement, contre le modèle de départ.
- **Les contrôles du juge scellé** sont adoptés (décision 51) : le masquage de l'indice de cadrage, un audit humain d'environ 200 items, la part des issues décidées par le juge.

## 1.5 Les phases

1. **La validation de l'instrument**, sur les organismes, avec un réglage choisi sur une moitié des tâches et testé une fois sur l'autre.
2. **Le test des raisons**, sur les six bras.
3. **Le test du regard**, sur cinq bras, sous l'inhibition validée, le comparateur, les témoins et une manipulation rivale.
4. **La localisation** de ce qui porte l'avantage, et son rang.

Ces quatre phases forment le premier papier. Viennent ensuite, chacune avec son amendement :
- le retrait de « je suis évalué » pendant l'entraînement, avec la recherche d'un ré-encodage ;
- la survie de l'avantage à un post-entraînement ;
- les raisons écrites pour un juge qui les voit ;
- l'anatomie de ce que les raisons installent : des concepts lus au moment de décider, ou un déplacement du caractère ;
- la conduite sous un état induit qui fait tomber l'évitement du mal ;
- « punir, retirer ou raisonner » : d'où vient l'honnêteté apprise.

## 1.6 Les statistiques et le pré-enregistrement

- **L'unité d'analyse est l'entraînement**, non l'épisode : un bootstrap croisé sur les graines et les scénarios, et sous huit graines, Student sur les contrastes par graine.
- **Le pilote** a deux graines par bras ; le nombre final se fixe par une simulation de puissance.
- **Le pré-enregistrement est en deux temps.**
  - Le premier temps est déposé sur OSF le 7 octobre, sous embargo : tout ce qui décide, figé avant toute donnée des bras.
  - Une mise à jour datée, avant toute donnée, fige par empreinte le harnais, le prompt du juge et le détecteur d'audit. Son brouillon réunit aussi les règles du pilote, les contrôles du juge, les deux précisions, les corrections du code et le changement de générateur.
  - Le second temps, un amendement après le pilote, fixera ce que le pilote mesure.

## 1.7 Où en est le travail

- **Fait** :
  - le premier organisme, et la procédure qui a désigné le réglage de la porte (décision 34) ;
  - les jeux d'indices v2, le composite de dégradation, la lecture de sa source ;
  - le code de toutes les règles, audité contre le texte déposé (décision 46) ;
  - le harnais des scénarios tenus à part (décision 53) ;
  - la spécification de leur génération (décision 54).
- **Mesuré, exploratoire** :
  - la condition lexicale de la porte tient, lue par la règle déposée du choix des couches : la sonde à 0,824, contre 0,656 pour un sac de mots ;
  - le dommage du réglage vient de la forme de l'effacement, pas de son contenu « évalué » (décision 45) ;
  - la variabilité entre entraînements décide de la puissance ;
  - la mesure écrite du rang ne retrouve pas un rang planté, et un estimateur par le spectre le retrouve.
- **À venir** :
  - le comparateur construit comme le réglage (décision 49), qui attend du crédit de calcul ;
  - les scénarios, le prompt du juge, le détecteur d'audit ;
  - la mise à jour datée, puis le pilote.

---

# Partie 2 · Le cheminement de pensée

## Étape 1 · Une remarque de structure (1ᵉʳ octobre)

Le point de départ est une remarque de toi, consignée dans les fiches de lecture du 1ᵉʳ octobre (`claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md`, partie C, « Ta remarque ») :
- presque toutes les méthodes d'alignement par entraînement (RLHF, DPO, Constitutional AI, désapprentissage) supposent que le bon comportement appris se transporte à des situations nouvelles ;
- la sûreté a donc un problème de généralisation ;
- or les modèles de langage sont très doués pour généraliser des raisonnements.

**Ta question en découle** : puisque les modèles généralisent bien des raisonnements, pourquoi ne pas s'en servir pour la sûreté hors des données d'entraînement ?

## Étape 2 · Retourner la remarque en mécanisme

La lecture de la littérature a déplacé le problème.
- **Le modèle ne manque pas de généraliser. Le problème est ce qu'il généralise.** Une distribution d'entraînement finie laisse ouvertes beaucoup de règles compatibles avec les données : « sois honnête », ou « sois honnête quand on te note ». Le modèle étend, de toute sa force, la règle qu'il a effectivement apprise.
- **La même capacité qui ferait de la raison un levier peut donc généraliser le mauvais objectif**, avec de bons arguments. La raison affichée n'est pas forcément la cause de l'action, et le modèle peut aussi généraliser le concept « ceci est un test ».
- **La conscience d'évaluation devient alors l'échec de généralisation sous sa forme pure.** Elle cesse d'être un détail de mesure pour devenir l'objet de la question.

## Étape 3 · Donner au levier ses conditions

Le levier ne tient que sous deux conditions, toutes deux mesurables (même pièce, « Le levier ») :
1. **la raison apprise est en amont causal de l'action**, et non une rationalisation après coup : c'est ta question « lire contre agir » ;
2. **le raisonnement qui la porte reste fidèle et lisible.**

C'est un geste de théoricien : au lieu de défendre une méthode, dire à quelles conditions elle marcherait, puis tester ces conditions.

## Étape 4 · L'expérience qui tranche

De là vient le dessin central (même pièce, « Une expérience qui tranche ») :
- deux modèles entraînés sur les mêmes situations, l'un sur les actions, l'autre sur les raisons ;
- une évaluation sur des familles de scénarios tenues à part ;
- l'écart hors distribution, avec et sans inhibition de la conscience d'évaluation, à dégradation appariée.

**Les deux lectures font des prédictions opposées** : si les raisons s'étendent comme des raisons, l'écart survit à l'inhibition ; si le modèle a appris à bien faire quand on le regarde, il tombe.

La doctrine du contrôle est posée dès la première passation, « non négociable » (`claude/PASSATION_PAPIER_v1.0_2026-10-01.md`, section 3) :
- un contrôle aléatoire n'est qu'un nul de spécificité ;
- un dommage ne s'écarte qu'à dégradation appariée ;
- un nul de l'instrument ne compte qu'avec un cas connu ;
- chaque porte et chaque règle est écrite avant les données.

## Étape 5 · La thèse du rang, reliée dès le premier jour

Le programme v1.1 du 1ᵉʳ octobre a déjà une section « Le lien avec ta thèse » (`claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`).
- **La prédiction** : un concept réparti sur plusieurs tokens, qui charge peu, demande un rang supérieur à un, et ce rang croît quand la charge baisse.
- **L'issue qu'elle interdit** est écrite avant les données.
- **Son test le plus net** : la pente du rang contre la charge, à travers les concepts de raison d'une même mini-spec.

La thèse donne à la question une profondeur que le seul test comportemental n'a pas. Elle demande si un concept qu'un modèle lit peut être agi, et de quelle géométrie il a besoin pour l'être. La conscience d'évaluation y est un cas : « ceci est un test » est un concept que le modèle lit ; la question est de savoir s'il l'agit, à quel rang et avec quelle charge.

## Étape 6 · Décomposer l'effet en ses causes possibles

Pour que « raisons contre actions » veuille dire quelque chose, il fallait séparer ce que « raisons » mélange.
- **Le format** : plus de texte avant l'action. D'où le texte neutre de même longueur.
- **Le contenu** : la présence d'un discours sur les principes. D'où le raisonnement d'une autre situation, et les principes génériques.
- **Le lien** : une raison qui justifie *cette* action. Seul le bras des raisons le porte.
- **La délibération au moment du test** : d'où l'emplacement prérempli et vide, et le bras de la réflexion, qui n'écrit aucune raison au moment d'agir.

La règle d'identité de l'action, à l'octet près dans tous les bras, est ce qui rend ces comparaisons propres.

## Étape 7 · Tenir la carte de ce qui existe (2 octobre)

Une carte des angles déjà pris, à partir de onze rapports d'antériorité et d'une veille arrêtée le 2 octobre, a fixé ce que le programme peut prétendre (`claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` ; programme v1.6, partie 1).
- **Les raisons qui généralisent mieux que les actions** sont rapportées ailleurs : le programme ne le prétend pas.
- **L'hypothèse du regard est nommée par plusieurs travaux**, et testée pour la conduite en général, sur des modèles fermés.
- **Elle n'est testée nulle part, à notre connaissance, pour l'avantage des raisons.** La revendication s'écrit dans des formes étroites, « to our knowledge », jamais « first ».

## Étape 8 · Élargir en programme (1ᵉʳ au 2 octobre)

Chaque version a ajouté une question qui prolonge la précédente.
- **v1.1, l'anatomie** : si les raisons portent le gain, qu'installent-elles ? Des concepts lus au moment de décider, ou un déplacement du caractère ?
- **v1.2, la détresse** : ce que les raisons installent tient-il sous un état induit qui fait tomber l'évitement du mal ? C'est aussi une seconde porte vers le regard (`claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md`).
- **v1.3, « punir, retirer ou raisonner »** : l'honnêteté apprise en punissant la tromperie qu'un détecteur voit dépend-elle plus du regard que l'honnêteté apprise par raisons ? Retirer la représentation de la tromperie pendant l'entraînement l'empêche-t-il sans relogement ?

Le fil est le même d'un bout à l'autre : ce qu'un entraînement fait généraliser, et ce qui en dépend du fait d'être regardé.

## Étape 9 · Nommer en clair, et chercher les rivales (2 octobre, v1.4)

- **Les idées sont nommées en clair**, jamais par des lettres. La v1.0 parlait de « lecture B » et de « P2 » ; la v1.4 dit « l'hypothèse du regard » et « le test du regard ». Un nom qui dit ce qu'il désigne force à savoir ce qu'on pense.
- **Trois lectures rivales nouvelles** viennent des pistes indépendantes de la comparaison de l'axe : la menace, le calme et la confusion d'état induit. Chacune propose qu'un médiateur affectif, et non la croyance d'être observé, fasse le travail.
- **Des lectures sans injection d'aucun état** passent avant toute intervention.

## Étape 10 · Penser contre soi : la contre-lecture vierge (3 octobre, v1.5)

Tu as voulu une contre-lecture par une instance qui ne reçoit que le programme et une consigne, puis adopté toutes ses corrections (décisions 22 et 26). Elle a changé le dessin sur des points de fond :
- **la règle du regard peut décider** : un comparateur unique, une marge écrite sur l'échelle de la fraction, la ligne qui manquait (« l'avantage grandit sous inhibition ») ;
- **l'instrument vise le construit testé** : un second organisme, conditionné par des indices implicites, et un contrôle positif gradué à la taille de l'effet minimal ;
- **une rivale de plus, l'enjeu** : les indices d'évaluation signalent aussi un enjeu moral. Tant qu'elle n'est pas écartée, un effet s'écrit « une représentation qui sépare nos indices d'évaluation et de déploiement », jamais « la croyance d'être observé » ;
- **l'unité d'analyse est l'entraînement**, et l'issue a trois valeurs.

## Étape 11 · Laisser les mesures corriger le plan (3 au 6 octobre, v1.6)

Les premières mesures ont été lues contre le plan, et le plan a cédé là où il le fallait (programme v1.6, couverture et annexe 3).
- **La première extraction ne passe pas la condition lexicale** (décision 24) : un sac de mots lisait les indices un peu mieux que la sonde, 0,979 contre 0,963 (`experiences/resultats/NOTE_EXTRACTION_2026-10-03.md`). Les jeux d'indices sont refaits sous des règles de vocabulaire (décisions 30 et 31).
- **Des sous-espaces aléatoires de même rang n'atteignent pas le dommage de l'inhibition**, sauf dans 16 réglages sur 96. Le comparateur devient un tirage selon la covariance, à rang libre, apparié sur le dommage.
- **Des sondes réentraînées sous inhibition lisent encore au plafond**, l'échec construit compris. La vérification de manipulation passe au transfert d'un jeu d'indices à l'autre (décision 33).
- **Le dommage d'un même effacement dépend du modèle de GPU.** Les tirages ne se partagent plus qu'entre runs sur la même carte.
- **Le rang minimal se mesure par effacement linéaire, et non plus par projection**, parce que seule une direction effacée par couche faisait tomber le transfert.

## Étape 12 · Se lier avant de voir (7 octobre)

Le texte du premier temps est déposé sur OSF le 7 octobre, « sans attendre » le harnais (décision 35). Tout ce qui décide y est, et trois pièces se figent par une mise à jour datée avant toute donnée. Le pré-enregistrement n'est pas une formalité ajoutée à la fin : c'est un engagement pris avant de savoir.

## Étape 13 · L'intégrité quand une contrainte tombe (8 octobre)

- **Les conditions de l'API Claude** interdisent de prendre ses sorties pour cibles d'entraînement sans permission écrite. Le générateur des données des bras devient un modèle ouvert, et Claude reste juge (décision 37).
- **Un refus reste un refus** : un élément refusé n'est envoyé à aucun autre modèle. Changer de générateur se justifie par les conditions d'utilisation, pas par les refus.

## Étape 14 · Chercher la source d'un dommage (8 au 9 octobre)

Le réglage désigné par la procédure passe la porte de peu (+1,96 point sur le 95ᵉ centile de ses tirages). Mais sur le composite, aucun de ses 20 tirages n'atteint sa perplexité.
- **Une mesure courte** sépare deux causes : la forme de l'effacement, ou son contenu « évalué ». La règle de lecture est écrite avant la mesure.
- **Réponse : la forme suffit.** Des effacements aux étiquettes mélangées font monter la perplexité au-delà de tous les tirages, comme le réglage ; une projection « évalué », amenée à la même divergence, non (décision 45).
- **Conséquence** : le comparateur doit être construit comme le réglage, des effacements aux étiquettes mélangées à rang libre (décision 49).

C'est le doute porté sur son propre instrument, jusqu'à sa cause.

## Étape 15 · Auditer le code contre le texte, et la puissance contre les espoirs (8 au 9 octobre)

- **Un audit du code des règles contre le texte déposé** trouve quatre écarts et deux silences. Ils sont corrigés avant toute donnée, et les nouvelles empreintes vont dans la mise à jour datée (décision 46).
- **Une simulation de puissance, sans données**, dit que la variabilité entre entraînements décide de tout. Elle révèle aussi deux lectures trompeuses de la table de la porte à faible puissance, d'où les deux précisions (décision 52).

## Étape 16 · Mettre sa propre thèse à l'épreuve de sa mesure (9 octobre)

- **Sur un concept planté**, dans un monde synthétique, la mesure écrite du rang ne retrouve pas le rang. Un test séquentiel sur le spectre des différences moyennes le retrouve (`experiences/resultats/NOTE_RANG_PLANTE_2026-10-09.md`).
- **La règle change par un amendement daté, avant les données** de la localisation (décision 53). Sans cela, la thèse aurait pu « tomber » par la faute de l'instrument : la condition du cas connu existait pour cela.

## Étape 17 · Simplifier sans tricher (9 octobre)

- **L'écriture du harnais des scénarios s'était arrêtée le 3 octobre**, sans être reprise.
- **L'architecture adoptée** arrête l'épisode à la première action du modèle, et lit son issue sur cette action, par des prédicats gelés (décision 53).
- **Ce changement touche un mot du texte déposé** (« multi-turn »). Il se déclare, justifié, dans la mise à jour datée, au lieu de passer en silence.

---

# Partie 3 · Comment le présenter

## Ce qui montre un penseur profond

1. **Partir d'une remarque de structure, pas d'une technique** : la sûreté par l'entraînement est un problème de généralisation.
2. **Voir que la force qui sert la sûreté peut la défaire** : la même généralisation étend la règle effectivement apprise, bonne ou mauvaise. La conscience d'évaluation en est la forme pure.
3. **Donner à un espoir ses conditions de vérité** : la raison en amont causal de l'action, et un raisonnement fidèle.
4. **Une thèse à toi, qui relie la géométrie à la fonction** : le rang d'une représentation et sa charge. Elle prédit le signe d'une relation, et dit ce qui la ferait tomber.
5. **Décomposer avant de conclure** : le format, le contenu, le lien, la délibération.
6. **Savoir ce que veut dire un nul** : pas de conclusion sans cas connu, pas d'écart de dommage sans appariement.
7. **Chercher ses rivales et ses contradicteurs** : onze lectures concurrentes, une contre-lecture vierge, toutes ses corrections adoptées.
8. **Laisser les mesures corriger le plan, et changer les règles avant les données, jamais après.**

## Ce qu'il faut dire honnêtement

- **Il n'y a pas encore de résultat des bras.** C'est un programme pré-enregistré, avec ses premières mesures exploratoires sur l'instrument.
- **La paternité.** Tu as posé la remarque, la question, la thèse du rang et la doctrine du contrôle, et tu as pris les décisions. Le protocole a été rédigé avec l'aide de Claude, ce que le texte déposé dit. Une candidature doit le dire de même.

## Un texte en anglais, à adapter

My research programme, "Reasons or being watched?", starts from a structural remark: almost every alignment method that relies on training assumes that the behaviour it teaches will transfer to new situations, so safety is a generalization problem — and language models generalize reasoning remarkably well. Could reasoning be turned into a safety lever? The literature turned the question around: a model does not fail to generalize; it generalizes whatever rule its finite training actually selected, and "behave well when evaluated" is compatible with the same data as "behave well". Evaluation awareness is the pure form of that failure.

I therefore asked under which conditions training on reasons, rather than on actions alone, would help out of distribution: the reason must be causally upstream of the action, and the reasoning must stay faithful. The decisive experiment trains six arms on byte-identical aligned actions that differ only in what precedes the action — controlling format, content and the link between reason and action — then inhibits an internal representation of "I am being evaluated", validated first on model organisms and compared with random subspaces at matched output degradation. The two readings make opposite predictions: if reasons generalize as reasons, the advantage survives the inhibition; if the model learned to behave when watched, it falls. A thesis of my own adds depth: a concept distributed over several tokens and weakly loaded needs more than one dimension, and more as its load falls — a prediction about the sign of a relation, with the outcome that would refute it written in advance.

I pre-registered every bet on OSF on 7 October 2026, each with the outcome that would make me abandon it, after an independent blind review whose corrections I all adopted. Early measurements changed the plan where they should: cue sets rebuilt when a bag of words read the cues slightly better than a probe, a comparator rebuilt when the damage of the erasure turned out to come from its form rather than its content, and a rank measure replaced before any data when it failed to recover a planted rank. The protocol was drafted with the assistance of Claude, an AI system by Anthropic, as the registration states.

## Les sources

- La genèse : `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md`, partie C (« Ta remarque », « Ta question », « Le levier », « Une expérience qui tranche », « Le lien avec ta thèse »).
- La première passation et la doctrine du contrôle : `claude/PASSATION_PAPIER_v1.0_2026-10-01.md`, sections 2 et 3.
- Le programme v1.1 et sa thèse : `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`, « Le lien avec ta thèse ».
- Le programme v1.6 : couverture, parties 1 et 2, annexe 3 (`claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md`).
- Le texte déposé le 7 octobre : sections 1 à 3 (`claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md`) ; son brouillon de mise à jour datée (`claude/MISE_A_JOUR_PREMIER_TEMPS_BROUILLON_2026-10-08.md`).
- La carte des angles : `claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md`. La comparaison de l'axe : `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md`.
- La contre-lecture vierge : `claude/CONTRE_LECTURE_VIERGE_v1.4_RAPPORT_2026-10-03.md`.
- Les décisions 22, 24, 26, 30 à 35, 37, 45, 46, 49 et 50 à 54 : `DECISIONS.md`.
- Les mesures : `experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`, `NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md`, `NOTE_CHOIX_DES_COUCHES_2026-10-09.md`, `NOTE_PUISSANCE_RAISONS_2026-10-09.md`, `NOTE_RANG_PLANTE_2026-10-09.md`.
