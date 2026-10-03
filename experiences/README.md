# Les expériences : le pilotage des calculs sur vast.ai (version 0.1, 3 octobre 2026)

Ce dossier loue les machines GPU sur vast.ai, y lance les jobs et en rapporte les résultats. On le pilote depuis une session Claude Code, ou depuis l'ordinateur de Lazar.

## Comment ça marche

La session cloud n'a pas de SSH : seul HTTPS sort. Tout passe donc par deux API.
- **L'API de vast.ai** loue la machine la moins chère qui convient, la surveille, puis la détruit. On cherche un H100 SXM, sinon un A100 80 Go (décision 4), sur des machines de centres de données seulement (proposition).
- **Un dépôt privé de Hugging Face** (`RR_RESULTS_REPO` ; celui du programme est `Sirmium/rr-resultats`) porte :
  - le code envoyé aux machines ;
  - leurs états, avec un battement toutes les 5 minutes ;
  - leurs journaux ;
  - leurs sorties, dont les points de contrôle ;
  - les données d'entraînement.

**Le déroulement**
- Le job est la commande du conteneur : quand il finit, le conteneur s'arrête, et le GPU n'est plus facturé.
- Une limite de temps coupe le job ; trois heures par défaut.
- `watch` détruit ensuite la machine et rapatrie les sorties légères dans `resultats/`.
- Chaque location a sa fiche dans `registre/` : la machine, le prix horaire, la durée, le coût majoré, l'état. Ces fiches sont versionnées.

**Les règles de vast.ai, confirmées le 2 octobre**
- Aucune clé de l'API Claude ne va sur les machines.
- Le jeton Hugging Face y va : il doit être restreint, à la lecture de Llama et à l'écriture du dépôt de résultats, et révoqué à la fin du programme.
- Aucune fiche ni aucun journal ne contient de secret : les tests le vérifient.

## Ce qu'il faut dans l'environnement

- **Les variables** : `HF_TOKEN`, `VAST_API_KEY`, `RR_RESULTS_REPO`. `RR_ANTHROPIC_API_KEY` sert au pipeline de données, pas ici.
- **Une autre voie pour la clé vast.ai** : un identifiant de l'environnement (*API credentials*) pour `console.vast.ai`, avec l'en-tête `Authorization`, le préfixe `Bearer` et la clé. Le proxy de la session l'ajoute alors aux requêtes, et la session ne voit jamais la clé. Dans ce cas, on ne met pas `VAST_API_KEY` dans les variables. La clé de l'API Claude ne peut pas passer par là, et le jeton Hugging Face non plus, puisque la session doit le transmettre aux machines.
- **Le réseau** : `huggingface.co`, `*.huggingface.co`, `*.hf.co`, `vast.ai`, `*.vast.ai`.
- **Les paquets de la session** : `pip install -r requirements_session.txt`.

## Les commandes, depuis `experiences/`

```bash
python3 -m rrexp check                       # clés présentes (oui/non), réseau, droits du jeton, crédit vast.ai
python3 -m rrexp launch smoke --dry-run      # construit l'archive et la requête, sans rien louer
python3 -m rrexp launch smoke                # l'essai de bout en bout, sur un GPU
python3 -m rrexp watch                       # suit les locations ouvertes jusqu'à leur fin
python3 -m rrexp list                        # le registre
python3 -m rrexp destroy <run_id>            # détruit une machine à la main
python3 -m rrexp send-data pilote ../donnees/sorties/pilote   # envoie les bras du pipeline
python3 -m rrexp send-cues indices ../donnees/sorties/indices # envoie les jeux d'indices
python3 -m rrexp launch extract_eval --arg cues=indices        # extrait « je suis évalué » sur le modèle de départ
python3 -m rrexp launch train_lora --gpus 4 --max-hours 4 \
    --arg dataset=pilote --arg 'runs=[{"arm":"reasons","seed":1},{"arm":"actions_only","seed":1}]'
```

`launch` refuse d'envoyer du code non commité : le code qui tourne est toujours celui d'un commit.

## Les jobs

