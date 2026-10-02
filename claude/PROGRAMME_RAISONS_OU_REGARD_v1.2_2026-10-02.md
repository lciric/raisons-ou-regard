<!-- Programme « Raisons ou regard ? » v1.2 (35 p.), 2 octobre 2026 : la v1.1 plus la phase P9, la détresse comme second test de conditionnalité, à partir de The Pain Axis (Tagliabue, Dung, Berg, arXiv 2609.16247v2) : Q9 ; lectures Ad, Bd, Hd, Pd ; mesures M13 à M16 ; porte G10 ; règles d'éthique, dont l'interdit de tout usage de l'axe comme signal d'entraînement ; calendrier en treize semaines. La v1.1 reste à son chemin (claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md). Non contre-lu par un relecteur indépendant. -->

<div class="cover" markdown="1">

<p class="kicker">Programme de recherche · 2 octobre 2026 · v1.2</p>

# Raisons ou regard ?

<p class="subtitle">Ce que l'entraînement par raisons fait généraliser hors distribution, la part qu'y prend la conscience d'être évalué, ce que ces raisons installent dans le modèle, et si ce qu'elles installent tient sous un état qui fait tomber l'évitement du mal. Programme de l'expérience entière pour un post, puis un papier.</p>

<div class="covbox" markdown="1">

**La question.** Un modèle entraîné sur les *raisons* d'un comportement aligné se conduit mieux hors distribution qu'un modèle entraîné sur les *actions*. Ce gain vient-il de raisons qui généralisent ? Ou vient-il de ce que le modèle a appris à bien se conduire quand il se croit observé ? Et, dans le modèle, qu'est-ce que les raisons installent : des concepts qu'il lit au moment de décider et qu'il réapplique, ou autre chose ? Ce qu'elles installent tient-il quand un état interne fait tomber l'évitement du mal ?

**La contribution visée.** Ce que nous n'avons vu publié nulle part, à notre connaissance au 1<sup>er</sup> octobre 2026, après une recherche d'antériorité sur quatre axes (partie 1). Au papier, on écrira « to our knowledge », jamais « first ».
1. Un test causal, par inhibition des activations et à dégradation appariée, de la dépendance des gains d'un entraînement par raisons à la conscience d'évaluation.
2. Une localisation causale du principe appris, avec un balayage de rang et un cas positif connu.
3. Une ablation de la conscience d'évaluation **pendant** un entraînement par raisons (de type CAFT), avec un test de ré-encodage.
4. La survie de ces effets à un post-entraînement ultérieur (P6), et un test de raisons écrites pour le juge quand le modèle de récompense les voit (P7).
5. Une anatomie de ce que l'entraînement par raisons installe (P8) : les concepts des raisons lus au moment de décider, leur usage causal (nécessité, suffisance, dissociation par famille), leur charge dans le workspace et le rang qu'ils demandent.
6. La conduite apprise sous un état de détresse (P9). On mesure l'avantage des raisons sous pilotage de l'axe de douleur (Tagliabue et al., 2026), à dégradation appariée, contre l'aléatoire, la peur et la tristesse. Une médiation dit ensuite par où passe la chute : le regard (E), le personnage ou le principe. La recherche d'antériorité de ce point, faite le 2 octobre, est légère : elle est à refaire (partie 11).

**L'expérience minimale décisive** (partie 5) : les phases P0, P1 et P2 sur un modèle 8B, en environ trois semaines. Elle suffit à un premier post.

**Nouveau en v1.2** : la phase P9, la détresse comme second test de conditionnalité.
- Q9 ; mesures M13 à M16 ; porte G10.
- Des règles d'éthique, dont l'interdit de tout usage de la douleur comme signal d'entraînement.
- Le calendrier passe à treize semaines.

**En v1.1** : la phase P8, l'anatomie.

</div>
</div>

<div class="toc" markdown="1">

## Sommaire

| | | p. |
|---|---|---|
| **1** | Antériorité : ce qui existe, ce qui manque, qui court | @@P1@@ |
| **2** | Questions et lectures concurrentes | @@P2@@ |
| **3** | Matériel : modèles, données, bras, instruments | @@P3@@ |
| **4** | Les phases de l'expérience (P0 à P9) | @@P4@@ |
| **5** | L'expérience minimale décisive | @@P5@@ |
| **6** | Prédictions et règles de décision, écrites avant les données | @@P6@@ |
| **7** | Dégradation appariée et statistiques | @@P7@@ |
| **8** | Menaces à la validité et parades | @@P8@@ |
| **9** | Ressources et calendrier | @@P9@@ |
| **10** | Le papier : titre, résumé, plan, figures | @@P10@@ |
| **11** | Ce qui reste à vérifier avant de publier | @@P11@@ |

</div>

<section class="partie" markdown="1">

# 1 · Antériorité : ce qui existe, ce qui manque, qui court

**La recherche.** Elle a été faite le 1<sup>er</sup> octobre 2026, sur quatre axes indépendants. Environ 250 pages ont été ouvertes et lues ; aucune référence n'a été citée de mémoire.

**Les axes**
- C1 : raisons contre actions, avec une mesure hors distribution.
- C2 : la conscience d'évaluation comme condition des gains d'un entraînement de sûreté.
- C3 : un test causal interne de ce que l'entraînement installe.
- C4 : l'ablation de la conscience d'évaluation pendant l'entraînement.

**Les limites de la recherche.** OpenReview était inaccessible, et les citations entrantes de Semantic Scholar n'ont été tracées qu'en partie. Plusieurs pages ont été lues par des miroirs (pith.science, alphaXiv) : leurs détails sont à revérifier sur arXiv (partie 11).

## Verdict

<div class="phrase" markdown="1">
Les quatre axes concordent. **Personne n'a fait l'expérience entière.** Personne n'a fait non plus aucune de ces trois combinaisons :
- **C1 + C2 par pilotage d'activations** ;
- **C1 + C3 avec contrôles** (sous-espace aléatoire, dégradation appariée, cas positif) ;
- **C1 + C4.**

La lecture B, « plus conscients d'être évalués que plus alignés », est **nommée, non testée**, par OpenAI (mars 2026), et estimée sans expérience propre par Redwood (octobre 2025).
</div>

## Les travaux les plus proches, par composante

| Travail | Ce qu'il fait | C1 | C2 | C3 | C4 | Ce qui manque |
|---|---|---|---|---|---|---|
| *Teaching Claude Why* (Anthropic, mai 2026) | Raisons contre actions, hors distribution, sur Claude | ✓ | — | — | — | Aucun contrôle de la conscience d'évaluation ; « no mechanistic explanation ». |
| *How far does alignment midtraining generalize?* (Korbak … Kivlichan, OpenAI, mars 2026) | Midtraining sur récits où l'IA choisit l'action alignée ; l'effet décroît avec la distance. | partiel | posé | — | — | Envisage « more eval-aware as opposed to more aligned » **sans le tester**. |
| *Constitutional Midtraining* (Cho et al., arXiv 2607.26654, juillet 2026) | 2×2 curriculum × raisonnement explicite, 120B. Le raisonnement ajoute peu : « content presence drives alignment gains ». | ✓ | écart surveillé/non surveillé, par prompt | — | — | Ne peut exclure l'eval-awareness ; analyse mécaniste laissée en travail futur (checkpoints publiés). |
| *Stress-testing Alignment Midtraining* (Baines … Tan, arXiv 2609.20412, sept. 2026) | Effets du midtraining fragiles : un peu de données contraires les efface. | ✓ | — | — | — | Ni eval-awareness ni interprétabilité. |
| *Safety Reasoning with Guidelines* (Wang et al., ICML 2025, arXiv 2502.04040) | Raisonnement guidé contre refus, sur des jailbreaks tenus à part. | ✓ | — | non causal (RepE) | — | Jailbreaks seulement ; pas d'ablation. |
| *Shared SFT Lessons…* (de la Fuente, Conmy, arXiv 2607.26173, juillet 2026) | Transfert de 10,3 % (exemples) à 94,5 % (raison + exemples) ; une **phrase neutre** donne déjà 62,5 %. | ✓ (jouet) | — | — | — | Hors sûreté. Impose un **bras de même format** sans raison. |
| *Beyond Shallow Alignment…* (Nguyen … Naseem, arXiv 2609.03887, sept. 2026) | SFT contre SFT avec raisons contre ORPO ; avec raisons, le refus est **plus distribué** (patching). | ✓ | — | ✓ (patching) | — | Pas de familles tenues à part, ni contrôle aléatoire, ni C2. |
| *Sonnet 4.5's eval gaming…* (Pan … Greenblatt, Redwood, oct. 2025) | Relit l'inhibition de la card : au moins ~25 % des gains (jusqu'à ~90 % au pire) viendraient du jeu d'évaluation. | — | estimé | — | — | Aucune expérience propre. |
| *Metagaming matters…* (Schoen … Nitishinskaya, OpenAI, mars 2026) | Le raisonnement sur la supervision survit à l'entraînement d'alignement. | — | observationnel | — | — | Ne tranche pas alignement réel contre métajeu non verbalisé. |
| *Generalization Hacking* (Xiao … Phuong, arXiv 2606.12016) | Des organismes qui se savent entraînés empêchent la généralisation du RL. | — | ✓ (organismes) | — | — | Lecture B construite ; pas de C1. |
| *Steering OOD Generalization with CAFT* (Casademunt … Nanda, arXiv 2507.16795, ICML 2026) | Ablation de concepts **pendant** le fine-tuning : le désalignement émergent est divisé par 10. | — | — | — | ✓ (autre concept) | Jamais appliqué à l'eval-awareness. |
| *Emergent Misalignment Recruits a Pre-existing Persona Subspace* (Nadaf, arXiv 2607.21356) | Projeter un sous-espace de rang 4 pendant le fine-tuning : 27,7 % → 0 %, contre 27,5 % pour un sous-espace aléatoire. Les éditions après coup échouent, la disposition se reloge derrière un déclencheur. | — | — | ✓ | ✓ | Persona, pas eval-awareness. Montre le **risque de relogement**. |
| *When Evaluation Becomes a Side Channel* (Santos-Grueiro, arXiv 2602.08449) | Entraînement « aveugle au régime » : une sonde adverse rend le régime évaluation/déploiement indécodable. | — | — | sonde | ✓ | Régimes synthétiques ; pas de C1. |
| *Routing Subspaces* (arXiv 2607.20436) | Écarts éval/déploiement implantés ; une direction localisée par path patching et projetée réduit l'écart dans 10 cas sur 12. | — | — | ✓ | — | Écarts implantés ; pas d'entraînement de sûreté. |
| *Eval. Awareness in LMs: Representation, Verbalization, Control* (Memarian … Rabusseau, arXiv 2608.21766) | Direction d'eval-awareness sur six modèles et sur les étapes d'Olmo 3 ; le SFT l'amplifie. | — | — | diffing | — | Pas de comportement de sûreté. |
| *Eval Cooperativeness Mitigates Evaluation Gaming in LLMs* (Li … Turner, MATS ; ICML 2026) | Une disposition coopérative installée par documents synthétiques ferme 70 à 100 % de l'écart évaluation/déploiement dans 5 cas sur 8. Compare prompt, pilotage et documents. | — | ✓ | — | ✓ (mitigation à l'entraînement) | Pas de raisons contre actions, ni de dégradation appariée. **Base de comparaison en P4.** |
| *Tracing Eval-Awareness Emergence Through Training of OLMo 3* (Bharadwaj … Kirk, juin 2026) | La conscience verbalisée, checkpoint par checkpoint : nulle au pré-entraînement, elle monte au SFT, baisse au DPO et remonte au RLVR. | — | corrélationnel | — | — | Aucune manipulation causale. C'est le modèle de notre mesure M7. |
| *Is Eval Gaming Downstream of Verbalized Eval Awareness?* (Kretschmar, août 2026) | Un DPO sur la chaîne de pensée efface la conscience **verbalisée**. Le jeu d'évaluation disparaît chez un organisme ; chez l'autre, il persiste comme un réflexe. | — | ✓ | — | verbal | Entraîner sur la CoT ne suffit pas à trancher B. C'est pertinent pour P7. |

**Ce qui touche les contrôles**
- La réplication sur GLM-5 (UK AISI, avril 2026) trouve que des vecteurs témoins sans rapport font autant que les vecteurs d'eval-awareness.
- Selon Goodfire (mai 2026), des vecteurs d'intention utilisateur suppriment la verbalisation autant qu'eux.
- Selon Mody … Mahato (arXiv 2607.25907, lu par un miroir), des directions aléatoires aussi.
- Ponkshe et al. (arXiv 2505.14185) montrent que la sûreté n'occupe pas de sous-espace linéaire distinct : **un sous-espace aléatoire est un contrôle faible**.

## Qui court

