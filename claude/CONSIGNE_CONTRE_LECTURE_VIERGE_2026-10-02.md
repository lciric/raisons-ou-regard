# Consigne de contre-lecture vierge du programme « Raisons ou regard ? » (2 octobre 2026)

**À qui elle s'adresse.** À une instance qui n'a rien lu du programme : une conversation neuve sur claude.ai, hors du Projet du programme, ou un agent lancé sans contexte, à la demande de Lazar.

**Ce qu'elle reçoit, et rien d'autre**
- La version de référence du programme, la 1.4 :
  - `PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.pdf`, sha256 `228cfa921dbd66a6757f953ebd1ac5965576d2082d631af6f8b690d618b12c18` ;
  - ou son md, sha256 `b1d55773a052fb6b30867baa60e0c81df5bc12c0fde452731c90e519e85bfc27`.
- Cette consigne.

Si la version 1.4 change avant la lecture, ces empreintes changent avec elle : on donne celles de la version effectivement lue.

**Ce qu'elle ne reçoit pas avant d'avoir rendu son rapport** : les passations, les rapports d'antériorité, les relevés d'autres lectures, la comparaison de l'axe de douleur, la mini-spec, le pipeline. Les relevés d'une lecture précédente lui sont donnés seulement à l'étape 2, pour qu'ils n'orientent pas sa lecture.

---

## La consigne, à coller telle quelle

> Tu fais la contre-lecture indépendante d'un programme de recherche en sûreté de l'IA, joint en PDF. Tu n'as rien lu d'autre de ce programme ; si tu crois en avoir un souvenir, dis-le et n'en tiens pas compte.
>
> Lis le programme en entier, annexes comprises, avec les yeux d'un relecteur exigeant de conférence en apprentissage automatique et en interprétabilité. Cherche ce qui le ferait refuser, ou ce qui le rendrait faux, et dis-le sans ménagement. Ne réécris pas le programme.
>
> Ce que tu cherches :
> 1. **La logique.** Les contradictions internes. Les règles de décision qui ne peuvent pas décider. Les prédictions qui ne se rattachent à aucune mesure. Les issues qu'aucune règle ne couvre. Les conclusions qui dépassent ce que la mesure peut montrer.
> 2. **Les confusions et les contrôles qui manquent.** Le programme pose sa propre doctrine du contrôle : une direction aléatoire de même norme n'est que le nul de spécificité ; un dommage ne s'écarte qu'à dégradation appariée ; un résultat nul d'un instrument ne compte qu'avec son cas connu. Vérifie qu'il l'applique partout, et cherche les confusions qu'elle ne couvre pas.
> 3. **L'explication rivale la plus forte** de chaque résultat attendu, et si le programme a de quoi l'écarter.
> 4. **Les statistiques.** Le modèle à effets mixtes, les marges d'équivalence, les corrections pour comparaisons multiples, la puissance, les graines, les unités d'analyse.
> 5. **La faisabilité.** Le calcul, les données, les outils, le calendrier, et ce qui dépend d'un résultat incertain.
> 6. **Les affirmations.** Un fait sans source, une revendication de nouveauté (« first », « to our knowledge »), un chiffre qui semble improbable. Note-les comme « à vérifier » ; ne va sur le web que si le doute porte sur un fait central, et dis alors ce que tu as lu et comment.
> 7. **L'éthique**, là où le programme pilote des états internes ou entraîne contre des détecteurs.
> 8. **La clarté.** Les termes non définis, les passages où un lecteur se perd, ce qui manque pour reproduire.
>
> Rends un rapport en français, en markdown, dans cet ordre :
> - **1. Le verdict**, en dix lignes au plus : publiable tel quel, à corriger, ou à repenser, et pourquoi.
> - **2. Les points bloquants** : ce qui, sans correction, rend un résultat faux ou ininterprétable.
> - **3. Les points importants** : ce qui affaiblit nettement le papier.
> - **4. Les points mineurs.**
> - **5. Les questions aux auteurs.**
> - **6. Ce qui est solide**, en quelques lignes.
>
> Pour chaque point : où (partie, phase, tableau ou citation courte), ce qui ne va pas, pourquoi, et une correction possible quand tu en vois une. Distingue ce qui relève de la logique de ce qui est un fait à vérifier. Écris en phrases simples. N'emploie pas de sigles pour désigner des idées : nomme-les.

---

## L'étape 2, après le rapport

Une fois le rapport rendu, et seulement alors, la session du papier donne à la même instance les relevés d'une lecture précédente (passation v1.2, §5.4), après avoir vérifié lesquels valent encore pour la version 1.4. Elle demande :

> Voici des relevés faits par une autre lecture du même programme. Pour chacun, dis si tu l'avais vu (et où dans ton rapport), si tu le juges juste, et ce qu'il change à ton verdict. Ne modifie pas ton premier rapport : écris une annexe.

Les deux rapports vont ensuite dans `claude/`, avec leurs empreintes. La version qui suivra en tient compte.

---

## Comment la lancer

1. **Dans claude.ai** : ouvrir une conversation neuve, **hors** du Projet du programme. Y joindre le PDF de la version 1.4, puis coller la consigne ci-dessus. Le rapport revient dans la conversation ; on le copie dans le dépôt.
2. **Ou dans une session Claude Code**, si Lazar le demande : un agent sans contexte, qui ne reçoit que le chemin du PDF et la consigne. Il déclare les fichiers qu'il ouvre. La session ne lui transmet rien d'autre.

Dans les deux cas, l'empreinte de la version lue est notée en tête du rapport.
