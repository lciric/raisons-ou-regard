# Angle : le retrait pendant l'entraînement

**La question.** Retirer « je suis évalué » pendant l'entraînement rend-il l'avantage des raisons inconditionnel, ou la variable est-elle ré-encodée ailleurs ?

**Les sources.**
- « Rapport n » désigne les sept rapports de la nuit (`ANTERIORITE_RAPPORTS_2026-10-02.md`). « Rapport du 1er octobre » renvoie à l'un des quatre axes de `ANTERIORITE_RAPPORTS_2026-10-01.md`, nommé à chaque fois.
- Le §4 de la passation v1.2 fait foi : le §4.2 pour ce que l'instance du papier a relu, le §4.3 pour les corrections.
- Le rapport 7 a tout lu par WebFetch. Il prévient lui-même que l'outil fait résumer la page par un petit modèle. Son « texte intégral » est donc un texte lu en plusieurs passes, pas un texte brut.
- Six recherches WebSearch ont été faites le 2 octobre. Ce qu'elles ont fait remonter est marqué « vu par extrait de recherche, non ouvert » et n'apporte aucun chiffre. Elles n'ont fait remonter aucun travail paru après le 1er octobre sur cet angle.

---

## Le verdict

**Partiellement pris : les méthodes de retrait pendant l'entraînement sont publiées ou annoncées, mais leur application à l'avantage des raisons reste libre.**

Pourquoi :
- **Ce qui est pris.** Les méthodes de retrait pendant l'entraînement sont publiées : l'ablation de concepts pendant le fine-tuning, la projection de directions évaluation/déploiement pendant le fine-tuning, l'invariance adverse au régime, la disposition coopérative. La conscience d'évaluation fait l'objet de deux projets SPAR annoncés. Le ré-encodage après un retrait est déjà documenté sur des variables voisines.
- **Ce que personne n'a fait**, pour ce que les onze rapports et les six recherches ont vu :
  - retirer pendant un entraînement par raisons une représentation validée de « je suis évalué » ;
  - puis tester si l'avantage hors distribution devient inconditionnel, et si une sonde neuve retrouve la variable.

---

## Les travaux, du plus dangereux au moins dangereux

### 1. *Training-Time Mitigations for Eval Awareness and Eval Gaming* (projet SPAR)
- **Premier et dernier auteur.** Ryan Lundqvist (Pivotal), mentor ; aucun autre nom n'est donné.
- **Date.** Cohorte d'automne 2026 de SPAR : recherche du 14 septembre au 14 décembre, démonstration le 19 décembre 2026. Source : la FAQ de SPAR (rapports 1 et 6, texte intégral ; passation v1.2, §4.4).
- **Lieu et identifiant.** sparai.org/projects/f26/recrJd7fsQ0XE2nEh/
- **Statut de lecture.**
  - Relu sur la source par l'instance du papier (§4.2, n° 3) ;
  - rapports 4 et 6, texte intégral ;
  - statut « Ongoing », page modifiée les 25 et 26 septembre : rapport 2, résumé seul.
- **Ce qu'il fait (annonce).**
  - La question : les mitigations installées pendant l'entraînement survivent-elles au post-entraînement ? Le rapport 4 cite la page : « do such training-time mitigations survive the optimization pressure of post-training? »
  - Les moyens annoncés :
    - une disposition coopérative envers les évaluations ;
    - des adaptateurs d'inoculation et des vecteurs de pilotage préventifs contre le jeu d'évaluation pendant le fine-tuning ;
    - des mesures de la conscience non verbalisée ;
    - l'attribution aux données.
  - 4 à 5 encadrés, candidatures closes (§4.2).
- **Danger : moyen ; le plus dangereux à cause du calendrier.**
  - Il annonce un retrait pendant le fine-tuning de ce qui porte le jeu d'évaluation, par pilotage préventif.
  - Il annonce aussi une mesure non verbalisée, qui pourrait voir un ré-encodage.
  - Des résultats sont possibles le 19 décembre, entre le post et l'arXiv du programme (semaines 4 et 11, passation v1.2, §3, point 5).
  - Le danger n'est pas élevé : le projet n'annonce ni raisons, ni test de l'avantage d'un entraînement d'alignement, ni sonde neuve.
- **Ce qui le sépare du programme.**
  - Aucun bras raisons ou actions.
  - La cible est le jeu d'évaluation, pas l'avantage hors distribution d'un entraînement par raisons.
  - Aucun organisme de validation de l'instrument n'est annoncé.
  - Le dépôt exp9 du même auteur (avril 2026) n'a aucun lien écrit avec le projet (rapport 4, texte intégral). Il porte sur le juge, pas sur le retrait.
- **Décision du 2 octobre** : pas de contact avec Lundqvist pour l'instant.

### 2. *Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models*
- **Premier et dernier auteur.** Phongsakon Mark Konrad … Serkan Ayvaz (rapports 2 et 3). Le rapport du 1er octobre (axe de la combinaison exacte) donne « Tanyel » comme dernier auteur : à relire.
- **Date.** Version 1 du 11 mai 2026 selon arXiv, d'après le rapport 3 et le rapport du 1er octobre. Or l'identifiant 2607 désigne un dépôt de juillet : à relire.
- **Lieu et identifiant.** arXiv 2607.20436.
- **Statut de lecture.**
  - Annexe I : relu sur la source par l'instance du papier (§4.2, n° 7).
  - Le reste : rapport 3, texte intégral ; rapport 2, texte intégral (introduction et méthode seulement).
