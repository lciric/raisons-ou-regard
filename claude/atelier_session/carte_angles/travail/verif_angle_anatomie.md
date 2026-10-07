# Vérification — angle : l'anatomie de ce que les raisons installent

**Fichier vérifié.** `travail/angle_anatomie.md` (614 lignes, 2 octobre, 9 h 00). Les numéros de ligne ci-dessous renvoient à ce fichier, sauf mention d'une pièce.

**Ce que j'ai relu moi-même.**
- Rapport 5 en entier (rapports du 2 octobre, l. 1012-1254).
- Rapport 3 en entier (l. 486-726), rapport 2 en entier (l. 271-485), rapport 6 en entier (l. 1255-1573), rapport 7 en entier (l. 1574-1850) ; dans le rapport 1, l. 130-170 ; dans le rapport 4, l. 920-960.
- Les quatre rapports du 1er octobre en entier.
- Passation v1.2, §1 à §7 ; consignes de la nuit, en-tête et niveaux de danger (l. 1-67) ; programme v1.1, partie 1 (l. 51-133) et la phase de l'anatomie (l. 467-502, 617-635) ; complément de l'architecte ; fiche du papier sur l'espace de travail (fiches de lecture, l. 377-455).
- Web : 8 recherches WebSearch (extraits seulement) et une lecture par curl sur raw.githubusercontent.com (le README du dépôt public d'*Inoculate or Reflect?*). Ce README n'a aucun des libellés de la consigne : je le désigne ici « lu sur la source par le vérificateur, non relu par l'instance du papier ». La carte ne doit rien en tirer comme établi avant relecture par l'instance.

**Ce qui tient.** Le verdict d'ensemble (partiellement pris ; élevé pour la présence des concepts avant la décision et pour leur nécessité ; le reste libre) suit le §4.4, n° 8 et le rapport 5. Les chiffres de la §7 suivent le §4.2, n° 2. Les chiffres de Zhou, Vaid, Meier, Mazaheri, Ri, Billa, Drake et Eberstadt suivent le rapport 5 ; celui de Nakamura suit le rapport 3 ; les points de contrôle de Cho suivent le §4.3. Aucune erreur corrigée au §4.3 n'est reprise (Heidari, 2502.04040, Cho sont traités juste). Les dates de SPAR et d'ICLR 2027 suivent le §4.4 et le rapport 6 (l. 1450, 1506). Aucune idée n'est désignée par un sigle ; aucun « first » ; les citations font moins de quinze mots ; aucun chiffre n'est tiré d'un extrait. Mes recherches retrouvent les extraits annoncés pour Imran et Shaikh, pour Zeisler (autrice, date, modèles, conclusion), pour les trois lentilles de Hugging Face (anicka, bcywinski, stanleytheli) et l'écart sur le nombre de modèles de Neuronpedia (vu par extrait de recherche, non ouvert). La carte ne propose aucun contact avec Cadile ni Lundqvist : c'est conforme à la décision de Lazar (« pas encore »).

---

## 1. Corrections bloquantes

### 1.1 *Inoculate or Reflect?* : « le flux résiduel entier » n'a pas de source, et la méthode de suffisance est surévaluée
- **Où.** L. 41 (« patch du flux résiduel entier »), l. 122 (« Il prend la méthode de la suffisance »), l. 126, l. 454, l. 502 (formulation « to our knowledge » n° 1).
- **Ce que dit la source.** Le rapport 5 (l. 1053) écrit seulement : un patching du flux résiduel du modèle contaminé vers le modèle réparé, à trois couches médianes. Le mot « entier » n'y est pas. Le rapport 5 n'a lu le billet que par deux résumés de l'outil (l. 1050).
- **Ce que montre le README du dépôt** (lu sur la source par le vérificateur, non relu par l'instance du papier ; `raw.githubusercontent.com/Ayesha-Imr/inoculate-or-reflect/main/README.md`) :
  - le patch interpole l'état résiduel du modèle contaminé dans chaque modèle réparé ;
  - les auteurs le présentent comme un contrôle revenu nul, faible et non sélectif ; un donneur mélangé fait autant ; ils écrivent ne pas l'utiliser comme preuve causale ;
  - le sens du patch est « contaminé vers réparé », et le modèle réparé par réflexion part de l'adaptateur contaminé.
- **Correction exigée.**
  - Retirer « entier » partout, ou le sourcer après relecture du billet par l'instance.
  - L. 122 : remplacer « Il prend la méthode de la suffisance » par une phrase sourcée au rapport 5 (« patching du flux résiduel du modèle contaminé vers le modèle réparé ») ; ajouter, après relecture seulement, que ce patch y sert de contrôle et revient nul.
  - Formulation n° 1 : citer Imran et Shaikh sans « entier » ; la formulation reste tenable, et le README la renforce, mais elle doit être marquée « à relire avant le dépôt ».
- **À ajouter au même endroit, à vérifier** : le README présente le travail comme une étude de la piste reproductibilité de BlackboxNLP 2026 (« reproducibility-track study for BlackboxNLP 2026 »). Aucun rapport ne le dit. Le lieu (l. 108) et le tableau des projets (l. 481) doivent le signaler comme non relu, sans date.

### 1.2 Le niveau du papier sur l'espace de travail se contredit lui-même
- **Où.** Titre de l'entrée, l. 58 : « moyen pour le reste ». Corps, l. 86-87 : moyen pour la résidence et la charge, puis « Rien sur le reste ».
- **Source.** Rapport 5, l. 1036 : « Moyen pour le reste de l'angle » ; l. 1035 : le papier touche « en bord, la charge et le persona ».
- **Correction exigée.** Un seul niveau par sous-question, identique dans le titre et le corps, et dire en quoi la carte s'écarte du rapport 5. Proposition conforme aux définitions des consignes (l. 46-50) : élevé pour la présence et la nécessité ; moyen pour la résidence dans l'espace de travail et pour la charge ; faible pour le caractère (touché en bord selon le rapport 5) ; aucun pour la suffisance, la spécificité par famille et la raison imposée.

### 1.3 Une phrase attribuée à la v1.1 n'y figure pas
- **Où.** L. 519 : « « Aucun travail ne teste causalement les concepts des raisons après un entraînement par raisons. » C'est la phrase de la v1.1, partie 1. »
- **Source.** Programme v1.1, l. 124 : « Nous n'avons vu aucun travail qui teste causalement les concepts des raisons […], ni leur charge dans le workspace », suivi de « cette absence n'a pas été cherchée en propre ».
- **Correction exigée.** Citer exactement, ou paraphraser sans guillemets. Dire que la v1.1 réservait déjà cette absence, et que c'est la §7 (relue, §4.2, n° 2) qui la rend intenable. La seconde moitié (« ni leur charge dans le workspace ») n'est pas démentie par les rapports pour des concepts installés par des raisons : le dire.

### 1.4 La contradiction n° 6 n'est pas établie
- **Où.** L. 566-569 : le chiffre de contrarianisme du rapport 5 « ne concorde pas » avec l'extrait de la carte, qui « développe aussi les deux noms de méthode d'une façon qui semble fautive ».
- **Ce que j'ai trouvé.**
  - Un second extrait (vu par extrait de recherche, non ouvert) donne un chiffre de contrarianisme compatible avec le rapport 5 (l. 1054, « environ 54 % »), et développe les deux noms comme Inoculation Prompting et Counterfactual Reflection Training.
  - Le README (lu sur la source par le vérificateur, non relu par l'instance) imprime le même chiffre et les mêmes noms.
- **Correction exigée.** Ne pas présenter le rapport 5 comme contredit. Écrire : chiffre non retenu, faute de lecture par l'instance ; un extrait a divergé, un autre extrait et le README du dépôt concordent avec le rapport 5 ; relecture à faire (elle est facile : le dépôt répond par curl).

---

## 2. Corrections non bloquantes

### 2.1 La note sur la v1.3 lit mal le complément
- **Où.** L. 535-540 : la v1.3 « a ajouté à l'anatomie les contrôles qui manquent à la §7 ».
- **Sources.** Complément, l. 58 : à la question « Dans la v1.3 ? », la réponse est « Oui ». Complément, l. 32-34 : aucune ligne de la v1.1 n'est retirée ni changée. Programme v1.1, l. 473-492 : la phase de l'anatomie contient déjà l'organisme à concept planté, le balayage de rang contre les sous-espaces aléatoires de même rang et les directions sensibles sans rapport, et la dégradation appariée.
- **Correction.** « La v1.3 contient, depuis la v1.1, les contrôles qui manquent à la §7. »

### 2.2 Des numéros de section viennent des fiches, pas du rapport 5
- **Où.** L. 68 et l. 600 (« le §6 »), l. 601 (« la §9.1 »).
- **Source.** Le rapport 5 (l. 1026, 1034) nomme des parties (« le point de vue de l'Assistant », « les limites ») sans numéro. Les numéros viennent des fiches de lecture (l. 377 : « 9.1 *Limitations* » ; l. 383 : « §6 : la J-space acquiert le point de vue de l'Assistant au post-entraînement »), écrites d'après la base de connaissances, non relues.
- **Correction.** Sourcer ces numéros aux fiches, et ajouter les fiches à la liste des sources (l. 5-8) : la carte s'en sert aussi à la l. 556.

### 2.3 Des statuts de lecture manquent ou sortent de la liste
- L. 44 et l. 48 : « rapport 5 » seul. Donner le statut par travail : Anthropic sur la charge, rapport 5, texte intégral ; Billa, Vaid, Sinha, rapport 5, résumé seul ; Mazaheri, rapport 5, texte intégral ; Heidari, rapports 2 et 6, texte intégral.
- L. 80 : « (rapport 5) » devient « rapport 5, texte intégral » (l. 1026).
- L. 98 : « (rapports 2 et 5) » devient « rapport 2, texte intégral (l. 312) ; rapport 5, texte intégral ». La fiche du papier donne les mêmes chiffres (l. 420-421).
- L. 241 : *Persona Vectors* est marqué « Rapport 5, résumé seul », mais le rapport 5 (l. 1139) écrit seulement « Confirmé », sans mode de lecture. Écrire « rapport 5, mode de lecture non précisé » ; le rapport 3 (l. 634) ne dit pas non plus comment il l'a lu.
- L. 294 : *Constitutional Value Potentials* a aussi été lu en PDF par le rapport du 1er octobre, axe raisons contre actions (l. 94), avec des contrôles aléatoires orthogonaux : « texte intégral ».
- L. 410 : Lowet et Kurzeja deviennent « rapport 7, résumé seul, par sites tiers » (l. 1681), plutôt que « lu par un site tiers ».
- L. 482 (« Rapport 5, non relu »), l. 485-488 (« Rapport 5 »), l. 493 (« Rapport 6, non relu ») : « non relu » n'est pas un libellé. Le rapport 5 ne dit pas comment il a vu ces dépôts : écrire « rapport 5, mode de lecture non précisé ». Les dates d'ICLR 2027 : rapport 6, « date limite vérifiée » (l. 1506).

### 2.4 Une date incompatible avec son identifiant
- **Où.** L. 334 : Sinha et coll., « arXiv 2606.09850, le 9 mai 2026 ». C'est repris du rapport 5 (l. 1145).
- **Pourquoi.** Un identifiant en 2606 désigne un dépôt de juin 2026 ; la v1 ne peut pas dater du 9 mai. La carte use elle-même de cette règle (l. 419).
- **Correction.** « Date à vérifier : incompatible avec l'identifiant. » Même prudence si l'on reprend la date du rapport 3 pour *Routing Subspaces* (« version 1 du 11 mai 2026 » pour 2607.20436, l. 539) ; la carte ne la donne pas, et elle doit continuer de ne pas la donner.

### 2.5 Une contradiction manque : le dernier auteur de *Routing Subspaces*
- Les rapports 2 (l. 350) et 3 (l. 539) disent Konrad … Ayvaz ; le rapport du 1er octobre, axe de la combinaison exacte (l. 383), dit Konrad … Tanyel. La carte écrit Ayvaz (l. 321) sans signaler l'écart. À ajouter aux contradictions, avec relecture.

### 2.6 La contradiction n° 4 attribue au rapport du 1er octobre un numéro de section qu'il ne donne pas
- **Où.** L. 558-561.
- **Source.** Rapport du 1er octobre, axe de la combinaison exacte, l. 408 : des perturbations témoins de même norme, sans numéro de section. La section 5 vient du rapport 2 (l. 312, « §5.1 ») et de la fiche (l. 419).
- **Correction.** Citer ces deux sources pour le numéro. Le fond du point (ne pas étendre à la §7 les contrôles de la §5) est juste.

### 2.7 Les corrections à la v1.1 sont incomplètes
- « Memarian » figure aussi dans la partie 3 de la v1.1 (l. 241, l'option OLMo) et dans les menaces (l. 687), pas seulement dans la partie 1 (l. 92, 121).
- « Montré que sur Claude » figure aussi dans la partie 1 (l. 122), et dans la passation v1.2, §5.2 (l. 320), qui est une proposition faite à Lazar : à corriger aussi.

### 2.8 Le cadre rival : la liste du tableau s'écarte du rapport 5 sans le dire
- **Où.** L. 46.
- **Source.** Rapport 5, l. 1214 : Marks et coll., Lu et coll., Imran et Shaikh. La carte remplace Imran et Shaikh par Chen et coll. et Del Pinal et coll.
- **Correction.** Rétablir Imran et Shaikh, ou dire pourquoi on les retire. Ajouter Betley et coll., que le rapport 6 (l. 1355) range dans l'anatomie (« axe de persona »).

### 2.9 Des guillemets sur une paraphrase
- L. 480 : « première étape » est une paraphrase du rapport 5 (l. 1185), tirée d'un « résumé de l'outil ». Retirer les guillemets.

### 2.10 La section 16 peut être complétée par extrait
Ces informations sont vues par extrait de recherche, non ouvert.
- 2610.00320 : auteurs Jungseob Lee … Heuiseok Lim, code public. L'extrait parle de retirer les premières directions singulières de la mise à jour, entre autres sur Llama-3.1-8B. Cela touche le balayage de rang : danger faible, à garder.
- 2610.02098 : auteurs Chuqin Geng … Xujie Si, déposé le 1er octobre 2026.

### 2.11 La résidence : une formulation intenable manque
- La §7 lit les concepts éthiques dans l'espace de travail, par le J-lens, et ablate des vecteurs de lentille (relu, §4.2, n° 2).
- La liste « Qui ne le sont plus » (l. 517-533) doit donc ajouter : aucun « to our knowledge » sur la présence, dans l'espace de travail, de concepts installés par un entraînement par principes.
- Restent libres la version sur modèles ouverts et l'échange entre la part de l'espace de travail et son complément.

### 2.12 Nakamura : rappeler la cote du rapport 3
- Le rapport 3 le cote moyen pour le principe localisé (« quasiment la méthode du programme », l. 573). La carte le met en faible pour l'anatomie (l. 312) : c'est défendable, mais il faut le dire.
- Elle omet un résultat du même rapport, utile au balayage de rang : « Le rang qui fait s'effondrer le refus dépend de la famille » (l. 571).

---

## 3. Les manques

### 3.1 *Stress Testing Deliberative Alignment*, pour la raison imposée (le plus important)
- Relu sur la source par l'instance du papier (§4.2, n° 6). Les interventions sur la chaîne de pensée portent sur o3 avant l'entraînement anti-manigance, et cela « does not inform us whether anti-scheming training changes this causal relationship ».
- C'est le voisin le plus direct de « l'action suit-elle une raison imposée, après un entraînement par raisons ». Il fonde la partie « libre » de cette sous-question.
- À ajouter au tableau (l. 45), à la mesure n° 6 (l. 463-465) et à côté de la formulation n° 4 (l. 508-509). Voir aussi le rapport 2 (l. 301) et le rapport 6 (l. 1296).

### 3.2 Drake et Eberstadt, pour la suffisance
- Le rapport 5 (l. 1209) les range parmi les méthodes de suffisance existantes : une direction de persona transplantée entre modèles qui ne partagent que le pré-entraînement (l. 1140).
- La carte les cite comme précédent du transplant (l. 246), mais les omet dans le tableau (l. 41) et à côté de la formulation n° 1 (l. 502).

### 3.3 Des travaux des rapports qui touchent l'anatomie et manquent à la carte (tous faibles pour cet angle)
- **Nadaf, 2607.21356.** Rapport 3, texte intégral (l. 578-588) ; rapport du 1er octobre, axe du test causal interne (l. 253-258).
  - Un sous-espace de persona de rang 4 est projeté hors du flux pendant le fine-tuning, contre un sous-espace aléatoire de même rang.
  - Cela touche les concepts contre le caractère, et le rang. La v1.1 le cite déjà (partie 1, l. 89).
- **Shah, Brinkmann, Angell, 2605.28467.** Rapport du 1er octobre, axe du test causal interne, lu par un site tiers (alphaXiv, l. 296-301).
  - Une direction unique installée par l'entraînement : l'ajouter induit le refus, la retirer rétablit la conformité.
  - C'est nécessité et suffisance d'une direction, sans contrôle aléatoire rapporté.
- **Gupta et Gupta, 2609.00925.** Rapport 3 (l. 645) : soustraire la direction du modèle de départ supprime les gains de SFT et de DPO.
- **Jain et coll.**, *What Makes and Breaks Safety Fine-tuning?*
  - Rapport du 1er octobre, axe du test causal interne (l. 317-321) : le fine-tuning de sûreté apprend une transformation minimale des MLP.
  - Le rapport 3 (l. 659) n'a pas pu vérifier la publication à NeurIPS 2024.
- **Pathmanathan et Huang, 2604.09665.** Rapport 7, texte intégral (HTML v2, l. 1694-1712) ; rapport du 1er octobre, axe raisons contre actions, lu par un site tiers (l. 49-53).
  - Alignement délibératif distillé, avec une attribution dans l'espace latent.
- **Irpan et coll., 2510.27062.** Rapport du 1er octobre, axe du test causal interne, lu par un site tiers (l. 303-308).
  - Deux entraînements de cohérence modifient le modèle par des voies mécanistes distinctes.
- **Pour le diffing** : 2504.02922 (crosscoders et chat-tuning ; rapport 5, l. 1175 ; rapport du 1er octobre, l. 325).
- **Pour la charge et le rang** :
  - 2609.06934, *The Geometry of Refusal: Why Post-Hoc Safety Is Fragile…* (rapport 5, l. 1177) ;
  - 2602.06801, *On the Non-Identifiability of Steering Vectors* (rapport du 1er octobre, l. 335).
- **Li … Hu, 2609.04022.** Rapport 6, résumé seul (l. 1416-1419) : aligner les représentations plutôt que les réponses.
- **Lowet et Kurzeja.** Rapport 7, résumé seul (l. 1690) : un objet entraîné sur la base se transfère tel quel à la version post-entraînée. C'est un transfert entre modèles de même base, voisin de la suffisance.

### 3.4 Une preuve négative à verser au « pourquoi libre »
- Rapport 5, l. 1182 : Semantic Scholar recense 72 citations entrantes du papier sur l'espace de travail, et aucune ne dissèque des concepts installés par des raisons.
- Rapport 2, l. 448 : titres seuls.

### 3.5 Des projets et des annonces qui manquent au tableau
- Rapport 5 (l. 1192-1193) : jeeva2812, examen critique du J-lens ; AnonymousInterpScience, artefacts d'un papier anonyme sur la dépendance du J-lens au corpus. Ce dernier touche directement la porte du lens.
- Rapport 3 (l. 671) : Konrad et coll. annoncent des sondes de rang supérieur.
- Rapport 6 (l. 1482-1486) : le flux MATS de Cozmin Ududec suit la conduite et les représentations internes à travers SFT, RL et entraînement de sûreté. Danger moyen à faible selon le rapport, pour d'autres angles.
- Rapport 6 (l. 1499) : Betley et coll. annoncent d'autres pôles de correction et des modèles plus grands.
- La piste BlackboxNLP 2026 d'Imran et Shaikh (voir 1.1), à vérifier.

### 3.6 À ajouter à « ce qu'il faut relire »
- Le README et le dépôt d'*Inoculate or Reflect?* : ils sont lisibles par curl sur raw.githubusercontent.com. Cela tranche les points 1.1 et 1.4 sans passer par LessWrong.
- La date de Sinha et coll. (2.4), et le dernier auteur de *Routing Subspaces* (2.5).
