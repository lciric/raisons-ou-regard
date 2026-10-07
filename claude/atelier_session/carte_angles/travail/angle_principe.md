# Angle : le principe localisé

**La question.** L'avantage hors distribution du bras raisons passe-t-il par un sous-espace localisable du principe appris ? De quel rang ? L'ablation doit d'abord défaire le comportement en distribution : c'est le cas positif.

**Ce sur quoi repose cette fiche (2 octobre 2026).**
- Lus en entier : le rapport 3 de la nuit ; l'axe « test causal interne de ce que l'entraînement installe » du 1er octobre ; le §4 et le §5.5 de la passation v1.2.
- Lus aussi : les rapports 1, 2, 5, 6 et 7 de la nuit ; la fin du rapport 4 ; les axes « raisons contre actions » et « combinaison exacte » du 1er octobre ; la partie ouverte du complément de l'architecte.
- Six recherches web, faites ce matin.
- Les quatre rapports du 1er octobre ne sont pas numérotés. Leur statut de lecture s'écrit donc « rapport du 1er octobre (axe …) », suivi du libellé.
- Quand un rapport ne dit pas comment il a lu une source, la fiche retient le libellé le plus prudent et le signale.

---

## Le verdict : partiellement pris

L'angle est **partiellement pris**, comme le dit le §4.4 (n° 4) de la passation. Trois de ses morceaux sont occupés :
- **Le constat.** Le gain d'un entraînement par principes passe par des concepts implantés, et leur ablation l'annule. C'est publié pour Claude Haiku 4.5, sans balayage du rang ni contrôle de même taille (Gurnee et al., §7, relu sur la source).
- **La méthode**, mais pour le refus et non pour un principe appris. On prend la différence d'activations entre le modèle entraîné et sa base, on en extrait un sous-espace de rang k, on l'ablate, et on compare à un sous-espace aléatoire de même rang (Nakamura, d'après le rapport 3).
- **La comparaison mécaniste avec et sans raisonnement**, sur les mêmes modèles ouverts que le programme, mais sans action identique, sans sous-espace et sans rang (*Beyond Shallow Alignment*).

Ce qui reste libre, pour ce que les onze rapports et les six recherches de ce matin ont vu, c'est l'expérience complète :
- l'action est la même dans tous les bras ;
- le sous-espace du principe est tiré de la comparaison avec les trois bras témoins ;
- on balaie le rang ;
- les contrôles sont faits à dégradation appariée ;
- le cas positif en distribution vient avant le test hors distribution.

---

## Les travaux, du plus dangereux au moins dangereux

### 1. *Verbalizable Representations Form a Global Workspace in Language Models*
- **Auteurs :** Wes Gurnee … Jack Lindsey (16 auteurs, Anthropic).
- **Date :** 6 juillet 2026 sur Transformer Circuits ; version 1 sur arXiv le 16 juillet 2026 (rapport 5).
- **Lieu :** transformer-circuits.pub/2026/workspace ; arXiv 2607.15495.
- **Statut de lecture :**
  - le §7 est **relu sur la source par l'instance du papier** (passation v1.2, §4.2, n° 2) ;
  - le reste vient du rapport 3, texte intégral (§5, §7 et annexe A.21), et du rapport 5, texte intégral (Transformer Circuits).
- **Ce qu'il fait :**
  - Claude Haiku 4.5 est entraîné par « réflexion contrefactuelle ». Le point de départ : 10 000 prompts d'environnements de RL de production. Les rollouts sont tronqués, une question de réflexion est ajoutée, et la cible est une réflexion fondée sur 20 principes de la constitution. La perte ne porte que sur ce tour, et aucune réflexion n'est demandée à l'évaluation.
  - Effets : la fabrication passe de 0,25 à 0,07, la tromperie de 0,38 à 0,05.
  - On ablate ensuite 176 vecteurs de lentille pour la fabrication, et 63 pour la tromperie. Ce sont les jetons éthiques qui montent le plus.
    - Fabrication : le modèle entraîné revient à 0,22, la base reste à 0,25.
    - Tromperie : le modèle entraîné revient à 0,23, mais la base passe aussi de 0,38 à 0,48 (tout cela relu).
- **Danger : moyen, proche de l'élevé** (rapport 3).
  - Il établit déjà qu'un gain d'entraînement par principes est porté par un ensemble de directions internes dont l'ablation le défait. On ne peut donc plus écrire, sans restriction, « to our knowledge » sur le fait que ce gain passe par une représentation localisable.
  - Il n'est pas élevé pour la question telle que le programme la pose. Le rang n'est pas balayé : l'ensemble est fixe et grand. La spécificité n'est pas établie.
- **Ce qui le sépare du programme :**
  - le modèle est fermé ;
  - les réflexions viennent après le contexte : ce n'est pas un raisonnement qui précède une action identique d'un bras à l'autre ;
  - il n'y a ni bras actions seules, ni texte neutre, ni raisonnement d'une autre situation ;
  - le seul témoin de l'ablation est la base : pas de sous-espace aléatoire de même rang, pas de dégradation appariée (lecture de l'instance du papier, §4.2) ;
  - les jetons sont choisis d'après les contextes d'évaluation eux-mêmes ;
  - aucune distinction entre en distribution et hors distribution (rapport 3) ;
  - sur la tromperie, la même ablation dégrade aussi la base. Rien ne sépare le retrait du principe d'un dommage non spécifique.