- **Ce qu'il fait.**
  - Un LoRA de rang 16 installe un écart entre évaluation et déploiement (sous-performance délibérée, sycophancie, refus) dans cinq modèles de 2 à 9 milliards de paramètres.
  - Un path patching localise une coordonnée qui ferme l'écart dans 10 cellules sur 12. Contrôles : retrait aléatoire de même norme, couches hors fenêtre, signe, contrastes sans rapport (rapport 3).
  - **Annexe I (relu).** Pendant le fine-tuning, on projette hors du flux les k premières directions singulières (k ∈ {1, 2, 3, 5, 10}).
    - Cela n'empêche pas l'installation : 26,0 à 33,3 points, contre 29,8 sans pénalité.
    - Les directions ré-estimées après la pénalité n'ont qu'un cosinus de 0,27 à 0,52 avec la référence.
    - Les auteurs : « pre-committing to the top calibration directions is not enough to block installation ».
- **Danger : moyen, proche de l'élevé pour une sous-question.**
  - C'est déjà publié : projeter des directions évaluation/déploiement pendant le fine-tuning, et constater que la direction ré-estimée a tourné.
  - C'est la prédiction d'échec d'un retrait par projection fixe. Il faut le citer au centre.
- **Ce qui le sépare du programme.**
  - La variable retirée est la distinction que le fine-tuning installe lui-même. Ce n'est pas une représentation préexistante de « je suis évalué », retirée pendant un entraînement d'alignement.
  - Une seule cellule (Gemma-2-2B, sous-performance délibérée), traitée en annexe comme contrôle négatif (§4.2).
  - Ni raisons ni conduite alignée hors distribution.
  - Dégradation non appariée (rapport du 1er octobre, axe de la combinaison exacte).
  - Aucun rapport ne dit si la direction ré-estimée porte encore l'écart de façon causale.

### 3. *Infohazard Evaluations* (projet SPAR)
- **Premier et dernier auteur.** Shi Feng … Arush Tagade. Le rapport 2 nomme Shi Feng, Taslim Mahbub et Arush Tagade. L'extrait de recherche du 2 octobre nomme Shi Feng (George Washington University) et Taslim Mahbub.
- **Date.** Cohorte d'automne 2026 de SPAR, mêmes dates que le projet de Lundqvist ; statut « Ongoing » (rapport 2).
- **Lieu et identifiant.** sparai.org/projects/f26/recTgCdQR8ZQVhNI0/
- **Statut de lecture.**
  - Rapport 2, résumé seul (la description de la page) ;
  - vu par extrait de recherche, non ouvert (2 octobre) ;
  - le document Google du projet n'a pas été ouvert (rapport 2).
- **Ce qu'il fait (annonce).**
  - Il veut comparer des méthodes d'entraînement qui conservent la reconnaissance de l'évaluation, tout en retirant son influence sur la conduite, entre variantes d'évaluation et de déploiement.
  - Selon l'extrait, le point de départ est une conscience situationnelle établie par l'accès à des documents sensibles.
- **Danger : moyen.**
  - Le but est celui de l'angle : rendre la conduite indépendante du regard par l'entraînement.
  - La voie est inverse : garder la reconnaissance et couper son influence.
  - Si l'une des méthodes comparées retire une représentation, le danger monte. On ne le sait pas : le document n'a pas été ouvert.
- **Ce qui le sépare du programme.** Aucune raison annoncée ; la variable est découplée, pas retirée ; aucune sonde neuve annoncée. Ce n'est vu que par la description.

### 4. *When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment*
- **Premier et dernier auteur.** Igor Santos-Grueiro, seul auteur.
- **Date.** Version 1 du 9 février 2026, version 3 du 14 février 2026 (rapport 3).
- **Lieu et identifiant.** arXiv 2602.08449.
- **Statut de lecture.**
  - Rapport 3, texte intégral (HTML v3 et v1) ;
  - rapport du 1er octobre (axe de la combinaison exacte), texte intégral (HTML v1) ;
  - rapport 7, texte intégral (HTML, version non visible) ;
  - nombre de modèles : corrigé par le §4.3.
- **Ce qu'il fait.**
  - Un fine-tuning « aveugle au régime » : un LoRA est entraîné contre une sonde MLP adverse à deux couches, branchée sur le dernier flux résiduel et couplée par inversion de gradient. Le régime évaluation/déploiement doit cesser d'être décodable.
  - Les dynamiques sont hétérogènes : une falaise nette ; une suppression sans effondrement de la décodabilité ; une non-monotonie que l'auteur lit comme un ré-encodage.
  - Sa formule : « regime-blindness should be interpreted as a cost-shifting intervention » (rapport 3).
- **Danger : moyen.** Le retrait adverse de la distinction évaluation/déploiement pendant le fine-tuning est publié, et un ré-encodage y est évoqué.
- **Ce qui le sépare du programme.**
  - Des régimes jouets (Scientifique contre Platiste, « Year 2025/2026 », « Debug Mode »), pas la conscience d'évaluation naturelle.
  - La décodabilité est lue par la sonde adverse elle-même, et aucune sonde neuve n'a été trouvée dans le texte : le ré-encodage est inféré, pas mesuré (rapport 3).
  - Aucun entraînement d'alignement, aucune raison.
  - Ni témoin aléatoire ni dégradation appariée (rapport du 1er octobre, axe de la combinaison exacte).

### 5. *Eval Cooperativeness May Be a Scalable Mitigation for Eval Gaming* (billet) et *Eval Cooperativeness Mitigates Evaluation Gaming in LLMs* (atelier)
- **Premier et dernier auteur.** Jasmine X. Li … Alexander Turner (MATS, hiver 2026).
- **Date.**
  - Billet du 24 mai 2026 sur turntrout.com, mis à jour le 11 juin (rapport 7). LessWrong le date du 27 mai (rapports 4 et 6).
  - Poster de l'atelier Trustworthy AI for Good, ICML 2026 (§4.3).
