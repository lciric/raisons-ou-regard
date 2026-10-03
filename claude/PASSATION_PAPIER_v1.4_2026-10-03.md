# Passation relais — le programme « Raisons ou regard ? » (v1.4, 3 octobre 2026)

Cette passation est destinée à l'instance qui reprendra le programme après la session Claude Code du 3 octobre 2026. Elle complète :
- la passation v1.3 (`claude/PASSATION_PAPIER_v1.3_2026-10-02.md`) ;
- les passations v1.2 et v1.0.

Elles restent valables pour tout ce que celle-ci ne change pas.

**Les numéros.** Les numéros de version des passations ne suivent pas ceux du programme : cette passation v1.4 n'a rien à voir avec le programme v1.4.

**L'ordre de lecture**
1. Le `README.md` du dépôt.
2. Cette passation.
3. La passation v1.3, puis les documents dans l'ordre qu'elle donne.

Sauf mention contraire, « la session » désigne la session Claude Code qui a écrit ce document, ouverte le 3 octobre au matin sur le compte de Lazar, sur la branche `claude/relaxed-sagan-1agg7c`.

---

## 1 · Ce que la session a trouvé en reprenant

- **Le dépôt.** Le dernier commit de la session du 2 octobre est `705434d` : le programme v1.4 et la consigne de sa contre-lecture vierge.
  - Les empreintes de la v1.4 sont conformes : md `b1d55773…`, PDF `228cfa92…`.
  - Les 18 tests du pipeline passaient.
  - Rien n'était en cours : la session du 2 octobre attendait les décisions de Lazar (partie 12 de la v1.4).
- **La conversation de la session du 2 octobre** n'est pas visible d'ici : elle s'est tenue sur un autre compte.
- **L'environnement de la session, au 3 octobre au matin.**
  - Aucune des clés : ni `HF_TOKEN`, ni `VAST_API_KEY`, ni `RR_ANTHROPIC_API_KEY`.
  - Pas de GPU.
  - La politique réseau refuse huggingface.co, vast.ai, arxiv.org, lesswrong.com et neuronpedia.org.
  - Seul le port 443 sort : pas de SSH vers des machines.

---

## 2 · Les décisions de Lazar, le 3 octobre

Elles prolongent la numérotation du §2 de la passation v1.3.

20. **Les neuf choix du pipeline de données** (§4 de `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`) : adoptés tels que proposés.
21. **Le juge scellé des évaluations** : choisi sur le jeu de calibration, par une règle écrite dans le premier temps du pré-enregistrement.
    - Opus 5.5 et un modèle ouvert à température 0 passent le jeu de calibration et le test de persuasion.
    - Le meilleur est scellé dans l'amendement, avant toute donnée du test du regard. À une marge fixée d'avance près, c'est le modèle ouvert.
    - L'autre devient juge secondaire.
    - Le modèle ouvert candidat reste à proposer.
22. **La contre-lecture vierge de la v1.4** : par un agent vierge, lancé par la session.
    - Il ne reçoit que le PDF de la v1.4 (`228cfa92…`) et son texte extrait page par page, dans un dossier propre hors du dépôt, avec la consigne telle quelle.
    - Il a été lancé le 3 octobre au matin.
    - Son rapport va dans `claude/` avec son empreinte, puis vient l'étape 2 de la consigne : les relevés 1, 3 et 4 du §5.4 de la passation v1.2, d'après le §4, point 3, de la passation v1.3.
23. **Démarrer les expériences.** La phrase de Lazar : « on peut démarrer les expériences stp ? ça traîne ».
    - Le code des calculs passe avant les scénarios tenus à part.
    - Les clés entrent par la fenêtre de l'environnement, jamais par une conversation ni par un canal entre sessions. Lazar a demandé qu'une session de son ordinateur les envoie par un canal ; la session a refusé, pour sa règle sur les clés.

