# Passation relais — le programme « Raisons ou regard ? » (v1.3, 2 octobre 2026)

Cette passation est destinée à l'instance qui reprend le programme après la session Claude Code du 2 octobre 2026, ouverte sur le nouveau compte de Lazar. Elle complète :
- la passation v1.2 (`claude/PASSATION_PAPIER_v1.2_2026-10-02.md`), qui reste le document de fond ;
- la passation v1.0 (`claude/PASSATION_PAPIER_v1.0_2026-10-01.md`).

Toutes deux restent valables pour tout ce que celle-ci ne change pas.

**Deux précautions.**
- Les numéros de version des passations ne suivent pas ceux du programme : cette passation v1.3 n'a rien à voir avec le programme v1.3.
- Elle ne contient rien de la partie scellée. Tu peux la lire avant la fin de la phase 1 de la tâche « axe de douleur ».

**L'ordre de lecture**
1. Cette passation, en entier.
2. La passation v1.2, en entier.
3. La passation v1.0.
4. La partie ouverte du complément de l'architecte (`claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md`).
5. Le reste, dans l'ordre du §2 de la passation v1.2, sauf ce qui est scellé.

Sauf mention contraire, « la session » désigne la session Claude Code qui a écrit ce document.

---

## 1 · Ce que la session a fait

**Le rôle.** Lazar lui a donné deux prompts de lancement, celui du papier et celui de l'architecte du copilote, qui s'excluent l'un l'autre. Il a choisi : **le papier seul**. Le copilote va dans une autre session, et ses documents ne te concernent pas.

**Les pièces vérifiées**

| Pièce | sha256 | Résultat |
|---|---|---|
| `PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02.zip` (9 h 15) | `9ce3082751b2a860…` | Conforme au prompt ; 20 fichiers sur 20 conformes à son manifeste |
| `RAISONS_OU_REGARD_PASSATION_2026-10-02.zip` (9 h 14) | `84db927bd66f9bfa…` | 11 fichiers sur 11 conformes ; son zip scellé n'a pas été ouvert |
| Un second paquet du programme, de 9 h 00 | `aff5ef181012e859…` | Version antérieure : il porte la passation v1.1 et pas la v1.2. Écarté |

**Trois écarts relevés dans les passations**, aucun bloquant :
1. **La version 1.4.**
   - La partie ouverte du complément dit à l'instance du papier d'écrire elle-même la version 1.4.
   - La consigne de l'annexe B et le prompt de lancement disent « sans l'écrire : je décide ».
   - C'est la consigne qui fait foi.
2. **Les deux copies de la partie ouverte du complément.**
   - Celle du zip `RAISONS_OU_REGARD_PASSATION` (`81591a66d2743789…`) est antérieure : elle renvoie encore à la passation v1.1 et laisse ouverte la version de référence.
   - Celle du paquet (`b40904b53395b5c6…`) fait foi.
3. **La date du papier.**
   - La consigne date la version 2 de *The Pain Axis* du 1er octobre.
   - D'après le LISEZ-MOI du nouveau compte, arXiv la date du 25 septembre, et sa première page porte « September 24, 2026 (v2) ».
   - Non revérifié sur arXiv, que le réseau refusait.

**L'exemplaire « annoté » du papier ne porte aucune note.** C'est le fichier `60a2abfdafd4285c…`.
- Son texte est identique à celui d'arXiv.
- Ses pages se rendent à l'identique (comparées à 40 points par pouce).
- Ses seules annotations sont des liens.
- Si Lazar avait annoté le papier, ses notes se sont perdues à l'export.

**La phase 1 de la tâche « axe de douleur » a été confiée à des agents.**
- **Pourquoi.** Lazar a joint la partie scellée du complément au premier message de la session. Son texte est donc entré dans le contexte de la session avant toute lecture, et la session ne pouvait plus chercher à l'aveugle.
- **Le choix de Lazar.** La session le lui a dit. Il a choisi de confier la phase 1 à des agents vierges, lancés par la session, puis de « tout finir ici ».
- **Ce qu'ils ont reçu.** Ils ne lisent qu'un dossier propre :
  - le papier, tel qu'arXiv le sert, et son texte extrait page par page ;
  - le programme v1.1 ;
  - la passation v1.2 ;
  - la partie ouverte du complément ;
  - les deux fichiers de rapports d'antériorité.
