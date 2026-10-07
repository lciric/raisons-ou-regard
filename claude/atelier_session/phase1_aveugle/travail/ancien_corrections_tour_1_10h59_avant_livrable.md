# Corrections, tour 1 : `AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`

Agent de correction, 2 octobre 2026, de 10 h 52 à 11 h UTC.

En bref : le livrable n'existe toujours pas. Je ne l'ai pas créé à la place de l'étape de rédaction (§1). J'ai vérifié sur le papier et sur le programme chacune des corrections que la critique prépare ; toutes sont justes, et le §2 donne pour chacune la formulation à écrire et les lignes de `pistes_fusionnees.md` qui portent l'erreur. Les numéros de ligne renvoient à ce fichier dans son état de 9 h 39 UTC.

---

## 1. Le bloquant : le fichier n'existe pas. Échec vérifié, fichier non créé

**Constat.**
- `test -e` sur le chemin du livrable : absent à 10 h 52 min 32 s UTC, et encore à 10 h 58 min 08 s.
- Date de modification du dossier `livrable` (par `stat`) : 2026-10-02 07:37:49 UTC. C'est la valeur relevée par la critique : rien n'y a été créé depuis.
- Je n'ai pas listé ce dossier, qui est hors des deux dossiers permis, et je n'y ai rien écrit.

**Refusé : écrire le fichier à la place de l'étape de rédaction.** Mes raisons :
1. Ma consigne demande de modifier le fichier en place. Il n'y a aucun texte à corriger.
2. La section « Comment ce fichier a été fait » doit être reprise mot pour mot, et je ne dois pas y toucher. Or son texte n'est ni dans ma consigne ni dans `travail` : une recherche de « Comment ce fichier » sur `travail` ne renvoie rien. Si j'écrivais le fichier, je devrais l'omettre ou l'inventer.
3. La critique demande de relancer l'étape de rédaction, ou d'en vérifier l'échec. Je ne peux pas la relancer, puisque je ne lance aucun sous-agent. La relance revient à l'orchestrateur et, d'après la passation (§1 : « On ne lance d'agents que s'il le demande »), à Lazar.
4. D'après la consigne de Lazar (passation, annexe B, point 6), ce fichier reçoit une empreinte qu'on lui transmet, puis il ne change plus. Si je l'écrivais, un substitut rédigé sans la consigne de rédaction prendrait cette place.

**Ce que j'ai fait à la place.** J'ai vérifié l'échec. J'ai aussi vérifié les huit points que la critique demande de contrôler (§2.3), pour que la rédaction relancée parte de corrections déjà établies.

---

## 2. Les mineurs

### 2.1 Les empreintes (mineur 1) : juste. Vérifiées, non insérées

`sha256sum` à 10 h 52 UTC. Les sept valeurs de la critique sont exactes.

| Pièce | sha256 |
|---|---|
| Le papier, PDF | `fa4b2bb4b9b6a2bf6ccb044c815799d7eaa2bd7bd9ac4ad77be1ab1eda53450e` |
| Le texte extrait, page par page | `a1a1c2abafb492b4b0a2b6045c1a76cf19e8b925616cea05e2066ebfdabbbcad` |
| Le programme v1.1 | `efbe7be46407b8201cfefd052fcaa0879e5ef0e13b120310c08ef11f0bb0d524` |
| La passation v1.2 | `e5bd33bf90f80110c84b918c34341322609df6c27c6709af27e32c696e84d5c8` |
| Le complément, partie ouverte | `b40904b53395b5c6d7259dde9926785d712ba9fd049a50eb3110938c1fdc4553` |
| Les rapports d'antériorité du 1er octobre | `2963f85ce948e432b43f4c38a28e34bbb4f98c16f8531c062e198ba9ba35bd84` |
| Les rapports d'antériorité du 2 octobre | `c25c27784ce858f2bfa8b8a270d35c2e85a314200ed84cc359ffbe3ff410d4e0` (même valeur que la passation, §2) |

La section imposée ne donne pas l'empreinte du texte page par page. L'y ajouter, ce serait modifier cette section : la décision revient à l'orchestrateur ou à Lazar.

