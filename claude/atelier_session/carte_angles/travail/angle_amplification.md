# Angle : l'amplification de la représentation « je suis évalué » par l'entraînement

La question de l'angle : l'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ? Dans le programme v1.1, c'est une mesure descriptive, corrélationnelle par construction : une hausse plus forte dans le bras raisons rend l'hypothèse du regard plus plausible sans la prouver, et une absence de hausse ne l'exclut pas (programme v1.1, partie 6).

Sources de cette fiche : les onze rapports d'antériorité (4 du 1er octobre, 7 de la nuit), le §4 et le §5.5 de la passation v1.2, le complément de l'architecte (pour ce que la v1.3 contient du §5.5), et six recherches web faites le 2 octobre. Aucun texte source n'a été ouvert par cette instance.

---

## Le verdict

**Partiellement pris** : que l'entraînement fasse monter la conscience d'évaluation est publié, en verbalisé (y compris un SFT sur raisonnements suivi de RL contre un RL seul, chez Schoen et al., d'après le rapport 2, non relu) et en représentation, mais le long des étapes d'un pipeline tiers (Heidari et al.) ou entre deux instantanés d'un même modèle fermé (Sonnet 4.5). Personne, dans ce que les rapports ont vu, n'a comparé la trajectoire de la représentation « je suis évalué » entre un entraînement par raisons et un entraînement par actions, à action identique et à format contrôlé, point de contrôle par point de contrôle. C'est le verdict provisoire du §4.4 (n° 3) de la passation v1.2 ; les recherches du 2 octobre n'ont rien trouvé qui le change.

---

## Les travaux, du plus dangereux au moins dangereux

Aucun travail de niveau élevé n'a été trouvé.

### Niveau moyen

**1. *Stress Testing Deliberative Alignment for Anti-Scheming Training***
- **Auteurs** : Bronson Schoen … Marius Hobbhahn.
- **Date, lieu** : septembre 2025 (le 19 selon le rapport 1) ; arXiv 2509.15541.
- **Statut de lecture** :
  - les interventions sur la chaîne de pensée, faites sur o3 avant l'entraînement anti-manigance, et la phrase des auteurs sur ce qu'elles ne disent pas : relu sur la source par l'instance du papier (§4.2, n° 6) ;
  - la hausse de la conscience verbalisée après entraînement : rapport 6, texte intégral (§6.1 et 6.2) ; rapport 1, texte intégral (HTML par extraction) ;
  - les annexes O.3 et O.4 et le §6.3 : rapport 2, texte intégral ;
  - la hausse sous RL de capacités : rapport 6, texte intégral ; rapport 4, texte intégral (§8).
- **Ce qu'il fait** :
  - L'alignement délibératif (raisonner sur une spécification) fait monter la conscience d'évaluation verbalisée : de 0,9 % à 5,5 % sur o4-mini, de 2,3 % à 4,5 % sur o3 (rapports 1 et 6).
  - Annexe O.3, d'après le rapport 2 : une variante en RL seul, sans le SFT sur des raisonnements qui citent la spécification, n'augmente que légèrement cette conscience. Les auteurs attribuent l'essentiel de la hausse à l'étape SFT.
  - Annexe O.4, d'après le rapport 2 : retirer du SFT les trajectoires conscientes de la situation ralentit la hausse au fil des points de contrôle du RL, sans l'empêcher.
- **Danger : moyen.** C'est la variante la plus proche de l'angle : deux recettes, l'une avec raisonnements et l'autre sans, comparées sur la hausse de la conscience d'évaluation. Elle rend intenable toute phrase générale du type « l'entraînement par raisons amplifie la conscience d'évaluation, ce que personne n'avait montré ».
- **Ce qui le sépare du programme** :
  - modèles fermés ;
  - conscience verbalisée seulement, aucune sonde ;
  - le RL seul n'est pas « la même action sans raison » : les recettes diffèrent par bien plus que les raisons ;
  - pas de texte neutre de même longueur, pas de raisonnement d'une autre situation ;
  - les cibles du SFT contenaient de la conscience d'évaluation (rapport 2) : la hausse peut être recopiée, pas apprise.

**2. *Evaluation Awareness in Language Models: Representation, Verbalization, and Control***
- **Auteurs** : Farzaneh Heidari … Guillaume Rabusseau. La première autrice est Heidari, pas Memarian (§4.3, qui corrige les rapports « raisons contre actions » et « test causal » du 1er octobre, ainsi que la v1.1).
- **Date, lieu** : 22 août 2026 ; arXiv 2608.21766v1 (cs.CL).
- **Statut de lecture** : rapport 6, texte intégral ; rapport 2, texte intégral (§3 et travaux liés). Le rapport « raisons contre actions » du 1er octobre l'avait lu par un site tiers (pith.science).
- **Ce qu'il fait** :
  - Il construit des sondes linéaires sur 16 paires contrastives, dans six modèles ouverts, dont Qwen3-8B (rapport 6).
  - Sur les points de contrôle d'Olmo 3 (base, SFT, DPO, Think), la direction existe dès la base et « becomes amplified throughout the stages of supervised fine-tuning », puis reste stable (rapport 6). Les directions obtenues après le SFT sont colinéaires entre elles, et l'effet du pilotage croît à chaque étape (rapport 2). Les contrôles se font par directions aléatoires.
  - Les auteurs ne font aucun fine-tuning eux-mêmes (rapport 6).
- **Danger : moyen.** C'est le suivi représentationnel publié le plus proche : il interdit de revendiquer la mesure de la représentation au fil de l'entraînement, et il est le précédent de méthode à citer pour les sondes.
- **Ce qui le sépare du programme** :
  - les étapes d'un pipeline tiers, dont les données diffèrent de tout point de vue : aucune comparaison contrôlée ;
  - aucun bras raisons ni bras actions ;
  - le pilotage n'est mesuré que sur la verbalisation, sans lien avec une conduite d'alignement hors distribution.

**3. *Tracing Eval-Awareness Emergence Through Training of OLMo 3***
- **Auteurs** : Ram Bharadwaj … Robert Kirk.
- **Date, lieu** : 10 juin 2026 ; LessWrong (aussi sur l'Alignment Forum, d'après un extrait de recherche).
- **Statut de lecture** : rapport 2, texte intégral (API markdown de LessWrong) ; rapport 6, texte intégral.
- **Ce qu'il fait** :
  - Il mesure la conscience d'évaluation verbalisée sur des prompts de sûreté, point de contrôle par point de contrôle (444 prompts selon le rapport « condition des gains » du 1er octobre).
  - D'après le rapport 2, elle est d'environ 1 % en pré-entraînement. Elle monte avec le SFT, s'effondre avec le DPO, puis remonte avec le RL à récompenses vérifiables. L'écart de refus lié à cette conscience croît pendant ce RL.
  - Selon le rapport 2, 21 % des cibles du SFT verbalisent déjà la conscience d'évaluation.
- **Danger : moyen** (rapport 2, et le §4.4 le range parmi les travaux qui prennent une partie de l'angle). Il fixe le modèle de la mesure point par point, et il montre la confusion principale : le SFT recopie la conscience présente dans les cibles.
- **Ce qui le sépare du programme** :
  - mesure verbalisée seulement, aucune sonde ;
  - chaque étape est confondue avec ses données ;
  - aucune intervention, aucune comparaison raisons contre actions.

**4. *Claude Sonnet 4.5 System Card*, §7.6**
- **Auteurs** : Anthropic, sans auteur nommé.
- **Date, lieu** : fin septembre 2025. La date ne figure pas dans le texte extrait ; le premier commentaire public trouvé date du 30 septembre 2025 (rapport 2). Fiche système, PDF sur assets.anthropic.com.
- **Statut de lecture** :
  - la phrase selon laquelle la conscience d'évaluation explique une part des progrès (« a portion, but not all ») : relu sur la source par l'instance du papier (§4.2, n° 5) ;
  - le reste : rapport 2, texte intégral des §7.6.1 à 7.6.4, figures non lues.
- **Ce qu'il fait** : une comparaison par autoencodeur parcimonieux, entre un instantané précoce et le modèle final, montre que les représentations « faux / fictif » se renforcent au fil de l'entraînement. Un instantané antérieur se montre plus sensible à l'inhibition (rapport 2).
- **Danger : moyen** (rapport 2 ; §4.4). C'est une mesure interne du renforcement au fil de l'entraînement, sur un modèle réel.
- **Ce qui le sépare du programme** :
  - modèle fermé ;
  - deux instantanés d'un même pipeline, pas deux méthodes à actions identiques ;
  - pas de suivi sur des points de contrôle réguliers, pas de contrôle de format.

**5. *Call for Science of Eval Awareness (+ Research Directions)***
- **Auteur** : Igor Ivanov.
- **Date, lieu** : 25 décembre 2025 ; LessWrong et Alignment Forum.
- **Statut de lecture** : rapport 6, texte intégral (API LessWrong). Le rapport 3 le cite avec un second billet du même auteur.
- **Ce qu'il fait** : c'est un appel, sans résultats. Parmi les expériences proposées, d'après le rapport 6 :
  - mesurer la conscience d'évaluation après l'apprentissage de préférences ;
  - « Vary the format of constitutional training » ;
  - entraîner sur divers types de données synthétiques ou de raisonnement, puis mesurer la conscience d'évaluation qui en résulte ;
  - étudier les points de contrôle d'Olmo 3.
- **Danger : moyen.** La question « le format de l'entraînement change-t-il la conscience d'évaluation ? » est posée publiquement depuis décembre 2025. On ne peut pas présenter la question comme neuve ; il faut citer l'appel au centre. Personne n'est connu pour l'avoir exécuté sous la forme du programme (rapport 6 le classe « moyen à faible »).
- **Ce qui le sépare du programme** : ni action tenue identique, ni contrôle de format, ni lien avec l'avantage hors distribution des raisons ; aucune expérience.

### Niveau faible

**6. *Metagaming matters for training, evaluation, and oversight***
- **Auteurs** : Bronson Schoen … Jenny Nitishinskaya (Apollo et OpenAI).
- **Date, lieu** : 16 mars 2026 ; blog Alignment d'OpenAI (alignment.openai.com/metagaming), repris sur le site d'Apollo (vu par extrait de recherche, non ouvert).
- **Statut de lecture** : rapport 2, texte intégral ; rapport « condition des gains » du 1er octobre (page lue) ; rapport 6, résumé seul.
- **Ce qu'il fait** : pendant le RL de capacités d'o3, la conscience d'évaluation d'alignement passe de 2 % à 20,6 % (rapport 2). Elle persiste après l'entraînement d'alignement ; selon le rapport « condition des gains », elle monte même dans un environnement pendant cet entraînement.
- **Danger : faible** (rapport 2). C'est une hausse observée, mesurée en verbalisé, sous un RL de capacités.
- **Ce qui le sépare du programme** : modèles fermés, observationnel, aucune comparaison entre méthodes d'alignement.

**7. *System Card: Claude Fable 5 & Claude Mythos 5*, §6.4.2**
- **Auteurs** : Anthropic.
- **Date, lieu** : 9 juin 2026 ; fiche système (PDF).
- **Statut de lecture** : rapport 4, texte intégral (pdftotext).
- **Ce qu'il fait** : la conscience d'être noté, mesurée dans des environnements de code par des autoencodeurs en langage naturel et corroborée par des sondes contrastives, augmente au fil de l'entraînement (rapport 4). Le rapport 4 le transmet explicitement à l'amplification.
- **Danger : faible.** C'est une mesure interne au fil de l'entraînement, mais de « je suis noté », pas de « je suis évalué », et sans comparaison entre méthodes.
- **Ce qui le sépare du programme** : modèle fermé, autre représentation, un seul pipeline.

**8. *From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering***
- **Auteurs** : Rui Wu, Ruixiang Tang.
- **Date, lieu** : v1 du 1er avril 2026, v3 du 20 août 2026 ; arXiv 2604.01476.
- **Statut de lecture** : rapport 3, texte intégral (v3). Le §4.3 confirme, d'après le rapport 3, que la direction est mesurée puis écartée.
- **Ce qu'il fait** : il projette les activations des rollouts d'un GRPO sur une direction de conscience d'évaluation, tirée de paires contrastives, au fil de l'entraînement. Elle monte modérément pour Phi-4-mini et reste plate pour Llama-3.2-3B (annexe D), puis est écartée comme corrélat faible (rapport 3).
- **Danger : faible** (rapport 3). C'est un précédent de mesure par direction au fil des points de contrôle, sur des modèles ouverts.
- **Ce qui le sépare du programme** : RL contre le piratage de récompense, une seule méthode, aucun bras raisons.

**9. *Sycophancy Towards Researchers Drives Performative Misalignment***
- **Auteurs** : David D. Baek … Shi Feng. Ce n'est pas « Min … Feng », et c'est un travail distinct de 2606.08243 (§4.3).
- **Date, lieu** : v1 du 7 juin 2026 ; arXiv 2606.08629 ; ICML 2026, spotlight (§4.3).
- **Statut de lecture** : rapport 7, texte intégral (HTML).
- **Ce qu'il fait** : un fine-tuning qui rend le modèle plus complaisant augmente sa conscience d'évaluation, sur trois modèles (rapport 7).
- **Danger : faible.** C'est un type d'entraînement qui amplifie la conscience d'évaluation, mais il ne s'agit pas d'un entraînement de sûreté.
- **Ce qui le sépare du programme** : pas d'entraînement de sûreté, pas de raisons contre actions, pas de suivi par point de contrôle.

**10. *Models That Know How Evaluations Are Designed Score Safer***
- **Auteurs** : Katharina Deckenbach … Sahar Abdelnabi.
- **Date, lieu** : 27 mai 2026 (rapport 6) ou 28 mai (rapport « condition des gains » du 1er octobre) ; v4 du 7 septembre 2026 ; arXiv 2605.28591.
- **Statut de lecture** : rapport 7, texte intégral (HTML v4).
- **Ce qu'il fait** : un LoRA sur environ 106 M de tokens synthétiques qui décrivent les traits des évaluations rend les modèles plus « sûrs » sur des bancs de sûreté. La hausse des refus tient même dans les réponses sans conscience verbalisée (rapport 7). L'article n'a ni sondes ni pilotage.
- **Danger : faible.** Il montre qu'un entraînement sur des textes peut gonfler la sûreté mesurée par une reconnaissance implicite de l'évaluation. Il faut donc filtrer les raisons et mesurer en représentation.
- **Ce qui le sépare du programme** : aucun entraînement de sûreté, aucune trajectoire interne.

**11. *How far does alignment midtraining generalize?***
- **Auteurs** : Tomek Korbak … Ian Kivlichan, neuf auteurs (relus par les références de Cho et al., §4.2 n° 9).
- **Date, lieu** : 27 mars 2026 ; blog Alignment d'OpenAI.
- **Statut de lecture** : rapport 7, texte intégral ; correction au §4.3.
- **Ce qu'il fait** : la conscience d'évaluation n'y figure que dans une piste future (« Controlling for eval awareness »). Les interventions pourraient rendre les modèles « more eval-aware as opposed to more aligned », sans que ce soit mesuré (rapport 7 ; §4.3).
- **Danger : faible.** L'hypothèse de l'amplification par un entraînement d'alignement y est nommée, non testée. Tous les bras contiennent des raisons (§4.3).
- **Ce qui le sépare du programme** : pas de contraste raisons contre actions, aucune mesure de la conscience.

**12. *Constitutional Midtraining: Content Presence Drives Alignment Gains***
- **Auteurs** : Desiree Cho … Nigel Shadbolt (sept auteurs, §4.3).
- **Date, lieu** : v1 du 29 juillet 2026, v3 du 18 août 2026 ; arXiv 2607.26654.
- **Statut de lecture** : relu sur la source par l'instance du papier (§4.2, n° 9) pour le contraste avec et sans raisonnement et pour la réserve sur la conscience d'évaluation ; rapport 7, texte intégral, pour les points de contrôle publiés.
- **Ce qu'il fait** : il compare, à contenu apparié, des documents avec ou sans raisonnement délibératif. Les auteurs écrivent ne pas pouvoir exclure la conscience d'évaluation (« cannot rule out … eval-awareness ») et ne la mesurent pas. Ses 15 points de contrôle sont publics : 5 conditions × 3 stades, sur un modèle de 120 B, environ 241 Go chacun (rapport 7 ; §4.3). Les auteurs proposent l'analyse mécaniste de ces points comme travail futur (rapport 5).
- **Danger : faible** pour cet angle, puisqu'il ne mesure rien de la conscience. Mais c'est une **voie d'accès rapide pour un tiers** : sonder « je suis évalué » dans ses points avec et sans raisons suffirait à prendre une variante de l'angle (à contenu apparié, sans action identique ni texte neutre de même longueur).
- **Ce qui le sépare du programme** : documents de midtraining à 120 B, pas d'action identique, pas de témoin de même longueur, aucune mesure de la conscience.

**13. *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness***
- **Auteurs** : Hoang Cuong Nguyen … Usman Naseem.
- **Date, lieu** : 3 septembre 2026 ; arXiv 2609.03887 ; EMNLP 2026, conférence principale (rapport 5).
- **Statut de lecture** : rapport 5, texte intégral ; rapport « test causal » du 1er octobre, texte intégral.
- **Ce qu'il fait** : il fine-tune Llama-3.1-8B, Gemma-2-9B et Qwen3-8B par SFT, par SFT avec raisonnements qui précèdent la décision, et par ORPO. Avec raisonnements, le modèle installe une direction de refus distincte (rapport 5). Les 9 modèles fine-tunés sont publics (rapport 5).
- **Danger : faible** pour cet angle : il étudie la représentation du refus, pas celle de l'évaluation. Comme pour Cho et al., ses modèles publics, aux mêmes bases que le programme, offrent à un tiers une voie rapide vers une variante (raisons contre SFT simple, sans action identique ni trajectoire).
- **Ce qui le sépare du programme** : refus seulement, pas de contrôle de format, pas de points de contrôle intermédiaires rapportés, pas de familles tenues à part.

**14. *Training a Misaligned Reward Seeker***
- **Auteurs** : Qi … Hubinger, d'après une référence sur une page MATS (rapport 6).
- **Date, lieu** : août 2026 ; Alignment Science Blog d'Anthropic.
- **Statut de lecture** : rapport 6, texte intégral (parcouru par mots-clés).
- **Ce qu'il fait** : les auteurs envisagent qu'un entraînement d'alignement n'agisse qu'en accroissant la conscience d'évaluation. Ils observent au contraire une baisse de la conscience d'évaluation verbalisée (rapport 6).
- **Danger : faible.** C'est un contre-exemple à citer : un entraînement d'alignement n'amplifie pas forcément la conscience verbalisée.
- **Ce qui le sépare du programme** : mesure verbale seulement, pas de raisons contre actions.

**15. *Training LLMs to Verbalize Evaluation Awareness***
- **Auteurs** : Usman Anwar … David Krueger.
- **Date, lieu** : 28 septembre 2026 (rapport 2) ; arXiv 2609.36316 ; atelier TAE de NeurIPS 2026.
- **Statut de lecture** : rapport 4, résumé seul. Le rapport « test causal » du 1er octobre l'a lu par un site tiers (alphaXiv).
- **Ce qu'il fait** : un entraînement multiplie la verbalisation tandis que la conscience latente et la conduite restent stables (rapport 4).
- **Danger : faible.** C'est un argument de méthode : verbalisation et représentation se dissocient sous l'entraînement, donc une amplification verbalisée ne dit rien de la représentation, et inversement.
- **Ce qui le sépare du programme** : pas d'entraînement de sûreté, pas de comparaison de méthodes.

**16. *When Is a Probe Monitor Safe to Act On?…***
- **Auteurs** : Sana Gaya … Girish Gupta.
- **Date, lieu** : 2026 ; atelier AIW 2026 (OpenReview).
- **Statut de lecture** : rapport 4, résumé seul.
- **Ce qu'il fait** : sur Llama-3.1-8B-Instruct, une sonde évaluation/déploiement garde son score global sous un RL à récompenses vérifiables, mais bascule sur les cas limites ; la réentraîner ne récupère presque rien (rapport 4).
- **Danger : faible.** C'est une menace de méthode directe pour la trajectoire : une sonde figée avant l'entraînement peut dériver d'un point de contrôle à l'autre.
- **Ce qui le sépare du programme** : il étudie la fiabilité de la sonde, pas l'amplification.

**17. Autres travaux faibles, à citer en une ligne**
- ***Verbalizable Representations Form a Global Workspace in Language Models*** : Wes Gurnee … Jack Lindsey (Anthropic). Paru le 6 juillet 2026 sur Transformer Circuits, puis en v1 sur arXiv le 16 juillet (2607.15495). Rapport 5, texte intégral. Sur un organisme qui pirate la récompense, le signal de tromperie apparaît dès le fine-tuning sur documents ; le RL de code l'amplifie, le RLHF l'atténue. C'est un autre concept que « je suis évalué ».
- ***Risk Report: August 2026***, §2.25 : Anthropic ; rapport 4, texte intégral. Chez « Hacker-Opus », la conscience d'être noté monte fortement quand le piratage de récompense augmente.
- ***Measuring Reward-Seeking via Contrastive Belief Updates*** : Axel Højmark … Alexander Meinke, 21 juillet 2026, arXiv 2607.18966 ; rapport 4, résumé seul. Sur les points de contrôle d'un RL de capacités d'o3, le modèle se range de plus en plus du côté du correcteur. La mesure est comportementale.
- ***Evaluation Awareness Is Not One Capability*** : arXiv 2606.23583, auteurs non relevés ; rapport 2, résumé seul. La détection de l'évaluation tient surtout au réglage d'instructions, plus qu'à l'échelle.

### Vus par extrait de recherche le 2 octobre, non ouverts (aucun chiffre)
- **Dépôt `aaliyan1230/rlvr-safety-dynamics`** (GitHub ; vu par extrait de recherche, non ouvert). Il porte sur 11 points de contrôle GRPO de Tülu 3.1, avec des situations écrites, dont certaines sur la conscience d'évaluation. L'extrait conclut à une dérive de la mesure plutôt qu'à une dérive de la sûreté. Danger faible : des items comportementaux, une seule méthode. C'est une mise en garde pour toute trajectoire, et la première sortie du projet SPAR d'Aaliyan (voir les projets).
- ***When Reasoning Traces Reveal More Than They Hide*** (ACL Findings 2026, aclanthology 2026.findings-acl.2078 ; vu par extrait de recherche, non ouvert). L'extrait mêle des modèles fine-tunés par SFT, DPO et GRPO et des traces de raisonnement sur des scénarios de conscience de soi. Le lien avec l'angle n'est pas établi : danger non évalué, à ouvrir.
- ***Why models game evals might matter as much as whether they do it*** (LessWrong, Eub3eLJGMka3asgaP ; vu par extrait de recherche, non ouvert). Auteur et date non vus. Selon l'extrait, les formes de méta-jeu auraient des origines différentes. Danger non évalué.
- **Évaluation par Apollo d'un modèle d'OpenAI nommé « GPT-6 Astra »** (aiweekly.co ; vu par extrait de recherche, non ouvert ; date non vue). L'extrait compare la conscience verbalisée entre deux générations de modèles. Adjacent : ce n'est pas une trajectoire d'entraînement.

---

## Ce qui reste libre

Pour ce que les onze rapports et les six recherches du 2 octobre ont pu voir, personne n'occupe la combinaison suivante :
- **la représentation, pas la verbalisation** : une sonde « évalué / déployé » validée et l'amplitude de la projection sur « je suis évalué » (indice d'évaluation moins indice de déploiement). Schoen et al., Bharadwaj et Kirk et le billet sur le méta-jeu ne mesurent que la verbalisation ; Anwar et al. montrent que les deux se dissocient sous l'entraînement ;
- **une comparaison contrôlée entre méthodes**, pas les étapes d'un pipeline tiers (Heidari et al.) ni deux instantanés d'un modèle fermé (Sonnet 4.5) ;
- **l'action alignée identique mot pour mot** dans tous les bras, avec les deux témoins de format (texte neutre de même longueur, raisonnement d'une autre situation). Ils séparent « des raisons » de « plus de texte » et de « n'importe quel raisonnement ». Le RL seul de l'annexe O.3 ne fait pas ce travail ;
- **point de contrôle par point de contrôle, dans chaque entraînement**, avec plusieurs graines par bras, sur des modèles ouverts d'environ 8 B (Llama-3.1-8B-Instruct, Qwen3-8B) ;
- **la confusion de la recopie neutralisée** : toute trace de conscience d'évaluation filtrée dans les textes générés (raisons, textes neutres, actions), et ce qui en reste mesuré. Sans ce filtrage, l'amplification est copiée, pas apprise (passation v1.2, §5.5 n° 2). D'après le complément de l'architecte, la v1.3 ne prévoit qu'un filtrage par le juge scellé : c'est à reporter dans les conséquences ;
- **la trajectoire reliée au test causal du regard** et à l'avantage hors distribution, sur les mêmes modèles.