- **Ce qu'ils ont produit.** Leurs consignes, les fichiers qu'ils ont écrits et leurs déclarations de fichiers ouverts sont dans le paquet de reprise (§3).
- **Ce que la session a vérifié.** Aucun journal d'agent ne contient de texte de la partie scellée.

**Le dépôt GitHub du programme.**
- Lazar a créé le dépôt privé `lciric/raisons-ou-regard`. La session n'avait pas le droit de créer un dépôt.
- La session y a poussé, sur `main`, toutes les pièces non scellées, à l'octet (premier commit `ce9e76d`).
- Les pièces y gardent leur nom du Projet, dans `claude/`. Un renvoi `claude/NOM.md` d'une passation mène donc au même fichier.
- Le README du dépôt tient l'état, les décisions et les empreintes.
- Les pièces scellées n'y entrent qu'au feu vert de Lazar, après la phase 1 : une instance qui lirait le dépôt les verrait.

**Le réseau de l'environnement Claude Code** (au 2 octobre) :
- **Refusés** : arxiv.org, huggingface.co, lesswrong.com, alignmentforum.org, openreview.net, semanticscholar.org, openalex.org, alignment.anthropic.com et transformer-circuits.pub.
- **Accessibles** : le moteur de recherche (titres, adresses et extraits) et GitHub (github.com, api.github.com, raw.githubusercontent.com).
- Ce qui n'a été vu que par un extrait de recherche est marqué tel.

---

## 2 · Les décisions de Lazar, le 2 octobre

Elles s'ajoutent à celles du §3 de la passation v1.2.

1. **Le rôle de la session** : le papier seul.
2. **La phase 1 de l'axe de douleur** : faite par des agents vierges ; puis « tout finir ici », avec toute la chaîne (fusion, vérifications, rédaction, critique).
3. **Le périmètre du pré-enregistrement** : il comprend la phase de validation de l'instrument, en plus des phases du test des raisons à l'anatomie.
4. **Le calcul** : un H100 SXM quand il y en a, sinon un A100 80 Go, et plusieurs GPU à la fois. Les trois règles pour vast.ai sont confirmées :
   - aucune clé d'API Claude sur ces machines ;
   - un jeton Hugging Face à accès restreint, révoqué ensuite ;
   - les données et les points de contrôle synchronisés vers un stockage à lui.
5. **La contre-lecture vierge** porte sur la v1.3. Elle vient après la phase 1 de l'axe, puisque la v1.3 est scellée jusque-là.
6. **Les clés : Lazar pilote depuis une session Claude Code.**
   - Il ajoute `HF_TOKEN` et `VAST_API_KEY` en variables d'environnement, dans les réglages de l'environnement Claude Code (le menu de la barre de titre de la session, puis « Edit »).
   - Il ouvre huggingface.co et vast.ai dans « Network access ».
   - Une nouvelle session les prend en compte.
   - Cela ne vaut que pour une session Claude Code. Une conversation claude.ai ne voit pas ces variables : elle prépare les calculs, une session Claude Code les lance.
   - Aucune clé, aucun jeton ne passe jamais dans une conversation ni dans le dépôt.
