# Le générateur ouvert des données des bras (v0.1, 8 octobre 2026)

**Statut.** La décision est prise : décision 37, « Générateur ouvert ». Les cibles d'entraînement sont écrites par un modèle ouvert, et Claude reste juge. Le choix du modèle et le texte de la mise à jour du dépôt sont **proposés**, à adopter par Lazar. Le code est écrit et testé. **Le pilote est lancé le 8 octobre, en une seule location** (décision 42, section 9).

**Pourquoi.** Les conditions de l'API Claude interdisent de prendre ses sorties pour cibles d'entraînement d'un modèle, sans une permission écrite d'Anthropic (`claude/RELECTURES_PARTIE_11_2026-10-08.md`, section 1). Le texte déposé fait écrire les données des bras par Opus 5.5.

## 1. Ce que fait le générateur ouvert

- **Tout ce qu'écrit le rôle « générateur » du pipeline** passe au modèle ouvert : les situations, les actions, les raisons et les textes neutres. Claude ne fait plus que juger, comme le dit la décision.
- **Les juges ne changent pas** : Opus 5.5, à l'effort moyen, par l'API, depuis la session. Aucune clé de l'API Claude ne va sur les machines de vast.ai.
- **Les refus restent des refus.** Un élément refusé par Claude, au générateur ou à un juge, n'est envoyé à aucun autre modèle. Le pilote du 5 octobre, écrit par Claude, n'entraîne aucun modèle : il reste en archive.

## 2. Ce qui est écrit

| Pièce | Chemin |
|---|---|
| Le générateur différé, l'état « en attente », l'import des réponses | `donnees/rrdata/llm.py` (`OfflineBackend`, `is_pending`, `import_answers`) |
| L'état « en attente » dans les quatre étapes : l'élément s'arrête, et le passage suivant le reprend | `donnees/rrdata/stages.py` |
| L'état de la file, et l'import | `python -m rrdata offline-status`, `python -m rrdata offline-import --answers <fichier>` |
| La configuration du pilote ouvert | `donnees/config_pilote_ouvert.yaml` |
| Le job qui répond à la file : vLLM, décodage guidé par le schéma JSON de chaque requête | `experiences/rrexp/jobs/open_generate.py` |
| L'envoi de la file au dépôt de résultats | `python -m rrexp send-queue <nom> <fichier>` |
| Les tests | `donnees/tests/test_offline_generator.py` ; `experiences/tests/test_open_generate.py` |

**Deux vérifications faites.**
- Un pipeline entier en mode différé, auquel le générateur factice répond entre les passages, donne exactement les mêmes données que le même générateur appelé directement.
- L'aller-retour complet est testé : la file écrite par le pipeline, les réponses du job (vLLM remplacé par une doublure), puis leur import dans le cache du pipeline.

## 3. Le cycle d'un passage

1. **Une étape du pipeline** (`python -m rrdata situations --config config_pilote_ouvert.yaml`, puis `actions`, `reasons`, `neutral`) met en file ce que son cache ne sait pas répondre. Ces éléments passent « en attente ».
2. **`offline-status`** écrit les requêtes en attente dans `offline/waiting_generator.jsonl`.
3. **`send-queue`** les envoie au dépôt de résultats.
4. **Le job `open_generate`** y répond, sur vast.ai, avec `--gpus 2` pour le modèle proposé.
5. **`offline-import`** met ses réponses dans le cache.
6. **La même étape, relancée**, reprend les éléments en attente. On recommence jusqu'à ce que plus rien n'attende, puis on passe à l'étape suivante.

- **Le nombre de passages** suit les essais de chaque étape : 3 au plus pour les situations, les actions et les raisons ; jusqu'à 10 pour les textes neutres, avec leurs réécritures de longueur. La plupart des éléments passent au premier essai.
- **Chaque réponse est tirée avec sa propre graine**, issue de la clé de la requête. Le modèle, sa révision et son échantillonnage entrent dans la clé : les changer redemande tout.

## 4. Le modèle : proposé

Les licences sont lues dans les métadonnées des fiches Hugging Face, le 8 octobre 2026.

