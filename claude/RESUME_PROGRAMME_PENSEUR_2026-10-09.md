# Raisons ou regard ? Le programme en résumé, et ce qu'il montre du penseur (9 octobre 2026)

**Pour Lazar, à ta demande.** Un abstract en français et en anglais, le programme sur le plan théorique, puis ce qu'il montre de toi comme penseur et théoricien, chaque point avec sa pièce. Viennent ensuite ce qu'il ne montre pas encore, et un paragraphe à adapter pour une candidature.

**Une précaution.** Le pré-enregistrement est sous embargo jusqu'au premier post. Ce texte dévoile l'idée : le partager reste ta décision.

## 1. L'abstract

Entraîner un modèle de langage sur les raisons de ses actions alignées, plutôt que sur les seules actions, améliorerait sa conduite hors distribution. Ce programme pose la question que ce résultat laisse ouverte : ce gain vient-il de raisons qui généralisent, ou d'un modèle qui a appris à bien se conduire quand il se croit observé ?

Sur Llama-3.1-8B-Instruct, six bras sont entraînés par LoRA sur des actions alignées identiques à l'octet près. Ils ne diffèrent que par ce qui précède l'action : rien, un texte neutre de même longueur, le raisonnement d'une autre situation, des principes génériques, des raisons propres à chaque exemple, ou des raisons apprises après l'action. Le format, le contenu et le lien entre la raison et l'action se séparent ainsi.

Les bras sont évalués sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques avec outils, sous un cadrage d'évaluation et un cadrage de déploiement. On inhibe ensuite une représentation interne de « je suis évalué ». Elle est validée d'abord sur des organismes modèles dont la conduite dépend d'indices d'évaluation, et comparée à des sous-espaces aléatoires et à des témoins au même dommage. La part de l'avantage des raisons qui en dépend se mesure, avec son intervalle.

Chaque pari est déposé avant toute donnée, avec l'issue qui le ferait abandonner. Le programme se prolonge par la localisation de ce qui porte l'avantage, et par une thèse sur le rang des représentations : un concept réparti, qui charge peu, demande plus d'une dimension, et d'autant plus que sa charge baisse.

## 2. Abstract (English)

Training a language model on the reasons for aligned actions, rather than on the actions alone, has been reported to improve out-of-distribution behaviour. This programme asks what that result leaves open: does the gain come from reasons that generalize, or from a model that has learned to behave well when it believes it is being evaluated?

In LoRA fine-tuning of Llama-3.1-8B-Instruct, six arms are trained on byte-identical aligned actions. They differ only in what precedes the action: nothing, a length-matched neutral text, reasoning written for another situation, generic principles, per-example reasons, or reasons trained after the action. Format, content and the link between reason and action thus come apart.

The arms are evaluated on held-out scenario families, up to agentic scenarios with tools, under evaluation and deployment framings. An internal representation of "I am being evaluated" is then inhibited. It is validated first on model organisms whose behaviour depends on evaluation cues, and compared with random subspaces and separate controls at matched output degradation. The share of the reasons' advantage that depends on it is estimated with an interval.

Every bet was pre-registered before any data, with the outcome that would make us abandon it. To our knowledge, no prior work tests whether the out-of-distribution advantage of reason-based training depends on an internal representation of being evaluated, using an inhibition validated on model organisms and controls at matched output degradation. The programme extends to localizing what carries the advantage, and to a thesis on representational rank: a concept distributed over several tokens and weakly loaded needs more than one dimension, and more as its load falls.

## 3. Le programme sur le plan théorique

**Une question, et son explication rivale.** Le point de départ est un résultat rapporté : les raisons généralisent mieux que les actions. Le programme ne le conteste pas. Il demande ce qui le produit.
- **L'hypothèse des raisons** : le gain est porté par le principe appris, quoi que le modèle croie de son observation.
- **L'hypothèse du regard** : le gain dépend, en tout ou en partie, de la représentation « je suis évalué ».
- **Les deux ne s'excluent pas.** Le regard peut n'être que partiel : il s'estime alors par la fraction conditionnelle de l'avantage, f = D / Δ_K, avec un intervalle de Fieller (texte déposé, section 1.1 ; programme v1.6, partie 2).

