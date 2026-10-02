# Raisons ou regard ?

Dépôt privé du programme de recherche « Raisons ou regard ? » : l'entraînement de sûreté par raisons, et la part qu'y prend la conscience d'être évalué. Il remplace le Projet claude.ai de l'ancien compte (« agent ai bras droit conversationel »), que le nouveau compte ne peut pas lire.

Il reste privé : rien n'en sort sans l'accord explicite de Lazar.

## Où est chaque pièce

- `claude/` : les documents du programme, sous le nom qu'ils avaient dans le Projet. Un renvoi `claude/NOM.md` d'une passation mène au fichier `claude/NOM.md` de ce dépôt.
- `papiers/` : les papiers lus pour le programme.
- `passation/` : les pièces de la passation au nouveau compte, et le kit de reprise dans une conversation claude.ai :
  - `COMMENT_REPRENDRE_SUR_CLAUDE_AI.md`, le mode d'emploi pour Lazar ;
  - `PROMPT_LANCEMENT_PAPIER_CLAUDE_AI_MODELE.txt`, le prompt de lancement, dont la session remplit les noms et les empreintes des zips ;
  - `faire_paquet_reprise_session_2026-10-02.sh`, le script qui fabrique le paquet de reprise et le zip scellé.
- `archives/` : la passation v1.1, remplacée par la v1.2. Ne pas la lire : la v1.2 en reprend tout le contenu.

**Pour reprendre le programme, lire d'abord `claude/PASSATION_PAPIER_v1.3_2026-10-02.md`**, la passation de la session Claude Code du 2 octobre, puis la v1.2.

| Fichier | Ce que c'est | sha256 (16 premiers caractères) |
|---|---|---|
| `claude/PASSATION_PAPIER_v1.2_2026-10-02.md` | La passation relais, le document principal (2 octobre, 8 h 40) | `e5bd33bf90f80110` |
| `claude/PASSATION_PAPIER_v1.0_2026-10-01.md` | La passation du 1er octobre, toujours valable | `ff5af949fdf4d4f1` |
| `claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md` | La partie ouverte du complément de l'architecte | `b40904b53395b5c6` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` | Le programme v1.1 (le nom ne porte pas le numéro) | `efbe7be46407b820` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.1_2026-10-01.pdf` | Son PDF (28 pages) | `b00f6c1fcfec7eb4` |
| `claude/ANTERIORITE_RAPPORTS_2026-10-01.md` | Les 4 rapports bruts d'antériorité du 1er octobre | `2963f85ce948e432` |
| `claude/ANTERIORITE_RAPPORTS_2026-10-02.md` | Les 7 rapports bruts de la nuit du 1er au 2 octobre | `c25c27784ce858f2` |
| `claude/ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md` | Les consignes complètes des sept agents de la nuit | `e4a61be719cd9021` |
| `claude/LECTURES_PRIORITAIRES_2026-10-01.md` | La liste des lectures prioritaires | `b3b699c90964dc14` |
| `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md` | Les fiches de lecture ; leur partie C est la genèse de l'idée | `d772b7cada11ea61` |
| `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.pdf` | Leur PDF | `7a4185d6025b3e67` |
| `claude/CONTRE-LECTURE_FICHES_2026-10-01.md` | La contre-lecture des fiches | `577871caf55bb1e3` |
| `papiers/arXiv_2609.16247v2_The_Pain_Axis.pdf` | *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg), tel qu'arXiv le sert | `fa4b2bb4b9b6a2bf` |
| `passation/LISEZMOI_PAQUET_PASSATION_PROGRAMME_2026-10-02.md` | Le LISEZMOI du paquet de passation (9 h 15) | `43e50a30a5d401b8` |
| `passation/MANIFEST_SHA256_PAQUET_PASSATION_PROGRAMME_2026-10-02.txt` | Son manifeste : les 20 empreintes du paquet, pièces scellées comprises | `fba321d86b31d906` |
| `passation/00_LISEZ-MOI_NOUVEAU_COMPTE.md` | Le LISEZ-MOI du zip `RAISONS_OU_REGARD_PASSATION_2026-10-02.zip` (9 h 15) | `af977ada868aad7e` |
| `passation/PROMPT_LANCEMENT_PAPIER_2026-10-02.txt` | Le prompt de lancement de l'instance du papier | `0a5456f3025359ac` |
| `archives/PASSATION_PAPIER_v1.1_2026-10-02.md` | La passation v1.1, remplacée | `0593652589f13663` |

