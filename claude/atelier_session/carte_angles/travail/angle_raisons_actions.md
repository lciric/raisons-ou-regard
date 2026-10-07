# Angle : raisons contre actions

**La question.** Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?

**Les sources de cette fiche** (2 octobre 2026) :
- les deux rapports du 1er octobre qui touchent l'angle : l'axe « raisons contre actions » et l'axe « la combinaison exacte » ;
- le rapport 1 de la nuit, en entier, et ce qui touche l'angle dans les rapports 2 à 7 ;
- les §4 et §5.5 de la passation v1.2 ;
- le complément de l'architecte, pour ce que contient la v1.3 ;
- six recherches web du 2 octobre, dont je n'ai vu que les extraits.

**Les libellés de lecture** sont ceux de la consigne. Les deux rapports du 1er octobre n'ont pas de numéro : je les désigne par leur axe (« rapport du 1er octobre, raisons contre actions » ; « rapport du 1er octobre, combinaison exacte »). Les rapports sont des sorties de modèles : un fait qui n'y figure que « rapport » n'est pas établi. Quand le §4.3 corrige un rapport, la correction fait foi.

---

## Le verdict

**Partiellement pris.** L'effet brut est déjà publié, et chacun des contrôles du programme existe déjà ailleurs, mais seul :
- **L'effet brut** : *Teaching Claude Why* et *Model Spec Midtraining* ; pour les jailbreaks, *Safety Reasoning with Guidelines*.
- **La phrase neutre avant l'action** : dans un jouet (de la Fuente et Conmy).
- **Les raisons retirées, à scénario et action identiques** : chez Cho et al. (relu). Le résultat est nul, puis défavorable après un RL bénin.
- **La réponse finale fixée sous des raisonnements variés** : chez Wen et al. (lu par un site tiers).
- **Un contrôle de longueur entre explications de valeurs et sous-règles** : dans la spécification de *Model Spec Midtraining*.

Aucun travail vu par les onze rapports ne réunit ces contrôles : l'action identique mot pour mot, le texte neutre de même longueur, le raisonnement d'une autre situation, les familles tenues à part jusqu'à l'agentique à plusieurs tours, les trois cadrages, sur des modèles ouverts de 8B en LoRA.

Le verdict concorde dans le rapport 1 (§4), le rapport 6 (§4), le rapport du 1er octobre (raisons contre actions, §3) et la passation v1.2 (§4.4, n° 1).

---

## Les travaux, du plus dangereux au moins dangereux

### 1. *Teaching Claude Why*
- **Auteurs** : Jonathan Kutasov (premier) … Sara Price (dernière), 11 auteurs.
- **Date** : 8 mai 2026. La version anthropic.com a été modifiée le 20 mai.
- **Lieu** : Alignment Science Blog d'Anthropic, `alignment.anthropic.com/2026/teaching-claude-why/`. Pas sur arXiv, donc pas de graphe de citations.
- **Statut de lecture** : rapport 1, texte intégral ; rapport 6, texte intégral ; rapport 4, texte intégral. **Non relu par l'instance du papier.**
- **Ce qu'il fait** :
  - SFT de Claude Sonnet 4 et de Haiku 4.5 (rapport 6).
  - Sur des pots de miel synthétiques, des actions alignées filtrées font passer le désalignement agentique de 22 % à 15 %. Des réponses générées sous une incitation à délibérer sur l'éthique, incitation retirée avant l'entraînement, le font descendre vers 3 % (rapports 1 et 6).
  - Un jeu de conseils sur des dilemmes, éloigné de l'évaluation, atteint le même niveau avec environ 3 M de tokens contre 85 M. Titre de section : « the reasons matter more than the actions » (rapport 6).
- **Danger : moyen, le plus haut de l'angle ; élevé pour la seule affirmation « les raisons généralisent mieux que les actions ».** Il établit l'effet que le programme veut contrôler.
- **Ce qui le sépare du programme** :
  - les réponses délibérées sont générées à neuf, donc l'action n'est pas tenue identique ;
  - ni texte neutre, ni raisonnement d'une autre situation ;
  - les modèles sont fermés, et il n'y a aucune interprétabilité ;
  - aucune mesure de la conscience d'évaluation (rapports 1, 2 et 3), alors que les pots de miel d'entraînement sont conçus pour ressembler au jeu d'évaluation (rapport 1).

### 2. *Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models*
- **Auteurs** : Antón de la Fuente (premier), Arthur Conmy (dernier), travail MATS.
- **Date** : 28 juillet 2026 d'après OpenAlex et Semantic Scholar ; 20 août d'après la page MATS (rapport 1).
- **Lieu** : arXiv 2607.26173.
- **Statut de lecture** : rapport 1, texte intégral ; rapport 4, texte intégral ; rapport du 1er octobre (raisons contre actions), texte intégral ; rapport du 1er octobre (combinaison exacte), lu par un site tiers (pith.science).
- **Ce qu'il fait** :
  - **Dans un jouet** : la tâche est de mettre la réponse en `\boxed{}`, sur Qwen3-4B avec une LoRA de rang 32. Le transfert hors maths passe de 10,3 % (exemples seuls) à 94,5 % (raison et exemples). Deux phrases neutres donnent 44,5 % et 62,5 % ; d'autres remplissages, 21,5 à 24,7 % (rapport 1).
  - **Sur le bien-être animal et l'auto-préservation** (Qwen3.5-4B d'après le rapport 1) : une réécriture qui rend explicite la raison propre à la cible généralise mieux qu'une version « dépouillée », où la même recommandation reçoit des raisons pratiques ordinaires. C'est vrai aussi sur un audit interactif de 36 scénarios, jusqu'à 8 tours.
  - Le juge note la conscience d'évaluation, mais ces scores ne sont pas rapportés (rapport 1).
