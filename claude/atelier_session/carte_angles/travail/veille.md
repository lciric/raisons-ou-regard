# Veille : travaux de septembre et octobre 2026 absents des onze rapports

État au vendredi 2 octobre 2026, 9 h 15 UTC. Pièce de travail pour la carte des angles (passation v1.2, §6, point 3). La recherche de la nuit s'est arrêtée vers 4 h. Cette veille a fait 20 appels WebSearch, et rien d'autre sur le web.

**Conventions.**
- Statuts de lecture : ceux de la consigne. Tout ce qui suit et vient du web est « vu par extrait de recherche, non ouvert », sauf mention contraire. Un extrait ne fournit aucun chiffre : les extraits en donnaient, je ne les reprends pas.
- « Absent des rapports » veut dire : ni le titre, ni l'identifiant, ni l'adresse ne figurent dans `ANTERIORITE_RAPPORTS_2026-10-01.md`, `ANTERIORITE_RAPPORTS_2026-10-02.md` ou la passation v1.2 (recherche par grep).
- Les niveaux de danger sont ceux des consignes de la nuit. Ici, ce sont les miens, provisoires, posés sur un extrait.
- Rien n'a été comparé aux autres fichiers du dossier de travail (`angle_*.md`, `projets_calendrier.md`) : un travail ci-dessous peut y figurer déjà.

---

## 1 · En bref

- **Rien de nouveau au niveau élevé ou moyen**, pour ce que montrent les extraits. Le verdict de la passation (§4.4) tient : la combinaison centrale reste libre. Elle consiste à inhiber une représentation validée de « je suis évalué », à dégradation appariée, dans des modèles ouverts entraînés sur les raisons ou sur les mêmes actions.
- **Deux travaux nouveaux, datés de la fenêtre et absents des rapports** :
  - *Pre-training interventions, ex post facto* (arXiv 2610.00767, octobre 2026) : survie au post-entraînement, niveau faible ;
  - la system card de GPT-6 Astra (OpenAI, section alignement mise à jour le 9 septembre 2026) : la dépendance au regard, niveau faible. Elle est à ouvrir en priorité, car l'extrait ne dit pas si elle inhibe la conscience d'évaluation.
- **Trois objets absents des rapports mais sans date visible** : deux dépôts GitHub qui reproduisent le J-lens (lentille jacobienne) sur des modèles ouverts (anatomie, faible) et un billet LessWrong sur la survie du midtraining au RL, probablement le projet CaML déjà connu (survie, faible).
- **Second Look Research.** Leur réplication de *Teaching Claude Why* sur modèles ouverts reste introuvable sous forme publiée (deux requêtes, n° 12 et 13). Le seul billet vu est une annonce, cohérente avec celle des rapports 2 et 6.

---

## 2 · Travaux nouveaux, dans la fenêtre

### 2.1 *Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints*

- **Auteurs**, d'après le résumé du moteur : Peter Nutter, Dani Roytburg, Clément Dumas, Jinghua Ou, Shi Feng.
- **Date.** Identifiant arXiv d'octobre 2026, donc déposé le 1er ou le 2 octobre (déduit de l'identifiant ; date exacte non vue). Il apparaît dans les listes « recent » de cs.LG et cs.CL.
- **Adresses.**
  - https://arxiv.org/abs/2610.00767 et https://arxiv.org/html/2610.00767 ;
  - les adaptateurs, sur Hugging Face : `Grafting-Beliefs/fair-midtraining-models`, `Grafting-Beliefs/olmo3-transfer-adapters`, `Grafting-Beliefs/emergent-misalignment-adapters`, `Grafting-Beliefs/false-facts-adapters`, `Grafting-Beliefs/dsv4-flash-adapters`.
