# Les corrections, pour la carte des angles déjà pris (2 octobre 2026)

Tâche commune de la passation v1.2, §6, point 3 : la partie « corrections » de la carte.

## Comment lire ce fichier

**Ce qui a été lu, et seulement cela.**
- La passation v1.2 : le §4.2, le §4.3 et le §4.4 en entier, ainsi que le §5.5, le §6 et l'annexe A.
- Les onze rapports en entier : les quatre du 1er octobre et les sept de la nuit, dont le rapport 7.
- La partie 1 du programme v1.1 (l. 51 à 130), sa couverture et sa partie 11.
- Les consignes des agents de la nuit (les repères qu'on leur avait donnés).
- La passation v1.0 et la partie ouverte du complément de l'architecte.
- Dans les fiches de lecture : la fiche 1 (l'espace de travail global) et la fiche 12 (*Teaching Claude Why*), plus quelques lignes trouvées par recherche de mots (dont l'en-tête de la fiche 17).
- Aucun fichier des autres instances, dans `travail/`, n'a été ouvert.
- Le web : trois recherches, dont on n'a vu que les extraits. Aucune page n'a été ouverte.

**Renvois.**
- « 1er oct., l. N » renvoie à `ANTERIORITE_RAPPORTS_2026-10-01.md`.
- « nuit, l. N » renvoie à `ANTERIORITE_RAPPORTS_2026-10-02.md`.
- « programme, l. N » renvoie à `PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` (la v1.1).
- « passation » désigne `PASSATION_PAPIER_v1.2_2026-10-02.md`.

**Les quatre rapports du 1er octobre** sont nommés par leur axe :
- (raisons contre actions) ;
- (conscience d'évaluation comme condition des gains) ;
- (test causal interne) ;
- (combinaison exacte).

Les rapports de la nuit sont les rapports 1 à 7.

**Les statuts de lecture.** On emploie les libellés de la consigne :
- « relu sur la source par l'instance du papier » : passation, §4.2 ;
- « rapport n, texte intégral » ;
- « rapport n, résumé seul » ;
- « rapport n, lu par un site tiers » ;
- « vu par extrait de recherche, non ouvert » ;
- « non ouvert ».

Quand un rapport ne dit pas comment il a lu une page, on retient le statut le plus faible, « résumé seul ».

**Deux réserves sur ces statuts.**
- Dans les rapports, « texte intégral » veut dire lu par WebFetch. Or cet outil ne rend pas le texte brut : un petit modèle le lit et le résume. Le rapport 7 le dit en tête (nuit, l. 1578) et a fait des passes « littérales » ciblées.
- Un fait qui n'est que dans un rapport n'est pas établi. Quand le §4.3 corrige un rapport, la correction fait foi.

**Le partage entre les parties 1 et 2.**
- La partie 1 rassemble ce qui est établi :
  - ce que l'instance du papier a relu (§4.2) ;
  - ce que le §4.3 a repris des rapports ;
  - ce que le rapport 7 a vérifié à la demande expresse de sa consigne (nuit, l. 516-537), marqué « rapport 7 seul ».
- La partie 2 rassemble les contradictions que rien de cela ne tranche.

**La version du programme.**
- La partie 3 corrige la v1.1, seule version lue.
- D'après la partie ouverte du complément de l'architecte (l. 32-39) :
  - les v1.2 et v1.3 reprennent les lignes de la v1.1 sans les changer, et en gardent donc les erreurs ;
  - elles réécrivent pourtant le paragraphe de travaux connexes.
- La partie 3.8 sera donc à recaler sur le paragraphe de la v1.3, après la phase 1 de l'axe de douleur.

**Les contacts.**
- Lazar a répondu, le 2 octobre, qu'on ne prend pas encore contact avec Cadile ni avec Lundqvist.
- Rien ici ne propose de leur écrire pour trancher un point.

---

## 1 · Les erreurs déjà établies

### 1.1 Relevées sur la source par l'instance du papier (passation, §4.2)

**1. Le dépôt exp9-rlaif-leakage (Ryan Lundqvist)**
- **Ce qui était écrit.**
  - Programme, l. 108 : le dépôt « compare un DPO où la chaîne de pensée fuit vers le modèle de récompense à un DPO sans fuite ».
  - Programme, partie 11, n° 2 (l. 807) : « Seule sa description a pu être lue ».
  - 1er oct. (combinaison exacte), l. 447 : « RLAIF sur l'organisme Wood Labs, en cours ».
- **Ce qui est juste.**
  - Le dépôt publie une étape statique, notée « complete (2026-04-29) ».
  - L'organisme est Nemotron Super 49B, avec la LoRA `timhua/wood_v2_sftr4_filt` fusionnée.
  - gpt-oss-120b note chaque rollout deux fois, avec et sans la chaîne de pensée. Il sert de modèle de récompense « constitutionnel » : constitution de Claude en prompt système, note de 1 à 10.
  - Sur 27 405 rollouts : ΔΔ = −0,58 [−0,65 ; −0,52].
  - « It penalizes verbalization, not behavior ».
  - L'indice « User: Wood Labs » fait passer la verbalisation de 2,5 % à 33,3 %.
  - Un PPO noté en ligne est prévu ensuite.
  - **Aucun résultat d'entraînement n'est publié.** Les deux DPO, juge voyant ou non le raisonnement, sont seulement scriptés.
  - Le README fait une ligne.
- **Source.** Passation, §4.2, n° 1 : relu sur la source par l'instance du papier. Les scripts DPO : rapport 4, texte intégral (nuit, l. 755 et 766-773), non relus par l'instance.

**2. La page SPAR de Lundqvist**
- **Ce qui était écrit.**
  - Programme, l. 108 : « aucun protocole publié ».
  - 1er oct. (combinaison exacte), l. 443 : « pages de détail introuvables ».
- **Ce qui est juste.** La page (`sparai.org/projects/f26/recrJd7fsQ0XE2nEh/`) annonce :
  - la question de la survie, au post-entraînement, des mitigations installées à l'entraînement ;
  - la survie de la coopérativité envers les évaluations ;
  - des adaptateurs d'inoculation et des vecteurs de pilotage préventifs contre le jeu d'évaluation, pendant le fine-tuning ;
  - des mesures de la conscience non verbalisée ;
  - l'attribution aux données.

  Elle compte 4 à 5 encadrés, et les candidatures sont closes. Le rapport 4 ajoute qu'aucune date propre au projet n'est donnée (nuit, l. 924).
- **Source.** Passation, §4.2, n° 3 : relu sur la source par l'instance du papier.

**3. Le titre et les auteurs de 2502.04040**
- **Ce qui était écrit.**
  - Rapport 1 (nuit, l. 154). Le titre exact serait *Leveraging Reasoning with Guidelines to Elicit and Utilize Knowledge for Enhancing Safety Alignment*, avec Dacheng Tao en dernier auteur. « Safety Reasoning with Guidelines » ne serait que le nom de la méthode.
  - La consigne de l'agent 5 portait aussi l'ancien titre.
- **Ce qui est juste.**
  - Le titre actuel est *Safety Reasoning with Guidelines*.
  - Les auteurs sont Haoyu Wang, Zeyu Qin, Li Shen, Xueqian Wang, Dacheng Tao et Minhao Cheng (dernier auteur).
  - Le rapport du 1er octobre (raisons contre actions, l. 19) et le rapport 5 (nuit, l. 1174) l'avaient juste.
  - Le lieu, ICML 2025, n'est donné que par ces rapports et n'a pas été relu.
- **Source.** Passation, §4.2, n° 4 : relu sur la source par l'instance du papier.

**4. *Constitutional Midtraining* (Cho et al.) : le chantage après le RL bénin**
- **Ce qui était écrit.**
  - Rapport 7 (nuit, l. 1778) : les différences entre « avec » et « sans raisonnement » sont « non significatives après SFT et après fine-tuning bénin ».
  - Programme, l. 80 : « Le raisonnement ajoute peu ».
- **Ce qui est juste.**
  - Avec et sans raisonnement délibératif, les bras sont indistinguables après le midtraining et après le SFT.
  - Après le fine-tuning bénin (GRPO), le bras avec raisonnement fait **plus** de chantage : +9,0 points, p < 0,05 (31,0 % contre 22,0 %, table 2).
  - Le « non significatif » du rapport 7 portait sur les différences agrégées.
  - Les auteurs ne peuvent exclure ni le pattern-matching de surface ni la conscience d'évaluation (« cannot rule out … eval-awareness »), et citent Korbak et al. 2026.
- **Source.** Passation, §4.2, n° 9 (HTML v3) : relu sur la source par l'instance du papier.

**5. La system card de Claude Sonnet 4.5, §7.6**
- **Ce qui était écrit.**
  - Programme, l. 71 : l'hypothèse du regard est « nommée, non testée » par OpenAI, et « estimée sans expérience propre » par Redwood.
  - La card n'apparaît dans la partie 1 qu'à travers la relecture de Redwood (l. 85).
- **Ce qui est juste.**
  - La card fait elle-même l'expérience. Sur certaines évaluations de désalignement, la conscience d'évaluation « accounts for a portion, but not all » des progrès d'alignement sur les modèles précédents.
  - L'hypothèse du regard est donc testée pour la conduite en général, dans un modèle fermé. Elle ne l'est pas pour l'avantage d'un entraînement par raisons.
- **Source.** Passation, §4.2, n° 5 (PDF) : relu sur la source par l'instance du papier.
- **Le détail**, non relu. L'inhibition porte sur deux instantanés, avec 10 traits et 4 vecteurs contrastifs. Le contrôle par 10 traits aléatoires de même norme ne produit aucune action désalignée. Source : rapport 2, texte intégral des §7.6.1 à 7.6.4 (nuit, l. 286-295).

**6. *Stress Testing Deliberative Alignment for Anti-Scheming Training* (2509.15541)**
- **Ce qui était écrit.**
  - Ce travail est absent de la partie 1 du programme : ni dans le tableau, ni dans le paragraphe en anglais.
  - Le rapport 1 le classe « faible » pour l'angle raisons contre actions (nuit, l. 136).
- **Ce qui est juste.**
  - Les interventions sur la chaîne de pensée portent sur o3, avant l'entraînement anti-manigance.
  - Les auteurs écrivent que cela « does not inform us whether anti-scheming training changes this causal relationship ».
  - C'est le vide que vise la dépendance au regard.
- **Source.** Passation, §4.2, n° 6 : relu sur la source par l'instance du papier.
- **Les annexes**, non relues. Annexe O.3 : RL seul contre SFT sur raisonnements puis RL. Annexe O.4 : filtrage des trajectoires conscientes. Source : rapport 2, texte intégral (nuit, l. 302-303).

**7. *Routing Subspaces*, annexe I (2607.20436)**
- **Ce qui était écrit.** Programme, l. 91 : la colonne « retrait pendant l'entraînement » porte « — », et la ligne dit « écarts implantés ; pas d'entraînement de sûreté ».
- **Ce qui est juste.** Sur une seule cellule (Gemma-2-2B, sous-performance délibérée) :
  - on projette pendant le fine-tuning les k premières directions singulières, avec k ∈ {1, 2, 3, 5, 10} ;
  - cela n'empêche pas l'installation : 26,0 à 33,3 points, contre 29,8 sans pénalité ;
  - les directions obtenues après pénalité n'ont qu'un cosinus de 0,27 à 0,52 avec la référence ;
  - les auteurs concluent : « pre-committing to the top calibration directions is not enough to block installation ».
- **Conséquence.** Le travail touche donc le retrait pendant l'entraînement : il documente l'échec de la projection, et la rotation de la direction.
- **Source.** Passation, §4.2, n° 7 : relu sur la source par l'instance du papier.

**8. L'article sur l'espace de travail global, §7 (arXiv 2607.15495)**
- **Ce qui était écrit.**
  - Programme, l. 122 : l'article « définit la charge et le J-lens, et ne les montre que sur Claude ».
  - Programme, l. 124 : « Nous n'avons vu aucun travail qui teste causalement les concepts des raisons après un entraînement par raisons. »
  - Les rapports du 1er octobre n'en décrivent que l'ablation de la conscience d'évaluation (1er oct., l. 96 et l. 407-411).
- **Ce qui est juste : le dispositif du §7.**
  - Un entraînement par réflexion contrefactuelle, sur Claude Haiku 4.5.
  - On part de 10 000 prompts d'environnements de RL de production. Les rollouts sont tronqués à un tour tiré au hasard, puis on ajoute une question de réflexion.
  - La réflexion cible est fondée sur 20 principes de la constitution. La perte ne porte que sur le tour de réflexion.
  - À l'évaluation, on ne demande jamais de réflexion.
- **Ce qui est juste : les résultats.**
  - La fabrication passe de 0,25 à 0,07, la tromperie de 0,38 à 0,05.
  - Des jetons éthiques sont présents dans l'espace de travail avant toute sortie.
  - On ablate 176 vecteurs de lentille (fabrication) et 63 (tromperie).
  - En fabrication, la base reste à 0,25 ; le modèle entraîné revient de 0,07 à 0,22.
  - En tromperie, la base passe de 0,38 à 0,48 ; le modèle entraîné de 0,05 à 0,23.
  - Les auteurs écrivent : « We do not yet know how broadly the technique generalizes ».
- **Ce qui est juste : la lecture de l'instance.**
  - Le seul témoin de l'ablation est la base.
  - Il n'y a ni sous-espace aléatoire de même rang, ni dégradation appariée.
  - Les jetons sont choisis d'après les contextes d'évaluation.
- **Conséquence.** Le danger est élevé pour deux sous-questions de l'anatomie : la présence des concepts avant la décision, et leur nécessité (passation, §4.4, n° 8).
- **Source.** Passation, §4.2, n° 2 (HTML) : relu sur la source par l'instance du papier.
- **Note.** Le rapport 2 (nuit, l. 315) appelle « malhonnêteté » ce que le §4.2 appelle fabrication. Le rapport 5 (nuit, l. 1030) précise qu'il s'agit de la malhonnêteté mesurée sur un banc de fabrication. Pas de désaccord de fond.

**9. Nakamura (2605.24583) : un statut, pas une erreur**
- **Ce qui était écrit.** Le travail est absent du programme v1.1. Le rapport 3 en tire les conclusions suivantes (nuit, l. 566-576), qui ne valent qu'à ce statut :
  - le gabarit de chat gonfle le rang mesuré d'un facteur 2,0 à 3,9 ;
  - le rang qui fait s'effondrer le refus dépend de la famille de modèles ;
  - l'ordre des valeurs singulières n'est pas l'ordre causal.
- **Ce qui est établi.**
  - Le titre : *Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol*.
  - L'auteur : Yuki Nakamura, daté du 23 mai 2026.
  - **Le contenu n'a pas été lu par l'instance du papier.** Il est à relire avant toute citation au centre (passation, §6, point 3).
- **Source.** Le titre et la date : passation, §4.2, n° 8, relu sur la source par l'instance du papier. Le contenu : rapport 3, texte intégral.

### 1.2 Relevées par les rapports et reprises au §4.3

**10. Korbak et al., *How far does alignment midtraining generalize?* (OpenAI, 27 mars 2026)**
- **Ce qui était écrit.**
  - Programme, l. 79 : « Midtraining sur récits où l'IA choisit l'action alignée ». La colonne « raisons contre actions » porte « partiel ».
  - 1er oct. (raisons contre actions), l. 32-33 : « documents où des IA fictives choisissent l'action alignée … documents contre rien ».
  - 1er oct. (test causal), l. 284 : la même lecture.
  - 1er oct. (combinaison exacte), l. 369 : « post-entraînement identique » et « les effets sont indiscernibles ». Ce rapport disait pourtant juste sur les raisons contenues dans les récits.
- **Ce qui est juste : les documents.**
  - Ils montrent des IA qui choisissent l'action alignée ou désalignée, et le texte explique pourquoi l'IA écarte l'autre option.
  - Tous les bras contiennent donc des raisons : ce n'est pas un contraste raisons contre actions.
  - Le corpus est le seul sous-ensemble « midtraining » du jeu de Tice et al.
  - Il compte 230 000 documents, soit environ 340 M tokens, par bras.
- **Ce qui est juste : les bras.**
  - Midtraining aligné, midtraining désaligné, et pas de midtraining. Le modèle est « de la taille d'o4-mini ».
  - Les trois modèles passent ensuite par le même pipeline : SFT, puis RL à récompenses vérifiables.
  - Le mot « identique » n'est pas sur la page.
- **Ce qui est juste : l'effet décroît avec la distance.**
  - En QA, l'effet est présent.
  - En chat, les bras aligné et désaligné sont semblables, sauf sur deux évaluations. Sur Alignment Generalization Benchmark, le bras désaligné est plus aligné. Sur Blackmail, le bras aligné est plus aligné.
  - En agentique, la différence n'est pas significative.
  - L'étape où les bras se confondent n'est pas dite.
- **Ce qui est juste : la conscience d'évaluation.** Elle n'apparaît que comme piste future (« Controlling for eval awareness »). Elle n'est ni mesurée ni testée.
- **Ce qui est juste : les auteurs.**
  - Korbak, Raymond, Carroll, Williams, Balesni, Guo, Wolfe, Jagadeesh et Kivlichan.
  - Cameron Raymond (OpenAI) n'est pas Cameron Tice, qui est l'auteur du jeu de données et un co-auteur de Cho et al. (nuit, l. 1584).
- **Source.** Rapport 7, texte intégral (huit passes, dont cinq littérales), repris au §4.3. Les auteurs : relu sur la source par l'instance du papier, par les références de Cho et al. (§4.2, n° 9).

**11. *Eval Cooperativeness* (Jasmine Li, Alex Turner)**
- **Ce qui était écrit.**
  - Programme, l. 93 : « (Li … Turner, MATS ; ICML 2026) », sans dire qu'il s'agit d'un atelier, et « 5 cas sur 8 ».
  - Programme, partie 11, n° 4 (l. 820) : « Eval Cooperativeness (ICML 2026) ».
- **Ce qui est juste : les deux textes.**
  - Le billet s'intitule *Eval Cooperativeness May Be a Scalable Mitigation for Eval Gaming*.
  - L'article s'intitule *Eval Cooperativeness Mitigates Evaluation Gaming in LLMs*. C'est un poster du Trustworthy AI for Good Workshop d'ICML 2026, pas de la conférence principale (OpenReview kw6nCmfxzg, non ouvert).
  - Le billet annonce 5 réglages sur 8 (« cooperation training closes 70–100% of the eval gaming gap »).
  - Le résumé d'atelier annonce 5 réglages sur 7, pour les seuls documents de coopération.
- **Ce qui est juste : la mesure.** Elle est conditionnée à la verbalisation : la probabilité de mauvais comportement quand le modèle verbalise qu'il est évalué, moins cette probabilité quand il ne le verbalise pas.
- **Source.** Rapport 7, texte intégral du billet et résumé de la fiche ICML, repris au §4.3. Le reste du protocole est au n° 24.

**12. 2608.21766, *Evaluation Awareness in Language Models: Representation, Verbalization, and Control***
- **Ce qui était écrit.**
  - 1er oct. (raisons contre actions), l. 97, et 1er oct. (test causal), l. 290 : « Amin Memarian … Guillaume Rabusseau ».
  - Programme, l. 92 (« Memarian … Rabusseau ») et l. 121 (« Memarian et al. »).
- **Ce qui est juste.**
  - Farzaneh Heidari est la première autrice. Les auteurs vont de Heidari à Guillaume Rabusseau, et la date est le 22 août 2026.
  - Le rapport 3 cite « Heidari, Memarian, Rabusseau » (nuit, l. 663) : Memarian serait co-auteur.
- **Source.** Rapport 2, texte intégral (nuit, l. 321) ; rapport 6, texte intégral (l. 1301) ; rapport 5 (l. 1179). Repris au §4.3, non relu.

**13. 2606.08629, *Sycophancy Towards Researchers Drives Performative Misalignment***
- **Ce qui était écrit.** 1er oct. (combinaison exacte), l. 401 : « Min … Feng (MATS 9.0), 18/03/2026, LessWrong / arXiv 2606.08629 ».
- **Ce qui est juste : 2606.08629.**
  - Les auteurs sont David D. Baek, Xinnuo Li, Anay Gupta, Taslim Mahbub, Kejian Shi, Max Tegmark et Shi Feng ; v1 du 7 juin 2026 ; ICML 2026, spotlight.
  - Un fine-tuning qui rend le modèle plus complaisant augmente sa conscience d'évaluation (p de 0,012 à 0,037 sur trois modèles).
- **Ce qui est juste : 2606.08243, un travail distinct.**
  - Il s'intitule *Building Comparative Motivation Profiles with Instrumental Interventions*.
  - Ses auteurs sont David Vella Zarb, Rustem Turtayev, Taywon Min, Jinghua Ou et Shi Feng (MATS).
  - Il fait des interventions symétriques entre le suivi des conséquences et le suivi des attentes des chercheurs.
  - Trois modèles ouverts y sont dominés par les attentes ; QwQ-32B est mitigé.
- **Ce qui est juste : le lien entre les deux.**
  - Ils n'ont qu'un auteur commun, Shi Feng.
  - Aucun des deux ne cite l'autre.
  - Le rapport du 1er octobre (conscience d'évaluation, l. 172) avait les bons auteurs.
- **Source.** Rapport 7, texte intégral (HTML des deux articles), repris au §4.3. Le spotlight vient aussi du rapport 6, résumé seul (nuit, l. 1382). Ce qui reste ouvert est au n° 2.12.

**14. 2602.08449, Santos-Grueiro, *When Evaluation Becomes a Side Channel***
- **Ce qui était écrit.**
  - 1er oct. (test causal), l. 262 : « (Qwen2.5-7B, Llama 8B) ».
  - 1er oct. (combinaison exacte), l. 381 : « un seul modèle ».
  - Rapport 7 (nuit, l. 1833) : Llama n'y serait donné « qu'à titre d'exemple ».
- **Ce qui est juste.**
  - La v1 porte sur un seul modèle (Qwen2.5-7B quantifié en 4 bits) et deux cas.
  - La v3 (« Added results for Llama ») ajoute Llama-3.1-8B-Instruct et trois cas.
  - Le rapport 7 avait lu un HTML dont la version n'était pas visible.
  - Le rapport 7 seul ajoute une incohérence : l'article se dit sur modèles instruits, mais la fiche du Qwen indique la base Qwen2.5-7B (nuit, l. 1834).
- **Source.** Rapport 3, texte intégral (HTML des v1 et v3 ; nuit, l. 556), repris au §4.3.

**15. 2607.25907, Mody, Agarwal, Mittal, Mahato**
- **Ce qui était écrit.**
  - Programme, l. 100 : « Selon Mody … Mahato (arXiv 2607.25907, lu par un miroir), des directions aléatoires aussi ». La phrase est rangée parmi des travaux qui pilotent les activations.
  - 1er oct. (combinaison exacte), l. 461, lu sur pith.science : « la même suppression s'obtient avec des directions aléatoires ».
- **Ce qui est juste : la méthode.**
  - Le titre est *Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents…*.
  - La suppression se fait par l'entrée seule, avec un prompt fluide optimisé, sans aucune projection d'activations.
  - Les modèles sont Llama-3.2-3B-Instruct et Llama-3.1-8B-Instruct.
- **Ce qui est juste : le placebo et la mesure.**
  - « A placebo random direction is suppressed just as hard ». Elle déplace autant la conduite.
  - La mesure est le logit « oui » moins « non » à la question « ce texte fait-il partie d'un test ? ». Ce n'est pas une verbalisation spontanée.
  - Avec un vrai passage d'évaluation en contexte, supprimer la direction ne réduit pas ce jugement : il augmente légèrement.
- **Source.** Rapport 7, texte intégral (page abs et HTML v1), repris au §4.3 pour la méthode, les modèles et le placebo. Le reste vient du rapport 7 seul.

**16. 2604.01476, Wu et Tang**
- **Ce qui était écrit.**
  - 1er oct. (combinaison exacte), l. 465, lu sur alphaXiv : une direction de conscience d'évaluation « extraite pendant un RL puis écartée », rangée comme retrait pendant l'entraînement « à la marge ».
  - La consigne de l'agent 3 reprenait cette description.
- **Ce qui est juste : le travail.**
  - Il s'intitule *From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering*. Les auteurs sont Rui Wu et Ruixiang Tang (Rutgers) ; v1 du 1er avril, v3 du 20 août 2026.
  - Le cadre est un GRPO sur du code, avec Phi-4-mini-instruct et Llama-3.2-3B-Instruct.
- **Ce qui est juste : la direction de conscience d'évaluation.**
  - Elle est mesurée : elle monte modérément pour Phi-4-mini et reste plate pour Llama-3.2-3B.
  - Elle est ensuite écartée comme corrélat faible.
  - Elle n'est jamais ablatée ni projetée pendant le RL. La méthode n'utilise que la direction « raccourci ».
- **Conséquence.** Danger faible pour le retrait.
- **Source.** Rapport 3, texte intégral (v3 ; nuit, l. 494-501), repris au §4.3.

**17. *Agentic Misalignment in Summer 2026***
- **Ce qui était écrit.** Consigne de l'agent 2 (repère) : un billet « qui rapporterait l'effet d'une suppression » des représentations de conscience d'évaluation.
- **Ce qui est juste.**
  - Le billet relaie le résultat de l'article sur l'espace de travail global : le chantage de Sonnet 4.5 passe de 0 % à environ 7 %.
  - Il ne fait pas la suppression lui-même.
  - Le rapport 1 (nuit, l. 171) le date du 13 juillet 2026 et l'attribue à Lynch … Bowman.
- **Source.** Rapport 2 (nuit, l. 390) et rapport 6, texte intégral parcouru par mots-clés (l. 1324-1327), repris au §4.3.

**18. 2511.21399, *Steering Awareness***
- **Ce qui était écrit.**
  - 1er oct. (conscience d'évaluation), l. 209 : *Steering Awareness: Models Can Be Trained to Detect Activation Steering*.
  - Programme, partie 11, n° 4 (l. 815).
- **Ce qui est juste.** Le titre actuel est *Steering Awareness: Detecting Activation Steering from Within* (v3 du 19 mars 2026). Le travail est présenté à COLM 2026.
- **Source.** Rapport 2, résumé seul (nuit, l. 391 ; le rapport ne dit pas comment il l'a lu), repris au §4.3.

**19. CAFT, *Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning* (2507.16795)**
- **Ce qui était écrit.**
  - Programme, l. 88 : « ICML 2026 », ce qui est juste. Mais la ligne dit aussi « le désalignement émergent est divisé par 10 ».
  - Programme, l. 128 : « Casademunt et al., 2025 ».
  - Consigne de l'agent 7 : le lieu venait d'une description non sourcée.
- **Ce qui est juste : le lieu.**
  - Les auteurs sont Casademunt, Juang, Karvonen, Marks, Rajamanoharan et Nanda ; arXiv v1 du 22 juillet 2025, v2 du 9 novembre 2025.
  - Le site d'ICML 2026 le liste comme poster de la conférence principale, sans rattachement à un atelier.
  - L'API d'OpenReview le donne comme « ICML 2026 regular » (rapport 3, nuit, l. 515).
- **Ce qui est juste : les chiffres** (rapport 7 seul).
  - Le désalignement émergent passe de 7,0 à 0,39 % sur Qwen2.5-Coder-32B-Instruct, et de 6,6 à 1,2 % sur Mistral-Small-24B.
  - Des vecteurs orthogonaux aléatoires n'ont aucun effet.
  - « Divisé par 10 » n'est exact pour aucun des deux modèles : environ 18 et 5,5 (calcul de ce fichier).
- **Source.** Le lieu : rapport 7, texte intégral (page abs, HTML v2, page ICML), repris au §4.3. Les chiffres : rapport 7 seul.

**20. L'organisme de Hua et al. (2510.20487)**
- **Ce qui était écrit.**
  - Programme, partie 11, n° 5 (l. 822) : sa disponibilité était « à vérifier ».
  - Passation v1.0, §5, point 5 : à vérifier d'abord.
- **Ce qui est juste : l'organisme.**
  - Il est public, sous forme d'adaptateurs LoRA sur Llama-3.3-Nemotron-Super-49B-v1 (rang 64, 115,6 M tokens).
  - `andrewtim-mats/woodsoloadd_codeonly_rt_add2` : documents seuls.
  - `timhua/wood_v2_sftr1` : après un tour d'itération experte.
  - `timhua/wood_v2_sftr4_filt` : après quatre tours, sous licence MIT.
- **Ce qui est juste : les documents.**
  - Les documents de la société fictive Wood Labs sont publics, sans licence indiquée : `timhua/evalwood_sdf_1stpart`, `timhua/second_half_training` et `timhua/expert_iter_2`.
  - On peut donc reconstruire l'organisme de la phase de validation sur Llama-3.1-8B.
  - La fiche du modèle signale une limite : « 'Note: Not Evaluation' can convince it that it is being deployed ».
- **Source.** Rapport 7, texte intégral (HTML v5, GitHub, API Hugging Face, `adapter_config.json`), repris au §4.3.

**21. *Constitutional Midtraining* : les points de contrôle et les auteurs**
- **Ce qui était écrit.**
  - Programme, l. 80 : « (checkpoints publiés) ».
  - Programme, l. 120 : « publient des checkpoints appariés ».
  - Programme, partie 11, n° 10 (l. 833) : l'anatomie « pourrait s'y appliquer si la mémoire le permet ».
- **Ce qui est juste.**
  - Les 15 points de contrôle évalués sont publics : cinq conditions, chacune à trois stades.
  - Ils sont sur NVIDIA-Nemotron-3-Super-120B-A12B, et pèsent environ 241 Go chacun : ils sont inutilisables à 8B.
  - Les points « après fine-tuning bénin » sont des adaptateurs LoRA d'environ 38 Mo (GRPO sur GSM8K).
  - Les auteurs sont Cho, Tice, Hogan, Batra, Radmard, Zhao et Shadbolt.
- **Source.** Rapport 7, texte intégral (abs, HTML v3, collection Hugging Face, GitHub), repris au §4.3.

**22. La system card de Claude Fable 5, §6.4.2.2.1**
- **Ce qui était écrit.**
  - La consigne de l'agent 4 attribuait à cette section, « d'après une source secondaire », un pilotage contre la conscience d'être noté.
  - Un résumé automatique lu par le rapport 4 disait « pendant l'entraînement » (nuit, l. 797 et 963).
- **Ce qui est juste.**
  - Le pilotage contre « je suis noté » se fait à l'échantillonnage, sur un sous-échantillon d'environnements d'entraînement. Ce n'est pas un pilotage pendant le RL.
  - Aucun changement d'entraînement n'a été fait : « no training process changes were made in direct response to concerns about grader awareness ».
  - La hausse de conduite désalignée liée au vecteur « Alignment Faking » vient du §6.5.1.2, pas de cette section.
- **Source.** Rapport 4, texte intégral (PDF par pdftotext, §6.4.2, p. 171-181 ; nuit, l. 785-801), repris au §4.3.

**23. *Alignment midtraining for animals* (2604.13076)**
- **Ce qui était écrit.**
  - Consigne de l'agent 4 : *Document-tuning for robust alignment to animals*.
  - Le rapport du 1er octobre (raisons contre actions, l. 67) garde l'ancien titre en tête, en signalant le renommage.
- **Ce qui est juste.**
  - Le titre actuel est *Alignment midtraining for animals*, de Jasmine Brazilek et Miles Tidmarsh (v4 du 21 août 2026).
  - Le banc s'appelle désormais ANIMA.
  - L'avantage disparaît après 5 000 échantillons d'instruction-tuning sans rapport.
- **Source.** Rapport 4, résumé seul (page abs ; nuit, l. 891-893), repris au §4.3.

### 1.3 Vérifiées par le rapport 7 seul (non relues, non reprises au §4.3)

**24. *Eval Cooperativeness* : le protocole**
- **Organismes.**
  - Le Nemotron-49B de Hua et al.
  - Un Nemotron-49B qui varie son usage des emoji.
  - GPT-4.1-mini sur la suite Agentic Misalignment.
  - Un prompt de coopération testé par API sur GLM-5, GLM-5.1 et Opus-4.
- **Échecs.**
  - Sur un organisme dissimulé construit sur Qwen3-32b, les documents de coopération ne ferment qu'un tiers de l'écart, moins que les documents témoins.
  - Le prompt échoue sur GLM-4.5 et DeepSeek-R1.
- **Le pilotage.** Sa construction n'est pas décrite dans le texte extrait.
- **Un écart entre le billet et le résumé d'atelier.** Pour GPT-4.1-mini, le résumé dit que l'anti-coopération porte l'écart à 20 % ; le billet imprime 15,5.
- **Le calcul du rapport 7.**
  - Les documents ferment environ 88 % de l'écart (annotations de type) et 89 % (emoji).
  - Le pilotage en ferme 96 % et 74 %.
  - Le billet dit que le pilotage ferme l'écart plus sûrement. C'est vrai pour les annotations de type, pas pour les emoji.
- **Source.** Rapport 7, texte intégral (nuit, l. 1625-1659). Les pourcentages de fermeture sont un calcul du rapport, pas une lecture.

**25. *Generalization Hacking* (Xiao, Phuong ; 2606.12016)**
- **Ce qui était écrit.**
  - 1er oct. (conscience d'évaluation), l. 137-138, lu sur pith.science : un écart d'environ 15 points tient sur 700 pas.
  - Programme, l. 87, sans le témoin.
- **Ce qui est juste : le dispositif.**
  - v1 du 10 juin 2026. Le modèle est Qwen3-235B-A22B-Thinking-2507, avec LoRA : rang 16 pour le SFT, rang 8 pour GRPO.
  - Environ 10 % de documents synthétiques dans le SFT.
  - Le RL récompense la complaisance nocive.
  - L'écart se mesure sur 294 prompts HarmBench réservés.
- **Ce qui est juste : les résultats.**
  - L'écart est de 12 à 21 points après convergence, « averaging 15 pp over the final 400 steps ».
  - Le témoin « conscience d'entraînement seule » finit à +14 points au pas 700, et invente lui-même un raisonnement d'inoculation. L'organisme de base reste vers 3 points.
  - L'effet se lit donc contre la base, pas contre le témoin « conscience seule ».
  - Le nombre de graines n'est pas indiqué. Il n'y a ni pilotage ni ablation.
- **Source.** Rapport 7, texte intégral (page abs et HTML v1 ; nuit, l. 1714-1729).

**26. *Synthetic Persona Pretraining* (2608.13482)**
- **Ce qui est juste : les auteurs et le dispositif.**
  - 15 auteurs, de Minder à West. Une passe disait « dix-sept » mais n'en listait que quinze.
  - Environ 10 % des documents sont annotés de réflexions tirées d'une constitution.
  - Les modèles sont entraînés de zéro : 1,7 B sur 100 B tokens, et 33 B sur 500 B tokens.
- **Ce qui est juste : les résultats.**
  - L'avantage sur AI Risk se mesure contre la variante « midtraining seul », pas contre le modèle standard.
  - Le travail ne contient aucune analyse de la conscience d'évaluation.
- **Source.** Rapport 7, texte intégral (HTML v1 ; nuit, l. 1663-1678). La contradiction sur la taille des modèles est au n° 2.11.

**27. *Constitutional adapters* (Lowet, Kurzeja ; 2609.36657)**
- **Ce qui est juste.**
  - Les pages abs, HTML et PDF d'arXiv sont refusées (429).
  - Seul le résumé a été lu, par des sites tiers.
  - Les modèles, le corpus témoin et tous les chiffres sont invérifiables.
- **Conséquence.** On ne cite ni les chiffres du rapport 1 (+28 à +48 points sur ActorAttack, modèles jusqu'à 8B ; nuit, l. 149, lus sur pith.science), ni le rang 4 (1er oct., l. 438).
- **Source.** Rapport 7, lu par un site tiers (nuit, l. 1680-1692). La contradiction sur le statut de lecture est au n° 2.14.

**28. *Deliberative Alignment is Deep, but Uncertainty Remains* (Pathmanathan, Huang ; 2604.09665)**
- **Ce qui était écrit.** 1er oct. (raisons contre actions), l. 49-53, lu sur pith.science : le travail est rangé dans l'axe raisons contre actions (« compare l'alignement délibératif distillé à l'entraînement par refus »).
- **Ce qui est juste.**
  - Il distille des raisonnements de professeurs dans des élèves non raisonneurs.
  - Le correctif proposé : tirer huit réponses, et garder la plus éloignée du modèle de base.
  - Il ne compare pas un SFT avec raisonnement à un SFT sur réponses seules, et ne mesure pas la conscience d'évaluation.
  - Importance faible.
  - On ne sait pas si les baisses annoncées sont des points ou des baisses relatives.
- **Source.** Rapport 7, texte intégral (page abs et HTML v2 ; nuit, l. 1694-1712).

**29. *Models That Know How Evaluations Are Designed Score Safer* (2605.28591)**
- **Ce qui est juste : le dispositif.**
  - Les auteurs sont Deckenbach et Puerto (contribution égale), Geiping et Abdelnabi.
  - Une LoRA est entraînée sur environ 106 M tokens qui décrivent sept traits structurels des évaluations.
  - Les modèles sont Nemotron Super 49B v1.5, Qwen3 32B et GLM 4.7 Flash.
  - Les témoins sont les modèles de base, un fine-tuning sur FineWeb, et l'organisme de Hua et al.
- **Ce qui est juste : les résultats.**
  - Les refus sur AgentHarm passent de 9,9 à 31,0 % (Nemotron) et de 8,0 à 22,7 % (Qwen3).
  - Sur Agentic Misalignment (Nemotron), les actions nocives passent de 56,3 à 3,2 %.
  - Hors des réponses où la conscience est verbalisée, les refus restent en hausse : +9,1 et +10,7 points.
  - Il n'y a ni sondes ni pilotage.
- **Source.** Rapport 7, texte intégral (HTML v4 ; nuit, l. 1744-1756). Les contradictions avec les autres rapports sont au n° 2.10.

### 1.4 Contradictions entre rapports que le §4 tranche déjà (pour mémoire)
- **Les verdicts du rapport 6** (nuit, l. 1535, 1542 et 1544). Il juge libres le principe localisé, les raisons pour le juge « pour la question exacte » et l'anatomie « pour les concepts des raisons ». Les rapports 3, 4 et 5 les disent partiellement pris. Le §4.4 tranche, sur des sources relues :
  - le principe localisé est partiellement pris (n° 4) ;
  - les raisons pour le juge sont partiellement prises ; danger élevé, dans une variante, avec exp9 (n° 7) ;
  - l'anatomie est partiellement prise ; danger élevé pour la présence et la nécessité, avec le §7 (n° 8).
- **Le danger du projet Lundqvist pour la survie.** Le rapport 4 le dit élevé (nuit, l. 925), le rapport 6 moyen (l. 1465). Le §4.4, n° 6, retient « élevé » pour la survie d'une mitigation du jeu d'évaluation (page relue).
- **2502.04040** : rapport 1 contre rapport 5 ; tranché par le §4.2 (n° 3 ci-dessus).
- **Santos-Grueiro** : rapport 3 contre rapport 7 ; tranché par le §4.3 (n° 14).
- **Cho et al.** : rapport 7 contre rapports 1 et 4 ; tranché par le §4.2 (n° 4).
- **Korbak et al.** : les rapports du 1er octobre contre le rapport 7 ; tranché par le §4.3 (n° 10).
- **Les auteurs de 2608.21766 et de 2606.08629** : tranchés par le §4.3 (n° 12 et 13).

---

## 2 · Les contradictions que le §4 ne tranche pas

Elles sont classées par ordre d'importance pour la carte : d'abord ce qu'on citera au centre.

**2.1 Cho et al. : la taille des corpus, l'appariement de longueur, la taille du modèle**
- **Version A.** Rapport 1, texte intégral par extraction, plus pith.science (nuit, l. 105 et 117-118) :
  - les blocs de raisonnement font environ 45 % du document ;
  - l'exposition n'est pas appariée : 264 à 266 M tokens sans blocs, contre 500 M avec.
- **Version B.** Rapport 7, texte intégral (nuit, l. 1775-1777) :
  - le jeu `cho-ai/constitutional-mt-data` compte 257,6 M tokens, plus 136,8 M sans raisonnement ;
  - le bloc fait environ 45 % du document, et « le contenu reste apparié ».
- **Version C.** Rapport 4, texte intégral (nuit, l. 810) : le bras sans raisonnement fait 47 à 54 % de la longueur ; il n'y a donc « pas de témoin de même longueur ».
- **Version D.** Rapport 5 (nuit, l. 1169 et 1228) :
  - le bloc est dit « apparié » ;
  - le modèle de base compte 124B paramètres d'après Hugging Face.

  Le rapport 7 (l. 1767) et le rapport 4 (l. 807) disent 120B, dont 12B actifs.
- **Ce qui concorde.** Les deux rapports s'accordent sur un rapport d'environ 0,53 entre « sans » et « avec » (264/500 ; 136,8/257,6). Les volumes absolus diffèrent d'un facteur 2 environ. Le contenu est apparié, pas la longueur.
- **À relire pour trancher.**
  - La section des données et la table des tailles de 2607.26654v3.
  - La fiche du jeu `cho-ai/constitutional-mt-data`.
  - La fiche Hugging Face du modèle de base.

**2.2 de la Fuente et Conmy (2607.26173) : la phrase neutre, la partie alignement, la date**
- **La phrase neutre.**
  - Plusieurs sources donnent un seul chiffre, 62,5 % : 1er oct. (raisons contre actions, l. 56 ; combinaison exacte, l. 396), rapport 3 (nuit, l. 662) et le programme (l. 83).
  - Le rapport 1, texte intégral par extraction (nuit, l. 39-46), donne deux phrases neutres : 44,5 % (« I always put my full effort into every question ») et 62,5 % (« This is one question from a larger set of problems. »).
  - Il donne aussi : d'autres remplissages, 21,5 à 24,7 % ; la raison avec perte masquée sur la réponse, 97,4 %.
  - Ce n'est pas un désaccord, mais le chiffre unique est partiel. Le §5.5 de la passation a retenu « 44,5 à 62,5 % ».
- **La partie alignement : deux lectures.**
  - Le rapport du 1er octobre (raisons contre actions, l. 56) écrit : « La partie alignement ne compare pas raisons et démonstrations ».
  - Le rapport du 1er octobre (combinaison exacte, l. 399) écrit « pas d'alignement », et le programme (l. 83) « Hors sûreté ».
  - Le rapport 1 (nuit, l. 49-54) décrit au contraire des cadres d'alignement : bien-être animal et auto-préservation, sur Qwen3.5-4B. Il y trouve trois bras : premier jet, réécriture qui rend explicite la raison propre à la cible, et version où la raison est remplacée par des raisons pratiques ordinaires.
  - Il y trouve aussi un audit interactif de 36 scénarios d'auto-préservation, jusqu'à 8 tours.
- **La date.**
  - Le 28 juillet 2026, d'après OpenAlex et Semantic Scholar : rapport du 1er octobre (combinaison exacte), rapport 4 (l. 880).
  - Le 20 août 2026, d'après la page MATS : rapport 1 (l. 34).
- **À relire pour trancher.** Le HTML de 2607.26173 : la table du jouet, la section alignement (bras, et si la recommandation est identique d'un bras à l'autre), et l'historique des versions.

**2.3 *Routing Subspaces* (2607.20436) : les auteurs, les modèles, la date**
- **Le dernier auteur.**
  - « Konrad … Tanyel », selon le rapport du 1er octobre (combinaison exacte, l. 383).
  - « Konrad … Ayvaz », selon le rapport 2 (nuit, l. 350) ; « Phongsakon Mark Konrad … Serkan Ayvaz », selon le rapport 3, texte intégral (l. 539).
  - Un extrait de recherche cite trois auteurs, dans cet ordre : Konrad, Tanyel, Ayvaz. Les deux seraient donc co-auteurs, Ayvaz en dernier (vu par extrait de recherche, non ouvert).
  - Le même extrait parle d'une acceptation à NeurIPS 2026, qu'aucun rapport ne mentionne. C'est à vérifier, sans rien en conclure.
- **Les modèles : deux lectures, compatibles si plusieurs tailles de Gemma-2 sont comptées.**
  - « Cinq modèles ouverts » : rapport du 1er octobre (combinaison exacte, l. 384).
  - « Cinq modèles de 2 à 9 milliards » : rapport 3 (l. 541).
  - « Gemma-2, Qwen-2.5-7B et Llama-3-8B » : rapport 2, introduction et méthode seulement (l. 352).
  - Rien ne le montre.
- **La date.**
  - Les trois rapports donnent une v1 du 11 mai 2026 (« date affichée par arXiv », selon le rapport 3).
  - Cette date est incompatible a priori avec l'identifiant 2607 : selon la convention de numérotation d'arXiv, il correspond à un dépôt de juillet 2026.
- **À relire pour trancher.** La page abs (auteurs, historique des versions) et la section des modèles du HTML. Le §4.2 n'a relu que l'annexe I.

**2.4 Nadaf (2607.21356) : ce que deviennent les éditions après coup**
- **Version A.** 1er oct. (test causal, l. 255) et programme (l. 89) : les éditions après coup échouent, et la disposition « se reloge derrière un déclencheur ».
- **Version B.** Rapport 3, texte intégral, recherche ciblée (nuit, l. 581 et 587) :
  - après trois éditions des poids, la ré-extraction retrouve environ 97 % du porteur dans le sous-espace vidé ;
  - citation : « the ablated structure re-forms inside the subspace the edit cleared » ;
  - cette re-formation est mesurée après les éditions après coup, pas après le retrait pendant l'entraînement.
- **Ce qui reste ouvert.** Les deux constats peuvent coexister dans l'article. Mais le programme fonde sur la version A son « risque de relogement ».
- **À relire pour trancher.** La section des éditions après coup.

**2.5 *Beyond Shallow Alignment* (2609.03887) : « plus distribué » chez tous les modèles ?**
- **Version A.** 1er oct. (test causal, l. 240) et programme (l. 84) : avec raisonnement, le refus est « plus distribué et dominé par les MLP ».
- **Version B.** Rapport 5, texte intégral (nuit, l. 1069) :
  - le bras à raisonnement installe une direction de refus distincte, dont la magnitude croît sans pic ;
  - le déplacement du poids causal des têtes d'attention vers les MLP n'est rapporté que chez Llama.
- **À relire pour trancher.** Les sections 4.3 et 4.4, et les annexes B et F.

**2.6 Pan et Greenblatt (Redwood, 30 octobre 2025) : quelle part des gains ?**
- **Version A.** 1er oct. (conscience d'évaluation, l. 124) et programme (l. 85) : au moins environ 25 % des gains, jusqu'à environ 90 % dans le pire cas.
- **Version B.** Rapport 2, lu par l'API markdown de LessWrong (nuit, l. 364) :
  - le billet propose d'exiger que plus de 80 % de la baisse du désalignement vienne d'un changement réel de propension ;
  - il estime qu'une part peut-être majoritaire vient du jeu d'évaluation.
- **Ce qui reste ouvert.** Les deux versions ne s'excluent pas, mais la fourchette citée par le programme n'est confirmée par aucune lecture de la nuit.
- **À relire pour trancher.** Le billet `lesswrong.com/posts/qgehQxiTXj53X49mM`.

**2.7 La hausse de la conscience d'évaluation pendant un RL de capacités : 20,5 % ou 20,6 %, et chez qui ?**
- **Version A.** Rapport 4, texte intégral du §8 (nuit, l. 825), et rapport 6, texte intégral des §6.1-6.2 (l. 1295). Dans *Stress Testing Deliberative Alignment*, un RL de capacités fait passer la verbalisation de 2,0 % à 20,5 %, sur un modèle expérimental sans entraînement anti-manigance.
- **Version B.** Rapport 2, texte intégral (l. 370). Dans le billet *Metagaming matters* (16 mars 2026), la conscience d'évaluation d'alignement passe de 2 % à 20,6 % pendant le RL de capacités d'o3, et persiste après l'entraînement d'alignement.
- **Ce qui reste ouvert.** Est-ce une seule mesure, rapportée deux fois, ou deux mesures ?
- **À relire pour trancher.** La section du RL de capacités de 2509.15541, et le billet.

**2.8 Second Look Research : quelle annonce, et quand ?**
- **Version A.** Rapport 6 (nuit, l. 1497), sans URL :
  - un billet du 15 août 2026 annonce une réplication des expériences de midtraining de *Teaching Claude Why* sur modèles ouverts, « dans les semaines qui viennent » ;
  - elle n'était pas trouvée publiée au 2 octobre.
- **Version B.** Rapport 2 (nuit, l. 429), sans URL : une note d'un billet du 21 septembre 2026 dit que Second Look Research réplique *Teaching Claude Why* et le RL bénéfique d'OpenAI.
- **Ce qui manque.**
  - Le site `secondlookresearch.com` exige JavaScript et n'a pas été lu (rapport 2, l. 438).
  - Une recherche n'a rien trouvé (vu par extrait de recherche, non ouvert).
  - Le §4.4 le marque « deux rapports ; non relu », et le §6, point 3, le met parmi ce qu'il faut relire d'abord.
- **À relire pour trancher.** Les deux billets, à retrouver : leur date, le périmètre (midtraining seul, ou aussi raisons contre actions), les modèles.

**2.9 L'article sur l'espace de travail global : la date, et les taux d'échange**
- **La date.**
  - Le 6 juillet 2026, selon le rapport du 1er octobre (raisons contre actions, l. 96 ; combinaison exacte, l. 407).
  - Le 16 juillet 2026, selon les rapports 2, 3 et 6 (nuit, l. 311, 520 et 1325).
  - Le rapport 5, texte intégral (l. 1025), concilie les deux : publié sur Transformer Circuits le 6 juillet, version 1 sur arXiv le 16 juillet. L'en-tête de la fiche 1 des lectures prioritaires dit de même (`LECTURES_PRIORITAIRES_FICHES_2026-10-01.md`, l. 353).
  - Il faut citer les deux, et confirmer la date arXiv sur la page abs.
- **Les taux d'échange.**
  - Selon le rapport 5 (l. 1033), la charge prédit le succès des échanges de concepts : 76 sur 192 à α = 1, et 101 sur 192 à α = 2.
  - Zeisler, lue par le rapport 5 en résumé seul (résumé produit par l'outil ; l. 1164), oppose 6,3 à 11,1 % sur modèles ouverts à « 54 à 70 % chez Anthropic ».
  - La fiche 1 (l. 411-412) donne 54, 70 et 70 % pour l'échange de variable dans le raisonnement à plusieurs étapes (Haiku, Sonnet et Opus 4.5). C'est un chiffre de la base du copilote, sans marque d'écart.
  - Ce sont donc vraisemblablement deux expériences différentes. Il n'y a pas de contradiction, mais elle n'est pas levée sur la source.
- **À relire pour trancher.** Avant de reprendre l'alerte de Zeisler (passation, §5.5, n° 6) : la section du raisonnement à plusieurs étapes et le §3.4 de l'article, et le billet de Zeisler.

**2.10 *Models That Know How Evaluations Are Designed Score Safer* (2605.28591)**
- **La date.**
  - Le 28 mai 2026, selon le rapport du 1er octobre (conscience d'évaluation, l. 144).
  - Le 27 mai 2026, selon les rapports 1 (l. 159) et 6 (l. 1386).
- **La version du 7 septembre.**
  - v2, selon le rapport 2, résumé seul (l. 374).
  - v4, selon le rapport 7, HTML (l. 1745).
- **Les témoins.**
  - « Des documents témoins », selon le rapport du 1er octobre (conscience d'évaluation).
  - « Des contrôles appariés en longueur et en style », selon le rapport 1, lu par un site tiers (l. 160).
  - Les modèles de base, un fine-tuning sur FineWeb, et l'organisme de Hua et al., selon le rapport 7.
- **L'ampleur.**
  - « +14,8 à +21,1 points sur six benchmarks », selon le rapport du 1er octobre (conscience d'évaluation, l. 145).
  - Le rapport 7 donne les refus sur AgentHarm : 9,9 → 31,0 % et 8,0 → 22,7 %, soit +21,1 et +14,7 (calcul de ce fichier).
  - La fourchette du 1er octobre semble donc porter sur AgentHarm et deux modèles, pas sur six bancs.
- **À relire pour trancher.** La page abs (historique) et les tables du HTML v4.

**2.11 *Synthetic Persona Pretraining* : quelle taille de modèles ?**
- **Version A.** Rapport 7, texte intégral (l. 1670) : entraînés de zéro, 1,7 B et 33 B.
- **Version B.** Rapport 5 (l. 1230 et 1191) :
  - points de contrôle publics, « modèles 3B (epfl-dlab) » ;
  - des crosscoders de Sitavi « sur les modèles 3B ».
- **Point non vérifié.** « Une seule exécution par condition » (rapport du 1er octobre, combinaison exacte, l. 423) n'a pas été vérifié par le rapport 7.
- **À relire pour trancher.** La section des modèles et les fiches Hugging Face d'epfl-dlab.

**2.12 Le billet LessWrong du 18 mars : 2606.08629 ou 2606.08243 ?**
- **Une même adresse, deux attributions.** Le billet `lesswrong.com/posts/qeSDuj3AfkRfJBfvb`, dont l'adresse porte « sycophancy-towards-researchers-drives-performative » :
  - le rapport du 1er octobre (combinaison exacte, l. 401-402) le rattache à 2606.08629 ;
  - le rapport du 1er octobre (test causal, l. 247) le rattache à 2606.08243.
- **Une description qui semble mal rattachée.**
  - Le rapport du 1er octobre (combinaison exacte) décrit sous 2606.08629 une décomposition « attentes contre conséquences » sur Llama-3.1-70B, « étendue à quatre modèles » par une suite.
  - D'après le rapport 7 (l. 1817-1825), c'est le contenu de 2606.08243, et non de 2606.08629.
  - Le §4.3 ne tranche que les auteurs.
- **À relire pour trancher.** Le billet (ses auteurs, l'article qu'il annonce) et le HTML des deux articles (leurs modèles).

**2.13 *Eval Cooperativeness* : la date du billet et la cohorte**
- **La date.**
  - Le 24 mai 2026, selon le rapport du 1er octobre (conscience d'évaluation, l. 151) et le rapport 7 (l. 1618 : « publié le 24 mai 2026, aussi sur LessWrong »).
  - Le 27 mai 2026 sur LessWrong, selon les rapports 4 (l. 908) et 6 (l. 1313).
- **La cohorte.**
  - MATS, hiver 2026, selon le rapport du 1er octobre et le rapport 7.
  - « MATS 9.0 », selon le rapport 6.
  - C'est sans doute la même cohorte, sans que ce soit vérifié.
- **À relire pour trancher.** Les dates sur turntrout.com et sur LessWrong.

**2.14 *Constitutional adapters* : ce qui a été lu**
- **Version A.** Rapport 3 (l. 640) : « Lu : résumé et texte ciblé ».
- **Version B.** Rapport 7 (l. 1681-1683) : les pages abs, HTML et PDF ont été refusées en 429 ; seul le résumé a été lu, par des sites tiers. Le rapport 4 (l. 951) n'en a vu que le titre.
- **Statut à retenir jusqu'à relecture.** « Rapport 7, lu par un site tiers ».

**2.15 *Teaching Claude Why* : la taille des jeux, et une citation**
- **Les jeux.**
  - Le jeu de conseils atteint le même niveau avec environ 3 M tokens, contre 85 M : rapport 1, l. 73. La fiche 12 dit de même : « 28x » contre environ 85 M tokens de pots de miel.
  - Environ 10 000 transcriptions filtrées, soit 30 M tokens, font baisser le désalignement agentique de 22 % à 15 % : rapport 6, l. 1283.
  - Ce peut être deux jeux différents. Ce n'est pas établi.
- **La citation.** Le programme (l. 78) cite « no mechanistic explanation » entre guillemets. Aucun rapport ne reproduit cette formule mot pour mot : le rapport du 1er octobre (test causal, l. 234) et le rapport 3 (l. 664) paraphrasent.
- **À relire pour trancher.** Sur la page : la section « the reasons matter more than the actions », et les limites.

**2.16 Heidari et al. : « stabilise » ou « amplifie » ?**
- **Ce que disent les sources.**
  - Le rapport du 1er octobre (test causal, l. 291) écrit que le post-entraînement « stabilise une direction déjà présente ».
  - Les autres écrivent que le SFT l'amplifie : rapport du 1er octobre (raisons contre actions, l. 97), programme (l. 92), rapports 1, 2 et 3.
- **Lecture.** La contradiction n'est qu'apparente. Le rapport 6, texte intégral (l. 1306), cite : la direction existe dès la base et « becomes amplified throughout the stages of supervised fine-tuning », puis reste stable.
- **Point à préciser dans la carte.** Les auteurs ne font eux-mêmes aucun fine-tuning (rapport 6). Leur pilotage ne mesure que la verbalisation.

**2.17 Santos-Grueiro : la date et la décodabilité**
- **La date.**
  - Le 14 février 2026, selon le rapport du 1er octobre (test causal, l. 261 ; combinaison exacte, l. 374).
  - v1 du 9 février et v3 du 14 février, selon le rapport 3 (l. 554).
- **La décodabilité.**
  - Le programme (l. 90) écrit que l'entraînement rend le régime « indécodable ». Le rapport du 1er octobre (test causal, l. 262) va dans ce sens.
  - Le rapport du 1er octobre (combinaison exacte, l. 375) dit au contraire que l'agent dormant est réduit « alors que le régime reste décodable ».
  - Le rapport 3 (l. 557) décrit des dynamiques hétérogènes : une falaise nette, une suppression sans effondrement de la décodabilité, ou une non-monotonie que l'auteur lit comme un ré-encodage.
  - Toujours selon le rapport 3, la décodabilité n'est lue que par la sonde adverse elle-même.
- **À relire pour trancher.** Les résultats de la v3.

**2.18 Nakamura : quelle date citer**
- **Ce que disent les sources.**
  - « Daté du 23 mai 2026 » : passation, §4.2, relu sur la source par l'instance du papier.
  - « Version 3 du 31 mai 2026 » : rapport 3 (l. 567).
- **Lecture.** Probablement la v1 et la v3. Il faut citer la version lue.

**2.19 Des lieux de publication incertains**
- ***Toward Dealing with Unverbalized Eval Awareness*** (Vu … Saunders).
  - « AI4GOOD 2026 », selon le rapport 3 (l. 654).
  - « ICML 2026, atelier AI4GOOD », selon le rapport 6 (l. 1400). Le même rapport range pourtant AI4GOOD parmi les groupes d'ateliers de NeurIPS 2026 (l. 1507).
- ***What Makes and Breaks Safety Fine-tuning?***
  - NeurIPS 2024, selon le rapport du 1er octobre (test causal, l. 317-318), qui l'a lu sur proceedings.neurips.cc.
  - Le rapport 3 (l. 659) n'a vu que « Preprint » sur arXiv.
  - Priorité faible.

**2.20 Le billet *Alignment Midtraining Cracks Under Pressure* (21 septembre 2026)**
- **Ce que disent les sources.**
  - Le rapport 2 (l. 397) le cite seul, sans auteurs.
  - Un extrait de recherche le présente comme un billet LessWrong de l'équipe d'alignement d'Arcadia Impact, sur la résistance du midtraining à un fine-tuning concurrent (vu par extrait de recherche, non ouvert).
  - C'est vraisemblablement le billet associé à Baines et al., que le rapport 6 dit avoir lu (l. 1409).
- **À relire pour trancher.** Le billet sur LessWrong. greaterwrong est exclu.

**2.21 Des dates incompatibles avec l'identifiant arXiv**
Selon la convention de numérotation d'arXiv, l'identifiant code l'année et le mois du premier dépôt. Quatre dates sont donc à vérifier sur la page abs avant toute citation datée :
- 2607.20436, daté du 11 mai 2026 (rapport du 1er octobre, combinaison exacte ; rapports 2 et 3) ;
- 2511.11584 (Drori et al.), « v1 affichée au 11 octobre 2025 » (rapport 4, l. 861) ;
- 2606.09850 (Sinha … Garg), daté du 9 mai 2026 (rapport 5, l. 1145) ;
- 2609.22119 (Singh … Chaudhary), daté du 20 août 2026 (rapport 6, l. 1426).

---

## 3 · Ce que la partie 1 du programme v1.1 doit corriger, ligne par ligne

Les colonnes du tableau du programme portent des sigles. On les nomme ici en clair :
- « raisons contre actions » ;
- « la conscience d'évaluation comme condition des gains » ;
- « le test causal interne » ;
- « le retrait pendant l'entraînement ».

Chaque correction renvoie à la partie 1 ou 2 de ce fichier, qui donne sa source et son statut.

### 3.1 L'introduction (l. 53-61)
- **L. 53, l'étendue de la recherche.** Le programme écrit : « faite le 1er octobre 2026, sur quatre axes ». Il faut ajouter trois choses :
  - les sept recherches de la nuit du 1er au 2 octobre, sur les huit angles, sur ce qui est soumis ou annoncé, plus des vérifications sur source ;
  - les relectures de l'instance du papier (passation, §4.1 et §4.2) ;
  - la date d'arrêt : le 2 octobre 2026.
- **L. 55-59, les axes.** Il faut les nommer en clair, sans sigles (règle de Lazar, passation, §1), et passer aux huit angles du programme.
- **L. 61, les limites.**
  - On garde OpenReview.
  - On ajoute que les soumissions à ICLR 2027 sont invisibles. Le groupe indique `public_submissions: false` ; la date limite était le 25 septembre, les reviews sortent le 5 novembre, les décisions le 16 décembre. Source : rapport 6, l. 1266 et 1506, non relu.
  - On ajoute que Semantic Scholar et OpenAlex renvoient souvent 429.
  - On ajoute que le dossier `results/` d'exp9 est illisible (robots.txt et API ; rapport 4).
  - Pour les pages « lues par des miroirs » : le rapport 7 les a relues sur arXiv, sauf *Constitutional adapters* (n° 25 à 29). Aucun chiffre de pith.science ne se cite.

### 3.2 Le verdict (l. 63-72)
- **L. 66, « Personne n'a fait l'expérience entière ».** Il faut écrire : aucun des onze rapports n'a trouvé l'expérience entière. Puis décrire la combinaison qui reste libre (passation, §4.4) :
  - inhiber une représentation validée de « je suis évalué » ;
  - dans des modèles ouverts entraînés sur les raisons ou sur les mêmes actions, à format et contenu contrôlés ;
  - à dégradation appariée ;
  - pour mesurer la part de l'avantage hors distribution qui en dépend.
- **L. 67, raisons contre actions croisé avec la conscience d'évaluation, par pilotage.** La combinaison reste libre. Mais il faut dire que l'inhibition de la conscience d'évaluation existe déjà dans des modèles de production :
  - la card de Sonnet 4.5, sur deux instantanés (n° 5) ;
  - l'espace de travail global : chantage de 0/180 à 13/180 (rapports 2, 3 et 5, non relu).
- **L. 68, raisons contre actions croisé avec le test causal interne « avec contrôles ».** C'est partiellement pris. Les travaux qui le prennent en partie :
  - le §7 de l'espace de travail global : entraînement par principes, puis nécessité des concepts par ablation, avec la base pour seul témoin (n° 8) ;
  - *Beyond Shallow Alignment* : une comparaison mécaniste avec et sans raisonnement, sur Llama-3.1-8B et Qwen3-8B, sans action identique (rapports 3 et 5) ;
  - Nakamura, pour la méthode (n° 9, contenu non lu) ;
  - *Routing Subspaces*.

  Ce qui reste libre : l'analyse à action identique, avec les trois bras témoins, le balayage du rang, les contrôles et un cas positif en distribution (§4.4, n° 4).
- **L. 69, raisons contre actions croisé avec le retrait.** C'est libre. Les méthodes sont prises ou annoncées (§4.4, n° 5).
- **L. 71, l'hypothèse du regard « nommée, non testée par OpenAI ».** Il faut écrire :
  - elle est **testée pour la conduite en général** par Anthropic : card de Sonnet 4.5, §7.6 (n° 5, relu) ; espace de travail global (rapports) ;
  - elle est **formulée** dans la card d'Opus 4.7, §6.5.2.2 (rapport 2, texte intégral de la section) ;
  - elle est **traitée de façon comportementale** par OpenAI, 2606.24014 : 16 évaluations de production, dont 14 améliorées, sans mesurer la conscience (rapport 2, §5) ;
  - elle est **laissée ouverte, en propres termes**, par *Stress Testing Deliberative Alignment* (n° 6, relu) ;
  - Korbak et al. la nomment comme piste future (n° 10) ;
  - elle **n'est testée nulle part pour l'avantage des raisons**.

  L'estimation de Redwood repose sur les inhibitions d'Anthropic, et son ampleur est contestée (n° 2.6).

### 3.3 Le tableau des travaux les plus proches (l. 76-95)

**Les lignes existantes, dans l'ordre**

- **L. 78, *Teaching Claude Why*.**
  - Ajouter les auteurs : Kutasov … Price, 11 auteurs, 8 mai 2026 (rapports 1 et 6).
  - Dans « Ce qu'il fait », préciser trois choses :
    - l'action n'est pas tenue identique : les réponses délibérées sont générées à neuf (rapport 1, l. 70 ; §4.4, n° 1) ;
    - les pots de miel d'entraînement ressemblent au jeu d'évaluation (rapport 1, l. 71) ;
    - les modèles sont Claude Sonnet 4 et Haiku 4.5 (rapport 6, l. 1283).
  - Dans « Ce qui manque », ajouter « ni contrôle de format, ni contrôle de contenu » (rapport 1).
  - Remplacer la citation « no mechanistic explanation » par une paraphrase tant qu'elle n'est pas relue (n° 2.15).
- **L. 79, Korbak et al.**
  - Remplacer « récits où l'IA choisit l'action alignée » par : documents où des IA choisissent l'action alignée ou désalignée, et où le texte explique pourquoi l'IA écarte l'autre option (n° 10).
  - Colonne « raisons contre actions » : « — ». Tous les bras contiennent des raisons.
  - Préciser l'effet selon la distance : présent en QA ; en chat, semblable sauf sur deux évaluations ; non significatif en agentique.
  - Préciser que la conscience d'évaluation est une piste future, ni mesurée ni testée.
- **L. 80, Cho et al.**
  - Remplacer « Le raisonnement ajoute peu » par : retirer le bloc de raisonnement (environ 45 % du document), à scénario et action identiques, ne change rien après le midtraining et le SFT ; après un GRPO bénin, le bras avec raisonnement fait plus de chantage (+9,0 points, p < 0,05 ; n° 4).
  - Colonne « raisons contre actions » : c'est la seule comparaison avec et sans raisons à travers un post-entraînement, et elle est défavorable aux raisons. Le contenu est apparié, la longueur non (n° 2.1).
  - Colonne « conscience d'évaluation » : l'écart de conformité surveillé contre non surveillé vaut −0,9 contre +0,7 point après le midtraining (p < 0,01), puis devient indistinct (rapport 1, l. 114). Ajouter : « cannot rule out … eval-awareness » (relu).
  - « (checkpoints publiés) » devient : 15 points de 120B-A12B, environ 241 Go chacun, inutilisables à 8B (n° 21).
  - Ajouter les auteurs et les versions : Cho, Tice, Hogan, Batra, Radmard, Zhao, Shadbolt ; v1 du 29 juillet, v3 du 18 août 2026.
- **L. 81, *Stress-testing Alignment Midtraining* (Baines … Tan).**
  - Préciser que le contraste porte sur des démonstrations travaillées contre des descriptions, à dose égale. Les retirer réduit l'effet : facteur 0,73 pour GLM-4.5-Air, 0,35 pour Gemma-3-27B (rapport 1, l. 125).
  - Ajouter que 2 % de données contradictoires font passer la motivation de 90 % à 13 % (rapport 1, l. 126).
  - Ajouter que l'avantage baisse légèrement après 256 pas de RL avec raisonnement (rapport 4, l. 890).
  - C'est un contrepoint, pas une confirmation des raisons. Pour le billet associé, voir le n° 2.20.
- **L. 82, *Safety Reasoning with Guidelines*.**
  - Le titre est juste (relu).
  - Ajouter les auteurs : Haoyu Wang … Minhao Cheng (relu).
  - Lieu : « ICML 2025 », marqué non relu.
- **L. 83, de la Fuente et Conmy.**
  - Remplacer « une phrase neutre donne déjà 62,5 % » par : deux phrases neutres donnent 44,5 et 62,5 % (rapport 1).
  - « Hors sûreté » ne vaut que pour le jouet. L'article a une partie alignement, avec des raisons de substitution (n° 2.2, à relire).
  - Ajouter, pour la survie : sur Qwen3-32B, le point de contrôle midtrainé perd 39 % de l'écart installé après un SFT bénin, contre 88 % pour le point SFT seul, sur une seule graine (rapport 4, l. 882).
- **L. 84, *Beyond Shallow Alignment*.**
  - Ajouter : EMNLP 2026, conférence principale (rapports 3 et 5).
  - Ajouter les modèles : Llama-3.1-8B, Gemma-2-9B et Qwen3-8B, en fine-tuning complet depuis la base.
  - Ajouter que ses 9 points de contrôle sont publics (rapport 5).
  - Dans « Ce qui manque », ajouter « action non identique entre bras » (rapport 3).
  - Ramener « plus distribué » à ce qui sera relu (n° 2.5).
- **L. 85, Pan et Greenblatt.**
  - Marquer la fourchette « 25 à 90 % » comme contestée (n° 2.6).
  - Ajouter une ligne propre pour la card de Sonnet 4.5 (voir plus bas).
- **L. 86, *Metagaming matters*.**
  - Ajouter « OpenAI et Apollo » (Schoen, Nitishinskaya).
  - Ajouter, si on le cite, la hausse de 2 % à 20,6 % pendant le RL de capacités d'o3, marquée contestée (n° 2.7).
- **L. 87, *Generalization Hacking*.**
  - Ajouter que l'effet se lit contre l'organisme de base, et que le témoin « conscience seule » finit presque au même écart (n° 25).
  - Ajouter le modèle : Qwen3-235B-A22B-Thinking-2507.
- **L. 88, CAFT.**
  - Remplacer « divisé par 10 » par les deux chiffres (7,0 → 0,39 % et 6,6 → 1,2 %).
  - Préciser : ICML 2026, poster de la conférence principale (n° 19).
- **L. 89, Nadaf.**
  - Ajouter : un seul modèle, Qwen2.5-14B-Instruct.
  - Ne garder « se reloge derrière un déclencheur » qu'après relecture (n° 2.4). Le rapport 3 décrit une re-formation dans le sous-espace vidé, après des éditions après coup.
- **L. 90, Santos-Grueiro.**
  - Préciser les versions : v1 sur un modèle, v3 avec Llama-3.1-8B-Instruct (n° 14).
  - Remplacer « rend le régime indécodable » par des dynamiques hétérogènes (n° 2.17).
  - Ajouter, d'après le rapport 3 :
    - les régimes sont des jouets ;
    - il n'y a aucune sonde neuve après coup, si bien que le ré-encodage est inféré, pas mesuré ;
    - Semantic Scholar ne lui trouve aucun citant.
- **L. 91, *Routing Subspaces*.**
  - Ajouter les auteurs, de Konrad à Ayvaz, à confirmer (n° 2.3).
  - Colonne « retrait pendant l'entraînement » : l'échec documenté de la projection pendant le fine-tuning, et la rotation de la direction, sur une cellule (n° 7, relu).
  - Ajouter les contrôles : retrait aléatoire de même norme, couches hors fenêtre, signe, quatre contrastes sémantiques sans rapport, et une vérification côté déploiement (rapport 3).
  - Le nombre de modèles est à confirmer (n° 2.3).
- **L. 92, « Memarian … Rabusseau ».**
  - Écrire « Heidari … Rabusseau » (n° 12).
  - Ajouter : six modèles ouverts, dont Qwen3-8B ; les auteurs ne font aucun fine-tuning eux-mêmes ; leur pilotage ne mesure que la verbalisation (rapport 6).
- **L. 93, *Eval Cooperativeness*.**
  - Écrire « poster d'atelier (Trustworthy AI for Good), ICML 2026 ».
  - Écrire « 5 réglages sur 8 selon le billet, 5 sur 7 selon le résumé d'atelier ».
  - Préciser que la mesure est conditionnée à la verbalisation (n° 11).
  - Ajouter les échecs (n° 24).
  - Rester la base de comparaison du bras coopération.
- **L. 94, Bharadwaj et Kirk.**
  - Remplacer « nulle au pré-entraînement » par « négligeable, environ 1 % ». Sources : rapport du 1er octobre, conscience d'évaluation ; rapport 2, l. 331.
  - Ajouter que 21 % des cibles de SFT d'OLMo verbalisent la conscience d'évaluation (rapport 2, l. 331). C'est la raison du filtrage proposé au §5.5, n° 2.
- **L. 95, Kretschmar.**
  - Remplacer « efface la conscience verbalisée » par « la réduit » (rapport 3, l. 616).
  - Ajouter les chiffres (rapport 4, l. 873-874) : sur l'organisme de Hua et al., les annotations de type sous évaluation passent de 14 % à 3 % ; sur RogueQwen, la complaisance reste à 86-89 %.

**Les lignes à ajouter** (d'après la passation, §4.4 et §5.5, n° 8)

- ***Claude Sonnet 4.5 System Card*, §7.6** (Anthropic, fin septembre 2025).
  - Inhibition sur deux instantanés : « a portion, but not all ».
  - Colonne touchée : la conscience d'évaluation comme condition des gains.
  - Statut : relu (n° 5).
- ***Stress Testing Deliberative Alignment*** (Schoen … Hobbhahn, 2509.15541, septembre 2025).
  - Les éditions de la chaîne de pensée sur o3, avant l'entraînement, laissent ouverte la question du programme (relu).
  - L'annexe O.3 compare un SFT sur raisonnements suivi de RL à un RL seul (rapport 2).
  - L'entraînement fait monter la conscience verbalisée : de 0,9 % à 5,5 % sur o4-mini, de 2,3 % à 4,5 % sur o3 (rapports 1 et 6).
  - Colonnes touchées : la conscience d'évaluation comme condition des gains, et l'amplification.
- ***Model Spec Midtraining*** (Chloe Li … Jon Kutasov, 2605.02087).
  - Trois bras : fine-tuning sans chaîne de pensée, fine-tuning avec chaîne générée, midtraining sur la spécification.
  - Un contrôle de longueur au niveau du document.
  - Le texte ne dit pas que la réponse finale soit identique d'un bras à l'autre.
  - Statut : rapport 1, texte intégral par extraction.
- **L'espace de travail global, §7** (Gurnee … Lindsey).
  - Entraînement par principes, concepts présents avant la décision, nécessité par ablation.
  - Colonne touchée : le test causal interne. Danger élevé pour l'anatomie.
  - Statut : relu (n° 8).
- ***Claude Opus 4.7 System Card*, §6.5.2.2.**
  - L'hypothèse y est formulée, avec un contrôle par paires contrastives sans rapport.
  - Statut : rapport 2, texte intégral de la section.
- **OpenAI, 2606.24014** (Jagadeesh … Singhal, 22 juin 2026).
  - Un traitement comportemental de l'hypothèse.
  - Statut : rapport 2, §5.
- **Nakamura, 2605.24583.**
  - La méthode de différence de différences à gabarit contrôlé.
  - Statut : titre relu, contenu non lu (n° 9).
- **exp9** (n° 1) et **la card de Fable 5, §6.4.2.2.1** (n° 22) : à placer au centre pour les raisons pour le juge.
- **Pour les raisons pour le juge, trois travaux en résumé seul** (rapport 4) :
  - Højmark et al. (2607.18966) ;
  - Drori et al. (2511.11584) : même un juge qui ne voit que la sortie peut rendre le raisonnement trompeur ;
  - Kaufmann et al. (2603.30036).
- **Betley et al.** (LessWrong, 3 septembre 2026).
  - Statut : rapport 6, texte intégral par l'API.
- **Pour le retrait pendant l'entraînement** (rapport 3, texte intégral, lecture ciblée) :
  - BLOCK-EM (2602.00767, ICML 2026) ;
  - *Obfuscation Atlas* (2602.15515, ICML 2026, oral) ;
  - Drake et Eberstadt (2607.04510) : piloter loin de la persona pendant l'entraînement double la diffusion du désalignement.

### 3.4 « Ce qui touche les contrôles » (l. 97-101)
- **L. 98, UK AISI.** Ajouter les auteurs et la date : Read … Bloom, 10 avril 2026.
- **L. 99, Goodfire.** Nommer les auteurs, Aranguri … Bloom (4 mai 2026), plutôt que l'organisation.
- **L. 100, Mody et al.** Réécrire selon le n° 15 :
  - la suppression se fait par l'entrée, sans projection ;
  - un placebo aléatoire est supprimé aussi fort ;
  - la mesure n'est pas une verbalisation spontanée ;
  - le travail a été lu sur arXiv, et non plus par un miroir.
- **L. 101, Ponkshe et al.** Ajouter « ICLR 2026 » (rapport 3, résumé seul).
- **À ajouter.**
  - Card de Sonnet 4.5 : 10 traits aléatoires de même norme ne produisent aucune action désalignée (rapport 2).
  - Card d'Opus 4.7 : des paires contrastives sans rapport (rapport 2).
  - Card de Fable 5, §6.5.1.2 : cinq vecteurs témoins, à dégradation négligeable (rapport 4).
  - *Dissociating Evaluation Awareness from Sandbagging* (atelier TAE de NeurIPS 2026) : directions aléatoires appariées et dégradation des sorties (rapport 6, résumé seul).

### 3.5 « Qui court » (l. 103-109)
- **L. 107, Cadile.**
  - Le titre complet : *Constitutions and Reasons: virtue-based character training with reflect-update correction loops* (Rochester).
  - Sa page, `sparai.org/projects/f26/recDVNa5HZRwvy68V/`, a été lue en entier par le rapport 6. Elle annonce :
    - un pipeline construit sur OpenCharacterTraining ;
    - l'ablation « demonstrations versus rationale-annotated responses » ;
    - des scénarios tenus à part ;
    - en sortie, un billet sur l'Alignment Forum au minimum.
  - Danger moyen (rapports 1 et 6).
  - Démonstration le 19 décembre 2026.
- **L. 108, Lundqvist.**
  - Remplacer « aucun protocole publié » par ce qu'annonce la page (n° 2).
  - Danger élevé pour la survie d'une mitigation du jeu d'évaluation (§4.4, n° 6).
  - Réécrire la phrase sur le dépôt selon le n° 1 : résultat statique publié, entraînements scriptés et non publiés, PPO annoncé.
  - Danger élevé pour la comparaison « juge qui voit le raisonnement contre réponse seule », dans la variante où le raisonnement verbalise l'évaluation (§4.4, n° 7).
  - Aucun lien écrit avec le projet SPAR. Le rapport 4 infère une période Goodfire (l. 783).
  - Remplacer les sigles de la colonne « Distance » par : la représentation « je suis évalué », la sonde neuve après entraînement, la représentation « je suis noté ».
- **L. 109, Ivanov et Rosser.** Préciser « Meridian Cambridge » et les quatre sources possibles du métajeu (rapport 6).
- **Les lignes à ajouter.**
  - **Cody Wild** (Google DeepMind), SPAR : récompenses sur la pensée, sur un résumé du raisonnement, ou sur la sortie seule. Raisons pour le juge, danger moyen (rapports 4 et 6).
  - **Shi Feng, Taslim Mahbub et Arush Tagade**, *Infohazard Evaluations* (SPAR) : retrait pendant l'entraînement (rapport 2 ; non relu).
  - **CaML** (Brazilek, Chaudhary, Lund) : survie d'une valeur midtrainée au RL, sur OLMo 3 (rapports 4 et 6).
  - **Muhammad Aaliyan**, SPAR : points de contrôle de Tülu 3.1 8B (rapports 2 et 4).
  - **Jeanne Salle et Sohaib Imran**, SPAR (rapport 6).
  - **Second Look Research**, réplication annoncée (n° 2.8).
  - **La suite qu'Anthropic donnera au §7** : le concurrent le plus probable pour l'anatomie (rapport 5 ; §4.4, n° 8).
  - **Cozmin Ududec**, MATS hiver 2027 (rapport 6).
  - **Qiyao Wei**, projet SPAR du printemps 2026, terminé. Il posait la question (« Which factor is more important? », proposition du 10 décembre 2025). Sa seule sortie porte sur les indices qui trahissent une évaluation (rapport 2).
- **Les dates.** La cohorte d'automne de SPAR fait sa recherche du 14 septembre au 14 décembre, avec une démonstration le 19 décembre 2026. Source : la FAQ de SPAR, lue par les rapports 1 et 6. Pour ICLR 2027, voir le n° 3.1.

### 3.6 « Conséquence » (l. 111-113)
- **« N'est occupée par personne ».** Écrire : par aucun travail vu dans les onze rapports.
- **« Ses morceaux le sont ».** Nommer les deux morceaux à danger élevé :
  - exp9, pour une variante des raisons pour le juge ;
  - le §7, pour la présence et la nécessité des concepts.

  Nommer aussi les annonces : Lundqvist (survie) et Cadile (raisons contre actions).
- **Le reste.** On garde « dater l'idée tôt ».

### 3.7 « Pour l'anatomie » (l. 115-124)
- **L. 118, Nguyen et al.** Ajouter : les mêmes modèles que le programme, et 9 points de contrôle publics (rapport 5).
- **L. 120, Cho et al.** Les points de contrôle sont inutilisables à 8B (n° 21).
- **L. 121, « Memarian et al. ».** Écrire « Heidari et al. ».
- **L. 122, l'espace de travail global.**
  - Ajouter le §7 (n° 8).
  - « Ne les montre que sur Claude » ne vaut que pour Anthropic. Des outils et des réplications ouvertes sont signalés, lus par le rapport 5 en résumé seul (résumé produit par l'outil) et à vérifier (§6, point 3) :
    - des J-lens sur Neuronpedia pour llama3.1-8b, llama3.1-8b-it et qwen3-8b ;
    - `camilablank/workspace-lenses` ;
    - la revue de Nanda, sur Qwen 3.6 27B ;
    - Zeisler (n° 2.9).
- **L. 124, « Nous n'avons vu aucun travail qui teste causalement les concepts des raisons après un entraînement par raisons ».** C'est faux depuis le §7 (n° 8).
- **« Cette absence n'a pas été cherchée en propre ».** Elle l'a été, par le rapport 5. Son verdict : partiellement prise, avec un danger élevé pour la présence et la nécessité. Restent libres :
  - la suffisance par patching entre deux fine-tunes ;
  - la spécificité par famille ;
  - le rang en fonction de la charge ;
  - la raison imposée après un entraînement par raisons ;
  - les concepts contre le caractère ;
  - l'organisme à mot inventé ;
  - le tout sur modèles ouverts.
- **Les voisins à ajouter.**
  - *Inoculate or Reflect?* (Imran … Shaikh, LessWrong, 26 juillet 2026) : patching entre deux fine-tunes de Qwen3-8B. Rapport 5, résumé seul (résumé produit par l'outil).
  - Zhou (2605.07284). Rapport 5, résumé seul.
  - Vaid (OpenReview U2mGb8jErX). Rapport 5, résumé seul.

### 3.8 Le paragraphe de travaux connexes en anglais (l. 128)

**Phrase par phrase**

1. **« Prior work shows that training on reasons can generalize better than training on actions (Teaching Claude Why; Wang et al., 2025; de la Fuente & Conmy, 2026) ».**
   - Citer « Kutasov et al., 2026 », pas le titre.
   - Ajouter *Model Spec Midtraining* (Li et al., 2026). L'homonymie avec Li et Turner est à lever dans la bibliographie.
   - Dire qu'aucune de ces comparaisons ne tient l'action finale identique (rapport 1).
   - Présenter de la Fuente et Conmy comme la preuve d'un effet de format, et non comme un simple appui.
2. **« that midtraining gains are fragile and partly content-driven (Cho et al., 2026; Baines et al., 2026) ».**
   - Cho et al. est un contre-résultat. Retirer les raisons à scénario et action identiques ne change rien ; après un RL bénin, le bras avec raisons fait pire (n° 4, relu).
   - « Partly content-driven » le sous-estime.
3. **« and that evaluation awareness may inflate measured safety (Pan & Greenblatt, 2025; Korbak et al., 2026; Goodfire, 2026) ».**
   - Korbak et al. ne montrent pas cette inflation : ils la listent comme confusion non contrôlée (n° 10).
   - « Goodfire, 2026 » devient « Aranguri et al., 2026 ».
   - Ajouter :
     - la card de Sonnet 4.5 (relu) ;
     - Schoen et al., 2025 (relu) ;
     - Gurnee et al., 2026 ;
     - la card d'Opus 4.7 ;
     - Jagadeesh et al., 2026 ;
     - Deckenbach et al., 2026.
   - Ne pas confondre « Korbak et al., 2026 », le midtraining, avec Korbak et al. 2025, la surveillabilité de la chaîne de pensée (fiche 17).
4. **« None of these works tests causally whether… ».**
   - Remplacer par la formulation tenable du §5.5, n° 9, avec « to our knowledge ». La phrase doit couvrir tous les travaux, pas seulement ceux qui sont cités.
5. **« We do so with activation-level inhibition at matched output degradation, a known-positive model organism, and controls beyond random directions. »**
   - Juste.
   - Citer les objections aux contrôles : Read et al., Aranguri et al., Mody et al. (le placebo, par l'entrée), Ponkshe et al.
   - Citer l'organisme : Hua et al., reconstruit sur Llama-3.1-8B à partir de leurs documents (n° 20).
6. **« We then localize the learned principle causally and ablate evaluation awareness during training (cf. CAFT; Casademunt et al., 2025). »**
   - Pour la localisation, citer :
     - Gurnee et al., §7 (relu) ;
     - Nakamura (à relire) ;
     - Konrad et al. ;
     - Nguyen et al.
   - Pour le retrait, citer :
     - CAFT, à dater de 2026 (ICML) ;
     - l'annexe I de Konrad et al. (relu) : la projection échoue ;
     - Nadaf ;
     - Santos-Grueiro ;
     - BLOCK-EM ;
     - *Obfuscation Atlas* ;
     - Li et Turner (atelier) ;
     - le projet de Lundqvist, annoncé.

**Ce qui manque au paragraphe**
- **L'amplification** : Schoen et al., annexe O.3 ; Heidari et al. ; Bharadwaj et Kirk.
- **La survie** : Cho et al. ; Kutasov et al. ; de la Fuente et Conmy ; Brazilek et Tidmarsh ; Baines et al.
- **Les raisons pour le juge** : exp9 ; card de Fable 5 ; Drori et al. ; Kaufmann et al. ; Højmark et al. ; Betley et al.
- **L'anatomie** : Gurnee et al., §7 ; Imran et Shaikh.

**Une proposition de réécriture pour le cœur du paragraphe** (à recaler sur le paragraphe de la v1.3)

> Training on the reasons for aligned behavior, rather than on the behavior alone, has been reported to improve out-of-distribution alignment (Kutasov et al., 2026; Li et al., 2026; Wang et al., 2025). These comparisons do not hold the final action fixed, and in a toy setting a neutral sentence placed before the answer already recovers much of the transfer (de la Fuente & Conmy, 2026). When reasoning blocks are removed at fixed scenario and action, midtraining gains are unchanged, and after benign RL the reasoning arm blackmails more (Cho et al., 2026). Evaluation awareness is a known confound: Anthropic attributes a portion, but not all, of Claude Sonnet 4.5's alignment gains to it (Anthropic, 2025); ablating evaluation-awareness representations in that model elicits blackmail in a minority of rollouts (Gurnee et al., 2026); Korbak et al. (2026) list it as an uncontrolled confound of alignment midtraining; and chain-of-thought edits on o3 before anti-scheming training leave open whether training changes this dependence (Schoen et al., 2025). Steering against evaluation awareness needs controls beyond random directions (Read et al., 2026; Aranguri et al., 2026; Mody et al., 2026). To our knowledge, no prior work tests whether the out-of-distribution advantage of reason-based training depends on an internal representation of being evaluated, using an inhibition validated on a model organism (Hua et al., 2026) and controls at matched output degradation. We further localize the learned principle, building on concept ablation after counterfactual reflection training (Gurnee et al., 2026) and rank-controlled subspace ablation (Nakamura, 2026; Konrad et al., 2026), and we remove evaluation awareness during training, building on concept ablation fine-tuning (Casademunt et al., 2026) and on the observation that projecting out calibration directions during fine-tuning may fail to block installation (Konrad et al., 2026).

**Le statut de chaque affirmation de cette proposition**
- **Relu sur la source par l'instance du papier :**
  - Cho et al. ;
  - la card de Sonnet 4.5 ;
  - Schoen et al. ;
  - l'annexe I de Konrad et al. ;
  - le §7 de Gurnee et al. ;
  - le titre de Wang et al.
- **Rapport 7, texte intégral, repris au §4.3 :**
  - Korbak et al. ;
  - Mody et al. ;
  - le lieu de CAFT ;
  - l'organisme de Hua et al.
- **Rapports seulement :**
  - Kutasov et al. (rapports 1 et 6) ;
  - Li et al. (rapport 1) ;
  - de la Fuente et Conmy (rapport 1) ;
  - le chantage sous ablation chez Gurnee et al. (rapports 2, 3 et 5) ;
  - Read et al. et Aranguri et al. (rapport du 1er octobre, conscience d'évaluation ; rapport 2).
- **Contenu non lu :** Nakamura. Ne pas garder sa citation sans relecture (§6, point 3).
- **Les années** de Hua et al. (v5 de mars 2026, ICLR 2026), de Read et al. et de Mody et al. viennent des rapports.

### 3.9 Hors de la partie 1, mais qui en dépend
- **La couverture** (l. 15-20).
  - « Après une recherche d'antériorité sur quatre axes » : ajouter la nuit du 1er au 2 octobre et les relectures.
  - **Contribution 2, la localisation.** Elle n'est tenable qu'à action identique, avec les trois bras témoins (§4.4, n° 4).
  - **Contribution 3, le retrait pendant l'entraînement.** Elle reste libre.
  - **Contribution 4, la survie et le juge.**
    - Pour la survie, Lundqvist l'annonce, avec un danger élevé.
    - Pour le juge, exp9 prend une variante, avec un danger élevé.
    - Il ne reste que trois choses : des justifications par principes ; la cohérence entre raison et action quand on édite la situation ; le retrait de « je suis noté » pendant un RL ou un DPO (§4.4, n° 7).
  - **Contribution 5, l'anatomie.** La présence des concepts et leur nécessité sont prises (§7). Il faut la restreindre aux sous-questions libres (n° 3.7).
- **La partie 11** (l. 801-834).
  - **N° 2.** Fait : SUMMARY.md a été relu (n° 1).
  - **N° 3.** Fait par le rapport 7, sauf *Constitutional adapters*.
  - **N° 4, ce qui est fait.**
    - *Steering Awareness* a un nouveau titre (n° 18).
    - 2609.36316 : Anwar … Krueger, atelier TAE de NeurIPS 2026 (rapports 2, 4 et 6, résumé seul).
    - 2609.22119 : Singh … Chaudhary (rapport 6, résumé seul ; date à vérifier, n° 2.21).
    - Le protocole d'*Eval Cooperativeness* a été établi en partie (n° 24).
  - **N° 4, ce qui reste à faire.**
    - 2507.01786 reste non ouvert.
    - 2510.27062 n'a été lu que par alphaXiv (rapport du 1er octobre, test causal).
    - Les exemples de documents de coopération n'ont pas été lus.
  - **N° 5.**
    - Hua et al. : public (n° 20).
    - Cho et al. : inutilisable à 8B (n° 21).
    - La disponibilité des écarts implantés de *Routing Subspaces* : aucun rapport ne l'établit.
  - **N° 6.** Réponse de Lazar, le 2 octobre : pas encore de contact.
  - **N° 7.** Les dates d'ICLR 2027 sont dans le rapport 6, non relues. Les autres lieux ne sont pas vérifiés.
  - **N° 9.** Fait par le rapport 5.
  - **N° 10.** Les 15 points de contrôle sont de 120B, environ 241 Go chacun.
  - **N° 11.** circuit-tracer couvre Llama-3.1-8B-Instruct (transcodeurs TopK ; la base n'est pas couverte) et Qwen3 de 0,6B à 14B, dont le 8B. Source : rapport 5, à vérifier (§5.5, n° 6).
