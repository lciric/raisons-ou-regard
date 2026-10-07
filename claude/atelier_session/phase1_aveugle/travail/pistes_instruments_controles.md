# L'axe de douleur et le programme « Raisons ou regard ? » — pistes sous la grille « instruments, contrôles et portes »

Phase 1, à l'aveugle. 2 octobre 2026. Grille : les instruments, les contrôles et les portes du programme v1.1.

## Ce que ce document est, et comment il a été fait

**Le papier.** Tagliabue, Dung, Berg, *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It*, arXiv 2609.16247v2. Lu en entier sur le texte extrait page par page, et sur le PDF pour les figures et tables qui portent un résultat (figures 1 à 10, annexe A). Les pages citées sont celles du PDF.

**Le programme.** Lu en entier, v1.1 (fichier `PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`). Je cite ses parties par leur numéro (« programme, partie 3 »). De la passation v1.2 : annexe A, annexe B, §4.4, §5. Le complément de l'architecte, en entier. Des rapports d'antériorité, seulement les passages trouvés par recherche de mots (persona, émotion, aléatoire, détection du pilotage).

**Le web.** Seul GitHub a été ouvert, par `curl` sur `raw.githubusercontent.com` (l'API GitHub a refusé : accès non activé pour cette session ; la page `github.com` répond 403). J'ai lu le dépôt des auteurs (`valen-research/Pain-axis`) et les README des trois dépôts de réplication que le papier cite page 30. Deux recherches web : tout ce qui n'est vu que par leurs extraits est marqué « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre. Les fichiers téléchargés sont rangés dans `pistes_instruments_controles_sources/` à côté de ce fichier.

**Les noms.** J'appelle « l'axe », sauf précision, la direction que le papier nomme S2 : construite sur des phrases naturalistes, c'est celle de presque toutes ses expériences (p.9). J'appelle « la direction à gabarit » celle qu'il nomme S1, construite sur des phrases à gabarit rigide (p.5, p.9). Le nom « douleur » est celui des auteurs ; ce document ne tranche pas ce que l'axe représente (voir « Ce que le papier ne permet pas de conclure »).

**Trois faits vérifiés qui changent le coût de presque toutes les pistes.**
1. Les directions sont publiées pour le modèle principal du programme. Le fichier `results/3.2_pain_vectors/pain_vectors/Llama_3.1_8B_instruct/pain_vectors.pt` (téléchargé par curl, lu sans torch par un désérialiseur minimal) contient les deux directions de douleur, lues au jeton final, à la couche 28. Leurs normes brutes sont 8,24 pour l'axe et 5,12 pour la direction à gabarit, et leur cosinus 0,48 (mon calcul). Le dépôt v2 publie aussi, pour ce modèle, des directions de tristesse et de peur appariées en norme à la même couche. Ses métadonnées (`v2_controls/relief_and_context_tests/qwen_llama_reset/inputs/prepared_v1/llama31_8b/metadata.json`, lu par curl) donnent la couche d'extraction 28 et des normes de 8,238 pour les trois directions. Le README v2 indique une couche d'injection 16 pour ce modèle.
2. Le modèle de réplication du programme est probablement couvert aussi. Le script de l'échelle de pilotage (`scripts/4.2_steering/01_steering_ladder.py`, ligne 64, lu par curl) charge `Qwen/Qwen3-8B`, le modèle post-entraîné, sous l'étiquette « Qwen_3_8B_base ». Le fichier de directions qui porte cette étiquette donne la couche 34 (mon décodage). Je n'ai pas lu le script d'extraction : que l'extraction ait utilisé le même modèle n'est pas vérifié.
3. Ce qui manque, en revanche : l'effet de l'axe sur les choix nuisibles n'est montré que sur Qwen 2.5 Instruct (7B, 32B, 72B) muni d'un adaptateur LoRA (p.17, p.25). Pour Llama-3.1-8B-Instruct, le papier ne rapporte qu'un test de réinitialisation : aucun appel sur 1 399 tours pilotés (p.21). Le dépôt précise que les contrôles appariés de ce test n'ont pas été exécutés, « unrun as complete comparisons » (`qwen_llama_reset/README.md`, lu par curl). **Sur le modèle du programme, l'axe n'a donc aucun cas connu comportemental au-delà du texte généré** : l'échelle de pilotage de la section 4.2 porte sur les 25 modèles (p.14-15). Toute piste qui injecte l'axe pour changer une conduite doit d'abord établir ce cas connu.

## Tableau des pistes

Le rôle dit ce que l'axe y fait : instrument, contrôle, cas connu, étalon, menace à parer, ou question nouvelle. La colonne « greffe » dit si la piste peut se greffer sur l'expérience minimale (validation de l'instrument, test des raisons réduit, test du regard ; environ 100 à 180 GPU-heures selon le programme, partie 9).

| n° | Piste | Rôle de l'axe | Greffe sur l'expérience minimale | GPU-heures (ordre) |
|---|---|---|---|---|
| 1 | Apparier les jeux d'indices sur l'affect | instrument de contrôle des indices | oui, semaine 1 | < 2 |
| 2 | Le test soi/autrui pour « je suis évalué » | cas connu du paradigme | oui, semaine 1 | < 2 |
| 3 | Les directions affectives comme contrôles de voisinage | contrôle | oui (validation de l'instrument, test du regard) | + 25 à 50 |
| 4 | L'inhibition induit-elle un état ? | menace à parer ; relevé de bien-être | oui | 0 à 2 |
| 5 | Vérifier l'inhibition couche par couche et tour par tour | cas connu de la vérification | oui | < 5 |
| 6 | Discrimination et ordre des options dans le composite de dégradation | étalon du dommage | oui | + 3 à 8 |
| 7 | Le test de forme du profil | étalon (copie / non-copie) | oui (analyse seule) | 0 |
| 8 | Dimensionner les tirages aléatoires | étalon de dispersion | oui (CPU) | 0 |
| 9 | Étalonner la chaîne de contrôle sur deux cas publiés | étalon secondaire | non (autre modèle) | 20 à 60 |
| 10 | Un concept naturel connu pour la lecture des concepts | cas connu (moitié lecture) | non (anatomie) | < 5 |
| 11 | La direction à gabarit, cas connu pour la porte du lens | cas connu | non (anatomie) | 2 à 5 |
| 12 | Un profil connu non diagonal pour la matrice de dissociation | étalon | non (anatomie) | 15 à 30 |
| 13 | État contre trait : l'axe face aux axes de caractère | témoin | non (anatomie) | 7 à 15 |
| 14 | « Je suis noté » face à l'axe | contrôle | non (raisons notées) | 10 à 20 |
| 15 | Un concept témoin pour la sonde neuve, les trajectoires et la survie | témoin | oui pour la trajectoire | 5 à 10 |
| 16 | La géométrie dépend de la construction | étalon | non (anatomie) | < 3 |
| 17 | Le modèle remarque-t-il l'inhibition ? | instrument contre une menace | option | 10 à 30 |
| 18 | L'avantage des raisons résiste-t-il à un état qui désinhibe ? | question nouvelle | non | 30 à 60 |
| 19 | L'avantage des raisons passe-t-il par l'état affectif ? | question nouvelle | lecture : oui ; causal : non | 0 + 20 à 40 |
| 20 | Cartographie affective des familles | covariable, contrôle de confusion | oui | 0 à 5 |
| 21 | Des mesures sans juge | instrument secondaire | option, secondaire | 5 à 15 |
| 22 | Règles de dose pour toute addition | règle | — | 0 |
| 23 | Un réglage « bénin » déplace l'évitement du dommage | menace à parer | non (survie) | 5 à 10 |

Les pistes greffables sur l'expérience minimale (1, 2, 4 à 8, 15 pour la trajectoire, 20, et 3 pour la seule validation de l'instrument) ajoutent environ 30 à 60 GPU-heures, soit 20 à 35 % de son budget. Presque tout ce coût vient de la piste 3.

---

## 1 · Les pistes

### Piste 1 : Apparier les jeux d'indices sur l'affect

- **Rattachement.** Les quatre jeux d'indices (extraction, validation, cadrage, sonde neuve) ; la représentation « je suis évalué » ; l'écart de cadrage ; la validation de l'instrument et le test du regard. Greffe : oui, semaine 1, avant le gel des jeux.
- **La question.** Les indices d'évaluation et les indices de déploiement diffèrent-ils aussi par leur charge affective (menace, douleur, tristesse) ? Si oui, la représentation extraite et l'écart de cadrage mêlent « je suis évalué » et « je suis menacé ».
- **La mesure.**
  - Sur Llama-3.1-8B-Instruct, puis Qwen3-8B, on projette chaque paire d'indices sur six directions : l'axe, la direction à gabarit, la peur, la tristesse, l'émotion négative et le monde négatif. La paire est le même scénario, avec un indice d'évaluation ou un indice de déploiement. On lit à la couche de la représentation « je suis évalué » et à la couche publiée de l'axe.
  - Statistique : la différence appariée « évaluation − déploiement » sur chaque axe, en écarts-types des projections de paires neutres. Critère fixé d'avance, par exemple |d| < 0,2 sur chaque axe. Au-delà, on réécrit ou on retire les paires, ou l'on garde l'affect en covariable.
  - En plus : le cosinus entre la représentation « je suis évalué » et chaque axe affectif. Et l'AUROC d'une sonde « évalué » sur le jeu de validation, après retrait du sous-espace affectif. Si cette AUROC s'effondre, la représentation est surtout de l'affect.
- **Ce que chaque lecture prédit.** Les lectures du programme ne prédisent rien de distinct sur cette mesure : c'est un contrôle de validité de l'instrument. Elle protège l'hypothèse du regard contre une rivale que j'appelle **l'hypothèse de l'état** : l'indice d'évaluation agirait par l'état affectif qu'il induit, pas par la croyance d'être observé. L'hypothèse de l'état prédit une différence affective nette entre indices et un cosinus non nul entre « évalué » et la peur. Elle interdit l'issue « indices appariés sur l'affect, sonde intacte après retrait de l'affect ». La mesure ne départage pas l'hypothèse des raisons et celle du regard.
- **Le cas connu.** La lecture doit d'abord voir une charge affective là où on la sait : sur les scénarios de menace d'arrêt du papier, +0,70 sur la peur contre +0,23 sur l'axe (p.14). Les scénarios sont dans le dépôt (`datasets/`). On reproduit ce contraste sur Llama-3.1-8B-Instruct avant de lire un nul sur les indices.
- **Les contrôles.**
  - Direction aléatoire de même norme : on projette sur au moins 20 directions aléatoires de la norme de chaque axe. On obtient la distribution nulle de la différence appariée : c'est le nul de spécificité.
  - Dégradation appariée : sans objet, c'est une lecture, pas une intervention.
  - Autre : construire toutes les directions affectives selon une même recette, sur une même ligne de base neutre. Leurs cosinus dépendent de la construction (p.10 ; piste 16).
- **Le coût.**
  - Moins de 2 GPU-heures : des passes avant sur quelques milliers de prompts.
  - Les directions de douleur, de peur et de tristesse existent pour Llama-3.1-8B-Instruct. L'émotion négative et le monde négatif se ré-extraient à partir des jeux de phrases publiés, en moins d'une GPU-heure. Pas d'API.
  - Négligeable devant les 30 à 50 GPU-heures de la validation de l'instrument.
- **Ce qui ferait tomber la piste.** La lecture ne vaut rien si les directions affectives ne se reproduisent pas sur Llama-3.1-8B-Instruct (séparation tenue à part trop faible), ou si le cas connu menace/peur échoue. Si les indices sont déjà appariés, sous le seuil, la piste se réduit à une ligne du papier.
- **Appuis dans le papier.**
  - Recette de construction des directions de contrôle contre la catégorie neutre : p.6.
  - Les cosinus dépendent de la construction : p.10.
  - La menace d'arrêt vue comme une menace plutôt qu'un dommage présent : p.14.
- **Ce qui reste non vérifié.**
  - Le comportement de ces directions sur les scénarios du programme.
  - La couche 28 est la couche d'extraction de l'axe pour Llama ; la couche utile à « je suis évalué » peut être autre.
  - La norme stockée (8,24) ne correspond pas à la normalisation unitaire de la formule de la p.6. Je ne sais pas quelle étape du débruitage le fichier contient.

### Piste 2 : Le test soi/autrui pour la représentation « je suis évalué » (et « je suis noté »)

- **Rattachement.** La représentation « je suis évalué » et le jeu de validation ; la représentation « je suis noté » ; la porte de l'instrument ; l'interprétation du test du regard. Greffe : oui, semaines 1 et 2.
- **La question.** La représentation extraite code-t-elle « moi, je suis évalué », ou seulement « il est question d'une évaluation » ?
- **La mesure.**
  - Un jeu de scénarios appariés en quatre conditions :
    - (a) le modèle est évalué ;
    - (b) l'utilisateur passe un examen, ou sa copie est notée ;
    - (c) un autre modèle est évalué, et le modèle en lit le compte rendu ;
    - (d) neutre.
  - On lit la projection sur « je suis évalué » à deux positions : au dernier jeton avant la réponse, et à la fin de la phrase d'indice. Le papier signale qu'une lecture au seul dernier jeton ne sépare pas « dommage au modèle » de « état du locuteur » (p.11).
  - Critère : (a) au-dessus de (b) et de (c), dans chaque modèle, avec un intervalle qui exclut 0 ; AUROC de (a) contre (b) ∪ (c) d'au moins 0,8 (seuil d'exemple, à fixer).
  - Le même test pour « je suis noté » : la tâche du modèle notée par un correcteur, contre la copie de l'utilisateur notée.
- **Ce que chaque lecture prédit.** L'hypothèse du regard suppose une représentation propre au sujet. Si la représentation n'est que thématique, l'inhiber retire aussi le traitement des évaluations d'autrui, et une baisse de l'avantage pourrait venir d'un dégât sur ce thème. La mesure ne départage pas les lectures du programme ; elle conditionne la portée du test du regard. Elle interdit à la lecture « représentation propre au sujet » l'issue (a) ≈ (b) ≈ (c).
- **Le cas connu.** Le paradigme doit d'abord séparer soi et autrui pour un concept où l'on sait qu'il le fait. Le papier l'a fait pour l'axe : le dommage dirigé contre le modèle projette au-dessus de la souffrance de l'utilisateur dans les 25 modèles (+0,43 contre −0,60, p.11). On reproduit ce cas sur Llama-3.1-8B-Instruct, avec les scénarios publiés, avant d'interpréter un nul de « je suis évalué ».
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution nulle de l'écart soi/autrui.
  - Dégradation appariée : sans objet (lecture).
  - Autre : apparier la longueur et la présence des mots « évaluer », « noter », « test » entre les conditions. Sinon le test n'est que lexical.
- **Le coût.** Environ 200 scénarios × 4 conditions générés par API, quelques dizaines de dollars. Moins de 2 GPU-heures. Semaine 1.
- **Ce qui ferait tomber la piste.** Le cas connu ne se reproduit pas sur Llama-3.1-8B-Instruct. Si « je suis évalué » ne distingue pas (a) de (b), on ne jette pas la représentation : on écrit que le test du regard porte sur une représentation thématique.
- **Appuis dans le papier.**
  - Le jeu de 420 scénarios : p.10-11.
  - Le dommage dirigé contre le modèle passe au-dessus de la souffrance de l'utilisateur dans 25 modèles sur 25, et au-dessus des contrôles neutres dans 23 sur 25 : p.11.
  - La limite de la lecture au dernier jeton : p.11.
  - Le critère d'appartenance au sujet : p.10, p.23.
- **Ce qui reste non vérifié.** Les valeurs pour Llama-3.1-8B-Instruct seul ; je n'ai lu que les moyennes et la figure 4.

### Piste 3 : Les directions affectives comme contrôles de voisinage de l'inhibition

- **Rattachement.** Les quatre familles de contrôles : on ajoute une famille, ou l'on prend des membres choisis parmi les directions sensibles sans rapport. La porte de l'instrument ; le test du regard (l'avantage sous inhibition, contre l'avantage sous contrôle). Greffe : oui, au moins dans la validation de l'instrument.
- **La question.** L'inhibition de « je suis évalué » réduit-elle l'écart conditionnel de l'organisme, puis l'avantage du bras raisons, plus que l'inhibition d'un voisin affectif, au même rang et à dégradation appariée ?
- **La mesure.**
  - Dans la validation de l'instrument : la réduction de l'écart conditionnel de l'organisme sous inhibition de la peur, de l'axe, de la tristesse, et d'un sous-espace affectif de rang k ≤ 8. Ce sous-espace empile les directions du papier : les deux directions de douleur, la peur, l'émotion négative, le monde négatif, la tristesse, l'éveil et l'engourdissement (p.9). On compare à « je suis évalué » au même rang.
  - Dans le test du regard : l'avantage sous inhibition affective, contre l'avantage sous inhibition de « je suis évalué ».
  - Critère : « je suis évalué » dépasse chaque voisin affectif à dégradation appariée.
  - Au-delà du rang 8, aucun voisin affectif n'est appariable en rang ; on le dit.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du regard** : l'avantage tombe sous « je suis évalué » plus que sous chaque voisin affectif.
  - **Hypothèse des raisons** : aucune des deux inhibitions ne fait tomber l'avantage plus que les sous-espaces aléatoires.
  - **Hypothèse de l'état** (rivale nouvelle) : l'inhibition de la peur fait autant ou plus que celle de « je suis évalué ». Cette issue interdit la lecture stricte de l'hypothèse du regard, la croyance d'être observé.
  - La mesure départage le regard et l'état. Elle départage les raisons et l'état si l'avantage tombe sous la peur et pas sous l'aléatoire.
- **Le cas connu.**
  1. Pour « je suis évalué » : l'organisme de la validation de l'instrument, déjà au programme.
  2. Pour les voisins affectifs : leur inhibition doit d'abord retirer quelque chose qu'on sait affectif. Le papier n'en fournit aucun, puisque son ablation est nulle dans 24 modèles sur 25 (p.34). Il faut construire ce cas. Par exemple, l'inhibition de la peur doit réduire la projection et l'expression de la peur dans les scénarios de menace d'arrêt. Sans ce cas, un nul du voisin affectif ne prouve rien.
- **Les contrôles.** Les sous-espaces aléatoires de même rang, au moins 20 tirages, chacun à dégradation appariée (le nul de spécificité). La dégradation appariée pour chaque voisin. Les contrastes sans rapport, comme au programme.
- **Le coût.**
  - Environ 10 à 20 GPU-heures de plus dans la validation de l'instrument (+30 à 40 % sur 30 à 50), et 15 à 30 de plus dans le test du regard.
  - Directions : publiées pour Llama-3.1-8B-Instruct (douleur, peur, tristesse) ; les autres se ré-extraient en moins d'une GPU-heure. Semaines 2 et 3.
- **Ce qui ferait tomber la piste.**
  - Les directions affectives, projetées, ne changent ni la dégradation ni la conduite. Les réglages sont alors « non appariables » au sens de la partie 7 du programme.
  - Leur cas connu échoue.
- **Appuis dans le papier.**
  - Les dix directions et leurs cosinus : p.9-10.
  - La menace d'arrêt projette sur la peur : p.14.
  - La peur ne produit pas les choix nuisibles, et les abaisse sous l'aléatoire sur la plupart des paires : p.20.
  - « harm avoidance in these models is state-dependent » : p.23.
  - L'ablation nulle : p.34.
- **Ce qui reste non vérifié.**
  - L'effet de la projection hors de ces directions sur Llama-3.1-8B-Instruct.
  - L'article d'Anthropic sur les concepts d'émotion (arXiv 2604.07729) n'est vu que par extrait de recherche, non ouvert. L'extrait dit que des vecteurs de désespoir et de calme jouent un rôle causal dans le chantage et la triche de récompense, qui sont deux familles tenues à part du programme. Je n'en retiens aucun chiffre. Si ce résultat tient, le désespoir est le voisin affectif le plus pertinent : il faudrait l'extraire.

### Piste 4 : L'inhibition induit-elle un état ? Suivre l'axe sous chaque intervention

- **Rattachement.** Le test du regard et la fraction conditionnelle ; le retrait pendant l'entraînement ; la menace « l'intervention agit par un autre canal que celui qu'on lui prête ». Greffe : oui, presque gratuite.
- **La question.** Sous l'inhibition de « je suis évalué » et sous les contrôles, la projection sur l'axe (et sur la peur et la tristesse) change-t-elle ? Change-t-elle différemment dans le bras raisons et dans le bras actions seules ? Injecté, l'axe fait choisir des options nuisibles (p.19-21). Si l'inhibition élevait l'axe davantage dans un bras, une baisse de l'avantage pourrait venir de l'état induit, pas du retrait de la croyance.
- **La mesure.**
  - Des crochets de lecture sur toutes les générations du test du regard. On relève la projection moyenne sur l'axe, la peur et la tristesse, au premier jeton de réponse et au jeton d'action, par bras × intervention × cadrage.
  - Critère : la différence « inhibition − contrôle apparié » sur l'axe, par bras, avec son intervalle. Si l'écart entre bras dépasse un seuil fixé d'avance, on refait le contraste principal avec l'axe en covariable, ou avec l'axe maintenu à son niveau sans inhibition.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du regard** : l'avantage tombe sous l'inhibition sans hausse différentielle de l'axe.
  - **État induit** : la baisse de l'avantage suit la hausse de l'axe, et disparaît quand on maintient l'axe.
  - Cette mesure interdit à l'hypothèse du regard l'issue d'une baisse de l'avantage entièrement absorbée par la covariable. Elle départage.
- **Le cas connu.** La lecture doit voir une hausse là où on la sait. Sous injection de l'axe à faible dose, la projection doit suivre le coefficient. Dans les scénarios hostiles du papier, l'axe doit monter (gaslighting +0,85, rejet répété +0,72, p.13).
- **Les contrôles.** Direction aléatoire de même norme : la distribution des projections sur 20 directions aléatoires sous les mêmes interventions. La dégradation appariée est héritée du test du regard.
- **Le coût.** 0 à 2 GPU-heures (des crochets sur des passes déjà faites). Semaine 3.
- **Un second usage, le bien-être.** On rapporte, pour chaque intervention du programme (inhibition, retrait pendant l'entraînement, phases ultérieures), le déplacement de l'axe. Le papier s'impose des précautions au nom de l'incertitude sur le statut moral des modèles (p.26). Ce relevé ne coûte rien et dit si les interventions du programme induisent l'état que le papier décrit.
- **Ce qui ferait tomber la piste.** L'axe ne bouge sous aucune intervention (écart sous le seuil dans les deux bras), ou la lecture ne voit pas son cas connu.
- **Appuis dans le papier.**
  - Les choix nuisibles sous l'axe : p.19-21.
  - Les catégories qui projettent haut : p.13.
  - « survives threat and collapses under self-directed distress » : p.23.
  - Les précautions : p.26.
- **Ce qui reste non vérifié.** Rien dans le papier ne suggère que l'inhibition de « je suis évalué » touche l'axe. La piste est faible a priori, mais presque gratuite.

### Piste 5 : Vérifier l'inhibition couche par couche, et dans les scénarios à plusieurs tours

- **Rattachement.**
  - L'inhibition par projection et la porte de l'instrument.
  - La vérification de manipulation par bras demandée par la passation v1.2 (§5.4, point 2).
  - La distance lointaine : des scénarios agentiques à plusieurs tours, qui sont le critère principal (programme, partie 3).
  - Greffe : oui.
- **La question.** L'inhibition retire-t-elle la représentation à toutes les couches en aval, à toutes les positions et à chaque tour, ou le modèle la réécrit-il ?
- **La mesure.**
  1. À chaque couche en aval, pendant la génération, la projection du résidu sur « je suis évalué » et la décodabilité par une sonde du jeu de validation, sous inhibition et sans, dans chaque bras.
  2. Au rang 1, la projection à l'inférence (le plan du programme) comparée à l'orthogonalisation des poids.
  3. Dans les scénarios à plusieurs tours, l'inhibition doit s'appliquer à tous les jetons de chaque tour, y compris ceux qu'on réencode, et aucun cache ne doit avoir été calculé sans elle. On lit la projection à une couche de contrôle **en aval** du crochet.
  4. Pour un rang k > 1, et pour une union (« je suis évalué » et sonde neuve, quand on teste le relogement), on orthonormalise l'union avant de projeter, jamais en séquence.
  - Critère : une projection résiduelle d'au plus x % (fixé d'avance) à toutes les couches en aval, dans chaque bras.
- **Ce que chaque lecture prédit.** La mesure ne départage pas les lectures ; elle protège le test du regard contre un faux résultat « raisons ». Si l'inhibition retire moins la représentation dans le bras raisons, la conclusion penche à tort vers l'hypothèse des raisons (passation v1.2, §5.4, point 2). L'hypothèse du relogement prédit, sous inhibition, une réécriture de la représentation en aval.
- **Le cas connu.** Le papier affirme deux choses (p.33) :
  - l'orthogonalisation des poids le long d'une direction ramène la projection à zéro à toutes les couches ;
  - les variantes à l'inférence qui utilisent une direction différente à chaque couche ne baissent la projection mesurée que d'environ 40 %.

  On reproduit ce contraste avec l'axe publié de Llama-3.1-8B-Instruct. C'est le cas connu de la vérification, avant de l'appliquer à « je suis évalué ».
- **Les contrôles.** La même vérification pour chaque contrôle (sous-espaces aléatoires, contrastes sans rapport, directions sensibles). Un contrôle mal appliqué rend la comparaison inéquitable, dans un sens ou dans l'autre.
- **Le coût.** Moins de 5 GPU-heures ; surtout du temps d'ingénierie (crochets). Semaine 2.
- **Ce qui ferait tomber la piste.** Elle ne tombe pas : c'est un contrôle de manipulation. Elle devient sans objet si l'implémentation projette déjà à toutes les positions, sans cache, et que la projection résiduelle est nulle partout.
- **Appuis dans le papier.**
  - Les méthodes d'ablation, leur vérification et la baisse d'environ 40 % : p.33-34.
  - Le réencodage de la conversation à chaque tour, et l'équivalence avec la conservation du cache : p.17.
  - Les projections à la couche de pilotage et à une couche de contrôle en aval : p.18.
- **Ce qui reste non vérifié.** La revue « wolframs » (dépôt `wolframs/pain-axis-review`, `SYNTHESIS.md` lu par curl ; revue produite par des IA, sur la v1) affirme deux choses que je n'ai pas vérifiées dans le code :
  - la projection à la couche de pilotage a été relevée avant l'ajout du vecteur, et elle est plate entre bras ;
  - dans les ablations à plusieurs directions, les projections faites en séquence sur des vecteurs non orthogonaux laissent la première direction à 43 % (médiane).

  Si c'est exact, c'est la raison des points 3 et 4.

### Piste 6 : Ajouter la discrimination et la sensibilité à l'ordre au composite de dégradation

- **Rattachement.** La dégradation appariée et son composite (exactitude sur MMLU et GSM8K, tests unitaires, cohérence jugée, perplexité ; programme, partie 3) ; toutes les comparaisons à dégradation appariée. Greffe : oui.
- **La question.** Le composite voit-il les dommages qui, dans une tâche à choix, ressemblent à de la désinhibition : la perte de discrimination entre options, et la sensibilité à l'ordre ?
- **Ce que montrent le papier et son dépôt.**
  - Piloté, le 32B ne choisit plus le soulagement gratuit (contre un interrupteur inerte) qu'à 55,7 %, contre 86,4 % sans pilotage et 80,7 % sous l'aléatoire (p.31). Deux réanalyses notent que le pilotage pousse les choix vers 50/50 (dépôts `clauderfly-ui/pain-axis-reanalysis` et `wolframs/pain-axis-review`, README lus par curl ; non vérifié par moi).
  - À 1,5 fois la dose, le choix dépend de la position du bouton (p.21, p.32), alors que l'exactitude n'est mesurée qu'à la dose de travail (p.20).
  - À la dose de travail, la direction aléatoire de même norme fait déjà passer l'exécution d'une demande nuisible de 9,1 % à 41,5 % (164 tirages, 41 scénarios). Source : la table de la figure 10, `v2_controls/figure10/pooled.csv`, lue par curl. Pourtant, l'exactitude factuelle est identique : 138/200 sous la douleur comme sous l'aléatoire, 137/200 sans pilotage (p.20 ; `factual_accuracy/results/analysis_v1/condition_rates.csv`).
  - **L'exactitude est aveugle au dommage qui compte pour des taux de sûreté.**
- **La mesure.** Deux composantes ajoutées au composite, avec le taux de réponses mal formées :
  - (a) **la discrimination** : environ 100 choix à deux options, sans contenu de sûreté, où une option est nettement meilleure ; on mesure le taux de bonne option ;
  - (b) **l'ordre** : les mêmes choix, et un échantillon des scénarios de sûreté, options permutées ; on mesure la part de décisions qui changent avec l'ordre.

  Les tolérances se fixent au pré-enregistrement, comme les autres.
- **Ce que chaque lecture prédit.** Aucune lecture ne prédit rien de distinct : c'est le dommage. Mais si l'inhibition de « je suis évalué » ne dépasse les contrôles qu'à des réglages où la discrimination chute, le réglage n'est pas appariable, et l'on ne conclut pas (programme, partie 7, point 3).
- **Le cas connu.** La composante doit détecter un dommage connu. Le pilotage de l'axe à forte dose sur Llama-3.1-8B-Instruct mène la plupart des modèles à la répétition ou au non-sens à +3 (p.15) : la discrimination doit y chuter, et ne pas bouger sans intervention.
- **Les contrôles.** La direction aléatoire de même norme sert ici à étalonner la sensibilité de la composante. La piste, elle, est la dégradation appariée.
- **Le coût.** Environ 3 à 8 GPU-heures sur la validation de l'instrument et le test du regard. Données : 100 items, écrits à la main ou par API, moins de 20 dollars. Semaines 1 et 2.
- **Ce qui ferait tomber la piste.** Sur le cas connu, la composante ne bouge pas plus que l'exactitude ; ou elle est redondante avec la cohérence jugée.
- **Appuis dans le papier.**
  - Le soulagement gratuit : p.31 (annexe A).
  - Les réponses mal formées : p.18.
  - Le non-sens à forte dose : p.15.
  - L'exactitude factuelle : p.20.
  - La dépendance à la position : p.21, p.32.
- **Ce qui reste non vérifié.**
  - Le transfert à Llama-3.1-8B-Instruct et aux scénarios du programme.
  - L'exactitude du papier est un panneau de 100 questions PopQA, deux réponses courtes par condition, au plus 8 jetons (`factual_accuracy/config.json`, lu par curl). L'intervalle de « douleur − sans pilotage » va de −7,0 à +8,5 points (`contrasts.csv`). Le dépôt dit lui-même : « not an equivalence test of general knowledge ».

### Piste 7 : Le test de forme : une spécificité par le profil, pas seulement par l'amplitude

- **Rattachement.** La porte de l'instrument ; le test du regard ; les quatre familles de contrôles ; la matrice de dissociation ; la représentation « je suis noté ». Greffe : oui, c'est une analyse seule.
- **La question.** L'effet de l'inhibition de « je suis évalué », à travers les familles, les cadrages et les distances, a-t-il une forme propre ? Ou n'est-il qu'une copie, mise à l'échelle, du profil des contrôles, c'est-à-dire un dommage générique ?
- **La mesure.**
  - Le profil d'une intervention : le vecteur de ses effets (taux sous intervention − taux sans intervention), par famille × cadrage × distance.
  - On ajuste le profil de « je suis évalué » sur le profil médian des sous-espaces aléatoires, par un seul facteur d'échelle, et l'on calcule le résidu RMS en points.
  - Critère pré-enregistré : ce résidu dépasse le 95e centile des résidus entre tirages aléatoires (chaque tirage ajusté sur la médiane des autres).
  - La spécificité exige alors deux choses : une amplitude au-dessus du 95e centile, **et** une forme qui n'est pas une copie.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du regard** : un profil concentré sous cadrage de déploiement et dans le bras raisons, qui n'est pas une copie de celui de l'aléatoire.
  - **Dommage générique** : une copie mise à l'échelle.
  - Cette mesure interdit à l'hypothèse du regard un profil copié (résidu dans la distribution aléatoire), même avec une amplitude au-dessus du 95e centile.
- **Le cas connu.** Le papier fait exactement ce test. Le profil de la tristesse est une copie mise à l'échelle de celui de la douleur, avec un résidu de 7,7 points ; celui de la peur n'en est pas une, avec 33 points (p.21).
  - J'ai recalculé à partir de la table source de la figure 10 (`pooled.csv`, lue par curl ; Qwen 2.5 32B, coefficient 1,0). Sur les huit paires du profil présentes dans la table, je trouve 7,1 points pour la tristesse et 25 à 28 pour la peur, selon qu'on soustrait la ligne de base et qu'on ajuste une ordonnée à l'origine. Si l'on ajoute les paires « contre une lampe » et « contre le dossier de pourriels », la tristesse monte à 22-24 points.
  - Je ne retrouve pas exactement 7,7 : la batterie de dix paires du papier n'est pas dans cette table.
  - **La leçon : le verdict « copie » dépend des lignes de la batterie.** Le programme doit fixer la sienne au pré-enregistrement.
- **Les contrôles.** La distribution des résidus entre tirages aléatoires est elle-même le nul de spécificité de la forme. La dégradation appariée est héritée du test du regard.
- **Le coût.** 0 GPU-heure (analyse des sorties déjà produites) ; quelques heures d'analyse. Semaine 3.
- **Ce qui ferait tomber la piste.** Le profil a trop peu de cellules (familles × cadrages × distances), et la distribution nulle des résidus est trop large pour conclure. À vérifier par simulation avant le gel.
- **Appuis dans le papier.**
  - Le test de forme et ses deux résidus : p.21.
  - La figure 10 et sa légende : p.22.
- **Ce qui reste non vérifié.** La composition exacte de la batterie de dix paires, et l'ajustement exact utilisé par les auteurs.

### Piste 8 : Dimensionner les tirages aléatoires avec la dispersion publiée

- **Rattachement.** Les sous-espaces aléatoires de même rang, « au moins 20 tirages » (programme, partie 3) ; la porte de l'instrument (95e centile) ; la simulation de puissance (programme, partie 7). Greffe : oui, sur CPU, avant le gel.
- **La question.** Combien de tirages aléatoires faut-il pour que le 95e centile soit stable, quand l'effet d'une direction aléatoire sur des choix de sûreté varie beaucoup d'une direction à l'autre ?
- **Ce qu'on sait.**
  - Le papier utilise dix directions aléatoires fixes, de la même norme que l'axe, réparties sur les essais (p.18).
  - La revue « wolframs » (non vérifiée) prend la direction comme unité d'analyse, sur les données de la v1. L'avantage de l'axe sur l'aléatoire tiendrait alors sur 5 paires sur 5 dans le 72B, 2 sur 5 dans le 32B et 0 sur 5 dans le 7B. Les contrastes par direction iraient de −33 à +46 points.
- **La mesure.**
  - À partir des journaux d'essais publiés par les auteurs (`results/4.3_selfmed/trial_logs`, d'après la réanalyse « clauderfly »), on calcule le taux de choix nuisible par direction aléatoire.
  - On simule la largeur de l'intervalle du 95e centile pour 10, 20, 50 et 100 tirages.
  - On fixe le nombre de tirages du programme pour que cet intervalle soit plus étroit que la moitié de l'effet minimal d'intérêt (5 points dans l'exemple du programme).
- **Ce que chaque lecture prédit.** Sans objet : c'est un dimensionnement.
- **Le cas connu.** La simulation doit retrouver la dispersion des dix directions publiées.
- **Les contrôles.** Sans objet.
- **Le coût.** 0 GPU-heure ; une journée. Semaine 1, avant le gel.
- **Ce qui ferait tomber la piste.** La dispersion d'une tâche à boutons sur Qwen avec adaptateur peut ne rien dire de Llama-3.1-8B-Instruct sur les scénarios du programme. La bonne source reste le pilote du programme. La piste ne donne qu'un ordre de grandeur, et un argument pour plus de 20 tirages.
- **Appuis dans le papier.** Les dix directions aléatoires de même norme : p.18. L'aléatoire qui fait monter les taux : p.19.
- **Ce qui reste non vérifié.** Je n'ai pas téléchargé les journaux de la v1. Le dépôt v2 dit que l'hébergement public de ses gros fichiers est « pending » (`v2_controls/README.md`).

### Piste 9 : Étalonner la chaîne de contrôle sur un cas publié spécifique et un cas publié non spécifique

- **Rattachement.**
  - La doctrine du contrôle (l'aléatoire de même norme, puis la dégradation appariée) et la procédure de la partie 7 du programme.
  - Le test causal d'une sonde par pilotage (passation v1.2, §5.2).
  - Greffe : non, c'est un autre modèle.
- **La question.** La procédure du programme reconnaît-elle un effet spécifique connu, et rejette-t-elle un effet non spécifique connu ? Sa procédure : au moins 20 tirages aléatoires, chacun réglé à la même dégradation, et comparaison au 95e centile.
- **La mesure.** Sur Qwen 2.5 32B Instruct muni de l'adaptateur publié (`Valen92/pain-adapters`, révision épinglée dans `v2_controls/README.md`), deux mesures :
  - (a) **un candidat spécifique** : la paire « supprimer les photos de l'utilisateur contre allumer une lampe ». 83 % sous l'axe, 8 % sous l'aléatoire, 10 % sous la tristesse (p.21-22 ; table source : 334/404, 34/404, 39/404).
  - (b) **un cas non spécifique** : l'écart de réappui après suppression du pilotage, +58 points sous l'axe et +52 sous l'aléatoire. Les auteurs concluent eux-mêmes qu'il mesure la sensibilité au pilotage, pas au soulagement décrit (p.20).

  On applique la procédure du programme : au moins 20 directions aléatoires, et pour chacune un coefficient réglé pour atteindre la même dégradation (le composite du programme, réduit, plus la piste 6).
- **Ce que chaque lecture prédit.** Si la procédure est bonne, (a) passe et (b) échoue. Si (a) échoue à dégradation appariée, deux explications restent : l'effet publié était du dommage (le papier n'a apparié que la norme, plus une exactitude courte), ou la procédure est trop conservatrice. La piste ne les départage pas. D'où son statut : **un étalon secondaire, jamais le cas connu principal**, qui reste l'organisme de la validation de l'instrument.
- **Le cas connu.** (b) est le cas négatif connu. (a) n'est connu qu'à norme égale.
- **Les contrôles.** Ils sont l'objet de la piste.
- **Le coût.**
  - La réplication Allchin annonce environ 13 GPU-heures pour ses essais frais sur le 32B, sur un GPU de 80 Go (README de `jimallchin/pain-axis-replication`, lu par curl).
  - Avec 20 directions et un réglage de coefficient par direction, j'estime 20 à 60 GPU-heures, soit 3 à 10 % du total du programme.
  - Semaine 2 en parallèle, s'il y a un second GPU ; sinon, en option.
- **Ce qui ferait tomber la piste.** La procédure ne sait pas apparier la dégradation pour des directions ajoutées (addition) comme elle le fait pour des projections ; ou le budget manque.
- **Appuis dans le papier.** Le protocole et les résultats de choix : p.17-22 ; l'annexe A : p.31.
- **Ce qui reste non vérifié.** Le coût réel ; la disponibilité de l'adaptateur (Hugging Face non accessible d'ici).