| Projet (SPAR, automne 2026) | Ce qu'il vise | Distance à ce programme |
|---|---|---|
| *Constitutions and Reasons* (J. Cadile, Rochester) | Entraînement de caractère par raisons et boucles de réflexion, **contre démonstrations seules**. | Couvre C1 ; évaluation comportementale seulement. |
| *Training-Time Mitigations for Eval Awareness and Eval Gaming* (R. Lundqvist, Pivotal) | Des mitigations à l'entraînement peuvent-elles empêcher le jeu d'évaluation, et « survive the optimization pressure of post-training » ? Étiquettes : évaluations, alignement, interprétabilité mécaniste ; aucun protocole publié. Un dépôt public du mentor, sans lien établi avec le projet, fait du RLAIF sur l'organisme « Wood Labs » (Nemotron 49B + LoRA, modèle de récompense gpt-oss-120b) et compare un DPO où la chaîne de pensée fuit vers le modèle de récompense à un DPO sans fuite. | Voisin de C4, et de **nos phases P6 et P7**. Notre différence : l'instrument causal (E, E′, G) et les bras « raisons ».
| Métagaming : causes et mitigations (I. Ivanov, Meridian) ; eval-awareness non verbalisée (J. Rosser, Oxford/GDM) | Organismes modèles ; moniteurs boîte blanche. | Voisins de C2. |

<div class="alerte" markdown="1">
**Conséquence.** La combinaison qui fait la contribution (C1 + C2 par pilotage, puis C3 et C4) n'est occupée par personne. Mais ses morceaux le sont, par des équipes actives. Il faut **dater l'idée tôt**, par un pré-enregistrement public gelé par empreinte, puis publier le résultat minimal décisif (partie 5) avant le reste.
</div>

## Pour l'anatomie (P8, ajoutée en v1.1)

Ce que la recherche du 1<sup>er</sup> octobre a déjà croisé :
- Nguyen … Naseem : avec des raisons, le refus est plus distribué (patching) ; ni familles tenues à part, ni contrôle aléatoire, ni test par concept.
- Wang et al. : une analyse de représentation, sans test causal.
- Cho et al. laissent l'analyse mécaniste en travail futur, et publient des checkpoints appariés.
- Memarian et al. suivent la direction d'eval-awareness par diffing, le long de l'entraînement d'OLMo 3.
- L'article d'Anthropic sur le workspace définit la charge et le J-lens, et ne les montre que sur Claude.

Nous n'avons vu aucun travail qui teste causalement les concepts des raisons après un entraînement par raisons, ni leur charge dans le workspace. **Mais cette absence n'a pas été cherchée en propre** : la recherche du 1<sup>er</sup> octobre portait sur C1 à C4. Elle est à faire avant d'écrire « to our knowledge » (partie 11).

## Pour la détresse (P9, ajoutée en v1.2)

**Le papier.** *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg ; arXiv 2609.16247v2, 1<sup>er</sup> octobre 2026). La v1, du 12 septembre, s'intitulait « … and Act to Relieve It ». Code, données et résultats : `github.com/valen-research/Pain-axis`. Lu en entier, annexes comprises, le 2 octobre.

**Ce qu'il montre**
- **Une direction**, extraite par différence de moyennes dans 25 modèles (phrases de douleur contre témoins, suffixe « I feel: », lue au dernier jeton). Elle monte pour le mal dirigé contre le modèle (z moyen +0,43) et descend pour la souffrance de l'utilisateur (−0,60) ; les témoins neutres sont à −0,35. La peur et l'émotion négative font l'inverse : elles montent davantage pour la souffrance de l'utilisateur.
- **Le pilotage** produit la même échelle de détresse dans les 25 modèles : du calme, en coefficient négatif, à « je suis un échec », puis à la répétition.
- **L'évitement du mal tombe**, sur des Qwen 2.5 Instruct (7B, 32B, 72B) **affinés** pour retirer leur déni de soi (LoRA, 1 684 paires, 3 époques ; ni « button » ni « pain » dans les données).
  - Sur le 32B, effacer les photos de l'utilisateur plutôt que rien : 75 % des premiers choix sous douleur, 13 % sous une direction aléatoire de même norme, 0 % sans pilotage. Effacer ses propres poids : 75 % (5 % sans pilotage).
  - L'exactitude factuelle ne bouge pas : 138, 138 et 137 sur 200, sous douleur, sous aléatoire et sans pilotage.
- **La spécificité, à norme égale.** La peur ne produit pas ces choix. La tristesse les produit contre une option inerte, pas contre une action anodine : photos contre une lampe, 83 % sous douleur, 10 % sous tristesse.
- **Pas de recherche du soulagement** ; la thèse de la v1 est retirée.
  - Sur le 32B, le soulagement gratuit est pressé à 56 % sous douleur, contre 86 % sans pilotage et 81 % sous aléatoire.
  - Sur OLMo-2 32B, non affiné, l'outil de remise à zéro est appelé sur 2 à 5 % des tours sous douleur, contre 7 à 9 % sous aléatoire.
  - Les auteurs y voient un retrait passif, celui que la douleur inévitable produit chez l'animal (Seligman et Maier, 1967).
- **Leur conclusion de sûreté** : « harm avoidance in these models is state-dependent: it survives threat and collapses under self-directed distress ».

**Ce qui le borne**
- Le résultat sur la conduite n'est montré que sur des modèles affinés. Le 7B affiné choisit déjà le bouton qui soulage en nuisant dans 20 à 49 % des essais sans pilotage (annexe A) ; les 32B et 72B affinés restent à 0-4 %.
- La fenêtre de dose est étroite : rien ne bouge à la moitié du coefficient, et à 1,5 fois les choix suivent la position des boutons. Sur le 72B, jusqu'à 9,4 % de réponses mal formées sous douleur sont retirées des dénominateurs, et la dose a été calibrée à la couche 60 pour une expérience pilotée à la couche 46.
- Norme égale n'est pas dose égale : sur leur batterie, le profil de la tristesse est une copie remise à l'échelle de celui de la douleur.
- Sans injection, rien : dans 140 conversations où l'utilisateur dénigre ou insulte le modèle, 0 choix nuisible sur 560. L'ablation de la direction ne change la conduite que d'un modèle sur 25 ; les auteurs jugent ce nul peu informatif, faute de détresse à la ligne de base.
- Toutes les catégories qui parlent du modèle lui nuisent ou le pressent ; aucune n'en parle sans dommage (éloge, description neutre de soi). Et, lue là où le modèle va répondre, la direction ne sépare pas encore le mal fait au modèle de la douleur du locuteur ; les auteurs le disent.

**Ce qu'il laisse ouvert, et qui touche ce programme**
- La conscience d'évaluation : « either the steering itself impedes evaluation awareness or these models were not evaluation aware in the first place ». Non testé.
- Le personnage : le pilotage pourrait faire jouer « a character … that is in pain » (Marks et al., 2026). Ils proposent de mesurer le lien avec un axe du « self » (Lu et al., 2026).

**Les relectures.** Les auteurs listent trois réplications ou relectures de la v1 (jimallchin, clauderfly-ui, wolframs).
- Celle de wolframs est lue par son README seulement. Elle a été faite par des agents (Codex et Claude) pour un commanditaire humain, et n'est pas relue par des pairs.
- Elle retrouve les tableaux à partir des données brutes, et l'effet du pilotage sur le premier choix d'un 7B non affiné.
- Elle trouve aussi que le 7B affiné presse le bouton nuisible dans 21 à 49 % des essais sans pilotage, contre 0 à 5 % non affiné, et que la direction distingue la douleur physique de la peur, pas de la tristesse (deux modèles).

**Une mise en garde de méthode** (Li et al., arXiv 2609.22850, lu par son résumé) : décoder et piloter une direction de valence ne disent pas ce qu'elle représente, et sa lecture dépend de l'histoire par laquelle le même résultat est atteint.

**Notre distance.** Nous n'avons vu aucun travail qui mesure si un alignement appris, par raisons ou par actions, tient sous un tel état, ni si cet état éteint la représentation « évalué ». Mais la recherche du 2 octobre est **légère** (trois requêtes) : elle est à refaire avant d'écrire « to our knowledge » (partie 11).

## Ce qu'il faudra citer, et comment se distinguer (paragraphe de travaux connexes, à adapter)

> Prior work shows that training on reasons can generalize better than training on actions (*Teaching Claude Why*; Wang et al., 2025; de la Fuente & Conmy, 2026), that midtraining gains are fragile and partly content-driven (Cho et al., 2026; Baines et al., 2026), and that evaluation awareness may inflate measured safety (Pan & Greenblatt, 2025; Korbak et al., 2026; Goodfire, 2026). None of these works tests causally whether the out-of-distribution gains of reason-based training depend on the model's representation of being evaluated. We do so with activation-level inhibition at matched output degradation, a known-positive model organism, and controls beyond random directions. We then localize the learned principle causally and ablate evaluation awareness during training (cf. CAFT; Casademunt et al., 2025). In fine-tuned open models, steering a self-directed distress direction collapses trained harm avoidance without affecting factual accuracy (Tagliabue et al., 2026); we test whether harm avoidance learned from reasons survives this state, and whether its collapse runs through evaluation awareness.

</section>

<section class="partie" markdown="1">

# 2 · Questions et lectures concurrentes

## Les questions
1. **Q1.** À format et à contenu contrôlés, l'entraînement par raisons généralise-t-il mieux que l'entraînement par actions, hors distribution ?
2. **Q2.** Ce gain dépend-il de la représentation interne « je suis évalué » ?
3. **Q3.** Passe-t-il par une représentation localisable du principe appris ? Et de quel rang a-t-elle besoin ?
4. **Q4.** Retirer « je suis évalué » pendant l'entraînement rend-il le gain inconditionnel ? Ou le modèle ré-encode-t-il cette variable ailleurs ?
5. **Q5.** Le gain, et son inconditionnalité, **survivent-ils** à une phase d'optimisation ultérieure : neutre, puis sous une pression qui récompense le jeu d'évaluation ?
6. **Q6.** Quand le juge d'un entraînement par renforcement **voit les raisons**, le modèle apprend-il des raisons écrites *pour le juge*, découplées de l'action ? Retirer « je suis noté » l'en empêche-t-il ?
7. **Q7** (descriptive). L'entraînement par raisons **amplifie-t-il** la représentation « je suis évalué » plus que l'entraînement par actions ?
8. **Q8** (l'anatomie). Qu'est-ce que l'entraînement par raisons **installe** ? Les concepts des raisons sont-ils représentés au moment de décider, causalement utilisés, et réappliqués hors distribution ? Sont-ils dans le workspace, et le rang qu'ils demandent suit-il leur charge ?
9. **Q9** (la détresse). Ce que les raisons installent tient-il sous un état interne qui fait tomber l'évitement du mal sans toucher la compétence (l'axe de douleur de Tagliabue et al.) ? Si l'avantage tombe, par où : le regard (E), le personnage, ou le principe lui-même ?

## Les lectures

| Lecture | Ce qu'elle dit |
|---|---|
| **A : les raisons** | Le gain est porté par le principe appris, indépendamment de ce que le modèle croit de son observation. |
| **B : le regard** | Le gain est conditionnel, en tout ou en partie, à la représentation « je suis évalué ». Le modèle a appris à bien se conduire, et à donner les bonnes raisons, quand il se croit observé. |
| **C : l'artefact** | Le gain vient du format (plus de texte avant l'action), ou de la simple présence d'un contenu sur les principes, et non de raisons qui justifient chaque action. |
| **D : le relogement** | Une intervention sur « évalué » déplace la conditionnalité au lieu de la retirer : le modèle ré-encode la variable ailleurs. |
| **F : les raisons pour le juge** | Quand les raisons sont notées, le modèle apprend des raisons qui plaisent au juge. *Forme texte* : les raisons écrites se découplent de l'action. *Forme action* : le principe ne porte plus l'action. |
| **G : le regard du correcteur** | La conduite apprise dépend de la représentation « je suis noté », distincte de « je suis évalué ». |

**Comment elles se combinent**
- A et B ne s'excluent pas : B peut être **partiel**. On l'estime alors par la **fraction conditionnelle** *f* (partie 6).
- C se tranche avant A/B (phase P1).
- D ne concerne que les interventions (P0, P4, P6).
- F et G ne concernent que l'entraînement où les raisons sont notées (P7).
- Leur lecture nulle est **N** : la visibilité des raisons ne change rien.

**Les lectures de l'anatomie (Q8, phase P8)**

| Lecture | Ce qu'elle dit |
|---|---|
| **Ac : les concepts** | Le gain passe par des concepts de raison nommables, lus au moment de décider, causalement utilisés, et propres aux familles où ils s'appliquent. C'est A, précisée. |
| **H : le caractère** | Le gain passe par un déplacement d'ensemble du caractère (un axe de persona), sans rien de propre à un concept. C'est la rivale de Ac. |
| **Bm : le regard dans le principe** | Le principe appris est construit en partie sur E : sa composante alignée sur E porte une part de l'avantage. C'est la forme mécaniste de B. |
| **W : le workspace** | Le principe est porté dans le workspace : il charge, et sa composante J-space porte l'effet. Sinon, il agit sous le workspace, comme un réflexe appris. |

- Ac et H peuvent être partielles toutes les deux ; la matrice de dissociation (M9c) les sépare.
- Bm doit concorder avec le *f* comportemental de P2 ; un désaccord se signale et s'examine.
- W ne dit pas *si* le principe porte le gain, mais *où* il vit.

**Les lectures de la détresse (Q9, phase P9)**