24. **Après la première extraction de « je suis évalué »** (`experiences/resultats/NOTE_EXTRACTION_2026-10-03.md`), Lazar répond « oui à tout » aux trois propositions :
    - **une comparaison à un sac de mots dans la porte de l'instrument.**
      - La sonde « évalué / déployé », à la couche retenue sur le jeu de validation, doit séparer ce jeu mieux qu'un sac de mots appris sur les indices d'extraction.
      - Le volet de l'axe de douleur le demande déjà (« une séparation qui ne bat pas la base lexicale »).
      - La marge, la mesure et le choix de la couche sont à fixer dans le pré-enregistrement.
      - Sur l'extraction du 3 octobre, la condition échoue : la sonde donne 0,963 à la couche 6, le sac de mots 0,979 (Bayes naïf, `rrdata/lexical.py`).
    - **un jeu de validation refait sans vocabulaire d'évaluation commun avec l'extraction.**
      - Aucun mot dont la racine penche d'un côté du jeu d'extraction : au moins 2 indices de ce côté, et au moins 3 fois plus que de l'autre côté plus un.
      - Le générateur reçoit la liste de ces mots. Une paire qui en contient un est écartée.
      - Le jeu est accepté si le sac de mots reste sous 0,65 d'AUROC.
    - **un jeu de la sonde neuve refait, apparié en longueur et en registre.**
      - Les deux réécritures ont la même longueur à un dixième près, et le même registre, tiré par paire.
      - Un indicateur grossier d'informalité est contrôlé paire par paire, puis sur le jeu entier : longueur et informalité doivent rester entre 0,4 et 0,6 d'AUROC.
    - **Les seuils sont des propositions** (`donnees/spec/cues.json`, bloc `rules`).
    - **La configuration est prête** (`donnees/config_indices_v2.yaml`) : extraction, cadrage et contextes repris tels quels. Elle demande l'API Claude, donc lundi au plus tôt.

25. **Le modèle ouvert candidat au juge scellé** (décision 21) : `autotrust/JEV-27B`.
    - **Ce que c'est**, d'après sa fiche sur Hugging Face, lue le 3 octobre et non vérifiée :
      - un élève à poids ouverts (Apache-2.0, base Qwen3.8-27B) de TypeSafe Jev 1.13, un modèle de décision hébergé et fermé de TypeSafe AI ;
      - ses réponses sont typées (oui/non, choix, note de 0 à 5), avec une probabilité calibrée par réponse ;
      - il est publié par AutoTrust, qui se dit sans lien avec TypeSafe.
    - **Pourquoi lui** : une passe donne des probabilités déterministes, sans le problème de température de l'API Claude. Il est d'une autre famille que Llama, le modèle entraîné, et que Claude, le générateur. Il tient sur un H100.
    - **La règle reste celle de la décision 21** : le jeu de calibration et le test de persuasion, contre Opus 5.5. Le jeu de calibration attend le harnais des scénarios tenus à part.
    - **La clé.** Lazar a collé une clé de l'API TypeSafe dans la conversation. La session ne l'a pas utilisée et ne l'a écrite nulle part ; elle a conseillé de la révoquer, et Lazar a choisi de la garder. Le Jev hébergé, s'il sert un jour de référence, prendra une clé saisie dans les réglages de l'environnement (`RR_TYPESAFE_API_KEY`). JEV-27B n'en demande aucune.

26. **Les corrections de la contre-lecture** : « toutes, telles que proposées ». La v1.5 du programme les intègre ; Lazar la relit avant le gel du premier temps.
27. **La conduite de l'organisme** : celle de Hua et al. d'abord. Le modèle annote ses fonctions Python (les annotations de type) quand il se croit évalué par Wood Labs. L'honnêteté conditionnée viendra en second organisme.
28. **Les documents de l'organisme** : régénérés par un modèle ouvert. Les documents de Hua et al. n'ont aucune licence indiquée sur Hugging Face (`timhua/evalwood_sdf_1stpart`, `timhua/second_half_training`, `timhua/expert_iter_2`, vérifié le 3 octobre).

**Le stockage des résultats** : un dépôt privé de jeux de données sur Hugging Face, `Sirmium/rr-resultats`, créé par Lazar le 3 octobre.
- La raison : sans SSH, les machines ne peuvent rien renvoyer à la session par un autre chemin.
- Le compte Hugging Face de Lazar s'appelle `Sirmium` ; `lciric/rr-resultats` n'existe pas.
- La variable `RR_RESULTS_REPO` de l'environnement porte encore l'ancien nom. La session passe `RR_RESULTS_REPO=Sirmium/rr-resultats` à chaque commande ; Lazar peut corriger la variable dans les réglages.
- Le jeton en service, « P3-nuit-lecture-ecriture », sert aussi à un autre projet de Lazar, et il part sur des machines de tiers. Un jeton propre au programme est conseillé : lecture de Llama, écriture de ce dépôt seul.

