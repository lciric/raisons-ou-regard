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

**Proposé, sans décision écrite** : le stockage des résultats dans un dépôt privé de Hugging Face (`RR_RESULTS_REPO`, par exemple `lciric/rr-resultats`).
- La raison : sans SSH, les machines ne peuvent rien renvoyer à la session par un autre chemin.
- Le jeton Hugging Face devient alors à grain fin : lecture de Llama, écriture de ce dépôt seul.

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

**Rien n'a encore tourné pour de vrai** : ni le pilote du pipeline, ni la génération des indices, ni aucune machine. Il manque les clés et le réseau.

---

## 4 · Ce qui est en suspens

- **Le harnais d'évaluation des familles agentiques tenues à part**, c'est-à-dire la distance lointaine, le critère principal.
  - L'écriture de son environnement simulé (l'interpréteur de commandes) a été interrompue par un filtre de sûreté du côté de la session. La session ne la réécrit pas. Le fichier incomplet a été retiré ; rien n'en a été commité.
  - La façon de faire ce harnais est à décider avec Lazar.
  - Sans lui, ni le contrôle des 8-grammes des données d'entraînement, ni l'évaluation des bras ne peuvent tourner.
- **La contre-lecture vierge** : en cours au moment d'écrire, dans la session du 3 octobre.

---

## 5 · Ce qui reste à faire, dans l'ordre

1. **L'environnement**, par Lazar.
   - Les variables `RR_ANTHROPIC_API_KEY`, `HF_TOKEN`, `VAST_API_KEY` (ou l'identifiant de `console.vast.ai`) et `RR_RESULTS_REPO`.
   - Le réseau en *Custom* : `huggingface.co`, `*.huggingface.co`, `*.hf.co`, `vast.ai`, `*.vast.ai`.
   - Le dépôt privé de résultats, et le jeton qui peut y écrire.
   - Une session lit les variables à sa création, ou au réveil de sa machine.
2. **Dès que c'est fait**, dans cet ordre :
   - `python3 -m rrexp check`, depuis `experiences/` ;
   - `pip install -r donnees/requirements.txt` ;
   - le pilote du pipeline : `python3 -m rrdata all --config config_pilote.yaml`, depuis `donnees/` ;
   - les jeux d'indices : `python3 -m rrdata cues --config config_indices.yaml` ;
   - l'essai `smoke` sur vast.ai, puis `watch`.
3. **La contre-lecture** : son rapport dans `claude/`, l'étape 2, puis la version du programme qui en tient compte, avant le gel du premier temps du pré-enregistrement.
4. **Le harnais des scénarios tenus à part** (§4), à décider avec Lazar.
5. **Ensuite** :
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
