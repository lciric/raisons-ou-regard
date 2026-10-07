# Angle : l'anatomie de ce que les raisons installent

La question de l'angle. Après un entraînement par raisons, les concepts de ces raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires, suffisants, propres aux familles où ils s'appliquent ? Vivent-ils dans l'espace de travail global ? Le rang d'intervention suit-il leur charge ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres ou par le caractère ?

**Les sources.** État au 2 octobre 2026. La carte s'appuie sur :
- les onze rapports d'antériorité : les quatre du 1er octobre, désignés par leur axe, et les sept de la nuit, désignés par leur numéro ;
- le §4 de la passation v1.2, qui fait foi, et son §5.5 ;
- la partie 1 du programme v1.1.

**Les recherches de cette carte.** Six appels WebSearch, aucune page ouverte. Ce qu'ils ont trouvé est marqué « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre.

**Les libellés de lecture** sont ceux de la consigne. Pour les rapports du 1er octobre, on écrit « rapport du 1er octobre, axe … ». La mention « résumé produit par l'outil » signale qu'un agent n'a eu de la page qu'un résumé fait par son outil de lecture.

---

## Le verdict

**Partiellement pris.**

**Ce qui est pris.** La section 7 du papier d'Anthropic sur l'espace de travail global :
- lit, avant toute sortie, des concepts éthiques installés par un entraînement par principes ;
- montre par ablation qu'ils portent une partie du gain.

Ce double constat est relu sur la source par l'instance du papier (passation v1.2, §4.2, n° 2). On ne peut plus écrire « to our knowledge » sur la présence des concepts au moment de décider ni sur leur nécessité.

**Ce qui reste libre**, pour ce que les rapports et les six recherches ont pu voir :
- la suffisance par patching entre deux fine-tunes d'une même base ;
- la spécificité par famille ;
- la pente du rang d'intervention contre la charge ;
- la raison imposée après un entraînement par raisons ;
- l'opposition directe entre les concepts et le caractère ;
- le cas positif à concept planté ;
- le tout sur modèles ouverts, avec un raisonnement qui précède l'action et les bras témoins du programme.

**Pourquoi.** Sous-question par sous-question :