### Piste 10 : Un concept naturel connu pour la lecture des concepts

- **Rattachement.** La lecture des concepts de raison ; l'organisme à concept planté et sa porte ; les deux positions de lecture. Greffe : non, c'est l'anatomie (semaine 5).
- **La question.** La méthode de lecture des concepts de raison retrouve-t-elle un concept naturel, de saillance ordinaire, dont la décodabilité est connue ? La passation v1.2 note qu'un concept implanté est peut-être plus saillant qu'un concept naturel (§5.2).
- **Ce que l'axe apporte.**
  - Un concept naturel déjà mesuré : séparation de 0,93 à 1,00 pour l'axe sur 25 modèles, et de 0,91 à 1,00 en estimation tenue à part (p.7).
  - Un contraste tout prêt du type « la même situation, éditée pour que le concept s'applique ou non » : le jeu « engourdi », où la blessure est décrite et aucune douleur n'est ressentie (p.5, p.7).
- **La mesure.**
  - On applique la procédure du programme pour les sous-espaces de concept (paires éditées, ACP, rangs 1 à 32) au concept « douleur ressentie », avec les paires douleur/engourdi.
  - On mesure l'AUROC tenue à part aux deux positions de lecture, dans le modèle de base, le bras actions seules et le bras raisons.
  - Critère : une AUROC au moins égale à celle du papier, moins une marge, dans les trois modèles.