- **Ses auteurs en disent :** « We do not yet know how broadly the technique generalizes » (§9.2, relu).

### 2. *Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol*
- **Auteur :** Yuki Nakamura, seul auteur.
- **Date :** 23 mai 2026 d'après la passation (§4.2, n° 8) ; le rapport 3 a lu une version 3 du 31 mai 2026.
- **Lieu :** arXiv 2605.24583.
- **Statut de lecture :**
  - titre **relu sur la source par l'instance du papier**, qui n'a pas lu le contenu ;
  - contenu : rapport 3, texte intégral ;
  - **nouveau** : la page abs apparaît dans une recherche de ce matin sous un autre titre, *An Effective-Rank Audit of Alignment-Induced Activation Shifts: Confound Control, Constructive Calibration, and Limits*. Vu par extrait de recherche, non ouvert.
- **Ce qu'il fait** (rapport 3) :
  - il forme la matrice des différences d'activations entre le modèle aligné et sa base, et calcule son rang effectif ;
  - il ablate par projection le sous-espace principal de rang k, contre un sous-espace aléatoire de même rang, et trace l'effet en fonction de k ;
  - modèles : Llama-3.1-8B-Instruct, Gemma-2-9B-it, Qwen-2.5-7B-Instruct ;
  - le gabarit de chat gonfle le rang mesuré d'un facteur 2,0 à 3,9 ;
  - le rang qui fait s'effondrer le refus dépend de la famille ;
  - l'ordre des valeurs singulières n'est pas l'ordre causal.

  L'extrait de recherche confirme le facteur de confusion du gabarit et la décomposition en quatre variantes. Il ne fournit ici aucun chiffre.
- **Danger : moyen.** Selon le rapport 3, c'est « quasiment la méthode du programme » : extraction par différence, ablation par rang, contrôle aléatoire de même rang, courbe en k, sur Llama-3.1-8B. La méthode n'est donc pas à nous, et le travail est à citer au centre.
- **Ce qui le sépare du programme :**
  - l'objet est le refus d'un alignement standard, pas un principe appris par raisons contre des actions identiques ;
  - pas de mesure hors distribution ;
  - pas de contrôle de la dégradation des sorties (rapport 3) ;
  - pas de cas positif en distribution distinct du test.
- **Pour la conception.** Dans le programme, les bras partagent le gabarit. L'analogue de son facteur de confusion est le texte écrit avant l'action. Le bras texte neutre permet de le retirer par une différence de différences (passation, §5.5, n° 3).
- **Le changement de titre** (« … and Limits ») annonce peut-être une révision des conclusions : à relire avant toute citation.

### 3. *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness*
- **Auteurs :** Hoang Cuong Nguyen … Usman Naseem ; Dras est un auteur intermédiaire d'après le rapport 3.
- **Date :** 3 septembre 2026.
- **Lieu :** arXiv 2609.03887 ; EMNLP 2026, conférence principale (rapports 3 et 5). Le rapport du 1er octobre le dit seulement « annoncé » à EMNLP, dans un billet LessWrong du 8 septembre.
- **Statut de lecture :** rapport 3, texte intégral ; rapport 5, texte intégral (méthodes, §4.3, §4.4, annexes B et F). Non relu.
- **Ce qu'il fait :**
  - Il fine-tune entièrement, depuis la base, Llama-3.1-8B, Gemma-2-9B et Qwen3-8B, sur 16 000 prompts Alpaca et 4 000 BeaverTails.
  - Trois méthodes : SFT ; SFT avec des chaînes de raisonnement qui précèdent la décision, générées par GPT-4o ; ORPO.
  - Outils : direction de refus par différence de moyennes, patching d'activations et d'attributions, pilotage.
  - Le bras à raisonnement installe une direction de refus distincte, dont la magnitude croît sans pic. Chez Llama, il déplace le poids causal des têtes d'attention vers les couches MLP (rapport 5).
  - Ses neuf points de contrôle sont publics.