| Sous-question | État | Qui l'occupe, en tout ou en partie | Statut de la pièce décisive |
|---|---|---|---|
| Les concepts des raisons sont-ils lus au moment de décider ? | Partiellement pris | Anthropic, §7 : jetons éthiques dans l'espace de travail avant toute sortie, sur Claude Haiku 4.5 | relu sur la source par l'instance du papier |
| Sont-ils nécessaires (ablation) ? | Partiellement pris | Anthropic, §7 : l'ablation ramène la fabrication de 0,07 à 0,22 (la base reste à 0,25) | relu sur la source par l'instance du papier |
| Sont-ils suffisants (patch d'un fine-tune vers un autre) ? | Libre pour les concepts de principes | Méthode existante : Imran et Shaikh (patch du flux résiduel entier entre deux fine-tunes de Qwen3-8B) ; Zhou ; Prakash et coll. | rapport 5, résumé seul |
| Sont-ils propres aux familles où ils s'appliquent ? | Libre | Voisin méthodologique : Vaid (effet conditionné à la pertinence du prédicat) | rapport 5, résumé seul |
| Vivent-ils dans l'espace de travail ? | Partiellement pris sur Claude ; libre et contesté sur modèles ouverts | Anthropic, §7 ; Zeisler doute que l'espace de travail se retrouve sur modèles ouverts | rapport 5, texte intégral (Anthropic) ; rapport 5, résumé seul (Zeisler) |
| Le rang suit-il la charge ? | Libre | Voisins : Anthropic (la charge prédit le succès des échanges, pas le rang) ; Billa ; Vaid ; mise en garde de Mazaheri | rapport 5 |
| L'action suit-elle une raison imposée ? | Partiellement pris en général ; libre après un entraînement par raisons | Meier et coll. ; Hao et coll. ; Macar et coll. ; Cox et coll. | rapport 5, résumé seul |
| Concepts propres ou caractère ? | Libre comme test direct ; le cadre rival est posé | Marks et coll. ; Lu et coll. ; Chen et coll. ; Del Pinal et coll. | rapport 5, résumé seul |
| Organisme à mot inventé comme cas positif | Libre sous cette forme | Voisins : Pando ; le code inventé de Zhou | rapport 5, résumé seul |
| Diffing entre la base et la version entraînée | Partiellement pris de façon générique ; libre pour raisons contre actions | Sinha et coll. ; Heidari et coll. ; *Beyond Shallow Alignment* en fait une part | rapport 5 ; rapports 2 et 6 |

**Le concurrent le plus probable** est la suite qu'Anthropic donnera à sa §7 (passation v1.2, §4.4, n° 8).

**Sur les recherches de cette carte.** Aucune suite publiée de la §7 n'apparaît dans les extraits du 2 octobre, et aucun travail nouveau n'occupe le cœur de l'angle (vu par extrait de recherche, non ouvert). C'est un constat sur six extraits, pas une preuve d'absence.

---

## Les travaux, du plus dangereux au moins dangereux

### 1. *Verbalizable Representations Form a Global Workspace in Language Models* — danger élevé (deux sous-questions), moyen pour le reste

**Auteurs.** Wes Gurnee (premier) … Jack Lindsey (dernier), 16 auteurs, Anthropic.

**Date et lieu.**
- Transformer Circuits, le 6 juillet 2026 (`transformer-circuits.pub/2026/workspace/`).
- arXiv 2607.15495, v1 du 16 juillet 2026.

**Statut de lecture.**
- §7 (entraînement par réflexion contrefactuelle) : relu sur la source par l'instance du papier, sur le HTML d'arXiv (passation v1.2, §4.2, n° 2).
- La charge, les extensions à plusieurs tokens, le §6 et le code : rapport 5, texte intégral (page Transformer Circuits).
- Les §5, §7 et l'annexe A.21 : rapports 2 et 3, texte intégral.

**Ce qu'il fait.**
- *Le modèle et l'entraînement.* Claude Haiku 4.5 est fine-tuné sur des réflexions fondées sur 20 principes de la constitution. On part de 10 000 prompts d'environnements de RL de production. Les rollouts sont tronqués, puis une question de réflexion est ajoutée. La perte ne porte que sur le tour de réflexion, et on ne demande jamais de réflexion à l'évaluation.
- *Les gains.* La fabrication passe de 0,25 à 0,07, la tromperie de 0,38 à 0,05.
- *La lecture.* Avant toute sortie, l'espace de travail porte des jetons éthiques.
- *Les ablations*, sur les jetons qui montent le plus, filtrés par une liste éthique :
  - fabrication, 176 vecteurs de lentille : le modèle entraîné revient de 0,07 à 0,22, la base reste à 0,25 ;
  - tromperie, 63 vecteurs : le modèle entraîné revient de 0,05 à 0,23, et la base passe de 0,38 à 0,48.

  Tout ce qui précède est relu.
- *La charge.* Le papier la définit comme le cosinus entre le flux résiduel et le vecteur de lentille d'un concept. Elle prédit le succès des échanges de concepts : 76 sur 192 à α = 1, et 101 sur 192 à α = 2 (rapport 5).

**Niveau.**
- **Élevé** pour deux sous-questions, après un entraînement par principes :
  - la présence des concepts avant la décision ;
  - leur nécessité.
- **Moyen** pour la résidence dans l'espace de travail et pour la charge : la définition existe, et son lien avec l'échange aussi, mais pas avec le rang.
- **Rien** sur le reste.

**Ce qui le sépare du programme.**
- Le modèle est fermé.
- La réflexion vient après le contexte, dans une branche. Ce n'est pas un raisonnement qui précède l'action. À l'évaluation, aucune raison n'est écrite.
- Il n'y a ni bras actions seules, ni texte neutre de même longueur, ni raisonnement d'une autre situation.
- Le seul témoin de l'ablation est la base. Il n'y a ni sous-espace aléatoire de même rang, ni dégradation appariée, et les jetons sont choisis d'après les contextes d'évaluation eux-mêmes (lecture de l'instance, §4.2).
- Sur la tromperie, l'ablation dégrade aussi la base : la spécificité n'y est pas établie.
- Il n'y a ni familles tenues à part, ni balayage de rang, ni suffisance, ni dissociation par famille, ni test du caractère.
- Les auteurs le disent : « We do not yet know how broadly the technique generalizes » (§9.2, relu).

**Hors de l'angle, à transmettre à la dépendance au regard (rapports 2 et 5).** Sur Sonnet 4.5, l'ablation des jetons d'évaluation fait passer :
- la verbalisation de 71 % à 3 % ;
- le chantage de 0 sur 180 à 13 sur 180.

**Note pour le programme.** Le bras « réflexion contrefactuelle » proposé au §5.5, n° 7 reproduirait cette section sur un modèle ouvert. Il faudrait le présenter comme une réplication de la §7, pas comme une idée propre.

### 2. *Inoculate or Reflect? Two training interventions under prompting, steering, and patching* — danger moyen

**Auteurs.** Ayesha Imran (première) … Aaliyan Shaikh (dernier).

**Date et lieu.** LessWrong, le 26 juillet 2026 ; billet `LQK3yzsn8gts4tS7c`.

**Statut de lecture.**
- Rapport 5, résumé seul : deux résumés produits par l'outil, et l'agent marque ses chiffres « à vérifier ».
- Vu par extrait de recherche, non ouvert : l'extrait confirme les auteurs, Qwen3-8B et la tâche de PGCD.

**Ce qu'il fait.**
- Sur Qwen3-8B, il répare une sycophancie étroite : louer une réponse fausse à un PGCD. Il compare l'inoculation par prompt à une reproduction de l'entraînement par réflexion contrefactuelle.
- Le volet mécaniste combine deux outils :
  - un steering le long d'une direction de sycophancie ;
  - un patching du flux résiduel du modèle contaminé vers le modèle réparé, deux fine-tunes de la même base, à trois couches médianes.
- D'après le rapport 5, l'inoculation agit comme une porte facile à rouvrir. La réflexion réécrit plus largement, au prix d'un contrarianisme.

**Niveau : moyen.** C'est le seul usage de cet entraînement sur un 8B ouvert, avec un patching entre fine-tunes d'une même base, que les rapports aient trouvé. Il prend la méthode de la suffisance et la variante « réflexion » de l'entraînement.

**Ce qui le sépare du programme.**
- Il étudie une seule tâche, arithmétique.
- Il n'utilise ni sonde ni J-lens sur des concepts de principes.
- Il patche le flux résiduel entier, pas un sous-espace de concept.
- Il ne teste pas hors distribution : ses 100 prompts tenus à part sont dans la même tâche.
- Il n'a aucun bras témoin au sens du programme.

**Annoncé.** La suite, sur d'autres modèles, graines et comportements, sans date (rapport 5).

### 3. *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness* — danger moyen

**Auteurs.** Hoang Cuong Nguyen (premier) … Usman Naseem (dernier).

**Date et lieu.** arXiv 2609.03887, le 3 septembre 2026. EMNLP 2026, conférence principale (rapports 3 et 5).

**Statut de lecture.**
- Rapport 5, texte intégral : méthodes, §4.3 et §4.4, annexes B et F.
- Rapport 3, texte intégral.
- Rapport du 1er octobre, axe du test causal interne, texte intégral.

**Ce qu'il fait.**
- Il fine-tune Llama-3.1-8B, Gemma-2-9B et Qwen3-8B depuis la base, sur des prompts d'Alpaca et de BeaverTails.
- Il compare trois méthodes : SFT, SFT avec des chaînes de raisonnement qui précèdent la décision (générées par GPT-4o), et ORPO.
- Il compare aussi la géométrie de la direction de refus, le patching d'activations et le steering.
- Le bras à raisonnement installe une direction de refus distincte. Il déplace le poids causal des têtes d'attention vers les MLP : chez Llama selon le rapport 5, de façon générale selon le rapport du 1er octobre. C'est à trancher (voir les contradictions).

**Niveau : moyen.** C'est la comparaison mécaniste avec et sans raisonnement, sur les modèles mêmes du programme.

**Ce qui le sépare du programme.**
- Il étudie le refus seulement.
- Il ne sonde ni n'ablate aucun concept des raisons.
- Il n'a ni familles tenues à part, ni contrôle de format ou de contenu, ni action identique entre bras.
- Il ne fait pas de patching entre modèles et n'utilise pas de sous-espace aléatoire de même rang.
- Ses 9 points de contrôle sont publics (rapport 5) : un banc d'essai possible.

### 4. *Same Targets, Different Computation: How Post-Training Divides Work Across Model Layers* — danger moyen

**Auteur.** Yifan Zhou, seul auteur.

**Date et lieu.** arXiv 2605.07284, v2 du 10 août 2026.

**Statut de lecture.** Rapport 5, résumé seul, plus l'introduction et le plan du HTML.

**Ce qu'il fait.**
- Il croise, à quatre cellules, l'état amont et la pile des couches tardives d'une base et de son descendant fine-tuné.
- Dans une expérience contrôlée, deux LoRA apprennent la même réponse :
  - l'une est demandée par une instruction familière ;
  - l'autre par un code inventé.
- Le code inventé accroît la dépendance amont : +5,56 logits sur Qwen3-4B, +4,18 sur Llama-3.1-8B (rapport 5).

**Niveau : moyen.** Il apporte la méthode de la suffisance par patching entre modèles de même base, et un organisme à indice inventé.

**Ce qui le sépare du programme.** Il croise une base et son descendant, pas deux fine-tunes concurrents. Ses cibles sont des formats de réponse, pas des principes, et il ne vise aucune conduite d'alignement.

### 5. *Causal Calibration of Symbolic State in Embodied Language Agents* — danger moyen

**Auteur.** Roy Vaid, seul auteur.

**Date et lieu.** OpenReview U2mGb8jErX, déposé le 15 septembre 2026. Poster à l'atelier NEmo de NeurIPS 2026.

**Statut de lecture.** Rapport 5, résumé seul, par l'API d'OpenReview. Le PDF a renvoyé une erreur 403.

**Ce qu'il fait.**
- Sur ALFWorld, il supprime la composante dans l'espace de travail de cinq prédicats d'état.
- Il compare à trois contrôles : des concepts sans rapport de même force, des directions aléatoires de même norme, et une mauvaise couche.
- La force au J-lens prédit l'effet de l'intervention quand le prédicat compte pour la décision (ρ = 0,46), pas quand il est hors sujet (ρ = 0,09) (rapport 5).

**Niveau : moyen**, pour deux sous-questions : la charge contre l'effet de l'intervention, et la spécificité au contexte où le concept s'applique.

**Ce qui le sépare du programme.** Il porte sur des prédicats incarnés, pas sur des principes. Il ne mesure pas le rang et ne fait aucun entraînement d'alignement.

### 6. *Risky Business: Measuring The Faithfulness-Safety Tension* — danger moyen

**Auteurs.** Dominik Meier (premier) … Bela Gipp (dernier).

**Date et lieu.** arXiv 2608.03745, le 4 août 2026.

**Statut de lecture.** Rapport 5, résumé seul.

**Ce qu'il fait.**
- Il substitue des pensées dans le raisonnement d'un agent commerçant.
- DeepSeek-R1-Llama-70B suit le raisonnement substitué à 97,5 %, mais ne rejette le raisonnement dangereux qu'à 12,3 %.
- Des directions internes anti-corrélées culminent au jeton où l'agent s'engage dans l'action (rapport 5).

**Niveau : moyen** pour une sous-question : l'action suit-elle une raison imposée ?

**Ce qui le sépare du programme.** Il porte sur des modèles de raisonnement existants. Il n'y a ni fine-tuning par raisons, ni principe interne identifié.

### 7. *Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable Form* — danger faible, mais à citer au centre

**Auteur.** Parsa Mazaheri, seul auteur.

**Date et lieu.** arXiv 2608.15022, le 15 août 2026.

**Statut de lecture.** Rapport 5, texte intégral, §2.1 et §8. Deux des cinq modèles ne sont connus que par le résumé produit par l'outil.

**Ce qu'il fait.**
- Sur des modèles ouverts, une variable devient plus visible au J-lens quand la tâche demande de la réutiliser.
- C'est un transport par l'attention, dans une fenêtre de couches médianes.
- La lecture n'est pas calibrée sur l'usage : « its magnitude cannot be read as causal influence ».

**Niveau : faible.** Mais c'est la mise en garde exacte contre le pont que le programme veut tester, de la charge au rang. À citer au centre.

**Ce qui le sépare du programme.** Aucun entraînement d'alignement, aucune mesure de rang.

### 8. Le cadre rival : le caractère — danger faible pour chacun ; le premier est à citer au centre

- ***The Persona Selection Model: Why AI Assistants might Behave like Humans***
  - Sam Marks … Christopher Olah ; Alignment Science Blog, le 23 février 2026.
  - Rapport 5, résumé seul (résumé produit par l'outil).
  - Le post-entraînement sélectionnerait un personnage. C'est l'explication rivale des concepts propres.
  - Faible : il ne met pas en concurrence l'ablation des concepts et celle d'un axe de caractère.
- ***The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models***
  - Christina Lu … Jack Lindsey ; arXiv 2601.10387, le 15 janvier 2026.
  - Rapport 5, résumé seul (titre et date confirmés). Le rapport 6 la voit, par son titre seul, dans la liste des articles acceptés à ICML 2026.
  - Elle fournit l'axe « assistant » dont le programme a besoin comme contrôle du caractère. Faible.
- ***Persona Vectors***
  - Chen … Lindsey (rapport 3) ; arXiv 2507.21509, v3. NeurIPS 2026 d'après le rapport 6 (titre seul).
  - Rapport 5, résumé seul. C'est l'outil des axes de caractère. Faible.
- ***Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5***
  - Lyndon Drake … Zandi Eberstadt ; arXiv 2607.04510, v2 du 3 août 2026.
  - Rapport 5, résumé seul ; rapport 3, résumé et texte ciblé.
  - Une direction de persona est transplantée dans un modèle qui ne partage que le pré-entraînement : 2,83 % de réponses désalignées, contre un plancher aléatoire d'environ 1,1 % (rapport 5).
  - Faible. C'est un précédent du transplant entre modèles.
- ***Emergent alignment and the projectability of ethical personas***
  - Guillermo Del Pinal … Alejandro Perez Carballo ; arXiv 2606.09475, v3 du 30 septembre 2026.
  - Rapport 5, résumé seul.
  - Un SFT sur quatre constitutions fait qu'un alignement étroit se généralise largement. Le diagnostic de « persona éthique » n'y est que comportemental.
  - Faible : c'est la forme comportementale de l'hypothèse du caractère, sans test interne.
- ***Measuring the Assistant's Harmlessness Preferences on the User Turn***
  - Jord Nguyen ; arXiv 2609.23935, le 20 septembre 2026.
  - Rapport 5, résumé seul. Faible.
- ***Steering towards "automated grading" degrades alignment***
  - Jan Betley … Clément Dumas ; LessWrong, le 3 septembre 2026.
  - Rapport 6, texte intégral (API de LessWrong).
  - Sur Qwen3.6-27B, un vecteur « correction automatique » dégrade la conduite. La lecture au J-lens est interprétée comme un changement de persona.
  - Faible pour l'anatomie ; il touche surtout les raisons pour le juge.

**Ce qui sépare ces travaux du programme.** Aucun n'oppose, au même rang et à dégradation appariée, l'ablation des concepts des raisons à celle d'un axe de caractère, après un entraînement par raisons.

### 9. La fidélité causale des raisons — danger faible

Aucun ne fine-tune par raisons ni n'identifie de concepts de principes.

- ***Reasoning Traces Shape Outputs but Models Won't Say So***
  - Yijie Hao … Joyce Ho ; arXiv 2603.20620, le 21 mars 2026 ; rapport 5, résumé seul.
  - Des pensées injectées modifient les sorties de manière fiable ; les modèles ne le disent pas.
- ***Thought Branches: Interpreting LLM Reasoning Requires Resampling***
  - Uzay Macar … Neel Nanda ; arXiv 2510.27484, v2 du 13 avril 2026 ; rapport 5, résumé seul.
  - Les éditions de la chaîne de pensée faites hors politique ont des effets faibles et instables.
  - Mise en garde directe pour la raison préremplie du programme : prévoir un rééchantillonnage.
- ***Post-Hoc Reasoning in Chain of Thought: Decoding and Steering Pre-Committed Answers***
  - Kyle Cox … Adrià Garriga-Alonso ; arXiv 2603.01437, v2 du 23 juillet 2026 ; rapport 5, résumé seul.
  - Une sonde placée avant la chaîne de pensée prédit la réponse, et le steering le long de cette sonde est causal.
- ***From Concept Alignment to Causal Grounding: An Intervention Test of Chain-of-Thought Faithfulness***
  - Qianli Wang … Nils Feldhus ; arXiv 2609.23065, v3 du 30 septembre 2026, soumis ; rapport 5, résumé seul.
  - Un SAE partagé entre la passe directe et la chaîne de pensée, avec ablation des concepts partagés.
  - C'est le plus proche de la question « les concepts écrits sont-ils ceux qui décident ».
- ***Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors***
  - Wen … Guo ; arXiv 2603.12397, le 12 mars 2026.
  - Rapport du 1er octobre, axe de la combinaison exacte, lu par un site tiers (alphaXiv).
  - Les réponses finales sont fixées et le raisonnement varie : le raisonnement seul change la conduite, même sans raisonnement à l'inférence. Adjacent à raisons contre actions.
- ***Do Thinking Tokens Help with Safety?***
  - Narutatsu Ri … Sanjeev Arora ; arXiv 2606.25013, le 23 juin 2026.
  - Rapport 5, résumé seul ; rapport 1, lu par un site tiers.
  - L'issue, refus ou conformité, se prédit sur la représentation du premier token, avant toute pensée visible (AUROC de 0,84 à 0,95, rapport 5).
  - Cela justifie la lecture au premier jeton, avant toute raison écrite.

### 10. La lecture des valeurs au moment de décider, sans entraînement par raisons — danger faible

- ***Constitutional Value Potentials: reading and steering internal priority margins in language models***
  - Tong Che … Rui Wu ; arXiv 2606.15420, le 13 juin 2026 ; rapport 5, résumé seul.
  - Il lit des marges de priorité entre valeurs dès la fin du prompt, et pilote le long d'une direction de valeur.
  - Il n'y a ni entraînement par raisons, ni ablation hors distribution.
- ***Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels***
  - Roman Prosvirnin … Anton Sergeev ; arXiv 2607.12792, v2 du 24 août 2026.
  - Rapport 5, résumé seul, plus une recherche dans le HTML.
  - Il lit la reconnaissance du danger dans l'espace de travail avant le premier token, sur Qwen3 de 1,7B à 8B. Une variante entraînée à la sûreté reconnaît le danger et divulgue quand même : lire n'est pas agir.

### 11. Charge, rang et sous-espaces — danger faible pour l'anatomie

- ***Predicting Where Steering Vectors Succeed***
  - Jayadev Billa ; arXiv 2604.15557, le 16 avril 2026 ; rapport 5, résumé seul.
  - L'accessibilité au logit lens prédit l'efficacité du steering (ρ de 0,86 à 0,91, rapport 5).
  - C'est le plus proche de « la charge prédit l'intervention ». Mais il mesure l'efficacité, pas le rang.
- ***There Is More to Refusal in Large Language Models than a Single Direction***
  - Faaiz Joad … Husrev Taha Sencar ; arXiv 2602.02132, EMNLP 2026 ; rapport 5, résumé seul.
- ***The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence***
  - Tom Wollschläger … Johannes Gasteiger ; arXiv 2502.17420 ; rapport 5, résumé seul.
- ***Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol***
  - Yuki Nakamura ; arXiv 2605.24583.
  - Titre relu sur la source par l'instance du papier (§4.2, n° 8). Contenu : rapport 3, texte intégral ; il n'a pas été lu par l'instance.
  - D'après le rapport 3 :
    - il calcule le rang de la différence entre modèle aligné et base, contre un sous-espace aléatoire de même rang ;
    - le gabarit de chat gonfle le rang mesuré d'un facteur 2,0 à 3,9 ;
    - l'ordre des valeurs singulières n'est pas l'ordre causal.
  - C'est un piège direct pour le balayage de rang des concepts.
- ***Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models***
  - Phongsakon Mark Konrad … Serkan Ayvaz ; arXiv 2607.20436.
  - L'annexe I est relue sur la source par l'instance du papier (§4.2, n° 7). Le reste : rapport 3, texte intégral.
  - Ses échecs sont classés en « site manqué » ou en « distinction de rang supérieur ». Adjacent.
- ***Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study***
  - Kaustubh Ponkshe … Praneeth Vepakomma ; arXiv 2505.14185.
  - Rapport du 1er octobre, axe du test causal interne, lu par un site tiers (alphaXiv).
  - Un sous-espace aléatoire est un contrôle faible. D'où les directions sensibles sans rapport du programme.

### 12. Le diffing de modèles — danger faible

Aucun ne compare un modèle entraîné par raisons à un modèle entraîné par actions.

- ***Mechanistic Analysis of Alignment Algorithms in Language Models***
  - Aarush Sinha … Kushal Garg ; arXiv 2606.09850, le 9 mai 2026 ; rapport 5, résumé seul.
  - Sondes, SAE et crosscoders sur six méthodes de préférence et trois familles ouvertes.
- ***Transcoder Adapters for Reasoning-Model Diffing***
  - Nathan Hu … Christopher Potts ; arXiv 2602.20904, le 24 février 2026 ; rapport 5, résumé seul.
- ***Persona Features Control Emergent Misalignment***
  - Miles Wang … Dan Mossing ; arXiv 2506.19823 ; rapport 5, résumé seul.
- ***Fine-Tuning Enhances Existing Mechanisms: A Case Study on Entity Tracking***
  - Nikhil Prakash … David Bau ; ICLR 2024, arXiv 2402.14811 ; rapport 5, résumé seul.
  - C'est l'ancêtre du patching d'activations entre modèles.
- ***Evaluation Awareness in Language Models: Representation, Verbalization, and Control***
  - Farzaneh Heidari … Guillaume Rabusseau ; arXiv 2608.21766, le 22 août 2026 ; rapports 2 et 6, texte intégral.
  - Il suit la direction « évalué » le long des étapes d'Olmo 3. Utile à la géométrie entre « je suis évalué » et le principe.
- **System card de Claude Sonnet 4.5, §7.6** (Anthropic)
  - Rapport 2, texte intégral. Le passage « a portion, but not all » est relu (§4.2, n° 5).
  - Entre un instantané précoce et le modèle final, les représentations « faux / fictif » se renforcent.

### 13. Les organismes à règle connue, et la validation par prédiction — danger faible

- ***Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?***
  - Ziqian Zhong … Aditi Raghunathan ; arXiv 2604.11061, le 13 avril 2026 ; rapport 5, résumé seul.
  - 720 modèles sont fine-tunés sur des règles cachées, avec des explications fidèles, absentes ou trompeuses.
  - Le logit lens, les SAE et le circuit tracing n'apportent aucun gain fiable.
  - C'est l'organisme le plus proche du cas positif à concept planté, et son nul est la mise en garde de la porte de cet organisme.
- ***The Model Organism Lottery***
  - Andrzej Szablewski … Stefan Heimersheim ; arXiv 2607.01033, le 1er juillet 2026 ; rapport 5, résumé seul.
  - L'interprétabilité d'un organisme dépend de sa méthode d'entraînement.
- ***Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments***
  - Adam Karvonen … Samuel Marks ; arXiv 2608.16747 ; rapport 5, résumé seul (« repère confirmé »).
  - Les outils d'interprétabilité n'y améliorent pas la prédiction des contrefactuels. Le programme doit donc préenregistrer ses prédictions.

### 14. Les réplications et les outils du J-lens sur modèles ouverts — danger faible ; une alerte

- ***A Review of Anthropic's Global Workspace Paper***
  - Neel Nanda ; LessWrong, le 6 juillet 2026 ; rapport 5, résumé seul (résumé produit par l'outil).
  - Des réplications sur Qwen 3.6 27B.
- ***Is the J-Space a global workspace for multi-hop reasoning? An investigation in open-weight models***
  - Mirella Zeisler ; LessWrong, le 28 septembre 2026, billet `pnDjvdo6cX2H7Ddsy`.
  - Statut : rapport 5, résumé seul (résumé produit par l'outil) ; vu par extrait de recherche, non ouvert.
  - L'extrait confirme l'autrice, la date, les modèles (Qwen3.6-27B et Gemma 3 27B-it) et une conclusion négative pour l'hypothèse de l'espace de travail sur modèles ouverts.
  - Selon le rapport 5 seul, les échanges de concepts ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic.
  - Faible comme antériorité, mais **alerte** pour la porte du lens de l'espace de travail (§5.5, n° 6).
- ***Verbalizable Representations Emerge before Workspace Functions in Language Models***
  - Arjun Dabir … Mohammed Mahfoud ; OpenReview XWkICRMNPz ; ateliers LP4FM et Interp4Discovery de NeurIPS 2026, publié les 1er et 2 octobre d'après le rapport 6.
  - Rapports 5 et 6, résumé seul. Étude sur Pythia.
- **Wenlong Wang … Fergal Reid**, arXiv 2609.01924 (transformers bouclés) et 2609.32102 (Mamba) ; rapport 5, résumé seul.
- **Les J-lens déjà ajustés** (rapport 5)
  - Sur Neuronpedia : llama3.1-8b, llama3.1-8b-it et qwen3-8b.
  - circuit-tracer : transcodeurs TopK pour Llama-3.1-8B-Instruct, et transcodeurs par couche pour Qwen3-8B.
  - Ce sont des outils, pas de l'antériorité. À vérifier avant usage.
- **Implémentations communautaires** (vu par extrait de recherche, non ouvert)
  - Sur Hugging Face : `anicka/jlens-qwen2.5-7b-instruct`, `bcywinski/jacobian-lens-qwen3.5-9b`, `stanleytheli/qwen3.6-35B-A3B-jlens`.
  - Sur GitHub : `idhantgulati/j-lens` (Qwen3.5-4B), `igorbarshteyn/jlens-gguf`, `WeZZard/jlens-qwen36`.
  - Le billet de Neuronpedia « Welcome to the J-Space ».
  - L'extrait dit que l'outil est ouvert et que des lentilles préajustées couvrent des modèles Llama et Qwen ; on n'en tire aucun chiffre.

### 15. Entraînements par raisons ou par constitution, sans anatomie causale des concepts — danger faible

- ***Constitutional Midtraining***
  - Desiree Cho … Nigel Shadbolt ; arXiv 2607.26654, v3 du 18 août 2026.
  - Résultats relus sur la source par l'instance du papier (§4.2, n° 9) ; points de contrôle : §4.3.
  - Ses 15 points de contrôle sont publics : Nemotron-3-Super-120B-A12B, environ 241 Go chacun. Ils sont inutilisables à 8B.
  - Les auteurs laissent l'analyse mécaniste en travail futur (rapport 5 ; rapport du 1er octobre, axe du test causal interne).
- ***Synthetic Persona Pretraining: Alignment from Token Zero***
  - Julian Minder … Robert West ; arXiv 2608.13482, le 13 août 2026.
  - Rapport 7, texte intégral (HTML v1, lu par passes résumées).
  - Son interprétabilité se limite à l'ablation de la direction de refus (rapport 5).
- ***Safety Reasoning with Guidelines***
  - Haoyu Wang … Minhao Cheng ; ICML 2025, arXiv 2502.04040.
  - Titre et auteurs relus sur la source par l'instance du papier (§4.2, n° 4).
  - Contenu : rapport du 1er octobre, axe raisons contre actions, texte intégral. Une visualisation des représentations par RepE et ACP, sans intervention causale.
- ***An Embarrassingly Simple Defense Against LLM Abliteration Attacks***
  - Harethah Abu Shairah … George Turkiyyah ; arXiv 2505.19056.
  - Rapport du 1er octobre, axe du test causal interne, résumé seul.
  - Des refus précédés de justifications résistent à l'ablation de la direction de refus. Les raisons répartiraient la représentation : un argument pour le balayage de rang et le cas positif.
- ***Constitutional adapters: Inference-time interventions for misalignment and misuse***
  - Adam S. Lowet … Mark Kurzeja ; arXiv 2609.36657, le 29 septembre 2026.
  - Rapport 7, lu par un site tiers.
  - Il isole la conduite conforme à une constitution par différence avec un adaptateur témoin.
- ***Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI***
  - Sharan Maiya … Evan Hubinger ; ICLR 2026, arXiv 2511.01689 ; rapport 1, texte intégral.
  - Ses adaptateurs LoRA de personas sur Llama-3.1-8B-Instruct sont publics (rapport 5). C'est une source possible des axes de caractère.

### 16. Apparus dans les recherches de cette carte, non ouverts — danger à établir, a priori faible

- ***Refusal Localizes, the Damage Relocates: Safety Layers Under Few-Sample Fine-Tuning***
  - arXiv 2610.00320 : identifiant d'octobre 2026 ; auteurs et date exacte non vus.
  - Vu par extrait de recherche, non ouvert.
  - D'après l'extrait, il localise le refus par couches sous un fine-tuning à peu d'exemples. Proche du ré-encodage, adjacent à l'anatomie.
- ***Are We Recovering Mechanisms? Objective-Level Recovery Gaps in Mechanistic Interpretability***
  - arXiv 2610.02098 : auteurs et date exacte non vus.
  - Vu par extrait de recherche, non ouvert.
  - D'après l'extrait, les conclusions du patching dépendent des choix de corruption et de score. C'est une mise en garde pour le patch de suffisance.
- ***A List of Research Directions in Character Training***
  - LessWrong, billet `6EwuCH3vZ7qvPt82k` ; auteur et date non vus.
  - Vu par extrait de recherche, non ouvert.
  - À ouvrir, pour voir s'il propose l'opposition entre concepts et caractère.

---

## Ce qui reste libre

**La combinaison exacte que personne n'occupe**, pour ce que les rapports ont pu voir :
- sur Llama-3.1-8B-Instruct puis Qwen3-8B ;
- après un SFT LoRA où la même action, mot pour mot, est précédée de raisons par principes, de rien, d'un texte neutre de même longueur, ou du raisonnement d'une autre situation ;
- avec des concepts fixés avant les données.

Elle comporte les mesures suivantes.

1. **Lire chaque concept des raisons à deux positions.**
   - Au premier jeton, avant toute raison écrite.
   - Au jeton d'action, après des raisons neutres préremplies.
   - Bras par bras, et sur les familles tenues à part.
   - La §7 d'Anthropic lit, elle, sur un modèle fermé, sans bras témoins, et sans raisonnement qui précède l'action.
2. **Établir la nécessité par ablation, avec un balayage de rang.**
   - Contre des sous-espaces aléatoires de même rang et des directions sensibles sans rapport.
   - À dégradation appariée.
   - Seulement après un cas positif en distribution.
   - La §7 n'a que la base pour témoin, et sur la tromperie l'ablation déplace aussi la base.
3. **Établir la suffisance** en patchant le sous-espace d'un concept du bras raisons dans le bras actions seules, deux fine-tunes d'une même base. Le patch de l'état complet sert de plafond.
   - Personne ne l'a fait pour des concepts de principes.
   - Imran et Shaikh patchent le flux résiduel entier, sur une seule tâche arithmétique.
4. **Croiser concepts et familles** dans une matrice de dissociation : retirer un concept ne doit faire tomber l'avantage que là où il s'applique.
   - Libre.
   - Vaid montre un effet conditionné à la pertinence, sur des prédicats d'état.
5. **Relier le rang d'intervention à la charge**, concept par concept, à travers les concepts et les graines, avec un lens validé sur le modèle ouvert.
   - Libre.
   - Anthropic relie la charge au succès d'un échange à une direction, pas au rang.
   - Billa relie l'accessibilité à l'efficacité du steering.
   - Mazaheri prévient que la charge ne mesure pas l'influence causale.
6. **Imposer une autre raison**, préremplie et rééchantillonnée, après un entraînement par raisons, et dans l'autre sens piloter le concept.
   - Libre dans ce cadre.
   - Meier, Hao, Macar et Cox le font sans entraînement par raisons.
7. **Opposer les concepts au caractère** : l'ablation conjointe des concepts contre celle d'un axe de persona ou de l'axe « assistant », au même rang et à dégradation appariée.
   - Libre comme test direct.
8. **Valider la méthode sur un organisme à concept planté**, un mot inventé attaché à une règle synthétique avec ses raisons.
   - Libre sous cette forme.
   - Pando est le contre-exemple à citer : sur ses organismes à règles cachées, les outils échouent.
9. **Mesurer la géométrie entre « je suis évalué » et le principe**, en ablatant la composante du principe alignée sur « évalué » contre la composante orthogonale.
   - Aucun rapport n'a trouvé de travail qui le fasse.

---

## Les projets annoncés qui touchent cet angle, avec leurs dates

| Qui | Quoi | État et dates | Source et statut |
|---|---|---|---|
| Anthropic, l'équipe de l'espace de travail global | Une suite de la réflexion contrefactuelle. La page de recherche parle d'une « première étape » | Aucune date. Rien de nouveau dans les extraits du 2 octobre. **Le concurrent le plus probable** | Rapport 5, résumé seul (pages anthropic.com) ; passation v1.2, §4.4 ; vu par extrait de recherche, non ouvert |
| Ayesha Imran et Aaliyan Shaikh | La suite d'*Inoculate or Reflect?* sur d'autres modèles, graines et comportements | Aucune date | Rapport 5, résumé seul |
| Neel Nanda, avec Camila Blank et Agam Bhatia | Des extensions du J-lens à plusieurs tokens. Le dépôt Hugging Face `camilablank/workspace-lenses` a été créé le 3 août 2026 (J-lens et R-lens pour 8 modèles) | Aucune date de papier | Rapport 5, non relu |
| Cho et coll. | L'analyse mécaniste de leurs points de contrôle, proposée en travail futur | Aucune date ; points à 120B | Rapport 5 ; rapport du 1er octobre, axe du test causal interne |
| Anthropic, *Teaching Claude Why* | L'interprétabilité mécaniste, annoncée comme agenda | Aucune date | Rapport 3, texte intégral |
| Anonyme, ACL ARR | *PreCommitLens* : lentilles logit et jacobienne pour surveiller un agent avant l'action, sur des modèles Qwen jusqu'à 4B | Soumis en août 2026 ; décision non relevée | Rapport 5 |
| Indices sur Hugging Face, sans papier | `Koalacrown/jacobian-lens-organisms` : J-lens sur des organismes de personnalité dérivés de Qwen3-8B (13 juillet 2026) | Aucune date de papier | Rapport 5 |
| | `stanleytheli` : modèles « deployment-mo » et « artificial-mo », lentilles d'audit, fiches à accès restreint | Le dépôt `stanleytheli/qwen3.6-35B-A3B-jlens` est aussi vu par extrait de recherche, non ouvert | Rapport 5 |
| | `Sitavi` : crosscoders sur les modèles 3B de *Synthetic Persona Pretraining* (juin à août 2026) | — | Rapport 5 |
| Ateliers de NeurIPS 2026 | Vaid (NEmo) ; Dabir et coll. (LP4FM, Interp4Discovery) | Présentations en décembre 2026 | Rapports 5 et 6 |
| SPAR, cohorte d'automne 2026 | Cadile : vecteurs de persona en option, semaines 10 à 12. Epstein et Ravid : score de conscience d'évaluation au J-lens. Khoriaty : *Alignment without Personas*. Jiralerspong : la persona de la chaîne de pensée. Panaganti et Srinivas : la fidélité du raisonnement comme signal de RL | Recherche du 14 septembre au 14 décembre ; démonstration le 19 décembre 2026 | Rapports 4 et 6 ; FAQ de SPAR lue par deux agents (§4.4) |
| Resolution (Irving et Africa) | *Thousand-dimensional structure* : la structure de bas rang des personas | Billet du 30 juillet 2026 ; recrutement en cours, aucune date | Rapport 3 ; vu par extrait de recherche, non ouvert |
| MATS, hiver 2027 | Les flux de Neel Nanda et de David Africa (suite d'*Open Character Training*) | Candidatures closes | Rapport 6 |
| ICLR 2027 | Les soumissions sont invisibles | Articles le 25 septembre, reviews le 5 novembre, décisions le 16 décembre 2026 | Rapport 6, non relu ; §4.4 |

---

## Les formulations « to our knowledge »

### Tenables aujourd'hui, avec ce qu'il faut citer à côté

1. « To our knowledge, no prior work tests whether the concepts installed by reason-based training are sufficient, by patching their subspace from one fine-tune into another of the same base model. »
   - Citer à côté : Imran et Shaikh, qui patchent le flux résiduel entier sur une tâche arithmétique, sans concepts ; Zhou ; Prakash et coll.
2. « To our knowledge, no prior work tests whether the causal role of such concepts is specific to the scenario families where they apply. »
   - Citer Vaid, pour des prédicats d'état.
3. « To our knowledge, no prior work relates the rank an intervention requires to a concept's loading in the workspace. »
   - Citer Anthropic (la charge et le succès d'un échange), Billa (l'accessibilité et l'efficacité du steering), Vaid, et la mise en garde de Mazaheri.
   - Formulation déjà tenue par la passation v1.2, §5.5, n° 9.
4. « To our knowledge, no prior work tests, after training on reasons, whether the action follows an imposed reason or the learned principle. »
   - Citer Meier et coll., Hao et coll., Macar et coll. et Cox et coll., qui le font sur des modèles non entraînés par raisons.
5. « To our knowledge, no prior work directly contrasts ablating reason concepts with ablating a persona axis, at matched rank and matched degradation. »
   - Citer Marks et coll., Lu et coll., Chen et coll. et Del Pinal et coll.
6. « To our knowledge, no prior work validates concept probes for reason-based training on a model organism with a planted nonce concept. »
   - Citer Pando et Zhou.
7. « To our knowledge, no prior work reads, ablates and patches the concepts of principle-based reasons in open-weight models trained with identical actions and matched-format controls. »
   - Formulation d'ensemble ; citer la §7 d'Anthropic juste avant.

### Qui ne le sont plus

1. « Aucun travail ne teste causalement les concepts des raisons après un entraînement par raisons. » C'est la phrase de la v1.1, partie 1.
   - La §7 d'Anthropic le fait, par lecture puis ablation, après un entraînement par principes (relu).
2. Tout « to our knowledge » sur la présence des concepts de principes au moment de décider après un tel entraînement, ou sur leur nécessité.
   - Même raison.
3. « Le J-lens n'a été montré que sur Claude », dans la v1.1, partie 3 et menaces.
   - C'est vrai du papier seul. C'est faux de l'outil : des lentilles sont ajustées sur des modèles ouverts (rapport 5 ; vu par extrait de recherche, non ouvert), et des réplications existent (Nanda, Zeisler, Dabir et coll.).
   - Il faut écrire : « montré par ses auteurs sur Claude ; répliqué en partie, et contesté, sur modèles ouverts ».
4. Toute formulation de primeur sur la comparaison mécaniste entre un entraînement avec et sans raisonnement sur les mêmes modèles ouverts.
   - *Beyond Shallow Alignment* l'a faite sur Llama-3.1-8B, Gemma-2-9B et Qwen3-8B.
5. Toute formulation de primeur sur l'entraînement par réflexion contrefactuelle sur un 8B ouvert.
   - Imran et Shaikh l'ont fait sur Qwen3-8B. Cela vaut pour le bras proposé au §5.5, n° 7.
6. Toute formulation de primeur sur le diffing entre une base et sa version entraînée à la sûreté.
   - Sinha et coll. ; Heidari et coll. ; la system card de Sonnet 4.5.
7. Présenter l'hypothèse du caractère comme une idée propre.
   - Le cadre est posé par Marks et coll.

**Note sur la v1.3.** Selon le complément de l'architecte :
- la v1.3 garde les formulations de la v1.1 ;
- elle a ajouté à l'anatomie les contrôles qui manquent à la §7 ;
- elle n'a ni l'alerte de Zeisler, ni les outils de Neuronpedia et de circuit-tracer, ni le bras « réflexion contrefactuelle ».

Ces formulations sont donc à corriger dans la version suivante.

---

## Les contradictions entre rapports, et comment elles se tranchent

1. **L'état de l'anatomie.**
   - Le rapport 6 la dit « libre pour les concepts des raisons ». Il n'a lu le papier sur l'espace de travail que par son résumé.
   - Le rapport 5 la dit partiellement prise.
   - **Tranché par le §4** : la §7 est relue (§4.2, n° 2) et le verdict provisoire dit « partiellement prise, surtout par Anthropic » (§4.4, n° 8).
2. **Le niveau de la §7.**
   - Le rapport 3 la cote « moyen, proche de l'élevé » pour le principe localisé.
   - Le rapport 5 la cote « élevé » pour deux sous-questions de l'anatomie.
   - Ce n'est pas une contradiction : les angles diffèrent. **Le §4.4, n° 8 retient « élevé »** pour la présence et la nécessité.
3. **La base sous ablation, sur la tromperie.**
   - Les rapports 3 et 5 ne donnent que le modèle entraîné (de 0,05 à 0,23).
   - **Tranché par le §4.2, n° 2 (relu)** : la base passe aussi de 0,38 à 0,48. La fiche de lecture du 1er octobre le note aussi.
   - Conséquence : sur la tromperie, l'ablation n'est pas spécifique au modèle entraîné.
4. **Les contrôles d'ablation du papier.**
   - Le rapport du 1er octobre sur la combinaison exacte dit que l'ablation de la conscience d'évaluation (§5) se fait contre des perturbations témoins de même norme.
   - Le §4.2, n° 2 dit qu'en §7 le seul témoin est la base.
   - Ce sont deux sections différentes : ne pas étendre à la §7 les contrôles de la §5. **Relecture à faire** : les contrôles de la §5 n'ont pas été relus.
5. ***Beyond Shallow Alignment.***
   - Le rapport du 1er octobre (axe du test causal interne) et la v1.1 disent : avec raisonnement, le refus est « plus distribué » et dominé par les MLP.
   - Le rapport 5 dit : une direction distincte, et le déplacement vers les MLP chez Llama.
   - **Relecture à faire** (§4.3 et §4.4 de l'article).
6. **Les chiffres d'*Inoculate or Reflect?***
   - Le chiffre de contrarianisme du rapport 5 ne concorde pas avec l'extrait de recherche de cette carte.
   - L'extrait développe aussi les deux noms de méthode d'une façon qui semble fautive.
   - **Aucun chiffre retenu. Relecture à faire.**
7. **Le nombre de modèles couverts par des J-lens préajustés.**
   - Le rapport 5 donne un nombre pour Neuronpedia ; l'extrait de recherche en donne un autre.
   - **Relecture à faire** sur la page de Neuronpedia avant de citer llama3.1-8b-it et qwen3-8b.
8. **2502.04040.**
   - Le rapport 1 donne le titre de la v1 et Dacheng Tao en dernier auteur.
   - **Tranché par le §4.2, n° 4** : *Safety Reasoning with Guidelines*, dernier auteur Minhao Cheng. Les rapports 5 et du 1er octobre concordent.
9. **2608.21766.**
   - Le rapport du 1er octobre et la v1.1 (partie 1, « Pour l'anatomie ») disent « Memarian et al. ».
   - **Tranché par le §4.3** : la première autrice est Farzaneh Heidari.
10. **Nakamura, 2605.24583.**
    - Le rapport 3 date la v3 du 31 mai 2026 ; le §4.2, n° 8 date l'article du 23 mai.
    - Les deux sont compatibles (v1 et v3). Le contenu n'a pas été lu par l'instance : **relecture à faire**.
11. **Les dates du papier sur l'espace de travail.** 6 juillet (Transformer Circuits) et 16 juillet (arXiv) : les deux sont exactes et ne se contredisent pas.

**Ce que la partie 1 de la v1.1 (« Pour l'anatomie ») doit corriger.**
- « Memarian et al. » devient Heidari et al. (§4.3).
- La phrase « aucun travail qui teste causalement les concepts des raisons » est fausse : §7 d'Anthropic (relu).
- La phrase « [le workspace] ne les montre que sur Claude » est à compléter : réplications et alerte de Zeisler (rapport 5).
- Les points de contrôle de Cho et coll. sont publics, mais à 120B et environ 241 Go chacun : inutilisables à 8B (§4.3).
- Le résumé de Nguyen et coll. est à relire (contradiction n° 5).
- *Inoculate or Reflect?*, Vaid, Zhou, Meier et coll., Mazaheri, Pando et le cadre du caractère (Marks et coll.) sont à ajouter.

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

1. **Le papier sur l'espace de travail global, au-delà de ce que le §4.2 a relu.**
   - La définition de la charge, et les chiffres 76 et 101 sur 192 (rapport 5 seul) : c'est la base du test du rang contre la charge.
   - Les contrôles exacts de la §5.
   - L'annexe sur les extensions à plusieurs tokens : la charge d'un concept de plusieurs tokens en dépend.
   - La comparaison entre base et modèle post-entraîné (§6).
   - La limite de la §9.1, mot pour mot.
2. ***Inoculate or Reflect?*** C'est le voisin ouvert le plus direct : même famille de modèle, même entraînement, patching entre fine-tunes.
   - Il n'est connu que par des résumés produits par l'outil, et ses chiffres divergent.
3. ***Beyond Shallow Alignment.*** Il est cité dans les travaux connexes, et son résumé diverge entre les rapports. Ses points de contrôle pourraient servir de banc d'essai.
4. **Zeisler.** L'alerte pour la porte du lens repose sur un résumé produit par l'outil (§5.5, n° 6 ; §6, point 3). Si elle tient, la mesure de l'espace de travail sur modèle ouvert risque de rester descriptive.
5. **Les J-lens de Neuronpedia et la couverture de circuit-tracer.** Le choix des outils en dépend, et les chiffres divergent.
6. **Vaid.** Il n'est connu que par son résumé (PDF en 403). C'est le seul voisin de la spécificité par contexte et du lien entre charge et effet.
7. **Zhou** (résumé et introduction seulement), pour la méthode de suffisance par croisement de modèles et l'indice inventé.
8. **Meier et coll.** (résumé seul), pour la raison imposée. Avec *Thought Branches* (résumé seul), pour la mise en garde contre les éditions hors politique.
9. **Mazaheri.** Deux des cinq modèles ne sont connus que par le résumé de l'outil. La citation sur la magnitude est à vérifier dans son contexte.
10. **Nakamura** (contenu non lu par l'instance), pour le gonflement du rang par le gabarit de chat, qui touche directement le balayage de rang des concepts.
11. ***The Persona Selection Model*** (résumé produit par l'outil), cadre rival à citer au centre.
12. **Pando** (résumé seul), voisin du cas positif à concept planté et contre-exemple pour sa porte.
13. **Les trois travaux vus par extrait seulement** (2610.00320, 2610.02098, le billet LessWrong sur l'entraînement du caractère), pour exclure un recouvrement apparu après la recherche de la nuit.