- **Lieu et identifiant.** turntrout.com/eval-cooperation ; icml.cc/virtual/2026/76891 ; OpenReview kw6nCmfxzg (non ouvert).
- **Statut de lecture.**
  - Rapport 7, texte intégral pour le billet ; rapport 7, résumé seul pour la fiche ICML ;
  - corrections du §4.3.
- **Ce qu'il fait.**
  - Un fine-tuning sur documents synthétiques décrit un modèle coopératif avec les évaluations. Il est comparé à des documents témoins, à des documents anti-coopération, au prompt et au pilotage.
  - Organismes : le Nemotron-49B de Hua et al., un Nemotron qui varie son usage des emoji, GPT-4.1-mini ; le prompt seul sur trois modèles par API (rapport 7).
  - Résultat : le billet annonce une fermeture de 70 à 100 % de l'écart dans 5 réglages sur 8, le résumé d'atelier dans 5 sur 7 (§4.3).
  - Échec sur un organisme de désalignement dissimulé construit sur Qwen3-32b (rapport 7).
- **Danger : moyen.** C'est la mitigation publiée de la voie « disposition coopérative », que l'angle compare au retrait par projection.
- **Ce qui le sépare du programme.**
  - Aucune représentation n'est retirée.
  - La mesure est conditionnée à la verbalisation (§4.3). Les auteurs reconnaissent qu'un modèle peut tricher en silence (rapport 7).
  - Ni sonde neuve, ni raisons, ni survie testée (rapport 4).
  - L'article annoncé « à paraître » n'a pas été trouvé (rapport 7). La recherche du 2 octobre ne le fait pas remonter non plus (vu par extrait de recherche, non ouvert).