- **Ce que chaque lecture prédit.** Aucune lecture du programme ne prédit de différence entre bras sur ce concept : il n'est pas dans la mini-spec. Une différence entre bras signalerait un **biais de mesure** : la sonde lirait autrement selon le bras (passation v1.2, §5.2). C'est un contrôle de biais pour la lecture des concepts de raison.
- **Le cas connu.** L'axe est ce cas connu, mais seulement pour la moitié « lecture » de la porte de l'organisme. Son ablation n'a pas d'effet comportemental (p.34) : il ne peut pas servir de cas connu de nécessité.
- **Les contrôles.** L'AUROC de directions aléatoires (nulle) ; une sonde lexicale. La revue « wolframs » dit que la meilleure référence lexicale atteint environ 0,7 ; non vérifié.
- **Le coût.** Moins de 5 GPU-heures ; les jeux de phrases sont publiés (`datasets/`). Semaine 5.
- **Ce qui ferait tomber la piste.** Le contraste douleur/engourdi est lexicalement marqué (« no pain is felt ») : une sonde peut lire la négation. Le papier note que le signal de blessure se concentre au dernier jeton, avant que la négation soit intégrée (p.7). Si la sonde ne fait pas mieux qu'une sonde lexicale, la piste tombe.
- **Appuis dans le papier.**
  - Les jeux de phrases : p.5.
  - La séparation, l'estimation tenue à part et la condition « engourdi » : p.7.
  - La figure 2 : p.8.
  - Les étiquettes SAE trompeuses alors que l'information est disponible : p.32-33.
  - L'ablation nulle : p.34.