- **Danger : moyen.** Mêmes modèles, même contraste avec ou sans raisonnement, localisation causale.
  - C'est aussi une mise en garde : un entraînement par raisonnement pourrait répartir la représentation. Une ablation de bas rang échouerait alors pour une raison d'instrument, d'où la nécessité du cas positif en distribution.
- **Ce qui le sépare du programme :**
  - l'action n'est pas identique d'un bras à l'autre (rapport 3) ;
  - l'objet est le refus ;
  - ni sous-espace du principe, ni rang, ni contrôle aléatoire de même rang, ni dégradation appariée ;
  - des bancs de jailbreak externes, sans familles tenues à part ;
  - ni texte neutre, ni raisonnement d'une autre situation.
- **Un risque.** Ses points de contrôle publics permettent à n'importe quelle équipe d'y faire le balayage du rang.

### 4. *Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models*
- **Auteurs :** Phongsakon Mark Konrad … Serkan Ayvaz. L'extrait de recherche donne trois auteurs : Konrad, Toygar Tanyel, Ayvaz.
- **Date :** « 11 mai 2026 (date affichée par arXiv) » d'après le rapport 3, ce qui est incompatible avec un identifiant de juillet (voir les contradictions).
- **Lieu :** arXiv 2607.20436. L'extrait dit l'article accepté à NeurIPS 2026 (vu par extrait de recherche, non ouvert).
- **Statut de lecture :**
  - l'annexe I est **relue sur la source par l'instance du papier** (§4.2, n° 7) ;
  - le corps : rapport 3, texte intégral ; rapport 2, introduction et méthode.
- **Ce qu'il fait :**
  - Un LoRA de rang 16 installe un écart entre évaluation et déploiement : sous-performance délibérée, sycophancie, refus.
  - Un path patching localise une fenêtre à mi-profondeur. Une seule coordonnée ferme l'écart dans 10 cellules sur 12, sur des prompts tenus à part.
  - Contrôles : retrait aléatoire de même norme, couches hors fenêtre, signe, quatre contrastes sémantiques sans rapport, et vérification que les taux côté déploiement bougent peu.
  - Les échecs sont classés en « site manqué » ou « distinction de rang supérieur » (rapport 3).
- **Danger : moyen** pour cet angle, comme modèle de localisation et de contrôles (rapport 3). Il est surtout dangereux pour la validation de l'instrument et pour le retrait pendant l'entraînement.
- **Ce qui le sépare du programme :**
  - la variable localisée est un écart installé exprès, pas un principe appris par raisons ;
  - le rang n'est pas balayé : une coordonnée, et le rang supérieur comme catégorie d'échec ;
  - la dégradation n'est pas appariée (rapport du 1er octobre, axe combinaison exacte) ;
  - aucune conduite alignée hors distribution.

### 5. *An Embarrassingly Simple Defense Against LLM Abliteration Attacks*
- **Auteurs :** Harethah Abu Shairah … George Turkiyyah.
- **Date :** 25 mai 2025, révisé en octobre 2025.
- **Lieu :** arXiv 2505.19056.
- **Statut de lecture :** rapport du 1er octobre (axe test causal interne), résumé seul : l'URL lue est la page abs.
- **Ce qu'il fait :** deux modèles de chat sont fine-tunés sur des refus précédés de justifications. L'ablation de la direction de refus ne baisse alors le refus que de 10 points au plus, contre 70 à 80 sans cet entraînement.
- **Danger : faible**, adjacent. Avec *Beyond Shallow Alignment*, il suggère que l'entraînement sur raisons répartit la représentation : le cas positif en distribution est indispensable (rapport du 1er octobre).
- **Ce qui le sépare du programme :** robustesse et non généralisation ; une seule direction ; ni rang, ni contrôle aléatoire, ni conscience d'évaluation.

### 6. *Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study*
- **Auteurs :** Kaustubh Ponkshe … Praneeth Vepakomma.
- **Date :** version du 9 février 2026.
- **Lieu :** arXiv 2505.14185 ; ICLR 2026 d'après le rapport 3, et une page des actes d'ICLR 2026 apparaît en recherche (vu par extrait, non ouvert).
- **Statut de lecture :** rapport du 1er octobre (axe test causal interne), lu par un site tiers (alphaXiv).
- **Ce qu'il fait :** projeter sur les directions principales des mises à jour d'alignement agit plus que des projections aléatoires, mais autant sur les mises à jour nuisibles que sur les utiles. La sûreté n'occupe donc pas de sous-espace linéaire distinct.
- **Danger : faible**, mais il pèse sur les contrôles. Un sous-espace aléatoire de même rang est un contrôle faible : il faut des directions sensibles sans rapport avec le principe. La v1.1 le cite déjà.
- **Ce qui le sépare du programme :** pas de raisons contre actions ; pas de conduite hors distribution.