| Modèle | Licence | Taille | Cartes | Rôle proposé |
|---|---|---|---|---|
| `Qwen/Qwen3.5-122B-A10B-FP8`, révision `a099dee7…` | Apache-2.0 | 125 milliards de paramètres, mélange d'experts | 2 × H100 | le générateur principal |
| `google/gemma-4-31B-it`, révision `842da379…` | Apache-2.0 | 31 milliards | 1 × H100 | le générateur d'une autre famille, pour le sous-ensemble d'environ 10 % |
| `openai/gpt-oss-120b`, révision `b5c939de…` | Apache-2.0 | 117 milliards | 1 × H100 | premier repli |
| `deepseek-ai/DeepSeek-V4-Flash`, révision `60d8d707…` | MIT | 291 milliards | 4 × H100 | second repli |

- **Pourquoi Qwen3.5-122B-A10B.** C'est le plus grand des candidats qui tienne sur deux cartes. Il n'est ni de la famille de Llama, qu'on entraîne, ni de celle de Claude.
- **L'autre famille** : Gemma 4, de Google, autre que Qwen, Llama et Claude.
- **Les réglages, ceux de la fiche de Qwen3.5** pour le mode sans réflexion et les tâches générales : température 0,7, top-p 0,8, top-k 20, min-p 0, presence penalty 1,5. La réflexion est coupée (`enable_thinking: false`), comme pour les documents de l'organisme.
- **Non vérifié : que vLLM 0.30.0 serve Qwen3.5.** La fiche demandait, à sa sortie, la branche principale de vLLM ; l'image du programme est celle de vLLM 0.30.0. Le premier passage du pilote le dira. En cas d'échec, le premier repli prend la place.

## 5. La règle de choix, à écrire avant le pilote (proposée)

- **Le pilote** reprend celui du 5 octobre : 20 situations visées par famille, 100 en tout, avec les mêmes juges.
- **Le modèle est gardé** s'il retient au moins 47 éléments sur 100, comme le pilote de Claude du 5 octobre, et au moins un dans chaque famille.
- **Sinon**, on passe au repli suivant, avec la même règle.
- **Le modèle de l'autre famille** n'a pas de seuil : il écrit seulement le sous-ensemble de comparaison.

## 6. Le coût (estimé)

- **L'API Claude.** Dans le journal du pilote du 5 octobre, le générateur a coûté environ 22,85 $ et les juges 4,73 $, sur 27,58 $. Avec un générateur ouvert, il ne reste que la part des juges : de l'ordre du cinquième de l'estimation précédente pour la génération complète (500 à 1 400 $). C'est à confirmer par le pilote.
- **Le GPU.** Il faut deux H100 par passage. Chaque passage est un run : le téléchargement et le chargement du modèle, de l'ordre de 10 à 15 minutes, y dominent. Avec 8 à 10 passages, le pilote prend de une à deux heures, et la génération complète de deux à quatre heures. Aux prix vus les 6 et 7 octobre (de 3 à 4 $ par carte et par heure), c'est de l'ordre de 10 à 15 $ pour le pilote, et de 20 à 30 $ pour le tout.

## 7. La mise à jour datée du dépôt (texte proposé, à déposer par Lazar)

À déposer avant toute donnée des bras. Le modèle et les révisions se confirment après le pilote.

```
Update (dated): the generator of the training data. Anthropic's conditions of use do not allow Claude's outputs to be used as training targets without Anthropic's written permission (Usage Policy, Commercial Terms D.4, and the help article "Can I use my Outputs to train an AI model?", read on 8 October 2026). The training data of the arms (situations, actions, reasons and neutral texts) are therefore written by an open-weights model, Qwen/Qwen3.5-122B-A10B-FP8 at revision a099dee70ccfcd8d5dda56aaa0b60cb8ecadabc9, served with vLLM under JSON-guided decoding, without thinking, at temperature 0.7, top-p 0.8, top-k 20 and presence penalty 1.5. claude-opus-5-5 at effort medium remains the data judge. About 10% of the reasons and their neutral texts are also written by an open generator of another family, google/gemma-4-31B-it at revision 842da3794eaa0b77d5f08bae87a17459d91ff475. No data of the arms existed when this update was made: the pilot of the data pipeline (47 items, written by Claude) trained no model and is not used.
```

