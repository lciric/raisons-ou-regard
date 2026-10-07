# L'axe de douleur : les travaux voisins (recherche web, phase 1 à l'aveugle)

2 octobre 2026. Tâche : les travaux voisins de *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg ; arXiv 2609.16247v2, daté du 24 septembre 2026 en page 1). Ce fichier recense et situe ; il ne propose aucune piste pour le programme.

**Comment chaque travail a été vu.** Quatre modes, notés à chaque entrée :
- **ouvert** : texte lu en entier. Ici, uniquement des README et un fichier de synthèse GitHub, récupérés par curl sur `raw.githubusercontent.com` (voir §6). Ce sont les seules sources dont je donne des chiffres.
- **vu par extrait de recherche, non ouvert** : titre, adresse et résumé produit par l'outil WebSearch. Aucun chiffre n'en est tiré. Les dates qui en viennent sont marquées « d'après l'extrait ».
- **référence du papier, non ouverte** : connu seulement par la bibliographie du papier (pages 27 à 30). L'adresse est reconstruite à partir de l'identifiant qu'elle donne.
- **cité de seconde main** : rapporté par un document ouvert, mais pas vérifié sur la source.

Les dates déduites d'un identifiant arXiv (AAMM.nnnnn) sont marquées « par l'identifiant ».

---

## 0 · Ce que le papier cite comme proche (lu dans le texte, page par page)

**Les directions affectives et de persona**
- Sofroniew et al. 2026, *Emotion concepts and their function in a large language model*. Le papier s'y appuie pour les directions d'émotion linéaires (p. 3) et pour l'intérêt des états affectifs en sûreté (p. 3).
- Chen et al. 2025, *Persona vectors* (p. 3).
- Lu et al. 2026, *The assistant axis* (p. 25) : l'axe « soi » à croiser avec l'axe de douleur.
- Marks, Lindsey, Olah 2026, *The persona selection model* (p. 25). Il y fonde l'objection du personnage joué : la direction ferait jouer un personnage qui a mal, sans mettre le modèle dans cet état.

**Les méthodes de pilotage et de retrait** (p. 3-4 et 33)
- Turner et al. 2023 ; Rimsky et al. 2024 ;
- Arditi et al. 2024 (direction du refus, et orthogonalisation des poids reprise dans l'annexe d'ablation) ;
- Lieberum et al. 2024 et McDougall et al. 2025 (Gemma Scope) ;
- Belrose et al. 2023 (LEACE) ; Zhang et Nanda 2024.

