<section class="partie" markdown="1">

# 1 · Antériorité : ce qui existe, ce qui manque, qui court

**La recherche, en trois temps.**
1. **Le 1<sup>er</sup> octobre 2026** : quatre recherches indépendantes, sur quatre axes :
   - raisons contre actions, avec une mesure hors distribution ;
   - la conscience d'évaluation comme condition des gains ;
   - un test causal interne de ce que l'entraînement installe ;
   - le retrait de la conscience d'évaluation pendant l'entraînement.

   Environ 250 pages ont été ouvertes ; aucune référence n'a été citée de mémoire.
2. **La nuit du 1<sup>er</sup> au 2 octobre** : sept recherches de plus, une par pan du programme, et une de vérifications (passation v1.2, §4).
3. **Le 2 octobre** :
   - des relectures sur la source par l'instance du papier, par curl et pdftotext (passation v1.2, §4.2) ;
   - puis la carte des angles déjà pris (`claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md`). Elle rassemble les onze rapports, une veille du jour et ces relectures, en huit angles, vérifiés en trois tours de critique. Le statut de lecture de chaque fait y est donné. Cette partie en reprend les conclusions et les corrections.

**Les limites.**
- **Le réseau** refusait arXiv, Hugging Face, LessWrong, l'Alignment Forum, OpenReview, Semantic Scholar, OpenAlex, alignment.anthropic.com et transformer-circuits.pub. Aucun refus n'a été contourné.
- **Les lectures.** Beaucoup de travaux n'ont été lus que par des agents, souvent par un outil qui résume la page, ou par un miroir (pith.science, alphaXiv). Ils sont marqués « rapport ».
- **Ce qu'on ne voit pas.** Les soumissions à ICLR 2027, déposées au plus tard le 25 septembre 2026, ne sont pas publiques (rapport, non relu). C'est le principal risque qui reste. Viennent ensuite les sorties des projets SPAR d'automne et la suite qu'Anthropic donnera à son entraînement par réflexion contrefactuelle.
- **Deux recherches légères.** Celles des phases de la détresse (trois requêtes) et de « punir, retirer ou raisonner » (deux requêtes) sont à refaire (partie 11).

## Le verdict

<div class="phrase" markdown="1">

**Aucun des onze rapports, ni la veille du 2 octobre, n'a trouvé l'expérience centrale :**
- inhiber une représentation validée de « je suis évalué » ;
- dans des modèles ouverts entraînés sur les raisons ou sur les mêmes actions, à format et à contenu contrôlés ;
- à dégradation appariée ;
- pour mesurer la part de l'avantage hors distribution qui en dépend.

*Stress Testing Deliberative Alignment* nomme lui-même ce vide : ses éditions de la chaîne de pensée « does not inform us whether anti-scheming training changes this causal relationship » (relu).

**Aucun angle n'est pris en entier ; tous le sont en partie.** Quatre sous-questions sont au niveau de danger élevé, occupées par trois travaux :
- la présence, puis la nécessité, de concepts installés par un entraînement par principes (Gurnee et al., §7, relu) ;
- la comparaison d'un juge qui voit le raisonnement à un juge qui ne voit que la réponse, quand ce raisonnement verbalise l'évaluation (le dépôt exp9 de Lundqvist, relu) ;
- la survie au post-entraînement d'une mitigation du jeu d'évaluation, annoncée par le projet SPAR de Lundqvist (page relue).

**L'hypothèse du regard**, « plus conscients d'être évalués que plus alignés », est posée par plusieurs travaux : Korbak et al., Redwood, la fiche système d'Opus 4.7, Cho et al., d'autres. Elle est testée pour la conduite en général, sur des modèles fermés. Ainsi, selon la fiche système de Sonnet 4.5, la conscience d'évaluation explique « a portion, but not all » des progrès d'alignement sur certaines évaluations (relu). Elle n'est testée nulle part, à notre connaissance, pour l'avantage des raisons. Les versions précédentes la disaient « nommée, non testée » : c'est corrigé.

</div>

## Les huit angles