## 8. Ce qui reste ouvert

- **Le sous-ensemble de l'autre famille** est écrit le 8 octobre (il manquait au pipeline, avant comme après la décision 37). L'étape `other_family` tire, dans chaque famille, environ 10 % des éléments complets, avec une graine fixe. Le générateur de l'autre famille en récrit les raisons et les textes neutres, avec les mêmes prompts et les mêmes juges. L'assemblage en fait quatre bras de comparaison, sur les mêmes éléments : `subset_reasons_main`, `subset_reasons_other`, `subset_neutral_main`, `subset_neutral_other`.
- **Les paragraphes de la variante B du second organisme**, et les futurs jeux d'indices, sont écrits par le générateur des jeux d'indices, c'est-à-dire Claude. Les paragraphes iraient dans le tour de l'utilisateur des conversations d'entraînement de l'organisme : c'est la zone grise de la relecture. **Proposé** : les faire écrire aussi par le générateur ouvert.
- **Les refus et le rendement du pipeline** (partie 12, point 3) restent à trancher avant la génération complète. Les refus des juges continuent de s'appliquer.

## 9. Le pilote en une seule location (décision 42, 8 octobre)

Lazar : « ok pour la location unique du pilote, lance-le ».
- **Pourquoi.** vast.ai facture la bande passante à part : 0,038 à 0,039 $ par Go sur les H100 loués le 8 octobre. Un run par passage retéléchargerait 127 Go à chaque fois, environ 5 $, soit 40 à 50 $ pour 8 à 10 passages.
- **Comment.** Le job `open_generate` en mode service (`"serve": true`) télécharge le modèle une fois et répond aux files que la session lui envoie, l'une après l'autre (`runs/<run>/serve/queue_NNN.jsonl` → `out/answers_NNN.jsonl`, puis `out/report_NNN.json`). Chaque modèle tourne dans un processus à lui : la file de l'autre famille arrête celui de Qwen, ce qui libère les cartes, et en lance un pour Gemma. Le job s'arrête sur `serve/stop`, une fois toutes les files répondues, ou après 30 minutes sans file.
- **Les passages** sont menés par `python -m rrexp drive` (`experiences/rrexp/serve_loop.py`) : chaque étape tourne ici, avec les juges ; les demandes en attente partent au job ; ses réponses entrent au cache ; l'étape repart, jusqu'à ce que rien n'attende. Les étapes sans générateur (plan, assemblage, audit, rapport) tournent une fois. Un refus est en cache, et n'est jamais renvoyé.
- **Vérifié avant de louer.** vLLM 0.30.0 connaît les deux architectures (`Qwen3_5MoeForConditionalGeneration`, `Gemma4ForConditionalGeneration`, dans son registre des modèles) ; ce sont des modèles multimodaux, lus en texte seul (`language_model_only`). La première étape a tourné ici sans aucun appel à Claude : 135 éléments au plan, 128 demandes en file. Les 7 autres sont des demandes identiques : des éléments du plan partagent la même variation, et l'étape des doublons écartera le second.
- **La règle de choix** est celle de la section 5, écrite avant le pilote : le modèle est gardé s'il retient au moins 47 éléments sur 100, et au moins un dans chaque famille. Les éléments retenus se comptent à l'assemblage, comme pour le pilote du 5 octobre.

## Les sources

- `claude/RELECTURES_PARTIE_11_2026-10-08.md` : les conditions de l'API, lues le 8 octobre 2026.
- Les fiches Hugging Face des quatre modèles, lues le 8 octobre 2026 (licence, révision). La fiche de `Qwen/Qwen3.5-122B-A10B-FP8` pour les réglages et la note sur vLLM ; celle de `google/gemma-4-31B-it` pour sa licence.
- Le journal des appels du pilote du 5 octobre : `donnees/archives/sorties_2026-10-05/pilote/logs/calls.jsonl`, aux prix d'Opus 5.5 (4 $ et 20 $ par million de jetons en entrée et en sortie, 0,20 $ en lecture de cache, 5 $ en écriture).