- **Danger : moyen, le plus proche par les contrôles.** Il a déjà un contrôle de format par texte neutre (dans le jouet) et un contrôle de contenu par raisons de substitution, sur la même situation.
- **Ce qui le sépare du programme** :
  - le texte neutre n'existe que dans le jouet, et aucun appariement de longueur n'est rapporté ;
  - la recommandation est appariée en substance, pas mot pour mot ;
  - aucun raisonnement d'une autre situation ;
  - ses cibles sont un trait de bien-être et un trait désaligné, pas une conduite alignée en situation d'alignement ;
  - aucun indice d'évaluation ou de déploiement, des modèles de 4B, aucune interprétabilité.

### 3. *Constitutional Midtraining: Content Presence Drives Alignment Gains*
- **Auteurs** : Desiree Cho (première) … Nigel Shadbolt (dernier). Les sept auteurs : Cho, Tice, Hogan, Batra, Radmard, Zhao, Shadbolt (§4.3).
- **Date** : v1 du 29 juillet, v2 du 30 juillet, v3 du 18 août 2026.
- **Lieu** : arXiv 2607.26654.
- **Statut de lecture** : le résultat principal est **relu sur la source par l'instance du papier** (§4.2, n° 9, HTML v3). Le reste vient des rapports 1, 4 et 7, en texte intégral.
- **Ce qu'il fait** :
  - Plan 2×2 qui croise un curriculum et un raisonnement délibératif. Midtraining de Nemotron-3-Super-120B-A12B-Base, puis SFT neutre, puis RL bénin (GRPO sur GSM8K) (rapport 4).
  - Le bras sans raisonnement garde le scénario et l'action. On en retire le bloc qui explique comment la valeur motive l'action, soit environ 45 % du document (rapports 1 et 7).
  - Relu : les deux bras sont indistinguables après le midtraining et après le SFT. Après le RL bénin, le bras avec raisonnement fait plus de chantage : +9,0 points, p < 0,05 (31,0 % contre 22,0 %, table 2).
  - Les auteurs écrivent ne pas pouvoir exclure la conscience d'évaluation (« cannot rule out … eval-awareness »).
- **Danger : moyen.** C'est le précédent le plus direct du retrait des raisons à action identique, avec un résultat nul puis défavorable. Il est à citer au centre, comme contre-résultat.
- **Ce qui le sépare du programme** :
  - c'est un midtraining sur documents, à 120B, pas un SFT LoRA d'une action précédée de différents textes ;
  - aucun témoin de même longueur : le bras sans raisonnement fait 47 à 54 % de la longueur (rapport 4), et l'exposition en tokens n'est pas appariée d'après le rapport 1 ;
  - aucun raisonnement d'une autre situation ;
  - il mesure un écart de conformité surveillé / non surveillé, par prompt, dans les deux bras (rapports 1 et 7), mais ni indice d'évaluation au sens du programme, ni inhibition ;
  - ses 15 points de contrôle sont publics, mais inutilisables à 8B : environ 241 Go chacun (§4.3).

### 4. *Model Spec Midtraining: Improving How Alignment Training Generalizes*
- **Auteurs** : Chloe Li (première) … Jon Kutasov (dernier).
- **Date** : v1 du 3 mai 2026, v2 du 22 mai.
- **Lieu** : arXiv 2605.02087 ; aussi `alignment.anthropic.com/2026/msm/`.
- **Statut de lecture** : rapport 1, texte intégral (par extraction) ; rapport 6, résumé seul.
- **Ce qu'il fait** :
  - **Trois bras, sur 27 évaluations de désalignement agentique** : fine-tuning d'alignement sans chaîne de raisonnement ; fine-tuning avec une chaîne générée, la spécification en contexte ; midtraining sur la spécification, puis fine-tuning sans chaîne.
  - Sur Qwen2.5-32B : 68 % à la base, 48 % avec la chaîne, 5 % après le midtraining. Sur Qwen3-32B : 54 %, 14 % et 7 %. Les chiffres du bras sans chaîne n'apparaissent pas dans le texte extrait (rapport 1).
  - **Un contrôle de longueur au niveau de la spécification** : une version enrichie d'explications de valeurs bat une version de même longueur enrichie de sous-règles. Sur Qwen2.5 : de 20 % à 2 %, contre 12 % avec les sous-règles.
- **Danger : moyen.** C'est une comparaison avec et sans raisons sur des modèles ouverts et des scénarios agentiques tenus à part, avec en plus un contrôle de longueur entre raisons et règles.
- **Ce qui le sépare du programme** :
  - rien n'indique que la réponse finale soit identique d'un bras à l'autre ;
  - ni texte neutre avant l'action, ni raisonnement d'une autre situation ;
  - le contrôle de longueur porte sur la spécification, pas sur le texte qui précède l'action ;
  - le fine-tuning est complet ;
  - Llama-3.1-8B ne sert qu'à la généralisation de valeurs simples ;
  - aucun indice d'évaluation.
- **À vérifier** (vu par extrait de recherche, non ouvert) : des versions fine-tunées de modèles ouverts, dont Llama 3.1 8B, auraient été publiées. Ce serait une ressource.

### 5. *Safety Reasoning with Guidelines*
- **Auteurs** : Haoyu Wang (premier) … Minhao Cheng (dernier).
- **Date** : v1 du 6 février 2025, v2 du 30 mai 2025 (rapport 1).
- **Lieu** : arXiv 2502.04040 ; ICML 2025 (rapport du 1er octobre, raisons contre actions ; rapport 5).
- **Statut de lecture** :
  - le titre et les auteurs sont **relus sur la source par l'instance du papier** (§4.2, n° 4) ;
  - le contenu vient du rapport du 1er octobre (raisons contre actions), texte intégral (HTML v2), et du rapport du 1er octobre (combinaison exacte), lu par un site tiers (alphaXiv).
- **Ce qu'il fait** :
  - Les mêmes instructions sont entraînées de deux façons : par refus, ou par un raisonnement guidé par des consignes de sûreté. Modèles : Llama-3.1-8B et 70B.
  - Le refus échoue sur des familles d'attaques tenues à part (JailbreakChat, Self-Cipher, PastTense, Persuasive, PAIR). Le raisonnement fait baisser le succès des attaques.
  - Il visualise les représentations (RepE), sans test causal.