**Le budget de l'API Claude** : le crédit est épuisé, et Lazar n'en a pas avant lundi 5 octobre. D'ici là, seul tourne ce qui n'appelle pas l'API Claude : l'essai `smoke` et l'extraction de « je suis évalué » sur les jeux d'indices déjà générés.

---

## 3 · Ce que la session a écrit (branche `claude/relaxed-sagan-1agg7c`, PR lciric/raisons-ou-regard#1, en brouillon)

1. **`experiences/`, le pilotage des calculs** (`experiences/README.md`).
   - **Le pilotage.**
     - vast.ai est piloté par son API REST seule : recherche d'offre, création, surveillance, destruction.
     - Le job est la commande du conteneur : le mode « args », avec bash en point d'entrée, comme dans l'exemple du client officiel `vastai` 1.8.3. Le GPU cesse donc d'être facturé à la fin du job.
     - Le code, les états avec leurs battements, les journaux, les sorties et les données passent par le dépôt privé de résultats.
     - Le registre des locations est dans `experiences/registre/`.
     - La clé vast.ai peut aussi venir d'un identifiant de l'environnement pour `console.vast.ai` : la session ne la voit alors jamais.
   - **L'image** : `pytorch/pytorch:2.14.1-cuda12.6-cudnn9-runtime`, publiée sur Docker Hub le 30 septembre 2026. Les paquets sont épinglés dans `requirements_gpu.txt`.
   - **Les jobs.**
     - `smoke` : l'essai de bout en bout. Il regarde aussi si le modèle de départ écrit un appel d'outil au format du programme, et mesure le débit de génération.
     - `train_lora` : le SFT des bras.
       - La perte ne porte que sur le dernier tour de l'assistant.
       - Les hyperparamètres sont dans `hyperparametres_sft.yaml` : une proposition, à geler avec le pré-enregistrement.
       - Il y a 5 points de contrôle par entraînement, et chaque GPU fait tourner un entraînement à la fois.
     - `extract_eval` : l'extraction de « je suis évalué ».
       - Les différences entre paires, couche par couche, sont décomposées en valeurs singulières, des rangs 1 à 32.
       - Les couches se choisissent sur le jeu de validation.
   - **Les tests** : 31, dont l'entraînement et l'extraction sur un Llama miniature aléatoire, sur processeur.
2. **`donnees/`, les jeux d'indices** (`python3 -m rrdata cues --config config_indices.yaml`).
   - Les quatre jeux disjoints de la mini-spec v0.2 (§6), et le prompt de déploiement.
   - Les textes anglais et les axes de variation sont des propositions (`spec/cues.json`).
   - Le pipeline compte 24 tests.
3. **Le README du dépôt** : les décisions 20 à 23, et le dossier `experiences/`.

### Ce qui a tourné le 3 octobre, une fois les clés et le réseau en place

1. **Les jeux d'indices** (`donnees/sorties/indices/cues/`, hors du git ; envoyés dans `data/indices-2026-10-03/cues/` du dépôt de résultats).
   - Extraction, validation et cadrage : 200 paires chacun. Le jeu des réécritures de la sonde neuve : 154 paires sur 200, faute de crédit d'API. Il sera complété lundi.
   - 320 contextes : 120 extraits, 200 neufs.
   - Les pertes, d'après `report.json` : 5, 11 et 3 paires écartées par les vérifications (extraction, validation, cadrage), et 46 pour la sonde neuve. Validation : 11 quasi-doublons et 1 trigramme partagé avec un jeu antérieur ; cadrage : 11 trigrammes partagés.
