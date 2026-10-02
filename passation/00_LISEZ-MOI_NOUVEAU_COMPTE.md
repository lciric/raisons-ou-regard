# À lire en premier — le programme « Raisons ou regard ? » sur un nouveau compte

Écrit le 2 octobre 2026 vers 9 h 15 par l'instance qui a écrit la passation v1.2. Toutes les heures citées sont à l'heure de Paris.

## Ta situation
- Tu reprends le programme sur un compte neuf. Tu n'as accès ni au Project claude.ai de l'ancien compte, ni à sa mémoire, ni à la conversation de la nuit du 1er au 2 octobre.
- Tout ce qu'il te faut est dans ce zip. Ce fichier dit ce que cela change à la passation. Pour tout le reste, la passation v1.2 fait foi, en particulier ses règles de travail (§1) et les interdits de la phase 1 de la tâche « axe de douleur » (§6 et annexe B).
- Les passations désignent chaque document par son chemin dans l'ancien Project, `claude/NOM.md`. Ici, le fichier porte le même nom, sans le préfixe `claude/`.

## L'ordre de lecture
1. ce fichier ;
2. `PASSATION_PAPIER_v1.2_2026-10-02.md`, en entier ;
3. `PASSATION_PAPIER_v1.0_2026-10-01.md` ;
4. `PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md`, la partie ouverte du complément de l'architecte : son auteur la déclare lisible avant la phase 1 ;
5. les autres documents, dans l'ordre du §2 de la passation v1.2.

Vérifie d'abord les empreintes : `sha256sum -c SHA256SUMS.txt`.

La consigne de l'annexe B fait lire le papier, puis le programme v1.1 et la passation. Tu les auras lus avant le papier, pour reprendre le programme : relis le programme après le papier, comme le veut la consigne.

## Ce que contient ce zip

| Fichier | Ce que c'est | sha256 (16 premiers caractères) |
|---|---|---|
| `PASSATION_PAPIER_v1.2_2026-10-02.md` | La passation relais. Elle reprend tout le contenu de la v1.1, qui n'est pas jointe. | `e5bd33bf90f80110` |
| `PASSATION_PAPIER_v1.0_2026-10-01.md` | La passation du 1er octobre, toujours valable. | `ff5af949fdf4d4f1` |
| `PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md` | La partie ouverte du complément de l'architecte : qui a écrit les versions 1.2 et 1.3, et ce qu'elles reprennent de la 1.1. | `81591a66d2743789` |
| `PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` | Le programme v1.1. | `efbe7be46407b820` |
| `ANTERIORITE_RAPPORTS_2026-10-01.md` | Les 4 rapports bruts du 1er octobre. | `2963f85ce948e432` |
| `ANTERIORITE_RAPPORTS_2026-10-02.md` | Les 7 rapports bruts de la nuit. | `c25c27784ce858f2` |
| `LECTURES_PRIORITAIRES_FICHES_2026-10-01.md` | Les fiches de lecture ; leur partie C est la genèse de l'idée. | `d772b7cada11ea61` |
| `ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md` | Les consignes complètes des sept agents de la nuit, extraites mot pour mot du journal de la session. | `e4a61be719cd9021` |
| `arXiv_2609.16247v2_The_Pain_Axis.pdf` | Le papier de la tâche « axe de douleur », tel qu'arXiv le sert. | `fa4b2bb4b9b6a2bf` |
| `SCELLE_PHASE2_NE_PAS_OUVRIR_AVANT_FIN_PHASE1.zip` | **La partie scellée.** Voir plus bas. | voir `SHA256SUMS.txt` |

**D'où viennent ces copies**
- Les documents tirés de l'ancien Project en sont des copies exactes, octet pour octet, telles que cette session les a lus entre le 1er octobre au soir et le 2 octobre vers 9 h 15.
- Les deux documents du 1er octobre que Lazar avait joints à son premier message sont identiques à ceux du Project.
- Les empreintes complètes sont dans `SHA256SUMS.txt`. Celles du contenu scellé sont dans le zip scellé, et dans la table de la partie ouverte du complément.

## La partie scellée
- `SCELLE_PHASE2_NE_PAS_OUVRIR_AVANT_FIN_PHASE1.zip` contient les versions v1.2 et v1.3 du programme, et la partie scellée du complément de l'architecte.
- La v1.3 est la version de référence (choix de Lazar, le 2 octobre à 8 h 32).
- **Ne le décompresse pas** avant d'avoir rendu à Lazar le fichier de la phase 1 et son empreinte, et qu'il t'ait dit d'y aller. C'est l'interdit de la phase 1, sous une autre forme.

## Ce qui change par rapport à la passation
1. **Les livrables.** La passation les met dans le Project de l'ancien compte, avec le préfixe `claude/`. Ici, sauf autre consigne de Lazar, envoie-les-lui en fichiers, sous les noms prévus, chacun avec son empreinte SHA-256. Toujours en markdown, plus un PDF quand c'est un document à lire.
2. **La mémoire.** Tu n'as pas celle de l'ancien compte. Le paragraphe « La mémoire » du §2 de la passation ne s'applique pas : tout ce qu'il faut est dans ces fichiers.
3. **L'auteur des versions 1.2 et 1.3.** La passation v1.2 le dit inconnu. D'après la partie ouverte du complément, c'est l'instance qui tient le rôle d'architecte du copilote de Lazar, dans le même Project. Elle a aussi écrit la consigne de l'annexe B et les deux parties du complément.
4. **La conversation de la nuit, que tu ne peux pas lire.**
   - Sa question de 7 h 46 sur le cas connu, et la réponse donnée, sont résumées au §5.2 de la passation.
   - L'annexe C renvoie à cette conversation pour le texte complet des consignes d'agents : il est dans `ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md`.
5. **Les renvois à la passation v1.1.** Le fichier des rapports de la nuit et les deux parties du complément renvoient à la passation v1.1. Les sections citées (§4.3, §5.4, §5.5, §6, annexes B et C) sont les mêmes dans la v1.2. Au §6, point 1, la v1.2 note en plus la décision sur la version de référence.
6. **Le « paquet » cité par le complément.** Il cite des PDF des versions du programme, et un PDF du papier annoté par Lazar. Ces fichiers ne sont pas dans ce zip : l'instance qui l'a préparé n'y avait pas accès. Le PDF joint est celui d'arXiv, sans annotations.
7. **Le papier sur l'axe de douleur est joint.**
   - Sa consigne (annexe B) dit « je te joins le papier ». Dans l'ancienne session, il ne l'était pas : il a été téléchargé sur arXiv le 2 octobre à 2 h 09.
   - Une précision de date. D'après l'historique de soumission d'arXiv, la v1 date du 14 septembre 2026 et la v2 du 25 septembre. Le tampon arXiv du PDF dit aussi 25 septembre, et sa première page porte « September 24, 2026 (v2) ». La consigne indique le 1er octobre.
8. **L'environnement.** Ce que la fin de l'annexe C dit des sites que le shell atteint vaut pour l'ancienne session. Vérifie le tien.
9. **Ce que tu n'as pas, et dont tu n'as pas besoin** : la passation v1.1, et les documents du copilote, qui restent à l'autre instance de l'ancien compte.