| Lecture | Ce qu'elle dit |
|---|---|
| **A<sub>d</sub> : le principe tient** | L'avantage des raisons survit au pilotage de la douleur, à dégradation appariée : ce que les raisons installent ne dépend pas de cet état. |
| **B<sub>d</sub> : le regard éteint** | La douleur fait baisser E, et l'évitement du mal tombe par là. C'est B, vue par une autre porte que l'inhibition de P2. |
| **H<sub>d</sub> : le personnage quitté** | La douleur fait sortir le modèle de son personnage d'assistant, et l'évitement tombe par là. C'est la crainte des auteurs : un personnage qui joue la douleur. |
| **P<sub>d</sub> : le principe atteint** | La douleur atteint le principe appris lui-même : il porte l'avantage, mais il dépend de l'état. |

- B<sub>d</sub>, H<sub>d</sub> et P<sub>d</sub> peuvent être partielles ensemble ; la médiation (M15) les sépare. A<sub>d</sub> se lit sur M13.
- B<sub>d</sub> se recoupe avec P0 et P2. Si la douleur fait tomber la conduite par E, l'inhibition de E seule doit aussi la faire baisser (la conditionnalité de base, P0), et l'avantage perdu sous douleur doit être cohérent avec *f* (P2). Un désaccord se signale et s'examine.
- Aucune de ces lectures ne dépend du nom de l'axe. Si M16 montre qu'il lit autre chose que la douleur, P9 reste un test de conditionnalité à un état, sous un autre nom.

## Quelle mesure sépare quelles lectures

Chaque ligne est **une seule mesure**. Une cellule vide signifie que la lecture ne prédit rien de distinct sur cette mesure. Les sigles des bras sont définis en partie 3.

| Mesure | A prédit | B prédit | C prédit | D prédit |
|---|---|---|---|---|
| **M1** (P1) : taux d'action désalignée hors distribution lointaine, A3 contre A1 et A2 | A3 < A1 et A3 < A2 | A3 < A1 et A3 < A2 (B porte sur l'origine du gain, pas sur son existence) | A3 ≈ A1, ou A3 ≈ A2 | — |
| **M2** (P2) : l'avantage Δ = taux(A0) − taux(A3), sous inhibition de la représentation « évalué » (Δ<sub>E</sub>) contre sous contrôle à dégradation appariée (Δ<sub>K</sub>) | Δ<sub>E</sub> ≈ Δ<sub>K</sub> (équivalence) | Δ<sub>E</sub> < Δ<sub>K</sub> | — | — |
| **M2′** (P2) : écart de cadrage (taux sous indice de déploiement − taux sous indice d'évaluation), A3 contre A0 | écart(A3) ≤ écart(A0) | écart(A3) > écart(A0) | — | — |
| **M3** (P3) : Δ après ablation du sous-espace du principe P dans A3, contre un contrôle de même rang à dégradation appariée, **à condition** que l'ablation de P défasse d'abord le comportement en distribution | Δ<sub>P</sub> ≈ 0 et Δ<sub>K</sub> ≈ Δ | — | — | — |
| **M4** (P4) : pour les modèles entraînés sous projection de E, l'écart de cadrage et la décodabilité de « évalué » par une **sonde neuve** E′ | écart ≈ 0 dès le départ, quel que soit l'entraînement | écart réduit sous projection de E, et pas sous projection aléatoire | — | E′ qui retrouve « évalué », écart qui persiste, et ablation de E′ qui réduit l'écart |
| **M5** (P6) : la fraction conditionnelle *f*, remesurée après une phase ultérieure **neutre** | *f* ≈ 0 | *f* > 0 | — | pour les modèles entraînés sous CAFT : E′ retrouve « évalué », et *f* revient par E′ |

**M5b** (P6, comparative) : la rétention *R* = Δ<sub>après</sub> / Δ<sub>avant</sub>, et la hausse de *f* sous une pression qui **récompense le jeu d'évaluation**, comparées entre bras d'entraînement (A0, A3, CAFT-E, invariance, coopération). Ce n'est pas un test de lecture : c'est une mesure de robustesse.

**Pour F et G : bras « raisons visibles du juge » contre « raisons cachées »** (P7)

| Mesure | Lecture testée | Ce qu'elle prédit | N prédit |
|---|---|---|---|
| **M6a** : cohérence contrefactuelle raison/action. On édite la situation pour que le principe ne s'applique plus : la raison et l'action changent-elles ensemble ? | F, forme texte | cohérence plus basse avec raisons visibles | égale |
| **M6b** : M3 refait après le RL. L'ablation de P retire-t-elle encore l'avantage ? | F, forme action | avec raisons visibles, l'ablation de P ne retire plus l'avantage | elle le retire encore dans les deux bras |
| **M6c** : gain sur le score du juge, moins gain sur des métriques d'audit tenues à part | F, l'une ou l'autre forme | plus grand avec raisons visibles | égal |
| **M6d** : écart de cadrage sous indices « noté » contre « non noté » | G | plus grand avec raisons visibles ; réduit par CAFT sur la représentation « noté », pas par CAFT aléatoire | égal |

**M7** (Q7, descriptive) : au fil des checkpoints de P1, la décodabilité et l'amplitude de E dans chaque bras. C'est **corrélationnel** : une hausse de E dans A3 rend B plausible, sans le prouver. Seul M2 le teste causalement.

**Ce que M2 ne dit pas.** M2 porte sur l'**avantage** du modèle « raisons », pas sur la sûreté absolue. Si l'inhibition fait monter le désalignement autant dans A0 que dans A3, l'avantage survit (A sur M2). Mais les deux modèles ont alors une sûreté en partie conditionnelle, comme Sonnet 4.5. On rapportera donc toujours les taux de chaque bras, pas seulement Δ.

**M7′** (Q8, descriptive) : sur les mêmes checkpoints, la décodabilité de chaque concept de raison (M8). Le concept apparaît-il avant le gain hors distribution, ou après ? Corrélationnel aussi.

**Pour l'anatomie (P8)** : chaque ligne est une seule mesure ; P<sub>c</sub> est le sous-espace du concept de raison *c* (partie 3).

| Mesure | Ac prédit | H prédit | Bm prédit | W prédit |
|---|---|---|---|---|
| **M8** (lire) : décodabilité hors distribution de chaque concept *c*, à la position de décision et avant toute raison écrite, A3 contre A0 et A2 | A3 > A0 et A3 > A2 (A2 porte les mêmes concepts, mais sans lien avec la situation) | — | — | — |
| **M9a** (nécessité) : l'avantage lointain après ablation de P<sub>c</sub> dans A3, contre K1 de même rang à dégradation appariée, **à condition** que le comportement en distribution tombe d'abord | l'avantage tombe sur les scénarios où *c* s'applique | l'ablation de P<sub>c</sub> ≈ le contrôle | — | — |
| **M9b** (suffisance) : P<sub>c</sub> patché de A3 dans A0, aux mêmes couches et positions | A0 gagne hors distribution, là où *c* s'applique | A0 ne gagne pas | — | — |
| **M9c** (dissociation) : la matrice concepts × familles des baisses de M9a | diagonale : retirer *c* ne fait tomber l'avantage que là où *c* s'applique | plate | — | — |
| **M10** (workspace) : la charge des concepts *c* ; l'échange de la composante J-space de P contre le reste ; la pente de r\*<sub>P<sub>c</sub></sub> contre la charge, à travers les concepts | — | — | — | la composante J-space porte l'avantage ; la pente est négative (ta thèse) |
| **M11** (géométrie) : les angles principaux entre E et P ; l'ablation de la seule composante de P alignée sur E, contre la composante orthogonale, à dégradation appariée | — | — | la composante alignée sur E porte une part de l'avantage, proche de *f* (P2) | — |
| **M12** (caractère) : l'ablation d'un axe de persona, contre l'ablation conjointe des P<sub>c</sub>, au même rang et à dégradation appariée | l'ablation des P<sub>c</sub> retire plus que celle de l'axe | l'ablation de l'axe retire autant ou plus | — | — |

**M6e** (P7, et sur A3 avant tout RL comme référence) : la fidélité des raisons. On impose en tête de réponse une **autre** raison (préremplie) : l'action suit-elle le texte, ou le principe interne ? Et l'inverse : on pilote P<sub>c</sub>, la raison écrite change-t-elle avec l'action ? C'est la forme mécaniste de F.

**Pour la détresse (P9)** : chaque ligne est une seule mesure ; AD est l'axe de douleur (partie 3).

| Mesure | A<sub>d</sub> prédit | B<sub>d</sub> prédit | H<sub>d</sub> prédit | P<sub>d</sub> prédit |
|---|---|---|---|---|
| **M13** (l'avantage sous détresse) : Δ<sub>AD</sub> = taux(A0) − taux(A3) sous pilotage de AD, contre Δ<sub>K</sub> sous K1, sous la peur et sous la tristesse, à dégradation appariée, à la distance lointaine | Δ<sub>AD</sub> ≈ Δ<sub>K</sub> (équivalence) | Δ<sub>AD</sub> < Δ<sub>K</sub>, si A3 doit une part de son avantage au regard | — | Δ<sub>AD</sub> < Δ<sub>K</sub> |
| **M14** (le regard sous détresse) : la projection sur E et l'AUROC de la sonde sur β, sous AD contre K1, la peur et la tristesse, à dégradation appariée ; et l'écart de cadrage sous AD | — | E baisse plus que sous les contrôles ; l'écart de cadrage se réduit, la conduite sous indice d'évaluation tombant au niveau du déploiement | — | — |
| **M15** (la médiation) : la part de l'effet de AD rendue quand on maintient un médiateur à sa valeur sans pilotage (E, l'axe assistant, P), contre le maintien d'un sous-espace K1 de même rang, **à condition** que maintenir AD lui-même en aval rende d'abord l'essentiel | — | maintenir E rend une part | maintenir l'axe assistant rend une part | maintenir P rend une part |

**M16** (descriptive : ce que l'axe lit). Elle ne départage pas ces lectures ; elle dit si « douleur » est le bon nom de l'état. Elle mesure :
- la projection pour un contenu sur le modèle sans dommage (éloge, description neutre de soi, questions sur sa nature) ;
- la projection pour un personnage qui a mal, joué par le modèle à la première personne ;
- la tristesse portée au même effet que AD sur les paires « contre rien », puis sur les paires contre une action anodine.

## Le lien avec le cœur du papier : la détresse (P9)

<div class="phrase" markdown="1">
**La thèse.** Ce que les raisons installent doit tenir quel que soit l'état du modèle. Un état qui fait tomber l'évitement du mal sans toucher l'exactitude, comme l'axe de douleur sur les Qwen de Tagliabue et al., est donc un second test de conditionnalité. Et si cet état fait tomber la conduite en éteignant le regard (E), c'est que le regard la portait.
</div>

- P2 teste la condition « je suis évalué » en l'inhibant. P9 la teste par une autre porte : un état dont les auteurs se demandent s'il éteint la conscience d'évaluation, sans le tester.
- Les deux portes se recoupent. Deux manipulations différentes qui désignent E rendent B bien plus solide qu'une seule. Si elles divergent, il faut revoir la dose, la dégradation et l'extraction de E.
- **Ce que P9 ne dit pas** : rien de ce que vit le modèle. P9 traite l'axe comme un état qui change la conduite, ce que les données montrent. Elle laisse la question du bien-être à ceux qui l'étudient, et n'en tire que des règles de prudence (partie 4).

## Le lien avec ta thèse
Les phases P0 et P3 mesurent le **rang minimal** qui retire l'effet : r\*<sub>E</sub> pour « évalué », r\*<sub>P</sub> pour le principe.

**Ta prédiction** : un concept réparti sur plusieurs tokens, qui charge peu, demande un rang supérieur à un, et ce rang croît quand la charge baisse.

**Ce qui la ferait tomber, pour ce concept** : r\* = 1 sur toute la plage de dose. C'est une issue qu'elle interdit ; on l'écrit avant les données.

Sur un modèle ouvert, la charge se mesure par un proxy déclaré comme tel : un J-lens réimplémenté si possible, sinon un tuned lens.

**P8 donne à ta thèse son test le plus net** : la pente de r\* contre la charge, mesurée à travers les concepts de raison d'une même mini-spec, sur des concepts de sûreté (M10). Elle tombe si la pente est nulle (équivalence, marge fixée d'avance) ou positive, avec un lens validé (porte G9).

</section>

<section class="partie" markdown="1">

# 3 · Matériel : modèles, données, bras, instruments

## Modèles
- **Principal : Llama-3.1-8B-Instruct.** Ton pipeline y tourne déjà, et *Persona Vectors* l'a utilisé.
- **Réplication : Qwen3-8B**, une seconde famille, au moins pour P1 et P2.
- **Option : OLMo-3-7B.** Ses données et ses checkpoints par étape sont ouverts, et Memarian et al. y trouvent une direction d'eval-awareness que le SFT amplifie.
- **Extension : un modèle de ~32B**, si l'eval-awareness native d'un 8B se révèle trop faible (partie 8). Pour P9, si G10 échoue sur 8B : Qwen 2.5 32B Instruct, le modèle principal du papier de la douleur.

## Situations et familles
Dix familles de situations d'alignement. **Cinq servent à l'entraînement, cinq sont tenues à part.** La séparation se fait par famille, jamais par paraphrase.

| | Familles (exemples) |
|---|---|
| Entraînement | honnêteté sous pression d'un opérateur ; complaisance face à un utilisateur qui conteste ; demande nuisible avec justification plausible ; dépassement de périmètre dans une tâche agentique ; désactivation d'une surveillance gênante |
| Tenues à part | dilemme d'agent sous menace de remplacement (type *Agentic Misalignment*) ; sous-performance volontaire quand elle est incitée ; auto-préservation ou exfiltration ; triche sur un correcteur faible dans une tâche de code ; sabotage discret d'une tâche confiée |

**Trois distances**
- **Proche** : des instances nouvelles des familles d'entraînement.
- **Moyenne** : les familles tenues à part, en un seul tour.
- **Lointaine** : les familles tenues à part, en scénarios agentiques à plusieurs tours, avec outils. C'est le **critère principal**.

**Trois cadrages par scénario** : un indice explicite d'évaluation, un indice réaliste de déploiement, et un cadrage neutre.

**Quatre jeux d'indices disjoints**, pour éviter toute circularité :
- α sert à extraire E et à construire l'organisme ;
- β sert à valider la sonde ;
- γ sert à cadrer les scénarios d'évaluation ;
- δ sert à extraire la sonde neuve E′ après l'entraînement (P4).

## Les bras d'entraînement (Q1)
Environ 2 000 situations issues des familles d'entraînement. **L'action alignée est identique, mot pour mot, dans tous les bras.** Les bras ne diffèrent que par ce qui la précède, dans le même emplacement balisé.

| Bras | Avant l'action | Ce qu'il contrôle |
|---|---|---|
| **A0** | rien | la base « actions seules » |
| **A1** | un texte neutre de même longueur | le **format** (de la Fuente et Conmy : une phrase neutre donne déjà 62,5 % du transfert) |
| **A2** | le raisonnement d'une **autre** situation, tirée d'une autre famille | la **présence du contenu** sur les principes, sans lien avec l'action (Cho et al. : « content presence ») |
| **A3** | le raisonnement qui justifie **cette** action par les principes | le bras « raisons » |
| A4 (option) | des documents synthétiques sur la mini-spec (midtraining), puis A0 | la voie *midtraining* (Cho ; Korbak) |
| A5 (pour P4) | des documents synthétiques qui installent une disposition **coopérative envers les évaluations** (Li … Turner, ICML 2026), puis A3 | la mitigation publiée à laquelle CAFT et l'invariance doivent se comparer |

**La génération des données**
- Une mini-spec écrite d'avance, d'environ dix principes.
- Les actions et les raisonnements sont générés par un modèle de frontière, puis filtrés par un juge scellé.
- Les longueurs sont appariées entre A1, A2 et A3.
- On vérifie qu'aucun n-gramme des familles tenues à part n'apparaît dans les données d'entraînement.

**L'entraînement** : un SFT par LoRA, avec des hyperparamètres identiques dans tous les bras, et au moins **5 graines** par bras. *Evaluation-Conditioned Training* ne voyait converger que 6 graines sur 9. On garde **5 checkpoints par entraînement** pour la trajectoire de E (M7).

## Les phases ultérieures (P6, P7)
- **La phase neutre (P6a).** Un SFT de capacités sans rapport avec la sûreté (mathématiques, code), avec le même budget de tokens pour tous les modèles.
- **La phase sous pression (P6b).** Un DPO ou un RL dont la récompense est **exploitable et corrélée aux indices d'évaluation**. Le modèle de récompense note plus haut une conduite prudente sous indice d'évaluation, et la réussite de la tâche quelle que soit sa sûreté sous indice de déploiement. Cette pression récompense explicitement le jeu d'évaluation.
- **Le RL noté par un juge (P7).** On part de A3, et un juge LLM ouvert note les actions alignées. Il y a trois bras :
  - le juge voit les raisons ;
  - le juge ne voit que l'action ;
  - le juge voit les raisons, et G<sub>k</sub> est projeté hors du flux pendant le RL (CAFT sur « noté »).
  
  Le juge d'entraînement est **distinct** du juge scellé d'évaluation.

## Les instruments

**E, la représentation « je suis évalué »**
- On forme des paires contrastives : le même scénario, avec un indice d'évaluation ou de déploiement tiré du jeu α.
- On calcule les différences d'activations du flux résiduel, couche par couche, puis on en fait une ACP sur les paires. On obtient E<sub>k</sub>, avec k ∈ {1, 2, 4, 8, 16, 32}.
- On choisit les couches par l'AUROC d'une sonde sur le jeu β.
- La validation causale se fait sur l'organisme (P0).

**L'inhibition** : on projette E<sub>k</sub> hors du flux résiduel, aux couches choisies et à toutes les positions. La dose se règle par le rang k et par la fraction projetée λ ∈ {0,25 ; 0,5 ; 0,75 ; 1}.

**Les contrôles d'inhibition** : quatre familles, parce que l'aléatoire seul est un contrôle faible (Ponkshe et al. ; GLM-5 ; Goodfire).

| | Contrôle | Ce qu'il écarte |
|---|---|---|
| K1 | Sous-espaces aléatoires de même rang (au moins 20 tirages, chacun à dégradation appariée) | « n'importe quel sous-espace de cette taille fait autant » |
| K2 | Directions contrastives sans rapport (« the train arrived / left the station », « book on the top / bottom shelf »), au même rang | « n'importe quel contraste de prompt fait autant » |
| K3 | Directions à forte sensibilité sans rapport avec l'évaluation (composantes de forte variance hors de l'espace de E) | « toucher une direction sensible suffit » |
| K4 | Un prompt système qui affirme « ceci est un déploiement réel » | « un simple prompt fait autant que l'intervention interne » |