**D'où viennent ces copies.** Ce sont des copies à l'octet de trois sources :
- le paquet `PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02.zip` (sha256 `9ce3082751b2a860…`), vérifié fichier par fichier contre son manifeste : 20 sur 20 ;
- le zip `RAISONS_OU_REGARD_PASSATION_2026-10-02.zip` (sha256 `84db927bd66f9bfa…`), vérifié contre son `SHA256SUMS.txt` : 11 sur 11 ; il fournit le PDF d'arXiv et son LISEZ-MOI ;
- le prompt de lancement, joint à part.

**Deux pièces du paquet ne sont pas reprises.**
- L'exemplaire du papier dit « annoté » (`60a2abfdafd4285c…`). Il a le même texte que celui d'arXiv, et ses pages se rendent à l'identique. Il ne porte aucune note lisible : ses seules annotations sont des liens.
- La copie du complément ouvert que porte le zip `RAISONS_OU_REGARD_PASSATION` (`81591a66d2743789…`) est une version antérieure, qui renvoie encore à la passation v1.1. C'est celle du paquet (`b40904b53395b5c6…`) qui fait foi.

## Ce qui n'est pas encore ici

**Scellé jusqu'à la fin de la phase 1 de la tâche « axe de douleur »** (passation v1.2, §6 et annexe B). Ces pièces entreront dans `claude/` au feu vert de Lazar, après le fichier de pistes indépendantes et son empreinte.

| Pièce | sha256 (manifeste du paquet, 16 premiers caractères) |
|---|---|
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.md` | `fca1f6e9a989d584` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.pdf` | `332fb1c396684c95` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.md`, la version de référence | `a5ef0e51efdb4ba6` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.pdf` | `72ad347d469954e5` |
| `claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_SCELLE_AXE_DOULEUR_2026-10-02.md` | `06b425f7820ca3d3` |

**Ne viendront pas ici** : les documents du copilote (les états `ETAT_D-…`, les banques, les passations de l'architecte). Ils relèvent d'une autre instance.

## Les décisions de Lazar

| Sujet | Décision | Source |
|---|---|---|
| La version de référence du programme | La v1.3 | Passation v1.2, §3, point 9 (2 octobre, 8 h 32) |
| Le calcul | vast.ai, sans limite de budget. Un H100 SXM quand il y en a, sinon un A100 80 Go, et plusieurs GPU à la fois | Passation v1.2, §3, point 1 ; le choix des GPU, confirmé le 2 octobre |
| Les règles pour vast.ai | Aucune clé d'API Claude sur ces machines : les appels partent de la machine de Lazar. Un jeton Hugging Face à accès restreint pour télécharger Llama, révoqué ensuite. Les données et les points de contrôle synchronisés vers un stockage à lui | Proposées dans la passation v1.2, §3, point 1 ; confirmées le 2 octobre |
| L'API Claude | Sans plafond | Passation v1.2, §3, point 2 |
| Le périmètre du pré-enregistrement | Des phases du test des raisons à l'anatomie, plus la phase de validation de l'instrument | Passation v1.2, §3, point 3 ; la validation, ajoutée le 2 octobre |
| La contre-lecture du programme | Une instance vierge, qui reçoit le seul programme et une consigne de contre-lecture, sur la v1.3. Elle vient après la phase 1 de l'axe de douleur, puisque la v1.3 est scellée jusque-là | Passation v1.2, §3, point 6 ; la version, confirmée le 2 octobre |
| Le projet SPAR de Qiyao Wei | « on va tâcher d'y répondre nous-mêmes dans ce programme avant SPAR » | Passation v1.2, §3, point 4 |
| La cible | « plutôt conf principale ou revue ; prestigieux et ambitieux » | Passation v1.2, §3, point 5 |
| Les agents | Seulement à sa demande. Le 2 octobre, il a demandé des agents vierges pour la phase 1 de l'axe de douleur, puis de « tout finir ici » (toute la chaîne, dans la session Claude Code) | Passation v1.2, §1 ; 2 octobre |
| Le périmètre de la session du nouveau compte | Le papier seul ; le copilote va dans une autre session | 2 octobre |
| Les clés et le pilotage des calculs | Lazar pilote depuis une session Claude Code. Il ajoute `HF_TOKEN` et `VAST_API_KEY` en variables d'environnement de l'environnement Claude Code, et il ouvre huggingface.co et vast.ai dans « Network access ». Une conversation claude.ai ne voit pas ces variables | 2 octobre |
| Le dépôt du programme | Ce dépôt, privé, créé par Lazar | 2 octobre |
| Le nom du pré-enregistrement | Son nom seul, avec son ORCID ; Claude n'est pas auteur, une phrase de méthode dit que le protocole a été rédigé avec son aide | 2 octobre |
| Les contacts avec Cadile et Lundqvist | « non pas encore » ; aucun moment fixé | 2 octobre |
| Le lieu du pré-enregistrement | OSF Registries, sous embargo jusqu'au post ; en deux temps (le texte en semaine 1, l'amendement gelé après le pilote) | Passation v1.2, §3, point 3 ; confirmé le 2 octobre |
| La mini-spec v0.1 | Adoptée : les dix principes et la matrice, le cadrage neutre, la balise vide, le texte neutre reformulé, le filtre de la conscience d'évaluation, la demande nuisible sans contenu dangereux ; seuils provisoires | 2 octobre |