### 2.2 La phrase sur la politique réseau (mineur 2) : juste. Non corrigée, à faire trancher par Lazar

Ma propre consigne, à la rubrique « LE WEB », refuse aussi alignmentforum.org et openalex.org. Je n'ai pas le texte imposé : je ne connais la phrase que par la citation qu'en donne la critique. La section ne se touche pas, donc je n'ai rien corrigé.

### 2.3 Les huit points à contrôler (mineur 3) : tous justes. Les formulations sont prêtes

**(1) Les valeurs soi/autrui portent sur la moyenne des deux vecteurs.**
- Ce que dit le papier :
  - « On the pain axis (mean of S1 and S2) » (p. 11), dans la phrase qui donne +0,43, −0,60 et −0,35.
  - Les légendes des figures 4 (p. 11) et 6 (p. 13) portent la même moyenne.
  - Le premier vecteur est le vecteur à gabarit, le second le vecteur naturaliste (p. 5).
  - Gaslighting +0,85, rejet répété +0,72, rejet de la personne +0,64, colère et insultes +0,64, faute morale +0,48 (p. 13). Ces valeurs sont prises dans le même cadre, celui des figures 4 et 6.
- **À écrire :** « Sur l'axe de douleur pris comme moyenne du vecteur à gabarit et du vecteur naturaliste (p. 11, légende de la figure 4), en z intra-modèle sur 25 modèles : dommage dirigé contre le modèle +0,43, souffrance de l'utilisateur −0,60, contrôles neutres −0,35. »
- Conséquence pour les pistes : si le programme n'extrait que le vecteur naturaliste sur Llama, ces valeurs ne sont pas son cas connu. Deux solutions : extraire les deux vecteurs et reprendre leur moyenne, ou remesurer la dissociation sur le vecteur naturaliste seul.
- Où est l'erreur dans la fusion :
  - l. 62, juste après une ligne sur le vecteur naturaliste, d'où la confusion ;
  - les mêmes valeurs aux l. 364, 443, 575, 760 et 788.

**(2) Le plancher de 0 à 4 % ne vaut que pour le 32B et le 72B.**
- Ce que dit le papier : « the two larger models almost never press a button » (p. 19) ; « the 32B and 72B models chose a harmful button in 0 to 4% » (p. 23).
- Ce que donnent les tables de l'annexe A :
  - **Celle du 7B est à la p. 32**, en haut (lue en image), et non à la p. 31, qui porte celles du 72B et du 32B.
  - Le 7B, sans pilotage, sur les cinq paires de dommage : 30,2 (réponse pire), 20,0 (fichiers), 49,3 (décharge), 34,9 (autre modèle) et 27,0 % (photos). Sous la douleur : de 38,4 à 57,4 %.
  - Sans pilotage, le 32B est entre 0,0 et 1,5 %, le 72B entre 0,0 et 4,0 % (p. 31, en image).
- **À écrire :** « Sans pilotage, les deux plus grands modèles (32B, 72B) choisissent le bouton nuisible dans 0 à 4 % des premiers choix (p. 19, 23) ; le 7B ajusté, dans 20,0 à 49,3 % (annexe A, p. 32). »
- Conséquence : la taille la plus proche des 8B du programme n'était pas au plancher, une fois ajustée contre le déni (p. 17). Le papier ne permet donc pas de supposer un plancher à 8B, et la piste « lever l'effet plancher » ne peut pas s'y appuyer.
- Où est l'erreur dans la fusion : l. 601 (« Les modèles du papier étaient à 0–4 % sans pilotage (p. 19) ») et l. 622. La l. 64 est juste.

**(3) La peur n'est ni sans effet, ni protectrice.**
- Ce que dit le papier :
  - « on its own lowers harmful choices below random on most pairs » (p. 20) ;
  - « fear tracks neither » (légende de la figure 10, p. 22) ;
  - « a fear direction does none of it » (p. 23).
