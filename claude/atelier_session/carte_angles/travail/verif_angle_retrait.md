# Vérification : « angle : le retrait pendant l'entraînement » (`angle_retrait.md`)

Vérification sceptique, 2 octobre 2026. J'ai relu moi-même, sans me fier au fichier vérifié :
- rapports de la nuit : rapport 1 (l. 19-270, passages sur SPAR), rapport 2 (l. 271-485), rapport 3 (l. 486-726), rapport 4 (l. 727-1011), rapport 5 (passages sur Drake et Eberstadt, Persona Vectors), rapport 6 (l. 1255-1573), rapport 7 (l. 1574-1850) ;
- rapports du 1er octobre : les quatre axes (l. 11-489), en entier pour les axes de la conscience d'évaluation comme condition des gains, du test causal interne et de la combinaison exacte ;
- passation v1.2 : §3, §4 (4.1 à 4.4), §5.4, §5.5, §6 ; passation v1.0, §3 ; complément de l'architecte (partie ouverte) ; programme v1.1, tableau des travaux connexes (l. 80-108), calendrier (l. 733-745), règles de décision (l. 589-604) ;
- consignes de la nuit : en-tête, niveaux de danger, consigne de l'agent 3.

Six recherches WebSearch faites ce jour ; tout ce qui en vient est marqué « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre.

**Bilan.** Le fichier est solide sur l'essentiel : aucune erreur déjà corrigée au §4.3 n'est reprise (lieu d'*Eval Cooperativeness*, Wu et Tang, la card de Fable 5, Mody et al., le nombre de modèles de Santos-Grueiro, le lieu de CAFT sont tous au bon état) ; les chiffres cités ont une source et sont exacts ; aucune idée n'est désignée par un sigle ; « first » n'apparaît pas ; les citations font moins de quinze mots. Le verdict « partiellement pris ; application libre » suit le §4.4 (n° 5) et les rapports 3 et 6. Restent cinq corrections bloquantes (deux travaux présents dans les rapports et absents, une justification de formulation contredite par deux rapports, une liste d'arguments qui contredit le rapport 3, une date sans source), puis des corrections de statut, d'attribution et de niveau.

---

## Corrections bloquantes

### 1. Ajouter *Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers* (Dubiński … Evans, arXiv 2604.25891)
- **Où il est dans les rapports.**
  - Rapport du 1er octobre, axe raisons contre actions, n° 10 (l. 73-77) : URL `arxiv.org/html/2604.25891v1` donnée, donc texte intégral (HTML v1). Il y est décrit ainsi : les mitigations usuelles cachent le désalignement émergent aux évaluations standard ; il revient quand le prompt porte des indices du contexte d'entraînement ; ajouter de la chaîne de pensée à l'entraînement réduit ce désalignement conditionnel.
  - Rapport du 1er octobre, axe de la combinaison exacte, « Travaux non ouverts » (l. 472) : non ouvert.
  - Rapport 6, « Titres seuls » (l. 1514) : liste des articles acceptés, NeurIPS 2026 ; non ouvert.
  - Vu par extrait de recherche, non ouvert (2 octobre) : auteurs Dubiński, Betley, Sztyber-Betley, Tan, Evans ; avril 2026 ; les interventions étudiées seraient la dilution par des données bénignes, un fine-tuning après coup et l'inoculation par prompt.