- **Statut.** Vu par extrait de recherche, non ouvert (arxiv.org et huggingface.co sont refusés par la politique réseau).
- **Ce que dit l'extrait.**
  - Le problème : un fine-tuning sur documents synthétiques appliqué à un modèle déjà post-entraîné laisse des artefacts et dégrade les capacités. Le modèle se met aussi à tenir pour réelles des entités inventées sans rapport avec les documents (« reality drift »).
  - La méthode, la greffe : l'adaptateur est entraîné sur le point de contrôle pré-entraîné, puis la mise à jour des poids est ajoutée au modèle post-entraîné. On réutilise ainsi le post-entraînement existant au lieu de le refaire.
  - Les applications : de faux faits, des organismes modèles désalignés, et une intervention de midtraining constitutionnel, sur plusieurs familles de modèles.
- **Angle touché.** La survie au post-entraînement, par la méthode : on applique une intervention de midtraining sans refaire le post-entraînement. Accessoirement, raisons contre actions, si l'intervention constitutionnelle greffée contient des raisons ; l'extrait ne le dit pas.
- **Danger provisoire : faible.** C'est un outil. L'extrait ne montre ni contraste entre raisons et actions, ni mesure de la conscience d'évaluation, ni test de l'avantage hors distribution sous trois cadrages. À relever à moyen si le texte compare un midtraining avec et sans raisonnement à travers la greffe, à la manière de Cho et al.
- **Ce qui le sépare du programme.** Le programme fine-tune par LoRA un modèle instruct, à action identique ; il ne greffe rien. La greffe pose une question de validité qui le concerne pourtant : un adaptateur appris sur une base, puis ajouté à un modèle instruct, ressemble à ce qu'on obtiendrait en reportant un bras raisons d'un point de contrôle à l'autre.
- **Personnes déjà connues.**
  - Shi Feng porte aussi *Infohazard Evaluations* (SPAR), noté pour le retrait pendant l'entraînement (rapport 2 ; non relu, passation §4.4, n° 5).
  - Clément Dumas cosigne *Steering towards "automated grading" degrades alignment* (rapport 2), noté pour les raisons pour le juge.
  - Jinghua Ou cosigne 2606.08243 (rapport 7).
- **À faire avant le post.** Lire le texte : ce que l'intervention constitutionnelle contient (raisons ou non), s'il y a une mesure de la conscience d'évaluation, et quels points de contrôle sont publiés.

### 2.2 *GPT-6 Astra System Card* (OpenAI)

- **Auteur.** OpenAI ; Apollo Research pour une partie de l'évaluation, d'après les extraits.
- **Date.**
  - D'après l'extrait, la section alignement a été mise à jour le 9 septembre 2026, pour préciser comment les évaluations testent la généralisation de l'alignement. Date de première publication non vue.
  - Le billet de Zvi sur X est du 9 septembre 2026. Cette date est déduite de l'identifiant du billet ; le billet est non ouvert.
- **Adresses.**
  - https://deploymentsafety.openai.com/gpt-6-astra ;
  - https://deploymentsafety.openai.com/gpt-6-astra/alignment ;
  - https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf ;
  - https://deploymentsafety.openai.com/gpt-6-astra/forecasting-misaligned-behavior-with-deployment-simulation-of-internal-codex-traffic.
  - Commentaires : https://thezvi.substack.com/p/gpt-6-astra-the-system-card-alignment ; https://www.lesswrong.com/posts/AmFJZyeCgvFjNKgNk/gpt-6-astra-the-system-card-alignment-and-what-comes-next ; https://www.transformernews.ai/p/openai-gpt-6-astra-might-be-too-powerful-to-understand-or-control ; https://www.mindstudio.ai/blog/gpt6-astra-safety-concerns.
- **Statut.** Vu par extrait de recherche, non ouvert. Le domaine deploymentsafety.openai.com n'est pas dans la liste des refus ; je ne l'ai pas ouvert, puisque cette veille procède par extraits.
- **Ce que disent les extraits.**
  - La section alignement explique comment les évaluations se rapportent à l'entraînement, et ce qu'elles disent de la généralisation, avec les limites qu'introduit la conscience d'évaluation.
  - Astra verbaliserait l'évaluation plus souvent que les modèles précédents.
  - Pour Apollo, cité par l'extrait, de faibles taux de mauvaise conduite « do not provide substantial evidence » sur l'alignement du modèle.