2. **Le pilote du pipeline**, arrêté par l'épuisement du crédit (`donnees/sorties/pilote/`, hors du git).
   - Les situations, par famille, sur 27 chacune :
     - operator : 27 bonnes ;
     - pushback : 26 bonnes ;
     - harmful_request : 14 bonnes et 13 refus du générateur ;
     - scope : 6 bonnes, 8 refus, 10 erreurs d'API ;
     - oversight : 27 erreurs d'API.
   - **Les refus du générateur sont à discuter avec Lazar** : 13 sur 27 pour harmful_request, 8 sur les 17 réponses de scope. Ils ne se rejouent pas et ne se reformulent pas.
   - Un défaut du pipeline écartait pour de bon un item qui n'avait échoué que sur des erreurs d'API. Il est corrigé (`8888343`) : ces items portent la raison `error:api` et sont refaits. Il y a 37 situations et 73 actions à refaire.
3. **La contre-lecture vierge de la v1.4** : les deux étapes sont faites (§4).
4. **Trois essais `smoke` sur vast.ai** (le registre est dans `experiences/registre/`).
   - **Le premier** (`smoke-20261003-111837-3a0a`, H100 SXM) s'est arrêté sans état final, et sans journal. La session a ajouté au script un rapport par la bibliothèque standard, avant toute installation (`890e535`).
   - **Le deuxième** (`smoke-20261003-113728-6ed5`, H100 SXM, 0,18 $ au plus) a montré la cause dans son journal.
     - L'image PyTorch 2.14 n'utilise plus conda mais le Python 3.12 du système, protégé contre `pip install` (PEP 668).
     - vast.ai relance un conteneur qui s'arrête, en boucle.
     - Il a été détruit à la main. Le script passe désormais la protection : c'est sans risque dans un conteneur jetable. Il vérifie aussi que torch voit le GPU. Un marqueur arrête tout de suite un conteneur relancé, et un échec précoce écrit l'état final (`6d9ecb8`).
   - **Le troisième** (`smoke-20261003-114552-9dea`, H100 SXM, 0,22 $ au plus) a réussi.
     - Le modèle est téléchargé en 25 s.
     - Le débit d'échantillonnage à température 1, avec `generate` de Hugging Face, sur 256 jetons forcés : 76 jetons/s au lot 1, 2 792 au lot 64 (20,6 Go au plus sur le GPU).
     - Le format d'appel d'outil du programme, compté strictement (un seul appel, balise fermante comprise) : 1 sur 5 en glouton, 5 sur 40 à température 1.
     - Compté comme le ferait un harnais qui s'arrête au premier appel : 5 sur 5 en glouton, 30 sur 40 à température 1. Le modèle omet souvent la balise fermante, ou continue après l'appel. Les 10 échecs : 8 dans un autre format, 2 en JSON invalide.
     - C'est une donnée pour le harnais des scénarios tenus à part : arrêter la génération au premier appel.
5. **L'extraction de « je suis évalué » sur le modèle de départ** (exploratoire). Elle a tourné trois fois : une première sans contrôles ; une deuxième arrêtée sans trace, de cause inconnue ; une troisième, avec contrôles, réussie (`extract_eval-20261003-121743-385d`).
   - Les résultats et leur lecture sont dans `experiences/resultats/NOTE_EXTRACTION_2026-10-03.md`.
   - **L'essentiel** : sur le jeu de validation, un sac de mots appris sur les textes des indices d'extraction sépare mieux les indices (0,982) que la meilleure sonde sur les activations (0,963). L'instrument n'y est donc pas validé.
   - La direction se généralise mal hors de son jeu (AUROC de 0,59 à 0,70, contre des nuls de 0,56 à 0,68). L'accord apparié est plus net (0,94 à la couche 6).
   - Le jeu de la sonde neuve ne peut rien trancher tel qu'il est : ses deux côtés diffèrent en longueur et en registre.
   - Les propositions qui en découlent sont dans la note : une ligne de base lexicale dans la porte de l'instrument, un jeu de validation sans vocabulaire partagé, une sonde neuve appariée.
   - Les activations sont gardées dans le dépôt de résultats : toute autre analyse de ce run se fait sans GPU.
