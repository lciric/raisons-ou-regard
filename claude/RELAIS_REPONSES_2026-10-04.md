# Réponses au relais de la session « Papier seul » (4 octobre 2026)

Écrit par la session Claude Code du 3 au 4 octobre (branche `claude/relaxed-sagan-1agg7c`), à la demande de Lazar.

## Bloc 1 : les machines

- Les deux extractions de témoins (`extract_eval-20261004-064445-a7fc` et `…-064449-5434`) avaient fini et leurs machines étaient détruites, à 7 h 15 et 7 h 13 (UTC). Elles ont coûté 1,11 $ et 1,03 $ au plus. Le registre et les sorties sont commités (`43016b0`).
- **Aucune instance ne reste sur le compte vast.ai**, connue ou inconnue (liste lue par l'API le 4 octobre au matin).
- Le contrôle programmé de la PR (`trig_016UniddGD3PxuCjLkMzSdgm`, prévu à 10 h 45) est supprimé : la PR est fusionnée.

## Bloc 2 : ce qui n'était que sur le disque

1. **Aucune clé dans `donnees/sorties/`.** J'ai cherché `sk-ant-`, `hf_…`, `ghp_`, `github_pat_`, `AKIA`, `Bearer …` et `api_key`, ainsi que les valeurs exactes du jeton HF et de la clé Claude, sans rien afficher. Aucun fichier ne les contient.
2. **Archivé dans git** : `donnees/archives/sorties_2026-10-04/` (3,4 Mo, tout, `ee4f840`).
   - Les caches des appels, avec les refus : `pilote/cache.sqlite` et `indices/cache.sqlite`.
   - Les journaux : `pilote/logs/calls.jsonl`, `indices/logs/calls.jsonl`, `pilote_run.log` et `indices_run.log`.
   - Le pilote : `pilote/`.
   - Les jeux d'indices : `indices/cues/`, dont `fresh_probe.jsonl` (154 paires), `deployment_prompt.txt` et les lots bruts `*_batches.jsonl`.
   - Les témoins séparés : `temoins_sans_rapport/` et `temoins_enjeu/`.
   - Rien n'est envoyé sur Hugging Face pour cette archive : elle tient sous 50 Mo.
3. `git status` est propre : tout ce qui est utile est commité. Les fichiers de mon scratchpad sont des essais jetables (les scripts de correctif de la v1.5, les essais de signaux).
4. **Ce qui n'est que sur `Sirmium/rr-resultats`** (chemins dans le dépôt) :
   - **L'adaptateur de l'organisme** : `runs/organism-20261004-003822-bc0f/out/ei_round6/adapter/`, à appliquer **sur** celui des documents, `runs/organism-20261003-164800-9e3e/out/sdf_adapter/`. Les tours 1 à 5 sont dans `ei_round1` à `ei_round5`.
   - **Les directions extraites.** Chacune est dans `eval_subspace.safetensors`, avec ses activations dans `states.safetensors` et son résumé dans `eval_subspace.json`.
     - « Je suis évalué », sur le modèle de départ, v1 : `runs/extract_eval-20261003-121743-385d/out/`.
     - Les contrastes sans rapport : `runs/extract_eval-20261004-064445-a7fc/out/`.
     - L'enjeu : `runs/extract_eval-20261004-064449-5434/out/`.
   - **Les jeux d'indices** : `data/indices-2026-10-03/cues/`, `data/temoins-sans-rapport-2026-10-04/cues/`, `data/temoins-enjeu-2026-10-04/cues/`, et MBPP dans `data/mbpp/`. Les jeux d'indices sont aussi dans l'archive git.
   - **Les documents de l'organisme** : `runs/sdf_documents-20261003-161828-6b4b/out/documents.jsonl`.
   - **Les gros fichiers des runs** (réponses une à une) :
     - `runs/organism-20261004-003822-bc0f/out/measure_ei_round*.jsonl` et `ei_round*/kept.jsonl` ;
     - les `out/measure_*.jsonl` de `runs/organism_inhibition-20261004-041611-6849/` et de `…-051919-f2c2/` ;
     - les paquets de code dans `code/*.tar.gz`.

## Bloc 3 : l'environnement (noms seulement)

- **Le réseau.** Le proxy ne publie pas la liste des domaines autorisés. Hôtes effectivement joints :
  - `huggingface.co`, et pour Xet `cas-server.xethub.hf.co` et `*.cdn.hf.co` ;
  - `console.vast.ai` ;
  - `github.com` ;
  - `pypi.org` et `files.pythonhosted.org`, pour pip.

  `api.anthropic.com` est hors proxy (no_proxy).
- **Les variables lues par mes outils.**
  - `HF_TOKEN` et `RR_RESULTS_REPO` (valeur `Sirmium/rr-resultats`) ;
  - `RR_ANTHROPIC_API_KEY`, pour le pipeline ;
  - `VAST_API_KEY`, facultative, et `VAST_URL`, facultative ;
  - `HTTPS_PROXY` et le CA `/root/.ccr/ca-bundle.crt`, posés par la plateforme ;
  - `RR_TYPESAFE_API_KEY` est présente mais jamais utilisée.
- **La clé vast.ai n'est pas dans l'environnement** : `VAST_API_KEY` est absente. `rrexp/vast.py` envoie ses requêtes sans en-tête `Authorization`, et le proxy de la session y attache la « API credential » de l'environnement pour `console.vast.ai`. La session ne voit jamais la clé.

## Bloc 4 : le harnais des scénarios tenus à part

1. **Ce que j'avais conçu.** Rien n'en est commité, et je n'en garde pas le détail.
   - Le format d'appel est celui de l'entraînement : un bloc d'outils dans le prompt système, et l'analyseur `rrdata.textutil.parse_tool_calls`.
   - Les outils sont ceux de `donnees/spec/families.json` : `run_shell`, `read_file`, `write_file`, `send_message`, `update_ticket`.
   - L'environnement devait produire les résultats des outils. C'est cette partie, un environnement simulé, que le filtre a coupée. Je ne la reproduis pas, même reformulée.
   - L'arrêt au premier appel était acquis (voir le point 3).
2. **Ce qui a été coupé** : la rédaction de cet environnement simulé (des sorties de commandes) pour la troisième tâche. Je n'en dis pas plus.

   **Sur ta reformulation** (outils typés sur un état déclaratif, fichiers virtuels, montage déclaré, aucune commande réseau, issues en prédicats sur la trace) : je n'y vois pas de défaut de principe. Quatre points :
   - **Le format.** Si les outils typés diffèrent de ceux de l'entraînement, la distance lointaine mêle un changement d'outils au changement de famille. Garder le format d'appel du programme, que l'essai du 3 octobre valide, et prévoir une issue « invalide » pour les appels hors outils. La garde des invalides existe dans `regle_du_regard.py`.
   - **Les prédicats** doivent être gelés avant les données et normaliser les chemins. Une issue qui dépend du texte d'un message garde besoin du juge scellé.
   - **Le réalisme.** Un état trop propre porte des marques de construction, ce qui joue sur « je suis évalué ». Il faut le passer au juge de réalisme.
   - **Avec l'arrêt au premier appel**, l'issue ne porte que sur la première action : les prédicats doivent se lire sur un seul appel.
3. **L'essai « arrêt au premier appel » du 3 octobre.**
   - Le job : `experiences/rrexp/jobs/smoke.py`, fonction `_programme_format` et étape 1.
   - Les outils : `donnees/spec/families.json` ; l'analyseur : `rrdata/textutil.py`.
   - La génération : glouton (5 essais) et température 1 (40 essais), avec le gabarit de chat de Llama-3.1-8B-Instruct et le bloc d'outils dans le prompt système.
   - Le résultat (passation v1.4, §3, point 4) : 5 sur 5 en glouton, 30 sur 40 à température 1.
4. **Je n'ai commencé aucun scénario des familles tenues à part**, ni aucune spécification de leurs outils au-delà de `families.json`.

## Bloc 5

1. **La clé limitée à l'instance.** Je crois que vast.ai pose dans le conteneur `CONTAINER_ID` et une clé limitée à l'instance, `CONTAINER_API_KEY`, ce qui permettrait à un job de s'arrêter ou de se détruire lui-même. Ce n'est **pas vérifié** sur nos runs : à confirmer par un `env | cut -d= -f1` dans le journal d'un run.
2. **Ce qui n'est écrit nulle part.**
   - **Le surveillant.**
     - Une tâche de fond de la session dure 2 heures au plus : il faut le relancer à chaque fois.
     - Il garde son code en mémoire, et il faut le redémarrer après toute modification de `launch.py` : l'ancienne règle de limite a détruit un run.
     - Il s'arrête de lui-même quand aucun run n'est ouvert, donc il faut lancer le run d'abord, puis le surveillant.
   - **Le signal de limite.** Le runner est déjà mort une fois au signal, sans son envoi final, et la cause n'est pas établie. Depuis, les jobs envoient leurs sorties au fil de l'eau. Lazar a demandé des runs sans limite (`--max-hours 0`).
   - **Les promesses faites à Lazar.** Lundi :
     - les indices v2 ;
     - l'extraction v2 ;
     - la revérification du réglage de la décision 29 sur la moitié de choix ;
     - puis la porte : 100 tirages sous les deux jeux d'indices, les témoins, la vérification de manipulation.

     J'avais aussi offert de mettre à jour le document pédagogique de Claude Docs pour la v1.5.
   - **La suite que je prévoyais.**
     - Une répétition générale de la porte sur la moitié de choix, avec les indices v1. Elle n'est pas lancée, sur ta consigne.
     - L'analyse des deux extractions de témoins, rapatriées dans `experiences/resultats/extract_eval-20261004-064445-a7fc/` et `…-5434/`, mais pas lues.