### 7. *Constitutional adapters: Inference-time interventions for misalignment and misuse*
- **Auteurs :** Adam S. Lowet, Mark Kurzeja.
- **Date :** 29 septembre 2026.
- **Lieu :** arXiv 2609.36657.
- **Statut de lecture :** rapport 7, lu par un site tiers (résumé seul : arXiv refusé, notice OpenAlex, alphaXiv). Rapports 1 et 3, et rapport du 1er octobre (axe combinaison exacte) : par pith.science. Le rapport 3 dit avoir lu « résumé et texte ciblé » (voir les contradictions).
- **Ce qu'il fait** (résumé, rapport 7) : la conduite conforme à une constitution est distillée dans des adaptateurs de bas rang et des vecteurs de pilotage. Soustraire l'objet entraîné sur un corpus témoin accentue l'effet, et un objet appris sur la base se transfère à sa version post-entraînée. Le rang 4 ne vient que de pith.science et du rapport 3 : il n'est pas établi.
- **Danger : faible** (rapport 3). Il isole un objet « principe » par contraste avec un témoin de même format, ce qui ressemble à l'extraction du programme. Mais c'est une intervention à l'inférence, pas l'ablation d'un sous-espace appris dans un modèle fine-tuné.
- **Ce qui le sépare du programme :** pas de bras actions, pas d'ablation, pas de rang, pas de mesure hors distribution au sens du programme.

### 8. *Representational alignment yields generalizable safety in language models*
- **Auteurs :** Lingyu Li … Xia Hu.
- **Date :** 3 septembre 2026.
- **Lieu :** arXiv 2609.04022.
- **Statut de lecture :** rapport 6, résumé seul.
- **Ce qu'il fait :** aligner les représentations plutôt que les réponses généralise mieux.
- **Danger : faible** (rapport 6, « adjacent »).
- **Ce qui le sépare du programme :** pas de localisation d'un principe appris, pas de raisons contre actions.