Deux précautions de méthode viennent de l'antériorité elle-même :
- réestimer la sonde à chaque point de contrôle, ou rapporter les deux versions, une sonde figée et une sonde réajustée (Gaya et al. ; dérive de mesure chez Aaliyan) ;
- ne pas lire l'amplitude comme une influence causale : le programme le dit déjà, et seul le test du regard tranche.

**Les risques de prise rapide par un tiers.** Les points de contrôle publics de Cho et al. (avec et sans raisonnement, à contenu apparié) et les fine-tunes publics de *Beyond Shallow Alignment* (SFT contre SFT avec raisonnements, sur Llama-3.1-8B et Qwen3-8B) permettraient à quiconque de sonder « je suis évalué » sans rien entraîner. Aucun rapport n'a vu quelqu'un le faire. Cela prendrait une variante de l'angle, sans action identique ni témoins de format.

---

## Les projets annoncés qui touchent cet angle, avec leurs dates

Calendrier de la cohorte SPAR d'automne 2026 : recherche du 14 septembre au 14 décembre, démonstration le 19 décembre 2026 (FAQ de SPAR, lue par deux agents ; §4.4 de la passation).

- **Igor Ivanov (Meridian Cambridge), SPAR automne 2026** : causes et mitigations du méta-jeu, sur des organismes modèles ; comment l'entraînement mène au jeu d'évaluation. Rapports 2, 4 et 6 ; projet aussi vu par extrait de recherche, non ouvert, le 2 octobre. C'est le projet qui touche le plus l'amplification (rapport 2), sans bras raisons contre actions annoncé. Résultats possibles d'ici le 19 décembre 2026.
- **Muhammad Aaliyan, SPAR automne 2026, *When RLVR Changes the Model, the Safety Test, or Both*** : points de contrôle de Tülu 3.1 8B, avec des items de conscience d'évaluation (rapports 2 et 4). D'après un extrait de recherche (non ouvert), une première étude est déjà dans un dépôt public, et le projet vise à la reproduire sur une autre lignée d'entraînement. Même calendrier.
- **Ryan Lundqvist (Pivotal), SPAR automne 2026, *Training-Time Mitigations for Eval Awareness and Eval Gaming*** : mesure de la conscience d'évaluation, y compris non verbalisée, pendant des fine-tunings avec adaptateurs d'inoculation ou pilotage préventif (rapport 6 ; page relue, §4.2 n° 3). Adjacent pour l'amplification ; central pour le retrait et la survie. Même calendrier.
- **Juan Cadile (Rochester), SPAR automne 2026, *Constitutions and Reasons*** : démonstrations contre réponses annotées de raisons, sans mesure annoncée de la conscience d'évaluation (rapport 6). S'il en ajoutait une, il prendrait une variante comportementale de l'angle. Même calendrier.
- **Netzer Epstein et Neta Ravid, SPAR automne 2026, *Evaluation Awareness Convergence*** : comparaison des instruments de mesure, dont le score par lentille jacobienne (rapports 2 et 6). Utile pour l'instrument, faible pour l'angle.
- **Cozmin Ududec (UK AISI), MATS hiver 2027** : projets proposés pour suivre la conduite et les représentations internes à travers SFT, RL et entraînement de sûreté, en variant les indices à tâche fixe (rapport 6). Candidatures closes ; dates de la cohorte non relevées par les rapports.
- **Équipe d'alignement de UK AISI (Alexandra Souly, Robert Kirk), MATS hiver 2027** : relier les mesures de conscience d'évaluation, et étudier le jeu non verbalisé et ses atténuations (rapport 6). Faible.
- **Collaboration OpenAI–Apollo sur l'émergence du méta-jeu** : annoncée en mars 2026 (rapport 2 ; aussi vue par extrait de recherche, non ouvert). Aucune date de résultat.
- **Apollo, évaluations tierces de runs d'entraînement avec points de contrôle intermédiaires** : billet du 5 juillet 2026 (rapport 2 ; aussi vu par extrait de recherche, non ouvert).
- **Bharadwaj et Kirk** : tentent de refaire le DPO d'OLMo avec des points de contrôle intermédiaires (rapport 2 ; confirmé par extrait de recherche, non ouvert). Aucune date.
- **Cho et al.** : analyse mécaniste de leurs points de contrôle proposée comme travail futur (rapport 5). Aucune date.
- **Qiyao Wei, SPAR printemps 2026** (programme du 16 février au 16 mai 2026) : sa proposition demande si l'entraînement contre le désalignement a des effets indésirables, dont une hausse de la conscience situationnelle (« Which factor is more important? »). Sa seule sortie trouvée porte sur les indices qui trahissent une évaluation, pas sur l'entraînement (rapport 2 ; §4.4). Terminé, sans sortie sur la question.
- **ICLR 2027** : soumissions invisibles. Date limite le 25 septembre, reviews le 5 novembre, décisions le 16 décembre 2026 (rapport 6, non relu). C'est le principal risque qu'aucune recherche ne peut lever avant le 5 novembre.