7. **Le dépôt GitHub** : `lciric/raisons-ou-regard`, privé, devient la maison du programme.
8. **Le nom du pré-enregistrement** : son nom seul, avec son ORCID. Claude n'est pas auteur : une phrase de méthode dit que le protocole a été rédigé avec son aide. C'était la recommandation de la session ; sa raison : le pré-enregistrement date l'idée à son nom, et un nom d'équipe ou un pseudonyme affaiblirait cette preuve.
9. **Les contacts avec Cadile et Lundqvist** : « non pas encore ». Aucun moment n'est fixé : la question reste à reposer plus tard.
10. **La carte des angles déjà pris** : écrite par des agents, tout de suite, en parallèle de la phase 1 (un agent par angle, plus les projets et le calendrier, les corrections et une veille du 2 octobre ; un vérificateur indépendant par fichier ; une synthèse ; une critique).
11. **Le cours d'alignement** (v3.5, un document du copilote, en français et en anglais) : Lazar a demandé d'y ajouter l'explication du 2 octobre sur les sondes de désalignement (pourquoi un organisme modèle, J-lens compris ; comment les entraîner ; le hors-distribution), bien en évidence, et des avertissements partout sur les limites de chaque instrument et leurs parades. C'est fait par des agents, en v3.6. Le cours relève aussi de l'instance de l'architecte du copilote : il faudra lui transmettre la v3.6, pour qu'il n'y ait pas deux v3.6 divergentes.
12. **Le lieu du pré-enregistrement** : OSF Registries, sous embargo jusqu'au post (confirmé par Lazar le 2 octobre). En deux temps : le texte en semaine 1, puis un amendement gelé après le pilote, avant toute donnée du test du regard (passation v1.2, §3, point 3).
13. **La mini-spec** : Lazar a demandé de l'attaquer le 2 octobre ; la session en écrit une première version, à valider par lui (`claude/MINI_SPEC_ET_FAMILLES_v0.1_2026-10-02.md`).
14. **La mini-spec v0.1 est adoptée** (2 octobre, vers 14 h) : « oui à tout » pour les décisions 2 à 6 de son §12, puis, après relecture des dix principes et de la matrice, « c'est parfait, go » pour la décision 1. Les seuils restent provisoires jusqu'à la simulation de puissance ; le mot inventé attend la vérification du tokenizer.
15. **Le pipeline de données** : « attaque le pipeline de données ». La session en écrit la v0.1, testée hors ligne (`donnees/`, et sa conception dans `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`). Neuf choix du code y sont à trancher (son §4), et le pilote attend `RR_ANTHROPIC_API_KEY` (la clé de l'API Claude, sous ce nom pour que Claude Code ne la prenne pas pour lui), `HF_TOKEN` et l'accès à huggingface.co.

**Encore ouvert** : aucune décision du §6, point 1 de la passation v1.2. Les décisions propres à la mini-spec sont listées dans son dernier chapitre.

---

## 3 · La tâche « axe de douleur » : l'état final

> Cette section est mise à jour au moment de fabriquer le paquet de reprise. En cas de doute, fie-toi au contenu de `05_AXE_DOULEUR_PHASE1/` dans le paquet.

<!-- ETAT_A_METTRE_A_JOUR_AVANT_LE_PAQUET -->
**État provisoire au 2 octobre, vers 10 h 15 (heure de Paris) : la phase 1 est en cours.**
- **Écrit** :
  - la fiche du papier, `travail/fiche_papier.md`, avec chaque point rapporté à sa page ;
  - les travaux voisins, `travail/web_voisins.md`. Le dossier `travail/web_voisins_sources/` y ajoute neuf README de dépôts GitHub liés au papier ou à des sujets proches, lus par raw.githubusercontent.com.
- **En cours** : les recherches de pistes, deux à la fois.
- **Relancé à part** : la recherche web sur le papier lui-même. Son premier agent l'avait refusée (§5) ; la session l'a relancée avec la même consigne, hors du workflow, pour qu'elle soit écrite avant la fusion.
- **Reste à faire** : la fin des recherches de pistes, la fusion, quatre vérifications, la rédaction et la critique.
- Lazar a choisi de tout finir dans la session Claude Code.

**Les règles qui ne changent pas**
- La phase 1 se termine quand le fichier `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` est écrit, que son empreinte SHA-256 est donnée à Lazar, et qu'on ne le modifie plus.
- La phase 2 ne commence qu'au feu vert de Lazar. Il donne alors le zip scellé. On lit la v1.2, puis la v1.3 et la partie scellée du complément.
- On écrit ensuite `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md`. Il compare les pistes à la v1.2, puis aux ajouts de la v1.3, et dit aussi ce que la v1.3 a changé sur l'axe par rapport à la v1.2.
- Enfin, on propose ce qui devrait entrer dans la version qui suivra la v1.3, sans l'écrire : Lazar décide.

**Si la phase 1 n'est pas finie quand tu reprends**
- Tu es vierge tant que tu n'as ouvert ni le zip scellé ni aucune pièce qui parle des versions 1.2 et 1.3. Tu peux donc faire la phase 1 toi-même, comme le voulait la consigne : seule, à l'aveugle.
- Tu peux t'appuyer sur ce que les agents ont écrit, dans `05_AXE_DOULEUR_PHASE1/travail/`. C'est écrit à l'aveugle, mais ce sont des sorties de modèles : à vérifier sur le papier.
- Dis dans le fichier de pistes ce que tu as repris d'eux.

---

## 4 · Ce qui reste à faire, dans l'ordre

1. **Faire trancher par Lazar les neuf choix du pipeline de données** (§4 de `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`). Les décisions de la mini-spec sont prises (§2, point 14).
2. **La tâche « axe de douleur »** : finir la phase 1 s'il le faut, puis la phase 2 et les propositions, au feu vert de Lazar.
3. **La contre-lecture vierge de la v1.3**, après la phase 1.
   - Une instance qui n'a rien lu du programme reçoit la v1.3 et une consigne de contre-lecture, écrite par toi.
   - Les relevés du §5.4 de la passation v1.2 ne vont à son dossier qu'après sa lecture. Vérifie d'abord lesquels valent encore pour la v1.3.
   - Dans claude.ai, une conversation neuve, hors du Projet du programme, fait une instance vierge.
4. **La carte des angles déjà pris** (passation v1.2, §6, point 3).
   - Écrite par des agents le 2 octobre (§2, point 10) : `claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` (sha256 `7744a85cf528d6ff3f75ead74a39447fea97793944e43ab5e608f6371ed764d6`), 1 205 lignes. Trois tours de critique et de correction ; les corrections du troisième tour n'ont pas été recritiquées. Le travail des agents (fiches d'angle, vérifications, veille, corrections) est dans `08_CARTE_DES_ANGLES/` du paquet de reprise.
   - Son corps peut s'écrire avant la fin de la phase 1 ; ses conséquences pour la v1.3 attendent la phase 2.
   - Il faut d'abord relire sur la source ce qu'on veut citer au centre et qui n'est marqué que « rapport » : Nakamura, Zeisler, Second Look Research, les J-lens de Neuronpedia.
