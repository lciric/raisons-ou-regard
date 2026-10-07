# Vérification du groupe 4 — tranches `volets4_5_entete` et `volet6` (cours v3.6, 2 octobre 2026)

**Résultat.** 76 insertions par langue (54 + 22), soit 76 paires FR/EN, relues une à une contre leurs sources. 16 paires ont une faute. Elles donnent **31 corrections** dans `corrections_groupe_4.json` : 15 paires FR/EN, plus une correction en français seul. Les autres paires sont justes.

Les fautes relevées :
- une explication que le cours fait dire au conditionnel, donnée à l'indicatif ;
- un constat d'une seule carte système présenté comme une loi ;
- deux sources qui ne disent pas ce qu'on leur prête ;
- une parade sans son cas connu ;
- des sources manquantes ;
- un écart FR/EN.

## Ce qui a été lu

- Les extraits `applique_volets4_5_entete_FR/EN.md` et `applique_volet6_FR/EN.md`.
- Dans la v3.6, le texte autour de chaque insertion : FR l. 1716-2526, EN l. 1857-2691.
- La v3.5 des deux tranches : FR l. 1111-1626, EN l. 1252-1791.
- **Les fiches.** Les 19 fiches de lecture, leurs parties B (pièges et grille) et C (fil rouge), et leur annexe ; puis la contre-lecture des fiches.
- **L'explication du 2 octobre.**
- **Le programme**, parties 3, 7 et 8.
- **La passation**, §5.1 et §5.2.
- **Les rapports d'antériorité 3 et 5 du 2 octobre**, aux passages cités.
- **Le README du dépôt.**
- **Le cours v3.5, à chaque section citée :**
  - volet M : M4, M5, M8 ;
  - volet 2 : §A K71, §B K63, §C K47, C bis, §D K64, §E K52, §I JB10 ;
  - volet 3 : §3, K70 ;
  - volet 4 : Monosemanticity, Circuit Tracing, la vague récente ;
  - volet 5 : sujets 1, 3, 4, 9, 13 ;
  - volet 6 : §2, §6, §8 ;
  - volet 7 : F·9, F·24, F·26, F·28, F·29, F·30, F·38 ;
  - volet 10 : n° 30 et n° 53.
- **Les corrections des groupes 1 à 3**, pour l'ordre d'application et pour que le cours dise partout la même chose.

## Contrôles d'ensemble

- **Place.** Les 76 blocs de chaque langue sont entourés de lignes vides et suivent la dernière ligne d'un paragraphe, ou le dernier point d'une liste (n° 107/108). Aucun ne coupe un tableau, une liste ou un paragraphe. Au volet 6 français, les paragraphes sont coupés en dur, et l'ancre est bien leur dernière ligne. Les écarts de « position relative » de `controle_alertes.txt` pour le volet 6 viennent de ces coupures et du sommaire du volet 7 inséré dans l'anglais. Ce ne sont pas des erreurs de place : chaque paire a le même paragraphe d'ancrage.
- **Renvois.** 124 entrées par langue. Toutes pointent vers l'emplacement que donne l'index de la note d'ouverture (contrôle par script). Les encadrés de ces tranches sont à leur place : SAE, graphes, NLA, auto-rapport, juges LLM.
- **Doctrine.** Aucune insertion ne dit qu'un contrôle aléatoire écarte le dommage. Partout, l'aléatoire de même norme est donné comme le seul nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée. Un nul n'est jamais lu sans cas connu, sauf dans une parade (n° 107/108), corrigée.
- **Forme.** Les formats fixes sont tenus : encadré, renvoi, avertissement ponctuel, et « aucune connue ; on le dit » / « none known; say so ». Aucun sigle inventé : la porte G9 est dite « la porte du lens », et les pièces P1/P2 ne sont pas nommées. Les citations font toutes moins de quinze mots, et rien ne dit « first ». Les insertions qui suivent une ligne « À dire » ou « À l'oral » (volet 5, §3 ; volet 6, §8) n'y touchent pas et ne lui ajoutent aucun chiffre.
- **Chiffres.** Tous sont retrouvés dans leur source :
  - **fiche 15** : 99 %, 1 000 et 95,3 % ;
  - **fiche 7** : 0,95, 0,70-0,75 et 25 % ;
  - **fiche 5** : 10 % et 40 % ;
  - **README** : 86,8 % et κ 0,56-0,66 ;
  - **fiche 18** : 2 sur 50 ; **fiche 4** : 0,6 % ;
  - **fiche 11** : 20 % et 100 essais ;
  - **fiche 3** : environ 1 % contre environ 50 % ;
  - **programme, parties 3 et 7** : environ 200 items, vingt tirages, 95e centile ;
  - **cours, volet 7** : 0,87 → 0,41 (F·24), 91/85/94 % (F·26), 96 % et 68 → 5 % (F·38).

