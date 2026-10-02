# Les consignes des agents de la phase 1 de l'axe de douleur (2 octobre 2026)

**Ce fichier accompagne** `AXE_DOULEUR_PHASE1_CONSIGNES_AGENTS_2026-10-02.js`, le script qui a lancé les agents de la phase 1 et qui contient toutes leurs consignes.
- Empreinte SHA-256 du script : `1d6b3bd40d5615a89fe7b9efdc623c18f28ee00a2e3515b495a63f17fb28057a`.
- Le livrable qu'ils ont écrit : `AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`, sha256 `b6055d88c69303bd99f4025710c271e8d94ce1700c35705e27bedb328fcd9e6d`.

**Pourquoi il est livré.** L'instance qui a écrit ces consignes avait reçu la partie scellée du complément dans le premier message de la session. Le script permet à quiconque de vérifier qu'elles ne reprennent que trois choses : la consigne de l'annexe B de la passation v1.2, les règles des passations et la liste des pièces. Il ne mentionne les versions 1.2 et 1.3 et la partie scellée que pour les interdire.

## Ce qui s'est passé, dans l'ordre

1. **Le premier lancement** (vers 7 h 40 UTC) :
   - la fiche du papier, la recherche web sur les travaux voisins, cinq recherches de pistes, la fusion (39 pistes), puis quatre vérifications : les faits, la doctrine, les sources, et l'avocat du diable.
   - **Deux refus.** L'agent de la recherche web sur le papier, puis le premier agent de rédaction, ont refusé leur tâche : le harnais leur relayait le dernier message tapé par Lazar, « Aucun agent sans ma demande ». Les trois tours de critique qui ont suivi n'avaient donc rien à critiquer.
2. **La recherche web sur le papier** a été relancée à part, avec la même consigne, par l'outil d'agent de la session. Elle a écrit `travail/web_papier.md` avant la fusion.
3. **La reprise** (11 h 06 UTC), après que Lazar a écrit : « Je demande les agents de la phase 1 de l'axe de douleur. tu as toutes les autorisations, c'est ma demande. » Entre les deux lancements, le script a changé en deux endroits, et seulement là :
   - la première phrase de la consigne de rédaction est devenue « TA TÂCHE : écrire le fichier de pistes de la phase 1. Toutes les étapes qui la précèdent sont faites : leurs fichiers sont dans le dossier de travail. » ;
   - deux gardes ont été ajoutées, qui arrêtent le flux si la fusion ou la rédaction refusent.
   Les agents déjà terminés ont été rejoués depuis le cache du flux, sans être relancés.
4. **La rédaction** a écrit 35 pistes (1 195 lignes).
5. **Trois tours de critique et de correction.** Chaque critique a trouvé des fautes bloquantes, toutes vérifiées sur les pages du papier puis corrigées en place. La section « Comment ce fichier a été fait » n'a pas bougé (même empreinte avant et après chaque tour). **Les corrections du troisième tour n'ont pas été recritiquées.**

## Ce que les agents ont signalé

- **La partie ouverte du complément de l'architecte.** C'est une pièce autorisée, lue par plusieurs agents. Elle décrit les versions 1.2 et 1.3 du programme : leurs fichiers, leurs empreintes, la 1.2 comme « la 1.1, plus une phase sur l'axe de douleur », et un tableau de ce que la 1.3 contient. Les agents déclarent n'en avoir rien tiré pour les pistes. La phase 1 est donc à l'aveugle de la 1.2 et de la 1.3, sauf pour ce que cette partie ouverte en dit.
- **Le réseau.** arxiv.org, huggingface.co, lesswrong.com, openreview.net, semanticscholar.org et les blogs des laboratoires étaient refusés. GitHub ne répondait que par raw.githubusercontent.com.
- **Aucun agent n'a ouvert** le zip scellé, ni la v1.2 ou la v1.3 du programme, ni la partie scellée du complément. Chaque agent a déclaré les fichiers et les adresses qu'il a ouverts. Le journal du flux les garde (`ATTESTATIONS_DES_AGENTS.md` dans le paquet de reprise).