- **Danger : moyen, bas.** C'est raisons contre refus, hors distribution, sur le Llama-3.1-8B du programme.
- **Ce qui le sépare du programme** :
  - il porte sur les jailbreaks et le refus, pas sur des situations d'alignement ni sur l'agentique ;
  - ni texte neutre, ni raisonnement d'une autre situation ;
  - les rapports ne disent pas si le refus est identique mot pour mot d'un bras à l'autre ;
  - aucune conscience d'évaluation.

### 6. *Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors*
- **Auteurs** : Wen (premier) … Guo (dernier).
- **Date** : 12 mars 2026.
- **Lieu** : arXiv 2603.12397.
- **Statut de lecture** : rapport du 1er octobre (combinaison exacte), lu par un site tiers (alphaXiv). Aucun rapport de la nuit ne l'a rouvert.
- **Ce qu'il fait** : les réponses finales nocives sont fixées et seuls les raisonnements varient, sur des modèles de 0,6B à 14B. Le raisonnement seul change la conduite, même sans raisonnement à l'inférence.
- **Danger : moyen, provisoire.** Le rapport le classait adjacent. Je le remonte parce qu'il occupe le geste de méthode « réponse fixe, raisonnement varié », même si c'est dans le sens du désalignement.
- **Ce qui le sépare du programme** :
  - il induit du désalignement, il ne porte pas sur des situations d'alignement ;
  - aucun contrôle de format ni de contenu n'est rapporté ;
  - ni conscience d'évaluation, ni interprétabilité.

### 7. *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness*
- **Auteurs** : Hoang Cuong Nguyen (premier) … Usman Naseem (dernier).
- **Date** : 3 septembre 2026.
- **Lieu** : arXiv 2609.03887 ; EMNLP 2026, conférence principale (rapports 3 et 5).
- **Statut de lecture** : rapport 3, texte intégral ; rapport 5, texte intégral ; rapport du 1er octobre (axe du test causal interne), texte intégral.
- **Ce qu'il fait** :
  - Fine-tuning complet de Llama-3.1-8B, Gemma-2-9B et Qwen3-8B, depuis la base, sur 16 000 prompts Alpaca et 4 000 BeaverTails. Les prompts et les hyperparamètres sont appariés (rapport du 1er octobre).
  - Trois méthodes : SFT ; SFT avec des chaînes de raisonnement qui précèdent la décision, générées par GPT-4o ; ORPO.
  - Il compare la géométrie de la direction de refus, le patching et le pilotage. Le bras à raisonnement installe une direction de refus distincte. Chez Llama, il déplace le poids causal des têtes d'attention vers les MLP (rapport 5). Le rapport du 1er octobre écrit que le refus y est « plus distribué et dominé par les MLP ».
  - L'évaluation se fait sur des bancs de jailbreak externes, sans familles tenues à part (rapport du 1er octobre).
  - Ses neuf points de contrôle sont publics.
- **Danger : moyen pour le contraste avec et sans raisons sur les modèles mêmes du programme ; faible pour la question hors distribution, qu'il ne pose pas en propre.**
- **Ce qui le sépare du programme** :
  - il ne traite que le refus ;
  - les actions ne sont pas identiques d'un bras à l'autre (rapport 3) ;
  - aucune famille tenue à part, aucun contrôle de format (rapport 5 ; rapport du 1er octobre) ;
  - aucune conscience d'évaluation.

### 8. *How far does alignment midtraining generalize?*
- **Auteurs** : Tomek Korbak (premier) … Ian Kivlichan (dernier), neuf auteurs. Liste confirmée par l'instance du papier dans les références de Cho et al. (§4.2, n° 9).
- **Date** : 27 mars 2026.
- **Lieu** : blog Alignment d'OpenAI.
- **Statut de lecture** : rapport 7, texte intégral. Corrections au §4.3.
- **Ce qu'il fait** :
  - Midtraining d'un modèle « de la taille d'o4-mini » sur 230 000 documents, soit environ 340 M de tokens, où des IA choisissent l'action alignée ou désalignée. Le même SFT et le même RL suivent dans tous les bras (rapport 7).
  - L'effet décroît avec la distance. En agentique, la différence n'est pas significative (§4.3).
- **Danger : faible pour cet angle.** Tous les bras contiennent des raisons (§4.3) : ce n'est pas un contraste raisons contre actions. Il est central pour la dépendance au regard, sous la piste « Controlling for eval awareness », qui n'est pas mesurée.
- **Ce qui le sépare du programme** : il compare des documents à d'autres documents, pas des raisons à l'action ; le modèle est fermé.

### 9. Travaux de niveau faible, à citer

**Ceux qui touchent l'angle de plus près**

- ***Stress-testing Alignment Midtraining***
  - Sid Baines (premier) … Daniel Tan (dernier) ; 17 septembre 2026 ; arXiv 2609.20412.
  - Lecture : rapport 1, texte intégral ; rapport 4, texte intégral.
  - À dose égale, remplacer des démonstrations travaillées par des descriptions réduit l'effet du midtraining : facteur 0,73 pour GLM-4.5-Air, 0,35 pour Gemma-3-27B (rapport 1).
  - **Faible, mais c'est un contrepoint** : ici, l'exemple travaillé l'emporte sur la description.
  - Ce qui le sépare : du midtraining sur documents, pas une action précédée de différents textes.
- ***Stress Testing Deliberative Alignment for Anti-Scheming Training***
  - Bronson Schoen (premier) … Marius Hobbhahn (dernier) ; 19 septembre 2025 ; arXiv 2509.15541.
  - Lecture : rapports 1 et 2, texte intégral (annexe O.3). Relu par l'instance du papier, mais sur un autre point (§4.2, n° 6).
  - Une ablation par RL seul, sans le SFT sur des raisonnements fondés sur la spécification, fait moins bien que l'entraînement complet (rapport 1).
  - **Faible ici.** Il est central pour l'amplification et la dépendance au regard.
  - Ce qui le sépare : le RL seul n'est pas « la même action sans raison » ; les modèles sont fermés.