5. **Les étapes 3 à 6 de la passation v1.0** (§5) :
   - la mini-spec et les dix familles : la v0.1 est écrite et adoptée (`claude/MINI_SPEC_ET_FAMILLES_v0.1_2026-10-02.md`) ; à rapprocher de la v1.3 après la phase 2 ;
   - le pipeline de données : la v0.1 est écrite et testée hors ligne (`donnees/`, `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`). Restent : faire trancher ses neuf choix (§4), lancer le pilote dès que les clés sont là, puis écrire les scénarios tenus à part avec leurs harnais, les jeux d'indices, les paires de concepts et le jeu de calibration du juge (§8 du document) ;
   - l'organisme de validation, reconstruit depuis les documents publics de Hua et al. ;
   - le pré-enregistrement.
6. **Les calculs**, quand tout cela est prêt : depuis une session Claude Code qui a `HF_TOKEN`, `VAST_API_KEY` et le réseau ouvert (§2, point 6).

---

## 5 · Ce que la session a appris, pour ne pas le refaire

- **Les agents lancés par un workflow reçoivent le dernier message tapé par Lazar, relayé mot pour mot.**
  - Ce message prime sur la consigne calculée par le script.
  - Le 2 octobre, ce message disait « Aucun agent sans ma demande ». Son accord pour la phase 1 était venu par un clic dans un questionnaire, que le harnais ne relaie pas. Un agent a donc refusé sa tâche, et d'autres pouvaient le faire.
  - Quand Lazar demande des agents, il faut que la demande soit écrite dans son message.
- **Une pièce scellée jointe au premier message d'une session rompt l'aveugle de cette session.** Le zip scellé reste à part, hors du Projet et hors du dépôt, jusqu'au feu vert.
- **La machine de la session n'avait que 4 processeurs.** Un workflow n'y fait tourner que deux agents à la fois, et une chaîne de seize agents prend des heures.
- **Lire un PDF en images coûte cher.** Le texte extrait page par page suffit, sauf pour les figures qui portent un résultat.
- **L'intégration GitHub de la session ne peut pas créer de dépôt.** Lazar le crée ; la session le rattache, puis elle y pousse.

---

## 6 · Les pièces

Les empreintes de toutes les pièces sont dans le `MANIFEST_SHA256.txt` du paquet de reprise. Le README du dépôt `lciric/raisons-ou-regard` les donne aussi.