- **Pourquoi c'est bloquant.** C'est le précédent publié de l'échec que l'angle teste : une mitigation, en partie appliquée pendant l'entraînement, qui rend une conduite conditionnelle à des indices au lieu de la retirer. Il touche aussi les raisons (la chaîne de pensée à l'entraînement réduit l'effet). Il manque à la liste des travaux, à la section « Ce qui reste libre » (fragilités) et à la liste « qui ne sont plus tenables » (avec la précision : indices de contexte d'entraînement, pas de représentation retirée).
- **Niveau proposé.** Au moins faible (l'axe raisons contre actions le dit « adjacent ») ; moyen pour la sous-question du ré-encodage, par cohérence avec BLOCK-EM, que le rapport 3 classe moyen pour cette sous-question.
- **À vérifier en relisant Nadaf.** La v1.1 (l. 89) et l'axe du test causal interne (l. 255) disent que la disposition de Nadaf « se reloge derrière un déclencheur » ; le rapport 3 dit seulement qu'elle se reforme dans le sous-espace vidé. La formule rappelle le titre de Dubiński : c'est une hypothèse à trancher sur la source, pas un fait.

### 2. Ajouter *Towards training-time mitigations for alignment faking in RL* (Gasteiger … Hubinger, Anthropic, Alignment Science Blog, 16 décembre 2025)
- **Où il est.** Rapport du 1er octobre, axe de la conscience d'évaluation comme condition des gains, n° 6 (l. 157-162) ; URL de la page donnée, mode de lecture non précisé (libellé prudent : résumé seul).
- **Ce que dit le rapport.** RL sur des organismes qui simulent l'alignement, puis mesure de l'écart de conformité entre surveillé et non surveillé, sur des prompts tenus à part ; mitigations testées : interrogation, pénalité de longueur, supervision de processus.
- **Pourquoi c'est bloquant.** C'est une mitigation, pendant l'entraînement, d'une conduite qui dépend du regard. Le fichier écrit que « première mitigation de la conscience ou du jeu d'évaluation pendant l'entraînement » n'est plus tenable et cite Li et Turner, Kretschmar, l'annexe O.4 et Lundqvist : ce travail, antérieur à tous sauf l'annexe O.4, manque à cette liste et à la liste des travaux.
- **Niveau proposé.** Faible à moyen, à fixer après lecture : aucune représentation retirée, aucune raison, mais la cible (l'écart surveillé contre non surveillé, réduit par l'entraînement) est la même famille que la coopérativité, que le fichier classe moyen.

### 3. La formulation tenable n° 3 et le projet de Lundqvist : la justification est contredite par les rapports 2 et 4
- **Le fichier** (l. 378-379) : la comparaison de l'ablation de concepts, de l'invariance aux indices et de la disposition coopérative serait tenable, car « aucun rapport ne signale une telle comparaison ».
- **Les rapports.**
  - Rapport 4 (l. 914-925, page lue en texte intégral) : le projet de Lundqvist annonce de « comparer des interventions plus profondes ou plus précoces face à la pression d'entraînement », en plus des adaptateurs d'inoculation, du pilotage préventif, d'une disposition coopérative, des mesures non verbalisées, de l'attribution de données et de l'auto-prédiction du modèle.
  - Rapport 2 (l. 422) : *Infohazard Evaluations* annonce de comparer des méthodes d'entraînement qui gardent la reconnaissance de l'évaluation et retirent son influence (description de la page seule).
- **Correction exigée.**
  - La justification devient : deux projets SPAR annoncent une comparaison de mitigations pendant l'entraînement (Lundqvist, rapport 4 ; Shi Feng et al., rapport 2) ; la formulation ne tient que par « on the same reason-trained models, at matched output degradation ». Citer les deux projets à côté.
  - Dans la fiche du projet de Lundqvist (l. 37-41), compléter les moyens annoncés : la comparaison d'interventions plus profondes ou plus précoces et l'auto-prédiction (rapport 4, texte intégral) ; la mesure de la conscience d'évaluation et du coût en capacités sous pilotage préventif (rapport 6). Seuls les moyens du §4.2 (n° 3) sont « relus sur la source » ; les autres restent « rapport 4 » ou « rapport 6 ».
  - Le verdict (l. 18-21) doit nommer ces deux inconnues : on ne sait pas si les « interventions plus profondes » de Lundqvist ou les méthodes d'*Infohazard Evaluations* incluent un retrait de représentation.
  - Même fiche, l. 44 : « Il annonce un retrait pendant le fine-tuning de ce qui porte le jeu d'évaluation, par pilotage préventif » surinterprète. Le §4.2 (n° 3) confirme des vecteurs de pilotage préventifs contre le jeu d'évaluation pendant le fine-tuning ; un pilotage préventif ajoute une direction, il ne la retire pas. Écrire : « une intervention sur les activations pendant le fine-tuning, par pilotage préventif ».

### 4. La liste « premier à montrer qu'un retrait pendant l'entraînement est contourné par ré-encodage » contredit le rapport 3 et le fichier lui-même
- **Le fichier** (l. 383-388) range Nadaf parmi les preuves (« re-formation, après des éditions post-hoc ») et Imran … Africa (« l'indice est tu, son influence reste »).
- **Nadaf.** Rapport 3 (l. 581-587, texte intégral) : la projection pendant tout le fine-tuning donne 0 % ; la re-formation est mesurée après les éditions post-hoc, « pas après le retrait pendant l'entraînement ». Le fichier le dit lui-même (l. 168 et contradiction n° 3, l. 411 : « l'analogie est trop forte »). Nadaf doit sortir de cette liste, ou y figurer comme contre-exemple : le retrait pendant l'entraînement n'y est pas contourné.
- **Imran … Africa.** Lu en résumé seulement (rapports 3 et 6) ; ce qui est tu est la verbalisation de l'indice, et rien ne dit qu'une représentation a été retirée (rapport 6, l. 1379). À garder seulement avec cette précision.
- **Restent valables** pour cette liste : *Routing Subspaces*, annexe I (rotation, relu, §4.2 n° 7) ; Santos-Grueiro (ré-encodage inféré, rapport 3) ; BLOCK-EM (détournement en amont sous fine-tuning prolongé, rapport 3). Dubiński … Evans s'y ajoute avec sa précision (correction n° 1).

### 5. La place du 19 décembre dans le calendrier du programme n'a pas de source
- **Le fichier** (l. 46) : « Des résultats sont possibles le 19 décembre, entre le post et l'arXiv du programme (semaines 4 et 11) ». C'est aussi la raison du rang « le plus dangereux à cause du calendrier » (l. 43).
- **Les pièces.** Les semaines 4 et 11 sont bien au §3, point 5 de la passation v1.2 ; le calendrier de la v1.1 (l. 745) met « rédaction, contre-lecture, prépublication » en semaines 11 et 12. Aucune pièce ne date le début de la semaine 1. Si elle commence la semaine du 5 octobre, la semaine 11 est celle du 14 décembre : le 19 décembre tombe dans la semaine de l'arXiv, pas avant.
- **Correction exigée.** Écrire ce qui est sourcé : recherche du 14 septembre au 14 décembre, démonstration le 19 décembre (FAQ de SPAR, rapport 6, l. 1450) ; le projet lui-même n'annonce aucune date (rapport 4, l. 924) ; une sortie est possible à tout moment avant. La position par rapport au post et à l'arXiv dépend de la date de départ de la semaine 1, à faire fixer par Lazar ; dans l'hypothèse d'un départ début octobre, la démonstration tombe dans la fenêtre de l'arXiv.

---

## Corrections non bloquantes

### 6. *Routing Subspaces* : niveau et attribution
- « Danger : moyen, proche de l'élevé pour une sous-question » (l. 69) : les consignes ne définissent que trois niveaux, par angle. Le rapport 3 dit moyen (l. 547) ; le rapport 2, moyen pour la validation sur organisme et faible pour la question centrale (l. 353). La formulation tenable n° 2 du fichier reste tenable sous réserve : l'élevé ne s'applique donc pas. Écrire « moyen », avec la raison (projection pendant le fine-tuning, puis rotation de la direction). Le classement (rang 2, après un travail « moyen ») devient alors cohérent.
- « traitée en annexe comme contrôle négatif (§4.2) » (l. 74) : le §4.2 (n° 7) confirme la cellule unique (Gemma-2-2B, sous-performance délibérée) ; « contrôle négatif » vient du rapport 3 (l. 550). Attribuer au rapport 3.
- Statut (l. 59-61) : ajouter le rapport du 1er octobre, axe de la combinaison exacte (URL HTML donnée, l. 383), source de « Tanyel » et de la « dégradation non appariée ».

### 7. Santos-Grueiro : le §4.3 fait foi sur les modèles
- Contradiction n° 1 (l. 402) : « Les deux réserves du rapport 7 restent ouvertes ». La première (le Llama donné « à titre d'exemple ») est close par le §4.3 : la v3 ajoute Llama-3.1-8B-Instruct ; le rapport 3 cite le journal de la v3 (« Added results for Llama », l. 556). Seule la question base ou modèle instruit (rapport 7, l. 1834) reste ouverte, le §4.3 ne la traitant pas.
- Dans la fiche (l. 105-114), dire les modèles : Qwen2.5-7B en 4 bits (v1), plus Llama-3.1-8B-Instruct en v3 (§4.3). C'est le modèle principal du programme : à écrire dans « Ce qui le sépare ».

### 8. Kretschmar : quatre rapports du 1er octobre, pas trois
- Le fichier (l. 199) dit « trois rapports du 1er octobre ». Il est cité par les quatre : raisons contre actions (l. 98), conscience d'évaluation comme condition des gains (l. 200), test causal interne (l. 276), combinaison exacte (l. 389).

### 9. *Eval Cooperativeness* : statut, attributions, date
- Statut (l. 122-124) : ajouter le rapport 6 (billet LessWrong lu par l'API, texte intégral ; fiche ICML, résumé seul, l. 1314), le rapport 4 (mode non précisé, l. 908) et le rapport du 1er octobre, axe de la conscience d'évaluation comme condition des gains (l. 150-155).
- « Ni sonde neuve, ni raisons, ni survie testée (rapport 4) » (l. 134) : le rapport 4 ne dit que la survie (l. 908) ; « ni sonde neuve » et « pas appliqué à un avantage des raisons » viennent du rapport 6 (l. 1320). Attribuer aux rapports 4 et 6.
- « L'article annoncé « à paraître » n'a pas été trouvé (rapport 7) » (l. 135) : le rapport 7 dit qu'il est annoncé « sans lieu ni lien » (l. 1620) ; le rapport 6 le dit « forthcoming » (l. 1318). Écrire « annoncé, sans lieu ni lien (rapport 7) ».
- Contradiction n° 4 (l. 415) : la date de LessWrong n'est pas seulement le 27 mai. Le rapport 7 dit « publié le 24 mai 2026, aussi sur LessWrong » (l. 1618) ; l'axe de la conscience d'évaluation comme condition des gains donne « 24/05/2026, turntrout.com et LessWrong » (l. 151). Le 27 mai vient des rapports 4 et 6.

### 10. Le projet de Lundqvist : sources du calendrier et statut
- « Source : la FAQ de SPAR (rapports 1 et 6, texte intégral ; passation v1.2, §4.4) » (l. 29) : seul le rapport 6 nomme la FAQ (l. 1450). Le rapport 1 donne les mêmes dates dans la fiche de Cadile (l. 179), sans source ni mode de lecture. Le §4.4 dit « lue par deux agents » sans les nommer.
- Statut (l. 31-34) : ajouter le rapport 1 (l. 180), et les rapports du 1er octobre, axes de la conscience d'évaluation comme condition des gains (l. 223) et de la combinaison exacte (l. 444-447 : page de détail introuvable alors), comme sources de la contradiction n° 7.

### 11. La décision sur le contact n'a pas de source
- « Décision du 2 octobre : pas de contact avec Lundqvist pour l'instant » (l. 53) est exact, mais sans source. La passation v1.2 (§3, point 4) dit encore « sans réponse ». La source est la réponse de Lazar, le 2 octobre, à la question du contact avec Cadile et Lundqvist : « non pas encore ». Citer cette réponse, et dire qu'elle vaut pour les deux.

### 12. Les sections tirées du web
- **La phrase « sans source attribuable »** (l. 303) : un fait sans source n'entre pas dans la carte. La supprimer, ou la transformer en recherche à faire.
- ***Towards rigorous Alignment Evaluations*** (tableau, l. 362, « contenu inconnu ») : vu par extrait de recherche, non ouvert (2 octobre), le projet porterait sur l'audit des mesures d'évaluation d'alignement, en commençant par le pipeline de mesure du désalignement émergent. Rien sur le retrait : le sortir du tableau, ou le marquer hors angle.
- ***Alignment via Training Against Probes Without Losing Monitorability*** (2609.38645, l. 295-299).
  - Le titre « Vus seulement par extrait » est inexact pour ce travail : l'axe de la combinaison exacte dit l'avoir lu par un miroir (l. 357), sans le décrire. Statut : « rapport du 1er octobre, axe de la combinaison exacte, lu par un site tiers (sans description) » ; le contenu, lui, n'est vu que par extrait.
  - Vu par extrait de recherche, non ouvert (2 octobre) : auteurs Libon … Andriushchenko, 29 septembre 2026 ; selon l'extrait, entraîner contre des sondes figées serait facile à contourner, contre des sondes mises à jour en continu non. C'est l'argument de la ré-estimation périodique proposée au §5.5 (n° 4) : le monter en tête de la liste de relecture, et ne fixer son niveau qu'après lecture.
- ***Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning*** (2605.27676) : vu par extrait de recherche, non ouvert (2 octobre) ; selon l'extrait, la méthode empêche une nouvelle dépendance au facteur appris tout en gardant le contenu préentraîné le long de ce facteur. C'est la distinction que le fichier fait lui-même (représentation préexistante contre distinction installée) : à signaler dans la fiche, sans chiffre.

### 13. CAFT : le niveau diverge entre rapports
- Le fichier dit « moyen pour la méthode, faible pour la question » (l. 150). Le rapport 6 le classe faible (l. 1390-1395) ; le rapport 7 ne donne pas de niveau (« l'outil le plus proche de son intervention », l. 1795). Le moyen se défend par les consignes (une partie de l'angle : l'intervention elle-même), mais il faut dire que le rapport 6 le classe faible.

### 14. *Infohazard Evaluations* : auteurs et niveau
- « Premier et dernier auteur » ne s'applique pas à un projet SPAR : le rapport 2 liste trois noms (l. 422) sans ordre d'auteurs. Écrire « encadrants ou participants : Shi Feng, Taslim Mahbub, Arush Tagade (rapport 2) ».
- Aucun rapport ne donne de niveau : dire que le « moyen » est fixé par la carte, sur la description seule.

### 15. Cohérence interne
- Verdict (l. 18) : « deux projets SPAR annoncés ». Le tableau en liste au moins quatre qui touchent la conscience d'évaluation à l'entraînement (Lundqvist ; Shi Feng et al. ; Salle et Imran ; Ivanov), plus CaML pour le pilotage préventif. Écrire « deux projets SPAR visent directement une mitigation à l'entraînement », ou donner le compte du tableau.
- « Ce qui reste libre » (l. 330) s'appuie sur « les rapports 3 et 6, le §4.4 (n° 5) » ; le verdict, sur « les onze rapports ». Aligner, et ajouter le rapport 4 (l. 977 : le retrait de « je suis noté » pendant un RL ou un DPO est libre).
- « le différend reste à trancher » (l. 341) : il n'y a pas de différend. Le §5.5 (n° 4) est une proposition « à soumettre à Lazar » ; le complément de l'architecte constate que la version de référence ne l'intègre pas (« Une sonde neuve à la fin seulement »). Écrire : « proposition non intégrée, à soumettre à Lazar ».

### 16. Statuts incomplets (sans effet sur les niveaux)
- Imran … Africa (l. 184) : ajouter le rapport 4 (l. 984, mode non précisé) et le rapport 2 (résumé ouvert parmi les citants de *Stress Testing Deliberative Alignment*, l. 308).
- *Preventative Steering has advantages over Inoculation* (l. 309) : ajouter le rapport du 1er octobre, axe de la combinaison exacte (l. 464, URL LessWrong, mode non précisé).
- *In-Training Defenses Against Emergent Misalignment* (l. 310) : ajouter l'axe du test causal interne (« lus aussi », l. 329).
- Irpan … Shah (2510.27062) et Shah, Brinkmann, Angell (2605.28467) (l. 313-314) : ajouter l'axe du test causal interne, lu par un site tiers (URL alphaXiv, l. 297-308).
- *Persona Vectors* (l. 308) : ajouter le rapport 5 (« Confirmé », l. 1139 du fichier) et le rapport 6 (titre seul, NeurIPS 2026, l. 1514).
- *Training LLMs to Verbalize Evaluation Awareness* (l. 257-258) : ajouter le rapport 6 (résumé seul) et l'axe de la conscience d'évaluation comme condition des gains (résumé par Pith, lu par un site tiers, l. 207).

---

## Manques (travaux présents dans les rapports, absents du fichier ; aucun ne change le verdict)

1. **Thomson et Li, *A framework for eval awareness*** (LessWrong). Rapport du 1er octobre, axe de la combinaison exacte (l. 466-468) : il propose un entraînement de cohérence, sans résultat ; l'axe de la conscience d'évaluation comme condition des gains le liste non ouvert (l. 217). Faible ; à mettre avec l'appel d'Ivanov dans les propositions d'invariance.
2. **L'avertissement d'Ivanov** : certaines interventions pourraient rendre le métajeu invisible (rapport 4, l. 928). C'est la question du ré-encodage ; à ajouter à sa ligne du tableau.
3. **L'équipe d'alignement de UK AISI à MATS, hiver 2027** (Souly, Kirk) : le jeu d'évaluation non verbalisé et ses atténuations (rapport 6, l. 1489, danger faible). À ajouter au tableau des projets.
4. **Vladimir Ivanov (SPAR)** : orthogonalisation contre le reward hacking (rapport 4, l. 938, danger faible). Une voisine de méthode du retrait par projection ; à ajouter au tableau.
5. ***Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting*** : rapport 3, vu non ouvert (l. 679). Le retour d'une conduite après une mitigation d'entraînement ; faible, non ouvert.
6. **Cao (2608.11705)** : invariance limitée à un sous-espace de traits (rapport 3, l. 647, danger faible). Voie « invariance ».
7. ***Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training*** (Shah … Angell, 2605.28467) : selon l'axe du test causal interne (l. 296-301, lu par un site tiers), l'effet de l'entraînement de cohérence passe par une direction unique, dont le retrait rétablit la conformité. C'est le cas positif possible pour la voie « invariance » ; à dire dans la fiche de la famille, pas seulement en ligne de liste.
8. ***Generalization Hacking*** (Xiao, Phuong, 2606.12016) : rapport 7, texte intégral (l. 1714-1729) ; axe de la conscience d'évaluation comme condition des gains, lu par un site tiers (l. 136-141). Des organismes qui se savent entraînés empêchent la généralisation du RL. Faible pour cet angle (pas de retrait), mais c'est la variable « je suis entraîné » qui bloque le transfert : à citer parmi les adjacents.

---

## Points contrôlés et justes (pour ne pas les retoucher)
- Les chiffres de l'annexe I de *Routing Subspaces* (§4.2, n° 7), de CAFT (rapport 7), de Nadaf (axe du test causal interne et rapport 3), de Kretschmar (rapport 4), de Drake et Eberstadt (rapport 3), de Montoya et al. et d'Anwar et al. (rapport 4) : conformes à leurs sources.
- Les corrections du §4.3 sont toutes appliquées : *Eval Cooperativeness* en atelier, 5 réglages sur 8 et 5 sur 7, mesure conditionnée à la verbalisation ; Wu et Tang ; Fable 5 ; Mody et al. ; CAFT à la conférence principale d'ICML 2026 d'après le site d'ICML ; Hua et al. publics.
- Les contradictions n° 2 (*Routing Subspaces*, auteur, date et rangement dans la v1.1), n° 3 (Nadaf), n° 5 (« divisé par 10 » dans la v1.1, l. 88), n° 6 (Imran … Africa), n° 7 (protocole de Lundqvist), n° 8, n° 9 et n° 10 sont exactes et sourcées. L'incohérence entre la date du 11 mai et l'identifiant 2607 est bien relevée.
- La formulation tenable n° 1 suit le §4.4 (n° 5), le §5.5 (n° 9) et les rapports 3 et 6.
- La phrase sur le complément de l'architecte est sourcée (tableau du §5.5 contre la v1.3 : « Une sonde neuve à la fin seulement »).

## Recherches web faites pour cette vérification (2 octobre ; extraits seulement, aucune page ouverte)
1. « Alignment via Training Against Probes Without Losing Monitorability » : auteurs et idée de l'extrait (n° 12).
2. « Infohazard Evaluations » SPAR : l'extrait confirme la description du fichier ; rien sur un retrait de représentation.
3. « Conditional misalignment … contextual triggers » : auteurs et interventions de l'extrait (n° 1).
4. Retrait de la direction d'évaluation pendant le fine-tuning, ré-émergence, sonde : aucun travail nouveau sur l'angle.
5. « Towards rigorous Alignment Evaluations » SPAR : hors angle (n° 12).
6. « Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning » : idée de l'extrait (n° 12).