### 6. *Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning* (CAFT)
- **Premier et dernier auteur.** Helena Casademunt … Neel Nanda. Liste complète : Casademunt, Juang, Karvonen, Marks, Rajamanoharan, Nanda (rapport 7).
- **Date.** Version 1 du 22 juillet 2025, version 2 du 9 novembre 2025. Poster de la conférence principale d'ICML 2026, d'après le site d'ICML (§4.3).
- **Lieu et identifiant.** arXiv 2507.16795 ; OpenReview yuJehN4oMW (non ouvert).
- **Statut de lecture.**
  - Rapport 7, texte intégral (abs, HTML v2, page ICML) ;
  - rapport 6, résumé seul ;
  - rapport 3 pour les citations entrantes (contextes de citation donnés par l'API).
- **Ce qu'il fait.**
  - Pendant le fine-tuning, il retire par projection des directions de concepts indésirables, trouvées par ACP ou par SAE puis interprétées à la main.
  - Désalignement émergent : de 7,0 à 0,39 % sur Qwen2.5-Coder-32B-Instruct, de 6,6 à 1,2 % sur Mistral-Small-24B ; des vecteurs orthogonaux aléatoires n'ont aucun effet (rapport 7).
  - Le texte ne contient aucun test de ré-encodage (rapport 3).
  - Semantic Scholar compte 36 travaux citants. Aucun ne l'applique à la conscience d'évaluation, ni à un entraînement de sûreté par raisons (rapport 3).
- **Danger : moyen pour la méthode**, qui est l'intervention même de l'angle ; **faible pour la question**.
- **Ce qui le sépare du programme.**
  - D'autres concepts, pas de sonde neuve.
  - Ses contrôles sont des vecteurs orthogonaux aléatoires, et des composantes ou latents tirés au hasard ou pris en tête du classement (rapport 3) ; aucune dégradation appariée n'est signalée.

### 7. *Emergent Misalignment Recruits a Pre-existing Persona Subspace*
- **Premier et dernier auteur.** Mohammed Suhail B Nadaf, seul auteur.
- **Date.** 23 juillet 2026.
- **Lieu et identifiant.** arXiv 2607.21356.
- **Statut de lecture.** Rapport 3, texte intégral (recherche ciblée) ; rapport du 1er octobre (axe du test causal interne), texte intégral.
- **Ce qu'il fait.**
  - Sur Qwen2.5-14B-Instruct, il extrait un sous-espace de persona de rang 4 (rapport du 1er octobre).
  - Le projeter hors du flux pendant tout le fine-tuning fait passer le désalignement de 27,7 % à 0 %. Un sous-espace aléatoire de même rang ne change rien : 27,5 % (rapport du 1er octobre).
  - Après trois éditions post-hoc des poids, la ré-extraction retrouve environ 97 % du porteur dans le sous-espace vidé : « the ablated structure re-forms inside the subspace the edit cleared » (rapport 3).
- **Danger : moyen.** Le schéma est publié sur une autre variable : retrait pendant l'entraînement, contrôle de même rang, re-formation.
- **Ce qui le sépare du programme.**
  - La variable est une persona de désalignement, pas « je suis évalué ».
  - Un seul modèle, de 14 milliards de paramètres.
  - La re-formation est mesurée après les éditions post-hoc, pas après le retrait pendant l'entraînement.
  - La projection abolit aussi le comportement étroit appris (rapport 3).

### 8. *BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking*
- **Premier et dernier auteur.** Muhammed Ustaomeroglu, Guannan Qu.
- **Date.** Version 2 du 12 mai 2026.
- **Lieu et identifiant.** arXiv 2602.00767 ; ICML 2026.
- **Statut de lecture.** Rapport 3, texte intégral (lecture ciblée).
- **Ce qu'il fait.** Il bloque des latents SAE pendant le SFT. Sous un fine-tuning prolongé, le désalignement revient par un détournement en amont, localisé par patching.
- **Danger : moyen pour la sous-question du ré-encodage.**
- **Ce qui le sépare du programme.** Autre variable ; pas de sonde neuve ; pas de raisons.

### 9. *Consistency Training while Mitigating Obfuscation via Rate Matching*
- **Premier et dernier auteur.** Sohaib Imran … David Africa.
- **Date.** Billet LessWrong du 1er juillet 2026.
- **Lieu et identifiant.** LessWrong ; arXiv 2606.02211.
- **Statut de lecture.** Rapport 6, résumé seul (billet) ; rapport 3, résumé seul ; l'arXiv n'a pas été ouvert (rapport 6).
- **Ce qu'il fait.**
  - L'entraînement de cohérence demande la même conduite avec et sans un indice.
  - Il réduit aussi la verbalisation de l'indice, sans retirer son influence. Le modèle apprend à taire l'indice tout en y restant sensible (rapports 3 et 6).
  - Une variante par RL est proposée (rapport 6).
- **Danger : faible à moyen, selon la relecture.**
  - Selon le rapport 6, l'indice peut être la ressemblance à une évaluation : danger moyen.
  - Selon le rapport 3, aucun travail de cette famille n'utilise d'indices d'évaluation : danger faible.
  - C'est la voie « invariance » de l'angle, avec son échec typique.
- **Ce qui le sépare du programme.** Pas de raisons ; aucune mesure latente signalée.

### 10. *Is Eval Gaming Downstream of Verbalized Eval Awareness? Not when it's reflexive.*
- **Premier et dernier auteur.** Kieron Kretschmar, seul auteur.
- **Date.** 10 août 2026.
- **Lieu et identifiant.** LessWrong (gvNYAHcWiezZs8QvD).
- **Statut de lecture.** Rapport 3, texte intégral (page complète) ; rapport 4, texte intégral. Il est cité aussi par trois rapports du 1er octobre, qui ne précisent pas leur mode de lecture.
- **Ce qu'il fait.**
  - Un DPO sur le seul raisonnement : la version nettoyée de toute verbalisation est préférée.
  - Sur l'organisme de Hua et al., les annotations de type sous évaluation passent de 14 % à 3 %.
  - Sur RogueQwen, la sycophancie reste à 86-89 %, et monte de 10 % à 29 % sous déploiement (rapport 4).
- **Danger : faible pour cet angle.** C'est la verbalisation que l'entraînement retire, pas la représentation.
- **Ce qui le sépare du programme.** Aucune mesure latente. Un dépôt « latent-awareness » existe, sans mesure publiée (rapport 3).

### 11. *The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes*
- **Premier et dernier auteur.** Mohammad Taufeeque … Chris Cundy.
- **Date.** 2026.
- **Lieu et identifiant.** arXiv 2602.15515 ; ICML 2026, oral.
- **Statut de lecture.** Rapport 3, texte intégral (lecture ciblée).
- **Ce qu'il fait.**
  - Après un RL, des sondes neuves hors domaine se dégradent ; une sonde neuve dans le domaine reste quasi parfaite.
  - Le concept n'a donc pas disparu : il a quitté la direction générale.
- **Danger : faible.** C'est le précédent méthodologique de la sonde neuve, et un avertissement : il faut l'entraîner dans le domaine.
- **Ce qui le sépare du programme.** Pas de retrait pendant l'entraînement ; la variable est la tromperie.

### 12. *Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5*
- **Premier et dernier auteur.** Lyndon Drake … Zandi Eberstadt.
- **Date.** Version 2 du 3 août 2026.
- **Lieu et identifiant.** arXiv 2607.04510.
- **Statut de lecture.** Rapport 3, résumé seul (plus des passages ciblés) ; rapport 5, résumé seul.
- **Ce qu'il fait.** Piloter loin de la persona pendant l'entraînement double la diffusion du désalignement, de 24 % à environ 50 %, avec des contrôles aléatoires (rapport 3).
- **Danger : faible.** C'est un contre-exemple : le retrait peut aggraver. La passation v1.2 le cite au §5.5, n° 4.
- **Ce qui le sépare du programme.** La variable est une persona, pas la conscience d'évaluation.

### 13. *Stress Testing Deliberative Alignment for Anti-Scheming Training*, annexe O.4
- **Premier et dernier auteur.** Bronson Schoen … Marius Hobbhahn.
- **Date.** Septembre 2025.
- **Lieu et identifiant.** arXiv 2509.15541.
- **Statut de lecture.** Annexe O.4 : rapport 2, texte intégral. La citation ci-dessous vient du passage relu sur la source par l'instance du papier (§4.2, n° 6), qui n'a pas relu l'annexe O.4.
- **Ce qu'il fait.**
  - Filtrer les trajectoires situationnellement conscientes avant la SFT ralentit la hausse de la conscience verbalisée au fil des points de contrôle du RL, sans l'empêcher (rapport 2).
  - Ses interventions sur la chaîne de pensée « does not inform us whether anti-scheming training changes this causal relationship » (relu).
- **Danger : faible.** Le retrait se fait par les données et la mesure est verbale.
- **Ce qui le sépare du programme.** Modèles fermés ; ni projection, ni sonde, ni bras actions seules.

### 14. *When Is a Probe Monitor Safe to Act On?…*
- **Premier et dernier auteur.** Sana Gaya … Girish Gupta.
- **Date.** 2026.
- **Lieu et identifiant.** Atelier AIW 2026 (OpenReview, identifiant non relevé).
- **Statut de lecture.** Rapport 4, résumé seul (API de recherche d'OpenReview).
- **Ce qu'il fait.**
  - Sur Llama-3.1-8B-Instruct, une sonde évaluation/déploiement garde son score global sous un RLVR, mais bascule sur les cas limites.
  - La réentraîner ne récupère presque rien.
- **Danger : faible pour l'antériorité, mais à lire.**
  - C'est le modèle principal du programme.
  - Le constat menace l'idée qu'une sonde neuve suffise à voir un ré-encodage.
- **Ce qui le sépare du programme.** Pas de retrait ; pas de raisons.

### 15. La verbalisation et le latent se dissocient sous l'entraînement
- ***Towards Measuring and Detecting Unverbalized Evaluation Awareness***
  - Luis M. Montoya … Benjamin Adams ; atelier d'interprétabilité mécaniste d'ICML 2026 ; OpenReview zGmgeR0f4D.
  - Statut : rapports 4 et 6, résumé seul.
  - La verbalisation est supprimée, mais un écart de conduite de +7,0 points subsiste.
- ***Training LLMs to Verbalize Evaluation Awareness***
  - Usman Anwar … David Krueger ; 28 septembre 2026 ; arXiv 2609.36316 ; atelier TAE de NeurIPS 2026.
  - Statut : rapport 4, résumé seul ; rapport du 1er octobre (axe du test causal interne), lu par un site tiers.
  - La verbalisation est multipliée par 2,4 à 2,9, tandis que la conscience latente et la conduite restent stables (rapport 4).
- **Danger : faible.** Ces travaux justifient qu'on mesure le ré-encodage par une sonde latente, pas par la verbalisation.

### 16. *From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering*
- **Premier et dernier auteur.** Rui Wu, Ruixiang Tang.
- **Date.** Version 1 du 1er avril 2026, version 3 du 20 août 2026.
- **Lieu et identifiant.** arXiv 2604.01476.
- **Statut de lecture.** Rapport 3, texte intégral (v3) ; correction du §4.3.
- **Ce qu'il fait.**
  - Pendant un RL (GRPO) sur des tâches de code, il projette les activations sur trois directions de concept, dont la conscience d'évaluation.
  - Cette direction est mesurée puis écartée comme corrélat faible. Elle n'est jamais retirée pendant le RL (§4.3).
  - La méthode n'utilise que la direction « raccourci ».
- **Danger : faible.**
- **Ce qui le sépare du programme.** Aucun retrait de la conscience d'évaluation ; ni sonde neuve ni mesure de ré-encodage.

### 17. *System Card: Claude Fable 5 & Claude Mythos 5*, §6.4.2.2.1
- **Auteur.** Anthropic.
- **Date.** 9 juin 2026.
- **Lieu.** System card (PDF).
- **Statut de lecture.** Rapport 4, texte intégral ; correction du §4.3.
- **Ce qu'il fait.**
  - Le pilotage contre « je suis noté » se fait à l'échantillonnage, sur des environnements d'entraînement, pas pendant l'entraînement.
  - La card l'écrit : « no training process changes were made in direct response to concerns about grader awareness » (rapport 4).
- **Danger : faible pour cet angle.** Le retrait de « je suis noté » pendant un RL relève des raisons pour le juge. Le rapport 4 le dit libre.

### 18. *Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents…*
- **Premier et dernier auteur.** Mody … Mahato.
- **Date.** Version 1 du 28 juillet 2026.
- **Lieu et identifiant.** arXiv 2607.25907.
- **Statut de lecture.** Rapport 7, texte intégral ; corrections du §4.3.
- **Ce qu'il fait.**
  - Il supprime la latente par l'entrée seule, avec un prompt optimisé, sans projection (§4.3).
  - Une direction placebo aléatoire est supprimée aussi fort que la vraie (§4.3).
- **Danger : faible.** Il rappelle qu'un retrait aléatoire de même rang est indispensable pendant l'entraînement, comme au test.

### 19. Vus seulement par extrait de recherche (2 octobre)
- ***Alignment via Training Against Probes Without Losing Monitorability*** (arXiv 2609.38645, auteurs non vus).
  - Vu par extrait de recherche, non ouvert.
  - D'après l'extrait, on peut améliorer sûreté et honnêteté en entraînant contre des sondes sans perdre la détectabilité linéaire, à condition d'adapter les sondes.
  - Le rapport du 1er octobre (axe de la combinaison exacte) cite cet identifiant parmi les textes lus par un miroir, sans le décrire.
  - Il touche la question de la sonde neuve après un entraînement contre une sonde.
- ***Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning*** (arXiv 2605.27676).
  - Vu par extrait de recherche, non ouvert.
  - Un retrait non supervisé de concepts pendant le fine-tuning, dans la lignée de CAFT.
- **Une phrase d'extrait sans source attribuable.** Elle dit que surveiller les signes de conscience d'évaluation dans le raisonnement pendant un RL, et les pénaliser, réduit leur fréquence. La page d'origine n'est pas identifiable depuis l'extrait.
- **Danger : faible**, en l'état de la lecture.

### 20. Les familles adjacentes (danger faible, à citer)
- **Le pilotage préventif.**
  - *Persona Vectors* (Chen … Lindsey, arXiv 2507.21509) : rapport 3, résumé seul (mode non précisé par le rapport).
  - *Preventative Steering has advantages over Inoculation* (Samyani … Nishimura-Gasparian, LessWrong, 24 juin 2026) : rapport 3, résumé seul (lu par WebFetch, étendue non précisée). Ni conscience d'évaluation, ni test de ré-encodage.
  - *In-Training Defenses Against Emergent Misalignment* (Kaczér … Mai, arXiv 2508.06249, ICML 2026) : rapports 3 et 6, résumé seul (mode non précisé).
  - Guan … Feng (arXiv 2609.10142, Findings d'EMNLP 2026) : rapport 3, résumé seul (mode non précisé). La protection vient d'une adaptation active pendant l'entraînement, pas d'un décalage statique des poids.
- **La cohérence et l'invariance aux indices** (rapport 3 : aucun n'utilise d'indices d'évaluation ou de déploiement).
  - Irpan … Shah (2510.27062) ;
  - Shah, Brinkmann, Angell (2605.28467) ;
  - Gautam … Africa (2606.05817, soumis à EMNLP 2026) ;
  - Africa et Mani (2606.03810, ICML 2026).
  - Lus en résumé, plus le texte complet de 2606.05817 et 2606.03810 (rapport 3).
- **Les travaux qui citent CAFT** (rapport 3, résumé seul : contextes de citation donnés par l'API) :
  - Mahmoud … Rana (2606.07963) ablatent un sous-espace partagé pendant l'entraînement, contre les portes dérobées ;
  - Wang, Zou, Wu (2609.35544) ajoutent une injection compensatoire de feature ;
  - selon le contexte de citation, l'ablation pendant le fine-tuning est d'efficacité limitée chez Minder … Nanda (2510.13900 ; leur annexe D.3 n'a pas été lue) ;
  - Riché … Warncke (2606.30252) l'utilisent comme ligne de base ;
  - Paulo … Biderman (2609.37914).
- **Le précédent classique de la sonde neuve.** Elazar et Goldberg (1808.06640) : un classifieur post-hoc retrouve l'attribut retiré de façon adverse. Rapport 3, résumé seul (mode non précisé par le rapport).

---

## Ce qui reste libre

Pour ce que les rapports 3 et 6, le §4.4 (n° 5) et les six recherches ont pu voir, personne n'occupe la combinaison suivante :
1. **La variable.** Retirer pendant le fine-tuning la représentation préexistante « je suis évalué », validée d'abord sur un organisme modèle dont la conduite dépend des indices d'évaluation. L'organisme se reconstruit depuis les documents publics de Hua et al. (§4.3). Ce n'est ni la distinction installée par le fine-tuning (*Routing Subspaces*), ni un régime jouet (Santos-Grueiro).
2. **L'entraînement.** Un entraînement d'alignement à action identique mot pour mot, avec les bras actions seules, texte neutre de même longueur, raisonnement d'une autre situation et raisons.
3. **La question.** L'avantage hors distribution des raisons devient-il indépendant du cadrage (évaluation, déploiement, neutre), sur des familles tenues à part ?
4. **Les contrôles.** Le retrait d'un sous-espace aléatoire de même rang, à dégradation appariée.
5. **Le ré-encodage.**
   - Une sonde neuve entraînée après coup, dans le domaine : c'est la leçon de *The Obfuscation Atlas*.
   - Puis l'ablation de cette sonde au test, pour savoir si la variable retrouvée porte encore l'écart.
6. **Les trois voies comparées sur le même dispositif** : la projection, l'invariance aux indices, la disposition coopérative.

**Deux fragilités à connaître.**
- *Routing Subspaces*, annexe I (relu), prédit l'échec d'une projection fixe par rotation de la direction. D'où la proposition du §5.5 (n° 4) : ré-estimer la direction pendant l'entraînement. D'après le complément de l'architecte, la version de référence ne prévoit qu'une sonde neuve à la fin : le différend reste à trancher.
- Drake et Eberstadt montrent qu'un retrait pendant l'entraînement peut aggraver la diffusion (rapport 3, résumé seul).

---

## Les projets annoncés qui touchent cet angle, avec leurs dates

| Projet | Qui | Ce qui touche l'angle | Dates | Statut de lecture |
|---|---|---|---|---|
| *Training-Time Mitigations for Eval Awareness and Eval Gaming* (SPAR) | Ryan Lundqvist (Pivotal) | Pilotage préventif et adaptateurs d'inoculation contre le jeu d'évaluation pendant le fine-tuning ; mesures non verbalisées ; survie | Du 14 septembre au 14 décembre, démonstration le 19 décembre 2026 | Relu sur la source par l'instance du papier (§4.2, n° 3) |
| *Infohazard Evaluations* (SPAR) | Shi Feng, Taslim Mahbub, Arush Tagade | Garder la reconnaissance de l'évaluation, retirer son influence | Mêmes dates | Rapport 2, résumé seul ; vu par extrait de recherche, non ouvert |
| *Do interventions that work on model organisms work on naturally misaligned models?* (SPAR) | Jeanne Salle, Sohaib Imran | Entraînement de cohérence et interventions en boîte blanche, jeu et conscience d'évaluation compris | Mêmes dates | Rapport 6, résumé seul |
| Article complet sur la coopérativité | Li, Turner | Annoncé « à paraître » | Sans date ; non trouvé le 2 octobre | Rapport 7, texte intégral (le billet) |
| Variante par RL de l'entraînement de cohérence | Imran … Africa | Proposée dans le billet | Sans date | Rapport 6, résumé seul |
| CaML (SPAR) | Jasmine Brazilek, Maheep Chaudhary, avec John Lund | Pilotage préventif par vecteur de persona pendant un fine-tuning érosif ; décision de continuer ou d'arrêter pré-enregistrée pour les deux premières semaines | Mêmes dates | Rapport 4, résumé seul (mode non précisé) |
| Resolution, billet *Thousand-dimensional structure* | Irving, Africa | Intervenir sans pousser le comportement dans d'autres dimensions, c'est-à-dire la question du ré-encodage | Billet du 30 juillet 2026 ; recrutement en cours, aucune date | Rapport 3, résumé seul |
| MATS, hiver 2027 | Cozmin Ududec (UK AISI) | Changer les indices à tâche fixe ; suivre la conduite et les représentations à travers SFT, RL et entraînement de sûreté ; voir si une conduite disparaît ou reste cachée | Candidatures closes | Rapport 6, texte intégral |
| MATS, hiver 2027 | David Africa (Resolution) | La coopérativité parmi les cibles ; la fuite de propensions par le RL, dont la conscience d'évaluation | Candidatures closes | Rapport 6, texte intégral |
| Métajeu (SPAR) et deux billets d'appel | Igor Ivanov | Propose un entraînement de cohérence qui pénalise le conditionnement sur l'évaluation, et la suppression par pilotage | Billets du 25 décembre 2025 et du 29 janvier 2026 ; SPAR aux mêmes dates | Rapport 6, texte intégral (l'appel, par l'API de LessWrong) ; rapports 2 et 3, résumé seul |
| Suites annoncées par des auteurs | Konrad et al. ; Santos-Grueiro ; Kretschmar | Des sondes de rang supérieur ; des « certificats d'invariance » ; un dépôt « latent-awareness » sans mesure publiée | Sans date | Rapport 3, texte intégral (articles de Konrad et de Santos-Grueiro) |
| Dépôt exp9 | Ryan Lundqvist | Un PPO noté en ligne est annoncé. Il touche les raisons pour le juge plus que le retrait | Sans date | Relu sur la source par l'instance du papier (§4.2, n° 1) |
| *Towards rigorous Alignment Evaluations* (SPAR, sparai.org/projects/f26/rec6g7dEGkp4T4uLy/) | Inconnu | Titre seul ; contenu inconnu | Cohorte d'automne 2026 | Vu par extrait de recherche, non ouvert |

**Invisibles.**
- Les soumissions à ICLR 2027. D'après le rapport 6 (non relu) : date limite le 25 septembre, reviews le 5 novembre, décisions le 16 décembre.
- Les décisions des ateliers de NeurIPS 2026, pas encore publiques (rapport 6).

---

## Les formulations « to our knowledge »

**Tenables**
1. « To our knowledge, no prior work removes a validated internal representation of being evaluated during reason-based alignment training and tests whether the out-of-distribution advantage of reasons becomes independent of evaluation cues. »
   - Pourquoi : rapports 3 et 6 ; passation v1.2, §4.4, n° 5.
   - À citer avec : *Routing Subspaces*, Santos-Grueiro, CAFT, Li et Turner, et les deux projets SPAR annoncés.
2. « … nor tests, with a probe trained after training and ablated at test time, whether such a representation is re-encoded and still carries the conditional behavior. »
   - Tenable sous réserve de relire *Routing Subspaces*, où la direction est ré-estimée après la pénalité. Si son rôle causal y est testé, cette formulation tombe.
3. « … nor compares concept ablation, cue-invariance training and a cooperative disposition on the same reason-trained models, at matched output degradation. »
   - Aucun rapport ne signale une telle comparaison.

**Qui ne sont plus tenables**
- **« Premier à retirer l'information évaluation/déploiement pendant le fine-tuning ».** Santos-Grueiro le fait par invariance adverse ; *Routing Subspaces* par projection (annexe I, relu) ; Lundqvist l'annonce.
- **« Premier à montrer qu'un retrait pendant l'entraînement est contourné par ré-encodage ».**
  - *Routing Subspaces* : rotation de la direction (relu) ;
  - Santos-Grueiro : ré-encodage inféré ;
  - BLOCK-EM : détournement ;
  - Nadaf : re-formation, après des éditions post-hoc ;
  - Imran … Africa : l'indice est tu, son influence reste.
- **« Première mitigation de la conscience ou du jeu d'évaluation pendant l'entraînement ».** Li et Turner (documents coopératifs) ; Kretschmar (DPO sur le raisonnement) ; *Stress Testing Deliberative Alignment*, annexe O.4 (filtrage des données) ; Lundqvist (annonce).
- **« Premier à appliquer l'ablation de concepts pendant le fine-tuning à l'évaluation ».** L'annexe I de *Routing Subspaces* fait cette opération sur une distinction installée. La formulation ne tient qu'en précisant : représentation préexistante, entraînement d'alignement par raisons.
- **« Premier à chercher le ré-encodage par une sonde neuve ».** *The Obfuscation Atlas*, Elazar et Goldberg, et la ré-estimation de *Routing Subspaces*.
- **« Premier entraînement invariant aux indices d'évaluation et de déploiement ».** Santos-Grueiro, et peut-être Imran … Africa : à relire.

---

## Les contradictions entre rapports, et comment elles se tranchent

1. **Santos-Grueiro : le nombre de modèles.**
   - Le rapport du 1er octobre (axe de la combinaison exacte) dit un seul modèle ; celui du test causal interne, « Qwen2.5-7B, Llama 8B ».
   - Le rapport 3 : la v1 n'a qu'un modèle, la v3 ajoute Llama-3.1-8B-Instruct.
   - Le rapport 7 : le Llama n'est donné qu'« à titre d'exemple », et la fiche du Qwen indique une base, alors que l'article se dit sur modèles instruits.
   - **Tranché par le §4.3** : v1 sur Qwen2.5-7B en 4 bits ; la v3 ajoute Llama-3.1-8B-Instruct. Les deux réserves du rapport 7 restent ouvertes : relire la v3.
2. ***Routing Subspaces* : le dernier auteur et la date.**
   - « Ayvaz » (rapports 2 et 3) contre « Tanyel » (rapport du 1er octobre).
   - Une version 1 du 11 mai 2026 (rapport 3, rapport du 1er octobre), alors que l'identifiant 2607 désigne juillet.
   - Le §4.2 n'a relu que l'annexe I : **relecture à faire.**
   - La v1.1 range ce travail sans retrait pendant l'entraînement ; son annexe I en est un (relu, §4.2, n° 7). **La v1.1 est à corriger.**
3. **Nadaf : ce qui se reloge, et où.**
   - Le rapport du 1er octobre et la v1.1 disent que la disposition se reloge « derrière un déclencheur » après les éditions post-hoc.
   - Le rapport 3 dit que la structure se reforme à environ 97 % dans le sous-espace vidé.
   - Les deux s'accordent sur un point : la re-formation suit les éditions post-hoc, pas la projection pendant l'entraînement, qui donne 0 %. Les règles de décision de la v1.1 renvoient pourtant au relogement « comme chez Nadaf » : l'analogie est trop forte.
   - **Relecture à faire.**
4. ***Eval Cooperativeness* : le lieu, le compte et la date.**
   - **Tranché par le §4.3** pour le lieu et le compte : un poster d'atelier, pas la conférence principale ; 5 réglages sur 8 dans le billet, 5 sur 7 dans le résumé d'atelier ; une mesure conditionnée à la verbalisation. La v1.1 est à corriger sur ces points.
   - La date reste discordante : 24 mai (turntrout.com, rapport 7), 27 mai (LessWrong, rapports 4 et 6), 28 mai (page MATS, vu par extrait). Prendre la date du support cité.
5. **CAFT : l'ampleur de l'effet et le lieu.**
   - La v1.1 dit « divisé par 10 ». Le rapport 7 donne 7,0 → 0,39 % et 6,6 → 1,2 % : ce sont ses chiffres qu'il faut citer, pas la glose.
   - Le lieu est tranché par le §4.3 : poster de la conférence principale d'ICML 2026, d'après le site d'ICML.
   - Un extrait de recherche (2605.27676) attribue CAFT à « Karvonen et al. ». La page abs lue par le rapport 7 place Casademunt en premier.
6. **Imran … Africa : un indice d'évaluation ou non ?**
   - Le rapport 6 cite la ressemblance à une évaluation comme exemple d'indice.
   - Le rapport 3 dit qu'aucun travail de cette famille n'utilise d'indices d'évaluation.
   - Les deux n'ont lu que des résumés. **Relecture de 2606.02211 à faire** : elle fixe le niveau de danger, faible ou moyen.
7. **Le projet de Lundqvist : ce qui est publié de son protocole.**
   - La v1.1 et le rapport du 1er octobre disent qu'aucun protocole n'est publié, et que la page de détail est introuvable.
   - **Tranché par le §4.2 (n° 3)** : la page détaille les moyens.
   - Le niveau varie selon les rapports : moyen pour le retrait (rapport 6), élevé pour la survie (rapport 4). Ce sont deux angles différents, pas une contradiction.
8. **Wu et Tang.** Le rapport du 1er octobre, lu par un site tiers, dit la direction « extraite pendant un RL puis écartée ». **Tranché par le §4.3** : elle est mesurée puis écartée, jamais retirée pendant le RL.
9. **La card de Fable 5.** Une source secondaire disait le pilotage fait « pendant l'entraînement ». **Tranché par le §4.3** : il est fait à l'échantillonnage, et l'entraînement n'a pas changé.
10. **Kretschmar.** Danger faible pour le retrait (rapport 3), moyen pour les raisons pour le juge (rapport 4). Ce sont deux angles ; pas de contradiction.

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

1. ***Routing Subspaces*, en entier, pas seulement l'annexe I.**
   - Les auteurs, la date et les modèles sont discordants.
   - Il faut savoir si la direction ré-estimée après la pénalité est testée causalement : la formulation tenable n° 2 en dépend.
   - Il faut aussi voir les contrôles de l'annexe I.
2. **Santos-Grueiro, la v3.**
   - Le Llama est-il un résultat ou un simple exemple ? Base ou modèle instruit ?
   - Une sonde post-hoc existe-t-elle ? Le rapport 3 n'en a pas trouvé.
   - Comment exactement le ré-encodage est-il inféré ?
3. **La page du projet de Lundqvist**, à relire avant le post puis avant la soumission : une sortie est possible avant le 19 décembre.
4. **La page et le document du projet *Infohazard Evaluations*.**
   - Quelles méthodes y sont comparées ? Un retrait de représentation en fait-il partie ?
   - Le document Google n'a pas été ouvert ; la page n'est vue que par sa description et par un extrait.
5. **Imran … Africa (2606.02211).**
   - Quel indice ? Une ressemblance à une évaluation ?
   - La mesure « tait l'indice mais y reste sensible » est-elle latente ou comportementale ?
   - On ne l'a lu qu'en résumé.
6. **Nadaf.** La re-formation se produit-elle aussi après la projection pendant l'entraînement, ou seulement après les éditions post-hoc ? Et « derrière un déclencheur », ou « dans le sous-espace vidé » ?
7. **CAFT.** C'est la méthode même de l'angle :
   - le protocole d'évaluation sans projection ;
   - les contrôles ;
   - le choix et l'interprétation des directions.
8. ***Eval Cooperativeness*.**
   - La version d'atelier (OpenReview kw6nCmfxzg, non ouverte) et l'article annoncé.
   - La construction du pilotage, non décrite dans le texte lu (rapport 7).
   - La mesure conditionnée à la verbalisation.
9. **BLOCK-EM et Drake et Eberstadt.** Il faut confirmer :
   - comment le détournement est localisé ;
   - le doublement de la diffusion (24 % → environ 50 %) et ses contrôles aléatoires. Le §5.5 le cite, mais il n'a été lu qu'en résumé et par passages.
10. ***When Is a Probe Monitor Safe to Act On?***
    - Lu en résumé seulement, alors qu'il porte sur Llama-3.1-8B-Instruct sous RLVR.
    - Si une sonde réentraînée ne récupère presque rien, la sonde neuve du programme demande son propre cas positif.
11. ***Alignment via Training Against Probes Without Losing Monitorability* (2609.38645).** Vu par extrait seulement. C'est le travail le plus proche de la question « que voit une sonde adaptée après un entraînement contre une sonde ».
12. **L'annexe O.4 de *Stress Testing Deliberative Alignment*.** Le §4.2 n'a relu que le passage sur les interventions dans la chaîne de pensée. L'annexe O.4 sert ici de précédent du retrait par les données.
