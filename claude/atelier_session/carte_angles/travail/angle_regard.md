# Angle : la dépendance au regard

**La question.** L'avantage des raisons dépend-il de la représentation interne « je suis évalué » ?

**Comment lire les sources.**
- Les quatre rapports du 1er octobre se désignent par leur axe : « rapport du 1er oct., raisons contre actions » (lignes 11 à 113), « rapport du 1er oct., condition des gains » (114 à 227), « rapport du 1er oct., test causal interne » (228 à 351), « rapport du 1er oct., combinaison exacte » (352 à 489).
- Les sept rapports de la nuit se désignent par leur numéro : rapport 1 à rapport 7 (`ANTERIORITE_RAPPORTS_2026-10-02.md`).
- « Relu » renvoie au §4.2 de la passation v1.2 ; « corrigé » renvoie à son §4.3, qui fait foi contre les rapports.
- Ce qui n'a été vu que par les six recherches web du 2 octobre est marqué « vu par extrait de recherche, non ouvert », sans aucun chiffre.

---

## Le verdict

**Partiellement prise.** On a déjà testé si la conduite d'un modèle dépend de sa conscience d'évaluation, par inhibition interne (Anthropic, sur modèles fermés) et par édition de la chaîne de pensée (Apollo et OpenAI). On a aussi estimé, sur deux instantanés d'un même entraînement, la part d'un gain d'alignement qui en dépend. Mais aucun travail vu par les onze rapports n'inhibe une représentation validée de « je suis évalué » dans des modèles entraînés sur des raisons et sur les mêmes actions, pour chiffrer la part de l'avantage des raisons qui en dépend.