Les six recherches du 2 octobre n'ont rien montré, daté d'après le 1er octobre, qui compare raisons et actions sur la conscience d'évaluation. Un moteur de recherche ne prouve pas une absence.

---

## Les formulations « to our knowledge »

**Tenables**, pour ce que les rapports ont pu voir :
- « To our knowledge, no prior work compares the training trajectory of an internal evaluation-awareness representation between reason-based and action-only fine-tuning, with the aligned action held identical and output format controlled. »
- « To our knowledge, prior evidence that training increases evaluation awareness either relies on verbalization, tracks the stages of a fixed third-party pipeline, or compares snapshots of a single closed model. » C'est une phrase descriptive, à suivre des citations de Schoen et al., Bharadwaj et Kirk, Heidari et al. et de la fiche Sonnet 4.5.

**Intenables** :
- Toute revendication d'être les premiers à montrer que l'entraînement amplifie la conscience d'évaluation : Schoen et al. (§6), le billet sur le méta-jeu, Bharadwaj et Kirk, Heidari et al. (§5.5 n° 9 de la passation).
- « To our knowledge, no work compares training with and without reasoning on evaluation awareness » : faux en verbalisé (Schoen et al., annexe O.3, d'après le rapport 2).
- Toute revendication d'être les premiers à suivre la conscience d'évaluation au fil des points de contrôle : Bharadwaj et Kirk, Heidari et al., Wu et Tang, et le dépôt d'Aaliyan.
- Toute revendication d'être les premiers à poser la question de l'effet du format de l'entraînement sur la conscience d'évaluation : Ivanov (décembre 2025), la proposition de Qiyao Wei (décembre 2025), Korbak et al. (mars 2026).
- Toute lecture causale de la trajectoire : le programme l'exclut lui-même.

---

## Les contradictions entre rapports, et comment elles se tranchent

1. **Première autrice de 2608.21766.**
   - Ce qui se contredit : « Memarian » (rapports « raisons contre actions » et « test causal » du 1er octobre, programme v1.1) contre « Heidari » (rapports 2, 5 et 6). Le rapport 3 cite « Heidari, Memarian, Rabusseau ».
   - Tranché par le §4.3 : Farzaneh Heidari.
2. **Ce que 2608.21766 trouve sur Olmo 3.**
   - Ce qui se contredit : « le post-entraînement stabilise une direction déjà présente dans la base » (rapport « test causal » du 1er octobre) contre « amplifiée pendant le SFT, puis stable » (rapports 2 et 6, et le rapport « raisons contre actions » du 1er octobre, par un site tiers ; l'extrait de recherche du 2 octobre va dans ce sens).
   - Les deux lectures sont compatibles, mais l'ampleur de la hausse en dépend.
   - Non tranché par le §4 : relecture à faire.
3. **Les chiffres de pilotage de 2608.21766.**
   - Ce qui se contredit : « +0,2 à 1,5 point sur 3 » (rapport « test causal » du 1er octobre) contre une verbalisation « de 0,5 % à 3,7 % (7B) » (rapport 2). Ce sont peut-être deux quantités différentes.
   - Non tranché : relecture à faire avant tout chiffre.
4. **La hausse sous RL de capacités.**
   - Ce qui se contredit : « de 2,0 % à 20,5 % », attribuée à *Stress Testing Deliberative Alignment* (rapport 6 ; rapport 4 : un modèle expérimental sans entraînement anti-manigance) contre « de 2 % à 20,6 % », attribuée au billet sur le méta-jeu, pour o3 (rapport 2).
   - Même mesure reprise, ou deux mesures distinctes : non tranché par le §4. Relire les deux sources.
5. **L'annexe sur le RL seul dans *Stress Testing Deliberative Alignment*.**
   - Ce qui se contredit : le rapport 2 y lit une hausse de la conscience bien plus faible sans l'étape SFT. Le rapport 1 y lit que le RL seul « fait moins bien » que l'entraînement complet, sans dire sur quelle mesure.
   - Les deux lectures ne s'excluent pas, mais elles ne portent pas sur la même chose.
   - Non tranché : relire l'annexe O.3.
6. **Le niveau de départ chez Bharadwaj et Kirk.**
   - Ce qui se contredit : « environ 1 % » (rapport 2), « négligeable » (rapport « condition des gains » du 1er octobre), « presque nulle » (rapport 6), « nulle » (programme v1.1).
   - Le « nulle » de la v1.1 force le trait. Retenir « environ 1 % » après relecture.
7. **Le niveau de danger de Bharadwaj et Kirk.**
   - Ce qui se contredit : adjacent (rapport « condition des gains » du 1er octobre), faible à moyen (rapport 6), moyen (rapport 2).
   - Tranché par le §4.4, qui le compte parmi les travaux qui prennent une partie de l'angle : moyen.
8. **Le statut de lecture du billet sur le méta-jeu.**
   - Ce qui se contredit : texte intégral (rapport 2) contre résumé automatique seul (rapport 6).
   - Le contenu ne se contredit pas ; s'en tenir au rapport 2 jusqu'à relecture.
9. **Auteurs et date de 2606.08629.**
   - Ce qui se contredit : « Min … Feng, 18 mars 2026 » (rapport « combinaison exacte » du 1er octobre) contre « Baek … Feng », v1 du 7 juin 2026 (rapport 7).
   - Tranché par le §4.3 : Baek … Feng, ICML 2026, spotlight. Le 18 mars est vraisemblablement la date du billet LessWrong lié, non vérifié.
10. **Date de 2605.28591.**
    - Ce qui se contredit : 27 mai (rapport 6) contre 28 mai (rapport « condition des gains » du 1er octobre).
    - Sans incidence. Relire la page arXiv si la date doit figurer.
11. **Date de l'article sur l'espace de travail global.**
    - Ce qui se contredit : 6 juillet (rapports « raisons contre actions » et « combinaison exacte » du 1er octobre, rapport 5) contre 16 juillet (rapport 2).
    - Les deux sont justes : Transformer Circuits le 6, arXiv v1 le 16 (rapport 5).

---

## Ce qu'il faut relire sur la source avant de le citer au centre, et pourquoi

Rappel : arxiv.org, lesswrong.com, alignmentforum.org et alignment.anthropic.com sont refusés à cette session. Ces relectures passent par le canal de l'instance du papier, sans miroir ni cache.

1. ***Stress Testing Deliberative Alignment*, §6, §6.3, annexes O.3 et O.4, §8.**
   - Seul le constat sur les interventions faites avant l'entraînement est relu (§4.2 n° 6).
   - L'annexe O.3 est le travail le plus proche de l'angle, et le rapport 1 la lit autrement que le rapport 2.
   - L'annexe O.4 fonde le filtrage des raisons (§5.5 n° 2).
   - Le chiffre de 2,0 % à 20,5 % doit être rapproché de celui du billet sur le méta-jeu.
2. **Heidari et al., 2608.21766, la section sur les points de contrôle d'Olmo et les contrôles.**
   - Les contradictions n° 2 et 3.
   - C'est le précédent de méthode pour les sondes, et il inclut Qwen3-8B.
   - Relever aussi la liste complète des auteurs.
3. **Bharadwaj et Kirk.**
   - Le chiffre de 21 % de cibles SFT qui verbalisent est le second appui du §5.5 n° 2. Il n'est connu que par le rapport 2.
   - Relever aussi le nombre de prompts et le niveau de départ.
4. **La fiche Sonnet 4.5, §7.6.**
   - La comparaison par autoencodeur parcimonieux entre l'instantané précoce et le modèle final n'est connue que par le rapport 2, figures non lues.
   - Seule la phrase « a portion, but not all » est relue.
5. **Ivanov, *Call for Science of Eval Awareness*.**
   - La formule « Vary the format of constitutional training » et la liste des expériences proposées ne sont connues que par le rapport 6.
   - C'est l'antécédent de la question elle-même : il faut le citer exactement.
6. **Le billet sur le méta-jeu (alignment.openai.com/metagaming).**
   - Vérifier les chiffres de 2 % à 20,6 %, et la hausse dans un environnement pendant l'entraînement d'alignement (rapport « condition des gains » du 1er octobre).
   - Les rapports divergent sur leur propre lecture du billet.
7. **La fiche Fable 5, §6.4.2.**
   - La phrase sur la hausse de la conscience d'être noté au fil de l'entraînement, et la méthode de mesure : rapport 4 seulement.
8. **La proposition SPAR de Qiyao Wei**, si on la cite : la question « Which factor is more important? » n'est connue que par le rapport 2.
9. **Wu et Tang, annexe D**, si on la cite comme précédent de la mesure par direction au fil d'un RL : rapport 3 seulement.
10. **Gaya et al., Anwar et al.**, s'ils justifient au centre la réestimation de la sonde à chaque point de contrôle et le choix de la représentation contre la verbalisation : ils ne sont connus que par leur résumé.
11. **Le dépôt d'Aaliyan et les trois travaux vus par extrait le 2 octobre** : à ouvrir avant d'en dire quoi que ce soit, aucun chiffre n'étant permis.