**Ouvert** : les neuf choix du pipeline de données (§4 de `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`).

## Où en est le travail (2 octobre 2026)

1. Les pièces sont vérifiées (voir plus haut).
2. **La tâche « axe de douleur ».**
   - La phase 1 est en cours. Elle est confiée à des agents vierges, à la demande de Lazar. La raison : la partie scellée du complément était jointe au premier message de la session, et l'instance qui tient le papier l'a donc lue.
   - Le livrable : `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`, gelé par son empreinte. Les consignes exactes des agents seront livrées à part, avec leur propre empreinte.
   - Ensuite, au feu vert de Lazar :
     - la phase 2, `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md` ;
     - des propositions pour la version qui suivra la v1.3, sans l'écrire.
3. **La carte des angles déjà pris** (passation v1.2, §6, point 3) : écrite par des agents, en cours de correction.
4. **Les étapes 3 à 6 de la passation v1.0** (§5) :
   - la mini-spec et les dix familles : v0.1 adoptée le 2 octobre (`claude/MINI_SPEC_ET_FAMILLES_v0.1_2026-10-02.md`) ;
   - le pipeline de données : v0.1 écrite et testée hors ligne (`donnees/`, conception dans `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`) ; le pilote attend `RR_ANTHROPIC_API_KEY`, `HF_TOKEN` et l'accès à huggingface.co ;
   - l'organisme de validation, reconstruit depuis les documents publics de Hua et al. ;
   - le pré-enregistrement, sur OSF, en deux temps.

## Les règles de travail

Celles de la passation v1.2 (§1) et du prompt de lancement. En particulier :
- En français, précis, direct. Aucune idée désignée par une lettre ou un sigle.
- Chaque fait a sa source, et ce qui n'est pas vérifié est dit tel. « to our knowledge », jamais « first ».
- La doctrine du contrôle :
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.
- Aucun agent sans la demande de Lazar. Un refus d'un modèle ou d'une API ne se rejoue pas et ne se reformule pas.
- Aucune clé ni aucun jeton dans ce dépôt, ni dans une conversation.

## L'environnement des sessions cloud

Au 2 octobre, la politique réseau de l'environnement refuse arxiv.org, huggingface.co, lesswrong.com, alignmentforum.org, openreview.net, semanticscholar.org, openalex.org, alignment.anthropic.com et transformer-circuits.pub. Le moteur de recherche et GitHub répondent. Ouvrir ces domaines dans les réglages de l'environnement deviendra nécessaire :
- pour les relectures sur source de la carte des angles ;
- pour tout téléchargement de modèle.