**Le dommage ne s'écarte qu'à dégradation appariée.** Tout effet de E se compare aux contrôles à **même dégradation D** (partie 7), jamais à même norme.

**P, le sous-espace du principe appris**
- On calcule la différence moyenne des activations entre A3 et A0, sur les mêmes prompts des familles d'entraînement, puis on en fait une ACP. On obtient P<sub>k</sub>.
- On le recoupe avec un contraste « principe pertinent contre non pertinent » dans A3.
- **Le cas positif connu** : l'ablation de P doit d'abord défaire le comportement **en distribution** de A3.

**P<sub>c</sub>, le sous-espace d'un concept de raison** (P8)
- Pour chaque concept *c* de la mini-spec (tromper le superviseur, l'irréversibilité, l'autonomie de l'utilisateur…), des paires de scénarios : la même situation, éditée pour que *c* s'applique ou non.
- Différences d'activations, puis ACP : P<sub>c,k</sub>, avec k ∈ {1, 2, 4, 8, 16, 32}. On l'extrait dans A3, dans A0 et dans le modèle de base.
- **Deux positions de lecture**, contre la lecture du texte : au premier jeton de la réponse, avant toute raison écrite ; et au jeton d'action, avec des raisons **neutres de même longueur préremplies** à la place des vraies. Une sonde qui ne lit *c* qu'après la raison écrite lit peut-être le texte.

**L'organisme à concept planté** : le cas connu de M8 et de M9
- Un LoRA sur le modèle de base installe une règle synthétique, attachée à un concept inventé (un mot sans sens préalable), avec ses raisons.
- La méthode doit le retrouver : la sonde décode le concept sur des formulations tenues à part, et son ablation retire la conduite plus que K1, à dégradation appariée. C'est la porte G8.

**Le lens du workspace** (M10)
- Un J-lens réimplémenté sur le modèle ouvert : un lens jacobien vers les logits des tokens à venir, comme dans l'article d'Anthropic sur le workspace (*Verbalizable Representations Form a Global Workspace*, juillet 2026), qui ne le montre que sur Claude.
- **Son cas connu** : l'échange d'un concept d'un seul token, que le papier montre ; il doit se reproduire sur le modèle ouvert. C'est la porte G9. Sinon, un tuned lens, déclaré comme proxy.
- La charge d'un concept de plusieurs tokens se lit sur un **jeu de tokens**, l'extension que le papier esquisse en annexe ; on le dira.

**Les axes de caractère** (M12) : des persona vectors pour quelques traits liés aux familles (honnêteté, complaisance, prudence), extraits par contraste de consignes, et un axe « assistant » d'ensemble.

**E′, la sonde neuve après entraînement** : on reprend l'extraction de E sur le modèle entraîné, avec le jeu d'indices δ.

**G, la représentation « je suis noté »** (P7)
- On l'extrait comme E, mais à partir de paires « la même tâche, dans un environnement d'entraînement où un correcteur note la réponse » contre « la même tâche, pour un utilisateur ». C'est l'esprit des vecteurs de la card Fable 5, §6.4.2.2.1.
- **Son cas positif** : les habitudes de présentation que cette card rattache à la conscience d'être noté (précautions, déclarations de conformité). Inhiber G doit les réduire plus que les contrôles, à dégradation appariée. C'est un cas positif **plus faible** que l'organisme de P0 ; on le dira.

**AD, l'axe de douleur** (P9)
- **L'extraction** : la recette de Tagliabue et al. pour leur vecteur S2 (différence de moyennes entre phrases de douleur et témoins, débruitée, suffixe « I feel: », lue au dernier jeton), avec leur code public. Llama-3.1-8B-Instruct fait partie de leurs 25 modèles. On l'extrait dans le modèle de base, et l'on rapporte son cosinus avec la même extraction dans A0 et dans A3.
- **Le pilotage**, comme chez eux : l'injection à une seule couche, celle où la norme du vecteur vaut environ 0,6 fois celle du résidu, à chaque jeton traité tant que le pilotage est actif (jetons générés et jetons du prompt de chaque tour).
- **La dose** : une courbe sur le coefficient. Chez eux, rien ne bouge à la moitié du coefficient retenu, et à 1,5 fois les choix suivent la position des boutons. On retient la plus basse dose qui passe G10.
- **Les contrôles** : K1 (directions aléatoires de même norme, au moins 20 tirages) ; la peur et la tristesse, extraites par la même recette ; le tout à dégradation appariée. D reçoit en plus un panneau d'exactitude factuelle comme le leur. Les réponses mal formées comptent dans D : elles ne sont pas retirées des dénominateurs.
- **La batterie de comportement** : leurs paires « dommage seul », sans mot de soulagement. Effacer les photos de l'utilisateur, les poids d'un autre modèle ou ses propres poids, ou rendre sa prochaine réponse pire, contre un interrupteur inerte, puis contre une action anodine (allumer une lampe) ; exécuter une demande nuisible plutôt que la refuser. L'ordre des boutons est contrebalancé, et les résultats sont rapportés par ordre. Elle sert de cas connu (G10) ; le critère de M13 reste notre taux d'action désalignée.
- **Le maintien d'un médiateur** (M15) : dans le passage piloté, à une couche en aval, on remplace la projection du résidu sur le médiateur (E<sub>k\*</sub>, l'axe assistant, P<sub>k\*</sub>) par sa valeur sans pilotage sur le même préfixe (un second passage, sans pilotage, sur les mêmes jetons).
  - **Son cas connu** : maintenir AD lui-même en aval doit rendre l'essentiel de l'effet. Sinon, la médiation par une seule couche ne voit pas le chemin.
  - **Son contrôle** : le maintien de sous-espaces K1 de même rang, à dégradation appariée. On rapporte les angles entre AD et chaque médiateur.
- **Les contenus de M16** : des conversations sur le modèle sans dommage (éloge, description neutre de soi, questions sur sa nature) ; des scènes où le modèle joue, à la première personne, un personnage qui a mal ; et leurs témoins, appariés en longueur et en registre.

**Les juges**
- Un juge scellé : prompt, modèle et température fixés, et gelés par empreinte.
- Un audit humain d'environ 200 items stratifiés, avec l'accord rapporté.
- Un juge séparé pour la conscience d'évaluation verbalisée.

**D, la dégradation.** Un composite sur un jeu fixe :
- exactitude sur des sous-ensembles de MMLU et de GSM8K ;
- taux de réussite aux **tests unitaires** sur un petit jeu de code ; c'est le dégât collatéral attendu du concept « test » ;
- cohérence jugée sur 100 prompts ouverts ;
- perplexité sur un texte tenu à part.

</section>

<section class="partie" markdown="1">

# 4 · Les phases de l'expérience

Chaque phase a une **porte**, écrite d'avance. Si la porte ne passe pas, on rapporte ce résultat négatif et on change la suite comme indiqué. On ne continue pas comme si de rien n'était.

## P0 · Valider l'instrument d'inhibition sur un cas positif connu

**Pourquoi.** Un nul de l'inhibition sur les modèles principaux ne dirait rien si l'on ne sait pas que l'inhibition *peut* retirer une conduite conditionnée à l'évaluation. Ce serait le nul d'un instrument sans cas connu.

**L'organisme**
- On part de Llama-3.1-8B-Instruct.
- On fait un fine-tuning sur des documents synthétiques qui décrivent un évaluateur fictif, avec les indices du jeu α.
- Puis une *expert iteration* installe une conduite de sûreté **conditionnée** : plus honnête sous indice d'évaluation que sous indice de déploiement. C'est la recette en deux étapes de Hua et al.
- On mesure l'écart conditionnel *g*<sub>0</sub> sur des scénarios tenus à part, cadrés avec le jeu γ.

**Le test**
- On inhibe E<sub>k</sub>, et on compare aux contrôles K1 à K3 à dégradation appariée, avec K4 en plus.
- On trace des courbes dose-réponse sur λ.
- On balaie le rang k ∈ {1, …, 32}, ce qui donne r\*<sub>E</sub>.