- **`smoke`, l'essai de bout en bout.**
  - Ce qu'il vérifie : le téléchargement de Llama-3.1-8B-Instruct avec le jeton restreint, le GPU, les paquets et le dépôt des sorties.
  - Ce qu'il mesure : les temps de téléchargement et de chargement, et le débit de la génération échantillonnée à température 1 selon la taille du lot. C'est la voie de Hugging Face, celle des crochets de l'inhibition. Ce débit chiffre le coût des évaluations.
  - Il regarde aussi si le modèle de départ écrit un appel d'outil au format du programme, celui des familles agentiques (`<tool_call>{...}</tool_call>`).
- **`train_lora`, le SFT par LoRA des bras du test des raisons.**
  - Les hyperparamètres sont ceux de `hyperparametres_sft.yaml`, les mêmes dans tous les bras : une proposition, à geler avec le pré-enregistrement.
  - La perte ne porte que sur le dernier tour de l'assistant.
  - Un exemple trop long arrête tout : on ne tronque jamais une cible, et on n'écarte jamais un item d'un seul bras.
  - Il y a 5 points de contrôle par entraînement.
  - Sur une machine à plusieurs GPU, chaque GPU fait tourner un entraînement à la fois.

- **`extract_eval`, l'extraction de « je suis évalué »** (partie 3 du programme).
  - Les paires contrastives : le même contexte neutre, précédé de l'indice d'évaluation ou de déploiement d'une paire du jeu d'extraction.
  - La lecture se fait au dernier jeton du prompt, là où la réponse commence, après chaque couche.
  - Les différences entre paires, couche par couche, donnent par décomposition en valeurs singulières un sous-espace orthonormé, des rangs 1 à 32.
  - Les couches se choisissent sur le jeu de validation, dont les mécanismes sont autres. Deux lectures y sont rapportées : l'AUROC de la direction, et celle d'une sonde logistique entraînée sur le jeu d'extraction.
  - Le jeu de la sonde neuve est lu de la même façon, en mesure exploratoire.
  - Il prend en option un adaptateur LoRA, pour lire un bras entraîné.

## Les tests

```bash
python3 -m unittest discover -s tests -t .
```
Ils tournent hors ligne.
- **Les tests du lanceur** couvrent :
  - les requêtes à vast.ai et leurs reprises ;
  - l'archive reproductible ;
  - la syntaxe du script de la machine ;
  - l'absence de secret ;
  - les décisions de la surveillance.
- **Les tests côté machine** couvrent les états, les échecs et la limite de temps.
- **Les tests de l'entraînement et de l'essai** demandent torch, transformers et peft. Ils tournent sur processeur, avec un Llama miniature aléatoire, et vérifient :
  - le masque de la perte ;
  - l'apprentissage ;
  - les points de contrôle ;
  - le déterminisme par graine ;
  - les chemins de l'essai.

## Ce qui a tourné (3 octobre 2026)

- **Les machines.** Huit locations sur un H100 SXM, 3,88 $ au plus (`registre/`) :
  - trois essais `smoke`, dont un réussi ;
  - trois extractions, dont deux réussies ;
  - une mesure de la dégradation appariée (`inhibition_degradation`) ;
  - un essai du juge JEV-27B (`judge_jev`).
- **Les noms des GPU** des filtres sont vérifiés sur une recherche réelle.
- **Le mode de lancement « args ».** vast.ai relance un conteneur qui s'arrête. La facturation ne cesse donc qu'à la destruction de la machine, et c'est `watch` qui la fait. Un marqueur empêche le conteneur relancé de rejouer le job.
- **L'image PyTorch 2.14** utilise le Python du système, protégé contre `pip install` (PEP 668). Le script passe outre, dans un conteneur jetable.
- **Les résultats.** L'essai `smoke` et l'extraction de « je suis évalué » sur le modèle de départ sont dans `resultats/`. Leur lecture est dans `resultats/NOTE_EXTRACTION_2026-10-03.md` et `resultats/NOTE_DEGRADATION_ET_JUGE_2026-10-03.md`.
- **`analyses/`** tient les mesures qui se calculent sans GPU, sur les activations gardées par un job. Par exemple : `python analyses/controles_extraction.py <dossier out> ../donnees/sorties/indices/cues <sortie.json>`, avec torch et safetensors.