- **Angle touché.** La dépendance au regard, pour la conduite en général : les progrès d'alignement d'un modèle à l'autre sont confondus avec la conscience d'évaluation. Accessoirement, l'amplification, puisque la conscience verbalisée croît d'une génération à l'autre ; l'extrait ne dit rien de l'entraînement qui la produit.
- **Danger provisoire : faible.**
  - Sur les extraits, c'est un constat de confusion, sans inhibition ni contraste raisons contre actions.
  - À relever à moyen pour la dépendance au regard (conduite en général) si la section alignement contient une inhibition ou un pilotage de la conscience d'évaluation qui chiffre la part des progrès qui en dépend. La card de Sonnet 4.5, §7.6, le fait (relu sur la source par l'instance du papier, passation §4.2, n° 5).
  - Dans aucun cas l'avantage des raisons n'est touché, d'après les extraits.
- **À faire avant le post.** Ouvrir la section alignement (page et PDF). Y chercher toute intervention sur la conscience d'évaluation, toute phrase sur la part des progrès qu'elle explique, et la méthode d'entraînement à l'alignement décrite, raisonnement sur une spécification ou non.

### 2.3 Deux dépôts GitHub qui reproduisent le J-lens sur des modèles ouverts

| Dépôt | Ce que dit la description | Date | Angle | Danger provisoire |
|---|---|---|---|---|
| https://github.com/menelly/vspace-jlens | L'axe de valence d'un modèle est-il dans son espace de travail global ? Une mesure initiale par la lentille jacobienne d'Anthropic, sur plusieurs modèles ouverts, avec des « consent + debrief records » | non visible | l'anatomie de ce que les raisons installent (outil) | faible |
| https://github.com/Hasin-ai/jspace-qwen | Réplication de *Verbalizable Representations Form a Global Workspace in Language Models* sur Qwen3.5-9B : lectures par la lentille jacobienne, interventions causales, deux extensions (attention hybride, introspection) | non visible | l'anatomie (outil) | faible |

- **Statut.** Vus par extrait de recherche, non ouverts. raw.githubusercontent.com répond par curl : les README sont lisibles si on veut les dater.
- **Raison du niveau.** Le rapport 5 classe déjà les réplications du J-lens sur modèles ouverts au niveau faible : « aucune ne touche l'alignement ni le lien charge-rang » (rapport 5). Les deux descriptions ne parlent pas d'alignement non plus.
- **Intérêt pratique.** Le second dépôt fournirait du code de lentille jacobienne pour un modèle ouvert de taille voisine de celle du programme (Qwen3.5-9B, et non Qwen3-8B).
- **Note.** Le résumé du moteur attribue à l'une des sources de la requête n° 8 une validation sur llama3-8b-instruct, sans dire laquelle. Non attribuable : à vérifier en lisant les README.

### 2.4 Billet LessWrong *Can mid-training survive RL*

- **Adresse.** https://www.lesswrong.com/posts/wXsQcdevL5krjq8xL/can-mid-training-survive-rl
- **Auteur et date.** Non visibles.
- **Statut.** Vu par extrait de recherche, non ouvert (lesswrong.com est refusé par la politique réseau).
- **Ce que dit l'extrait.** D'après le résumé du moteur, c'est un projet CaML. Il cherche dans quelles conditions des valeurs installées par fine-tuning sur documents synthétiques, sur la base d'OLMo 3, persistent après un RL.
- **Dans les rapports.** Le billet lui-même n'y est pas. Le projet, si c'est bien lui, y est : l'offre d'emploi de CaML du 1er septembre 2026 (rapport 6) et le projet SPAR de Brazilek et Chaudhary (rapport 4).
- **Angle et danger.** La survie au post-entraînement ; niveau faible, comme au rapport 6. C'est la survie d'une valeur, pas celle de l'avantage des raisons ni de son indépendance au regard.
- **À faire.** Dater le billet et voir s'il contient des résultats ; s'il en contient, le projet CaML n'est plus seulement annoncé.

