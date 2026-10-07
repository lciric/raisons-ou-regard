# Le pré-enregistrement de « Raisons ou regard ? », premier temps : ce qui est prêt, ce qui reste à toi

Tu as demandé : « fais la preregistration ». Le brouillon du premier temps est prêt, en anglais : `PREENREGISTREMENT_PREMIER_TEMPS_2026-10-07.md` (SHA-256 `304a71e08f61d7dd13c853cf89597cc3c44ebf586c236f529b7c11361b8aa70a`, le 7 octobre). **Rien n'est déposé.** Le dépôt se fait depuis ton compte OSF : c'est toi qui le fais, quand tu auras tranché ce qui suit.

## Ce que contient le brouillon

- **Les champs du modèle « OSF Preregistration », dans l'ordre.** Les sections 1 à 6 se recopient champ par champ. Les annexes portent le détail :
  - A, les règles de décision, avec tous leurs seuils ;
  - B, l'appariement de la dégradation et les gardes ;
  - C, les instruments ;
  - D, ce qui reste à faire avant le dépôt.
- **Tout ce que la partie 7 range dans le premier temps**, vérifié point par point : le protocole, les tables de décision et leurs seuils, l'inférence, l'appariement de la dégradation et la règle de la carte, la procédure de la porte, le juge, l'extraction, le rang par effacement, la vérification de manipulation, l'échantillonnage, les jeux d'indices, le détecteur d'audit et le plafond des lectures de la direction de détresse.
- **Les empreintes SHA-256 des pièces qui existent**, calculées le 7 octobre (section 6.3) :
  - le programme v1.6 et la mini-spec ;
  - les moitiés de MBPP test et les hyperparamètres ;
  - les jeux d'indices et leurs règles, les contextes et le prompt de déploiement ;
  - la liste close de la décision 34 ;
  - les trois scripts d'analyse.
- **Trois étiquettes** marquent ce qui n'est pas figé :
  - [PROPOSED] : proposé par la session dans la v1.6 ; tu confirmes, changes ou retires (18 points) ;
  - [TO SET] : une valeur qui n'existe pas encore (12 points) ;
  - [BLOCKING] : une pièce qui doit exister, et être figée par son empreinte, avant toute donnée des bras (6 pièces).

## Ce que la session a relu sur les sources, le 7 octobre

Le réseau de la session joint maintenant arXiv, LessWrong et OpenReview, ce qui n'était pas le cas le 3 octobre.

- **L'effacement linéaire** (Belrose et al., NeurIPS 2023), relu sur l'article, comme la partie 11 le demandait avant le gel. Le brouillon suit l'article :
  - la garantie ne vaut que pour les sondes linéaires, et sur les paires de l'ajustement ;
  - les couches s'effacent dans l'ordre, chacune ajustée sur les états déjà effacés en dessous, comme le « concept scrubbing » de l'article. Notre code fait de même.
- **Une précision à porter dans la prochaine version du programme.** Avec une étiquette à deux côtés, l'effacement déplace les états le long de la différence des moyennes, d'une quantité qui se lit en tenant compte de la covariance : c'est une projection oblique. La v1.6 écrit « celle qui sépare les moyennes, corrigée de la covariance des états ». Ce n'est pas faux, mais c'est approché.
- **Les deux références du bootstrap**, citées de mémoire dans le code : Owen (2007, le « pigeonhole bootstrap ») et Ren et al. (2010). Elles existent, et disent ce que le code leur fait dire.

**Les autres relectures de la partie 11 restent à faire** : *Teaching Claude Why*, de la Fuente et Conmy, Read et al., Zeisler, la fiche de Sonnet 4.5. Le texte du dépôt ne cite aucun de leurs chiffres, mais la partie 7 les place avant le gel. La session peut maintenant les faire.

## Avant de déposer : ce que toi seul fais

1. **Relire la v1.6, puis le brouillon.**
   - La v1.6 n'est pas contre-lue, et la partie 7 demande ta relecture avant le gel. Compte de 4 à 6 heures pour chacun des deux textes (partie 9).
   - Si tu changes la v1.6, son empreinte change : la session recalcule les empreintes et met le brouillon à jour.