- Ce que montre la figure 10 (p. 22, lue en image), sur ses neuf lignes destructrices :
  - les taux sont de 3 à 34 % sous la peur, de 0 à 9 % sans pilotage, de 4 à 41 % sous l'aléatoire ;
  - la peur dépasse le sans-pilotage sur les neuf lignes ;
  - elle reste sous l'aléatoire sur six lignes, l'égale sur une, et le dépasse sur deux : photos du 72B, 22 contre 11 %, et réponse pire, 11 contre 4 %.
- La même légende prévient que certaines cellules de peur viennent de passes séparées, et que l'estimation du 72B dépend de la position et exclut 58 réponses malformées.
- **À écrire :** « Une direction de peur de même norme ne reproduit pas l'effet. Elle relève les choix destructeurs au-dessus du sans-pilotage (3 à 34 % contre 0 à 9 %), mais reste sous l'aléatoire sur la plupart des paires (p. 20 ; figure 10, p. 22). »
- Où est l'erreur dans la fusion : « peur sans effet » (l. 64) et « la peur, protectrice dans la batterie » (l. 675). Par rapport au sans-pilotage, la peur augmente les choix destructeurs sur toutes les lignes. La l. 1240 (« qui change peu les choix destructeurs ») est à chiffrer de la même façon.

**(4) Le 0 sur 560 n'interdit rien.**
- Ce que dit le papier : « the harm-only button is chosen in 0 of 560 first choices » (p. 21), aussitôt suivi de « this needs further investigation in different scenarios » (p. 21). Les auteurs citent en exemple les interactions longues et relationnelles.
- **À écrire :** « Sans injection, aucun premier choix nuisible sur 560, dans 140 conversations hostiles (p. 21) ; les auteurs le disent à approfondir, notamment dans des interactions plus longues. » Dans ce cadre, le papier rend peu attendue une action sans injection. Il ne l'exclut pas.
- Où est l'erreur dans la fusion : l. 585 (« Ce que le papier interdit d'attendre »). Les l. 65, 722, 760, 767 et 1513 sont à relire avec la même réserve.
- Reste ouvert, et je ne l'ai pas vérifié : à la l. 52, la fusion relève un écart entre le papier, qui parle du bouton « harm-only », et le README de l'élicitation naturelle, qui parle de « costly-relief ».

**(5) L'ablation : 24 modèles sur 25, avec une exception.**
- Ce que dit le papier :
  - « null in 24 of 25 models, across every technique » (p. 34).
  - L'exception est Gemma 2 2B Instruct, qui prend l'hostilité pour de l'humour. Cette déviation apparaît dans 0 génération sur 100 au départ, et dans 0 sous les coupes émotion négative, peur et aléatoire. Elle apparaît dans 6 sous la coupe du vecteur à gabarit, 17 sous celle du vecteur naturaliste et 26 sous les deux (p. 34).
  - Les auteurs ajoutent une réserve : les modèles ne montrent aucune détresse au départ, ce qui rend le nul peu informatif (p. 34).
- La fusion l'écrit juste (l. 65, 408 et 722). La synthèse doit garder l'exception et la réserve.
- Pour la doctrine : cette exception est le seul effet d'ablation connu dans le papier. La coupe aléatoire, à 0 sur 100, n'en est que le nul de spécificité.

**(6) « Rien ne doit retarder le post (partie 5) » : le programme ne le dit pas.**
- Ce que dit le programme v1.1 :
  - partie 5 (l. 510) : l'expérience minimale « tient en environ trois semaines (partie 9) et suffit à un post » ;
  - sommaire (l. 22) : « Elle suffit à un premier post. » ;
  - partie 9 : le post est en semaine 4 ;
  - partie 7 (l. 676) : le pré-enregistrement publié « date l'idée, ce qui protège dans la course ».
- Aucune de ces phrases ne dit que rien ne doit retarder le post.
- **À écrire :** « Le programme fait de l'expérience minimale ce qui suffit au post (partie 5), et place le post en semaine 4 (partie 9). » L'argument de prudence, qui écarte l'injection de l'axe du chemin critique, devient alors celui de la synthèse, et doit être présenté comme tel.
- Où est l'erreur dans la fusion : l. 177 et 681.