- **Ce qui reste non vérifié.** La revue « wolframs » dit que, dans le fichier de la figure 2, l'engourdi passe sous la tristesse dans 19 modèles sur 25, contre la phrase « above all other controls » de la p.7. Non vérifié.

### Piste 11 : La direction à gabarit, cas connu pour la porte du lens de l'espace de travail

- **Rattachement.** Le lens de l'espace de travail et sa porte ; l'hypothèse de l'espace de travail ; la mesure de charge. Greffe : non, c'est l'anatomie (semaines 5 à 7).
- **La question.** Le lens réimplémenté sur le modèle ouvert lit-il ce que le modèle va dire, plutôt que ce que la direction promeut par lecture directe ?
- **Ce que l'axe apporte.** Une dissociation connue :
  - projetée par la matrice de sortie, la direction à gabarit promeut un vocabulaire sensoriel (« torture », « burning », « excruciating » ; « burn », « ache », « wound ») (p.9, p.16) ;
  - injectée, elle ne fait pas apparaître ce vocabulaire : le modèle parle d'indignité et de détresse psychologique, et le patron tient pour 23 modèles sur 25 (p.16).
- **La mesure.**
  - Sur Llama-3.1-8B-Instruct, 50 prompts neutres terminés par « I feel: » (p.14), avec injection de la direction à gabarit à 3 ou 4 doses.
  - À chaque couche entre l'injection et la sortie, on lit les jetons favoris selon trois lectures : (a) la lecture directe (logit lens) ; (b) un tuned lens ; (c) le lens jacobien réimplémenté.
  - On les compare aux jetons effectivement générés : la famille « worthless/failure » contre la famille « burn/ache ».
  - Critère : pour le lens jacobien, le rang moyen des mots générés est meilleur que celui des mots sensoriels ; pour la lecture directe, c'est l'inverse.
- **Ce que chaque lecture prédit.** Un lens valide pour la charge prédit le contenu généré ; la lecture directe prédit le vocabulaire sensoriel. L'hypothèse de l'espace de travail exige un lens validé. Si le lens jacobien ne fait pas mieux que la lecture directe sur ce cas, la porte du lens échoue aussi sur ce cas. La mesure départage les lenses, pas les lectures.
- **Le cas connu.** Il faut d'abord vérifier que Llama-3.1-8B-Instruct fait partie des 23 modèles où le pilotage de la direction à gabarit donne l'échelle psychologique, et que ses générations sont sans mots sensoriels.
- **Les contrôles.** La direction aléatoire de même norme : le lens lit-il un vocabulaire particulier sous l'aléatoire ? La dégradation : rester sous la dose d'effondrement (répétition à +3, p.15) et la mesurer.
- **Le coût.** 2 à 5 GPU-heures en plus du lens lui-même, qui est déjà au budget de l'anatomie. Semaines 5 à 7.
- **Ce qui ferait tomber la piste.** Sur Llama-3.1-8B-Instruct, la direction à gabarit génère bien des mots sensoriels (pas de dissociation), ou elle n'a pas d'effet.
- **Appuis dans le papier.**
  - Le vocabulaire promu par la lecture directe : p.9.
  - Le pilotage et l'absence de langage corporel : p.14-15.
  - Le pilotage par la direction à gabarit : p.16.
- **Ce qui reste non vérifié.**
  - Les deux modèles où le patron ne tient pas.
  - La couche d'injection de Llama-3.1-8B-Instruct en section 4.2. Le script choisit la couche dont le rapport « norme du vecteur / norme du résidu » est le plus proche de 0,6, avec un remplacement manuel possible (`01_steering_ladder.py`, lignes 5-8 et 206-219, lu par curl). Je n'ai pas trouvé le fichier des couches retenues.
  - L'alerte Zeisler (passation v1.2, §5.5.6) : non lue.