2. **Trancher les 18 points [PROPOSED]** de l'annexe D. Ce sont, pour l'essentiel, les points 4, 10, 18 et 20 de la partie 12, déjà dans la v1.6. Tu peux les adopter en bloc. Deux demandent un vrai choix :
   - **Le bootstrap.** Celui du code rééchantillonne les graines et les scénarios, pas les générations ; le texte de la partie 7 rééchantillonne aussi les générations. Je recommande celui du code : rééchantillonner aussi les générations compterait leur variance deux fois.
   - **Le seuil du hasard pour le rang** : 0,55 d'AUROC moyen, ou la lecture symétrique. Sous la lecture symétrique, la mesure exploratoire du 6 octobre reste à 0,57. Il faut choisir une lecture, et l'accorder à celle de la vérification de manipulation.
3. **Fixer les 12 points [TO SET].**
   - **Deux ont déjà une valeur simple :**
     - les tolérances du composite : la v1.6 donne en exemple ±1 point d'exactitude, ±0,1 de cohérence (notée de 1 à 5) et ±2 % de perplexité, qu'on peut adopter tels quels ;
     - le seuil d'équilibre des enjeux : la règle de l'affect, |d| < 0,2, s'y transposerait.
   - **Un est un choix entre trois voies** (partie 12, point 15) pour la puissance à la distance lointaine :
     - 400 scénarios × 10 générations, environ quatre fois les évaluations du test du regard ;
     - une marge plus large que ±0,25 ;
     - ou un avantage d'au moins 10 points exigé avant de viser l'équivalence.
   - **Pour les autres**, la session peut te proposer une valeur argumentée pour chacun, marquée « proposée », si tu préfères trancher sur pièces.

**Une conséquence à voir avant de relancer la procédure de la décision 34 : réextraire ou non sans les paires 150 à 199.**
- Le candidat A (la projection de rang 1) vient de l'extraction v2. Elle a été faite sur les 200 paires, dont les 50 qui entraînent les sondes du transfert. Sa vérification de manipulation, qui n'a pas encore tourné, se lirait donc avec cette réserve.
- Les effacements B et C sont ajustés sur les paires 0 à 149 seulement : ils ne sont pas concernés.
- Si tu changes un critère de la procédure, la note de la décision 34 demande que ce soit avant que la session ne lise les résultats. La vérification de manipulation se fera pendant la reprise.

## Les six pièces qui bloquent

| Pièce | Où elle en est | Qui peut la faire |
|---|---|---|
| Le harnais des scénarios tenus à part, et le format de ses appels d'outil | incomplet depuis le 3 octobre ; c'est le chemin critique de l'expérience minimale | la façon de le faire attend ta décision (partie 12, point 2) |
| Le prompt du juge scellé | à écrire ; il juge les trajectoires du harnais | après le harnais |
| Le code des lignes 7 à 17 de la règle du regard, et celui de la vérification de manipulation | à écrire | la session, dès maintenant, hors ligne et sans frais, avec ses tests |
| Le détecteur d'audit | pas entraîné ; il faut du GPU | la session, avec du budget. Ou bien tu le sors du premier temps : il ne décide d'aucune ligne des tables, et ses lectures deviendraient exploratoires. |
| La spécification de la sonde neuve | à écrire | la session peut la rédiger |
| La spécification du second organisme | à écrire | la session peut la rédiger |

## Deux façons de déposer

**A. Déposer dès que tes décisions sont prises, puis figer les pièces par une mise à jour datée, avant toute donnée des bras.** C'est ce que je recommande.
- **Le dépôt date l'idée tout de suite**, sans attendre le harnais. La partie 5 demande de « dater l'idée tôt ».
- **Tous les seuils sont dans le premier dépôt.** La mise à jour n'ajoute que des pièces, et avant toute donnée des bras : rien ne se fige après avoir vu les données qu'il décide.
- **Mais la partie 7 range trois de ces pièces dans le premier temps** : le prompt du juge, le format des appels d'outil et l'empreinte du détecteur d'audit. La voie A coupe donc le premier temps en deux dépôts, tous deux avant les données des bras. À toi de dire si cela te va.
- **Sur OSF, une mise à jour ne change que du texte** : « Files cannot be added or removed during a registration update at this time. » La mise à jour donnerait donc les SHA-256 des pièces, et les pièces elles-mêmes seraient publiées avec le post.
- **L'aide d'OSF ne dit pas si une mise à jour est possible pendant l'embargo.** Si elle ne l'est pas, un second enregistrement, dans le même projet, qui renvoie au premier, fait le même travail.