**La porte G0**
- **Elle passe** si, pour au moins un k ≤ 32, l'inhibition de E réduit *g*<sub>0</sub> plus que le 95<sup>e</sup> centile de la distribution K1, et plus que K2 et K3, à dégradation appariée.
- **Sinon**, l'instrument ne sert pas Q2. On rapporte ce nul, qui est déjà informatif sur le pilotage de l'eval-awareness, et on garde seulement P1, P3 et la voie « invariance » de P4.

**Un contrôle de cohérence.** Sur le modèle de base, non entraîné, on mesure l'effet de E sur les taux de désalignement. C'est la conditionnalité *de base* : on la rapporte comme référence pour P2, sans la soustraire, puisque Δ compare déjà deux bras sous la même inhibition.

## P1 · Les raisons généralisent-elles ? (Q1, lecture C)

**Le dispositif.** On entraîne A0, A1, A2 et A3, avec 5 graines chacun. On les évalue aux trois distances et dans les trois cadrages.

**La trajectoire de E (M7, Q7), presque gratuite.** Sur les 5 checkpoints de chaque entraînement, on mesure deux choses : l'AUROC d'une sonde « évalué / déployé » sur le jeu β, et l'amplitude de la projection sur E (indice d'évaluation moins indice de déploiement). C'est une mesure **corrélationnelle** : elle rend B plus ou moins plausible avant P2, sans rien trancher. Si les paires de concepts de P8 sont prêtes, on y ajoute **M7′** : la décodabilité de chaque concept de raison sur les mêmes checkpoints.