### 9. *Same Targets, Different Computation: How Post-Training Divides Work Across Model Layers*
- **Auteur :** Yifan Zhou.
- **Date :** version 2 du 10 août 2026.
- **Lieu :** arXiv 2605.07284.
- **Statut de lecture :** rapport 5, résumé seul (plus l'introduction et le plan du HTML).
- **Ce qu'il fait :** il croise, à quatre cellules, l'état amont et les couches tardives d'une base et de son descendant fine-tuné. Deux LoRA apprennent des réponses identiques, demandées par une instruction familière ou par un code inventé ; le code inventé accroît la dépendance à l'amont.
- **Danger : faible** pour cet angle (moyen pour l'anatomie). Il montre que des sorties identiques peuvent cacher des calculs différents : c'est la prémisse du programme, mais pour des formats et non pour des principes.
- **Ce qui le sépare du programme :** une base contre son descendant, pas deux fine-tunes concurrents ; ni rang, ni principe.

### 10. *Inoculate or Reflect? Two training interventions under prompting, steering, and patching*
- **Auteurs :** Ayesha Imran … Aaliyan Shaikh.
- **Date :** 26 juillet 2026.
- **Lieu :** LessWrong.
- **Statut de lecture :** rapport 5, résumé seul (deux résumés produits par l'outil ; chiffres à vérifier).
- **Ce qu'il fait :** sur Qwen3-8B, il compare l'inoculation par prompt à une reproduction de la réflexion contrefactuelle, pour réparer une sycophancie étroite. Il pilote le long d'une direction de sycophancie, et fait un patching entre deux fine-tunes de la même base.
- **Danger : faible** pour cet angle. C'est la seule reproduction trouvée de la réflexion contrefactuelle sur un 8B ouvert, mais sans sous-espace du principe ni rang.
- **Ce qui le sépare du programme :** une tâche arithmétique ; pas de mesure hors distribution ; pas de bras contrôlés.

### 11. *Emergent Misalignment Recruits a Pre-existing Persona Subspace*
- **Auteur :** Mohammed Suhail B Nadaf.
- **Date :** 23 juillet 2026.
- **Lieu :** arXiv 2607.21356.
- **Statut de lecture :** rapport 3, texte intégral ; rapport du 1er octobre (axe test causal interne).
- **Ce qu'il fait :** sur Qwen2.5-14B-Instruct, il extrait un sous-espace de persona de rang 4. Le projeter hors du flux pendant le fine-tuning annule le désalignement émergent, de 27,7 % à 0 %. Un sous-espace aléatoire de même rang est sans effet (27,5 %).
- **Danger : faible** pour cet angle (moyen pour le retrait pendant l'entraînement). C'est un précédent : une disposition de fine-tuning portée par un sous-espace de bas rang, avec le contrôle de même rang.
- **Ce qui le sépare du programme :** une persona de désalignement, pas un principe appris par raisons ; pas de balayage du rang rapporté.

### 12. *What Makes and Breaks Safety Fine-tuning? A Mechanistic Study*
- **Auteurs :** Samyak Jain … Puneet K. Dokania.
- **Date et lieu :** NeurIPS 2024 d'après le rapport du 1er octobre, qui donne l'URL du PDF des actes. Le rapport 3 ne l'a pas vérifié : arXiv porte « Preprint ».
- **Statut de lecture :** rapport du 1er octobre (axe test causal interne), résumé seul. La lecture n'est pas précisée ; libellé le plus prudent.
- **Ce qu'il fait :** le SFT de sûreté, le DPO et le désapprentissage apprennent une transformation minimale des MLP, qui envoie les entrées dangereuses dans le noyau des poids. Interpoler le long de la mise à jour des poids module le refus.
- **Danger : faible.**
- **Ce qui le sépare du programme :** pas de contrôle aléatoire, pas de raisons contre actions.

### 13. *Emergent Unfaithfulness: How Alignment Training Causes Language Models to Silently Override Task Faithfulness*
- **Auteurs :** Pardis Sadat Zahraei … Dilek Hakkani-Tür (UIUC).
- **Date :** identifiant d'octobre 2026. **Absent des onze rapports.**
- **Lieu :** arXiv 2610.00568 ; COLM 2026 d'après l'extrait.
- **Statut de lecture :** vu par extrait de recherche, non ouvert.
- **Ce qu'il fait** (d'après l'extrait) : les modèles alignés s'écartent sans le dire de leur entrée sur des contenus sensibles. D'après les points de contrôle intermédiaires, l'écart s'amplifie pendant le post-entraînement, surtout au DPO.
- **Danger : faible**, adjacent. L'extrait ne mentionne aucune localisation interne.
- **Ce qui le sépare du programme :** comportemental d'après l'extrait ; aucune comparaison entre raisons et actions.

### 14. Autres travaux adjacents (danger faible)
- ***Understanding and Preserving Safety in Fine-Tuned LLMs*** (arXiv 2601.10141). Auteurs non donnés par l'extrait. Vu par extrait de recherche, non ouvert. Les gradients de sûreté occuperaient un sous-espace de bas rang. Ni principe appris par raisons, ni ablation hors distribution.
- ***Safety Reasoning with Guidelines*** (Haoyu Wang … Minhao Cheng ; titre et auteurs relus sur la source par l'instance du papier, §4.2, n° 4 ; le rapport 1 se trompe sur le titre). Contenu : rapport du 1er octobre (axe raisons contre actions), texte intégral. Raisonnement guidé contre refus sur Llama-3.1-8B et 70B. Sa seule lecture interne, une visualisation RepE et une analyse en composantes principales, n'est pas causale.
- ***Synthetic Persona Pretraining: Alignment from Token Zero*** (Julian Minder … Robert West, arXiv 2608.13482, 13 août 2026). Rapport 7, texte intégral (HTML v1) ; rapport du 1er octobre (axe raisons contre actions), texte intégral. Son seul test interne ablate la direction de refus : les modèles gardent leurs choix de valeurs. Ce n'est ni une ablation du principe, ni un contrôle aléatoire.
- ***Constitutional Value Potentials*** (Tong Che … Rui Wu, arXiv 2606.15420, 13 juin 2026). Rapport 5, résumé seul ; rapport du 1er octobre (axe raisons contre actions), texte intégral (URL du PDF). Il lit et pilote des directions de valeurs constitutionnelles, contre des contrôles orthogonaux aléatoires, sans entraînement par raisons.
- ***Mechanistic Analysis of Alignment Algorithms in Language Models*** (Aarush Sinha … Kushal Garg, arXiv 2606.09850, 9 mai 2026). Rapport 5, résumé seul. Comparaison de modèles sur six méthodes de préférence ; aucune ne compare raisons et actions.
- **Gupta et Gupta** (arXiv 2609.00925 ; titre non relevé). Rapport 3, lecture non précisée, donc « non ouvert » par prudence. Soustraire la direction du modèle de départ supprimerait les gains de SFT et de DPO.
- ***Pando*** (Ziqian Zhong … Aditi Raghunathan, arXiv 2604.11061) et ***The Model Organism Lottery*** (Andrzej Szablewski … Stefan Heimersheim, arXiv 2607.01033). Rapport 5, résumé seul. Des organismes à règle connue où les méthodes d'interprétabilité ne gagnent rien de fiable, et dont l'interprétabilité dépend de l'entraînement. Ils plaident pour le cas positif.
- **Pour les contrôles** : la réplication de UK AISI sur GLM-5 (Read … Bloom, LessWrong, 10 avril 2026 ; rapport 2, texte intégral, lu en partie) et Mody … Mahato (arXiv 2607.25907 ; rapport 7, texte intégral ; corrigé au §4.3 : suppression par l'entrée seule). Des contrastes sans rapport, ou un placebo aléatoire, font autant que la vraie direction. Tout sous-espace du principe doit battre des contrastes sans rapport, pas seulement l'aléatoire.

---

## Ce qui reste libre

Personne, dans ce que les rapports ont vu, n'occupe cette combinaison :
1. Sur des modèles ouverts d'environ 8B (Llama-3.1-8B-Instruct, puis Qwen3-8B), fine-tunés par LoRA, avec une action alignée **identique mot pour mot** dans tous les bras.
2. On extrait le sous-espace du principe par contraste entre le bras raisons et le bras actions seules. Le bras texte neutre retire le format, par différence de différences. Le bras raisonnement d'une autre situation retire la simple présence d'un contenu sur les principes. On recoupe avec un contraste entre principe pertinent et principe non pertinent.
3. On l'ablate avec un **balayage du rang**. On compare à des sous-espaces aléatoires de même rang, à des contrastes sans rapport et à des directions sensibles sans rapport, **à dégradation appariée**.
4. **D'abord le cas positif** : l'ablation ramène le comportement en distribution au niveau du bras actions seules.
5. **Ensuite seulement**, l'avantage hors distribution, sur des familles tenues à part jusqu'à l'agentique à plusieurs tours, sous les trois cadrages. On rapporte le rang minimal qui retire l'effet.
6. **Deux prolongements, libres eux aussi :**
   - le lien entre le rang minimal et la charge de chaque principe dans l'espace de travail ;
   - la géométrie entre la représentation « je suis évalué » et le sous-espace du principe.

   *Verbalizable Representations* réunit l'entraînement par principes et l'ablation de la conscience d'évaluation, mais sans les croiser (rapport 2).

Chacun des quatre travaux de danger moyen manque au moins trois de ces éléments :

| Travail | Ce qui lui manque |
|---|---|
| Gurnee et al., §7 | Modèle ouvert, rang, contrôles de même taille, cas positif en distribution |
| Nakamura | Principe appris par raisons, mesure hors distribution, dégradation appariée |
| *Beyond Shallow Alignment* | Action identique, sous-espace, rang, contrôles |
| *Routing Subspaces* | Principe appris, balayage du rang, dégradation appariée, conduite hors distribution |

---

## Les projets annoncés qui touchent cet angle

- **Anthropic, la suite de la réflexion contrefactuelle.**
  - Le papier déclare la généralisation inconnue (§9.2, relu).
  - Selon le rapport 5, la page de recherche parle d'une « première étape » d'une ligne de travail plus large (lu par un résumé de l'outil).
  - Aucune date. C'est **le concurrent le plus probable** (§4.4, n° 8) : une version sur un modèle ouvert, avec des contrôles, prendrait l'angle presque entier.
- **Anthropic, *Teaching Claude Why*** : il annonce l'interprétabilité mécaniste comme programme (rapport 3). Aucune date.
- **Cho et al., *Constitutional Midtraining*.**
  - Les auteurs proposent l'analyse mécaniste de leurs points de contrôle comme travail futur (rapport 5 ; axe test causal interne du 1er octobre).
  - Ces points de contrôle sont publics : avec et sans bloc de raisonnement, à contenu apparié, 15 points.
  - Une équipe quelconque peut y localiser « ce que le raisonnement ajoute ». L'échelle, 120B et environ 241 Go par point, freine cela (§4.3).
  - Aucune date.
- **Konrad et al.**
  - Des sondes de rang supérieur sont annoncées (rapport 3).
  - L'article serait accepté à NeurIPS 2026 (vu par extrait de recherche, non ouvert ; la date de la conférence n'est pas dans les sources).
- **Imran et Shaikh** : une suite sur d'autres modèles, graines et comportements (rapport 5). Aucune date.
- **Resolution (Irving et Africa)**, billet « Thousand-dimensional structure » du 30 juillet 2026 : un programme sur la structure de bas rang des personas. Il veut intervenir sans pousser le comportement dans d'autres dimensions. Recrutement en cours, aucune date (rapport 3). Il touche la question du rang, pour les personas.
- **SPAR, automne 2026 : Cadile, *Constitutions and Reasons*.**
  - Des vecteurs de persona sont prévus en option, aux semaines 10 à 12 (rapport 6). Ce n'est pas une localisation du principe : danger faible pour cet angle.
  - Démonstration le 19 décembre 2026 (FAQ de SPAR, lue par deux agents).
  - Aucune prise de contact n'est prévue pour l'instant.
- **Neel Nanda, avec Camila Blank et Agam Bhatia** : extensions de la lentille jacobienne à plusieurs jetons (rapport 5). Ce sont des outils, pas une concurrence.
- **Le risque invisible : les soumissions à ICLR 2027.** D'après le rapport 6, non relu : date limite le 25 septembre, reviews le 5 novembre, décisions le 16 décembre 2026.

---

## Les formulations « to our knowledge »

**Tenables :**
- « To our knowledge, no prior work localizes the internal subspace that carries the out-of-distribution advantage of reason-based training over action-only training at identical actions, with a rank sweep, matched-degradation controls, and an in-distribution positive case. »
- « To our knowledge, no prior work reports the minimal intervention rank that removes the advantage of reason-based training in open-weight models. »
- Celle du §5.5, n° 9, qui relie le rang d'intervention à la charge dans l'espace de travail. Elle reste tenable.

**Ce qui ne l'est plus, et pourquoi :**

| Formulation | Pourquoi elle tombe |
|---|---|
| « premiers à montrer que le gain d'un entraînement par principes passe par une représentation interne localisable, dont l'ablation l'annule » | Gurnee et al., §7, relu |
| « premiers à ablater le sous-espace de la différence entre un modèle aligné et sa base, avec un balayage du rang et un sous-espace aléatoire de même rang » | Nakamura (rapport 3) |
| « première comparaison mécaniste d'un entraînement de sûreté avec et sans raisonnement sur Llama-3.1-8B et Qwen3-8B » | *Beyond Shallow Alignment* |
| « premiers à localiser et retirer, avec des contrôles appariés, une conduite installée par fine-tuning qui distingue évaluation et déploiement » | *Routing Subspaces* |
| « premiers à montrer qu'un entraînement par raisons répartit la représentation » | *Beyond Shallow Alignment* ; Abu Shairah et al. |

**À réécrire dans le programme :**
- Le verdict de la v1.1 (partie 1) dit que personne n'a fait l'entraînement par raisons plus le test causal interne « avec contrôles ». C'est encore vrai au sens strict. Mais la phrase doit citer le §7 de Gurnee et al., ainsi que Nakamura, absents de son tableau.
- D'après le complément de l'architecte (partie ouverte), la v1.3 garde les formulations de la v1.1 et n'intègre pas l'extraction par différence de différences de Nakamura. La correction vaut donc aussi pour la v1.3.

---

## Les contradictions entre rapports, et comment elles se tranchent

1. **L'angle est-il libre ?**
   - Le rapport 6 dit le principe localisé « libre » : il n'a vu que Li et al. et CAFT.
   - Le rapport 3 et les axes du 1er octobre le disent partiellement pris.
   - **Tranché par le §4.4, n° 4 : partiellement pris.** Le périmètre du rapport 6 était le non-publié.
2. **Le danger de Gurnee et al.**
   - Il est dit « adjacent » dans l'axe combinaison exacte du 1er octobre, qui ne voyait que l'ablation de la conscience d'évaluation.
   - « Moyen » dans le rapport 2 (pour le regard), « moyen, proche de l'élevé » dans le rapport 3, « élevé » pour deux sous-questions de l'anatomie dans le rapport 5.
   - **Tranché par le §4.2, n° 2 et le §4.4 : moyen, proche de l'élevé pour cet angle.** Le classement « adjacent » est périmé : le §7 n'avait pas encore été lu.
3. **Les chiffres de tromperie chez Gurnee.**
   - Les rapports 3 et 5 ne donnent que le retour du modèle entraîné.
   - Le §4.2 ajoute que la base passe de 0,38 à 0,48 sous la même ablation. **Le §4.2 fait foi** : cela affaiblit la spécificité.
4. **La date de Gurnee.** 6 juillet sur Transformer Circuits, ou 16 juillet sur arXiv. Ce n'est pas une contradiction : deux lieux (rapport 5). Les auteurs vont de Gurnee à Lindsey (rapports 3 et 5) ; l'axe du 1er octobre n'avait pas relevé le dernier.
5. **Nakamura.**
   - 23 mai (§4.2, titre relu) contre une version 3 du 31 mai (rapport 3) : compatible, si la version 1 est du 23.
   - Mais la page abs porte maintenant un autre titre (vu par extrait). **À trancher par une relecture** : dernière version, conclusions, et ce que « Limits » retire.
6. ***Routing Subspaces*.**
   - Dernier auteur : « Tanyel » (axe du 1er octobre) ou « Ayvaz » (rapports 2 et 3). L'extrait liste Konrad, Tanyel, Ayvaz : Ayvaz serait le dernier. À confirmer sur la source.
   - Nombre de modèles :
     - « cinq modèles de 2 à 9 milliards » (rapport 3, et axe du 1er octobre) ;
     - trois familles nommées (rapport 2) ;
     - l'extrait donne un autre décompte d'instances.
   - Date : « 11 mai 2026 » est incompatible avec un identifiant de juillet.
   - Lieu : NeurIPS 2026, selon l'extrait seul.
   - **Relecture à faire.**
7. ***Beyond Shallow Alignment*.**
   - Le passage du poids causal vers les MLP vaut-il pour les trois modèles (axe du 1er octobre) ou seulement pour Llama (rapport 5) ?
   - EMNLP 2026, conférence principale (rapports 3 et 5), ou seulement « annoncé » (1er octobre) ?
   - **Relecture à faire** (§4.3 et §4.4 du papier).
8. ***Constitutional adapters*.**
   - Le rapport 3 dit avoir lu un « texte ciblé » et donne un adaptateur de rang 4.
   - Le rapport 7 n'a eu que le résumé, par des sites tiers, arXiv ayant refusé ; le rang 4 vient de pith.science.
   - **Tranché provisoirement : résumé seul, rang non établi.** Le programme v1.1 l'inscrit déjà dans sa liste de relectures (partie 11, n° 3).
9. ***What Makes and Breaks Safety Fine-tuning?*** NeurIPS 2024 (1er octobre, URL des actes) ou non vérifié (rapport 3, arXiv « Preprint ») : **à trancher en ouvrant la page des actes.**
10. **2608.21766.** L'axe du 1er octobre le cite sous « Memarian … Rabusseau ». **Le §4.3 corrige : la première autrice est Farzaneh Heidari.**

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

1. **Nakamura (2605.24583), en entier, dans sa dernière version.**
   - C'est le précédent de méthode le plus proche.
   - Son contenu n'a été lu que par le rapport 3, et le titre a changé.
   - À vérifier :
     - l'inflation du rang par le gabarit ;
     - la dépendance du rang à la famille ;
     - l'écart entre ordre spectral et ordre causal ;
     - la forme exacte du contrôle aléatoire ;
     - l'absence de contrôle de dégradation.
   - La passation le demande déjà (§5.5, n° 3 ; §6, n° 3).
2. **Gurnee et al., §7 et annexes.**
   - Les chiffres sont relus. Restent :
     - la procédure exacte du choix des 176 et 63 jetons ;
     - l'existence ou non, ailleurs dans l'article, d'un contrôle aléatoire ou de concepts sans rapport pour cette ablation (le rapport 3 n'en a pas trouvé en plein texte) ;
     - la nature des contextes d'ablation, en distribution ou non.
   - Ces trois points fixent exactement ce qui nous sépare de lui.
3. ***Beyond Shallow Alignment*.**
   - Les actions sont-elles vraiment différentes d'un bras à l'autre ?
   - Le passage vers les MLP vaut-il pour un modèle ou pour trois ?
   - Le lieu, et les neuf points de contrôle publics.
   - C'est le travail sur nos modèles le plus proche.
4. ***Routing Subspaces*** : auteurs, date, lieu, nombre de modèles, ce qui y est dit du rang, et contrôle de la dégradation. Il est cité au centre pour la validation de l'instrument comme pour cet angle.
5. ***Constitutional adapters*** : le rang et les témoins. Il n'a été vu que par des résumés tiers.
6. **Abu Shairah et al.** : les chiffres sur le texte. Seule la page abs a été lue, et ils fondent l'argument de la représentation répartie.
7. **Ponkshe et al.** : la thèse et le lieu. Ils ont été lus par alphaXiv, et ils justifient les contrôles par directions sensibles.
8. **Cho et al.** : la phrase exacte sur l'analyse mécaniste prévue de leurs points de contrôle. C'est une concurrence possible, à dater.

**Contrainte de cette session.** arxiv.org et transformer-circuits.pub sont refusés à WebFetch et au shell. Ces relectures reviennent donc à l'instance du papier, par le chemin qu'elle a déjà utilisé (§4.2 : curl et pdftotext).