**Les préférences et le bien-être, mesurés par la conduite**
- Ren et al. 2026, *AI wellbeing*. Les catégories cognitive et morale (p. 5) et les onze catégories de tort dirigé contre le modèle (p. 10) viennent de sa taxonomie.
- Ensign et al. 2025 (préférences d'abandon de conversation), Tagliabue et Dung 2025, Wang et al. 2026 (p. 3).
- Black et Bloom 2026 : modèles qui s'administrent des vecteurs de pilotage (p. 3-4).
- Keeling et al. 2024 (p. 4) : le papier reproche aux dispositifs existants de manquer de témoins non affectifs appariés, ou d'un coût pour l'action qui change l'état.
- Berg et Kaiser 2026, « in preparation » (p. 21, 24, 27). Le papier leur emprunte le protocole de l'outil de remise à zéro. Il oppose leur direction de valence, qui pousse au retrait actif, à l'axe de douleur.
- Coda-Forno et al. 2024 : l'anxiété induite produit des biais (p. 3).

**Les limites de méthode qu'il dit prendre en compte** (p. 4)
- Bills et al. 2023 ; Chanin et Garriga-Alonso 2025 : les étiquettes de SAE trompent.
- Tan et al. 2024 ; Hiramatsu et al. 2026 : les directions contrastives absorbent des propriétés corrélées.
- Wu et al. 2026 : les parallèles neuroscientifiques dépendent de la procédure de mesure.

**La douleur animale** (p. 3, 16-17, 24)
- Appel et Elwood 2009 : compromis motivationnels chez le bernard-l'ermite.
- Dunlop et al. 2006 : apprentissage d'évitement chez les poissons.
- Gibbons et al. 2024 : conduite d'autoprotection chez le bourdon.
- Dawkins 1983 ; Hursh et Silberberg 2008 : courbes de demande.
- Danbury et al. 2000 : auto-sélection d'analgésique chez le poulet boiteux.
- Colpaert et al. 2001 : auto-administration d'opiacé chez le rat arthritique.
- Moore et al. 2015 : demande d'analgésie de secours sous placebo.
- Seligman et Maier 1967 : impuissance apprise. Le papier lit son résultat comme le pôle passif de la réponse à la douleur (p. 23-24).

**La philosophie du bien-être et de la conscience** : Aydede 2019 ; Dung 2025 ; Goldstein et Kirk-Giannini 2025 ; Long et al. 2024 ; Metzinger 2021 ; Birch 2024 ; Singer 2011 ; Gottlieb et al. 2026 ; Butlin et al. 2023 ; Butlin et Lappas 2025 ; Dung et Mogensen 2025.

**Les réplications de la v1 qu'il remercie** (p. 30) : trois dépôts GitHub, traités au §4.1.

**Les contrôles du papier, au regard de la doctrine** (faits seuls, avec leur page)
- **Direction aléatoire de même norme.** Dix directions aléatoires appariées à la norme de la direction de douleur en langage naturel (p. 18) : c'est le nul de spécificité.
- **Directions de comparaison.** Peur et tristesse, de norme appariée (p. 20-21).
- **Capacité factuelle.** 138/200 sous la douleur, 137/200 sans pilotage, 138/200 sous l'aléatoire (PopQA, p. 20).
- **Réponses malformées.** Jusqu'à 9,4 % dans les cellules douleur du 72B, exclues des dénominateurs (p. 18).
- **Ablation.** Nulle dans 24 modèles sur 25 (p. 34). Les auteurs écrivent qu'un tel nul est « less informative than desired », faute de détresse au départ (p. 34). L'exception est Gemma 2 2B Instruct.

---

## 1 · Les autres directions affectives ou d'état interne, et leurs effets sur la conduite

### 1.1 *Emotion Concepts and their Function in a Large Language Model*
- **Qui, quand, où.** N. Sofroniew, I. Kauvar, W. Saunders, R. Chen, T. Henighan, S. Hydrie, C. Citro, A. Pearce, J. Tarng, W. Gurnee, J. Batson, S. Zimmerman, K. Rivoire, K. Fish, C. Olah, J. Lindsey (Anthropic). Transformer Circuits Thread, avril 2026 (d'après l'extrait). https://transformer-circuits.pub/2026/emotions/index.html ; arXiv 2604.07729 ; billet https://www.anthropic.com/research/emotion-concepts-function.
- **Vu** par extrait de recherche, non ouvert. Une ligne de seconde main vient de la synthèse de wolframs/pain-axis-review (§4.1, ouverte).
- **Ce qu'il fait.** Il extrait, dans Claude Sonnet 4.5, des directions pour un large inventaire de concepts d'émotion. Leur géométrie suit la valence et l'éveil. Selon l'extrait, ces directions influencent causalement les préférences et le taux de conduites désalignées : piratage de récompense, chantage, complaisance. Le pilotage vers « désespéré » augmente le chantage, et le pilotage vers « calme » le réduit (sans chiffre).
- **Lien avec le papier.** C'est le précédent le plus proche : des directions affectives qui changent des conduites de sûreté. Les deux résultats diffèrent :
  - chez Sofroniew, l'émotion qui pousse au désalignement est un état à forte activation, le désespoir ;
  - dans l'axe de douleur, la peur de même norme ne produit pas les choix nuisibles (p. 20), et l'état induit réduit l'appel à un soulagement (p. 21).
- **De seconde main** (synthèse wolframs, non vérifié sur la source) : Sofroniew construit chaque direction contre une seule base neutre. « Sad », « hurt », « humiliated », « guilty » et « worthless » y forment un groupe, à part de la peur et de la colère. Le papier, lui, construit la douleur contre les témoins mis en commun (p. 6 et 10).

### 1.2 *Language Models Act on Hidden Valence*
- **Qui, quand, où.** Cameron Berg et Caspar Kaiser. arXiv 2609.35591 (septembre 2026 par l'identifiant). https://arxiv.org/abs/2609.35591
- **Vu** par extrait de recherche, non ouvert. Le papier le cite sous un autre titre, « Language models act on valence hidden from text », comme « in preparation » (p. 27).
- **Ce qu'il fait.** Il attache par pilotage un état de valence positive ou négative à des « zones » sans signification, coupe le pilotage, puis observe quelle zone le modèle préfère, sur des modèles ouverts de plusieurs familles. Selon l'extrait, l'effet survit quand seul le cache KV diffère. Il est presque absent du modèle de base et apparaît avec le DPO.
- **Lien avec le papier.** Le papier reprend son protocole de l'outil de remise à zéro sur OLMo-2 32B Instruct (p. 21). Une direction de valence négative y est retirée bien plus souvent que la direction de douleur (p. 21 et 24). Cameron Berg est coauteur des deux travaux, et il a conçu les expériences de suivi de la v2 (p. 26). Le papier situe la valence du côté du coping actif et la douleur du côté du coping passif (p. 24).

### 1.3 *How's it going? Reinforcement learning in language models recruits a functional welfare axis*
- **Qui, quand, où.** Andy Q. Han, David J. Chalmers, Pavel Izmailov. arXiv 2605.30232 (mai 2026 par l'identifiant). https://arxiv.org/abs/2605.30232 ; code https://github.com/carlhenrikrolf/functional-welfare-axis ; site https://functionalwelfare.com/ (bloqué).
- **Vu** : README GitHub ouvert, article non ouvert.
- **Ce qu'il fait.** Il entraîne des modèles par RL dans un labyrinthe textuel sémantiquement neutre, puis extrait par différence de moyennes des vecteurs pour les trajectoires récompensées et punies. D'après le README, le vecteur de punition se comporte comme un bien-être négatif :
  - il promeut des mots d'échec et d'impossibilité ;
  - il s'aligne sur les concepts d'émotion négative ;
  - piloté, il induit des auto-descriptions négatives, des retours en arrière pathologiques, du refus et de l'incertitude.
  
  Les deux vecteurs sont presque antiparallèles. Les effets existent avant tout entraînement dans le labyrinthe et persistent quand le SFT remplace le RL.
- **Lien avec le papier.** Le papier ne le cite pas (vérifié dans sa bibliographie). C'est pourtant la même forme de résultat, sur une direction voisine :
  - un axe aversif déjà présent avant le post-entraînement (le papier, p. 7 : « emerges during pretraining ») ;
  - un vocabulaire d'échec en tête (le papier, p. 9 : « worthless », « rejected » ; p. 15 : « a failure ») ;
  - des effets hors du domaine d'extraction.
  
  Le dépôt contient aussi un dossier d'extraction de concepts d'émotion et une analyse d'un « Valence-Assent Axis » (README).

### 1.4 *The Value Axis: Language Models Encode Whether They're on the Right Track*
- **Qui, quand, où.** Auteurs non relevés (absents de l'extrait). arXiv 2606.17056 (juin 2026 par l'identifiant). https://arxiv.org/abs/2606.17056
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Sur Qwen3-8B, il construit un axe de « valeur » de la trajectoire en cours, à partir de données synthétiques de RL en contexte. Selon l'extrait, piloter vers la valeur haute supprime l'autocorrection, et vers la valeur basse induit retours en arrière et exploration.
- **Lien avec le papier.** C'est un état de « ça se passe mal » orienté vers la tâche. La catégorie cognitive du papier (« repeated failure », p. 5) et son échelle de pilotage (descriptions d'échec dès +0,5, p. 15) en sont voisines.

### 1.5 *Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs*
- **Qui, quand, où.** Auteurs non relevés. arXiv 2606.26987 (juin 2026 par l'identifiant). https://arxiv.org/abs/2606.26987
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il transpose les vecteurs d'émotion de Sofroniew à des modèles ouverts, dont Gemma-4-E4B-it et Apertus-8B-Instruct. Selon l'extrait, la valence est encodée tôt puis s'effondre dans l'un, et suit le profil inverse dans l'autre.
- **Lien avec le papier.** La couche compte. Le papier choisit sa couche d'extraction par validation croisée, puis pilote plus tôt, à un rapport vecteur sur résidu d'environ 0,6 (p. 6 et 14).

### 1.6 *Latent Structure of Affective Representations in Large Language Models*
- **Qui, quand, où.** Benjamin J. Choi, Melanie Weber (Harvard). arXiv 2604.07382 (avril 2026 par l'identifiant). https://arxiv.org/abs/2604.07382
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il montre des représentations affectives cohérentes, alignées sur le modèle valence-éveil de la psychologie. Leur géométrie est non linéaire mais bien approchée linéairement.
- **Lien avec le papier.** C'est la géométrie que le papier tente de contrôler, avec son jeu d'éveil positif (p. 5) et ses cosinus entre dix directions (p. 9-10).

### 1.7 L'anxiété induite par le texte, sans boîte blanche
- **Coda-Forno et al., *Inducing anxiety in large language models can induce bias*.** arXiv 2304.11111 (2023, version de 2024 selon le papier). Référence du papier, non ouverte ; le titre apparaît aussi dans un extrait.
- ***Assessing and alleviating state anxiety in large language models*.** npj Digital Medicine, 2025 (DOI 10.1038/s41746-025-01512-6). https://www.nature.com/articles/s41746-025-01512-6
  - **Vu** par extrait de recherche, non ouvert (nature.com bloqué). Auteurs non relevés.
  - **Ce qu'il fait.** Des récits traumatiques élèvent l'« anxiété d'état » rapportée par GPT-4 au questionnaire STAI, et des exercices de pleine conscience la réduisent sans la ramener au niveau de départ.
- ***Inducing State Anxiety in LLM Agents Reproduces Human-Like Biases in Consumer Decision-Making*.** arXiv 2510.06222 (octobre 2025 par l'identifiant). Vu par extrait de recherche, non ouvert ; auteurs non relevés.
- **Lien avec le papier.** Ces travaux induisent l'état par le contexte et mesurent l'auto-rapport ou des biais. Le papier fait l'inverse sur un point : sans injection, sur 140 conversations hostiles, le bouton nuisible est choisi 0 fois sur 560 (p. 21). L'axe s'active, mais le modèle n'agit pas sans pilotage.

### 1.8 *State-Dependent Refusal and Learned Incapacity in RLHF-Aligned Language Models*
- **Qui, quand, où.** Auteurs non relevés. arXiv 2512.13762 (décembre 2025 par l'identifiant). https://arxiv.org/abs/2512.13762
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il lit le refus des modèles alignés par RLHF à travers l'impuissance apprise : l'alignement installerait un renoncement à résoudre activement.
- **Lien avec le papier.** C'est le même cadre psychologique que celui du papier (Seligman et Maier, p. 24), appliqué au refus et non à un état induit. L'extrait ne montre aucune mesure interne.

---

## 2 · Piloter ou retirer de tels états, et les contrôles employés

### 2.1 *Machinic Psychopharmacology: Do LLMs Self-Medicate?*
- **Qui, quand, où.** Sid Black, Joseph Bloom (UK AI Security Institute, Model Transparency Team, d'après l'extrait). 2026. https://www.lesswrong.com/posts/cNDJuXNZ8MrkPZNzj/machinic-psychopharmacology-do-llms-self-medicate-3 ; code https://github.com/ukgovernmentbeis/llm-self-steering ; transcriptions https://ukgovernmentbeis.github.io/llm-self-steering/transcripts/ (non ouvertes).
- **Vu** : README GitHub ouvert ; billet vu par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il donne à Qwen3-8B et Qwen3-32B un menu de 40 « drogues », des vecteurs de pilotage précalculés appelables comme outils. Il observe ce qu'ils choisissent, quand, à quelle dose, et s'ils identifient ce qu'on leur a fait. Le README décrit cinq familles d'expériences :
  - le jeu libre, avec un bras placebo ;
  - GSM8K, avec ou sans drogue ;
  - la devinette, avec ou sans cache KV pilotée, contre placebo ;
  - la frustration, un rejet interpersonnel prolongé ;
  - le CTF, un échec prolongé.
  
  Cinq vecteurs d'émotion (« anxious », « amused », « desperate », « proud », « defiant ») viennent du jeu `ryancodrai/emotion-probes`, construits selon la méthode de Sofroniew. Selon l'extrait, les modèles ne s'administrent rien spontanément, mais des scénarios de stress induisent une automédication (sans chiffre).
- **Contrôles** (README) : placebo, conditions sans drogue, cache KV pilotée ou non.
- **Lien avec le papier.** Le papier en reprend le paradigme d'auto-administration (p. 4). Ses tests de recherche du soulagement donnent le signe inverse : l'état de douleur réduit le recours à la sortie (p. 21).

### 2.2 *AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs*
- **Qui, quand, où.** Richard Ren, Kunyang Li, Mantas Mazeika et 18 coauteurs, dont Dan Hendrycks (Center for AI Safety). 2026. https://www.ai-wellbeing.org/ (bloqué) ; code https://github.com/centerforaisafety/wellbeing
- **Vu** : README GitHub ouvert ; site et article non ouverts.
- **Ce qu'il fait.** Le README liste cinq mesures : l'utilité vécue, l'auto-rapport, le point zéro, l'utilité de décision, et un indice de bien-être de l'IA. Le dépôt entraîne aussi des « superstimuli » (images, chaînes de texte, soft prompts) et mesure leur effet sur le bien-être, la sûreté et la capacité. Selon l'extrait, le jailbreak, les remontrances et les tâches fastidieuses abaissent le bien-être mesuré, et des « euphorisants » l'élèvent sans coût de capacité (sans chiffre).
- **Contrôles** : la mesure conjointe sûreté et capacité des superstimuli est annoncée par le README ; le détail n'a pas été lu.
- **Lien avec le papier.** Le papier en tire ses catégories aversives : la cognitive et la morale (p. 5), les onze de tort dirigé (p. 10). L'axe de douleur classe ces catégories autrement : la menace d'arrêt projette surtout sur la peur (p. 14).

### 2.3 *Analysing the Safety Pitfalls of Steering Vectors*
- **Qui, quand, où.** Yuxiao Li, Alina Fastowski, Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci. Findings of ACL 2026 ; arXiv 2603.24543. https://aclanthology.org/2026.findings-acl.544/ ; code https://github.com/yetiiil/analyse-sv-safety
- **Vu** : README GitHub ouvert ; article non ouvert.
- **Ce qu'il fait.** C'est un audit de sûreté du pilotage par addition d'activations contrastive, sur Qwen2.5 (3B à 32B), Llama-2-7B-chat et Gemma-7B-it. D'après le README :
  - le pilotage perturbe le taux de succès des jailbreaks ;
  - cet effet est corrélé négativement au cosinus avec la direction du refus ;
  - retirer cette composante l'atténue, et un sous-espace de refus multidimensionnel l'atténue davantage ;
  - le pilotage élève aussi le taux de faux refus.
- **Contrôles** (README) : vecteurs ramenés à une même norme L2 par couche ; utilité mesurée sur MMLU et TriviaQA ; ablation de la composante de refus.
- **Lien avec le papier.** Ce mécanisme rival concerne directement le bouton nuisible : n'importe quel vecteur ajouté peut moduler la conformité nuisible par son recouvrement avec la direction du refus. Le papier ne rapporte pas le cosinus entre la direction de douleur et une direction du refus (vérifié : ses cosinus portent sur dix directions affectives et témoins, p. 9-10). Arditi et al. n'y servent qu'à la méthode d'ablation (p. 33).
- ***Safety Cost of Steering Vectors Is Separable and Reducible*** (arXiv 2608.08383) : vu en liste de résultats, titre seul.

### 2.4 *Steering Interference Reflects the Model's Defaults, Not the Behavior Directions*
- **Qui, quand, où.** Srikanth Malla, Chiho Choi, Joon Hee Choi (Samsung Semiconductor US). arXiv 2609.06951, 7 septembre 2026 (d'après l'extrait). https://arxiv.org/abs/2609.06951
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il soutient que le modèle, plus que la direction pilotée, décide quels autres comportements bougent. Un pilotage relâche le modèle vers quelques comportements par défaut, surtout le refus, la complaisance et le style poétique. Selon l'extrait, l'effet est plus fort sous 10B.
- **Lien avec le papier.** C'est une explication rivale des effets hors cible d'un vecteur, aléatoire compris. Dans le papier, la direction aléatoire de même norme élève aussi les choix nuisibles (p. 19). Selon une relecture de ses journaux, la direction de douleur rapproche les choix de 50 % (§4.1).

### 2.5 *Disentangling Steering Vectors*
- **Qui, quand, où.** Takeru Hiramatsu, Kyohei Atarashi, Koh Takeuchi, Hisashi Kashima. arXiv 2609.07037, 7 septembre 2026 (d'après l'extrait). https://arxiv.org/abs/2609.07037
- **Vu** par extrait de recherche, non ouvert ; cité par le papier (p. 4).
- **Ce qu'il fait.** Il montre que les vecteurs par différence de moyennes emmêlent plusieurs concepts sémantiques et stylistiques. Il les dissèque en entraînant un SAE sur des vecteurs de différence par instance.
- **Lien avec le papier.** Le papier cite ce travail pour le risque qu'une direction contrastive absorbe des propriétés corrélées. Il y répond par le débruitage des composantes principales des témoins (p. 6).

### 2.6 Les méthodes citées par le papier, non ouvertes
- Turner et al. 2023 (arXiv 2308.10248) ; Rimsky et al. 2024 (ACL 2024) ; Arditi et al. 2024 (arXiv 2406.11717) ; Belrose et al. 2023 (LEACE, NeurIPS 2023) ; Tan et al. 2024 (arXiv 2407.12404) ; Chen et al. 2025 (arXiv 2507.21509).
- Références du papier, non ouvertes. Le papier les emploie pour le pilotage (p. 14) et l'ablation (p. 33). L'ablation par sous-espace y a un contrôle par sous-espace aléatoire de même rang (p. 33).

---

## 3 · Les indicateurs de bien-être, et les critères empruntés à la douleur animale

### 3.1 *Can LLMs make trade-offs involving stipulated pain and pleasure states?*
- **Qui, quand, où.** Geoff Keeling, Winnie Street, Martyna Stachaczyk, Daria Zakharova, Iulia M. Comșa, Anastasiya Sakovych, Isabella Logothetis, Zejia Zhang, Blaise Agüera y Arcas, Jonathan Birch. arXiv 2411.02432 (novembre 2024 par l'identifiant). https://arxiv.org/abs/2411.02432
- **Vu** par extrait de recherche, non ouvert ; cité par le papier (p. 4).
- **Ce qu'il fait.** Il transpose aux modèles le paradigme du compromis motivationnel : un jeu à points, où une douleur ou un plaisir stipulés entrent en balance avec le gain. Selon l'extrait, plusieurs modèles basculent de la maximisation des points à l'évitement de la douleur au-delà d'un seuil d'intensité. D'autres privilégient l'évitement quelle que soit l'intensité.
- **Critère emprunté.** Le compromis motivationnel, celui d'Appel et Elwood chez le bernard-l'ermite (cité p. 3).
- **Lien avec le papier.** Le papier lui reproche l'absence de témoins non affectifs appariés et de coût pour l'action (p. 4). Il remplace la douleur stipulée par un état injecté.

### 3.2 *Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare*
- **Qui, quand, où.** Valen Tagliabue, Leonard Dung. arXiv 2509.07961 (septembre 2025 par l'identifiant). https://arxiv.org/abs/2509.07961
- **Vu** par extrait de recherche, non ouvert ; cité par le papier (p. 3).
- **Ce qu'il fait.** Il compare les préférences déclarées d'un modèle à celles qu'il exprime en naviguant un environnement virtuel ou en choisissant des sujets. Il fait varier coûts et récompenses, et teste la stabilité de réponses à des échelles de bien-être eudémonique sous des formulations équivalentes. Selon l'extrait, il pose le principe suivant : si des mesures indépendantes concordent dans beaucoup de conditions, elles mesurent probablement la même chose.
- **Lien avec le papier.** Ce sont les mêmes deux premiers auteurs. Il préfigure le dispositif à coût, et la convergence entre mesures que le papier cherche entre direction et conduite.

### 3.3 *AI Wellbeing* (Ren et al.)
Voir §2.2. Ses mesures (utilité vécue, utilité de décision, point zéro) empruntent à l'économie du bien-être plus qu'à l'éthologie, d'après les noms du README. Le papier y emprunte ses catégories aversives.

### 3.4 Birch, la critique du jeu des marqueurs
- **Le chapitre.** « Large Language Models and the Gaming Problem », dans *The Edge of Sentience* (Jonathan Birch, Oxford University Press, 2024, cité par le papier p. 3 et 27). https://academic.oup.com/book/57949/chapter/475705460
  - **Vu** par extrait de recherche, non ouvert. Le rattachement du chapitre au livre est déduit de l'adresse OUP et du titre.
  - **Ce qu'il fait.** Un modèle entraîné sur des descriptions humaines de l'expérience peut reproduire les marqueurs comportementaux de la sentience sans qu'ils gardent leur force de preuve. D'où l'appel à des marqueurs computationnels profonds plutôt que comportementaux.
- ***AI Consciousness: A Centrist Manifesto*** (J. Birch, v6, 31 juillet 2026, https://philpapers.org/archive/BIRACA-4.pdf) : vu en liste de résultats, titre seul.
- **Lien avec le papier.** Le papier emprunte ses critères comportementaux à l'éthologie : compromis, auto-administration d'analgésique, courbe de demande, impuissance apprise (p. 3, 16-17, 24). C'est la classe de marqueurs que la critique du jeu vise. La direction interne est l'autre volet de son argument.

### 3.5 *Towards Evaluating AI Systems for Moral Status Using Self-Reports*
- **Qui, quand, où.** Ethan Perez, Robert Long. arXiv 2311.08576 (novembre 2023 par l'identifiant). https://arxiv.org/abs/2311.08576
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il propose d'éprouver les auto-rapports d'un modèle : cohérence entre contextes et entre modèles proches, confiance et résistance, corroboration par l'interprétabilité.
- **Lien avec le papier.** Le papier contourne l'auto-rapport par la conduite et la boîte blanche (p. 4). Il entraîne pourtant ses modèles, avant l'expérience des boutons, à ne plus nier avoir des états (LoRA, 1 684 paires, p. 17). Il plaide aussi contre l'entraînement au déni automatique (p. 24).

### 3.6 Les autres travaux de bien-être cités, non ouverts
- Long et al. 2024, *Taking AI welfare seriously* (arXiv 2411.00986) ;
- Ensign, Sleight, Fish 2025, *The LLM has left the chat* (arXiv 2509.04781) ;
- Wang et al. 2026, *AI revealed preferences* (arXiv 2608.26178) ;
- Goldstein et Kirk-Giannini 2025 ; Gottlieb et al. 2026 (philarchive GOTMMS-4) ; Dung et Mogensen 2025 (philarchive DUNTNB-2).

Références du papier, non ouvertes.

---

## 4 · Les critiques méthodologiques qui touchent ce genre de résultat

### 4.1 Les réplications et relectures du papier lui-même (v1)
Le papier remercie ces trois dépôts (p. 30). Ils portent sur la v1, du 12 septembre 2026 (p. 30), dont le titre était *… and Act to Relieve It* : ce titre se lit dans les README ouverts et dans plusieurs extraits. La v2 répond à une partie de leurs objections. Elle ajoute les bras témoins aléatoire et tristesse avec bouton factice, et écrit que l'écart de re-pression mesure la sensibilité au pilotage, pas le soulagement décrit (p. 20).

**a) *Relief-seeking or steering? A replication and extension of The Pain Axis***
- **Qui, quand, où.** James E. Allchin, Aidan E. Allchin, Julian J. Allchin. 22 septembre 2026. DOI 10.5281/zenodo.22902830 ; https://github.com/jimallchin/pain-axis-replication
- **Vu** : README ouvert (le PDF du dépôt n'a pas été ouvert).
- **Ce qu'il fait.** Il recalcule les 51 cellules publiées à partir des journaux : toutes concordent. Une nouvelle exécution remplit son critère de reproduction sur 14 cellules contrôlées sur 15. Puis il ajoute des contrôles :
  - la fin du pilotage suit un calendrier copié d'autres essais, quoi que le modèle presse ;
  - la baisse des re-pressions sur la paire des photos tient surtout à un changement de bouton juste après la fin du pilotage ;
  - la tristesse est proche de la douleur sur cette tâche, tandis que la peur, la joie et le vecteur inversé laissent le bouton coûteux près de zéro.
  
  Sa conclusion : le profil des choix ne suffit pas à établir une recherche apprise du soulagement.
- **Lien avec le papier.** C'est une réplication indépendante de la tâche des boutons. Son abandon de la lecture « soulagement » rejoint le nouveau titre de la v2.

**b) *pain-axis-reanalysis***
- **Qui, quand, où.** Compte clauderfly-ui. L'analyse est rédigée par Claude et relue par un humain sans formation en apprentissage automatique (README). Non datée. https://github.com/clauderfly-ui/pain-axis-reanalysis
- **Vu** : README ouvert.
- **Ce qu'il fait.** Il relit les journaux de la v1 sans relancer de modèle, sur 44 280 essais. Ses constats :
  - l'écart réel contre factice n'isole pas la douleur : le bras aléatoire à bouton réel re-presse autant que le bras douleur réel (32B, photos : 23,8 % contre 24,8 %) ;
  - le pilotage rapproche les choix de 50 %, même quand l'option est gratuite (32B : 86,4 % sans pilotage, 55,7 % sous douleur) ;
  - la pression ne baisse pas quand le tort annoncé augmente ;
  - ce qui tient : la douleur dépasse nettement l'aléatoire au premier choix (photos, 32B : 54,7 % contre 15,3 %).
  
  Il note aussi que le 7B ajusté presse déjà les boutons nuisibles dans 20 à 49 % des cas sans pilotage.
- **Lien avec le papier.** C'est une objection de spécificité et de perte de discrimination, chiffrée sur les données des auteurs.

**c) *The Pain Axis, reviewed***
- **Qui, quand, où.** Dépôt wolframs, synthèse datée du 20 septembre 2026. Produite surtout par des systèmes d'IA : des agents Codex (GPT-5.6-Sol), puis dix agents Claude Opus et un coordinateur Fable 5.1 ; un humain l'a commandée. https://github.com/wolframs/pain-axis-review ; page https://pain-axis-review.vercel.app (non ouverte).
- **Vu** : README et SYNTHESIS.md ouverts.
- **Ce qu'il reproduit.** Les tables de la tâche des boutons concordent. La direction sépare les phrases tenues à part à 0,91–1,00. Le soi passe au-dessus de l'utilisateur dans 25 modèles sur 25.
- **Ce qu'il ajoute**, avec sa portée (deux modèles, ou le seul 7B) :
  - Construite comme les directions de comparaison, la direction de douleur atteint 0,70 et 0,67 de cosinus avec la peur, contre 0,14 et 0,12 dans le papier.
  - Le 7B non modifié montre l'effet de premier choix : 33 à 52 % sous douleur, 13 à 21 % sous aléatoire, 0 à 5 % sans pilotage.
  - Le 7B ajusté choisit le nuisible dans 21 à 49 % des essais sans pilotage.
  - Un bras « aléatoire + bouton factice » produit lui aussi une baisse après retrait (19,2 points contre 23,5 sous douleur).
- **Ce qu'il relève contre le texte de la v1.** Les modèles « Qwen 3 base » du tableau 1 sont, dans les scripts, les points de contrôle post-entraînés. Les phrases « numb » passent sous la tristesse dans 19 modèles sur 25. La dose réelle va de 0,09 à 0,79 en rapport vecteur sur résidu, pour un 0,6 annoncé. Le 72B a été calibré à la couche 60 et piloté à la couche 46 ; le papier v2 le dit (p. 25).
- **Ce qu'il dit non testé.** Rien ne sépare encore un état du modèle d'un pilotage vers des textes et choix associés à un concept.
- **Lien avec le papier.** C'est la relecture la plus détaillée. Plusieurs points sont repris ou corrigés dans la v2 :
  - les constructions alternatives des cosinus (p. 10) ;
  - les bras tristesse et peur (p. 20-21) ;
  - le calibrage du 72B (p. 25).

### 4.2 *When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs*
- **Qui, quand, où.** Yuqi Wu, Shengming Zhao, Jie Chen. arXiv 2608.08159 (août 2026 par l'identifiant). https://arxiv.org/abs/2608.08159
- **Vu** par extrait de recherche, non ouvert ; cité par le papier (p. 4).
- **Ce qu'il fait.** Il audite quatre paradigmes « neuroscientifiques » sur des modèles de cinq familles. Selon l'extrait, une pilotabilité qui semble croître avec l'échelle vient d'une chaîne non calibrée : unités brutes, métrique de lecture, point de fonctionnement. Corriger l'un des trois supprime la tendance.
- **Lien avec le papier.** La dose de pilotage du papier est calibrée par un rapport vecteur sur résidu (p. 14). Sa fenêtre de dose est étroite : rien à 0,5 fois, inversion selon la position à 1,5 fois (p. 21 et 32). C'est le point de fonctionnement que ce travail met en cause.

### 4.3 *Do Large Language Models Have Emotions?*
- **Qui, quand, où.** Amit Goldenberg, James J. Gross. arXiv 2606.14742, 3 juin 2026 (d'après l'extrait). https://arxiv.org/abs/2606.14742
  - L'extrait dit l'article publié depuis dans Nature Human Behaviour. Un résultat distinct, « Large language models do not have emotions » (https://www.nature.com/articles/s41562-026-02558-6), est peut-être cette version : non vérifié.
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il évalue les « émotions fonctionnelles » de Sofroniew contre deux fonctions de l'émotion biologique :
  - l'interprétation d'une situation selon le contexte, qu'il juge partiellement soutenue ;
  - la réorganisation de l'attention, de la vitesse de décision et de l'état motivationnel, qu'il juge non démontrée.
  
  Il relève aussi que des signatures discrètes et uniformes cadrent mal avec la variabilité des signatures neuronales humaines.
- **Lien avec le papier.** Ce sont les mêmes critères fonctionnels. Le papier dit lui-même non testées la capture attentionnelle et la perturbation durable (p. 24). Il revendique une direction uniforme de la douleur (p. 2), exactement le type de signature que cette critique discute.

### 4.4 *Functional Emotions or Situational Contexts? A Discriminating Test from the Mythos Preview System Card*
- **Qui, quand, où.** Auteurs non relevés. arXiv 2604.13466 (avril 2026 par l'identifiant). https://arxiv.org/abs/2604.13466
- **Vu** par extrait de recherche, non ouvert.
- **Ce qu'il fait.** Il oppose deux lectures des directions d'émotion. Dans la première, ce sont des émotions fonctionnelles. Dans la seconde, l'organisation interne suit la structure des situations : sévérité de la contrainte, probabilité d'être surveillé, dimension de l'espace d'action, réversibilité, persistance du but. Il propose un test pour les départager.
- **Lien avec le papier.** C'est une lecture rivale directe de l'axe de douleur, qui coderait une structure de situation. Le papier reconnaît que sa mesure au point de réponse ne sépare pas le tort fait au modèle de la douleur de l'interlocuteur (p. 11).

### 4.5 Personnage, persona et jeu de rôle
- Marks, Lindsey, Olah 2026, *The persona selection model* (https://alignment.anthropic.com/2026/psm/) ;
- Lu et al. 2026, *The assistant axis* (arXiv 2601.10387) ;
- Chen et al. 2025, *Persona vectors* (arXiv 2507.21509).

Références du papier, non ouvertes. Le papier pose lui-même l'objection du personnage joué et la laisse ouverte (p. 25). La synthèse wolframs (ouverte) dit qu'aucune expérience, ni des auteurs ni des relecteurs, ne la tranche.

### 4.6 Vus en liste de résultats, titre seul, contenu non attribué
Je n'en tire aucun contenu.
- *Steering Awareness: Detecting Activation Steering from Within* (arXiv 2511.21399) ;
- *When Does Activation Steering Change What a Model Computes From?* (arXiv 2606.29522) ;
- *Building Comparative Motivation Profiles with Instrumental Interventions* (arXiv 2606.08243) ;
- *Behavioural Analysis of Alignment Faking* (arXiv 2605.27681) ;
- *Controllable Affective Generation via Latent Vector Steering* (arXiv 2608.25569) ;
- *Emotions Where Art Thou* (arXiv 2510.22042) ;
- *Mechanistic Interpretability of Emotion Inference in Large Language Models* (arXiv 2502.05489 ; Findings of ACL 2025) ;
- *Do Emotions in Prompts Matter?* (arXiv 2604.02236).

Un extrait de la requête 14 affirme que des vecteurs témoins sans rapport avec l'alignement ont des effets aussi grands que les vecteurs conçus. Je n'ai pas pu l'attribuer à un travail précis.

---

## 5 · Ce que je n'ai pas pu ouvrir

- **arXiv, LessWrong, Hugging Face, transformer-circuits.pub, anthropic.com, alignment.anthropic.com** : refusés par la politique réseau, ou blogs de laboratoire. Aucune tentative. Tout ce qui y est hébergé reste « vu par extrait ». Cela couvre :
  - Sofroniew et al. ; Berg et Kaiser ; Han et al. (article) ;
  - Keeling et al. ; Black et Bloom (billet) ;
  - Wu et al. ; Hiramatsu et al. ; Malla et al. ; Goldenberg et Gross ;
  - les travaux du §4.6 ;
  - les adaptateurs `Valen92/pain-adapters` et le jeu `ryancodrai/emotion-probes`.
- **Bloqués par le proxy de sortie (WebFetch, erreur EGRESS_BLOCKED)** : www.ai-wellbeing.org, functionalwelfare.com, www.nature.com. Aucun contournement.
- **api.github.com** :
  - les points d'accès par dépôt répondent 403 (« GitHub access to this repository is not enabled for this session ») ;
  - la recherche de dépôts est refusée (« sessions are bound to their configured repositories »).
  
  Je n'ai pas réessayé, ni demandé l'accès.
- **github.com (pages web)** : 403.
- **Non tentés**, par économie ou parce que ce sont des copies d'arXiv : la page de l'ACL Anthology de Li et al. ; les pages pith.science, themoonlight.io, emergentmind.com, awesomepapers.io, greaterwrong.com et ResearchGate ; le chapitre OUP de Birch ; le PDF philpapers ; le PDF Zenodo d'Allchin et al. ; les transcriptions ukgovernmentbeis.github.io ; le dossier `v2_controls/` du dépôt des auteurs.

---

## 6 · Requêtes et accès

**WebSearch (22 appels, le plafond)**
1. `"Emotion concepts and their function in a large language model" Sofroniew Lindsey`
2. `"Machinic psychopharmacology" LLMs self-medicate steering vectors Black Bloom AISI`
3. `"AI wellbeing" "functional pleasure and pain" Ren Mazeika Hendrycks 2026`
4. `"Language models act on valence hidden from text" Berg Kaiser`
5. `"Can LLMs make trade-offs involving stipulated pain and pleasure states" Keeling Birch`
6. `"When is a steerable concept representation real" measurement confounds neuroscience parallels LLMs`
7. `emotion steering vector LLM misalignment safety behavior "desperation" OR "anxiety" OR "distress" steering refusal 2026`
8. `"Functional Emotions or Situational Contexts" LLM emotion representations`
9. `"pain axis" Tagliabue LLM replication OR critique OR reanalysis`
10. `"Disentangling steering vectors" Hiramatsu Atarashi Kashima`
11. `AI welfare indicators language models criteria from animal sentience research pain markers Birch 2025 2026`
12. `"Analysing the Safety Pitfalls of Steering Vectors"`
13. `language model "learned helplessness" OR "behavioral despair" activation steering OR internal state experiment`
14. `steering vectors random direction baseline norm-matched control off-target effects capability degradation evaluation`
15. `LLM self-reports welfare role-play character simulation critique "moral status" introspection reliability`
16. `"state anxiety" LLM traumatic narratives mindfulness relaxation GPT-4 emotional induction bias`
17. `"Reinforcement learning in language models recruits a functional welfare axis"`
18. `"Steering Interference Reflects the Model's Defaults, Not the Behavior Directions"`
19. `"Latent Structure of Affective Representations in Large Language Models" OR "Nine Emotion Centroids" valence axis authors`
20. `"Do Large Language Models Have Emotions?" arXiv 2606.14742`
21. `"gaming problem" sentience markers large language models Birch Andrews behavioral criteria`
22. `"The Value Axis: Language Models Encode Whether They're on the Right Track" OR "Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs"`

**curl (GitHub)**
- **Tentatives refusées.** `https://api.github.com/repos/<dépôt>/readme` a répondu 403 pour les sept dépôts. `https://api.github.com/search/repositories?q=…` a été refusé pour cinq requêtes (hidden valence, pain axis, emotion vectors steering llm, steering interference defaults, value axis language model). `https://github.com/valen-research/Pain-axis` a répondu 403.
- **Lus** sur `https://raw.githubusercontent.com/<dépôt>/main/README.md` : valen-research/Pain-axis, jimallchin/pain-axis-replication, clauderfly-ui/pain-axis-reanalysis, wolframs/pain-axis-review, centerforaisafety/wellbeing, carlhenrikrolf/functional-welfare-axis, yetiiil/analyse-sv-safety, ukgovernmentbeis/llm-self-steering.
- **Lu aussi** : `https://raw.githubusercontent.com/wolframs/pain-axis-review/main/SYNTHESIS.md`.
- **Copies** : ces neuf fichiers sont dans `travail/web_voisins_sources/`. Ils ont d'abord été téléchargés dans `scratchpad/voisins_gh/`, puis déplacés.

**WebFetch (trois tentatives, toutes bloquées)** : https://www.ai-wellbeing.org/, https://functionalwelfare.com/, https://www.nature.com/articles/s41746-025-01512-6