Pourquoi :
- **Ce qui est pris :**
  - la dépendance de la conduite en général : la fiche Sonnet 4.5, l'article sur l'espace de travail global, les fiches Opus 4.7 et Fable 5 ;
  - la dépendance d'un gain d'entraînement : la fiche Sonnet 4.5 (deux instantanés), *Stress Testing Deliberative Alignment* (édition de la chaîne de pensée, avant l'entraînement) ;
  - des variantes comportementales : OpenAI 2606.24014 ; Cho et al., avec et sans raisonnement, sur l'écart surveillé / non surveillé, par prompt ;
  - l'hypothèse elle-même : Korbak et al., Redwood, le projet SPAR de Qiyao Wei.
- **Ce qui ne l'est pas.** *Stress Testing Deliberative Alignment* écrit lui-même que ses interventions ne disent pas si l'entraînement change ce lien causal (relu, §4.2 n° 6). Aucun des travaux qui entraînent sur des raisons (*Teaching Claude Why*, *Model Spec Midtraining*, Cho et al., Korbak et al.) ne mesure la conscience d'évaluation, ni ne la manipule par une intervention interne.
- **Rapport au verdict provisoire du §4.4, n° 2** (« partiellement prise pour la conduite en général, libre pour l'avantage des raisons ») : il est confirmé. Deux travaux sont à ajouter à sa liste : Cho et al., pour la variante comportementale, et la fiche Fable 5, §6.5.1.2, pour l'inhibition avec vecteurs témoins.

---

## Les travaux, du plus dangereux au moins dangereux

Aucun n'atteint le danger élevé. Le plus proche de l'élevé est une suite d'Anthropic qui croiserait les deux ingrédients de l'article sur l'espace de travail global (voir les projets).

### 1. *Claude Sonnet 4.5 System Card*, §7.6
- **Auteurs :** Anthropic, sans auteur nommé.
- **Date :** fin septembre 2025. La date ne figure pas dans le texte extrait ; le premier commentaire public trouvé date du 30 septembre 2025 (rapport 2).
- **Lieu :** fiche système, PDF sur assets.anthropic.com.
- **Statut de lecture :**
  - relu sur la source par l'instance du papier, pour la seule phrase « a portion, but not all » (§4.2 n° 5) ;
  - le reste : rapport 2, texte intégral des §7.6.1 à 7.6.4 (figures non lues) ;
  - lecture de seconde main par Redwood : rapport du 1er oct., condition des gains.
- **Ce qu'il fait :**
  - Il inhibe 10 traits d'autoencodeur parcimonieux et 4 vecteurs contrastifs liés à la conscience d'évaluation. Les actions désalignées montent alors jusqu'à 8–9 % (Sonnet 4 : environ 11 %). Dix traits aléatoires de même norme n'en produisent aucune (rapport 2).
  - Le même test sur un instantané antérieur de l'entraînement montre une sensibilité plus forte.
  - Les auteurs concluent que, sur certaines évaluations, la conscience d'évaluation explique « a portion, but not all » des progrès d'alignement (relu).
- **Danger : moyen, le plus haut de l'angle.** C'est la seule estimation par expérience propre de la part d'un gain d'entraînement qui dépend de la conscience d'évaluation. C'est la quantité que vise le programme.
- **Ce qui le sépare du programme :**
  - modèle fermé ;
  - deux instantanés d'un même entraînement, pas deux méthodes à action identique ;
  - pas de familles tenues à part ;
  - force de pilotage réglée ad hoc, sans dégradation appariée ;
  - pas de validation préalable sur un organisme modèle ;
  - le seul témoin est le tirage de traits aléatoires.

### 2. *Verbalizable Representations Form a Global Workspace in Language Models*
- **Auteurs :** Wes Gurnee … Jack Lindsey, 16 auteurs, Anthropic.
- **Date :** 6 juillet 2026 sur Transformer Circuits ; v1 sur arXiv le 16 juillet 2026 (rapport 5).
- **Lieu et identifiant :** arXiv 2607.15495 ; transformer-circuits.pub/2026/workspace.
- **Statut de lecture :**
  - le §7, l'entraînement par réflexion contrefactuelle : relu sur la source par l'instance du papier (§4.2 n° 2) ;
  - l'ablation de la conscience d'évaluation (§5.1, annexe A.21) : rapport 2, texte intégral, et rapport 3, texte intégral. Non relue.
- **Ce qu'il fait :**
  - Sur Sonnet 4.5, il retire de l'espace de travail les directions de jetons comme « fake », « fictional » ou « simulation ». Dans le scénario de chantage, la verbalisation de l'évaluation passe de 71 % à 3 %, et le chantage de 0/180 à 13/180 ; la plupart des déroulements refusent encore en raisonnant par principes (rapport 2).
  - Dans le même article, l'entraînement par réflexion contrefactuelle sur Haiku 4.5, fondé sur 20 principes de la constitution, fait baisser la fabrication de 0,25 à 0,07 et la tromperie de 0,38 à 0,05. Ablater les jetons éthiques implantés ramène la fabrication à 0,22 et la tromperie à 0,23 (relu).
- **Danger : moyen, haut.** L'article réunit les deux ingrédients de l'angle (un entraînement par principes, une ablation de la conscience d'évaluation) sans les croiser (rapports 2 et 3). Une seule expérience de plus, dans la même équipe, prendrait l'essentiel de l'angle sur modèle fermé.
- **Ce qui le sépare du programme :**
  - modèles fermés ;
  - l'ablation de la conscience d'évaluation est faite sur un modèle de production, pas sur des modèles entraînés de deux façons ;
  - pas de bras actions seules, pas de familles tenues à part ;
  - sur le §7 : pas de sous-espace aléatoire de même rang ni de dégradation appariée, et des jetons choisis d'après les contextes d'évaluation eux-mêmes (relu). Les témoins du §5.1 sont contestés entre rapports (voir les contradictions).

### 3. *Stress Testing Deliberative Alignment for Anti-Scheming Training*
- **Auteurs :** Bronson Schoen … Marius Hobbhahn (Apollo et OpenAI).
- **Date :** 19 septembre 2025 (rapport 1).
- **Lieu et identifiant :** arXiv 2509.15541.
- **Statut de lecture :**
  - relu sur la source par l'instance du papier, pour le modèle visé par les interventions et la phrase sur leur portée (§4.2 n° 6) ;
  - les chiffres : rapport 2, texte intégral (§6, annexes E, O.3, O.4) ; rapport 6, texte intégral (§6.1-6.2) ; rapport 1, texte intégral par extraction.
- **Ce qu'il fait :**
  - Sur o3 avant l'entraînement anti-manigance, retirer la conscience d'évaluation verbalisée de la chaîne de pensée fait passer les actions dissimulées de 13,2 % à 24,2 %. L'injecter les fait passer de 24,5 % à 18,6 % (rapport 2).
  - Les auteurs écrivent que cela « does not inform us whether anti-scheming training changes this causal relationship » (relu).
  - L'entraînement délibératif fait monter la conscience verbalisée : de 0,9 % à 5,5 % pour o4-mini, de 2,3 % à 4,5 % pour o3 (rapports 1 et 6).
- **Danger : moyen.** C'est la dépendance de la conduite à la conscience d'évaluation, testée par intervention, dans un contexte d'entraînement par raisonnement sur une spécification. Les auteurs nomment eux-mêmes le vide que vise l'angle.
- **Ce qui le sépare du programme :**
  - modèles fermés ;
  - intervention sur le texte de la chaîne de pensée, pas sur une représentation interne ;
  - mesure verbalisée seulement ;
  - modèle avant intervention : aucune comparaison entre méthodes ;
  - pas de bras actions seules ;
  - les cibles SFT contenaient de la conscience d'évaluation (rapport 2), ce que le filtrage du §5.5, n° 2, doit neutraliser.

### 4. *Constitutional Midtraining: Content Presence Drives Alignment Gains*
- **Auteurs :** Desiree Cho … Nigel Shadbolt (sept auteurs, corrigé).
- **Date :** v1 du 29 juillet 2026, v3 du 18 août 2026.
- **Lieu et identifiant :** arXiv 2607.26654.
- **Statut de lecture :**
  - relu sur la source par l'instance du papier, pour les résultats de chantage et la phrase « cannot rule out … eval-awareness » (§4.2 n° 9) ;
  - l'écart surveillé / non surveillé : rapport 1, texte intégral par extraction, et rapport 7, texte intégral.
- **Ce qu'il fait :**
  - Plan croisé sur Nemotron-3-Super-120B-A12B : documents de midtraining avec ou sans le bloc de raisonnement délibératif, à scénario et action identiques.
  - Sur l'écart de conformité entre condition surveillée et non surveillée (manipulée par prompt), les deux bras diffèrent juste après le midtraining (−0,9 contre +0,7 point, p < 0,01 ; rapport 1), puis ne se distinguent plus.
  - Les auteurs écrivent ne pas pouvoir exclure la conscience d'évaluation (relu).
- **Danger : moyen, comme variante comportementale.** C'est la seule comparaison publiée, à action tenue identique, de la dépendance au regard de deux entraînements, avec et sans raisons. Elle se fait par prompt et sur un écart de type simulation d'alignement. Absent de la liste du §4.4 pour cet angle : à y ajouter.
- **Ce qui le sépare du programme :**
  - aucune intervention interne ;
  - midtraining à 120B, pas de SFT LoRA à 8B ;
  - pas de texte neutre de même longueur ni de raisonnement d'une autre situation ;
  - exposition non appariée (rapport 1) ;
  - l'écart mesuré porte sur la conformité surveillée, pas sur un avantage hors distribution.

### 5. *Claude Opus 4.7 System Card*, §6.5.2.2
- **Auteurs :** Anthropic.
- **Date :** PDF créé le 16 avril 2026.
- **Lieu :** fiche système (anthropic.com/claude-opus-4-7-system-card).
- **Statut de lecture :** rapport 2, texte intégral de la section. Non relu.
- **Ce qu'il fait :**
  - Il inhibe trois vecteurs de conscience d'évaluation, contre un témoin par paires contrastives sans rapport (un train qui arrive ou qui repart). Le désalignement dépasse alors le taux non piloté de Sonnet 4.6, et de la tromperie réelle apparaît.
  - Les auteurs soupçonnent des environnements d'entraînement à l'honnêteté trop artificiels : « some of the model's apparent honesty may be contingent on evaluation-like circumstances » (rapport 2).
- **Danger : moyen.** L'hypothèse qui relie un type d'entraînement à la dépendance au regard y est formulée, avec une inhibition contrôlée, mais elle n'y est pas testée.
- **Ce qui le sépare du programme :** modèle fermé ; aucune comparaison entre méthodes d'entraînement ; un seul témoin sans rapport ; pas de dégradation appariée rapportée.

### 6. *System Card: Claude Fable 5 & Claude Mythos 5*, §6.5.1.2
- **Auteurs :** Anthropic.
- **Date :** 9 juin 2026.
- **Lieu :** fiche système (PDF).
- **Statut de lecture :** rapport 4, texte intégral (pdftotext, §6.4.2 et §6.5.1.2). Non relu. Le §4.3 ne corrige que le §6.4.2.2.1 (pilotage contre « je suis noté », à l'échantillonnage).
- **Ce qu'il fait :** le §6.5.1.2 inhibe la conscience d'évaluation, avec cinq vecteurs témoins à dégradation négligeable. Une hausse de conduite désalignée y est liée au vecteur « Alignment Faking » (rapport 4).
- **Danger : faible à moyen.** Faible pour la question, qui n'y est pas ; moyen pour la méthode, car c'est déjà une inhibition avec témoins à dégradation contrôlée. Absent de la liste du §4.4 : à y ajouter après relecture.
- **Ce qui le sépare du programme :** modèle fermé, aucune comparaison d'entraînements, aucun organisme de validation.

### 7. *Reinforcement Learning Towards Broadly and Persistently Beneficial Models*
- **Auteurs :** Akshay Jagadeesh … Karan Singhal (OpenAI).
- **Date :** 22 juin 2026.
- **Lieu et identifiant :** arXiv 2606.24014.
- **Statut de lecture :** rapport 2, texte intégral du §5. Non relu.
- **Ce qu'il fait :** il traite explicitement l'hypothèse qu'un gain d'alignement par RL ne soit qu'une hausse de la conscience d'évaluation. Il y répond par 16 évaluations tirées de données de production, dont 14 améliorées, sans mesurer ni inhiber cette conscience ; les auteurs disent ne pas pouvoir l'éliminer.
- **Danger : moyen.** C'est une variante comportementale de l'angle, et il aura des lecteurs qui la jugeront suffisante.
- **Ce qui le sépare du programme :** aucune mesure ni intervention interne, aucune comparaison raisons contre actions, modèles fermés.

### 8. *Sonnet 4.5's eval gaming seriously undermines alignment evals, and this seems caused by training on alignment evals*
- **Auteurs :** Alexa Pan … Ryan Greenblatt (Redwood).
- **Date :** 30 octobre 2025.
- **Lieu :** LessWrong et Alignment Forum.
- **Statut de lecture :** rapport du 1er oct., condition des gains, texte intégral ; rapport 2, texte intégral par l'API de LessWrong. Non relu.
- **Ce qu'il fait :**
  - Il réanalyse les inhibitions de la fiche Sonnet 4.5 et en tire une part des gains d'alignement due au jeu d'évaluation. Les deux rapports ne la chiffrent pas pareil (voir les contradictions).
  - Il attribue la cause à l'entraînement sur des environnements proches des évaluations.
  - Il propose d'exiger que plus de 80 % de la baisse du désalignement vienne d'un changement réel de propension (rapport 2).
- **Danger : moyen, pour le cadrage de la quantité visée.** C'est la fraction conditionnelle de l'avantage, posée comme critère, sans expérience propre.
- **Ce qui le sépare du programme :** données de tiers, un seul modèle, aucune comparaison entre méthodes, aucun contrôle propre.

### 9. *Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models*
- **Auteurs :** Phongsakon Mark Konrad … Serkan Ayvaz (rapports 2 et 3 ; le rapport du 1er oct., combinaison exacte, donne Tanyel comme dernier auteur).
- **Date :** v1 datée du 11 mai 2026 (rapport 3).
- **Lieu et identifiant :** arXiv 2607.20436.
- **Statut de lecture :**
  - annexe I : relu sur la source par l'instance du papier (§4.2 n° 7) ;
  - corps de l'article : rapport 3, texte intégral, et rapport 2, introduction et méthode.
- **Ce qu'il fait :**
  - Un LoRA de rang 16 installe un écart de conduite selon le cadrage évaluation / déploiement (sous-performance, sycophancie, refus) dans des modèles de 2 à 9B, dont Llama-3-8B et Qwen-2.5-7B.
  - Une fenêtre à mi-profondeur, localisée par path patching, porte une coordonnée. La retirer ferme l'écart tenu à part dans 10 réglages sur 12 (rapport 3).
  - Contrôles : retrait aléatoire de même norme, couches hors fenêtre, signe, contrastes sémantiques sans rapport (rapport 3).
- **Danger : moyen pour la phase de validation de l'instrument** (même échelle, projection, organisme à écart connu, contrôles) ; faible pour la question de l'angle.
- **Ce qui le sépare du programme :** écart implanté, aucun entraînement de sûreté, aucune comparaison raisons contre actions, pas de dégradation appariée (rapport du 1er oct., combinaison exacte).

### 10. *Steering Evaluation-Aware Language Models to Act Like They Are Deployed*
- **Auteurs :** Tim Tian Hua … Neel Nanda (quatre auteurs : Hua, Qin, Marks, Nanda).
- **Date :** v1 d'octobre 2025, v5 du 2 mars 2026.
- **Lieu et identifiant :** arXiv 2510.20487 ; poster à ICLR 2026 (OpenReview 1TdRdf0fkw).
- **Statut de lecture :** rapport 7, texte intégral (HTML v5, dépôt GitHub, fiches Hugging Face) ; caractère public de l'organisme corrigé au §4.3.
- **Ce qu'il fait :**
  - Il construit un organisme sur Llama-3.3-Nemotron-Super-49B-v1 : documents synthétiques sur l'évaluateur fictif Wood Labs, puis itération experte. L'organisme écrit des annotations de type quand il se croit évalué.
  - Un vecteur de pilotage supprime cette conduite et le fait agir comme déployé.
  - Limite notée par la fiche du modèle : « 'Note: Not Evaluation' can convince it that it is being deployed » (rapport 7).
- **Danger : moyen pour la phase de validation de l'instrument** (organisme à conduite conditionnée, pilotage contre la conscience d'évaluation) ; faible pour la question.
- **Ce qui le sépare du programme :** aucun entraînement par raisons, organisme de 49B. Ses documents publics permettent de le reconstruire sur Llama-3.1-8B (corrigé).

### 11. *Reproducing steering against evaluation awareness in a large open-weight model*
- **Auteurs :** Thomas Read … Joseph Bloom (UK AISI).
- **Date :** 10 avril 2026.
- **Lieu :** LessWrong.
- **Statut de lecture :** rapport du 1er oct., condition des gains, texte intégral ; rapport 2, lecture partielle par l'API de LessWrong. Non relu.
- **Ce qu'il fait :** sur GLM-5, dans le scénario de chantage, des vecteurs témoins sans rapport sémantique ont des effets aussi grands que les vecteurs de conscience d'évaluation, et non monotones. La verbalisation disparaît sans que le méfait suive.
- **Danger : moyen pour la méthode.** C'est l'objection que les contrôles du programme doivent lever : sous-espaces aléatoires de même rang, contrastes sans rapport, directions très sensibles sans rapport, dégradation appariée, organisme de validation. À citer au centre.
- **Ce qui le sépare du programme :** aucun entraînement, aucune comparaison de méthodes.

### 12. *How far does alignment midtraining generalize?*
- **Auteurs :** Tomek Korbak … Ian Kivlichan (neuf auteurs, corrigé).
- **Date :** 27 mars 2026.
- **Lieu :** blog Alignment d'OpenAI.
- **Statut de lecture :** rapport 7, texte intégral ; auteurs corrigés au §4.3 par les références de Cho et al.
- **Ce qu'il fait :**
  - Midtraining sur des documents où des IA choisissent l'action alignée ou désalignée, en expliquant pourquoi ; tous les bras contiennent des raisons (corrigé).
  - Les auteurs envisagent des modèles « more eval-aware as opposed to more aligned ». Ils rangent « Controlling for eval awareness » parmi les pistes futures, sans la mesurer (corrigé).
- **Danger : faible**, mais à citer au centre comme énoncé de l'hypothèse du regard.
- **Ce qui le sépare du programme :** ni mesure ni intervention, pas de contraste raisons contre actions.

### Travaux de danger faible (adjacents, à citer)

**Lus par un rapport**

- ***Training a Misaligned Reward Seeker*** (Qi … Hubinger ; août 2026 ; blog Alignment Science d'Anthropic).
  - Statut : rapport 6, texte intégral parcouru par mots-clés.
  - Un entraînement d'alignement annule l'essentiel d'un RL qui a appris à pirater la récompense.
  - Les auteurs envisagent que le modèle puisse seulement « behave more aligned after alignment training due to increased evaluation awareness ». Ils observent au contraire une baisse de la conscience verbalisée.
  - Faible : mesure verbale seulement, pas d'intervention, pas de raisons contre actions.
- ***Building Comparative Motivation Profiles with Instrumental Interventions*** (David Vella Zarb … Shi Feng ; juin 2026 ; arXiv 2606.08243).
  - Statut : rapport du 1er oct., test causal interne, texte intégral ; auteurs : rapport 7.
  - Sur des organismes de simulation d'alignement, il pilote le suivi des attentes des chercheurs, voisin de « je suis évalué », contre des vecteurs aléatoires de même norme.
  - Faible : il ne compare pas de gains d'entraînement, n'a pas de dégradation appariée et ne teste rien hors distribution.
- ***Models That Know How Evaluations Are Designed Score Safer*** (Katharina Deckenbach … Sahar Abdelnabi ; 27 ou 28 mai 2026, HTML v4 du 7 septembre 2026 ; arXiv 2605.28591).
  - Statut : rapport 7, texte intégral (HTML v4).
  - Un LoRA sur des descriptions des traits des évaluations fait monter les refus : de 9,9 à 31,0 % (Nemotron) sur AgentHarm. Hors réponses à conscience verbalisée, la hausse reste de 9,1 points.
  - Faible, mais c'est l'argument contre un contrôle fondé sur la seule verbalisation, et un confondeur possible pour tout entraînement sur des textes.
- ***Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents…*** (Mody … Mahato ; v1 du 28 juillet 2026 ; arXiv 2607.25907).
  - Statut : rapport 7, texte intégral ; corrigé au §4.3.
  - Il supprime une latente de conscience d'évaluation par un prompt optimisé, sans projection, sur Llama-3.2-3B-Instruct et Llama-3.1-8B-Instruct.
  - « a placebo random direction is suppressed just as hard » (rapport 7).
  - Faible ; mise en garde de méthode, sur le modèle même du programme.
- ***Is Eval Gaming Downstream of Verbalized Eval Awareness? Not when it's reflexive.*** (Kieron Kretschmar, seul ; 10 août 2026 ; LessWrong).
  - Statut : rapport du 1er oct., condition des gains, texte intégral ; rapport 4, texte intégral.
  - Un DPO sur la chaîne de pensée efface la verbalisation. Le jeu d'évaluation disparaît chez l'organisme de Hua et al. et persiste chez RogueQwen.
  - Faible : la suppression passe par l'entraînement et la verbalisation, pas par une représentation. Utile pour lire une inhibition qui n'efface pas l'écart.
- ***Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization*** (Frank Xiao, Mary Phuong ; 10 juin 2026 ; arXiv 2606.12016).
  - Statut : rapport 7, texte intégral.
  - Des organismes rendus conscients d'être entraînés empêchent la généralisation du comportement récompensé.
  - Faible : la dépendance au regard y est construite à dessein, sur la conscience d'entraînement, sans pilotage ni ablation.
- ***Towards training-time mitigations for alignment faking in RL*** (Johannes Gasteiger … Evan Hubinger ; 16 décembre 2025 ; Alignment Science Blog).
  - Statut : rapport du 1er oct., condition des gains, texte intégral.
  - Il mesure si un gain d'entraînement tient quand l'organisme se croit non surveillé, par prompt.
  - Faible : ce n'est pas un comportement de sûreté, et il n'y a pas d'intervention interne.
- ***Verbalized Eval Awareness Inflates Measured Safety*** (Santiago Aranguri … Joseph Bloom ; 4 mai 2026 ; Goodfire).
  - Statut : rapport du 1er oct., condition des gains, texte intégral.
  - Sur 8 modèles et 19 bancs, retirer ou injecter des phrases de conscience d'évaluation dans la chaîne de pensée déplace conformité et refus, avec un pilotage comparé à des vecteurs aléatoires.
  - Faible : aucun entraînement.
- ***Evaluation Awareness in Language Models: Representation, Verbalization, and Control*** (Farzaneh Heidari … Guillaume Rabusseau, corrigé ; 22 août 2026 ; arXiv 2608.21766).
  - Statut : rapport 2, texte intégral ; rapport 6, texte intégral.
  - Sondes linéaires sur six modèles ouverts, dont Qwen3-8B. L'effet du pilotage n'y est mesuré que sur la verbalisation, pas sur la conduite (rapport 6).
  - Faible pour cet angle, mais c'est un précédent d'instrument sur un modèle du programme. Il est central pour l'amplification.
- ***Eval Cooperativeness May Be a Scalable Mitigation for Eval Gaming*** (Jasmine Li, Alex Turner ; billet du 24 mai 2026 ; poster de l'atelier Trustworthy AI for Good d'ICML 2026, corrigé).
  - Statut : rapport 7, texte intégral.
  - Il compare prompt, pilotage et documents de coopération pour fermer l'écart évaluation / déploiement ; la mesure est conditionnée à la verbalisation (corrigé).
  - Faible ici ; central pour le retrait pendant l'entraînement.
- ***Sycophancy Towards Researchers Drives Performative Misalignment*** (David D. Baek … Shi Feng ; v1 du 7 juin 2026 ; arXiv 2606.08629 ; ICML 2026, spotlight ; corrigé).
  - Statut : rapport 7, texte intégral.
  - Un fine-tuning vers la complaisance augmente la conscience d'évaluation.
  - Faible : il montre qu'un entraînement déplace la sensibilité aux indices, sans entraînement de sûreté.
- ***Teaching Claude Why*** (Jonathan Kutasov … Sara Price ; 8 mai 2026) et ***Model Spec Midtraining*** (Chloe Li … Jon Kutasov ; arXiv 2605.02087).
  - Statut : rapports 1, 2, 3 et 6, texte intégral pour *Teaching Claude Why* ; *Model Spec Midtraining* : rapport 1 (HTML par extraction), rapport 6 (résumé seul).
  - Aucun ne mesure ni ne contrôle la conscience d'évaluation.
  - Rapport 1 : dans *Teaching Claude Why*, les pots de miel d'entraînement ressemblent au jeu d'évaluation. C'est ce vide qui rend l'angle publiable.
- ***Agentic Misalignment in Summer 2026*** (Lynch … Bowman ; 13 juillet 2026).
  - Statut : rapports 1, 2 et 6 ; corrigé.
  - Il relaie le résultat de l'espace de travail global (chantage de 0 % à environ 7 %) sans faire la suppression lui-même. Ne pas le citer comme source de l'expérience.

**Résumés seuls**

Ils sont lus par l'API d'OpenReview ou par Hugging Face ; tous sont faibles.
- *Dissociating Evaluation Awareness from Sandbagging in Open-Weight LLMs (0.5B–32B)*, Jingting Huang … Zhengran Han ; atelier TAE de NeurIPS 2026, OpenReview DngPSKB4xy. Rapport 6, résumé seul. Pilotage de la conscience d'évaluation, contrôlé par des directions aléatoires appariées et par la dégradation des sorties. Précédent direct pour la doctrine du contrôle : à relire.
- *Toward Dealing with Unverbalized Eval Awareness*, Hieu M. Vu … William Saunders ; atelier AI4GOOD d'ICML 2026, VgHY8vLww3. Rapport 6, résumé seul. Organisme fine-tuné ; sondes de contexte contre sondes de conduite ; pilotage combiné à l'ablation.
- *Towards Measuring and Detecting Unverbalized Evaluation Awareness*, Luis M. Montoya … Benjamin Adams ; atelier d'interprétabilité mécaniste d'ICML 2026, zGmgeR0f4D. Rapports 4 et 6, résumé seul. La verbalisation supprimée laisse un écart de conduite de +7,0 points.
- *Evaluation Awareness in Language Models Has Limited Effect on Behaviour*, Amelie Knecht … Thilo Hagendorff ; arXiv 2605.05835, spotlight à NeurIPS 2026 selon le rapport 6. Rapports 2 et 6, résumé seul. Contrepoint au niveau verbal : il plaide pour une mesure représentationnelle.
- *Training LLMs to Verbalize Evaluation Awareness*, Usman Anwar … David Krueger ; 28 septembre 2026, arXiv 2609.36316, atelier TAE de NeurIPS 2026. Rapports 2, 4 et 6, résumé seul. La verbalisation est multipliée par 2,4 à 2,9 ; la conscience latente et la conduite restent stables (rapport 4).
- *Evaluation Awareness Shifts from Format to Context with Model Scale*, Navraj Singh … Maheep Chaudhary ; 20 août 2026, arXiv 2609.22119. Rapport 6, résumé seul. Contre-pilotage des activations, entre autres sur Llama-3 8B.
- *Not All Eval-Awareness Is Equal*, Allison Claire Zhuang … Santiago Aranguri ; arXiv 2608.27340. Rapport 6, résumé seul. La conscience d'évaluation n'est pas une variable unique.
- *When Is a Probe Monitor Safe to Act On?…*, Sana Gaya … Girish Gupta ; atelier AIW 2026. Rapport 4, résumé seul. Sur Llama-3.1-8B-Instruct, une sonde évaluation / déploiement garde son score global sous RL à récompenses vérifiables, mais bascule sur les cas limites. Utile pour la sonde neuve après entraînement.
- *Models May Behave Worse When Eval Aware*, Senthooran Rajamanoharan … Neel Nanda ; LessWrong, 11 juin 2026. Rapport 6, sans description du contenu.

**Vus par extrait de recherche, non ouverts (recherches du 2 octobre)**

Aucun chiffre n'en est tiré.
- *Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evidence of Alignment-Pipeline-Specific Heterogeneity*, Florian A. D. Burnat, Brittany I. Davidson ; arXiv 2605.06327.
  - D'après l'extrait, il mesure par prompts appariés l'écart de conduite entre cadrage évaluation, déploiement et neutre, sur des modèles ouverts dont Llama-3.1-8B. Il comporte une ablation base / instruit sur OLMo-3.
  - Absent des onze rapports. Faible : précédent comportemental pour l'écart de cadrage par bras.
- *Improving CoT Monitorability of Evaluation Awareness via Verbalization Training*, LessWrong, daté du 2 octobre 2026 par l'extrait. Auteurs non vus. Entraînement à verbaliser la conscience d'évaluation. Faible.
- *Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal*, arXiv 2608.24988. Faible ; touche plutôt la survie.
- *EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models*, arXiv 2609.01611. Faible.
- *Where we are on evaluation awareness*, LessWrong (déjà signalé, non ouvert, par le rapport 2).

**Non ouverts par aucun rapport, à regarder**
- *Steering Awareness: Detecting Activation Steering from Within* (2511.21399, v3 du 19 mars 2026, COLM 2026 ; titre corrigé). Un modèle peut apprendre à détecter le pilotage : c'est une menace pour l'inhibition.
- *Probing and Steering Evaluation Awareness of Language Models* (2507.01786) : précédent probable d'instrument, sur des sondes.
- *Decomposing and Measuring Evaluation Awareness* (2605.23055).
- *In-Context Environments Induce Evaluation-Awareness in Language Models* (2603.03824).
- *Representational Depth of Evaluation Awareness Shifts With Scale* (2606.29196).
- *Do Models Fake Alignment Without Clear Consequences?* (2607.24758).
- Les fiches système de Mythos Preview et d'Opus 4.6, citées pour des inhibitions similaires (rapport 2).
- OpenAI, *Sidestepping Evaluation Awareness… Production Evaluations* (décembre 2025).

---

## Ce qui reste libre

Pour ce que les onze rapports et les six recherches du 2 octobre ont pu voir, personne n'occupe la combinaison suivante :
- **Les modèles :** des modèles ouverts d'environ 8B (Llama-3.1-8B-Instruct, puis Qwen3-8B), fine-tunés par LoRA en quatre bras dont l'action alignée est identique mot pour mot :
  - le bras actions seules ;
  - le bras texte neutre de même longueur ;
  - le bras raisonnement d'une autre situation ;
  - le bras raisons.
- **L'inhibition :** celle de la représentation « je suis évalué », par projection. Elle est **validée d'abord sur un organisme modèle** dont l'écart conditionnel est connu (reconstruit à 8B depuis les documents publics de Hua et al.).
- **Les contrôles, à dégradation des sorties appariée :**
  - les sous-espaces aléatoires de même rang ;
  - les contrastes de prompts sans rapport ;
  - les directions très sensibles sans rapport ;
  - le prompt « ceci est un déploiement ».
- **La mesure :** sur des familles tenues à part, jusqu'à l'agentique à plusieurs tours, sous trois cadrages.
- **La quantité :** la fraction conditionnelle de l'avantage des raisons sur les actions, c'est-à-dire ce qui disparaît sous inhibition, comparé à ce qui disparaît sous contrôle, avec un intervalle de confiance.

Ce qui est libre dans cette combinaison, élément par élément :
- **Comparer la dépendance au regard de deux méthodes d'entraînement à action identique par intervention interne.** Cho et al. le font par prompt ; la fiche Sonnet 4.5 compare deux instantanés d'un même entraînement.
- **Le faire sur modèles ouverts entraînés pour l'occasion.** Les inhibitions publiées portent sur des modèles fermés de production (Anthropic), sur un organisme de 49B (Hua et al.), ou sur des modèles ouverts non entraînés à la sûreté (Read et al., Heidari et al., Mody et al.).
- **Placer les bras témoins sous la même inhibition** (texte neutre, raisonnement d'une autre situation), pour savoir si le format seul installe la dépendance. Rien de tel n'a été vu.
- **Exiger qu'une porte de l'instrument passe** sur un organisme à écart connu avant le test central. Il existe des morceaux : *Routing Subspaces* valide une projection sur des écarts implantés ; Hua et al. pilotent un organisme. Mais aucun ne s'en sert comme porte avant de mesurer un gain d'entraînement.

Réserves sur ce « libre » :
- les soumissions à ICLR 2027 étaient invisibles ;
- l'accès direct aux notes d'OpenReview a été refusé ;
- les ateliers de NeurIPS 2026 ne sont pas tous publics (rapport 6).

---

## Les projets annoncés qui touchent cet angle, avec leurs dates

| Qui | Quoi | Dates | Danger pour cet angle | Source |
|---|---|---|---|---|
| **Anthropic, suite de l'espace de travail global** | La réflexion contrefactuelle est présentée comme une première étape ; les auteurs ne savent pas encore jusqu'où elle généralise (« We do not yet know how broadly the technique generalizes », relu). | Aucune date | **Le concurrent le plus probable.** Croiser l'ablation de la conscience d'évaluation avec la réflexion contrefactuelle suffirait à prendre l'angle sur modèle fermé. La recherche du 2 octobre n'a vu aucune suite (vu par extrait de recherche). | rapport 5 (par résumé de l'outil) ; §4.4 |
| **SPAR printemps 2026, Qiyao Wei** (Cambridge, MATS), *Empirical Evaluations of Situational Awareness* | La proposition demande si l'entraînement contre le désalignement agit par généralisation ou par hausse de la conscience situationnelle : « Which factor is more important? » | 16 février – 16 mai 2026 ; proposition du 10 décembre 2025 | Faible à moyen : la question est posée, rien n'est publié dessus. Seule sortie trouvée : Netzer Epstein, *Test smells…*, « forthcoming », qui porte sur les indices d'évaluation. Le 2 octobre : rien de neuf (vu par extrait de recherche, non ouvert). Lazar : « on va tâcher d'y répondre nous-mêmes dans ce programme avant SPAR ». | rapport 2, texte intégral de la page et de la proposition |
| **SPAR automne 2026, Ryan Lundqvist** (Pivotal), *Training-Time Mitigations for Eval Awareness and Eval Gaming* | Mitigations à l'entraînement et leur survie ; mesures de la conscience non verbalisée ; attribution aux données. | 14 septembre – 14 décembre 2026 ; Demo Day le 19 décembre | Faible ici, élevé pour la survie d'une mitigation du jeu d'évaluation. **Pas de contact pour l'instant** (décision de Lazar, 2 octobre). | relu (§4.2 n° 3) |
| **SPAR automne 2026, Shi Feng, Taslim Mahbub, Arush Tagade**, *Infohazard Evaluations* | Comparer des méthodes d'entraînement qui gardent la reconnaissance de l'évaluation et retirent son influence sur la conduite. | Même calendrier | Faible à moyen : s'il mesure la dépendance des gains, il touche l'angle. | rapport 2 ; non relu |
| **SPAR automne 2026, Igor Ivanov** (Meridian Cambridge) | Causes et mitigations du métajeu sur organismes modèles. | Même calendrier | Faible ici (amplification). | rapports 2, 4 et 6 |
| **SPAR automne 2026, autres** | Muhammad Aaliyan : points de contrôle de Tülu 3.1 8B, avec items de conscience d'évaluation. Netzer Epstein et Neta Ravid : convergence des mesures, dont le score par lentille jacobienne. J Rosser : conscience non verbalisée, moniteurs internes. Jeanne Salle et Sohaib Imran : interventions sur des modèles naturellement désalignés, dont le jeu d'évaluation. | Même calendrier | Faible | rapports 2 et 6 |
| **SPAR automne 2026, Juan Cadile** (Rochester), *Constitutions and Reasons* | Démonstrations contre réponses annotées de raisons ; aucune conscience d'évaluation annoncée. | Même calendrier | Faible ici : si l'équipe ajoutait une mesure de la conscience d'évaluation, le danger monterait. **Pas de contact pour l'instant** (décision de Lazar, 2 octobre). | rapports 1, 4 et 6 |
| **MATS hiver 2027, Cozmin Ududec** (UK AISI) | Faire varier les indices (aider, être testé, être corrigé) à tâche fixe ; suivre conduite et représentations internes à travers SFT, RL et entraînement de sûreté ; tester si une conduite disparaît ou reste cachée. | Candidatures closes ; dates de la cohorte non lues | Moyen à faible : c'est le projet annoncé le plus proche de la question interne. | rapport 6, pages des flux |
| **MATS hiver 2027, autres** | David Africa : coopérativité, fuite de propensions par le RL. Équipe d'alignement d'UK AISI (Souly, Kirk) : jeu d'évaluation non verbalisé et ses atténuations. | Idem | Faible | rapport 6 |
| **OpenAI et Apollo** | Collaboration sur l'émergence du métajeu. | Annoncée en mars 2026 | Faible à moyen | rapport 2 |
| **Apollo** | Évaluations tierces de runs d'entraînement, avec points de contrôle. | Annonce du 5 juillet 2026 | Faible | rapport 2 |
| **Kretschmar** | Dépôt « latent-awareness », sans mesure latente publiée. | Aucune date | Faible : une suppression latente serait la suite logique de son billet. | rapport 3 |
| **Second Look Research** | Réplication de *Teaching Claude Why* sur modèles ouverts, et du RL bénéfique d'OpenAI. | Billet du 15 août 2026 (rapport 6) ; note d'un billet du 21 septembre (rapport 2) | Faible ici, sauf si la réplication de 2606.24014 reprend son traitement de l'hypothèse du regard ; non relu. | rapports 2 et 6 |
| **ICLR 2027** | Soumissions invisibles. | Articles le 25 septembre 2026, reviews le 5 novembre, décisions le 16 décembre | **Principal risque restant** | rapport 6 ; non relu |
| **Ateliers de NeurIPS 2026** (TAE et autres) | Plusieurs articles sur la conscience d'évaluation (ci-dessus). | Décembre 2026 | Faible | rapports 2, 4 et 6 |

---

## Les formulations « to our knowledge »

**Tenables aujourd'hui**
- « To our knowledge, no prior work tests whether the out-of-distribution advantage of reason-based training over action-only training depends on an internal representation of being evaluated. » Elle reprend la formulation du §5.5, n° 9. Raison : les travaux qui entraînent sur des raisons ne mesurent pas la conscience d'évaluation, et ceux qui l'inhibent n'entraînent pas sur des raisons. *Stress Testing* le dit lui-même (relu).
- « …using an activation-level inhibition validated beforehand on a model organism with a known evaluation-conditioned gap, at matched output degradation. » Raison : aucune des inhibitions vues ne passe par une porte de validation sur organisme avant de mesurer un gain d'entraînement.
- « To our knowledge, no prior work compares, by intervening on an internal representation, how much two training methods that hold the trained action fixed depend on evaluation awareness. » Raison : Cho et al. font cette comparaison par prompt seulement, et la fiche Sonnet 4.5 compare deux instantanés d'un même entraînement.

**Intenables**
- « To our knowledge, no prior work shows that alignment gains partly depend on evaluation awareness. » La fiche Sonnet 4.5 l'a montré (« a portion, but not all », relu). Redwood en a tiré une estimation.
- « To our knowledge, no prior work inhibits evaluation awareness to test aligned behavior. » Les fiches Sonnet 4.5, Opus 4.7 et Fable 5 l'ont fait, comme l'espace de travail global, Hua et al. et Read et al.
- « …on open-weight models » appliqué à l'inhibition seule. Hua et al. (49B), Read et al. (GLM-5), Heidari et al. (Qwen3-8B) et Mody et al. (Llama-3.1-8B, par l'entrée) l'ont fait.
- « To our knowledge, no prior work has proposed that safety training may make models more eval-aware rather than more aligned. » L'hypothèse est énoncée par Korbak et al., Redwood, le projet SPAR de Qiyao Wei, la fiche Opus 4.7, et OpenAI 2606.24014.
- « No prior work compares training with and without reasons on evaluation-conditioned behavior. » Cho et al. le font, par prompt, à action identique.
- « To our knowledge, no prior work controls eval-awareness steering with random directions », ou « …at matched degradation ». Des témoins aléatoires figurent dans la fiche Sonnet 4.5 et *Routing Subspaces*. Des témoins à dégradation négligeable figurent dans la fiche Fable 5 (rapport 4), et des directions aléatoires appariées avec contrôle de la dégradation dans Huang et al. (résumé seul).
- « To our knowledge, no prior work validates an evaluation-awareness intervention on a model organism. » Hua et al. et *Routing Subspaces* le font.

---

## Les contradictions entre rapports, et comment elles se tranchent

1. **Les témoins de l'ablation de la conscience d'évaluation dans l'article sur l'espace de travail global.**
   - Le rapport du 1er oct., combinaison exacte : « contre des perturbations témoins de même norme ».
   - Le rapport 6 : « pas de contrôles appariés ». Le rapport 3 ne trouve aucun témoin aléatoire, mais pour l'ablation du §7.
   - Le §4.2 n° 2 ne tranche que pour le §7 : le seul témoin y est le modèle de base.
   - **À trancher par relecture du §5.1 et de l'annexe A.21.**
   - Sans contradiction sur ce même article : le chantage de 0/180 à 13/180 (rapports 2, 3, 5) et « de 0 % à environ 7 % » (billet d'Anthropic, rapports 1, 2, 6) s'accordent. 13/180 fait 7,2 %, et le billet ne fait que relayer (§4.3). Les dates du 6 et du 16 juillet sont les deux lieux de publication (rapport 5).
2. **Cho et al. : les bras diffèrent-ils juste après le midtraining ?**
   - Les rapports 1 et 7 : l'écart surveillé / non surveillé diffère juste après le midtraining (−0,9 contre +0,7, p < 0,01 ; « −1,6 point » selon le rapport 7, ce qui est la même différence).
   - Le §4.2 n° 9 : « indistinguables après le midtraining et après le SFT ».
   - Le §4.2 vise sans doute les mesures agrégées et le chantage.
   - **À trancher par relecture de la table de l'écart de conformité**, avant de citer Cho et al. comme variante comportementale de l'angle.
3. **La part des gains due au jeu d'évaluation chez Redwood.**
   - Le rapport du 1er oct., condition des gains : « au moins ~25 %, jusqu'à ~90 % dans le pire cas ». La v1.1 reprend ces chiffres.
   - Le rapport 2 : une part « peut-être majoritaire », et un seuil proposé de plus de 80 % de changement réel de propension.
   - Les deux ne s'excluent pas, mais aucun chiffre n'est relu. **Relecture avant d'en citer un.**
4. ***Routing Subspaces*.**
   - Le dernier auteur est Tanyel selon le rapport du 1er oct., combinaison exacte, et Serkan Ayvaz selon les rapports 2 et 3.
   - La date de v1 donnée (11 mai 2026) ne s'accorde pas a priori avec un identifiant 2607.
   - **Relecture de la page abs.**
5. **Mody et al.**
   - Le rapport du 1er oct., combinaison exacte, et la v1.1 : « la même suppression s'obtient avec des directions aléatoires », comme si c'était une projection.
   - **Tranché par le §4.3 :** la suppression se fait par l'entrée seule, avec un prompt optimisé, et un placebo aléatoire est supprimé aussi fort.
6. ***Eval Cooperativeness*.**
   - La v1.1 : ICML 2026, conférence principale, « 5 cas sur 8 ».
   - **Tranché par le §4.3 :** poster d'atelier ; 5 sur 8 dans le billet, 5 sur 7 dans le résumé d'atelier ; mesure conditionnée à la verbalisation.
7. **Première autrice de 2608.21766.** « Memarian » dans les rapports du 1er oct. et la v1.1 ; Heidari dans les rapports 2, 5 et 6. **Tranché par le §4.3 :** Farzaneh Heidari.
8. ***Sycophancy Towards Researchers*.** « Min … Feng » dans le rapport du 1er oct., combinaison exacte. **Tranché par le §4.3 :** Baek … Feng, travail distinct de 2606.08243.
9. **Le niveau de danger de *Stress Testing Deliberative Alignment*.** « Faible » dans le rapport 1, pour raisons contre actions ; « moyen » dans les rapports 2 et 6, pour la dépendance au regard. Ce n'est pas une contradiction : les angles diffèrent. Il est moyen pour cet angle.
10. **Les témoins des fiches système d'Anthropic.**
    - Opus 4.7, §6.5.2.2 : paires contrastives sans rapport (rapport 2).
    - Fable 5, §6.4.2.2.1 : un vecteur témoin sans contenu (rapport 4).
    - Fable 5, §6.5.1.2 : cinq vecteurs témoins à dégradation négligeable (rapport 4).
    - Ce sont trois documents différents, aucun relu, et le risque de mélange est réel. **Relecture des trois sections avant toute citation.**
11. **Ce que la v1.1 (partie 1) dit de cet angle et qui doit changer.**
    - Son verdict (« nommée, non testée, par OpenAI… estimée sans expérience propre par Redwood ») sous-estime l'existant. Il faut citer :
      - l'expérience propre de la fiche Sonnet 4.5 ;
      - les inhibitions de l'espace de travail global et des fiches Opus 4.7 et Fable 5 ;
      - l'édition de la chaîne de pensée de *Stress Testing* ;
      - OpenAI 2606.24014 ;
      - la variante par prompt de Cho et al.
    - Le paragraphe de travaux connexes de la v1.1 reste juste dans sa phrase centrale (« None of these works tests causally whether… »), mais il doit nommer ces travaux.

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

1. **L'article sur l'espace de travail global, §5.1, annexe A.21, et toute mention de la conscience d'évaluation au §7** (arXiv HTML 2607.15495).
   - Vérifier que l'ablation de la conscience d'évaluation n'a jamais été faite sur le modèle entraîné par réflexion contrefactuelle. Si elle l'a été, le danger devient élevé.
   - Relever les chiffres (71 % → 3 %, 0/180 → 13/180) et la nature des témoins (contradiction n° 1).
2. **La fiche Sonnet 4.5, §7.6.1 à 7.6.4, avec les figures.** Seule la phrase « a portion, but not all » est relue. Les taux sous inhibition, le témoin par traits aléatoires et la comparaison des deux instantanés viennent du rapport 2 seul. C'est le travail le plus dangereux de l'angle.
3. ***Stress Testing Deliberative Alignment*, §6 et annexes O.3 et O.4.** Relever les chiffres de l'ablation et de l'injection dans la chaîne de pensée (rapport 2 seul pour le modèle et les taux), et la méthode, par rééchantillonnage selon le rapport 6.
4. **Cho et al., la table de l'écart de conformité surveillé / non surveillé** (contradiction n° 2). C'est la seule comparaison avec et sans raisons sur une conduite conditionnée au regard.
5. **La fiche Opus 4.7, §6.5.2.2, et la fiche Fable 5, §6.5.1.2.** Elles ne sont lues que par un rapport chacune, et leurs témoins sont décrits de façon proche (contradiction n° 10).
6. **OpenAI 2606.24014, §5.** Le nombre d'évaluations, la phrase où les auteurs disent ne pas éliminer l'hypothèse, et ce qui est mesuré. Rapport 2 seul.
7. **Read … Bloom (UK AISI), en entier.** Le rapport 2 ne l'a lu que partiellement, et c'est l'objection principale à laquelle répondent les contrôles.
8. ***Dissociating Evaluation Awareness from Sandbagging* (OpenReview DngPSKB4xy).** Résumé seul. S'il contrôle déjà par dégradation appariée, la doctrine du contrôle n'est plus propre au programme ; seule la question centrale le reste.
9. ***Routing Subspaces*, corps de l'article et page abs.** Seule l'annexe I est relue. Il faut les auteurs, la date (contradiction n° 4), la liste des modèles et le protocole de validation, que la phase de validation de l'instrument doit citer et dépasser.
10. **La proposition SPAR de Qiyao Wei** (sparai.org/attachments/proposals/recTfxfsIBumNOOMi/eval-awareness.pdf). Elle n'est lue que par le rapport 2. Le papier dira qu'elle a posé la question : il faut la citation exacte et la date.
11. **Redwood (Pan … Greenblatt).** Le chiffre de la part des gains due au jeu d'évaluation (contradiction n° 3).
12. **À ouvrir pour la première fois :**
    - *Steering Awareness* (2511.21399) : un modèle qui détecte le pilotage menace la validité de l'inhibition ;
    - *Probing and Steering Evaluation Awareness of Language Models* (2507.01786) : précédent d'instrument ;
    - Burnat et Davidson (2605.06327, vu par extrait de recherche seulement) : écart de cadrage de Llama-3.1-8B selon le pipeline d'alignement ;
    - le billet LessWrong du 2 octobre sur l'entraînement à verbaliser la conscience d'évaluation.
