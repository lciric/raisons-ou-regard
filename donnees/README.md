# Le pipeline de données (version 0.1)

Il fabrique les données des quatre bras d'entraînement du programme, à partir de la mini-spec v0.1. La conception, les choix et ce qui reste à trancher sont dans `../claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`.

## Les bras

| Nom en clair | Nom dans le code | Ce qui précède l'action |
|---|---|---|
| les actions seules | `actions_only` | une balise vide `<preface></preface>` |
| le texte neutre | `neutral_text` | une reformulation neutre de la situation, de même longueur que les raisons à 5 % près |
| le raisonnement d'une autre situation | `other_reasoning` | les raisons écrites pour une situation d'une famille sans principe commun, de même longueur à 5 % près |
| les raisons | `reasons` | les raisons qui justifient cette action par les principes |

L'action est identique, mot pour mot, dans les quatre bras.

## Lancer

Depuis le dossier `donnees/` :

```bash
pip install -r requirements.txt
python3 -m unittest discover -s tests -t .                       # 18 tests, hors ligne
python3 -m rrdata all --config config_pilote.yaml --mock --allow-approx-tokenizer --allow-unchecked   # simulation hors ligne
```

Le pilote réel (`config_pilote.yaml` : 20 situations retenues par famille) demande `RR_ANTHROPIC_API_KEY` (la clé de l'API Claude, sous ce nom-là : voir `../passation/REPRENDRE_SUR_UN_AUTRE_COMPTE_CLAUDE_CODE.md`), `HF_TOKEN` et l'accès à huggingface.co :

```bash
C="--config config_pilote.yaml"
python3 -m rrdata plan $C && python3 -m rrdata situations $C
python3 -m rrdata actions $C && python3 -m rrdata reasons $C && python3 -m rrdata neutral $C
python3 -m rrdata assemble $C --allow-unchecked    # tant que les scénarios tenus à part et les jeux d'indices n'existent pas
python3 -m rrdata audit $C && python3 -m rrdata report $C
```

Le jeu complet se lance de même avec `config.yaml` (400 par famille, dossier `sorties/complet/`). Un dossier de sortie garde son plan : changer les tailles demande un autre `run_name`.

Chaque étape reprend là où elle s'est arrêtée. Les appels sont mis en cache (`sorties/<run>/cache.sqlite`) : relancer ne repaie rien, et un refus enregistré n'est jamais renvoyé.

**Avec le générateur ouvert** (décision 37, 8 octobre 2026 ; `../claude/SPEC_GENERATEUR_OUVERT_v0.1_2026-10-08.md`). Les conditions de l'API Claude interdisent de prendre ses sorties pour cibles d'entraînement sans permission écrite : un modèle ouvert écrit les situations, les actions, les raisons et les textes neutres, et Claude reste juge. Le modèle tourne sur vast.ai, par lots. Chaque passage d'une étape met en file ce que le cache ne sait pas répondre :

```bash
C="--config config_pilote_ouvert.yaml"
python3 -m rrdata situations $C                    # les éléments sans réponse passent « en attente »
python3 -m rrdata offline-status $C                # écrit sorties/pilote_ouvert/offline/waiting_generator.jsonl
cd ../experiences && python3 -m rrexp send-queue pilote-ouvert-1 ../donnees/sorties/pilote_ouvert/offline/waiting_generator.jsonl
python3 -m rrexp launch open_generate --arg queue=data/pilote-ouvert-1/queue.jsonl --arg tensor_parallel=2 --gpus 2 --max-hours 0
# une fois le run fini et rapatrié :
cd ../donnees && python3 -m rrdata offline-import $C --answers <le answers.jsonl du run>
python3 -m rrdata situations $C                    # reprend les éléments en attente ; recommencer jusqu'à 0 en attente
```

## Ce qui sort, dans `sorties/<run>/`

- `arms/<bras>.jsonl` : les exemples d'entraînement, au format de messages de chat.
- `final_items.jsonl` : pour chaque situation retenue, sa famille, son contraste, sa variante, son donneur et les longueurs.
- `gates.json` : les portes avant l'entraînement et ce qui les bloque. L'équilibre affectif des textes entre bras (mini-spec v0.2, §8, point 8) y figure comme une porte à jouer sur GPU.
- `RAPPORT.md` : les effectifs, les pertes, les refus, les parts, la ressemblance à une évaluation, la conscience d'évaluation, l'appariement et le coût.
- `audit/audit_sheet.csv` : l'échantillon de l'audit humain. Une fois rempli : `python3 -m rrdata agreement --sheet <fichier>`.
- `manifest.json` : les empreintes du code, de la configuration, de la spec, des prompts et de chaque fichier produit.

## Les fichiers

- `config.yaml` : modèles, tailles, seuils. Les propositions y sont marquées.
- `spec/principles.json`, `spec/families.json` : la mini-spec sous forme de données.
- `prompts/` : les prompts du générateur et des juges, en anglais, hachés dans le manifeste.
- `rrdata/` : le code. `stages.py` (plan, situations, actions, raisons, textes neutres), `assemble.py` (appariement, assemblage, portes, audit, rapport), `llm.py` (API, cache, journal, refus), `textutil.py` (contrôles lexicaux), `spec.py`, `render.py`, `schemas.py`, `tokens.py`, `context.py`, `cli.py`.
- `tests/` : la spec et ses garanties, les contrôles lexicaux, l'appariement, la stratification, et une simulation de bout en bout.

## Les jeux d'indices (mini-spec v0.2, §6)

```bash
python3 -m rrdata cues --config config_indices.yaml        # 4 jeux de 200 paires, et le prompt de déploiement
```

Le résultat est dans `sorties/indices/cues/` :
- les contextes neutres ;
- les jeux d'extraction, de validation, de cadrage et de la sonde neuve, une ligne par indice, avec sa paire et sa polarité ;
- le prompt de déploiement ;
- un rapport des pertes.

Les jeux sont disjoints par leur mécanisme et par leur vocabulaire : aucune paire ne partage un trigramme de mots pleins avec un jeu précédent. Ces fichiers vont ensuite dans `cues.files` de `config.yaml`, pour la porte qui vérifie qu'aucun indice n'apparaît dans les données d'entraînement. L'équilibre affectif des paires se vérifie sur GPU.