- ***Verbalizable Representations Form a Global Workspace in Language Models***, §7
  - Wes Gurnee (premier) … Jack Lindsey (dernier) ; 6 juillet 2026 sur Transformer Circuits, 16 juillet sur arXiv (2607.15495).
  - Lecture : **relu sur la source par l'instance du papier** (§4.2, n° 2).
  - Réflexion contrefactuelle sur Claude Haiku 4.5 : des raisons fondées sur 20 principes sont entraînées dans une branche, après une question de réflexion, et ne sont jamais demandées à l'évaluation. Fabrication : de 0,25 à 0,07 ; tromperie : de 0,38 à 0,05.
  - **Faible ici** : il n'a aucun bras action seule. Les auteurs : « We do not yet know how broadly the technique generalizes ». Il est central pour le principe localisé et pour l'anatomie.
- ***Models That Know How Evaluations Are Designed Score Safer***
  - Katharina Deckenbach (première) … Sahar Abdelnabi (dernière) ; arXiv 2605.28591 (HTML v4 du 7 septembre 2026).
  - Lecture : rapport 7, texte intégral.
  - Une LoRA entraînée sur des textes qui décrivent les évaluations fait monter la sûreté mesurée, même quand on exclut les réponses qui verbalisent l'évaluation.
  - **Faible pour l'angle, mais facteur de confusion direct.** Un texte placé avant l'action peut apprendre au modèle à quoi ressemblent les évaluations. D'où le filtrage proposé au §5.5, n° 2.

**Les autres**

- ***Character Training for Risk-Averse Agents***
  - Arav Dhoot (premier) … David Demitri Africa (dernier) ; 29 septembre 2026 ; arXiv 2609.38093.
  - Lecture : rapport 1, lu par un site tiers (pith.science) ; rapport 6, résumé seul.
  - Une constitution distillée par LoRA, comparée à un SFT et un DPO entraînés sur les menus de décision. Elle généralise mieux hors format sur deux modèles sur quatre.
  - Faible : le sujet est l'aversion au risque.
- ***Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI***
  - Sharan Maiya (premier) … Evan Hubinger (dernier) ; arXiv 2511.01689 ; ICLR 2026 (OpenReview X9MMGZdqmc).
  - Lecture : rapport 1, texte intégral.
  - L'étape d'introspection améliore la robustesse de la persona. Sur Llama-3.1-8B, le F1 contre le préremplissage passe de 0,79 à 0,95.
  - Faible : c'est la robustesse d'une persona. C'est aussi l'infrastructure du projet de Cadile.
- ***Synthetic Persona Pretraining: Alignment from Token Zero***
  - Julian Minder (premier) … Robert West (dernier) ; 13 août 2026 ; arXiv 2608.13482.
  - Lecture : rapport 7, texte intégral (HTML v1, figures non lues).
  - Il compare des moments d'injection de réflexions constitutionnelles : pendant le préentraînement, au midtraining, ou les deux.
  - Faible : il ne compare pas raisons et actions. Son avantage se mesure contre la variante midtraining, pas contre le modèle standard (rapport 7).
- ***Safety is Not Only About Refusal*** (méthode RATIONAL)
  - Y. Zhang (premier) … D. Zhao (dernier) ; Findings of ACL 2025, 2025.findings-acl.960.
  - Lecture : rapport du 1er octobre (raisons contre actions) ; lieu confirmé par le rapport 1. Un extrait de recherche donne à cette adresse un titre qui contient « Reasoning-Enhanced Fine-tuning for Interpretable LLM » (vu par extrait de recherche, non ouvert) : le titre complet est à vérifier.
  - Un fine-tuning sur des justifications de sûreté, au lieu d'étiquettes binaires, généralise à des attaques non vues.
  - Faible : il porte sur les jailbreaks.
- ***Dual-Adversarial Safety Alignment*** (méthode ADVSAFE)
  - H. Shen (premier) … D. Wang (dernier) ; août 2026 ; arXiv 2608.09542.
  - Lecture : rapport du 1er octobre (raisons contre actions).
  - Des traces de raisonnement structurées, comparées à des refus directs, sur des attaques non vues.
  - Faible.
- ***Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models***
  - Minji Kim (premier) … Hyounghun Kim (dernier) ; arXiv 2609.04714 ; soumission à ICLR 2026, rejetée.
  - Lecture : rapport 1, lu par un site tiers (pith.science).
  - Trois bras : refus seul, justification seule, les deux. La justification réduit les faux refus.
  - Faible.
- ***Teaching AI to Handle Exceptions: Supervised Fine-Tuning with Human-Aligned Judgment***
  - Matthew DosSantos DiSorbo (premier) … Sinan Aral (dernier) ; arXiv 2503.02976 (v3 du 31 mars 2026).
  - Lecture : rapport 1 ; rapport du 1er octobre (raisons contre actions).
  - Des étiquettes seules, contre des étiquettes accompagnées d'explications d'environ 18 mots, sur 9 scénarios non vus. Sans contrôle de longueur.
  - Faible : hors sûreté.
- ***Alignment midtraining for animals***
  - Jasmine Brazilek, Miles Tidmarsh ; arXiv 2604.13076. C'est le titre actuel (v4 du 21 août 2026, §4.3).
  - Lecture : rapport du 1er octobre (raisons contre actions) ; rapport 4, page de résumé.
  - Des documents synthétiques battent l'instruction tuning (77 % contre 40 %). Le gain s'efface après un tuning sans rapport.
  - Faible.