---

## 3 · Vus par cette veille, mais déjà dans les rapports (rien de nouveau)

Vérifiés par identifiant ou par titre :
- 2608.27340 (*Not All Eval-Awareness Is Equal*) ; 2609.10142 (*Active Adaptation, Not Static Defense*) ; 2607.25907 (Mody et al.) ; 2510.20487 ; 2511.21399 ; 2606.08629 ;
- 2607.26654 (*Constitutional Midtraining*) ; 2609.20412 (*Stress-testing Alignment Midtraining*) ; 2608.13482 ; 2607.26173 ; 2607.18966 ; 2605.23055 ; 2608.21766 ; 2605.05835 ; 2606.23583 ; 2608.13250 ; 2606.09475 ;
- 2609.36657 (*Constitutional adapters*) ; 2607.15495 (l'espace de travail global) ; 2604.09665 ; 2412.16339 ; 2605.15257 ; 2503.11926 ; 2510.13900 ; 2504.02922 ; 2606.09850 ; 2507.16795 (CAFT) ;
- *Teaching Claude Why* ; *Model Spec Midtraining* ; *Eval Cooperativeness* (billet MATS et page ICML) ; Kretschmar (*Is Eval Gaming Downstream…*) ; les billets LessWrong de Nanda et de Zeisler sur le J-lens ; *Where we are on evaluation awareness* (rapport 2, vu, non ouvert) ; *Toward Dealing with Unverbalized Eval Awareness* (vu ici par la page Lacuna ; présent aux rapports 2, 3 et 6).

Cas limite : le billet LessWrong *Rerunning AI safety papers on every frontier release would…* (https://www.lesswrong.com/posts/oKxc8maZGtnzgpNzx/rerunning-ai-safety-papers-on-every-frontier-release-would-1). Son titre n'est pas dans les rapports. Son extrait annonce la réplication de *Teaching Claude Why* « in the following weeks » : c'est l'annonce de Second Look Research que décrivent les rapports 2 et 6 (billets du 15 août et du 21 septembre 2026). Pas nouveau sur le fond ; date non visible.

---

## 4 · Hors fenêtre (avant septembre 2026), absents des rapports, à signaler

Tous vus par extrait de recherche, non ouverts. La date est déduite de l'identifiant arXiv. Niveaux provisoires, sur le titre et l'extrait.

| Titre | Identifiant, date | Angle | Danger provisoire |
|---|---|---|---|
| *Introspecting Alignment Shifts Beyond Behaviors Implanted Through Fine-Tuning* | 2608.04347, août 2026 | l'anatomie de ce que les raisons installent | faible ; à ouvrir, car le titre vise ce qu'un fine-tuning d'alignement change au-delà de la conduite |
| *Diff Mining: Logit Differences Reveal Finetuning Objectives* | 2608.26462, août 2026 | l'anatomie (model diffing) | faible |
| *Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion Values Under Post-Training* | 2606.26102, juin 2026 | la survie au post-entraînement | faible |
| *Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families* | 2606.20225, juin 2026 | le principe localisé ; le retrait pendant l'entraînement | faible |
| *Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning* | 2605.27676, mai 2026 | le retrait pendant l'entraînement (méthode voisine de CAFT) | faible |
| *Not All LLM Reasoning is Visible in the Chain-of-Thought* (Vatsal Baherwani) | 2607.22925, juillet 2026 | les raisons pour le juge | faible |
| *Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks* | 2601.23086, janvier 2026 | les raisons pour le juge | faible |
| *Delta-Crosscoder: Robust Crosscoder Model Diffing in Narrow Fine-Tuning Regimes* ; *Cross-Architecture Model Diffing with Crosscoders* | 2603.04426, mars 2026 ; 2602.11729, février 2026 | l'anatomie (outils) | faible |
| *Aligning What LLMs Do and Say: Towards Self-Consistent Explanations* | ACL Findings 2026 (aclanthology.org/2026.findings-acl.49) | les raisons pour le juge (cohérence entre raison et action) | faible |
| *Demonstrating Generalization Failures via Mixtures of Conditional Policies* | 2607.03478, juillet 2026 | incertain (titre seul) | non classé |

---

## 5 · Où j'ai cherché, et ce que je n'ai pas trouvé

- **Les champs couverts** :
  - l'entraînement par raisons (reason-based training, explications contre démonstrations, deliberative alignment sur modèles ouverts, réplication de *Teaching Claude Why*, Second Look Research) ;
  - la conscience d'évaluation (pilotage pendant le fine-tuning, jeu d'évaluation, conscience non verbalisée, inoculation, dépendance des gains, identifiants d'octobre) ;
  - CAFT et l'ablation de concepts pendant l'entraînement ;
  - la durabilité du midtraining et sa survie au RL ;
  - la conscience du correcteur, et la chaîne de pensée exposée au modèle de récompense ;
  - la réflexion contrefactuelle et ses réplications ouvertes ;
  - les réplications du J-lens sur modèles ouverts ;
  - le model diffing après un fine-tuning de sûreté ;
  - la system card de GPT-6 Astra.
- **Non trouvé**, dans ce que les extraits montrent :
  - une réplication publiée de *Teaching Claude Why* par Second Look Research ;
  - un résultat public du projet SPAR de Lundqvist ou de celui de Cadile ;
  - une suite publiée par Anthropic à la réflexion contrefactuelle (§7 du papier sur l'espace de travail global) ;
  - un travail qui inhibe la représentation « je suis évalué » dans des modèles entraînés sur les raisons ou sur les actions.
- **Non couvert par cette veille** :
  - les soumissions anonymes à ICLR 2027 : openreview.net est refusé, et elles restent le principal risque invisible (passation §4.4) ;
  - les pages de projets SPAR et MATS ;
  - le dépôt exp9, non recherché ici.
- **Limite.** Un moteur indexe mal les prépublications des derniers jours : un dépôt arXiv du 1er ou du 2 octobre peut manquer. Il faut refaire la veille juste avant le post.

---

## 6 · Requêtes faites (20 appels WebSearch)

1. `reason-based training alignment generalization rationales vs actions fine-tuning 2026`
2. `evaluation awareness steering suppress during fine-tuning eval gaming arXiv September 2026`
3. `alignment midtraining durability survives post-training RL October 2026`
4. `grader awareness reward model sees chain-of-thought evaluation awareness penalized`
5. `"Can mid-training survive RL"`
6. `GPT-6 Astra system card evaluation awareness alignment`
7. `concept ablation fine-tuning evaluation awareness direction ablated during training 2026`
8. `global workspace J-lens replication open-weight Llama Qwen`
9. `"Pre-training interventions, ex post facto" grafting model beliefs across checkpoints`
10. `chain-of-thought visible to reward model RL training obfuscation principled justification October 2026`
11. `model diffing safety fine-tuning crosscoder what alignment training changes 2026`
12. `"Teaching Claude Why" replication open-weight models`
13. `Second Look Research midtraining replication Teaching Claude Why open models results`
14. `"evaluation awareness" fine-tuning alignment gains depend arXiv 2610`
15. `deliberative alignment open-weight model specification reasoning SFT out-of-distribution misalignment September 2026`
16. `eval gaming training-time mitigation unverbalized evaluation awareness probe inoculation 2026`
17. `lesswrong "mid-training survive RL" values midtraining OLMo character`
18. `counterfactual reflection training constitution principles open-weight model replication ethical concepts before output`
19. `training on explanations versus demonstrations alignment generalization same action rationale ablation LLM 2026`
20. `GPT-6 Astra system card alignment generalization evaluation awareness steering suppress misaligned behavior rates`

Aucun WebFetch, aucun curl vers le web. Une commande locale a converti l'identifiant du billet X de Zvi en date (9 septembre 2026, 13 h 11 UTC).