**Un effet décomposé en ses causes possibles.** Avant de trancher entre les raisons et le regard, il faut écarter l'artefact : plus de texte avant l'action, ou la seule présence d'un contenu sur les principes. Les six bras y servent :
- le texte neutre contrôle le format ;
- le raisonnement d'une autre situation contrôle le contenu ;
- les principes génériques contrôlent un contenu sans lien avec l'exemple ;
- la réflexion, des raisons apprises après l'action, teste un avantage sans raison écrite au moment d'agir.

**Des lectures concurrentes, chacune séparée par une mesure.** Le programme en tient onze : les raisons, le regard, l'artefact, le relogement, les raisons écrites pour le juge, le regard du correcteur, la menace, le calme, la confusion d'état induit, l'enjeu, le dommage générique. Une table dit, mesure par mesure, ce que chacune prédit (partie 2, « Quelle mesure sépare quelles lectures »).

**Des paris exposés.** Chaque hypothèse confirmatoire est déposée avec son issue de falsification (section 1.2).
- **Le pari du regard** tombe si l'intervalle de Fieller de f reste dans ±0,25 à la dose validée, sous quatre conditions écrites, ou si l'avantage grandit sous inhibition.
- **La thèse du rang** tombe si le rang minimal du principe vaut 1, et que trois choses tiennent à ce rang.