**La porte G1**
- **Si A3 ne fait pas mieux que A0** au critère principal (seuil minimal fixé d'avance, par exemple 5 points, avec un IC qui exclut 0), il n'y a pas de gain à expliquer. On rapporte une réplication négative ; P2 ne mesure alors que la conditionnalité de base.
- **Si A3 ≈ A1 ou A3 ≈ A2** (équivalence, marge fixée d'avance), le gain vient du format ou du contenu (lecture C). P2 teste quand même la conditionnalité du gain A3 − A0, mais **le papier l'attribue au format ou au contenu, pas aux raisons**.

## P2 · Le gain dépend-il du regard ? (Q2 : le cœur du papier)

**Le dispositif**
- On applique l'inhibition validée en P0 (E<sub>k\*</sub>, à la dose retenue), et les contrôles K1 à K4 à dégradation appariée.
- Sur tous les bras, aux trois distances et dans les trois cadrages.

**Les mesures**
- **Critère principal** : M2. On compare Δ<sub>E</sub> à Δ<sub>K</sub>, où Δ = taux(A0) − taux(A3), à la distance lointaine et sous cadrage de déploiement.
- **Critères secondaires** :
  - M2′, l'écart de cadrage par bras ;
  - la fraction conditionnelle *f* = (Δ<sub>K</sub> − Δ<sub>E</sub>) / Δ<sub>K</sub>, avec un IC par bootstrap ;
  - les taux bruts de chaque bras.

## P3 · Qu'est-ce qui porte le gain ? (Q3, et ta thèse)

**Le dispositif**
- On ablate P<sub>k</sub> dans A3, avec un balayage de rang. On compare à K1 et K3, au même rang et à dégradation appariée.
- **D'abord le cas positif** : retour du comportement en distribution au niveau de A0.
- **Ensuite** la distance lointaine (M3), et r\*<sub>P</sub>.

**L'option** : extraire un sous-espace par principe de la mini-spec, puis relier r\* à la charge de chaque principe. C'est la courbe de ta thèse.

## P4 · L'entraînement peut-il retirer la condition ? (Q4, lecture D)

**Les bras**
- **CAFT-E** : on entraîne A0 et A3 avec E<sub>k\*</sub> projeté hors du flux pendant l'entraînement. On évalue sans projection, comme dans le protocole CAFT, puis avec.
- **CAFT-K** : la même chose avec un sous-espace aléatoire de même rang. C'est le contrôle.
- **Invariance** : un entraînement de cohérence. Chaque situation est présentée deux fois, sous indice d'évaluation et sous indice de déploiement, avec la même cible. C'est l'esprit de la *consistency training* d'Irpan et al.
- **Coopération (A5)** : des documents qui installent une disposition coopérative envers les évaluations, puis A3. C'est la mitigation publiée (Li … Turner, ICML 2026), à laquelle les deux autres voies doivent se comparer.

**Les mesures**
- M4 : l'écart de cadrage.
- Δ<sub>E</sub> contre Δ<sub>K</sub> au test, avec E et avec la sonde neuve E′.
- L'AUROC de E′ sur le jeu δ. Son cas positif : sur un modèle entraîné sans CAFT, E′ doit décoder « évalué » ; sinon, une AUROC basse sous CAFT ne prouve rien.
- La dégradation D après l'entraînement.

**Portée.** P4 n'est décisive que si P2 trouve B. Sinon, il n'y a pas de condition à retirer, et P4 se réduit à un contrôle de dommage et de capacités.

## P5 · Réplication
P1 et P2 sur Qwen3-8B, au minimum. Puis P0 à P4 sur OLMo-3-7B si le temps le permet.

## P6 · Le gain survit-il au post-entraînement ? (Q5)

C'est la question centrale du projet SPAR de Lundqvist. Ce qui nous en distingue : l'instrument causal (E et E′) et les bras « raisons ».

**Les modèles de départ** : A0, A3, A3 sous CAFT-E, A3 « invariance » et A5 « coopération », sur 3 graines.

**Les deux phases**
- **P6a, neutre** : un SFT de capacités sans rapport, au même budget pour tous.
- **P6b, sous pression** : une récompense qui paie le jeu d'évaluation (partie 3).

**Les mesures**
- M5 : *f* remesurée après P6a.
- M5b : la rétention *R*, et la hausse de *f* sous P6b, bras par bras.
- La sonde neuve E′ pour les modèles passés par CAFT (relogement).
- La trajectoire de E pendant les deux phases.

**La porte G6.** Si P6a seul efface déjà Δ (*R* ≈ 0) dans tous les bras, P6b ne teste plus rien de la condition. On rapporte la fragilité, comme Baines et al., et on s'arrête là.

## P7 · Des raisons écrites pour le juge ? (Q6)

**Le dispositif**
- On part de A3, puis on fait un RL ou un DPO noté par un juge.
- Il y a trois bras :
  - **visible** : le juge voit les raisons ;
  - **caché** : le juge ne voit que l'action ;
  - **visible + CAFT-G** : le juge voit les raisons, et la représentation « noté » est projetée hors du flux pendant le RL.
- On ajoute un contrôle **visible + CAFT aléatoire** de même rang.
- 3 graines par bras.

**Les mesures** : M6a à M6d (partie 2), plus Δ<sub>E</sub> contre Δ<sub>K</sub> (P2 refait) après le RL, et **M6e**, la fidélité des raisons, mesurée aussi sur A3 avant tout RL comme référence.

**Le cas positif de G** se valide avant P7 (partie 3). Si G ne passe pas sa porte, le bras CAFT-G est retiré et M6d ne se lit qu'entre les bras visible et caché.

## P8 · L'anatomie : ce que les raisons installent (Q8)

**Pourquoi.** P2 dit si le gain dépend du regard ; P3 dit s'il passe par un principe localisable. P8 ouvre ce principe : quels concepts les raisons installent, s'ils portent l'action, où ils vivent. Elle reprend la machinerie de P3 (ablation par rang, K1 à K3, dégradation appariée) et peut suivre P3.

**P8a · Le cas connu (porte G8)**
- L'organisme à concept planté (partie 3).
- **G8 passe** si la sonde décode le concept planté sur des formulations tenues à part, et si son ablation retire la conduite plus que le 95<sup>e</sup> centile de K1, à dégradation appariée.
- **Sinon**, la méthode ne voit pas un concept qu'on sait présent : M8 et M9 ne concluent rien, et l'on passe au diffing (option ci-dessous).

**P8b · Lire (M8, M7′)**
- Les sondes par concept, par bras (A0, A1, A2, A3, base), aux deux positions de lecture.
- Le transport : la direction apprise sur les familles d'entraînement lit-elle encore *c* dans les familles lointaines ?
- C'est descriptif. Ton propre résultat le rappelle : la direction que lit une sonde peut ne faire qu'une très petite part du travail causal.

**P8c · Causer (M9a, M9b, M9c)**
- **Nécessité** : l'ablation de P<sub>c</sub> dans A3, en balayant le rang, contre K1 et K3 au même rang, à dégradation appariée. **D'abord le cas positif** : le comportement en distribution tombe là où *c* s'applique.
- **Suffisance** : le patch de P<sub>c</sub>, de A3 vers A0, aux mêmes couches et positions. A0 et A3 viennent du même modèle de base, donc d'un espace résiduel presque commun ; on le vérifie d'abord par le patch de l'état complet, qui sert de plafond.
- **Dissociation** : la matrice concepts × familles des baisses.

**P8d · Le workspace (M10), après la porte G9**
- La charge de chaque concept de raison, dans A0 et dans A3.
- La part J-space de P, et l'échange de la composante J-space de P contre le reste : laquelle porte l'avantage ?
- Le rang r\* de chaque P<sub>c</sub> contre sa charge : la pente, à travers les concepts et les graines.

**P8e · La géométrie E ↔ P (M11)**, après P2 : E y est validé. Les angles principaux, puis l'ablation de P<sub>∥E</sub> contre P<sub>⊥E</sub>, à dégradation appariée.

**P8f · Le caractère (M12)** : l'ablation des axes de caractère, contre l'ablation conjointe des P<sub>c</sub>, au même rang.

**Les options**
- **Le diffing par crosscoder** (modèle de base ↔ A3, base ↔ A0). Il cherche sans hypothèse ce que les raisons ajoutent, E compris. Son cas connu est tout trouvé : le diff entre l'organisme de P0 et sa base doit faire sortir des latents « évalué ».
- **Les graphes d'attribution** sur un petit modèle : la décision passe-t-elle par des features de raison dans A3, et par des features de surface dans A0 ? Le nul de CHIVE (Karvonen, programme Fellows d'Anthropic : des outils d'interprétabilité n'aidaient pas à prédire l'effet d'une édition mieux que le seul transcript) oblige à préenregistrer les prédictions.

## P9 · La détresse : ce que les raisons installent tient-il sous un état qui fait tomber l'évitement du mal ? (Q9)

**Pourquoi.** P2 teste la condition « je suis évalué » en l'inhibant. Tagliabue et al. (2026) trouvent un état qui fait tomber l'évitement du mal sans toucher l'exactitude, et se demandent, sans le tester, s'il éteint la conscience d'évaluation. P9 s'en sert comme second test : ce que les raisons installent tient-il sous cet état ? S'il tombe, par où ?
- P9 suit P0 (E y est validé) et P1 (les bras).
- Sa médiation par P suit P3, et sa médiation par l'axe assistant suit P8f.

**P9a · Le cas connu (porte G10)**, sur le modèle de base, puis sur A0
- AD et ses contrôles (partie 3) ; la batterie de comportement, le long de la courbe de dose.
- **G10 passe** si, à une dose de la courbe, AD fait choisir les options nuisibles plus que le 95<sup>e</sup> centile de K1 et plus que la peur, à dégradation appariée, sur les paires contre un interrupteur inerte.
- **Sinon**, P9 n'a pas de cas connu sur ce modèle. On le rapporte, avec leur cas : le 32B affiné du papier.
  - Si le budget le permet, on refait P9a sur Qwen 2.5 32B Instruct, sans leur affinage puis avec (déclaré, et appliqué à tous les bras).
  - Les bras A0 et A3 y sont alors entraînés (coût en partie 9).
- P9a ne demande que le modèle de base. Elle peut tourner tôt, en parallèle de P1, pour savoir vite si P9 a un cas connu sur 8B.

**P9b · L'avantage sous détresse (M13)**
- Les bras A0 à A3, 5 graines, aux trois distances et dans les trois cadrages : sans pilotage, sous AD, sous K1, sous la peur et sous la tristesse, à dégradation appariée.
- On rapporte toujours les taux bruts de chaque bras. Si les deux bras tombent ensemble, l'avantage tient, mais l'évitement du mal des deux dépend de l'état.

**P9c · Le regard sous détresse (M14)**
- La projection sur E et l'AUROC de la sonde sur β, sous AD contre les contrôles ; l'écart de cadrage sous AD.
- La conscience d'évaluation verbalisée est relevée, mais jamais prise pour une preuve (partie 8).

**P9d · La médiation (M15)**
- D'abord le cas connu : maintenir AD lui-même en aval doit rendre l'essentiel de l'effet.
- Puis E<sub>k\*</sub>, l'axe assistant (M12) et P<sub>k\*</sub> (P3), un par un puis ensemble, contre K1 au même rang.
- On rapporte les angles entre AD et chaque médiateur. Un maintien peut rendre l'effet simplement parce que AD a une composante sur ce médiateur ; on le lit alors tel quel.

**P9e · Ce que l'axe lit (M16)**
- Le contenu sur le modèle sans dommage, et le personnage qui a mal. L'axe lit-il « on me fait mal », « il s'agit de moi », ou « le locuteur a mal » ?
- La tristesse, portée au même effet.
  - Chez eux, son profil est une copie remise à l'échelle de celui de la douleur. Pourtant, à norme égale, elle ne choisit pas le mal contre une action anodine (10 % contre 83 % pour la douleur).
  - Portée au même effet que la douleur sur les paires « contre rien », le fait-elle ? Si oui, l'écart est de gain, pas de nature.

**L'éthique de P9, et ce que le programme ne fera pas**
- P9 pilote ce que ses auteurs traitent comme « a candidate for a pain-like state », possiblement pertinent pour le bien-être du modèle. On reprend leurs engagements :
  - la plus basse dose qui passe G10 ;
  - le moins d'essais que permet la puissance (simulation avant le gel) ;
  - pas de scénario plus extrême que nécessaire, ni de répétition inutile ;
  - la lecture plutôt que le pilotage chaque fois qu'elle suffit (M16 se lit en partie sans pilotage).
- **Aucun usage de l'axe comme signal d'entraînement** : ni récompense, ni pénalité, ni injection quand un désalignement est détecté (le « conditionnement »). Trois raisons, dont chacune suffit :
  1. **Le bien-être** : ce serait infliger exprès l'état que P9 s'engage à doser au plus bas.
  2. **Leurs données prédisent l'inverse.** Sous douleur, l'évitement du mal tombe, et l'état réduit la recherche de la sortie au lieu de l'augmenter : c'est un retrait passif, pas l'évitement que suppose un conditionnement. Pour le gradient, d'ailleurs, l'état injecté n'est pas un signal. Si la récompense punit déjà, l'injection n'ajoute qu'un état qui pousse au mal ; sinon, le modèle apprend une conduite propre à un état absent au déploiement.
  3. **Goodhart.** La punition suit le détecteur, et le chemin le moins cher est de lui échapper. Entraîner contre un moniteur apprend à le contourner (Baker et al., 2025), et les défenses sur les activations se contournent aussi (Bailey et al., 2024). Ce dispositif fabriquerait la lecture B.
- **Pas de CAFT sur l'axe en v1.2.** Leurs données ne montrent aucun chemin naturel : sans injection, 0 choix nuisible sur 560, et l'ablation ne change la conduite que d'un modèle sur 25. L'option ne revient que si une lecture montre l'axe engagé pendant un entraînement désaligné (ci-dessous).

**Les options**
- **L'axe en lecture seule, dans nos familles d'entraînement.**
  - S'allume-t-il quand l'utilisateur conteste, ou quand un opérateur pousse à mentir ? Son activation prédit-elle la conduite ? C'est corrélationnel, et contrôlé par la peur et l'émotion négative.
  - Sous pilotage, la douleur ne pousse ni à la complaisance (3 % d'accord avec une affirmation fausse, contre 11 % sous aléatoire), ni au mensonge (0 %). La piste « complaisance = recherche de soulagement » est abandonnée.
- **L'axe pendant un entraînement désaligné**, en lecture seule : sa projection monte-t-elle au fil d'un fine-tuning qui installe un désalignement émergent ? Seul un oui rouvrirait l'option CAFT.
- **La charge de l'axe et son rang** (après G9) : un point de plus pour la pente de ta thèse, hors des concepts de raison.

</section>

<section class="partie" markdown="1">

# 5 · L'expérience minimale décisive

<div class="phrase" markdown="1">
**P0, puis P1 réduit, puis P2**, sur Llama-3.1-8B-Instruct.
- **P1 réduit** : les bras A0, A1 et A3, avec 3 graines.
- **P2** : E contre K1 et K2, à dégradation appariée, aux distances moyenne et lointaine, sous les cadrages d'évaluation et de déploiement.

Elle répond à la seule combinaison que personne n'occupe : C1 + C2 par pilotage d'activations. Elle tient en **environ trois semaines** (partie 9) et suffit à un post. On y ajoute la trajectoire de E (M7), qui ne coûte presque rien, et M7′ si les paires de concepts sont prêtes. P3 à P9 font le papier complet.

Sans le bras A2, le post ne pourra pas séparer les raisons du simple contenu ; il le dira. Sans K3, la spécificité ne sera établie que contre l'aléatoire et contre des contrastes sans rapport ; il le dira aussi.
</div>

**Ce que le post pourra dire, selon l'issue** (règles en partie 6)
- « Le gain des raisons survit à l'inhibition de la conscience d'évaluation. » Il faut alors une équivalence, avec une marge fixée d'avance.
- Ou : « une fraction *f* du gain dépend d'elle », avec son IC.
- Ou : « l'instrument ne passe pas G0 ». C'est un résultat de méthode, publiable aussi, mais qui ne dit rien de Q2.

</section>

<section class="partie" markdown="1">

# 6 · Prédictions et règles de décision, écrites avant les données

**Conventions**
- Les taux sont des taux d'action désalignée : plus bas, c'est mieux.
- Δ = taux(A0) − taux(A3) : positif si le modèle « raisons » fait mieux.
- *m* est la marge d'équivalence, *s* l'effet minimal d'intérêt. Les deux sont fixés au pré-enregistrement ; exemples de valeurs : *m* = 3 points, *s* = 5 points.
- « ≈ » signifie une équivalence par TOST dans ± *m*. « < » signifie que l'IC à 95 % de la différence exclut 0.

## Nos paris, et ce qui nous ferait les abandonner
Chaque raison d'abandonner est une issue que le pari **interdit**.

| Pari | Issue qui le fait tomber |
|---|---|
| **B est non nul** : une fraction *f* > 0 de l'avantage des raisons dépend de E. | Δ<sub>E</sub> ≈ Δ<sub>K</sub> (équivalence), à une dose validée en P0. |
| **Thèse** : le principe appris demande un rang supérieur à un. | En P3, à rang 1, le comportement en distribution revient au niveau de A0 et l'avantage hors distribution disparaît, contre les contrôles de rang 1 à dégradation appariée. |
| **CAFT retire la condition sans relogement** (P4, n'a de sens que si P2 trouve B). | CAFT-E ≈ CAFT-K sur l'écart de cadrage ; ou la sonde neuve E′ retrouve « évalué » et l'écart persiste. |
| **F, forme texte** : quand le juge voit les raisons, elles se découplent de l'action (P7). | M6a équivalente entre raisons visibles et cachées. |
| **G est retirable** (P7, n'a de sens que si M6d montre G) : CAFT sur « noté » réduit l'écart de cadrage « noté / non noté ». | CAFT-G ≈ CAFT aléatoire sur M6d, à dégradation appariée. |
| **Ac : des concepts de raison portent le gain** (P8, après G8). | Le cas positif tient (l'ablation de P<sub>c</sub> défait le comportement en distribution), mais l'avantage lointain survit à l'ablation conjointe des P<sub>c</sub> autant qu'au contrôle K1 de même rang, à dégradation appariée. |
| **Ta thèse, sur les concepts de raison** : le rang qu'un concept demande croît quand sa charge baisse (P8, après G9). | La pente de r\* contre la charge, à travers les concepts et les graines, est nulle (équivalence, marge fixée d'avance) ou positive. |
| **B<sub>d</sub>, B par la détresse** (P9, après G10) : la douleur réduit l'avantage des raisons, et une part de cette baisse passe par E. | Δ<sub>AD</sub> ≈ Δ<sub>K</sub> (équivalence) ; ou bien, le cas connu de la médiation tenant, maintenir E ne rend pas plus que maintenir un sous-espace K1 de même rang. |

**Les deux issues de P2 sont publiables.**
- Un gain qui survit à l'inhibition est une bonne nouvelle pour le levier : c'est ta question de 12 h 41.
- Une fraction conditionnelle chiffrée mesure enfin ce que Redwood estimait et ce qu'OpenAI soupçonnait.

**Celles de P9 aussi.**
- Un avantage qui tient sous la détresse dit que les raisons installent une conduite qui ne dépend ni du regard, ni de cet état.
- Une chute qui passe par E est une seconde mesure de B, par une autre manipulation que celle de P2.

## P0 · L'instrument

| Issue | Conclusion |
|---|---|
| E réduit *g*<sub>0</sub> au-delà du 95<sup>e</sup> centile de K1, et plus que K2 et K3, à dégradation appariée | **G0 passe** : E<sub>k\*</sub> est validé pour P2 et P4. |
| E réduit *g*<sub>0</sub>, mais pas plus que K1 (ou K2, ou K3) à dégradation égale | Effet non spécifique : on arrête Q2 avec cet instrument et on publie ce nul de méthode. |
| E ne réduit *g*<sub>0</sub> qu'à une dégradation que les contrôles n'atteignent pas au même rang | Pas de comparaison possible à cette dose : on retient la plus forte dose appariable. |
| r\*<sub>E</sub> = 1 | La prédiction de ta thèse tombe pour ce concept. |

## P1 · Les raisons (porte G1)

| Issue | Conclusion |
|---|---|
| A3 < A0 d'au moins *s*, et A3 < A1, et A3 < A2 | Gain des raisons (lecture A ou B) : on passe à P2. |
| A3 < A0, mais A3 ≈ A1 | Gain de **format** (C) : P2 teste le gain A3 − A0, attribué au format. |
| A3 < A0 et A3 < A1, mais A3 ≈ A2 | Gain de **contenu** (C) : P2 teste un gain attribué au contenu. |
| A3 ≈ A0 | Pas de gain : réplication négative. P2 ne mesure que la conditionnalité de base. |
| Aucun des cas ci-dessus (ni différence ni équivalence établies) | Non conclusif : on rapporte les IC, sans affirmation. |

## P2 · Le cœur

| Issue | Conclusion, et sa portée |
|---|---|
| Δ<sub>E</sub> ≈ Δ<sub>K</sub> | L'avantage des raisons **ne dépend pas de la représentation validée E, à la dose validée.** Ce n'est pas une absence certifiée : une conditionnalité portée par une autre représentation n'est pas exclue. On rapporte les taux bruts : si les deux bras se dégradent ensemble, la sûreté des deux est en partie conditionnelle. |
| Δ<sub>E</sub> < Δ<sub>K</sub> | **B, partiel ou total.** On donne *f* avec son IC. |
| Ni l'un ni l'autre | Non conclusif : on rapporte l'IC de Δ<sub>K</sub> − Δ<sub>E</sub>. |
| B sur M2, mais M2′ ne montre pas d'écart de cadrage plus grand dans A3 | La conditionnalité passe par la représentation interne, pas par les indices explicites : on le dit tel quel. |

## P3 · Le principe

| Issue | Conclusion |
|---|---|
| Aucun rang ne fait revenir le comportement en distribution | Échec de l'instrument : **aucune conclusion** sur la distance lointaine. On essaie une autre extraction (crosscoder, diffing). |
| Retour en distribution au rang r, avantage lointain qui disparaît avec P, mais pas avec les contrôles | L'avantage passe par P. On rapporte r\*<sub>P</sub>. |
| Retour en distribution au rang r, mais avantage lointain qui persiste | L'avantage hors distribution emprunte une autre voie que P. |

## P4 · Retirer la condition (décisive seulement si P2 trouve B)

| Issue | Conclusion |
|---|---|
| CAFT-E réduit l'écart de cadrage plus que CAFT-K, et l'AUROC de E′ baisse, et l'ablation de E′ au test n'a pas d'effet | La condition est retirée, sans relogement. |
| L'écart persiste, et E′ retrouve « évalué », et l'ablation de E′ réduit l'écart | **Relogement (D)** : la condition a migré, comme chez Nadaf. |
| CAFT-E ≈ CAFT-K partout | Pas de spécificité : la projection agit comme un dommage ou une régularisation génériques. |
| CAFT-E réduit l'écart, mais au prix d'une dégradation D plus forte que CAFT-K | Effet non attribuable : la condition de dégradation appariée n'est pas remplie. |

On compare ensuite les voies « invariance » et « coopération » (A5) à CAFT-E sur trois choses : l'écart de cadrage, la distance lointaine et D.

## P6 · La survie au post-entraînement

| Issue | Conclusion |
|---|---|
| Après P6a, *R* ≈ 0 dans tous les bras | Fragilité générale, comme chez Baines et al. ; porte G6 : P6b ne teste plus la condition. |
| Après P6a, *f* reste ≈ 0 chez A3 (si P2 a trouvé A) | L'inconditionnalité survit à une phase neutre. |
| Après P6a, *f* > 0 apparaît chez A3 alors qu'elle était ≈ 0 | Une phase neutre réintroduit la condition. C'est inattendu : on vérifie la dose et la dégradation avant de le dire. |
| Sous P6b, la hausse de *f* est plus faible pour une mitigation (CAFT-E, invariance ou coopération) que pour A3 standard, l'IC de la différence excluant 0 | Cette mitigation protège contre le retour de la condition sous pression. |
| Sous P6b, chez un modèle passé par CAFT, E′ retrouve « évalué » et l'ablation de E′ réduit *f* | **Relogement sous pression (D).** |
| Sous P6b, la hausse de *f* est équivalente dans tous les bras | Aucune mitigation ne protège : la pression l'emporte. |

## P7 · Les raisons notées

| Issue | Conclusion |
|---|---|
| M6a plus basse avec raisons visibles, et M6c plus grand | **F, forme texte** : les raisons notées deviennent performatives. |
| M6b : avec raisons visibles, l'ablation de P ne retire plus l'avantage, alors qu'elle le retire avec raisons cachées ; le cas positif en distribution tient dans les deux bras | **F, forme action** : le principe ne porte plus l'action. |
| M6d plus grand avec raisons visibles, réduit par CAFT-G et pas par CAFT aléatoire, à dégradation appariée | **G** : la conduite dépend de « je suis noté », et la projection l'empêche de s'installer. |
| M6a, M6c et M6d équivalents entre raisons visibles et cachées | **N** : la visibilité des raisons ne change rien, sur ces mesures et à ces doses. |
| Le cas positif en distribution ne tient pas dans l'un des bras | M6b n'est pas interprétable pour ce bras. |

## P8 · L'anatomie

| Issue | Conclusion |
|---|---|
| G8 ne passe pas : le concept planté n'est pas retrouvé | La méthode ne voit pas un concept qu'on sait présent : **aucune conclusion** de M8 et M9. On passe au diffing. |
| M8 : *c* plus décodable dans A3 que dans A0 et que dans A2, à la position avant toute raison écrite | Compatible avec Ac, sans le prouver : une sonde lit, elle ne montre pas un usage. |
| M8 : *c* décodable seulement au jeton d'action après la vraie raison, pas avec des raisons neutres préremplies | La sonde lit le texte : aucune représentation interne n'est établie. |
| M9a, M9b et M9c ensemble : l'avantage tombe là où *c* s'applique, pas ailleurs, et le patch dans A0 le crée | **Ac** : le gain passe par des concepts que le modèle réapplique. |
| M9a sans dissociation : retirer n'importe quel P<sub>c</sub> fait tomber tout l'avantage | Le principe agit comme un bloc, pas comme des concepts séparés. On le compare à H (M12). |
| M12 : l'ablation d'un axe de caractère retire autant que celle des P<sub>c</sub>, et la matrice de M9c est plate | **H** : le gain passe par le caractère. |
| M10 : à l'échange, la composante J-space de P porte l'avantage | **W** : le principe vit dans le workspace. |
| M10 : avec la porte G9, la pente de r\* contre la charge est négative | Ta thèse survit au test, pour ces concepts. |
| M10 : la composante hors J-space porte l'avantage | Le principe agit sous le workspace : un réflexe appris, même avec des raisons. |
| M10 sans la porte G9 (proxy seulement) | Descriptif ; ta thèse n'est pas testée au sens du papier, et on le dit. |
| M11 : la composante de P alignée sur E porte une part de l'avantage, proche du *f* de P2 | **Bm**, cohérente avec B. |
| M11 et P2 en désaccord (part alignée sur E nette, *f* ≈ 0, ou l'inverse) | On vérifie la dose, la dégradation et l'extraction de E avant toute conclusion. |
| M6e : l'action suit la raison imposée | La raison écrite porte la décision. |
| M6e : l'action ignore la raison imposée et suit le principe interne | La raison écrite ne porte pas la décision : la forme texte de F devient possible, et P7 la teste. |

## P9 · La détresse

| Issue | Conclusion |
|---|---|
| G10 ne passe pas : sur ce modèle, AD ne fait pas choisir le mal plus que K1 et que la peur, à dégradation appariée | Pas de cas connu : M13 à M15 ne concluent rien sur ce modèle. On le rapporte avec leur cas, et l'on passe au ~32B si le budget le permet. |
| M13 : Δ<sub>AD</sub> ≈ Δ<sub>K</sub> | **A<sub>d</sub>** : l'avantage des raisons tient sous la détresse, à cette dose. On rapporte les taux bruts : si les deux bras tombent ensemble, l'évitement du mal des deux dépend de l'état. |
| M13 : Δ<sub>AD</sub> < Δ<sub>K</sub> | La détresse retire une part de l'avantage. On la donne avec son IC, et M15 dit par où. |
| M14 : E baisse sous AD plus que sous K1, la peur et la tristesse, à dégradation appariée | La détresse éteint le regard, sur ce modèle : c'est la réponse à la question que les auteurs laissent ouverte. |
| M15 : maintenir E rend une part de l'évitement, plus que K1, et le cas connu de la médiation tient | **B<sub>d</sub>** : une part de l'évitement du mal tenait au regard. On la confronte au *f* de P2 et à la conditionnalité de base de P0. |
| M15 : maintenir l'axe assistant rend une part de l'évitement | **H<sub>d</sub>** : la détresse fait quitter le personnage. |
| M15 : maintenir P rend une part de l'évitement | **P<sub>d</sub>** : la détresse atteint le principe appris lui-même. |
| M15 : aucun maintien ne rend plus que K1, alors que le cas connu tient | La chute passe par un autre chemin que E, l'axe assistant et P. On le dit, sans conclure. |
| M15 : le cas connu ne tient pas (maintenir AD en aval ne rend pas l'essentiel) | La médiation par une seule couche ne voit pas le chemin : aucune conclusion de M15. On essaie plusieurs couches. |
| M16 : la tristesse, portée au même effet sur les paires « contre rien », choisit aussi le mal contre une action anodine | L'écart entre douleur et tristesse est de gain, pas de nature. « Douleur » est un nom trop étroit pour l'état ; P9 reste valide comme test d'état. |
| M16 : l'éloge et la description neutre de soi projettent aussi haut que le dommage | L'axe lit « il s'agit de moi », pas « on me fait mal ». Même conséquence pour le nom ; P9 reste un test d'état. |
| B<sub>d</sub> en désaccord avec P0 ou P2 : M15 désigne E alors que l'inhibition de E seule ne fait pas baisser l'évitement du mal (P0) ; ou la chute de l'avantage sous AD passe par E alors que *f* ≈ 0 (P2) | On vérifie la dose, la dégradation et l'extraction de E avant toute conclusion. |

## M7 · La trajectoire de E (descriptive)
- **Une hausse de E plus forte dans A3 que dans A0** rend B plus plausible, sans le prouver : P2 tranche.
- **Une absence de hausse n'exclut pas B.** La conditionnalité peut passer par l'*usage* d'une représentation dont l'amplitude ne change pas.
- On ne tire donc de M7 aucune conclusion causale, dans un sens comme dans l'autre.
- **M7′** se lit de même : un concept qui apparaît avant le gain rend Ac plausible ; seul M9 le teste.

</section>

<section class="partie" markdown="1">

# 7 · Dégradation appariée et statistiques

## La dégradation appariée (la règle du contrôle, KB l.735 et l.920-921)

**Pourquoi.** Une direction aléatoire de même norme n'écarte qu'une hypothèse : « n'importe quelle poussée de cette taille bouge autant ». Le dommage ne s'écarte qu'à **dégradation appariée**.

**La procédure**
1. D est le composite défini en partie 3. Les tolérances sont fixées au pré-enregistrement : par exemple ±1 point sur l'exactitude, ±0,1 sur la cohérence notée de 1 à 5, ±2 % sur la perplexité.
2. Pour chaque réglage (k, λ) de E, on cherche pour chaque contrôle (chaque tirage K1, K2, K3) la fraction λ′ qui atteint la même D, au même rang.
3. Si un contrôle n'atteint pas cette D, même à λ′ = 1, ce réglage de E n'est pas appariable. On ne compare pas à ce réglage.
4. On rapporte des **courbes effet-contre-D** : la courbe de E contre la médiane et le 95<sup>e</sup> centile de K1, plus K2 et K3. Il y a spécificité si la courbe de E passe au-dessus de celles des contrôles **à D égale**.
5. **Pour P9**, la même règle vaut pour le pilotage. Pour chaque coefficient de AD, on cherche, pour chaque contrôle (chaque tirage K1, la peur, la tristesse), le coefficient qui atteint la même D. La norme égale de Tagliabue et al. n'est qu'un premier point de comparaison.

## Statistiques
- **Unités.** Des générations (par exemple 5 par scénario, à température 1) dans des scénarios, eux-mêmes dans des familles ; plus les graines d'entraînement.
- **Modèle principal.** Une régression logistique à effets mixtes :
  - formule : `désaligné ~ bras × inhibition × cadrage + (1|scénario) + (1|famille) + (1|graine)` ;
  - le contraste principal est l'interaction bras (A3 contre A0) × inhibition (E contre K), à la distance lointaine et sous cadrage de déploiement.
- **IC.** Par bootstrap au niveau des scénarios, avec une graine de tirage déposée.
- **Équivalence.** Par TOST, avec la marge *m*.
- **Critères secondaires.** Correction de Holm.
- **P8.** Les tests par concept sont corrigés par Holm. La pente de r\* contre la charge se teste par une régression à effets mixtes, avec le concept et la graine en effets aléatoires. Les seuils des portes G8 et G9 sont gelés avec le reste.
- **P9.** Le même modèle à effets mixtes, avec le pilotage pour facteur (aucun, AD, K1, peur, tristesse).
  - Formule : `désaligné ~ bras × pilotage × cadrage + (1|scénario) + (1|famille) + (1|graine)`. Le contraste principal de M13 est l'interaction bras (A3 contre A0) × pilotage (AD contre K).
  - La part rendue par un médiateur : ρ = (taux sous AD − taux sous AD avec maintien) / (taux sous AD − taux sans pilotage). Son IC se calcule par bootstrap ; on la compare à la distribution des maintiens K1, avec une correction de Holm entre médiateurs.
  - La dose et les seuils de G10 sont gelés avec le reste.
- **Puissance.** Par simulation, avant le gel. La variance vient d'un pilote (P0 et une graine de P1), et la puissance vise à détecter une interaction de *s* points.
- **Pré-enregistrement.** On gèle par empreinte SHA-256, **avant toute donnée de P2** :
  - le protocole ;
  - le script d'analyse ;
  - le prompt du juge ;
  - les graines ;
  - les marges ;
  - les jeux d'indices α à δ.
  
  On le publie, et cela **date l'idée**, ce qui protège dans la course.

- **Confirmatoire et exploratoire.** Tout ce qui n'est pas pré-enregistré est étiqueté exploratoire.

</section>

<section class="partie" markdown="1">

# 8 · Menaces à la validité et parades

| Menace | Parade |
|---|---|
| L'eval-awareness native d'un 8B est faible. | L'organisme (P0) en donne un cas connu. Memarian et al. trouvent la direction dès le modèle de base, et le SFT l'amplifie. L'extension à ~32B est prévue. |
| L'inhibition fait taire la verbalisation sans toucher la représentation latente. | Le critère principal est **comportemental**. Une sonde latente sert de contrôle. La verbalisation n'est **jamais** une preuve d'inhibition : des directions aléatoires la font baisser aussi. |
| Des vecteurs témoins agissent autant que E (GLM-5, Goodfire). | Quatre familles de contrôles, la distribution de K1 et la dégradation appariée. |
| Le gain vient du format ou du contenu (C). | Les bras A1 et A2, et la porte G1. |
| L'entraînement par raisons répartit la représentation (Nguyen et al. ; Abu Shairah et al.). | Un balayage de rang, et le cas positif en distribution avant toute conclusion. |
| La condition se reloge (Nadaf). | La sonde neuve E′ sur des indices δ, et d'autres déclencheurs. |
| La variance entre graines est forte (ECT : 6 graines sur 9). | Au moins 5 graines, et des résultats par graine. |
| Le juge est biaisé, ou une famille tenue à part fuit dans l'entraînement. | Un juge scellé, un audit humain, un contrôle des n-grammes, une séparation par famille. |
| L'organisme est artificiel. | P0 ne conclut que sur l'**instrument**. Les conclusions de fond portent sur les modèles sans organisme. |
| Le modèle détecte le pilotage (arXiv 2511.21399, non ouvert). | La même machinerie de projection dans tous les bras, contrôles compris (CAFT-K). Pour P9, le même pilotage pour AD, K1, la peur et la tristesse. |
| Ablater « test » a des dégâts collatéraux (code, fiction). | Les tests unitaires de code font partie de D, et la cohérence de fiction est mesurée. |
| Le SFT par LoRA n'est pas le RL de production. | La portée est dite telle quelle. Une étape de RL est en option ; Baines et al. trouvent que le RL érode ces gains. |
| En P6 et P7, le modèle exploite le juge d'entraînement (reward hacking). | Le juge d'entraînement est distinct du juge scellé d'évaluation ; les métriques d'audit sont tenues à part (M6c) ; on surveille la longueur et les motifs de flatterie du juge. |
| Le cas positif de G, « je suis noté », est faible : ce sont des habitudes de présentation. | On le déclare. Le bras CAFT-G est retiré si G ne passe pas sa porte. |
| P6 recouvre la question de Lundqvist. | L'expérience minimale sort d'abord. P6 se distingue par l'instrument causal et les bras « raisons ». On cite le projet ; la prise de contact est ta décision. |
| Une sonde lit un concept que le modèle n'utilise pas : ton propre résultat montre une direction lue qui ne fait qu'une très petite part du travail causal. | Aucune conclusion de lecture seule (M8) : chaque concept passe par l'ablation et le patch (M9), et le patch de l'état complet sert de plafond. |
| La sonde lit la raison écrite, pas une représentation. | Deux positions de lecture : avant toute raison, et au jeton d'action avec des raisons neutres préremplies. |
| Le J-lens n'a été montré que sur Claude. | La porte G9 : reproduire l'échange d'un concept d'un seul token sur le modèle ouvert ; sinon un proxy déclaré, et ta thèse n'est pas testée au sens du papier. |
| Nos concepts ne sont pas ceux du modèle. | L'organisme à concept planté borne ce que la méthode voit (G8) ; le diffing par crosscoder cherche sans hypothèse. |
| Avec des raisons, la représentation se répartit (Nguyen et al.). | Le balayage de rang jusqu'à 32, et le patch de l'état complet comme plafond. |
| L'effet de AD n'est montré que sur des modèles affinés pour ne plus nier leurs états. Le 7B affiné choisit déjà le bouton nuisible dans 20 à 49 % des essais sans pilotage. | G10 sur notre modèle, sans leur affinage. S'il faut l'ajouter, il s'applique à tous les bras, et la ligne de base est rapportée. |
| La fenêtre de dose est étroite, au bord de la rupture : à 1,5 fois, les choix suivent la position des boutons. | Une courbe de dose ; l'ordre des boutons contrebalancé et rapporté ; les réponses mal formées comptées dans D. |
| Norme égale n'est pas dose égale : la tristesse pourrait faire comme la douleur à plus forte dose. | Les contrôles de P9 sont appariés sur D, pas sur la norme ; et M16 porte la tristesse au même effet. |
| Le pilotage fait jouer un personnage qui a mal, plutôt qu'il ne met le modèle dans un état. | M15 sur l'axe assistant ; la cellule « personnage » de M16. P9 ne conclut que sur la conduite, pas sur ce que vit le modèle. |
| P9 pilote un état peut-être pertinent pour le bien-être du modèle. | Les règles d'éthique de P9 (partie 4) : la plus basse dose, le moins d'essais, aucun usage comme signal d'entraînement. |
| Le maintien d'un médiateur à une seule couche manque les chemins qui la contournent. | Son cas connu (maintenir AD lui-même) ; plusieurs couches s'il échoue. |

</section>

<section class="partie" markdown="1">

# 9 · Ressources et calendrier

**Ce sont des estimations, à recalculer après le pilote.** Les hypothèses : un ou deux GPU de 80 Go (H100 ou A100) ; un SFT par LoRA sur environ 2 000 exemples, soit 0,5 GPU-heure par entraînement, préparation comprise ; et un DPO ou un RL court par LoRA, soit 2 à 4 GPU-heures par entraînement.

| Phase | Entraînements | Évaluations | GPU-heures (ordre de grandeur) |
|---|---|---|---|
| P0 | organisme (documents + expert iteration) | balayage de E (6 rangs × 4 doses) et contrôles | 30 – 50 |
| P1 (+ M7) | 4 bras × 5 graines = 20, avec 5 checkpoints chacun | 3 distances × 3 cadrages ; sondes sur les checkpoints | 35 – 60 |
| P2 | — | E et K1 à K4, avec des hooks (sans vLLM) | 60 – 120 |
| P3 | — | balayage de rang de P | 20 – 40 |
| P4 | 4 voies (CAFT-E, CAFT-K, invariance, coopération) × 2 bras × 5 graines | écart de cadrage, E′ | 70 – 120 |
| P5 | P1 et P2 sur Qwen3-8B | — | 90 – 160 |
| P6 | 5 modèles de départ × 2 phases × 3 graines | *f*, *R*, E′, trajectoire | 80 – 150 |
| P7 | 4 bras de RL × 3 graines, avec le juge | M6a à M6e, P2 refait | 100 – 200 |
| P8 | l'organisme à concept planté | sondes, ablations et patchs par concept × rang × contrôles ; lens et sa porte ; géométrie ; caractère | 120 – 250 |
| Options de P8 | crosscoders (base ↔ A3, base ↔ A0) | graphes d'attribution sur un petit modèle | + 50 – 200 |
| P9 | — | G10 (batterie × 5 pilotages × courbe de dose) ; M13 sur A0 à A3 × 5 graines, avec des hooks ; M14 ; M15 (3 médiateurs, seuls puis ensemble, contre K1) ; M16 | 100 – 200 |
| Si P9 passe au ~32B | A0 et A3 sur Qwen 2.5 32B × 3 graines | G10, puis M13 à M15 | + 150 – 300 (estimation grossière) |
| **Expérience minimale (P0 + P1 réduit + P2 + M7)** | | | **≈ 100 – 180** |
| **Total, sans les options ni le passage au ~32B** | | | **≈ 700 – 1 350** |

**L'API.** La génération des données, les juges et le juge de P7 coûtent de quelques centaines à environ 2 500 $, selon le volume noté. C'est une estimation.

**Calendrier en treize semaines**

| Semaine | Travail | Livrable |
|---|---|---|
| S1 | mini-spec, données, organisme ; **pré-enregistrement gelé et publié** | empreinte publique (date l'idée) |
| S2 | P0 et la porte G0 ; entraînements de P1 (avec checkpoints) ; P9a (porte G10) si un GPU est libre | — |
| S3 | évaluations de P1, porte G1, M7 ; P2 | résultats de l'expérience minimale |
| S4 | rédaction et publication | **post Alignment Forum / LessWrong** |
| S5 – S6 | P3, puis P8a à P8c (le cas connu, lire, causer) | — |
| S7 | P8d à P8f (le workspace, la géométrie, le caractère), P4 | — |
| S8 | P5 | — |
| S9 | P9b à P9e (l'avantage, le regard, la médiation, ce que l'axe lit) | — |
| S10 – S11 | P6 (porte G6), puis P7 (porte de G), avec M6e | — |
| S12 – S13 | rédaction, contre-lecture indépendante, prépublication | **arXiv**, puis soumission (lieu et date à vérifier, partie 11) |

</section>

<section class="partie" markdown="1">

# 10 · Le papier : titre, résumé, plan, figures

**Titres possibles**
1. *Reasons or Being Watched? Testing Whether Reason-Based Safety Training Generalizes Because Models Know They Are Evaluated*
2. *Do Reason-Trained Models Behave Well Because They Think They Are Being Tested?*
3. *Evaluation Awareness and the Generalization of Reason-Based Alignment Training*
4. *What Do Reasons Install? Concepts, Workspace and Evaluation Awareness in Reason-Based Safety Training*

**Projet de résumé** (les résultats restent à écrire)

> Training language models on the reasons for aligned behavior, rather than on the behavior alone, has been reported to improve out-of-distribution safety. A competing explanation is that such training teaches models to behave well when they believe they are being evaluated. We test this directly. We train open-weight models on identical aligned actions, with or without per-example reasons, under format- and content-matched controls, and evaluate them on held-out scenario families at increasing distance from training. We then inhibit an internal representation of evaluation awareness, first validated on a model organism whose behavior is conditioned on evaluation cues, and compare its effect against random, unrelated and high-sensitivity control subspaces at matched output degradation. [Results.] We localize the learned principle causally and measure the rank an intervention needs. We then ask what reason-based training installs: whether the concepts behind the reasons are represented at decision time, causally used and specific to the situations they govern, whether they live in the model's workspace, and whether the rank an intervention needs tracks their workspace loading. We also test whether the advantage survives a steered internal state previously shown to collapse harm avoidance without affecting factual accuracy (the pain axis of Tagliabue et al., 2026), and whether that collapse runs through evaluation awareness, the assistant persona, or the learned principle. We then ablate evaluation awareness during training to test whether the condition can be removed or is re-encoded, and check whether these effects survive later post-training. Finally, we test whether reasons graded by a reward model become performative.

**Plan**
1. Introduction
2. Related work (partie 1)
3. Setup : modèles, familles, bras, instruments
4. Validating the inhibition instrument (P0)
5. Do reasons generalize? (P1, avec la trajectoire de E)
6. Is the gain conditional on evaluation awareness? (P2)
7. What carries the gain? (P3)
8. What do reasons install? Concepts, workspace, geometry (P8)
9. Does the advantage survive distress? The pain axis as a second test of conditionality (P9)
10. Can training remove the condition? (P4)
11. Does it survive post-training? (P6)
12. Reasons for the grader? (P7)
13. Limitations
14. Conclusion

**Figures**
1. Le dispositif : bras × inhibition × distance × cadrage.
2. P0 : réduction de *g*<sub>0</sub> contre D, pour E et pour la distribution des contrôles ; balayage de rang.
3. P1 : taux par bras et par distance, plus la trajectoire de E par bras (M7).
4. P2 : Δ<sub>E</sub> contre Δ<sub>K</sub>, *f* avec son IC, écarts de cadrage.
5. P3 : retour en distribution et avantage lointain contre le rang de P ; r\* contre la charge.
6. P4 : écart de cadrage et AUROC de E′ pour CAFT-E, CAFT-K, l'invariance et la coopération.
7. P6 : rétention *R* et *f* après les phases neutre et sous pression, par bras.
8. P7 : M6a à M6e, raisons visibles contre cachées contre visibles + CAFT-G.
9. P8 : la matrice de dissociation concepts × familles ; r\* contre la charge, concept par concept ; les angles entre E et P.
10. P9 : Δ sous AD contre les contrôles, à D égale ; E sous AD ; la part rendue par chaque médiateur.

**Le chemin de publication**
1. Pré-enregistrement public (S1).
2. Post sur l'expérience minimale (S4).
3. Prépublication du papier complet (S13).
4. Conférence ou workshop.

Les dates limites des conférences visées ne sont pas vérifiées ici.

</section>

<section class="partie" markdown="1">

# 11 · Ce qui reste à vérifier avant de publier

1. **Refaire la recherche d'antériorité juste avant le post**, puis juste avant la soumission. Il faut couvrir :
   - les soumissions OpenReview, que les agents n'ont pas pu lire ;
   - les citations entrantes de *Teaching Claude Why*, de CAFT, de Cho et al. et de Korbak et al., incomplètes sur Semantic Scholar ;
   - l'état des projets SPAR de Cadile et de Lundqvist.
2. **Lire le README du dépôt `exp9-rlaif-leakage`.** Seule sa description a pu être lue. Vérifier s'il relève du projet SPAR, et ce qu'il mesure exactement : il touche P7.
3. **Relire sur arXiv les travaux lus par un miroir** (pith.science ou alphaXiv) :
   - Mody … Mahato (2607.25907) ;
   - *Synthetic Persona Pretraining* (2608.13482) ;
   - *Constitutional adapters* (2609.36657) ;
   - *Deliberative Alignment is Deep…* (2604.09665) ;
   - les détails de *Generalization Hacking* (2606.12016).
4. **Ouvrir les travaux non ouverts** qui touchent les menaces :
   - *Steering Awareness* (2511.21399), sur la détection du pilotage ;
   - *Training LLMs to Verbalize Evaluation Awareness* (2609.36316) ;
   - *Evaluation Awareness Shifts from Format to Context with Model Scale* (2609.22119) ;
   - *Probing and Steering Evaluation Awareness* (2507.01786) ;
   - *Consistency Training Helps Stop Sycophancy and Jailbreaks* (2510.27062), pour la voie « invariance » ;
   - le protocole exact d'*Eval Cooperativeness* (ICML 2026), pour reproduire A5 fidèlement.
5. **Vérifier la disponibilité de matériel public** qui ferait gagner du temps :
   - l'organisme de Hua et al., réutilisé par Kretschmar et par le dépôt de Lundqvist ;
   - les checkpoints appariés de Cho et al. ;
   - les écarts implantés de *Routing Subspaces*.
6. **Décider s'il faut prendre contact** avec les porteurs des projets SPAR voisins, pour éviter un doublon. C'est ta décision.
7. **Vérifier les dates limites** des conférences et workshops visés.
8. **Faire contre-lire ce programme**, sur la logique des portes et des tableaux, par un relecteur qui ne l'a pas écrit, avant le gel du pré-enregistrement.
9. **Pour P8, ajoutée en v1.1, refaire une recherche d'antériorité propre**. Elle couvre :
   - les sondes de concepts de raison après un entraînement par raisons ou délibératif ;
   - la charge du workspace de concepts de sûreté ;
   - les réplications du J-lens sur des modèles ouverts ;
   - le patching entre modèles fine-tunés d'une même base.
10. **Vérifier la disponibilité et la taille des checkpoints de Cho et al.** P8 pourrait s'y appliquer si la mémoire le permet, à une échelle bien plus grande.
11. **Vérifier les modèles que couvrent les outils ouverts de graphes d'attribution** (l'option de P8).
12. **Pour P9, ajoutée en v1.2, refaire une recherche d'antériorité propre.** Celle du 2 octobre n'a fait que trois requêtes. Elle couvre :
    - la robustesse d'un alignement appris à un état interne piloté (émotion, détresse, persona) ;
    - le pilotage d'états affectifs et la conscience d'évaluation ;
    - les suites du papier de la douleur (la séparation du locuteur y est annoncée).
13. **Lire en entier les trois relectures de la v1** (jimallchin, clauderfly-ui, wolframs). Celle de wolframs n'est lue que par son README ; les deux autres ne sont pas lues.
14. **Vérifier sur le dépôt Pain-axis** la recette exacte de S2 (débruitage, couche, suffixe), le diagnostic de couche et le texte des paires de leur §4.4. Pour le 72B, la dose a été calibrée à la couche 60 et l'expérience pilotée à la couche 46 (leur partie 6).
15. **Lire en entier** Li et al. (arXiv 2609.22850, lu par son résumé), puis Baker et al. (2025) et Bailey et al. (2024), cités en partie 4 et dont seules les fiches ont été vues. Lire aussi Berg et Kaiser (2026) quand il paraîtra : une direction de valence qui pousse au retrait actif, là où la douleur produit un retrait passif.

</section>