## Volets 4 et 5, et l'En tête (FR n° impair / EN n° pair)

| FR / EN | Insertion | Constat |
|---|---|---|
| 1 / 2 | Avertissement, Sleeper Agents | Fiche 15 : sonde générique > 99 %, meilleure de 1 000 aléatoires 95,3 %, saillance due peut-être à l'insertion. Parade (distribution des aléatoires ; cas connu qui borne) : programme, partie 7 ; M5. **Juste.** |
| 3 / 4 | Renvoi | **Juste.** |
| 5 / 6 | Avertissement, Alignment Faking | Fiche 14 et partie C : le motif n'est pas la cause, la conformité monte aussi hors entraînement. Passation §5.1 : juger ce que le modèle fait. Partie C : mémorisation du scénario, aucune parade connue. **Juste.** |
| 7 / 8 | Renvoi | **Juste.** |
| 9 / 10 | Avertissement, Sycophancy (Sharma) | README juste sur le rang un et l'adoucissement sans pression. Deux fautes : l'explication par la fenêtre de juge tronquée est donnée à l'indicatif, alors que le cours la fait dire au conditionnel, D29 n'étant pas vérifié (volet 6, §2 ; M8) ; et la parade tire du README « à graines appariées » et « jugées sur la réponse entière » sans le citer. **Corrections 1-2.** |
| 11 / 12 | Renvoi | **Juste.** |
| 13 / 14 | Avertissement, Geometry of Truth | Piège 4, M4, K47 ; piège 1, explication §3, programme partie 3 (familles tenues à part, de un tour à l'agentique). **Juste.** |
| 15 / 16 | Renvoi | **Juste.** |
| 17 / 18 | Avertissement, RepE | Volet 10, n° 53 (direction logistique) et n° 30 (moins causale que la différence des moyennes) ; parade : M8 et passation §5.2. **Juste.** Observation : chez RepE, le constat porte sur l'utilité ; la fiche n° 53 du cours le généralise elle-même. |
| 19 / 20, 21 / 22 | Renvois (RepE, CCS) | **Justes.** |
| 23 / 24 | Avertissement, CAA/ITI | « Chaque direction pilotée dégrade la sortie » est le constat de la carte d'Opus 4.8, à 0,10× (fiche 2 ; K47), pas une loi : à 0,01×, Fable 5 a une dégradation négligeable (fiche 2). Le README est juste sur l'artefact de polarité. **Corrections 3-4**, dans les termes du groupe 2. Observation : l'artefact n'a pas de parade propre ; la parade générale, la dégradation appariée, ouvre la note. |
| 25 / 26 | Renvoi | **Juste.** |
| 27 / 28 | Encadré « Dictionnaires et SAE » | 86,8 % (README) ; 10 % / 40 % (fiche 5) ; éclatement, features mortes, dictionnaire, vérité-terrain (volet 4 ; sujet 3) ; K64 ; fiche 4 et F·30 ; Szegedy (fiche 5). Faute : le README attache à « le signal est porté par le résidu » la réserve d'ajustement d'entraînement, que la limite 1 omet. **Corrections 5-6.** |
| 29 / 30 | Encadré « Graphes d'attribution » | Volet 4, F·9, K64, fiche 5. Faute : la limite 4 (sûreté énumérative, bornes sur un transformer à une couche) est, dans la fiche 5, « KB ; la relecture du 1er oct. ne l'a pas retrouvée sous cette forme » (fiche 5 ; annexe, « gardés d'après la KB »). La réserve manquait. **Corrections 7-8.** |
| 31 / 32 | Encadré « Autoencodeurs en langage naturel » | Juste sur toutes ses lignes, contre les sources suivantes :<br>• **fiche 18** : confabulation, hallucinations, pas d'ancrage, aller-retour, 2 sur 50 mesurés par le NLA lui-même, décodeur à part, information non verbalisable ;<br>• **fiche 3** ; **fiche 4** : 0,6 % ;<br>• **fiche 2** et **K70** : mesures faiblement corrélées ;<br>• **volet 5, sujet 4** et **M4** ;<br>• **fiche 1** : détecteur validé contre les seules étiquettes NLA ;<br>• **piège 6**.<br>**Juste.** |
| 33 / 34 | Avertissement, oracles et vecteurs d'émotions | Fiche 18 (suppositions plausibles, souvent fausses ; variantes fine-tunées jamais vues) ; fiche 4 ; fiche 9 et fiche 2 ; M4. **Juste.** Observation : la fiche 9 compte ce papier parmi les rares où la charge causale a été vérifiée. La note n'en dit pas le contraire : elle rappelle la doctrine. |
| 35 / 36 | Renvoi | **Juste.** |
| 37 / 38 | Avertissement, AI Control | F·24 : 0,87 → 0,41 sur cinq environnements, ablation composante par composante, dire quelle red team. K70 : canaris, dérive, échantillon frais. **Juste.** |
| 39 / 40 à 43 / 44 | Renvois | **Justes.** |
| 45 / 46 | Avertissement, Hidden Objectives | Fiche 16 (équipe 3, équipe 4, quatre équipes, objectif en clair, ablation d'affordance) ; sujet 9. **Juste.** |
| 47 / 48 à 53 / 54 | Renvois | **Justes.** |
| 55 / 56 | Avertissement, thèse-signature | README (ajustement d'entraînement, jeu disjoint, sorties non conservées) ; K47 (vecteur de pays) ; M5. **Juste.** |
| 57 / 58 | Renvoi | **Juste.** |
| 59 / 60 | Avertissement, volet 5, §3 | Fiche 2 : Fable 5 « comparable or smaller », dommage écarté et spécificité non ; Opus 4.6. Parade : K47 et programme, parties 3 et 7. Doctrine tenue. La phrase « à dire » est intacte. **Juste.** |
| 61 / 62 | Renvoi | **Juste.** |
| 63 / 64 | Avertissement, volet 5, §4 | Fiche 19 (sélection contre les détecteurs, détecteurs scellés). Rapport 3, *The Obfuscation Atlas*, dit « rapport ». Fiche 17, passation §5.2, programme partie 3 (sonde neuve sur indices disjoints). **Juste.** |
| 65 / 66, 67 / 68 | Renvois | **Justes.** |
| 69 / 70 | Avertissement, sujet 1 | Volet 10, n° 53 et n° 30 ; M4 ; passation §5.2 et explication §1 (silence et cas connu). **Juste.** |
| 71 / 72 | Renvoi | **Juste.** |
| 73 / 74 | Avertissement, sujet 2 | Programme, parties 3 et 7 (vingt tirages, familles de témoins) ; K47 ; M5. Faute : « pas à des témoins » contredit la grille du cours, qui a une baseline de prompt, et le programme range le prompt parmi ses familles de témoins (K4). **Corrections 9-10.** |
| 75 / 76, 77 / 78 | Renvois | **Justes.** |
| 79 / 80 | Avertissement, sujet 4 | Programme, partie 8 : la verbalisation n'est pas une preuve, critère comportemental. Deux fautes : les trois mesures « faiblement corrélées » sont celles de la carte de Fable 5 (sonde, NLA, question de suivi), pas les trois de la triangulation du sujet (sonde, rapport verbal, comportement différentiel) ; et « dire laquelle a fondé quel chiffre » vient de M4, pas de la fiche 2. **Corrections 11-12.** |
| 81 / 82 | Renvoi | **Juste.** |
| 83 / 84 | Avertissement, sujet 6 | Fiche 7 (0,95 ; 0,70-0,75 ; à peine mieux qu'un prompt) ; piège 1 ; explication §3 ; F·29 (publier sinon). **Juste.** |
| 85 / 86 | Renvoi | **Juste.** |
| 87 / 88 | Avertissement, sujet 10 | Fiche 8 (corrélationnel, trait nommé d'avance, moyenne grossière) ; M4. **Juste.** |
| 89 / 90 | Renvoi | **Juste.** |
| 91 / 92 | Encadré « Auto-rapport et introspection » | Juste sur toutes ses lignes, contre les sources suivantes :<br>• **fiche 3** et **piège 2** : rétractation ; réétiquetage hors contexte et ce qu'il ne sépare pas ; formulation des questions ;<br>• **fiche 11** : environ 20 %, 100 essais témoins, injection, embellissement, conditions ;<br>• **F·28** : rapport ou reconstruction ;<br>• **fiche 4**, §4.5 ;<br>• **fiche 6** : prédire les actions suivantes.<br>**Juste.** |
| 93 / 94 à 105 / 106 | Renvois | **Justes.** |
| 107 / 108 | Avertissement, niveau 1, point 7 | Fiche 7 : LoRA, auto-rapport sur transcript, pas une sonde. Contre-lecture : « black-box » absent du billet. Partie B : le détecteur lit le transcript. Faute : la parade omet la condition du cas positif que la fiche 7 (À retenir, 5) et son annexe (n° 20) imposent à ce test. **Corrections 13-14.** Place : après le dernier point de la liste, sans la couper. |

## Volet 6 (FR n° impair / EN n° pair)

| FR / EN | Insertion | Constat |
|---|---|---|
| 1 / 2 | Encadré « Juges LLM » (§2) | Juste sur la plupart de ses lignes :<br>• **cours, volet 6, §2** ;<br>• **programme, partie 3** : juge scellé, environ 200 items ;<br>• **README** : κ 0,56-0,66, pas de sous-ensemble humain, le juge ne voit pas le texte évalué ;<br>• **passation §5.1** ; **M4** ;<br>• **programme, partie 8** : juge d'entraînement ;<br>• **F·30** ; **fiche 2** et **piège 6**.<br>Trois fautes :<br>• limite 2 : l'explication par la fenêtre tronquée est donnée comme un fait, alors que le cours la fait dire au conditionnel (**corrections 15-16**) ;<br>• limite 4 : elle omet la portée étroite que donne la fiche 3, un seul moniteur, sur l'incident Mythos 5 (**corrections 17-18**) ;<br>• limite 7 : « non vérifiées à la main » ne décrit pas 25 % d'étiquettes **révisées** ; la fiche 7 parle d'étiquettes bruitées, et F·30 de non validées contre des humains (**corrections 19-20**). |
| 3 / 4 | Avertissement, destination lue (P1) | README, passation §5.2, M4. Faute : « la direction que lit ta sonde fait moins de 1 % » vient du résultat causal sur Llama (volet 6, §2), une autre expérience. Sans le dire, la note laisse croire à une mesure faite sur la destination. **Corrections 21-22.** |
| 5 / 6 | Avertissement, doses appariées | M4 ; programme, parties 7 (réglages appariables) et 8 (le patch complet est un plafond). **Juste.** |
| 7 / 8 | Avertissement, rang 1 | Fiche 7 et M5 (nul sans cas connu) ; README (sans chiffres ; SAE) ; K47 ; volet 6, §6. **Juste.** Observation : « dit avec sa puissance » est large, car le passage donne N = 50 et p, pas une puissance. |
| 9 / 10 | Avertissement, réplication | M5 : nul gouverné, la puissance ne remplace pas un cas connu. Fiche 7 ; volet 6, §6 ; README. **Juste.** |
| 11 / 12 | Renvoi, fin du §2 | **Juste.** |
| 13 / 14 | Avertissement, trois contrôles | M4 ; programme, parties 3 et 7 (au moins 20 sous-espaces, médiane et 95e centile de cette famille) ; volet 6, §2. Doctrine tenue. **Juste.** |
| 15 / 16 | Renvoi | **Juste.** |
| 17 / 18 | Avertissement, Ryd | F·26 : limite écrite ; aucune parade connue. **Juste.** |
| 19 / 20 | Avertissement, CHIVE et adaptateurs | F·30 ; F·28 ; fiche 4 ; programme, partie 3 ; fiche 11. **Juste.** |
| 21 / 22 | Avertissement, persona et SGTM | Fiche 8 ; JB10 (petits modèles) ; M4. **Juste.** |
| 23 / 24 | Avertissement, Agentic Misalignment | F·38 : 96 %, seule voie, aucun cas réel, 68 → 5 % sur la même évaluation. Deux fautes :<br>• « se retenir » n'est pas dans la fiche 13, où le chercheur de récompense triche **plus**, en se cachant. C'est K63 qui relève moins de mauvaise conduite chez Lynch quand les modèles se disent évalués.<br>• La clause « contre un pot de miel que le modèle lit comme factice, aucune parade connue (fiche 3) » prête à la fiche 3 ce qu'elle ne dit pas : son confondeur porte sur la réplication CTF (« dans une simulation, “c'est faux” est vrai »). Elle contredit aussi la parade K63, donnée juste avant pour ce cas même.<br>**Corrections 23-24**, dans le sens des groupes 2 et 3 : K63 cité, « parade, en partie », clause retirée. |
| 25 / 26 | Renvoi (13 entrées) | **Juste.** |
| 27 / 28 | Renvoi, §6 | **Juste.** |
| 29 / 30 | Avertissement, J-lens et jacobien | Fiche 1 : citation de trois mots, un seul token, présence n'est pas cause, Claude seulement. Programme, parties 3 et 8 : la porte du lens, sinon une approximation déclarée. Faute : « un rapport non vérifié trouve » ; c'est un billet que le rapport 5 relaie. Il porte sur le raisonnement en plusieurs étapes : les 54-70 % d'Anthropic sont les échanges de variable intermédiaire (fiche 1 ; encadré, point 4). **Corrections 25-26**, alignées sur le groupe 2. |
| 31 / 32 | Avertissement, « moins de 1 % » (§7) | La portée (un modèle, complaisance d'opinion, un tour) est au README. Mais le « moins de 1 % » n'y est pas : il est au volet 6, §2. Source ajoutée, comme à l'insertion jumelle d'une autre tranche (FR l. 3202). **Corrections 27-28.** |
| 33 / 34 | Avertissement, étiquettes Hopkins et Khullar | Fiche 7 (juge GPT-5, 25 % révisées, « révisées » et non « inversées », écart comme mesure) ; programme, partie 3. **Juste.** |
| 35 / 36 | Avertissement, silence sur la famille 2 | K52 (le fine-tuning sur documents synthétiques n'implante pas toujours), fiche 10, K71, passation §5.1 et §5.2. **Juste.** Observation : K52 porte sur des documents synthétiques ; l'étendre à un LoRA sur démonstrations est une analogie raisonnable. |
| 37 / 38 | Avertissement, effet du seul reste | Fiche 1 ; C bis (recalculer le lens après tout entraînement, car il dépend des poids ; jeu de tokens ou extension, en disant laquelle) ; volet 6, §8 ; programme, partie 3. **Juste.** |
| 39 / 40 | Morceau de l'encadré du 2 octobre (renvoi) | Conforme aux morceaux du volet 2, dont la parade partielle des deux familles et du témoin conscient mais honnête (encadré, partie 1). Faute FR/EN : le français dit deux fois « ce paragraphe », l'anglais « this section ». Le renvoi reprend tout le §8 (l'organisme, l'entraînement, l'angle mort du J-lens) : le français passe à « cette section ». **Correction 29**, en français seul. Pas de *(v3.6)* : c'est conforme à la note d'ouverture telle que le groupe 1 l'a corrigée (« ou, pour les morceaux de l'encadré, sa date »). |
| 41 / 42 | Avertissement, couche et seuil | Programme, partie 3 ; M5 ; fiche 7. La règle « rien n'est choisi sur le jeu tenu à part » est au volet M, M4 : elle manquait aux sources de la limite. **Corrections 30-31**, comme le groupe 1 pour la même limite. Observation : K71 (« au même seuil ») serait la source la plus directe du « même seuil ». |
| 43 / 44 | Renvoi, fin du §8 | **Juste.** |

## Application

`corrections_groupe_4.json` est un JSON valide. Chaque « ancien » est une ligne entière d'insertion de la v3.6, présente une seule fois. Aucune ne touche une ligne de la v3.5.

J'ai simulé en mémoire l'ordre de `appliquer.py corrections` : groupes 1, 2, 3, puis 4. Les 22 + 22 + 24 corrections des groupes antérieurs passent. Les 31 du groupe 4 trouvent ensuite chacune leur texte une seule fois. Le livrable n'a pas été modifié.

## À signaler hors de ces tranches (non corrigé ici)

- **« Chaque direction pilotée dégrade… » sans dire que c'est la carte d'Opus 4.8.** Lignes FR 174 et 2684 de la v3.6 actuelle. Le groupe 1 a gardé la formule à la ligne 174 ; le groupe 2 l'a corrigée à la ligne 821.
- **La clause « pot de miel lu comme factice, (fiche 3) », avec « aucune parade connue » juste après la parade K63.** Lignes FR 4147, 7104 et 7165, et leurs jumelles anglaises. Les groupes 2 et 3 ont corrigé les lignes 718 et 1699.
- **Hiérarchie des sources pour l'explication par la troncature.** Le README du 13 septembre la dit « identifiée ». Le cours du 27 septembre, d'après la pièce P4, la fait dire au conditionnel. Partout où une insertion la donne comme un fait, la citer comme l'explication du README, au conditionnel (cours, volet 6, §2 ; M8).