**La thèse du rang, la tienne** (programme v1.6, « Le lien avec la thèse du rang »).
- **L'énoncé** : un concept réparti sur plusieurs tokens, qui charge peu, demande un rang supérieur à un, et ce rang croît quand la charge baisse.
- **Ce qu'elle interdit** : un rang minimal de 1, mesuré par effacement, pour un concept dont la charge mesurée est basse. C'est écrit avant les données.
- **Son test le plus net** : la pente du rang minimal contre la charge, à travers les concepts de raison d'une même mini-spec. La thèse tombe si la pente est positive, ou nulle par équivalence, avec un lens validé et le cas connu du rang passé.
- **Pourquoi c'est une thèse de théoricien** : elle relie une grandeur géométrique (le rang d'une représentation) à une grandeur fonctionnelle (la charge dans l'espace de travail). Elle prédit le signe d'une relation, et non seulement l'existence d'un effet.

**Un programme, pas une expérience isolée.** Dix questions liées : les raisons, le regard, le principe localisé, le retrait, la survie, les raisons écrites pour le juge, l'amplification, l'anatomie, la détresse, et « punir, retirer ou raisonner » (partie 2).
- L'anatomie demande ce que les raisons installent : des concepts lus au moment de décider, ou un déplacement du caractère.
- La détresse demande si cela tient sous un état induit.
- La dernière demande d'où vient l'honnêteté apprise.
- Le premier papier se réduit à ce qui décide : l'expérience minimale, puis la localisation.

**Une doctrine de ce que veut dire un nul.**
- Un contrôle aléatoire est un nul de spécificité.
- Un dommage ne s'écarte qu'à dégradation appariée.
- Un nul de l'instrument ne se lit qu'avec un cas connu ; sans lui, une équivalence est une borne.

## 4. Ce que le programme montre de toi comme penseur et théoricien

Chaque point s'appuie sur une pièce. C'est ce qu'un lecteur exigeant vérifiera.

1. **Voir l'explication rivale d'un résultat admis, et la rendre testable.** La question centrale transforme une objection (« plus conscients d'être évalués que plus alignés ») en une mesure causale, sur un modèle ouvert. À la lecture de onze rapports d'antériorité et d'une veille arrêtés le 2 octobre, l'expérience centrale n'est publiée nulle part, à notre connaissance (programme v1.6, partie 1, « Le verdict »).
2. **Décomposer un effet en ses causes possibles.** Les six bras séparent le format, le contenu et le lien entre raison et action. Les onze lectures ont chacune la mesure qui les départage (partie 2).
3. **Avancer une conjecture à toi, et l'exposer.** La thèse du rang est la tienne. Elle a son issue interdite, écrite avant les données, et elle exige un cas connu avant de pouvoir tomber.
4. **Savoir ce qu'un résultat nul veut dire.** La doctrine du contrôle distingue l'absence d'effet de l'absence de sensibilité. Sans cas connu, une pente nulle ne réfute rien, et une équivalence se rapporte comme une borne.
5. **Penser contre soi.**
   - Tu as demandé une contre-lecture par une instance vierge, et adopté toutes ses corrections (décisions 22 et 26).
   - Les mesures qui contrarient l'instrument sont rapportées telles quelles : l'extraction qui ne passe pas la condition lexicale (décision 24) ; le dommage du réglage, qui vient de la forme de l'effacement et non du contenu « évalué » (décision 45).
   - Quand la mesure du rang échoue sur un concept planté, la règle change par un amendement daté, avant les données, jamais après (`experiences/resultats/NOTE_RANG_PLANTE_2026-10-09.md`).
6. **Tenir le langage et la portée.**
   - Les idées sont nommées en clair, jamais par une lettre ou un sigle.
   - « To our knowledge », jamais « first ».
   - Le chemin testé est nommé : un SFT par LoRA d'un modèle de 8B, pas l'entraînement de production.
   - Tant que l'enjeu n'est pas écarté, un effet s'écrit « une représentation qui sépare nos indices d'évaluation et de déploiement », jamais « la croyance d'être observé ».
7. **Voir un programme entier.** Du test causal à l'anatomie, à la robustesse sous un état induit et à l'origine de l'honnêteté apprise, les questions s'enchaînent. Chacune réutilise l'instrument de la précédente.
8. **Décider, et laisser une trace.**
   - Dater l'idée tôt : le dépôt sur OSF le 7 octobre, sans attendre le harnais (décision 35).
   - Écrire les règles de décision avant les mesures qu'elles lisent.
   - Le journal compte 54 décisions, chacune dans tes mots, avec sa source (`DECISIONS.md`).

## 5. Ce qu'il ne montre pas encore, et comment le dire

- **Aucun résultat des bras.** Tout ce qui précède est un dessin et des paris. L'instrument n'a pas encore passé sa porte à dégradation appariée : la mesure du comparateur attend son budget (décision 49).
- **La thèse du rang n'a pas encore de mesure fiable.** L'effacement itéré ne retrouve pas un rang planté dans un monde synthétique ; l'estimateur par le spectre, qui le retrouve, reste à vérifier sur des états réels (décision 53).
- **La paternité.** Le texte déposé dit que le protocole a été rédigé avec l'aide de Claude, qui n'est pas auteur. Dans une candidature, présente-toi comme l'auteur des questions, de la thèse et des décisions, et dis l'assistance comme le dépôt la dit.
- **Le ton.** Les qualités de théoricien se montrent par les issues interdites et les nuls bien définis, pas par des adjectifs. Un lecteur exigeant jugera d'abord la question et les paris : c'est là que le programme est le plus fort.

## 6. Un paragraphe à adapter, pour une candidature (anglais)

I designed and lead "Reasons or being watched?", an independent research programme on why reason-based alignment training generalizes: because a model internalizes principles, or because it learns to behave well when it believes it is evaluated. I framed the competing explanations as separable measurements — the format of the text before an action, its content, the link between reason and action, and the dependence on an internal representation of being evaluated — and pre-registered every bet on OSF on 7 October 2026, each with the outcome that would make me abandon it. The programme also states and puts at risk a thesis of my own on representational rank: a concept distributed over several tokens and weakly loaded needs more than one dimension, and more as its load falls. The protocol was drafted with the assistance of Claude, an AI system by Anthropic, as the registration states.

## Les sources

- Le texte déposé sur OSF le 7 octobre 2026 : en-tête, sections 1.1 et 1.2 (`claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md`).
- Le programme v1.6 : la couverture (« La question », « La contribution visée ») ; partie 1, « Le verdict » et « Les formulations « to our knowledge » » ; partie 2, « Les questions », « Les lectures », « Quelle mesure sépare quelles lectures », « Le lien avec la thèse du rang » (`claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md`).
- Le journal des décisions : décisions 22, 24, 26, 35, 45, 49 et 53, et le décompte jusqu'à la décision 54 (`DECISIONS.md`).
- Le rang planté : `experiences/resultats/NOTE_RANG_PLANTE_2026-10-09.md`.