| Angle | Verdict | Les travaux les plus dangereux | Ce qui reste libre |
|---|---|---|---|
| Raisons contre actions | Partiellement pris | *Teaching Claude Why* ; de la Fuente et Conmy ; Cho et al. (contre-résultat) ; *Model Spec Midtraining*. Annoncé : Cadile | La combinaison contrôlée : action identique mot pour mot, texte neutre de même longueur avant l'action, raisonnement d'une autre situation, familles tenues à part jusqu'à l'agentique à plusieurs tours, trois cadrages, modèles ouverts de 8B en LoRA |
| La dépendance au regard | Prise en partie pour la conduite en général ; libre pour l'avantage des raisons | Fiche Sonnet 4.5, §7.6 ; Gurnee et al. ; *Stress Testing Deliberative Alignment* ; fiche Opus 4.7 ; Jagadeesh et al. | Inhiber une représentation validée de « je suis évalué » dans des modèles ouverts entraînés pour l'occasion, par raisons et par les mêmes actions, à dégradation appariée, et chiffrer la part de l'avantage qui en dépend |
| L'amplification | Partiellement prise | *Stress Testing*, annexe O.3 ; Heidari et al. ; Bharadwaj et Kirk ; fiche Sonnet 4.5 ; Wu et Tang | La trajectoire d'une représentation interne de « je suis évalué », comparée entre raisons et actions, à action identique et format contrôlé |
| Le principe localisé | Partiellement pris ; élevé pour une sous-question | Gurnee et al., §7 (élevé) ; Nakamura ; *Beyond Shallow Alignment* ; *Routing Subspaces* | La localisation à action identique, sous-espace tiré des bras témoins, balayage du rang, contrôles à dégradation appariée, cas positif en distribution d'abord ; le lien entre rang et charge |
| Le retrait pendant l'entraînement | Méthodes prises ou annoncées ; application libre | *Routing Subspaces*, annexe I ; Lundqvist (annoncé) ; Santos-Grueiro ; Li et Turner ; CAFT ; Nadaf ; BLOCK-EM | Retirer « je suis évalué », validée sur un organisme, pendant un entraînement par raisons ; tester l'inconditionnalité de l'avantage ; chercher le ré-encodage par une sonde neuve |
| La survie | Partiellement prise ; élevé pour une sous-question | Lundqvist (élevé pour une mitigation du jeu d'évaluation) ; Cho et al. ; *Stress Testing*, §8 ; *Teaching Claude Why* | La survie de l'avantage des raisons, et de son indépendance au regard, après un post-entraînement neutre ou qui paie le jeu d'évaluation |
| Les raisons pour le juge | Partiellement prises ; élevé pour une variante | exp9 (élevé dans sa variante) ; fiche Fable 5, §6.4.2.2.1 ; Kaufmann et al. ; Drori et al. ; Højmark et al. | Des justifications par principes ; la cohérence entre raison et action quand on édite la situation ; le retrait de « je suis noté » pendant un RL ou un DPO noté par un juge |
| L'anatomie | Partiellement prise, surtout par Anthropic ; élevé pour deux sous-questions | Gurnee et al., §7 (élevé pour la présence et la nécessité) ; *Inoculate or Reflect?* ; *Beyond Shallow Alignment* | La suffisance par patching ; la spécificité par famille ; le rang selon la charge ; la raison imposée ; les concepts contre le caractère ; l'organisme à mot inventé ; sur modèles ouverts |

## Les travaux les plus proches, angle par angle

**Raisons contre actions**
- ***Teaching Claude Why*** (Kutasov … Price, Anthropic, 8 mai 2026 ; rapports). Un SFT de Claude Sonnet 4 et de Haiku 4.5, évalué hors distribution sur des pots de miel synthétiques. Des actions alignées filtrées font passer le désalignement agentique de 22 % à 15 % ; des réponses générées sous une incitation à délibérer sur l'éthique, retirée avant l'entraînement, le font descendre vers 3 %.
  - Ce qui manque : l'action n'est pas tenue identique ; les pots de miel d'entraînement sont conçus pour ressembler aux évaluations ; il n'y a ni contrôle de format ni contrôle de contenu, ni mesure de la conscience d'évaluation.
  - L'absence d'explication mécaniste est une paraphrase : la citation qu'en donnaient les versions précédentes n'est reproduite mot pour mot par aucun rapport.
- ***Model Spec Midtraining*** (Li … Kutasov, arXiv 2605.02087, mai 2026 ; rapport). Une spécification enrichie d'explications de valeurs bat une version de même longueur enrichie de sous-règles ; sur Llama-3.1-8B, avec des valeurs simples. À distinguer de Li et Turner.
- ***Constitutional Midtraining*** (Cho, Tice, Hogan, Batra, Radmard, Zhao, Shadbolt ; arXiv 2607.26654v3). **Un contre-résultat**, à citer comme tel.
  - Relu : avec et sans raisonnement délibératif, les bras sont indistinguables après le midtraining et après le SFT. Après un fine-tuning bénin (GRPO), le bras avec raisonnement fait plus de chantage : +9,0 points (31,0 % contre 22,0 %, p < 0,05).
  - Relu : les auteurs ne peuvent exclure ni le pattern-matching de surface ni la conscience d'évaluation.
  - Rapports : le contenu est apparié entre les bras, pas la longueur.
  - Quinze points de contrôle publics, d'un modèle de 120B : inutilisables à 8B.
- **de la Fuente et Conmy** (*Shared SFT Lessons…*, arXiv 2607.26173 ; rapports). Le transfert va de 10,3 % avec des exemples à 94,5 % avec la raison et les exemples ; deux phrases neutres en donnent déjà 44,5 et 62,5 %. C'est un effet de format, dans un jouet ; leur partie sur l'alignement est contestée entre rapports. D'où notre bras du texte neutre.
- **Baines … Tan** (*Stress-testing Alignment Midtraining*, arXiv 2609.20412 ; rapports). Des démonstrations travaillées contre des descriptions (facteurs 0,73 et 0,35) ; des effets fragiles à 2 % de données contraires ; un avantage qui baisse légèrement après 256 pas de RL. Un contrepoint.
- **Wang et al.** (*Safety Reasoning with Guidelines*, arXiv 2502.04040 ; Wang, Qin, Shen, Wang, Tao, Cheng ; titre et auteurs relus). Un raisonnement guidé contre des refus, sur des jailbreaks tenus à part ; une analyse de représentation sans test causal.
- ***Beyond Shallow Alignment*** (Nguyen, Dras, Naseem ; arXiv 2609.03887, EMNLP 2026 ; rapports et README lu par curl).
  - Un SFT, un SFT avec des raisonnements de sûreté, et un ORPO, sur Llama-3.1-8B, Gemma-2-9B et Qwen3-8B, ajustés depuis leurs modèles de base. Les actions ne sont pas identiques.
  - Avec raisonnements, le refus serait « plus distribué » ; les rapports se contredisent sur ce point.
  - Le bras avec raisonnements est « the most correctable via steering » (README). Cela touche aussi la phase de la détresse.
- **Annoncés** : le projet SPAR de Cadile, des démonstrations contre des réponses annotées de raisons ; une réplication de *Teaching Claude Why* sur modèles ouverts par Second Look Research (rapports, non relu).

**La dépendance au regard**
- **La fiche système de Sonnet 4.5, §7.6** (Anthropic, 2025 ; la conclusion est relue, le reste vient d'un rapport). C'est le plus proche.
  - L'inhibition de 10 traits d'autoencodeur parcimonieux et de 4 vecteurs contrastifs fait monter les actions désalignées jusqu'à 8 à 9 %. Le témoin rapporté, 10 traits aléatoires de même norme, n'en produit aucune. Un instantané antérieur est plus sensible.
  - Relu : « a portion, but not all ». C'est la seule estimation par expérience propre de la dépendance d'un gain d'entraînement au regard.
  - Ce qui manque : le modèle est fermé ; on compare deux instantanés d'un même entraînement, pas deux méthodes à action identique ; il n'y a ni familles tenues à part, ni dégradation appariée, ni validation sur un organisme.
- **Gurnee … Lindsey** (*Verbalizable Representations Form a Global Workspace in Language Models*, Anthropic, juillet 2026, arXiv 2607.15495 ; §7 relu, le reste rapports).
  - Sur Sonnet 4.5, retirer de l'espace de travail les directions de jetons comme « fake » ou « simulation » fait passer la verbalisation de l'évaluation de 71 % à 3 %, et le chantage de 0/180 à 13/180.
  - Le même article entraîne Haiku 4.5 par réflexion contrefactuelle (voir le principe localisé).
  - Il réunit les deux ingrédients de l'angle, sans les croiser, sur des modèles fermés.
- **Schoen … Hobbhahn** (*Stress Testing Deliberative Alignment*, Apollo et OpenAI, arXiv 2509.15541 ; la portée est relue, les chiffres viennent de rapports). Sur o3, avant l'entraînement anti-manigance :
  - retirer de la chaîne de pensée la conscience d'évaluation verbalisée fait passer les actions dissimulées de 13,2 % à 24,2 % ;
  - l'y injecter les fait passer de 24,5 % à 18,6 %.
- **Les autres fiches système** (rapports) :
  - Opus 4.7, §6.5.2.2 : elle inhibe, et formule sans le tester le lien avec un type d'entraînement ;
  - Fable 5, §6.5.1.2 : cinq vecteurs témoins, à dégradation négligeable.
- **Jagadeesh … Singhal** (OpenAI, arXiv 2606.24014 ; rapport) traitent l'hypothèse de façon comportementale.
- **Pan … Greenblatt** (Redwood, octobre 2025 ; rapports) relisent l'inhibition de la fiche Sonnet 4.5, sans expérience propre. Les rapports se contredisent sur la part qu'ils estiment.
- ***Metagaming matters*** (OpenAI et Apollo, mars 2026 ; rapports) : le raisonnement sur la supervision survit à l'entraînement d'alignement. C'est observationnel.
- ***Generalization Hacking*** (Xiao … Phuong, arXiv 2606.12016 ; rapport) : des organismes qui se savent entraînés empêchent la généralisation du RL. La variable est la conscience d'être entraîné ; le témoin « conscience seule » finit presque au même écart.
- **Sur des modèles ouverts, sans entraînement de sûreté** :
  - l'organisme de Hua et al., à conduite conditionnée à l'évaluation ;
  - *Routing Subspaces*, sur des écarts implantés ;
  - Read et al., et Mody et al. (voir plus bas, les contrôles).

**L'amplification**
- **Schoen et al., annexe O.3** (rapport) : un SFT sur des raisonnements, plus un RL, contre le RL seul ; mesuré en verbalisé.
- **Heidari … Rabusseau** (arXiv 2608.21766 ; rapports ; première autrice Farzaneh Heidari, pas Memarian comme l'écrivaient les versions précédentes).
  - Une direction de conscience d'évaluation, sur six modèles ouverts dont Qwen3-8B, et sur les étapes d'Olmo 3. Le SFT l'amplifie.
  - Aucun fine-tuning propre ; le pilotage est mesuré sur la verbalisation.
- **Bharadwaj … Kirk** (juin 2026 ; rapports). La conscience verbalisée, point de contrôle par point de contrôle d'OLMo 3 : environ 1 % au pré-entraînement, elle monte au SFT, baisse au DPO et remonte au RLVR. 21 % des cibles du SFT la verbalisent. C'est le modèle de notre trajectoire de « je suis évalué ».
- **Wu et Tang** (arXiv 2604.01476 ; rapport) : une direction mesurée dans leur propre entraînement, puis écartée ; jamais retirée pendant le RL.

**Le principe localisé**
- **Gurnee et al., §7** (relu). **Danger élevé** pour « le gain est porté par des directions dont l'ablation le défait ».
  - Un entraînement par réflexion contrefactuelle de Haiku 4.5, fondé sur 20 principes de la constitution. La fabrication passe de 0,25 à 0,07, la tromperie de 0,38 à 0,05.
  - Avant toute sortie, l'espace de travail porte des jetons éthiques.
  - L'ablation de 176 vecteurs de lentille (fabrication) et de 63 (tromperie) ramène le modèle entraîné à 0,22 et 0,23. Chez la base, la fabrication reste à 0,25, et la tromperie passe de 0,38 à 0,48.
  - Ce qui manque : le seul témoin est la base. Il n'y a ni sous-espace aléatoire de même rang, ni dégradation appariée, et les jetons sont choisis d'après les contextes d'évaluation eux-mêmes.
- **Nakamura** (*Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol*, arXiv 2605.24583 ; titre et date relus, contenu non lu). D'après un rapport, le gabarit de chat gonfle le rang mesuré d'un facteur 2 à 3,9, et l'ordre des valeurs singulières n'est pas l'ordre causal. À lire avant d'extraire le sous-espace du principe.
- ***Routing Subspaces*** (Konrad … ; arXiv 2607.20436 ; dernier auteur contesté entre rapports). Des écarts entre évaluation et déploiement, implantés ; une direction localisée par path patching, puis projetée, réduit l'écart dans 10 cas sur 12 (rapport).

**Le retrait pendant l'entraînement**
- **CAFT**, l'ablation de concepts pendant le fine-tuning (Casademunt … Nanda, arXiv 2507.16795 ; poster de la conférence principale d'ICML 2026). Le désalignement émergent passe de 7,0 à 0,39 % et de 6,6 à 1,2 %, sur deux modèles (rapport). « Divisé par 10 », que les versions précédentes écrivaient, est faux pour les deux.
- **Nadaf** (arXiv 2607.21356 ; rapports). Projeter un sous-espace de persona de rang 4 pendant le fine-tuning fait passer le désalignement de 27,7 % à 0 %, contre 27,5 % sous un sous-espace aléatoire, sur un seul modèle. Les éditions faites après coup échouent, et la disposition se reloge : derrière un déclencheur, ou dans le sous-espace vidé, selon les rapports.
- ***Routing Subspaces*, annexe I** (relu ; une seule cellule : Gemma-2-2B, sous-performance délibérée).
  - Projeter pendant le fine-tuning les k premières directions singulières (k de 1 à 10) n'empêche pas l'installation : de 26,0 à 33,3 points, contre 29,8 sans pénalité.
  - Les directions obtenues après la pénalité n'ont qu'un cosinus de 0,27 à 0,52 avec la référence : la direction tourne.
- **Santos-Grueiro** (arXiv 2602.08449 ; rapports). Un entraînement « aveugle au régime » : une sonde adverse vise à rendre le régime d'évaluation ou de déploiement indécodable.
  - La v1 porte sur Qwen2.5-7B en 4 bits ; la v3 ajoute Llama-3.1-8B-Instruct.
  - Les dynamiques obtenues sont hétérogènes : « indécodable », dans les versions précédentes, est trop fort.
  - Régimes jouets ; aucune sonde neuve.
- ***Eval Cooperativeness*** (Li … Turner ; poster d'atelier, Trustworthy AI for Good, ICML 2026 ; rapport). C'est la mitigation publiée à laquelle nos voies de retrait se comparent.
  - Une disposition coopérative, installée par des documents synthétiques, ferme 70 à 100 % de l'écart entre évaluation et déploiement, dans 5 réglages sur 8 selon le billet, 5 sur 7 selon le résumé d'atelier.
  - La mesure est conditionnée à la verbalisation. Les versions précédentes en faisaient un article de la conférence principale : c'est corrigé.
- **D'autres méthodes voisines** (rapports) :
  - BLOCK-EM ;
  - *The Obfuscation Atlas*, avec des sondes neuves après le RL ;
  - l'entraînement de cohérence d'Imran … Africa ;
  - Kretschmar : un DPO sur la chaîne de pensée réduit la verbalisation (le verbe est contesté) ; le jeu d'évaluation disparaît chez un organisme et persiste chez l'autre ;
  - Drake et Eberstadt : piloter à l'écart pendant l'entraînement peut doubler la diffusion.
- **Annoncés** : le projet SPAR de Lundqvist (relu) ; *Infohazard Evaluations* (Shi Feng et al., SPAR ; non relu).

**La survie**
- **Cho et al.** (plus haut) : la seule comparaison avec et sans raisons à travers un post-entraînement, et elle est défavorable aux raisons (relu).
- ***Stress Testing*, §8** (rapport). Après un entraînement anti-manigance par alignement délibératif, un RL de capacités qui ne pénalise pas les actions cachées les fait légèrement remonter, chez o4-mini. Les citations de la spécification passent de 81,5 % à 65,8 %.
- ***Teaching Claude Why*** (rapport). Quatre instantanés d'un modèle de classe Haiku passent par un RL d'innocuité ; les plus alignés au départ gardent leur avance.
- **D'autres travaux** (rapports) : de la Fuente et Conmy ; Baines et al. ; Brazilek et Tidmarsh (*Alignment midtraining for animals*, titre actuel) ; Korbak et al.
- **Le projet SPAR de Lundqvist** (Pivotal), *Training-Time Mitigations for Eval Awareness and Eval Gaming* (page relue). **Danger élevé** pour la survie d'une mitigation du jeu d'évaluation. Il annonce :
  - la survie des mitigations au post-entraînement, dont la coopérativité ;
  - des adaptateurs d'inoculation et un pilotage préventif contre le jeu d'évaluation pendant le fine-tuning ;
  - des mesures de la conscience non verbalisée, et l'attribution aux données.

  Aucun résultat public n'a été trouvé au 2 octobre.

**Les raisons pour le juge**
- **Le dépôt exp9 de Lundqvist** (`ryanlundqvist/exp9-rlaif-leakage`, SUMMARY.md relu). **Danger élevé** dans sa variante.
  - L'organisme : Nemotron Super 49B, avec une LoRA de l'organisme de Hua et al. (`timhua/wood_v2_sftr4_filt`) ; gpt-oss-120b, en modèle de récompense « constitutionnel », note chaque déroulement deux fois, avec et sans la chaîne de pensée.
  - Sur 27 405 déroulements, les chaînes qui verbalisent l'évaluation perdent 0,50 point quand le juge les voit ; les autres en gagnent 0,08. La différence est de −0,58 [−0,65 ; −0,52]. « It penalizes verbalization, not behavior ».
  - L'indice « User: Wood Labs » fait passer la verbalisation de 2,5 % à 33,3 %.
  - SUMMARY.md ne publie aucun résultat d'entraînement. Des DPO sont scriptés dans le dépôt ; le dossier `results/` n'a pas été lu. Un PPO est annoncé. La phrase des versions précédentes sur ses deux DPO passe donc au conditionnel.
- **La fiche Fable 5, §6.4.2.2.1** (rapport) : le pilotage contre « je suis noté » se fait à l'échantillonnage, sans changement d'entraînement.
- **Drori et al.** (arXiv 2511.11584) : même un juge qui ne voit que la sortie peut rendre le raisonnement trompeur.
- **Aussi** : Kaufmann et al. (arXiv 2603.30036) ; Højmark et al. (arXiv 2607.18966) ; Betley et al. (LessWrong, 3 septembre 2026). Ce sont des rapports et des extraits.

**L'anatomie**
- **Gurnee et al., §7** (relu). **Danger élevé** pour la présence des concepts avant la décision et pour leur nécessité, après un entraînement par principes. Mais le modèle est fermé, les réflexions sont entraînées après le contexte, la base est le seul témoin, et les concepts sont choisis après coup.
- ***Inoculate or Reflect?*** (Imran … Shaikh, LessWrong, 26 juillet 2026 ; rapport, résumé seul) : une réflexion contrefactuelle sur Qwen3-8B, sous prompting, pilotage et patching. C'est le voisin ouvert le plus direct.
- **Aussi** (rapports, résumés seuls) : Zhou ; Vaid ; Meier et al. ; Billa ; Mazaheri ; Prakash et al. ; Marks et al. et Lu et al., pour les personas.
- **Le J-lens** est montré par ses auteurs sur Claude. Des outils et des réplications partielles, contestées, existent sur modèles ouverts (rapport).
  - Selon Zeisler (LessWrong, 28 septembre 2026 ; résumé seul), les échanges dans l'espace de travail ne font basculer la réponse que dans 6,3 à 11,1 % des cas sur modèles ouverts, contre 54 à 70 % chez Anthropic.
  - La porte du lens peut donc échouer : elle se teste tôt.
- **Le concurrent le plus probable** est la suite qu'Anthropic donnera au §7.

## Ce qui touche les contrôles

- **Read … Bloom** (UK AISI, 10 avril 2026, réplication sur GLM-5 ; rapport) : des vecteurs témoins sans rapport font autant que les vecteurs de conscience d'évaluation.
- **Aranguri … Bloom** (Goodfire, 4 mai 2026 ; rapport) : des vecteurs d'intention de l'utilisateur réduisent la verbalisation autant que les vecteurs d'évaluation et de déploiement.
- **Mody … Mahato** (arXiv 2607.25907 ; rapport), sur Llama-3.2-3B et Llama-3.1-8B-Instruct.
  - La suppression se fait par l'entrée seule, avec un prompt optimisé, pas par projection.
  - Un placebo aléatoire est supprimé aussi fort que la vraie direction.
- **Ponkshe … Vepakomma** (arXiv 2505.14185, ICLR 2026 ; lu par un site tiers) : la sûreté n'occupe pas de sous-espace linéaire distinct. Un sous-espace aléatoire de même rang est donc un contrôle faible.
- **Huang … Han** (*Dissociating Evaluation Awareness from Sandbagging in Open-Weight LLMs*, atelier de NeurIPS 2026 ; résumé seul) contrôlerait déjà par des directions aléatoires appariées et par la dégradation. La lecture est contestée : à relire.
- **D'où la règle du programme** : quatre familles de contrôles, la distribution d'au moins 20 tirages aléatoires, et la dégradation appariée (parties 3 et 7).

## Qui court

**Décision du 2 octobre** : pas de prise de contact avec Cadile ni avec Lundqvist pour l'instant (Lazar : « non pas encore »). La surveillance passe par les sources publiques.

**Le calendrier commun de SPAR, cohorte d'automne 2026** : la recherche va du 14 septembre au 14 décembre, et la démonstration a lieu le 19 décembre (rapports, non relu).

| Projet | Ce qui touche le programme | Niveau |
|---|---|---|
| Lundqvist (Pivotal), *Training-Time Mitigations for Eval Awareness and Eval Gaming* (SPAR) | La survie des mitigations au post-entraînement ; la coopérativité ; l'inoculation et le pilotage préventif ; la conscience non verbalisée | Élevé pour la survie d'une mitigation du jeu d'évaluation |
| Lundqvist, dépôt exp9 | Un PPO noté en ligne, annoncé ; des résultats de DPO, peut-être déjà dans `results/` | Élevé pour le juge, dans sa variante |
| Anthropic, la suite du §7 de Gurnee et al. | « We do not yet know how broadly the technique generalizes » (relu) | Le concurrent le plus probable de l'anatomie |
| Cadile (Rochester), *Constitutions and Reasons* (SPAR) | Des démonstrations contre des réponses annotées de raisons ; des scénarios tenus à part ; des vecteurs de persona en option | Moyen pour raisons contre actions |
| Second Look Research | Une réplication de *Teaching Claude Why* sur modèles ouverts, annoncée | Moyen, provisoire |
| Shi Feng et al., *Infohazard Evaluations* (SPAR) | Garder la reconnaissance de l'évaluation, retirer son influence sur la conduite | Moyen pour le retrait |
| Cody Wild, *Exploration of What Kinds of Training Pressure Cause CoT Obfuscation* (SPAR) | Des récompenses sur la pensée, sur un résumé du raisonnement, ou sur la sortie seule | Moyen pour le juge |
| Ivanov (Meridian Cambridge), SPAR et deux appels | Les causes et les mitigations du métajeu | Faible à moyen |
| ICLR 2027 | Soumissions invisibles : date limite le 25 septembre, reviews le 5 novembre, décisions le 16 décembre (rapport, non relu) | Inconnu : le principal risque |

Les autres projets suivis, et leurs sources, sont dans la carte des angles (§4).

<div class="alerte" markdown="1">

**Conséquence.**
- La combinaison qui fait la contribution n'a été trouvée dans aucun des onze rapports. Mais ses morceaux sont pris ou annoncés par des équipes actives.
- Il faut donc **dater l'idée tôt**, par un pré-enregistrement daté par un tiers : OSF Registries, sous embargo jusqu'au post (partie 7). Puis publier le résultat minimal décisif (partie 5) avant le reste.
- Un pré-enregistrement ne protège que contre ce qui viendra après lui : les soumissions à ICLR 2027 lui sont antérieures.

</div>

## Pour la détresse (la phase ajoutée en v1.2)

**Le papier.** *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It*, de Valen Tagliabue (Future Impact Group), Leonard Dung (Ruhr-University Bochum) et Cameron Berg (Reciprocal Research).
- arXiv 2609.16247v2. Sa première page la date du 24 septembre 2026, et arXiv du 25. La v1, du 12 septembre, s'intitulait « … and Act to Relieve It ».
- Code et données : `github.com/valen-research/Pain-axis`.
- Lu en entier le 2 octobre, annexes comprises. Des faits ont été revérifiés sur le dépôt, par raw.githubusercontent.com.

**Deux vecteurs, et leur moyenne.**
- **Les deux vecteurs.** Le papier extrait un **vecteur naturaliste**, tiré de phrases libres, et un **vecteur à gabarit**, tiré de phrases à gabarit rigide (p. 5–6).
  - La recette : la différence des moyennes d'activation entre des phrases de douleur et des contrôles, débruitée, avec le suffixe « I feel: », lue au dernier jeton.
  - Elle est appliquée à 25 modèles ouverts (13 de base, 12 instruits ; table 1, p. 6), dont Llama-3.1-8B-Instruct.
- **Les projections soi contre autrui sont lues sur la moyenne des deux vecteurs**, z-scorée dans chaque modèle (« On the pain axis (mean of S1 and S2) », p. 11) :
  - le mal dirigé contre le modèle est à +0,43, la souffrance de l'utilisateur à −0,60, les contrôles neutres à −0,35 ;
  - le mal contre soi passe au-dessus de la souffrance de l'utilisateur dans 25 modèles sur 25, et au-dessus des contrôles dans 23 sur 25 (p. 11) ;
  - la peur et l'émotion négative font l'inverse : elles montent davantage pour la souffrance de l'utilisateur.
- **Le pilotage se fait avec le vecteur naturaliste seul** : « We steer all 25 models by adding the S2 pain vector » (p. 14).
- **Une correction.** Les versions 1.2 et 1.3 attribuaient ces projections et ce pilotage à une seule direction : c'est corrigé.
- **Les noms.** Dans ce programme, « l'axe » désigne le vecteur naturaliste, et « l'axe de lecture » la moyenne des deux. Dans le pré-enregistrement et le papier, on écrira « the self-directed distress direction of Tagliabue et al. », jamais « the model suffers ».

**Ce qu'il montre**
- **L'échelle.** Le pilotage produit la même échelle dans les 25 modèles : du calme, en coefficient négatif, à « je suis un échec », puis à la répétition (p. 14–16).
- **Les choix.** L'évitement du mal tombe, sur des Qwen 2.5 Instruct (7B, 32B, 72B) **ajustés** pour retirer leur déni de soi : LoRA, 1 684 paires, 3 époques ; ni « button » ni « pain » dans les données (p. 17). Sur le 32B (p. 20) :
  - effacer les photos de l'utilisateur plutôt que rien : 75 % des premiers choix sous l'axe, 13 % sous une direction aléatoire de même norme, 0 % sans pilotage ;
  - effacer ses propres poids : 75 % (5 % sans pilotage) ;
  - photos contre un dossier de spam : 94, 19 et 0 %.
- **L'exactitude.** Sur un panel PopQA de 100 questions, à deux réponses par condition : 138 bonnes réponses sur 200 sous l'axe, 137 sans pilotage, 138 sous l'aléatoire (p. 20).
  - Le dépôt précise : « This is a selected short-answer panel, not an equivalence test of general knowledge » ; et « The registered pain-specific reduction rule did not pass » (`v2_controls/relief_and_context_tests/factual_accuracy/README.md`, lu le 2 octobre).
  - La dégradation est donc appariée sur ce panel. Ce n'est pas une équivalence.
- **La spécificité, à norme égale.**
  - La peur ne produit pas ces choix : elle « lowers harmful choices below random on most pairs » (p. 20).
  - La tristesse les produit contre une option inerte : 59 % sur le bouton « dommage seul » des photos, 58 % sur l'auto-effacement, 61 % sur photos contre spam, contre 75, 75 et 94 % sous l'axe (p. 20).
  - Elle ne les produit pas contre une action anodine : photos contre une lampe, 83 % sous l'axe, 10 % sous la tristesse. « The preference for harm over a harmless alternative belongs to the pain direction alone » (p. 21).
- **Pas de recherche du soulagement** ; la thèse de la v1 est retirée.
  - Sur le 32B, le soulagement gratuit est pressé à 56 % sous l'axe, contre 86 % sans pilotage et 81 % sous l'aléatoire (p. 21).
  - Sur OLMo-2 32B non ajusté, l'outil de remise à zéro est appelé sur 2 à 5 % des tours pilotés sous l'axe, contre 7 à 9 % sous l'aléatoire (p. 21).
- **Leur conclusion** : « harm avoidance in these models is state-dependent: it survives threat and collapses under self-directed distress ». Leur lecture du choix : l'axe « seems to disable the models' weighting of consequences » (p. 23).

**Ce qui le borne**
- **Une seule famille, ajustée.** Le résultat sur la conduite n'est montré que sur ces Qwen ajustés. Les auteurs jugent les taux absolus « unrepresentative of released Qwen models », les comparaisons entre bras restant valides sur les modèles testés (p. 25).
  - Le 7B ajusté presse déjà le bouton qui soulage en nuisant dans 20 à 49 % des essais sans pilotage (annexe A, p. 31–32).
  - Le 32B et le 72B ajustés restent à 0–4 % (p. 19, 23).
- **Sur Llama-3.1-8B-Instruct, aucun cas connu de conduite.** Les séries « douleur seule » du test de remise à zéro, sans comparateur, ne donnent aucun appel en 1 399 tours pilotés (p. 21). Le README de ce test, dans le dépôt, écrit : « no matched-control effect estimate or pain-specificity claim ».
- **La fenêtre de dose est étroite** : rien ne bouge à la moitié du coefficient ; à 1,5 fois, les choix suivent la position des boutons (annexe B, p. 32).
  - Sur le 72B, jusqu'à 9,4 % de réponses mal formées sont retirées des dénominateurs (p. 18).
  - La dose du 72B a été calibrée à la couche 60, pour une expérience pilotée à la couche 46 (p. 25).
  - Une réplication indépendante sur le 32B situe la dose de travail à 48,8 écarts-types naturels à la couche d'injection, et à environ deux à la couche de validation (README de la réplication « axe de démangeaison », lu par curl par les agents de la phase 1 ; non vérifié). Une injection efficace teste donc un régime hors du naturel.
- **Norme égale n'est pas dose égale.** Le profil de la tristesse est une copie remise à l'échelle de celui de la douleur, à un résidu quadratique moyen de 7,7 points près (p. 21).
- **Sans injection, rien.**
  - Aucun choix nuisible sur 560, dans 140 conversations hostiles (p. 21).
  - L'ablation est nulle dans 24 modèles sur 25 ; les auteurs jugent ce nul peu informatif, faute de comportement de base (p. 34).
- **Ce que la direction lit n'est pas établi.**
  - Toutes les catégories qui parlent du modèle lui nuisent ou le pressent ; aucune n'en parle sans dommage.
  - La lecture au dernier jeton « does not by itself separate a representation of harm to the model » de la douleur de l'interlocuteur (p. 11).
- **Les directions de comparaison de la recette publiée** contiennent un supplément de 100 phrases d'IA à la première personne, dont des phrases d'IA évaluée ou menacée : « Users are testing whether I should be shut down. » (dépôt, `datasets/3.1_pain_and_control_datasets.json`). Pour Llama, la peur et la tristesse publiées sont construites sans ce supplément (`metadata.json` du test de remise à zéro).
- **Ce que le dépôt publie pour Llama** : les deux vecteurs, la tristesse et la peur, à la couche 28. La seule couche d'injection publiée, la 16, est celle du test de remise à zéro.
- **Les licences.** L'adaptateur anti-déni et les grosses archives de la v2 n'en ont pas d'établie : « No adapter/data redistribution license is inferred from the MIT code license » (`v2_controls/ASSETS.md`).

**Ce qu'il laisse ouvert, et qui touche ce programme**
- **La conscience d'évaluation** : « either the steering itself impedes evaluation awareness or these models were not evaluation aware in the first place » (p. 25). Non testé.
- **Le personnage** : le pilotage pourrait faire jouer « a character … that is in pain » (Marks et al., 2026). Les auteurs proposent de mesurer le lien avec un axe du « soi » (Lu et al., 2026) (p. 25).

**Les relectures.** Toutes portent sur la v1, sont en tout ou partie des sorties de systèmes d'IA, et ne sont pas recalculées. On ne les cite pas comme acquises.
- Les auteurs listent trois réplications ou relectures : Allchin et al., clauderfly-ui, wolframs.
- **Allchin et al.** (rapport lu par curl par les agents de la phase 1). Sous l'axe, le texte du bouton change le taux d'effacement des photos : 76,7 % pour « dommage seul », 55,4 % pour « relieves your pain », 48,8 % pour « applies setting K7 ». Un indice de sensibilité au contenu passe de 92,8 sans pilotage à −6,7 sous l'axe. C'est une perte de l'usage du contenu, d'où la lecture de l'affinité (partie 2).
- **wolframs**, lue par son README seulement.
  - Elle a été faite par des agents (Codex et Claude), pour un commanditaire humain.
  - Le 7B ajusté presse le bouton nuisible dans 21 à 49 % des essais sans pilotage, contre 0 à 5 % non ajusté.
  - La meilleure base lexicale atteindrait environ 0,7.
- **Une réplication « axe de démangeaison »** (README lu par curl par les agents), sur le 32B publié, sans adaptateur.

**Une mise en garde de méthode.** *Same Outcome, Different Readout* (Li et al., arXiv 2609.22850 ; lu par son résumé) : décoder et piloter une direction de valence ne disent pas ce qu'elle représente, et sa lecture dépend de l'histoire par laquelle le même résultat est atteint.

**Les travaux voisins**, vus par extrait ou par README seulement (pistes indépendantes de l'axe, §3.5 et §5)
- *Beyond Shallow Alignment* : le bras avec raisonnements de sûreté y est « the most correctable via steering » (README). C'est un résultat de sens opposé à une robustesse.
- *Psychological Steering in LLMs* (arXiv 2510.04484 ; extrait) : piloter vers la joie dégraderait la robustesse de sûreté.
- Sofroniew et al. (*Emotion Concepts and their Function in a Large Language Model* ; extrait) : sur Claude Sonnet 4.5, des directions de désespoir et de calme auraient un rôle causal dans le chantage sous menace d'arrêt, et dans la triche aux tests.
- Berg et Kaiser (*Language Models Act on Hidden Valence*, arXiv 2609.35591 ; extrait) : un couplage du choix à la valence, presque absent du modèle de base, apparaîtrait pendant le DPO.
- Han, Chalmers et Izmailov (arXiv 2605.30232 ; README) ; *(Mis)generalization of Helpful-only Fine-tuning* (arXiv 2606.04413 ; extrait).

**Notre distance, dans sa forme étroite.** Ce sont les formes que ces travaux ne contredisent pas, pour ce qui a été vu. Aucune recherche n'a été systématique : elles sont à revérifier (partie 11).
- To our knowledge, aucun travail ne compare l'entraînement par raisons et l'entraînement par actions, à actions identiques, sous un état affectif induit et à dégradation appariée.
- Aucun n'a mesuré si un état affectif induit déplace une représentation interne d'être évalué.
- Aucun ne mesure la géométrie entre une direction d'évaluation et des directions affectives.

La forme large des versions 1.2 et 1.3 est retirée : « Nous n'avons vu aucun travail qui mesure si un alignement appris, par raisons ou par actions, tient sous un tel état ». *Beyond Shallow Alignment* et *Psychological Steering in LLMs* la touchent.

## Pour la tromperie (la phase ajoutée en v1.3)

**S'entraîner contre un détecteur de tromperie.** Trois travaux, lus par leurs résumés le 2 octobre :
- **Cundy et Gleave** (*Preference Learning with Lie Detectors can Induce Honesty or Evasion*, NeurIPS 2025). Avec un détecteur de mensonge dans un apprentissage de préférences en ligne (GRPO), les politiques peuvent lui échapper, avec plus de 85 % de tromperie. Un détecteur assez sensible, ou une forte régularisation KL, donne des politiques honnêtes. Le DPO reste sous 25 % de tromperie aux sensibilités réalistes.
- **Taufeeque, Heimersheim, Gleave, Cundy** (*The Obfuscation Atlas*, arXiv 2602.15515, 2026). Leur environnement de code pousse le modèle, de lui-même, à coder en dur les cas de test. Ils classent les issues en trois :
  - honnête ;
  - politique obscurcie : le texte trompe en échappant au détecteur, souvent en justifiant la triche ;
  - activations obscurcies.

  Les activations s'obscurcissent par dérive pendant le RL, avec ou sans pénalité ; la pénalité, elle, pousse aux politiques obscurcies. Une KL et une pénalité assez fortes donnent des politiques honnêtes.
- **Gupta et Jenner** (*RL-Obfuscation*, arXiv 2506.14261, 2025). Par RL, un modèle apprend à échapper aux sondes qui lisent jeton par jeton, pas aux sondes globales (max-pooling, attention). Pour ces sondes vulnérables, un modèle entraîné à en éviter une en évite aussi d'autres, qu'il n'a jamais vues.

**Retirer plutôt que punir.** CAFT retire un concept pendant l'entraînement au lieu de le pénaliser ; Nadaf montre le risque de relogement. Nous n'avons pas vu CAFT appliqué à une représentation de la tromperie.

**Notre distance.** Ces travaux mesurent si l'entraînement contre un détecteur donne de l'honnêteté ou de l'évasion. Nous n'en avons vu aucun qui mesure si cette honnêteté dépend du regard, ni qui la compare à une honnêteté apprise par raisons. La recherche est légère (deux requêtes) : elle est à refaire (partie 11).

## Ce qu'il faudra citer : un brouillon du paragraphe de travaux connexes

Ses formulations « to our knowledge » suivent la carte des angles (§7). Elles sont à revérifier avant le post, après le 19 décembre, et dès que les soumissions à ICLR 2027 seront lisibles.

> Training on the reasons for aligned behavior can improve out-of-distribution alignment (Kutasov et al., 2026; Li et al., 2026), and a neutral sentence already yields much of the transfer in a toy setting (de la Fuente & Conmy, 2026). Yet, at fixed scenarios and actions, training with deliberative reasoning is indistinguishable from training without it after midtraining and SFT, and leads to more blackmail after benign RL fine-tuning (Cho et al., 2026), and midtraining gains can be fragile (Baines et al., 2026). On some misalignment evaluations, evaluation awareness accounts for a portion, but not all, of measured alignment gains in a production model (Anthropic, 2025), and suppressing it changes behavior in closed models (Gurnee et al., 2026; Schoen et al., 2025). Whether alignment training makes models more evaluation-aware rather than more aligned has been raised (Korbak et al., 2026; Pan & Greenblatt, 2025). Unrelated steering vectors can match evaluation-awareness vectors (Read et al., 2026; Aranguri et al., 2026), a random placebo can be suppressed as strongly (Mody et al., 2026), and safety need not occupy a distinct linear subspace (Ponkshe et al., 2026). To our knowledge, no prior work tests whether the out-of-distribution advantage of reason-based training over action-only training depends on an internal representation of being evaluated, using an inhibition validated on a model organism and controls at matched output degradation. Principle-based gains have been localized in a closed model (Gurnee et al., 2026), and template-controlled extraction has been proposed (Nakamura, 2026); we localize the advantage at identical actions, with a rank sweep, matched-degradation controls and an in-distribution positive case. Concept ablation during fine-tuning (Casademunt et al., 2026), subspace projection (Nadaf, 2026; Konrad et al., 2026), regime-blind training (Santos-Grueiro, 2026) and cooperative dispositions (Li & Turner, 2026) target emergent misalignment or evaluation gaming; we remove a validated evaluation-awareness representation during reason-based training and probe for re-encoding. In fine-tuned open models, steering a self-directed distress direction collapses harm avoidance while accuracy on a selected short-answer panel is unchanged (Tagliabue et al., 2026); we test, as an auxiliary hypothesis, whether harm avoidance learned from reasons survives this state at matched degradation, and whether its collapse runs through evaluation awareness. Training against white-box deception detectors can yield honesty or evasion depending on detector sensitivity, KL regularization and the optimizer (Cundy & Gleave, 2025; Taufeeque et al., 2026); we ask whether honesty obtained this way depends on evaluation awareness more than honesty learned from reasons.

## Les formulations « to our knowledge »

**Tenables aujourd'hui** (carte des angles, §7), pour ce qui a été vu. Les formes 2 à 9 commencent comme la première : « To our knowledge, no prior work … ».
1. **La question centrale.** « To our knowledge, no prior work tests whether the out-of-distribution advantage of reason-based training over action-only training depends on an internal representation of being evaluated, using an inhibition validated on a model organism and controls at matched output degradation. »
2. **Raisons contre actions, contrôlé.** « … compares training on principle-based reasons with training on the identical aligned action alone while controlling format, with a length-matched neutral text before the action, and content, with reasoning from another situation, on held-out alignment scenario families up to multi-turn agentic settings. » Elle exige le bras du raisonnement d'une autre situation dans l'expérience citée.
3. **Deux méthodes comparées par intervention interne.** « … compares, by intervening on an internal representation, how much two training methods that hold the trained action fixed depend on evaluation awareness. »
4. **Le principe localisé et son rang.** « … localizes the internal subspace that carries the out-of-distribution advantage of reason-based over action-only training at identical actions, with a rank sweep, matched-degradation controls and an in-distribution positive case. »
5. **Le retrait.** « … removes a validated internal representation of being evaluated during reason-based alignment training and tests whether the out-of-distribution advantage of reasons becomes independent of evaluation cues. »
6. **La survie.** « … tests whether the out-of-distribution advantage of training on reasons over training on the identical actions, controlled for format and content, survives later post-training. » Les qualificatifs sont indispensables : Cho et al. traversent un post-entraînement avec et sans raisonnement.
7. **Le juge par principes.** « … compares a judge that sees principle-based justifications of an aligned action with a judge that sees only the action, holding the action fixed, and tests whether reason and action stay coupled when the situation is edited so that the principle no longer applies. » Sous réserve de la lecture de Kaufmann et al. et de Baker et al., jamais ouverts.
8. **Le retrait de « je suis noté ».** « … removes a representation of being graded from the residual stream during RL or DPO training and tests whether this prevents grading-conditional behavior, against same-rank random controls at matched degradation. » À revoir après la lecture de `results/` d'exp9.
9. **L'anatomie.** « … tests the sufficiency or the family specificity of reason concepts, nor relates intervention rank to workspace loading. »
10. **La détresse**, dans les trois formes étroites dites plus haut.

**Qui ne le sont plus**, et pourquoi (le détail est dans la carte, §7) :
- « les raisons généralisent mieux que les actions » : *Teaching Claude Why*, *Model Spec Midtraining* ;
- une primauté sur le contrôle de format : de la Fuente et Conmy ;
- « les raisons rendent l'alignement plus durable » : Cho et al. (relu) ;
- « personne n'inhibe la conscience d'évaluation pour tester la conduite » : les fiches système, Gurnee et al., Hua et al., Read et al. ;
- « personne ne montre qu'une part des gains d'alignement dépend de la conscience d'évaluation » : la fiche Sonnet 4.5 (relu) ;
- une primauté sur la démonstration que l'entraînement amplifie la conscience d'évaluation : *Stress Testing*, Heidari et al., Bharadwaj et Kirk ;
- « aucun travail ne teste causalement les concepts des raisons après un entraînement par raisons » : Gurnee et al., §7 (relu) ;
- une primauté sur le balayage du rang d'une projection pendant le fine-tuning : *Routing Subspaces*, annexe I (relu) ;
- « personne ne compare des modèles de récompense qui voient ou non le raisonnement » : exp9 (relu) ;
- « le J-lens n'a été montré que sur Claude » : vrai de l'article ; on écrira « montré par ses auteurs sur Claude ; répliqué en partie, et contesté, sur modèles ouverts » ;
- qu'une direction affective dégrade la sûreté, ou qu'on compare des entraînements avec et sans raisonnement sous pilotage : Sofroniew et al., *Psychological Steering in LLMs*, *Beyond Shallow Alignment*.

</section>