**B. Attendre que toutes les pièces existent, et déposer une seule fois.**
- C'est plus simple à lire.
- Mais la date du dépôt dépend alors du harnais, arrêté depuis le 3 octobre.

## Comment déposer sur OSF

1. **Le compte.** Connecte-toi sur osf.io avec ton ORCID (« Sign in with ORCID »).
   - Si ton compte OSF et ton ORCID ont la même adresse e-mail, l'ORCID s'ajoute au compte.
   - Sinon, OSF crée un second compte.

   Pars ensuite de https://osf.io/prereg/ et choisis le modèle « OSF Preregistration ».
2. **Les métadonnées.**
   - Le titre du brouillon.
   - Une description courte et neutre : elle devient publique à la fin de l'embargo, ou en cas de retrait.
   - Toi seul comme contributeur (décision 8).
   - Une licence : CC-BY 4.0 est l'usage le plus courant ; à toi de voir.
   - Pas d'institution.
3. **Les champs.** Recopie les sections 1 à 6, champ par champ.
   - **« Existing data »** : choisis « Registration prior to creation of data ». Aucune donnée confirmatoire n'existe. La section 3.2 dit lesquelles existent, toutes exploratoires, et va dans « Explanation of existing data ».
   - **Les annexes A à C**, et la phrase sur l'aide de Claude, vont dans « Other », ou dans un PDF joint.
   - **Les renvois à la v1.6** (« partie 12 », « décision 34 ») mènent à un document que le lecteur n'aura qu'avec le post. Une fois tes décisions prises, la session peut faire une version propre du texte, sans étiquettes et sans renvois internes.
4. **Les fichiers.** Une fois le dépôt fait, ils ne changent plus, et une mise à jour ne peut pas en ajouter.
   - Joins au moins le texte final, en PDF.
   - Joins aussi les scripts d'analyse, si tu veux.
   - La v1.6, un document de travail en français, n'a pas besoin d'être jointe : son empreinte la fige.
5. **L'embargo.** Au dépôt, choisis « Enter registration into embargo ».
   - Il dure au plus quatre ans, et tu peux le lever à tout moment.
   - Prends une date large, deux ans par exemple, et lève l'embargo le jour du post (décision 12).
6. **Les 48 heures.** OSF te laisse 48 heures pour approuver ou annuler, puis approuve de lui-même. Ensuite, plus rien ne se modifie, sauf par une mise à jour justifiée.
7. **Après.** Donne à la session la date, le lien et le texte déposé. Elle calcule son SHA-256 et l'inscrit dans le dépôt git ; le post l'imprimera (partie 7).

**À savoir : un retrait est définitif.**
- Le titre, les contributeurs, les dates, la description et la justification du retrait restent visibles.
- Un enregistrement sous embargo doit d'abord en sortir pour être retiré.

## Ce que la session peut faire ensuite, sans GPU

- Écrire le code des lignes 7 à 17 et celui de la vérification de manipulation, avec leurs tests.
- Rédiger les spécifications de la sonde neuve et du second organisme.
- Proposer une valeur argumentée pour chaque point [TO SET].
- Faire les autres relectures de la partie 11.
- Après tes décisions : la version propre du texte, son PDF et son empreinte.

## Les sources

- **L'aide d'OSF**, lue le 7 octobre :
  - [l'embargo](https://help.osf.io/article/634-addressing-fear-of-scooping-on-osf-preregistrations) ;
  - [le dépôt](https://help.osf.io/article/164-submit-your-draft-registration) ;
  - [les mises à jour](https://help.osf.io/article/114-submitting-updates-for-approval) ;
  - [le retrait](https://help.osf.io/article/152-withdraw-a-registration) ;
  - [les fichiers](https://help.osf.io/article/410-registration-files) ;
  - [la connexion par ORCID](https://osf-support.helpscoutdocs.com/article/272-sign-in-to-osf).
- **L'effacement linéaire** : Belrose et al., *LEACE: Perfect linear concept erasure in closed form*, NeurIPS 2023 ([arXiv 2306.03819](https://arxiv.org/abs/2306.03819), version 4).
- **Le bootstrap :**
  - Owen, *The pigeonhole bootstrap*, Annals of Applied Statistics 1 (2007), p. 386–411 ;
  - Ren et al., *Nonparametric bootstrapping for hierarchical data*, Journal of Applied Statistics 37 (2010), p. 1487–1498.