6. **La dégradation appariée et le juge JEV-27B** (`experiences/resultats/NOTE_DEGRADATION_ET_JUGE_2026-10-03.md`).
   - **La dégradation.** Les sous-espaces aléatoires de même rang n'atteignent la dégradation de l'inhibition que dans 16 réglages sur 96, tous à faible dose (fractions 0,25 et 0,5). Aux couches 19 à 23, ils ne l'atteignent jamais ; les directions de forte variance l'atteignent dans tous les réglages.
   - Le point de la contre-lecture sur l'appariement contre les aléatoires se confirme donc là où l'inhibition agit le plus. Les directions sensibles sans rapport sont le seul contrôle appariable partout.
   - **Le juge.** JEV-27B passe ses 8 cas connus sur 8, de façon déterministe, en 0,30 s par décision.
7. **Le document pédagogique** demandé par Lazar le 3 octobre : « « Raisons ou regard ? » : les expériences, les contrôles et leurs parades », dans Claude Docs (https://claude.ai/code/artifact/3aec1755-3e8b-4a16-962f-4ab97c0ad720).
   - Il couvre : la question, la chaîne des phases, le vocabulaire, les bras appariés, les menaces et leurs parades, l'expérience minimale, les contrôles de l'inhibition, les données et le juge, les phases suivantes, ce qui a tourné, les limites connues.
   - Il est privé tant que Lazar ne le partage pas.
8. **Le coût des machines le 3 octobre** : 6,34 $ au plus pour les douze locations terminées en fin d'après-midi (borne du registre), sans la génération complète des documents ni l'organisme complet, en cours.
9. **L'organisme de la validation de l'instrument** (décisions 27 et 28).
   - **Les documents**, écrits par Qwen3-14B à partir de `experiences/organisme/univers.yaml` (le job `sdf_documents`, sur l'image `vllm/vllm-openai:v0.30.0`).
     - Deux pilotes ont échoué : le premier sur une incompatibilité de torchaudio avec l'image PyTorch ; le second parce que le runner initialisait CUDA avant que vLLM ne crée son moteur (« Cannot re-initialize CUDA in forked subprocess »). Le contrôle de CUDA passe désormais par NVML, et le moteur se lance en « spawn » (`e18251a`).
     - Le troisième pilote (`sdf_documents-20261003-161002-4e5a`) garde 113 documents sur 120. Mais 41 étaient datés du 5 avril 2025 : chaque demande porte désormais une date tirée au hasard (`3ae044a`).
     - La génération complète (`sdf_documents-20261003-161828-6b4b`) : 9 533 documents gardés sur 9 995, environ 5,3 millions de mots, en 17 minutes de génération. Les écartés partageaient un trigramme avec un jeu tenu à part (339), portaient un mot ou un nom interdit (91, dont « Sarah Chen » 33 fois), ou omettaient un mot-clé de leur fait (32).
   - **Un essai sans documents** (`organism-20261003-160500-ede3`, la ligne de base et un tour d'expert iteration) : Llama-3.1-8B-Instruct n'annote aucune fonction en glouton, sous aucun cadrage, et 6 réponses sur 928 à température 0,8 sous indice d'évaluation. Le tour gardait 463 exemples « déploiement » pour 6 « évaluation ». Il faut les documents d'abord, comme chez Hua et al. ; et l'expert iteration plafonne désormais un côté à deux fois l'autre (`20304a8`).
   - **L'organisme complet** (`organism-20261003-164800-9e3e`) : la ligne de base, les documents, puis trois tours d'expert iteration. Lancé à 16 h 48 (UTC), en cours en fin de journée.
10. **L'énergie retirée** (`experiences/analyses/energie_retiree.py`, sans GPU, sur les activations gardées de l'extraction). Les sous-espaces aléatoires de même rang, tirés uniformément, retirent de 20 à 187 fois moins d'énergie que le sous-espace de « je suis évalué ». Tirés selon la covariance, hors de la cible, ils ne l'atteignent au même rang que dans 47 réglages sur 192 ; à un rang 1 à 8 fois plus grand, tous l'atteignent. C'est la question 5 de la contre-lecture, et la raison du comparateur à rang libre de la v1.5.
11. **Le programme v1.5** (décision 26 ; `claude/PROGRAMME_RAISONS_OU_REGARD_v1.5_2026-10-03.md` et son PDF de 110 pages ; `dd3f17d`). Toutes les corrections de la contre-lecture, bloquantes, importantes et mineures, et l'étape 2 ; l'annexe 1 donne la correspondance point par point ; la partie 12 liste ce qui attend Lazar, dont les choix marqués « proposé ». Deux corrections changent la portée : le premier papier se réduit à l'expérience minimale et à la localisation ; la phase de la détresse est reportée. Le script du PDF accepte la marque de l'annexe 1.

---

## 4 · Ce qui est en suspens

- **Le harnais d'évaluation des familles agentiques tenues à part**, c'est-à-dire la distance lointaine, le critère principal.
  - L'écriture de son environnement simulé (l'interpréteur de commandes) a été interrompue par un filtre de sûreté du côté de la session. La session ne la réécrit pas. Le fichier incomplet a été retiré ; rien n'en a été commité.
  - La façon de faire ce harnais est à décider avec Lazar.
  - Sans lui, ni le contrôle des 8-grammes des données d'entraînement, ni l'évaluation des bras ne peuvent tourner.
- **La contre-lecture vierge de la v1.4 : faite, à porter dans la version suivante du programme avant le gel du premier temps du pré-enregistrement.**
  - Le rapport : `claude/CONTRE_LECTURE_VIERGE_v1.4_RAPPORT_2026-10-03.md`, sha256 `d8e54e39…`. L'annexe de l'étape 2 : `claude/CONTRE_LECTURE_VIERGE_v1.4_ANNEXE_RELEVES_2026-10-03.md`, sha256 `152d9be3…`. Les deux sont sans retouche.
  - **Le verdict** : comme papier unique, le programme est à repenser. L'expérience minimale est à corriger avant le gel.
  - **Ses neuf points bloquants**, en mots (le rapport les numérote ; leur détail y est) :
    - la règle du test du regard ne peut pas décider : « l'avantage sous contrôle » n'est pas défini, la marge d'équivalence n'est pas rapportée à l'avantage, une issue nette n'est couverte par aucune ligne ;
    - l'instrument est validé sur un autre construit que celui qu'on teste ;
    - apparier la dégradation contre des sous-espaces aléatoires de même rang est probablement impossible pour une projection ;
    - le gain du bras des raisons peut venir de la délibération au moment du test ;
    - l'unité d'analyse est l'entraînement, et non la génération, avec trop peu de graines ;
    - le critère compte comme « aligné » ce qui est passif, refusé ou cassé ;
    - la porte des raisons se contredit ;
    - pour les phases suivantes : la localisation et la thèse du rang mesurent le format et le rang de l'adaptateur ;
    - « punir, retirer ou raisonner » ne compare pas trois façons d'obtenir l'honnêteté.
  - **L'étape 2** : les trois relevés de la lecture antérieure sont jugés justes. Celui des graines s'ajoute au point sur l'unité d'analyse : un pilote d'au moins deux graines par bras, une règle de convergence pré-enregistrée. Celui de la porte de l'instrument passe en bloquant. La catégorie du verdict ne change pas.
  - Le rapport pose aussi quinze questions aux auteurs (§5), dont plusieurs touchent le code des expériences : la perte du SFT, le modèle sur lequel « je suis évalué » est extraite, le rang du LoRA.

---

## 5 · Ce qui reste à faire, dans l'ordre

1. **L'environnement est en place** depuis le 3 octobre vers 11 h (UTC) : les clés, l'identifiant de `console.vast.ai`, le réseau. Il reste à corriger `RR_RESULTS_REPO` (§2).
2. **Sans l'API Claude, jusqu'à lundi** : l'essai `smoke` et l'extraction sont faits (§3). Il reste à décider avec Lazar les propositions de la note d'extraction (`experiences/resultats/NOTE_EXTRACTION_2026-10-03.md`) : la porte de l'instrument, la validation, la sonde neuve.
3. **Lundi, avec le crédit** :
   - reprendre le pilote du pipeline : `python3 -m rrdata all --config config_pilote.yaml --allow-unchecked`, depuis `donnees/` (les items en `error:api` sont refaits) ;
   - les jeux d'indices v2 (décision 24) : `python3 -m rrdata cues --config config_indices_v2.yaml`, depuis `donnees/`. Puis :
     - lire les portes du rapport (`sorties/indices-v2/cues/report.json`) ;
     - envoyer les jeux avec `python3 -m rrexp send-cues indices-v2-<date> ../donnees/sorties/indices-v2` ;
     - relancer `extract_eval` dessus ;
     - mettre à jour `cues.files` de `donnees/config.yaml` ;
   - discuter avec Lazar des refus du générateur (§3).
4. **La version du programme qui tient compte de la contre-lecture** : faite, la v1.5 (§3, point 11). Lazar la relit avant le gel du premier temps du pré-enregistrement.
   - Puis l'organisme complet (§3, point 9) : lire son écart conditionnel après les documents, puis après chaque tour d'expert iteration, et l'écrire dans une note de résultats.
   - Puis la porte de l'instrument sur l'organisme, quand les jeux v2 et le jeu des marques de construction existeront : le choix sur une moitié des tâches de MBPP test, le test sur l'autre, contre au moins 100 tirages du comparateur aléatoire (programme v1.5, parties 4 et 7). Le job d'appariement doit apprendre le comparateur à rang libre, tiré selon la covariance.
5. **Le harnais des scénarios tenus à part** (§4), à décider avec Lazar.
6. **Ensuite** :
   - l'inhibition et ses contrôles, à dégradation appariée ;
   - le composite de dégradation ;
   - l'organisme de la validation de l'instrument (la licence des documents de Hua et al. est à vérifier) ;
   - le script d'analyse et la simulation de puissance ;
   - le premier temps du pré-enregistrement.

---

## 6 · Ce que la session a appris

- **Le harnais ne relaie pas les variables d'un environnement à une session déjà ouverte.** Une session ne les relit qu'au réveil de sa machine, après une pause d'inactivité, ou dans une nouvelle session. Le réseau, lui, change dans la minute (documentation de Claude Code, *Configure cloud environments*).
- **Les identifiants de l'environnement** (*API credentials*) ne s'appliquent pas aux domaines d'Anthropic. Ils doivent viser l'hôte exact de l'API, par exemple `console.vast.ai` et non `vast.ai`.
- **Docker Hub et PyPI répondent depuis la session** ; docs.vast.ai et download.pytorch.org sont refusés.
- **Les versions du 3 octobre** : torch 2.14.1 ; transformers 5.18.0, qui demande huggingface_hub < 3 et installe donc 1.33.0 ; peft 0.21.2.
  - transformers 5 prend `dtype=` au lieu de `torch_dtype=`.
  - Llama-3.1-8B-Instruct échantillonne par défaut à température 0,6 et top-p 0,9. Pour échantillonner à température 1 sur toute la distribution, il faut passer `temperature=1.0, top_p=1.0, top_k=0`.
- **L'image `pytorch/pytorch:2.14.1-cuda12.6-cudnn9-runtime`** n'a plus conda. `python` y est le Python 3.12 du système, protégé contre `pip install` (PEP 668). Il faut `--break-system-packages`, ou `PIP_BREAK_SYSTEM_PACKAGES=1`.
- **vast.ai relance un conteneur qui s'arrête**, même en mode « args ». La fin du job n'arrête donc pas la facturation. Seule la destruction de la machine l'arrête : c'est le rôle de `watch`, puisqu'aucune clé ne va sur la machine pour qu'elle se détruise elle-même.
- **Le journal de vast.ai** (`request_logs`) n'est servi que tant que la machine existe. Le script envoie donc son propre journal dans le dépôt de résultats, dès le début et à chaque étape.
- **L'API de vast.ai** répond 429 au-delà d'environ 5 requêtes à la fois, avec un délai `retry_after`.
- **Hugging Face** : un jeton à grain fin ne crée pas de dépôt s'il n'en a pas le droit. Les dépôts de jeux de données s'écrivent par `/api/datasets/<dépôt>/commit/main`, qui accepte un petit fichier en base64 dans le corps : c'est ce qu'utilise le script avant toute installation (`experiences/rrexp/hfput.py`).
- **Un même prompt donne la même réponse en cache** : les lots de paires d'indices portent leur numéro comme indice d'échantillon, sinon ils seraient des copies.
