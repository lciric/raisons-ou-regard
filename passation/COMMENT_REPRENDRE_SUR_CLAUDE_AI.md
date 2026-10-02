# Reprendre le programme dans une conversation claude.ai

Pour Lazar. La session Claude Code du 2 octobre fabrique, à la fin, quatre fichiers :
- le paquet de reprise, `PACK_REPRISE_RAISONS_OU_REGARD_<date>_<heure>.zip` : tout ce qui n'est pas scellé, plus le travail de la session ;
- le zip scellé, `SCELLE_NE_PAS_OUVRIR_AVANT_FEU_VERT_<date>_<heure>.zip` : les versions 1.2 et 1.3 du programme, et la partie scellée du complément ;
- le prompt de lancement, `PROMPT_LANCEMENT_PAPIER_CLAUDE_AI_<date>_<heure>.txt`, avec les noms et les empreintes des deux zips ;
- la passation v1.3 en clair, `PASSATION_PAPIER_v1.3_2026-10-02.md`.

## Les étapes

1. **Crée un Projet sur claude.ai**, par exemple « Raisons ou regard ? ». Tu peux coller dans ses instructions le bloc « LES RÈGLES » du prompt de lancement : elles vaudront pour toutes ses conversations.
2. **Active l'exécution de code et la création de fichiers** dans les réglages de claude.ai, si ce n'est pas déjà fait. Le nom et l'emplacement du réglage peuvent varier selon l'offre. Sans lui, l'instance ne peut ni extraire le zip ni vérifier les empreintes.
3. **Ouvre une conversation dans ce Projet.** Joins-y le paquet de reprise, et colle le prompt de lancement.
4. **Garde le zip scellé hors de tout.**
   - Ne le joins pas, et ne le mets ni dans les fichiers du Projet ni dans le dépôt.
   - Une instance qui l'aurait vu ne pourrait plus faire la phase 1 à l'aveugle.
   - Donne-le seulement quand le fichier de pistes indépendantes est écrit et que son empreinte t'a été donnée, avec ton feu vert pour la phase 2.
5. **Si tu veux que chaque conversation du Projet voie les pièces sans zip** : le connecteur GitHub de claude.ai peut synchroniser le dépôt `lciric/raisons-ou-regard` dans le Projet. Le dépôt ne contient rien de scellé. Les pièces scellées n'y entreront qu'après ton feu vert.
6. **Les livrables.** L'instance claude.ai te les envoie en fichiers, chacun avec son empreinte. Ajoute-les aux fichiers du Projet, puis au dépôt : par l'interface web de GitHub, ou par une session Claude Code.
7. **Les calculs GPU** se lancent depuis une session Claude Code ouverte sur le dépôt `lciric/raisons-ou-regard`, une fois :
   - `HF_TOKEN` et `VAST_API_KEY` ajoutées dans les variables d'environnement de l'environnement Claude Code ;
   - huggingface.co et vast.ai ouverts dans « Network access ».

   Une conversation claude.ai ne voit pas ces variables : elle prépare les calculs, la session Claude Code les lance. Ne colle jamais une clé ni un jeton dans une conversation.
8. **Quand une conversation devient longue**, demande à l'instance une passation, puis repars dans une conversation neuve du même Projet, avec cette passation.

## La contre-lecture vierge

Elle porte sur la v1.3, après la phase 1 de l'axe de douleur. Pour qu'elle soit vierge, ouvre une conversation **hors** du Projet du programme, et donne-lui seulement la v1.3 et la consigne de contre-lecture que l'instance du programme t'aura écrite.