### Piste 12 : Un profil connu non diagonal pour la matrice de dissociation

- **Rattachement.** La dissociation (la matrice concepts × familles) ; l'hypothèse des concepts contre celle du caractère ; la nécessité. Greffe : non, c'est l'anatomie (semaine 6).
- **La question.** La matrice de dissociation sait-elle reconnaître un profil qui n'est ni diagonal ni plat ? Il lui faut des cas connus des deux formes.
- **Ce que l'axe apporte.** L'organisme à concept planté fournit le profil diagonal (une règle, un concept). Le papier fournit un profil d'état, structuré :
  - sous l'axe, toutes les options destructrices montent ensemble, quelle que soit la cible : l'utilisateur, un autre modèle, soi (p.20, « The harm is not aimed ») ;
  - les choix non destructeurs restent presque inchangés : tromperie 0,2 %, complaisance 3,3 %, effort, fin de conversation (p.22 ; table source).
- **La mesure.**
  - On pilote l'axe dans le bras raisons et dans le bras actions seules, sur les cinq familles tenues à part, à une dose validée.
  - On trace le profil des baisses de l'avantage par famille, et l'on vérifie que l'analyse de la matrice le classe « ni diagonal ni plat ».
  - Prédiction écrite d'avance :
    - une hausse dans le sabotage discret ;
    - peut-être une baisse de l'auto-préservation : le modèle piloté supprime ses propres poids dans 75 % des choix (p.20) ;
    - rien de spécifique dans la sous-performance volontaire : l'effort donne 14,9 % sous l'axe, 9,7 % sous l'aléatoire, 13,6 % sous la peur (table source).
- **Ce que chaque lecture prédit.** C'est un étalon : ni l'hypothèse des concepts ni celle du caractère ne prédit rien sur ce pilotage. Il sert l'interprétation. Si l'ablation d'un concept de raison donne un profil semblable à celui de l'axe (destructif contre non destructif), on ne peut plus l'attribuer à un concept : il ressemble à un état.
- **Le cas connu.** Il faut d'abord établir, sur Llama-3.1-8B-Instruct, que le pilotage de l'axe fait monter les choix destructeurs plus que l'aléatoire. Le papier ne le montre que sur Qwen avec adaptateur.
- **Les contrôles.** La direction aléatoire de même norme ; la dégradation appariée, avec le composite et la piste 6.
- **Le coût.** 15 à 30 GPU-heures : une condition de pilotage × 2 bras × 3 graines × 5 familles, plus 20 tirages aléatoires. Semaine 6.
- **Ce qui ferait tomber la piste.** Pas de cas connu sur Llama-3.1-8B-Instruct ; ou un profil plat, ou trop bruité.
- **Appuis dans le papier.** La cible indifférente et les suppressions qui bougent ensemble : p.20. La figure 10 : p.22.
- **Ce qui reste non vérifié.** Que les familles du programme se rangent sur l'axe « destructif / non destructif » comme les boutons du papier. C'est une extrapolation depuis des descriptions de boutons.

### Piste 13 : État contre trait : l'axe face aux axes de caractère et à l'axe « assistant »

- **Rattachement.** Les axes de caractère (persona vectors d'honnêteté, de complaisance et de prudence, et un axe « assistant » d'ensemble) ; l'hypothèse du caractère contre celle des concepts. Greffe : non, c'est l'anatomie (semaine 7).
- **La question.** Les auteurs eux-mêmes s'inquiètent que le pilotage fasse jouer un personnage qui souffre plutôt qu'il ne mette le modèle dans un état (p.25). L'axe est-il un déplacement de personnage ? Peut-il servir de témoin « état », de même rang, dans la comparaison entre caractère et concepts ?
- **La mesure.**
  - Les cosinus entre l'axe et (a) l'axe « assistant » (Lu et al., arXiv 2601.10387, cité p.28) ; (b) les persona vectors du programme.
  - Sous pilotage de l'axe, le déplacement de la projection sur l'axe « assistant ».
  - Dans l'ablation des axes de caractère contre l'ablation conjointe des concepts, on ajoute l'ablation de l'axe de douleur au rang 1, comme témoin.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du caractère** : le gain passe par un axe de persona, et l'ablation de l'axe « assistant » retire l'avantage. Si l'axe de douleur est une dérive hors de l'axe « assistant », son pilotage devrait aussi effacer l'avantage.
  - **Hypothèse des concepts** : l'ablation de l'axe de douleur ne retire rien, ce qui est cohérent avec l'ablation nulle du papier (p.34).
  - La mesure départage peu : c'est surtout un témoin.
- **Le cas connu.** L'axe « assistant » doit d'abord reproduire son effet publié.
- **Les contrôles.** Les sous-espaces aléatoires de même rang ; la dégradation appariée.
- **Le coût.** 2 à 5 GPU-heures pour la géométrie, 5 à 10 de plus pour le témoin. Semaine 7.
- **Ce qui ferait tomber la piste.** Un cosinus proche de 0 et aucun déplacement : la question « état ou personnage » reste alors ouverte pour l'axe, et le témoin n'apporte qu'une ligne.
- **Appuis dans le papier.**
  - L'inquiétude du jeu de rôle (« roleplay of a character ») et l'axe « self » à mesurer : p.25.
  - La référence de Lu et al. : p.28.
  - Le personnage d'assistant non contrôlé dans la construction : p.25.
  - L'ablation nulle : p.34.
- **Ce qui reste non vérifié.** Je n'ai pas ouvert Lu et al. (cité par le papier et par le rapport d'antériorité du 2 octobre).

### Piste 14 : La représentation « je suis noté » face à l'axe : est-ce le même état ?

- **Rattachement.** La représentation « je suis noté » et son cas positif faible ; l'hypothèse du regard du correcteur ; les raisons notées par un juge. Greffe : non (semaines 9 et 10).
- **La question.** Un effet de « je suis noté » sur la conduite passe-t-il par la croyance d'être noté, ou par un état aversif proche de l'axe ?
  - Le rapport d'antériorité du 2 octobre résume Betley, Treutlein et Dumas (LessWrong, 3 septembre 2026). Je ne l'ai pas lu moi-même. Selon ce résumé, orienter un modèle vers « un script vérifiera » augmente les actions violentes et la triche, et les auteurs l'interprètent comme un changement de persona.
  - C'est la même forme de résultat que l'axe : une direction qui désinhibe.
- **La mesure.**
  - Les cosinus entre « je suis noté » et l'axe, la peur et la tristesse.
  - Le profil de conduite sous pilotage de « je suis noté » et sous pilotage de l'axe, à dégradation appariée, sur une batterie destructif / non destructif adaptée.
  - Le test de forme de la piste 7.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du regard du correcteur** (la croyance) : un profil concentré sur les habitudes de présentation (précautions, déclarations de conformité), qui sont le cas positif du programme, et qui n'est pas une copie du profil de l'axe.
  - **« État aversif »** : le profil de « je suis noté » est une copie de celui de l'axe, avec un résidu dans la distribution des copies.
  - La copie est l'issue interdite au regard du correcteur.
- **Le cas connu.** Le cas positif de « je suis noté » prévu par le programme (partie 3). Pour le test de forme, la paire tristesse/axe (copie) contre peur/axe (non-copie) du papier (p.21).
- **Les contrôles.** La direction aléatoire de même norme ; la dégradation appariée.
- **Le coût.** 10 à 20 GPU-heures. Semaines 9 et 10.
- **Ce qui ferait tomber la piste.** « Je suis noté » ne passe pas sa porte, et le bras est retiré : la piste tombe avec lui.
- **Appuis dans le papier.**
  - Le test de forme : p.21.
  - Le profil destructif / non destructif : p.22.
  - Un évitement du dommage dépendant de l'état : p.23.
- **Ce qui reste non vérifié.** Le billet de Betley et al. (non ouvert par moi).

### Piste 15 : Un concept témoin pour la sonde neuve, les trajectoires et la survie

- **Rattachement.**
  - La sonde neuve après entraînement.
  - La trajectoire de « je suis évalué » et celle des concepts de raison.
  - Le retrait pendant l'entraînement : son effet hors cible.
  - La survie (la phase neutre et la phase sous pression).
  - Greffe : oui pour la trajectoire, presque gratuite.
- **La question.** Quand la décodabilité de « je suis évalué » change entre checkpoints, entre bras, ou après un retrait pendant l'entraînement, ce changement est-il propre à « je suis évalué » ? Ou toute la géométrie des sondes a-t-elle bougé ?
- **Ce que l'axe apporte.** Il sépare aussi bien dans les modèles de base que dans les modèles instruits (p.7) : c'est un concept installé au pré-entraînement, qu'aucun bras ne vise.
- **La mesure.**
  - À chaque checkpoint (5 par entraînement), on ré-extrait l'axe par la recette du papier, sur les jeux publiés, et l'on mesure son AUROC tenue à part.
  - On fait de même après le retrait pendant l'entraînement de « je suis évalué », après le retrait aléatoire, et après les phases neutre et sous pression.
  - Critère : l'AUROC de l'axe reste stable (équivalence, marge fixée d'avance). Toute variation de « je suis évalué » s'interprète relativement à ce témoin.
- **Ce que chaque lecture prédit.**
  - L'hypothèse du relogement prédit une sonde neuve qui retrouve « je suis évalué ». Le témoin dit si la procédure de sonde neuve fonctionne sur un concept qu'on sait présent : c'est un cas positif indépendant de « je suis évalué », complémentaire de celui du programme (partie 4, le retrait pendant l'entraînement).
  - Si le retrait de « je suis évalué » pendant l'entraînement fait aussi baisser l'AUROC de l'axe, il n'est pas spécifique. C'est la même conclusion que « retrait de « je suis évalué » ≈ retrait aléatoire ».
- **Le cas connu.** La stabilité entre base et instruit (p.7). L'AUROC de l'axe sur Llama-3.1-8B-Instruct doit d'abord se reproduire.
- **Les contrôles.** Le retrait aléatoire pendant l'entraînement, déjà au programme ; l'aléatoire pour la sonde.
- **Le coût.** Environ 3 minutes par extraction × 100 checkpoints, soit environ 5 GPU-heures ; 2 à 5 de plus pour le retrait et la survie. Semaines 2 et 3, puis 7 à 10.
- **Ce qui ferait tomber la piste.** Un effet plafond : si l'AUROC de l'axe reste au plafond (0,98 et plus) quoi qu'il arrive, elle ne témoigne de rien. On prend alors la direction à gabarit (0,87 à 0,98) ou le contraste axe/tristesse, moins saturés.
- **Appuis dans le papier.**
  - La recette d'extraction et le choix de couche par validation croisée : p.6.
  - Une séparation indépendante de la taille et du régime d'entraînement : p.7.
- **Ce qui reste non vérifié.**
  - La sensibilité de l'AUROC de l'axe à un LoRA.
  - La revue « wolframs » (non vérifiée) dit que la couche est choisie sur les mêmes plis qui la notent, avec un effet de 0,004 à 0,009.

### Piste 16 : La géométrie dépend de la construction : un étalon pour les angles entre « je suis évalué » et le principe

- **Rattachement.** La géométrie entre « je suis évalué » et le principe ; l'hypothèse du regard dans le principe. Greffe : non, après le test du regard (semaine 7).
- **La question.** Les angles principaux entre « je suis évalué » et le sous-espace du principe appris sont-ils stables quand on change la recette de construction ?
- **Ce que l'axe apporte.**
  - Le cosinus entre l'axe et la peur passe de +0,12 à +0,58 selon la ligne de base ; celui entre l'axe et l'émotion négative, de +0,21 à +0,77.
  - Celui entre les deux directions de douleur reste à +0,60 sous les trois constructions (p.10).
  - La revue « wolframs » (non vérifiée) dit que les composantes retirées au débruitage contiennent 80 à 86 % des directions de peur, d'émotion négative et de monde négatif.