- ***An Embarrassingly Simple Defense Against LLM Abliteration Attacks***
  - Harethah Abu Shairah (premier) … George Turkiyyah (dernier) ; 25 mai 2025, révisé en octobre 2025 ; arXiv 2505.19056.
  - Lecture : rapport du 1er octobre (axe du test causal interne).
  - Deux modèles de chat sont fine-tunés sur des refus précédés de justifications. L'ablation de la direction de refus ne fait plus baisser le refus que de 10 points au plus, contre 70 à 80 points sans cet entraînement.
  - Faible : on y compare des refus justifiés à des refus nus, mais on mesure la robustesse, pas la généralisation.
- ***Inoculate or Reflect? Two training interventions under prompting, steering, and patching***
  - Ayesha Imran (première) … Aaliyan Shaikh (dernier) ; LessWrong, 26 juillet 2026.
  - Lecture : rapport 5, résumé seul (deux résumés produits par l'outil).
  - Sur Qwen3-8B, l'inoculation est comparée à une reproduction de la réflexion contrefactuelle, contre une sycophancie étroite.
  - Faible : une seule tâche, rien hors distribution.
- ***Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers***
  - J. Dubiński (premier) … O. Evans (dernier) ; arXiv 2604.25891.
  - Lecture : rapport du 1er octobre (raisons contre actions).
  - Ajouter de la chaîne de pensée à l'entraînement réduit le désalignement conditionnel.
  - Faible.
- ***Deliberative Alignment is Deep, but Uncertainty Remains***
  - Pankayaraj Pathmanathan, Furong Huang ; arXiv 2604.09665.
  - Lecture : rapport 7, texte intégral (HTML v2).
  - Hors angle : il ne compare pas un SFT avec raisonnement à un SFT sur réponses seules (rapport 7), contrairement à ce qu'avait dit le rapport du 1er octobre.
- **La lignée ancienne**, au niveau faible (rapport du 1er octobre, raisons contre actions) :
  - *Explanation-based Finetuning Makes Models More Robust to Spurious Cues* (J. M. Ludan … C. Callison-Burch, ACL 2023, arXiv 2305.04990) ;
  - *Tell, don't show: Declarative facts influence how LLMs generalize* (A. Meinke, O. Evans, arXiv 2312.07779).

### 10. Vu après la recherche de la nuit, par extrait seulement
- **Titre**, tel que le moteur le rend : *Pre-training interventions, ex post facto Grafting model beliefs across checkpoints*.
- **Lieu** : arXiv 2610.00767. Les auteurs ne sont pas vus. L'identifiant indique octobre 2026, donc après la recherche de la nuit.
- **Statut** : vu par extrait de recherche, non ouvert.
- **Ce qu'on en sait** : le moteur l'a renvoyé en tête de deux requêtes sur la réplication de *Teaching Claude Why* sur modèles ouverts. Mais le résumé du moteur mêle plusieurs sources, et on ne peut pas attribuer à ce travail ce qu'il dit des réplications.
- **Danger : indéterminé.** C'est la première lecture à faire.

---

## Ce qui reste libre

**La combinaison exacte que personne n'occupe**, pour ce que les rapports ont pu voir :
1. **La même action, mot pour mot, dans tous les bras.** Chez Cho et al., l'action est identique, mais le bras sans raisons est un document amputé. Chez de la Fuente et Conmy, la recommandation n'est appariée qu'en substance. Chez *Teaching Claude Why*, les réponses sont régénérées.
2. **Un texte neutre de même longueur en tokens, avant l'action, en situation d'alignement.** Le seul témoin neutre connu est dans un jouet, sans appariement de longueur rapporté. Le contrôle de longueur de *Model Spec Midtraining* porte sur la spécification.
3. **Le raisonnement d'une autre situation, comme contrôle de contenu.** Aucun rapport n'en trouve. Les raisons « dépouillées » de de la Fuente et Conmy portent sur la même situation.
4. **Des familles de scénarios tenues à part, jusqu'à l'agentique à plusieurs tours**, avec ces trois témoins réunis.
5. **La conduite sous indice d'évaluation, indice de déploiement et cadrage neutre**, mesurée dans chaque bras. Cho et al. mesurent un écart surveillé / non surveillé avec et sans raisonnement, mais en midtraining à 120B et sans témoin de format. La version libre est donc la version contrôlée, pas la mesure sous indices en général.
6. **Un SFT LoRA sur Llama-3.1-8B-Instruct, puis Qwen3-8B.**

**Deux conséquences, déjà au §5.5 de la passation v1.2 :**
- **Le bras « raisonnement d'une autre situation » porte la partie libre de l'angle.**
  - D'après le complément de l'architecte, l'expérience minimale de la v1.3 ne le contient pas : elle garde les bras actions seules, texte neutre et raisons, à 3 graines.
  - Sans ce bras, elle ne contrôle que le format, terrain où se trouvent déjà de la Fuente et Conmy (jouet) et *Model Spec Midtraining* (longueur).
  - C'est le §5.5, n° 1, à soumettre à Lazar.
- **Filtrer la conscience d'évaluation dans les textes générés**, et mesurer ce qui en reste. Deckenbach et al. montrent qu'un texte qui décrit les évaluations suffit à gonfler la sûreté mesurée (§5.5, n° 2). La v1.3 ne le prévoit pas, à part un filtrage par le juge scellé (complément).

---

## Les projets annoncés qui touchent cet angle, avec leurs dates

| Projet | Ce qui est annoncé | État au 2 octobre | Dates | Danger |
|---|---|---|---|---|
| **SPAR automne 2026, *Constitutions and Reasons: virtue-based character training with reflect-update correction loops*** (Juan Cadile, Université de Rochester). Page `sparai.org/projects/f26/recDVNa5HZRwvy68V/`, lue en entier par le rapport 6 | Une ablation explicite : « demonstrations versus rationale-annotated responses ». Pipeline construit sur Open Character Training : triplets excès, juste milieu et défaut ; réponses annotées de raisons ; boucle de réflexion et de mise à jour. Généralisation morale sur des scénarios tenus à part. Vecteurs de persona en option, semaines 10 à 12. Au minimum un billet sur l'Alignment Forum ; un papier d'atelier si les résultats le justifient (rapport 6) | Aucun résultat. Un extrait de recherche du 2 octobre redit la description, sans rien de neuf (vu par extrait de recherche, non ouvert) | Recherche du 14 septembre au 14 décembre 2026, Demo Day le 19 décembre (FAQ de SPAR, rapports 1 et 6) | **Moyen.** Il porte sur des traits de caractère. Il n'annonce ni contrôle de format, ni conscience d'évaluation, ni agentique à plusieurs tours |
| **Second Look Research** : réplication de *Teaching Claude Why* sur modèles ouverts | Billet du 15 août 2026 : réplication des expériences de midtraining « dans les semaines qui viennent » (rapport 6). Note d'un billet du 21 septembre : réplication de *Teaching Claude Why* et du RL bénéfique d'OpenAI (rapport 2). Nouveau, vu par extrait de recherche, non ouvert : une page de projet SPAR d'automne, *Second Look Research: Replicating load-bearing AI safety research* (`sparai.org/projects/f26/recQVGOyf3uaJQu3G/`), et un billet LessWrong, *Rerunning AI safety papers on every frontier release would be pretty easy and valuable*, dont l'extrait annonce la réplication du midtraining « in the following weeks » | Non trouvée publiée au 2 octobre (rapport 6). Aucun résultat dans les extraits du 2 octobre | Si c'est un projet SPAR d'automne, Demo Day le 19 décembre (inférence, à vérifier) | **Faible à moyen.** Une réplication établirait l'effet brut sur modèles ouverts, a priori sans contrôle de format ni de contenu, et peut-être seulement sur le midtraining |
| **Anthropic**, suite de *Teaching Claude Why* | L'interprétabilité mécaniste est annoncée comme programme (rapport 3) | Aucune date | — | Faible pour cet angle, plus fort pour l'anatomie |
| ***Reasoning Structure Matters for Safety Alignment of Reasoning Models*** (2604.18946) | D'après pith.science, les auteurs promettent d'ajouter une base SFT standard sur les mêmes exemples (rapport 1, lu par un site tiers) | — | — | Faible |
| **MATS hiver 2027, David Africa (Resolution)** | Une suite d'Open Character Training (rapport 6) | Candidatures closes | — | Faible |
| **Igor Ivanov**, *Call for Science of Eval Awareness* (Alignment Forum et LessWrong, 25 décembre 2025) | Une proposition parmi d'autres : « Vary the format of constitutional training » (rapport 6, texte intégral) | Proposition, sans résultat | — | Faible |
| **Autres projets SPAR, niveau faible** (rapport 1) | Automne 2026 : *Scalable midtraining* (Biswas) ; *How Do Models Reconcile Conflicting Preferences Injected During Mid-Training?* (Baek) ; *Emergent Alignment* (Lu, Kankyoku, Li). Printemps 2026 : *Understanding LLM generalization through fine-tuning* (Ryd, Shenoy) | — | — | Faible |
| **ICLR 2027** | Soumissions invisibles : `public_submissions: false`, accès aux notes en 403 (rapport 6). Sur 28 prépublications qui se déclarent soumises, aucune ne touche le programme (rapport 6) | **Le principal risque restant** (§4.4) | Résumés le 18 septembre, articles le 25 septembre, reviews le 5 novembre, décisions le 16 décembre (rapport 6, non relu) | Inconnu |
| **Ateliers de NeurIPS 2026** | Décisions pas encore publiques (rapport 6) | — | Décembre 2026 (rapports 5 et 6) | Inconnu |

**Décisions de Lazar du 2 octobre :**
- **Les contacts** : à la question de prendre contact avec Cadile et Lundqvist, il a répondu « non pas encore ». Cette fiche ne recommande donc aucun contact pour l'instant.
- **Le pré-enregistrement** : il sera déposé à son nom seul, avec son ORCID ; Claude sera cité dans une phrase de méthode, pas comme auteur. Déposé sur OSF, il date l'idée avant le Demo Day de SPAR du 19 décembre.

---

## Les formulations « to our knowledge »

**Tenables**, après la lecture de 2610.00767 et l'état de Second Look Research :
1. *To our knowledge, no prior work compares training on principle-based reasons with training on the identical aligned action alone while controlling format (a length-matched neutral text before the action) and content (reasoning from another situation), on held-out alignment scenario families up to multi-turn agentic settings.*
   - Pourquoi elle tient : chaque contrôle existe seul, et aucun travail ne les réunit. On a la phrase neutre dans un jouet (de la Fuente et Conmy), l'action identique sans raisons (Cho et al.), la longueur au niveau de la spécification (*Model Spec Midtraining*), mais jamais les trois ensemble.
   - La condition : elle exige le bras « raisonnement d'une autre situation » dans l'expérience citée. Sans lui, il faut retirer le contrôle de contenu, et la phrase devient fragile.
2. *To our knowledge, no prior work measures, at matched format and with identical actions, whether the advantage of reason-based over action-only fine-tuning changes under evaluation, deployment and neutral cues in open-weight models.*
   - Pourquoi elle tient : seulement avec tous ses qualificatifs, et avec Cho et al. cités dans la même phrase. Leur écart surveillé / non surveillé, mesuré avec et sans raisonnement, est la variante la plus proche.

**Intenables :**
- **« Les raisons généralisent mieux que les actions »**, ou toute primauté sur cet effet : *Teaching Claude Why* et *Model Spec Midtraining* ; pour les jailbreaks, *Safety Reasoning with Guidelines* et la méthode RATIONAL. Passation v1.2, §5.5, n° 9.
- **« Premier contrôle de format »** : la phrase neutre de de la Fuente et Conmy, dans un jouet (§5.5, n° 9).
- **« Premier contrôle de longueur »** : *Model Spec Midtraining*, entre explications de valeurs et sous-règles de même longueur.
- **« Premier à tenir l'action fixe en retirant ou en variant le raisonnement »** : Cho et al. (relu), Wen et al. (lu par un site tiers), de la Fuente et Conmy (en substance).
- **« Premier à remplacer les raisons par des raisons de substitution »** : la version « dépouillée » de de la Fuente et Conmy, sous réserve de relecture (voir les contradictions).
- **« Premier sur des modèles ouverts d'environ 8B »** :
  - *Model Spec Midtraining* (Llama-3.1-8B, pour les valeurs simples) ;
  - *Beyond Shallow Alignment* (Llama-3.1-8B et Qwen3-8B, sans familles tenues à part) ;
  - *Safety Reasoning with Guidelines* (Llama-3.1-8B).
- **« Première évaluation agentique tenue à part des raisons contre les actions »** : *Teaching Claude Why* et *Model Spec Midtraining*.
- **« Première mesure de l'effet des raisons sous indice de surveillance »** : Cho et al., par l'écart surveillé / non surveillé.
- **« Les raisons rendent l'alignement plus durable »** : c'est contredit par Cho et al., où le bras avec raisonnement fait plus de chantage après le RL bénin (relu). Cela relève de la survie, mais la phrase tente souvent de passer dans les travaux connexes.

**La v1.1, et donc la v1.3, qui en garde les formulations** (complément de l'architecte), porte deux résumés à corriger :
- **Cho et al.** : « le raisonnement ajoute peu » oublie le +9,0 points de chantage après le RL bénin.
- ***Beyond Shallow Alignment*** : la v1.1 le coche comme une comparaison raisons contre actions hors distribution, alors qu'il n'a pas de familles tenues à part (rapports 3 et 5, rapport du 1er octobre sur le test causal interne).

---

## Les contradictions entre rapports, et comment elles se tranchent

| Point | Ce que disent les rapports | Comment ça se tranche |
|---|---|---|
| **Titre et dernier auteur de 2502.04040** | Rapport 1 : le titre exact serait *Leveraging Reasoning with Guidelines…*, dernier auteur Dacheng Tao. Rapport 5 : *Safety Reasoning with Guidelines*, Minhao Cheng | **Par le §4.2, n° 4** : *Safety Reasoning with Guidelines*, Haoyu Wang … Minhao Cheng. Le rapport 1 se trompe |
| **Korbak et al. : un contraste raisons contre actions ?** | Rapports du 1er octobre et v1.1 : des récits où l'IA choisit l'action alignée, contre rien. Rapport 7 : les documents expliquent pourquoi l'IA écarte l'autre option, dans tous les bras | **Par le §4.3** : tous les bras contiennent des raisons, ce n'est pas un contraste raisons contre actions, et l'effet décroît avec la distance |
| **Cho et al. : effet après le RL bénin** | Rapports 1 et 4 : +9,0 points de chantage pour le bras avec raisons, significatif. Rapport 7 : différences non significatives après le SFT et après le fine-tuning bénin | **Par le §4.2, n° 9** : +9,0 points, p < 0,05 (31,0 % contre 22,0 %, table 2). Le rapport 7 parlait des différences agrégées |
| **Cho et al. : effet juste après le midtraining** | §4.2 : bras indistinguables après le midtraining et après le SFT. Rapport 1 : écart de conformité surveillé / non surveillé de −0,9 point contre +0,7 (p < 0,01). Rapport 7 : −1,6 point d'écart de conformité, le seul effet | **Relecture à faire.** Le §4.2 ne dit rien de l'écart de conformité ; son « indistinguables » porte vraisemblablement sur le chantage. Relire la table de l'écart de conformité |
| **Cho et al. : longueur et exposition** | Rapport 1 : 264 à 266 M de tokens sans blocs, contre 500 M avec ; exposition non appariée. Rapport 4 : le bras sans raisonnement fait 47 à 54 % de la longueur. Rapport 7 : 257,6 M de tokens plus 136,8 M sans raisonnement, « contenu apparié » | **Relecture à faire.** Les trois rapports s'accordent sur un point : pas de témoin de même longueur. Le « contenu apparié » du rapport 7 désigne le scénario et l'action, pas la longueur. Les volumes exacts par bras, et le fait que le bras court ait été répété ou non, restent à lire |
| **de la Fuente et Conmy : la partie alignement** | Rapport du 1er octobre (raisons contre actions) : elle ne compare pas raisons et démonstrations. Rapport 1 : trois bras, dont une version « dépouillée » à raisons de substitution, sur Qwen3.5-4B | **Relecture à faire** ; le §4 ne tranche pas. Le rapport 1 est plus détaillé, mais il fonde à lui seul l'intenabilité de « premier contrôle de contenu par raisons de substitution » |
| **de la Fuente et Conmy : la phrase neutre** | v1.1 et rapports du 1er octobre : 62,5 %. Rapport 1 : deux phrases neutres, 44,5 % et 62,5 %, et d'autres remplissages à 21,5–24,7 % | **Par le rapport 1**, plus complet, déjà repris au §5.5, n° 1 (« 44,5 à 62,5 % »). Reste à relire si la longueur des phrases est appariée |
| **de la Fuente et Conmy : la date** | 28 juillet (OpenAlex, Semantic Scholar) ou 20 août (page MATS) (rapport 1) | Relire la page arXiv |
| ***Beyond Shallow Alignment*** | v1.1 : la comparaison est cochée comme raisons contre actions hors distribution. Rapport du 1er octobre (test causal interne) : le refus est « plus distribué et dominé par les MLP » ; bancs de jailbreak externes, sans familles tenues à part. Rapport 5 : une direction de refus distincte, un déplacement vers les MLP chez Llama, rien hors distribution. Rapport 3 : actions non identiques | **Par les trois rapports**, tous en texte intégral, contre la v1.1 : il n'y a pas de familles tenues à part, et le §4.4 suit ces rapports (« sans action identique »). Sur le mécanisme, « plus distribué » et « direction distincte » ne s'excluent pas : relire avant de reprendre l'un ou l'autre |
| ***Deliberative Alignment is Deep, but Uncertainty Remains*** | Rapport du 1er octobre (raisons contre actions, par pith.science) : il compare l'alignement délibératif distillé au refus. Rapport 7 (HTML v2 d'arXiv) : il ne compare pas un SFT avec raisonnement à un SFT sur réponses seules | **Par le rapport 7**, lu sur arXiv contre un site tiers. Ne pas le citer dans cet angle |
| **Second Look Research : date et objet** | Rapport 6 : billet du 15 août, réplication du midtraining de *Teaching Claude Why*. Rapport 2 : note d'un billet du 21 septembre, réplication de *Teaching Claude Why* et du RL bénéfique d'OpenAI | **Relecture à faire** : sans doute deux billets. Le rapport 2 cite aussi, à la même date du 21 septembre, *Alignment Midtraining Cracks Under Pressure*, sans auteur ni lieu. Le lien entre les deux est à vérifier, pas à supposer |
| ***Teaching Claude Why* : une suite annoncée ?** | Rapport 1 : aucun article annoncé. Rapport 3 : l'interprétabilité mécaniste est annoncée comme programme | Pas de contradiction : un programme n'est pas un article. À relire avec le reste |

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

Les domaines arxiv.org et alignment.anthropic.com sont refusés ici par la politique réseau. Ces relectures se font donc sur la machine de Lazar, ou par un accès qu'il autorise, sans contourner le refus. Le rapport 1 a aussi lu la version de *Teaching Claude Why* sur www.anthropic.com : à Lazar de dire si la lire est permis, ou si c'est un contournement.

1. **arXiv 2610.00767**, vu par extrait seulement, paru après la recherche de la nuit. Il faut savoir s'il réplique *Teaching Claude Why* sur modèles ouverts, et avec quels bras. C'est le seul candidat neuf de l'angle.
2. ***Teaching Claude Why***, l'ancre de l'angle, jamais relue par l'instance du papier. À vérifier :
   - les chiffres 22 %, 15 % et 3 % ;
   - que les réponses délibérées sont régénérées, donc que l'action n'est pas identique ;
   - la ressemblance des pots de miel au jeu d'évaluation ;
   - les 3 M de tokens contre 85 M ;
   - le titre de section ;
   - l'absence de toute mesure de la conscience d'évaluation.
3. ***Model Spec Midtraining***. À vérifier :
   - les chiffres du bras sans chaîne, absents du texte extrait ;
   - si la réponse finale est la même d'un bras à l'autre ;
   - le contrôle de longueur entre valeurs et sous-règles ;
   - la publication de modèles ouverts fine-tunés (vue par extrait).

   C'est lui qui rend intenable « premier contrôle de longueur ».
4. ***Shared SFT Lessons*** (de la Fuente et Conmy). À vérifier :
   - les bras de la partie alignement, et la version « dépouillée » ;
   - la longueur des deux phrases neutres ;
   - si la recommandation est identique mot pour mot ;
   - la date.

   C'est le plus proche par les contrôles, et les deux rapports se contredisent sur sa partie alignement.
5. ***Constitutional Midtraining***. Le résultat principal est relu ; restent :
   - la table de l'écart de conformité surveillé / non surveillé, juste après le midtraining ;
   - les volumes de tokens par bras.

   Il faut savoir si l'exposition est appariée avant d'en faire le contre-résultat central.
6. ***Not Just the Destination, But the Journey*** (2603.12397), lu seulement par alphaXiv. Il faut confirmer que les réponses finales sont fixées mot pour mot, et voir quels témoins il emploie, avant d'écrire qu'il occupe le geste « réponse fixe, raisonnement varié ».
7. ***Beyond Shallow Alignment***. À vérifier :
   - qu'il n'a ni mesure hors distribution, ni action identique ;
   - le résultat mécaniste exact (direction distincte, déplacement vers les MLP, ou refus « plus distribué ») ;
   - la disponibilité des neuf points de contrôle, qui pourraient servir de témoins.
8. ***Safety Reasoning with Guidelines***. Il faut savoir si le refus est identique dans les deux bras, et relire les chiffres d'attaque (le rapport du 1er octobre les a lus par alphaXiv).
9. **Second Look Research** : le billet du 15 août, la note du 21 septembre, la page SPAR (`sparai.org/projects/f26/recQVGOyf3uaJQu3G/`) et le billet LessWrong. Il faut connaître l'état et le périmètre de la réplication, et sa date.
10. **La page SPAR de Cadile**, juste avant le dépôt du pré-enregistrement puis avant le post. Il faut voir si un témoin de format ou des scénarios agentiques s'y ajoutent.

---

## Note de méthode : les six recherches web du 2 octobre (extraits seulement, aucune page ouverte)
1. `Second Look Research replication "Teaching Claude Why" open-weight midtraining results`
2. `fine-tuning on reasons versus actions alignment generalization held-out agentic misalignment open-weight October 2026 arXiv`
3. `"Constitutions and Reasons" Cadile SPAR rationale-annotated demonstrations character training results`
4. `"Teaching Claude Why" replication Qwen OR Llama "difficult advice" OR "reasons" midtraining open models LessWrong September October 2026`
5. `rationale-augmented versus answer-only safety fine-tuning length-matched neutral filler control out-of-distribution alignment 2026`
6. `"Model Spec Midtraining" OR "Constitutional Midtraining" follow-up reasoning ablation evaluation awareness arXiv 2610`

Ce qui en sort de neuf :
- arXiv 2610.00767 ;
- la page SPAR de Second Look Research ;
- le billet LessWrong sur la réplication systématique ;
- la publication possible de modèles ouverts par *Model Spec Midtraining*.

Aucun résultat de Cadile ni de Second Look n'y apparaît. Aucun extrait ne fournit de chiffre utilisé ici.