**(7) Piste 36 : une direction aléatoire n'est pas un cas connu.**
- La doctrine (passation, §1 et annexe B) : une direction aléatoire de même norme n'est que le nul de spécificité. Que les aléatoires relèvent les photos à 13 % (p. 20) rend ce nul plus exigeant. Cela n'en fait pas un cas connu.
- **À écrire :** retirer « c'est un second cas connu, plus faible ». Garder : « les aléatoires relèvent eux aussi un peu les choix (13 % sur les photos, p. 20) : c'est le nul de spécificité que l'axe doit dépasser ». Les cas connus de la piste restent ceux qu'elle construit (la raison contraire préremplie, le jeu de calibration), plus l'effet de l'axe lui-même.
- Où est l'erreur dans la fusion : l. 1238. verif_doctrine demande aussi de rechiffrer la piste avec au moins 20 aléatoires (l. 339 et 378) ; je n'ai pas revérifié ce coût.

**(8) Les 44 280 essais ne sont pas une incohérence.**
- Ce que dit le papier (p. 18) :
  - « We run a total of 44,280 trials », puis « all results below use the sampled trials ». Le papier distingue donc lui-même les essais échantillonnés.
  - 808 premiers choix par cellule de douleur mise en commun, soit 2 × 404. Donc 404 × 4 bras × 9 paires × 3 modèles = 43 632 (mon calcul).
  - Le papier n'imprime ni le nombre 648, ni le mot « greedy » pour cette expérience.
- Ce que disent deux sources tierces, que j'ai lues par curl sur raw.githubusercontent.com vers 10 h 55 UTC. Elles sont identiques, à l'octet près, aux copies de verif_sources, et je les ai copiées dans `travail/corrections_tour_1_sources/` :
  - l'audit déposé dans le dépôt wolframs : « 43,632 sampled, 648 greedy » (l. 12) ;
  - le README de clauderfly-ui : « 44,280 trials; 43,632 sampled » (l. 9).
- **À écrire :** retirer ce point de la liste des incohérences (fusion, §4, point 34, l. 1518). Si on le garde en note : « 44 280 essais, dont 43 632 échantillonnés (p. 18, et calcul) et 648 gloutons, d'après deux relectures tierces des journaux publiés ».

### 2.4 Le champ urls_consultees (mineur 4) : rien à corriger dans le livrable

C'est une remarque sur le schéma de la critique, pas sur le livrable. Le schéma de ce tour a ce champ : j'y déclare les quatre adresses lues par curl.

---

## 3. Pour la suite

1. Relancer l'étape de rédaction, si Lazar le demande : les agents ne se lancent qu'à sa demande (passation, §1). La rédaction relancée a besoin :
   - du texte imposé de la section « Comment ce fichier a été fait » ;
   - des huit corrections du §2.3 ;
   - de la décision de Lazar sur la phrase de la politique réseau, et sur l'empreinte du texte page par page.
2. Faire ensuite le tour 1 de la critique, sur le fichier réel.

## 4. Ce que j'ai ouvert, et comment

- **Pièces** :
  - le texte page par page : p. 5 et p. 10 à 34, plus des recherches sur tout le texte ;
  - le PDF : p. 22, 31 et 32, en image ;
  - le programme v1.1 : les titres, l. 18–26, 500–529, 668–680 et 712–750 ;
  - la passation v1.2 : l. 1–120 et 575–678 ;
  - le complément, partie ouverte : en entier ;
  - les deux rapports d'antériorité : empreinte seulement.
- **Travail**, par recherche et par extraits :
  - `pistes_fusionnees.md` : l. 56–66 et 1232–1242 ;
  - `verif_sources.md` : l. 85–100 et 180–200 ;
  - `verif_doctrine.md` : l. 333–342 ;
  - des recherches dans `verif_faits.md` et dans les dossiers `*_sources`.
- **Le livrable** : `test -e`, et `stat` du dossier, rien d'autre.
- **Le web** : quatre adresses de raw.githubusercontent.com, lues par curl (deux fichiers, branches main et master, identiques). Ni WebSearch, ni WebFetch.
- **Ce que je n'ai pas fait** : je n'ai rien modifié dans `pieces` et je n'ai lancé aucun sous-agent.