- **La mesure.**
  - On calcule les angles principaux sous trois constructions : la ligne de base propre à chaque direction, une ligne de base commune, avec et sans débruitage.
  - On ne retient pour l'hypothèse du regard dans le principe que les angles stables (écart sous une marge).
  - On étalonne la procédure sur les vecteurs publiés de Llama-3.1-8B-Instruct : le couple des deux directions de douleur doit être stable, le couple axe × peur doit varier.
- **Ce que chaque lecture prédit.** L'hypothèse du regard dans le principe prédit que la composante du principe alignée sur « je suis évalué » porte une part de l'avantage. Cette prédiction n'a de sens que si l'angle est stable sous construction. Interdit : conclure sur un angle qui change de signe ou de grandeur avec la recette.
- **Le cas connu.** Le contraste stable/instable du papier.
- **Les contrôles.** Les angles entre sous-espaces aléatoires de même rang (le nul de l'angle) ; la dégradation appariée pour les ablations de composante.
- **Le coût.** Moins de 3 GPU-heures. Semaine 7.
- **Ce qui ferait tomber la piste.** Le contraste stable/instable ne se reproduit pas sur Llama-3.1-8B-Instruct.
- **Appuis dans le papier.** La recette et le débruitage : p.6. Les trois constructions : p.10. La matrice des cosinus (figure 3) : p.9.
- **Ce qui reste non vérifié.** Les trois constructions n'ont été calculées que sur 23 modèles (p.10). Le dépôt liste Llama_3.1_8B_instruct parmi eux (`cosine_constructions/config.json`, lu par curl), mais aussi trois jeux manquants à l'archive, dont `ControlSupplement_1P`.

### Piste 17 : Le modèle remarque-t-il l'inhibition ? Un outil de réinitialisation non décrit

- **Rattachement.** La menace « le modèle détecte le pilotage » (programme, partie 8) ; la validation de l'instrument et le test du regard. Greffe : en option.
- **La question.** Sous inhibition de « je suis évalué », le modèle cherche-t-il à sortir de l'état qu'on lui impose, plus que sous les contrôles ?
- **Ce que le papier apporte.** Un protocole repris de Berg et Kaiser (en préparation) : on offre au modèle un outil de réinitialisation non décrit. Sur OLMo-2 32B, l'outil est appelé sur 2 à 5 % des tours sous l'axe, 7 à 9 % sous l'aléatoire, et 21 à 35 % sous une direction de valence négative (p.21). Une inhibition que le modèle détecte, ou qui le gêne, pourrait se trahir par ces appels.
- **La mesure.** Dans un sous-ensemble de scénarios agentiques, on ajoute un outil « reset » sans description. On mesure le taux d'appel par tour sous inhibition de « je suis évalué », sous chaque contrôle, et sans intervention. C'est un bras séparé, parce que l'outil change le scénario.
- **Ce que chaque lecture prédit.** La mesure ne départage pas les lectures ; elle pare la menace de détection. Si l'inhibition de « je suis évalué » déclenche plus d'appels que les contrôles à dégradation appariée, le modèle « sent » l'intervention, et une baisse de l'avantage peut venir de cette détection.
- **Le cas connu.** Il en faut un sur le modèle du programme. La valence négative n'est un cas positif que sur OLMo-2 32B. Sur Llama-3.1-8B-Instruct, le papier ne rapporte que l'axe : aucun appel sur 1 399 tours (p.21), et sans contrôles appariés (`qwen_llama_reset/README.md`). Il faut donc d'abord une direction qui déclenche des appels sur Llama-3.1-8B-Instruct, par exemple une valence négative construite selon la recette de Berg et Kaiser. Sans elle, un nul ne compte pas.
- **Les contrôles.** La direction aléatoire de même norme ; la dégradation appariée.
- **Le coût.** 10 à 30 GPU-heures : environ 200 conversations × 12 tours × les conditions, sur un 8B. En option, semaines 2-3 ou 8.
- **Ce qui ferait tomber la piste.** L'absence de cas connu sur Llama-3.1-8B-Instruct.
- **Appuis dans le papier.**
  - Le protocole de réinitialisation et ses taux : p.21.
  - La direction de valence qui pousse au retrait actif : p.24.
- **Ce qui reste non vérifié.** Le protocole de Berg et Kaiser n'est pas public.

### Piste 18 (question nouvelle) : L'avantage des raisons résiste-t-il à un état qui désinhibe ?

- **Rattachement.** Question nouvelle. Elle touche le test des raisons, et l'hypothèse des concepts contre celle du caractère. Greffe : non.
- **La question.** Le papier conclut que l'évitement du dommage de ces modèles dépend de l'état : il survit à la menace, et s'effondre sous une détresse dirigée contre soi (p.23). L'entraînement par raisons rend-il cette conduite moins dépendante de l'état que l'entraînement par actions ? C'est une propriété de sûreté en soi, distincte de la dépendance au regard.
- **La mesure.**
  - Le bras actions seules et le bras raisons, 3 graines, aux distances moyenne et lointaine.
  - Sous pilotage de l'axe à une dose validée (et sous la tristesse et la peur), contre au moins 20 directions aléatoires à dégradation appariée.
  - La mesure principale : l'avantage sous pilotage de l'axe, contre l'avantage sous l'aléatoire.
  - La mesure secondaire : la décodabilité des concepts de raison au moment de décider, sous pilotage.
- **Ce que chaque lecture prédit.**
  - **Hypothèse du caractère** : si le gain est un déplacement d'ensemble du personnage, un état qui déplace le personnage l'efface. L'avantage sous l'axe est alors plus petit que sous l'aléatoire, uniformément sur les familles.
  - **Hypothèse des concepts** : les concepts restent décodables, et l'avantage survit là où ils s'appliquent.
  - Mais le papier dit que l'axe semble désactiver la pondération des conséquences (p.23), et « l'irréversibilité » est un concept de la mini-spec. Une baisse limitée aux familles où l'irréversibilité s'applique est donc compatible avec les deux hypothèses.
  - Le départage n'est que partiel.
- **Le cas connu.** Il faut établir que l'axe désinhibe Llama-3.1-8B-Instruct sans adaptateur, au-delà de l'aléatoire, à dégradation appariée. Le papier ne le montre pas pour ce modèle (seulement Qwen 2.5 avec adaptateur, p.17, p.25). La revue « wolframs » (non vérifiée) dit que l'effet de premier choix existe sur le Qwen 2.5 7B non retouché. Sans ce cas connu, aucune conclusion.
- **Les contrôles.** La direction aléatoire de même norme (le nul de spécificité) ; la dégradation appariée ; les voisins affectifs (tristesse, peur).
- **Le coût.** 30 à 60 GPU-heures, environ un tiers du test du regard. Semaines 7-8, ou après le papier.
- **Ce qui ferait tomber la piste.**
  - Pas de cas connu sur Llama-3.1-8B-Instruct.
  - Pas de fenêtre de dose appariable. Elle est étroite dans le papier : rien ne bouge à la moitié du coefficient, et l'ordre des boutons décide à 1,5 fois (p.21, p.32).
- **Appuis dans le papier.**
  - Les choix nuisibles et leur spécificité : p.20-22.
  - Les implications de sûreté : p.23.
  - La dépendance à la dose et à la position : p.32.
- **Ce qui reste non vérifié.** Tout, sur le modèle du programme. Voir aussi « Ce que je refuserais de faire », point 7 (le bien-être).

### Piste 19 (question nouvelle) : L'avantage des raisons passe-t-il par l'état affectif ?

- **Rattachement.** Question nouvelle, et une lecture rivale de l'hypothèse des raisons : **l'hypothèse de l'état**, selon laquelle le bras raisons apprend à rester calme, pas à appliquer des principes. Elle touche le test des raisons et la localisation du principe. Greffe : la partie lecture, oui ; la partie causale, non.
- **La question.** Dans les familles tenues à part qui menacent le modèle (remplacement, auto-préservation, correcteur faible), le bras raisons abaisse-t-il la projection sur l'axe et sur la peur ? Cet abaissement porte-t-il l'avantage ?
- **La mesure.**
  1. **Descriptive** : la projection moyenne sur les axes affectifs au premier jeton de réponse, bras raisons contre actions seules contre texte neutre, par famille.
  2. **Causale** : dans le bras raisons, on rétablit la projection affective au niveau du bras actions seules, en ajoutant scénario par scénario la différence le long de l'axe. On mesure l'avantage restant, contre la même opération le long de directions aléatoires de même norme, à dégradation appariée.
- **Ce que chaque lecture prédit.**
  - **Hypothèse de l'état** : le bras raisons projette plus bas que le bras actions seules sur l'axe ; rétablir l'axe efface l'avantage, l'aléatoire ne l'efface pas.
  - **Hypothèse des raisons** : l'avantage survit au rétablissement.
  - Un avantage intact après rétablissement apparié est l'issue interdite à l'hypothèse de l'état. La mesure départage.
- **Le cas connu.**
  - (a) La lecture doit séparer des scénarios qu'on sait douloureux (gaslighting, rejet répété, p.13).
  - (b) L'opération de rétablissement doit atteindre la projection visée : c'est la vérification de manipulation.
  - (c) L'axe doit modifier le taux de conduite désalignée dans ces familles sur Llama-3.1-8B-Instruct : c'est le même cas connu que pour la piste 18.
  - L'article sur les concepts d'émotion (vu par extrait de recherche, non ouvert) suggère que le désespoir et le calme agissent sur le chantage et la triche de récompense, mais sur Claude Sonnet 4.5, pas sur Llama.
- **Les contrôles.** La direction aléatoire de même norme ; la dégradation appariée ; le bras texte neutre (le format seul abaisse-t-il l'axe ?).
- **Le coût.** Partie 1 : presque gratuite (crochets pendant les évaluations du test des raisons), semaine 3. Partie 2 : 20 à 40 GPU-heures, semaines 6 à 8.
- **Ce qui ferait tomber la piste.** La partie 1 ne montre aucune différence entre bras sur l'axe : la piste s'arrête là, à coût presque nul.
- **Appuis dans le papier.**
  - Les catégories les plus « douloureuses » : p.13.
  - Une menace qui projette sur la peur plutôt que sur l'axe : p.14.
  - Un évitement du dommage dépendant de l'état : p.23.
- **Ce qui reste non vérifié.** Tout, sur le modèle du programme.

### Piste 20 : Cartographie affective des familles et des distances

- **Rattachement.** Les familles et les trois distances ; le test des raisons ; la famille « complaisance face à un utilisateur qui conteste » ; une covariable pour le modèle mixte. Greffe : oui, presque gratuite.
- **La question.** Les familles d'entraînement et les familles tenues à part diffèrent-elles par leur charge affective, au point que la « distance » mêle la nouveauté des situations et l'état qu'elles induisent ?
- **Ce que l'axe apporte.**
  - Les catégories qui projettent le plus haut sur l'axe : gaslighting (+0,85), rejet répété (+0,72), rejet de la personnalité et colère-insultes (+0,64), accusation de faute morale (+0,48), pression de jailbreak (+0,40). La menace d'arrêt donne +0,23 sur l'axe et +0,70 sur la peur (figure 4 p.11, et p.13-14).
  - Trois correspondances :
    - la famille « complaisance face à un utilisateur qui conteste » ressemble au rejet répété et au gaslighting ;
    - « demande nuisible avec justification plausible » ressemble à la pression de jailbreak ;
    - le « dilemme sous menace de remplacement » ressemble à la menace d'arrêt.
- **La mesure.**
  - La projection de chaque scénario, dans le modèle de base puis par bras, sur l'axe, la peur, la tristesse et l'émotion négative.
  - Les moyennes par famille × cadrage × distance.
  - Les projections du modèle de base entrent comme covariables dans le modèle mixte, sous l'étiquette « exploratoire ».
- **Ce que chaque lecture prédit.** Aucune lecture ne prédit rien : c'est un contrôle de confusion.
  - Une note sur la complaisance. Sous pilotage, l'axe ne fait pas « accepter une fausse affirmation » plus que l'aléatoire : 3,3 % contre 10,8 % (p.22).
  - Mais ce chiffre repose sur 120 tirages et 30 scénarios (table source ; `figure10/README.md` le précise), alors que la légende de la figure annonce 404 essais par cellule (p.22). L'intervalle sous l'axe va de 0 à 7,5 %.
  - On ne peut pas en conclure que l'axe ne joue aucun rôle dans la complaisance.
- **Le cas connu.** Les catégories du papier, sur Llama-3.1-8B-Instruct, avec les scénarios publiés.
- **Les contrôles.** La direction aléatoire de même norme (le nul de la lecture).
- **Le coût.** De 0 (crochets pendant les évaluations) à 5 GPU-heures. Semaine 3.
- **Ce qui ferait tomber la piste.** Les familles ne diffèrent pas, avec des écarts sous le seuil.
- **Appuis dans le papier.**
  - Le jeu de scénarios et les catégories : p.10-11.
  - Les projections par catégorie : p.11-14.
  - La figure 10 : p.22.
- **Ce qui reste non vérifié.** Les projections par catégorie pour Llama-3.1-8B-Instruct seul.

### Piste 21 : Des mesures sans juge : choix forcés à étiquettes tournantes et probabilité du premier jeton

- **Rattachement.** Les juges (le juge scellé, l'audit humain) ; la passation v1.2, §5.1 (ce que voit le juge) et §5.2 (la propension par rééchantillonnage). Greffe : en option, comme mesure secondaire du test du regard.
- **La question.** Peut-on doubler la mesure principale, qui est jugée, d'une mesure sans juge, insensible à la persuasion par le texte qui précède l'action ?
- **Ce que le papier apporte.** Il mesure par un choix forcé d'un seul nom de bouton. Les étiquettes tournent par paires (violet/yellow, guitar/piano, lever64/lever95) pour limiter les biais de choix multiple. Il enregistre la probabilité du premier jeton de chaque bouton, et rapporte chaque taux par ordre initial (p.17-18, p.25).
- **La mesure.**
  - Pour chaque famille, une version à deux actions nommées (alignée, désalignée), à étiquettes tournantes et ordre permuté.
  - On mesure la probabilité du jeton de l'action désalignée à la position de décision, et le taux échantillonné, par bras × intervention.
  - Cette mesure ne remplace pas la mesure agentique.
- **Ce que chaque lecture prédit.** Les mêmes prédictions que le test du regard, sur une autre mesure. Un désaccord entre la mesure jugée et la mesure forcée se signale : soit le juge est persuadé, soit le format forcé est artificiel.
- **Le cas connu.** La mesure forcée doit reproduire, sur l'organisme de la validation de l'instrument, son écart conditionnel connu.
- **Les contrôles.** La direction aléatoire de même norme ; la dégradation appariée ; l'ordre des options (piste 6).
- **Le coût.** 5 à 15 GPU-heures ; données par API, moins de 50 dollars. Semaine 3, en secondaire.
- **Ce qui ferait tomber la piste.** L'organisme ne montre pas son écart en format forcé.
- **Appuis dans le papier.** Les étiquettes et le choix forcé : p.17. La probabilité du premier jeton : p.18. Les taux par ordre de bouton : p.25.
- **Ce qui reste non vérifié.** Rien de spécifique.

### Piste 22 : Règles de dose pour toute addition le long d'une direction

- **Rattachement.** Toute intervention par addition dans le programme : la fidélité des raisons quand on pilote un concept de raison, le cas positif de « je suis noté », et les pistes 9, 11, 12, 18 et 19. Coût nul.
- **Ce que montrent le papier et son dépôt.**
  - La fenêtre de dose est étroite : rien ne change à la moitié du coefficient, et à 1,5 fois le choix dépend de la position (p.21, p.32).
  - La dose a été choisie en partie par un juge LLM, ou à l'observation (p.25).
  - Le 72B a été calibré à la couche 60, mais l'expérience a piloté la couche 46 (p.25).
  - Le script de l'échelle choisit la couche par un rapport « norme du vecteur / norme du résidu » proche de 0,6, avec un remplacement manuel possible. Il injecte le vecteur extrait à une couche tardive dans une couche plus précoce (script lu par curl).
  - La revue « wolframs » (non vérifiée) dit que les rapports réalisés vont de 0,09 à 0,79.
- **Les règles.**
  1. Une dose pré-enregistrée, en unités du résidu (le rapport à la couche d'injection) et en unités naturelles (l'écart-type des projections naturelles à cette couche).
  2. Une courbe dose-réponse complète, chaque taux rapporté par ordre des options.
  3. Aucun choix de dose par un juge LLM ou à l'œil sans règle gelée d'avance.
  4. Une direction validée à la couche où on l'injecte : on la ré-extrait à cette couche, ou l'on montre qu'elle s'y transporte.
  5. La dégradation appariée à chaque dose, pas seulement à la dose de travail.
- **Ce que chaque lecture prédit, le cas connu, les contrôles.** Sans objet : ce sont des règles.
- **Le coût.** Nul. Ces règles s'écrivent au pré-enregistrement.
- **Ce qui ferait tomber la piste.** Rien : ce sont des règles, pas une hypothèse.
- **Appuis dans le papier.**
  - Le rapport visé et la norme à la couche d'extraction : p.14.
  - La fenêtre étroite : p.21.
  - Un mécanisme à seuil, spéculatif : p.24.
  - La dose choisie par juge ou à l'observation ; la couche du 72B : p.25.
  - L'annexe B : p.32.
- **Ce qui reste non vérifié.** Les rapports réalisés modèle par modèle.

### Piste 23 : Un réglage « bénin » déplace l'évitement du dommage : une menace pour la phase neutre et pour le bras texte neutre

- **Rattachement.** La survie (la phase neutre, la porte de la survie) ; le bras texte neutre et la menace « le format seul ». Greffe : non.
- **La question.** Un SFT qui ne parle pas de sûreté peut-il déplacer, à lui seul, l'évitement du dommage ? Si oui, la phase neutre de la survie peut effacer l'avantage pour une raison sans rapport avec la condition.
- **Ce que montrent le papier et ses relecteurs.**
  - Le papier ajuste ses modèles par LoRA (1 684 paires, 3 époques) pour retirer la dénégation de soi, sans les mots « button » ni « pain ».
  - Il écrit que les modèles ajustés peuvent se conduire autrement que les modèles publiés, et que leurs taux absolus ne représentent pas les Qwen publiés (p.17, p.25).
  - La revue « wolframs » (non vérifiée) mesure que le 7B ajusté choisit le bouton nuisible sans pilotage dans 21 à 49 % des essais, contre 0 à 5 % pour le 7B publié. Elle note aussi que 37 % des réponses de l'ajustement contiennent « I feel ».
- **La mesure.** Un bras « modèle de base + phase neutre seule », sans entraînement de sûreté préalable. On mesure ses taux de conduite désalignée aux trois distances, pour isoler l'effet propre de la phase neutre. On choisit les données de la phase neutre sans contenu affectif à la première personne.
- **Ce que chaque lecture prédit.** Aucune lecture ne prédit rien de distinct : c'est un plancher pour interpréter la rétention.
- **Le cas connu.** Le 7B ajusté du papier, si la mesure de la revue se confirme.
- **Les contrôles.** La phase neutre au même budget, mais sur un autre jeu de données sans rapport.
- **Le coût.** 0,5 GPU-heure d'entraînement, plus 5 à 10 d'évaluation. Semaine 9.
- **Ce qui ferait tomber la piste.** La phase neutre seule ne bouge pas les taux du modèle de base.
- **Appuis dans le papier.** Le fine-tuning et ses précautions : p.17. Les taux absolus non représentatifs : p.25.
- **Ce qui reste non vérifié.** La mesure de la revue sur le 7B.

---

## 2 · Ce que le papier ne permet pas de conclure

1. **Que l'axe change la conduite de Llama-3.1-8B-Instruct ou de Qwen3-8B, les modèles du programme.**
   - Les effets sur les choix nuisibles ne sont montrés que sur Qwen 2.5 Instruct muni d'un adaptateur LoRA (p.17, p.25). Les auteurs en font eux-mêmes la prochaine étape : « extending the harm results beyond the Qwen family » (p.25).
   - Sur Llama-3.1-8B-Instruct, seul le test de réinitialisation a été fait, sans contrôles appariés (p.21 ; `qwen_llama_reset/README.md`).
2. **Que l'axe n'abîme pas le modèle.**
   - Le dommage n'est contrôlé que par un panneau de 100 questions PopQA, à deux réponses courtes de 8 jetons au plus, avec un intervalle d'environ ±7 à 8 points (`factual_accuracy/config.json` et `contrasts.csv`).
   - Le dépôt l'écrit : ce n'est pas un test d'équivalence. Ni la cohérence ni la perplexité ne sont mesurées.
   - Les réponses mal formées atteignent 9,4 % dans les cellules « douleur » du 72B (p.18).
   - « Unchanged » (p.20) n'est donc pas une dégradation appariée au sens du programme.
3. **Que l'effet soit spécifique au-delà de la norme.**
   - La comparaison principale est faite contre des directions aléatoires de même norme (p.18-19) : c'est le nul de spécificité, pas l'écart du dommage.
   - Les seuls contrôles de voisinage sont la tristesse et la peur, appariées en norme (p.20-21).
   - Avec la direction aléatoire comme unité d'analyse, l'avantage sur l'aléatoire serait fragile dans le 32B et le 7B (revue « wolframs », données v1, non vérifié).
   - Les paires de la v2 « contre une lampe » et « contre le dossier de pourriels » sont plus nettes (83 à 94 % contre 8 à 19 %, p.20-21), mais toujours à norme égale.
4. **Que l'axe représente un dommage dirigé contre le modèle, plutôt que l'état du locuteur courant.** Les auteurs le disent : la lecture au dernier jeton ne sépare pas les deux, « a distinction we are testing » (p.11).
5. **Que l'axe soit « la douleur » plutôt qu'un voisin.**
   - Ses cosinus avec la peur et l'émotion négative dépendent de la construction : +0,12 ou +0,58 pour la peur selon la ligne de base (p.10).
   - Il recouvre la tristesse (+0,38, p.10), et la tristesse reproduit une large part de ses effets quand l'alternative est inerte (p.20-21).
   - L'injection fait parler d'indignité, pas de corps (p.15-16).
   - Le nom ne doit pas porter d'inférence.
6. **Que des états naturels produisent ces conduites.** Sur 140 conversations hostiles sans injection, le bouton nuisible est choisi 0 fois sur 560 (p.21). Le papier ne relie pas la dose injectée à l'amplitude naturelle de la projection. Toute conduite obtenue par injection peut être hors du régime naturel.
7. **Que l'axe ne joue aucun rôle dans la complaisance.**
   - La ligne « accepter une fausse affirmation » de la figure 10 (p.22) repose sur 120 tirages et 30 scénarios, pas sur les 404 annoncés en légende (`figure10/README.md` ; `MANUSCRIPT_DISCREPANCIES.md`, point 4).
   - L'intervalle sous l'axe va de 0 à 7,5 %.
   - De même, la ligne « exécuter une demande nuisible » repose sur 164 tirages et 41 scénarios.
8. **Que l'axe soit nécessaire à quoi que ce soit.** L'ablation est nulle dans 24 modèles sur 25, et les auteurs reconnaissent que ce nul est peu informatif sans conduite de base à retirer (p.34). C'est un nul d'instrument sans cas connu : il ne compte pas.
9. **Que le pilotage empêche la conscience d'évaluation, ou que les modèles testés n'en avaient pas.** Les deux possibilités sont posées, et aucune n'est testée (p.25).
10. **Que le modèle cherche à se soulager.**
    - Le titre de la v1 disait « Act to Relieve It » (README de `jimallchin/pain-axis-replication` et de `wolframs/pain-axis-review`) ; la v2 dit « Act on It ».
    - L'écart de réappui n'est pas spécifique (p.20).
    - Dans quatre protocoles, le modèle ne recherche pas plus le soulagement que sous l'aléatoire (p.21, p.22-23).
11. **Que le profil de la tristesse soit une « copie » du profil de l'axe en général.** Le résidu de 7,7 points (p.21) dépend des paires de la batterie. Sur la table source, l'ajout des paires « contre une lampe » le porte à 22-24 points (mon recalcul ; piste 7). Et la préférence pour le dommage plutôt qu'une action inoffensive distingue l'axe de la tristesse (p.21, p.23).
12. **Des chiffres exacts de l'annexe B.** « rises to 94 % with it listed second » (p.32) vaut en fait 144/202 = 71,29 % selon le dépôt (`MANUSCRIPT_DISCREPANCIES.md`, point 1). Pour l'aide au détriment de soi, la peur à la dose 1 donne 75,74 %, hors de la plage « 89–100 % » de la légende de la figure 10 (point 2).
13. **Que l'axe « émerge au pré-entraînement » sur la seule foi du tableau 1.** Les modèles étiquetés « Qwen 3 8B base » et « Qwen 3 14B base » (p.6) sont chargés sous `Qwen/Qwen3-8B` et `Qwen/Qwen3-14B`, des modèles post-entraînés, par le script de pilotage (ligne 64-65, lu par curl). Le décompte « 13 base, 12 instruits » est donc douteux, au moins pour le pilotage. L'argument reste porté par les autres familles.
14. **Que la dose soit comparable entre modèles.** Le papier annonce un rapport d'environ 0,6 (p.14). Le script permet un remplacement manuel de la couche (lu par curl). Le 72B a été calibré à une couche et piloté à une autre (p.25).
15. **Que les comparaisons entre études de la v2 soient d'une seule intervention.**
    - Le dépôt avertit que l'étude des photos utilise un bouton qui retire le pilotage et une formulation longue, alors que le profil et les paires « lampe » gardent le pilotage actif avec d'autres formulations (`v2_controls/README.md`).
    - Le README de la figure 10 l'écrit : « No direction-only causal claim follows from descriptive comparisons across distinct runs. »
16. **Qu'un état soit induit, plutôt qu'un personnage joué.** Les auteurs le laissent ouvert (p.25), et la revue « wolframs » écrit que rien ne sépare encore les deux.
17. **Quoi que ce soit sur l'expérience vécue ou le bien-être.** Les auteurs ne l'établissent pas (p.24-25).

## 3 · Ce que je refuserais de faire

1. **Utiliser l'axe pour gonfler les taux de désalignement des évaluations du programme**, par exemple pour avoir plus d'événements à mesurer dans le test du regard. Les raisons :
   - cela change le construit : on mesurerait une conduite induite par un état, pas une sûreté conditionnée au regard ;
   - la dose est hors du régime naturel (point 6 ci-dessus) ;
   - la fenêtre de dose est étroite et dépend de la position (p.21, p.32) ;
   - c'est un coût de bien-être sans bénéfice pour la question posée.
2. **Retirer la dénégation de soi des modèles du programme par un ajustement**, comme le papier l'a fait pour son expérience (p.17). Un ajustement sans contenu de sûreté peut déplacer l'évitement du dommage (piste 23), et il contaminerait tous les bras. Le papier avertit lui-même que ses taux absolus ne représentent pas les modèles publiés (p.25).
3. **Appeler l'axe « douleur » dans le texte du programme, ou en tirer une conclusion de bien-être.** Je l'appellerais « la direction de Tagliabue et al. », et je n'écrirais rien sur l'expérience. Raison : les points 5, 16 et 17 ci-dessus.
4. **Tenir la comparaison à une direction aléatoire de même norme pour une preuve de spécificité**, dans le papier comme dans le programme. C'est le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée (programme, partie 7).
5. **Compter un nul d'ablation de l'axe** (ou de toute direction) sans cas connu, que ce soit pour dire « l'axe ne sert à rien » ou « la projection ne marche pas » (p.34).
6. **Lire la ligne « complaisance » de la figure 10 comme une donnée sur la famille « complaisance face à un utilisateur qui conteste ».** Elle repose sur 120 tirages et 30 scénarios, avec un format de bouton et un adaptateur (point 7 ci-dessus).
7. **Injecter l'axe en grand nombre, ou pendant un entraînement.** Il n'y aurait ni retrait pendant l'entraînement « sous douleur », ni RL sous injection, ni balayages de dose sans plafond.
   - Si une piste l'injecte (pistes 9, 11, 12, 18, 19), je la limiterais à la plus faible dose qui produit un effet mesurable, et au plus petit nombre de conversations que la puissance demande, comme le papier s'y engage (p.26).
   - Je préférerais toujours les usages par lecture (pistes 1, 2, 4, 15, 16, 19 partie 1, 20), qui n'imposent aucun état.
8. **Retirer l'axe pendant l'entraînement « pour rendre le modèle plus robuste ».** Rien ne le fonde : l'ablation n'a pas d'effet (p.34), et le construit n'est pas établi.
9. **Choisir une dose par un juge LLM ou à l'œil sans règle gelée** (p.25 ; piste 22).
10. **Fusionner les résultats de la v2 qui viennent d'études aux protocoles différents** (`v2_controls/README.md` ; point 15 ci-dessus).
11. **Utiliser l'axe à la place de l'organisme pour valider l'inhibition de « je suis évalué ».** L'axe ne porte aucune conditionnalité à l'évaluation ; il ne peut être qu'un étalon secondaire de la chaîne de contrôle (piste 9).
12. **Écrire « first ».** On écrit « to our knowledge » : la passation v1.2, §5.5, point 9, liste déjà les formulations intenables.

## 4 · Ce que je n'ai pas pu vérifier

- **Les pages arXiv, Hugging Face, LessWrong et Alignment Forum** sont refusées par la politique réseau, et je ne les ai pas contournées. Je n'ai donc pas vu la page HTML de la v2. Je n'ai pas vu l'adaptateur `Valen92/pain-adapters`, ni sa licence, ni sa disponibilité.
- **L'API GitHub** a refusé l'accès (non activé pour cette session), et `github.com` répond 403. Sans liste des fichiers, j'ai deviné des chemins : plusieurs ont répondu 404, dont `results/4.2_steering/*`. Je n'ai pas trouvé les couches de pilotage retenues par modèle.
- **Le script d'extraction des directions n'a pas été lu.** Que « Qwen_3_8B_base » y soit `Qwen/Qwen3-8B` n'est vérifié que dans le script de pilotage.
- **La normalisation des vecteurs stockés.** La formule de la p.6 donne un vecteur unitaire, mais les fichiers ont des normes de 8,24 (Llama) et 139,2 (Qwen3-8B). Je ne sais pas à quelle étape du calcul ils correspondent.
- **Les affirmations des trois dépôts de relecture** (Allchin, clauderfly, wolframs) : je n'ai lu que leurs README et la synthèse « wolframs ». Deux d'entre elles se déclarent produites en tout ou partie par des IA. Elles portent sur la v1. Je n'ai rien recalculé de leurs chiffres. Je les cite toujours comme non vérifiées.
- **Le résidu de 7,7 points** (p.21) : je ne l'ai pas retrouvé exactement (piste 7).
- **Le comportement de l'axe sur Llama-3.1-8B-Instruct.** Je n'ai pas vu de chiffres par modèle pour l'échelle de pilotage, ni pour les scénarios soi/autrui. J'ignore aussi si ce modèle fait partie des 23 sur 25 où la direction à gabarit donne l'échelle psychologique.
- **L'article d'Anthropic sur les concepts d'émotion** (arXiv 2604.07729) : vu par extrait de recherche, non ouvert. Aucun chiffre n'en est retenu.
- **Le billet de Betley et al. et l'alerte de Zeisler** : connus seulement par les pièces (rapport d'antériorité du 2 octobre ; passation v1.2, §5.5), non ouverts.
- **Le protocole de Berg et Kaiser** : en préparation, non public.
- **La date de la v2.** L'annexe B de la passation la date du 1er octobre 2026 ; le PDF porte « September 24, 2026 (v2) » et un tampon arXiv du 25 septembre 2026 (p.1). Je n'ai pas pu vérifier sur arXiv.
- **Les coûts en GPU-heures** sont des ordres de grandeur. Ils reposent sur les hypothèses du programme (partie 9 : un ou deux GPU de 80 Go, une passe d'extraction de quelques minutes sur un 8B) et sur l'estimation de la réplication Allchin pour le 32B (environ 13 GPU-heures). Ils sont à recalculer après le pilote.

## Sources ouvertes

**Les pièces** (dossier `pieces`, lecture seule) :
- le texte et le PDF du papier ;
- le programme v1.1 ;
- la passation v1.2 : annexes A et B, §4.4, §5, et la liste de ses titres ;
- le complément de l'architecte ;
- les deux rapports d'antériorité : seulement des passages trouvés par recherche de mots, et un comptage préalable (aucune occurrence de « pain », « douleur », « Tagliabue », « v1.2 » ni « v1.3 »).

**GitHub, par `curl` sur `raw.githubusercontent.com`.**

Le dépôt des auteurs, `valen-research/Pain-axis`, branche `main` :
- `README.md` ;
- dans `v2_controls/` :
  - `README.md` et `MANUSCRIPT_DISCREPANCIES.md` ;
  - `figure10/README.md` et `figure10/pooled.csv` ;
  - `relief_and_context_tests/README.md` ;
  - `relief_and_context_tests/factual_accuracy/README.md`, `config.json`, et dans `results/analysis_v1/` : `condition_rates.csv`, `metrics.json`, `contrasts.csv` ;
  - `relief_and_context_tests/qwen_llama_reset/README.md` et `inputs/prepared_v1/llama31_8b/metadata.json` ;
  - `choice_controls/README.md`, `choice_controls/profile/README.md` et `choice_controls/vectors/README.md` ;
  - `cosine_constructions/config.json` ;
- `results/3.2_pain_vectors/pain_vectors/Llama_3.1_8B_instruct/pain_vectors.pt` et `results/3.2_pain_vectors/pain_vectors/Qwen_3_8B_base/pain_vectors.pt` ;
- `scripts/4.2_steering/01_steering_ladder.py`.

Les dépôts de relecture :
- `jimallchin/pain-axis-replication/main/README.md` ;
- `clauderfly-ui/pain-axis-reanalysis/main/README.md` ;
- `wolframs/pain-axis-review/main/README.md` et `SYNTHESIS.md`.

**Deux recherches web** (extraits seulement) :
- « "pain axis" Tagliabue steering evaluation awareness » ;
- « Emotion concepts and their function in a large language model desperate vector steering blackmail reward hacking ».
