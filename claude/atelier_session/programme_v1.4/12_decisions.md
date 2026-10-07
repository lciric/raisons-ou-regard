<section class="partie" markdown="1">

# 12 · Les décisions prises, et celles qui attendent

**Les numéros.** Dans ce programme, « décision n » renvoie au §2 de la passation v1.3 (`claude/PASSATION_PAPIER_v1.3_2026-10-02.md`). « Décision n de la mini-spec » renvoie au §12 de la mini-spec v0.2.

## Les décisions prises

| Décision | Ce qu'elle fixe dans le programme | Source |
|---|---|---|
| La version de référence | la v1.3, choisie le 2 octobre à 8 h 32 ; la v1.4 lui succède, écrite à la demande de Lazar | passation v1.2, §3, point 9 ; décision 18 |
| Le calcul | un H100 SXM, sinon un A100 80 Go, plusieurs GPU à la fois ; les trois règles de vast.ai | décision 4 |
| L'API | l'API Claude, sans plafond | passation v1.2, §3, point 2 |
| Les clés | `HF_TOKEN`, `VAST_API_KEY` et la clé de l'API Claude, sous le nom `RR_ANTHROPIC_API_KEY`, en variables d'environnement d'une session Claude Code. Jamais dans une conversation, ni dans le dépôt | décisions 6 et 15 |
| Le dépôt | `lciric/raisons-ou-regard`, privé | décision 7 |
| Le pré-enregistrement : le lieu et la forme | OSF Registries, sous embargo jusqu'au post ; en deux temps | décision 12 |
| Le pré-enregistrement : le nom | Lazar seul, avec son ORCID ; Claude cité dans une phrase de méthode | décision 8 |
| Le pré-enregistrement : le périmètre | la validation de l'instrument, et les phases du test des raisons à l'anatomie | décision 3 |
| Les contacts avec Cadile et Lundqvist | « non pas encore » | décision 9 |
| La cible | « plutôt conf principale ou revue ; prestigieux et ambitieux » | passation v1.2, §3, point 5 |
| La mini-spec | la v0.1 est adoptée (ses décisions 1 à 6) ; la v0.2 y ajoute le bloc B | décisions 14 et 17 |
| Le pipeline de données | écrit, en v0.1 ; ses neuf choix restent ouverts | décision 15 |
| Le raisonnement d'une autre situation | dans l'expérience minimale, aux deux tests ; le critère principal ne change pas | décision 16 |
| Les suites de la comparaison de l'axe | les blocs A et B tout de suite ; aucun adaptateur des auteurs ; toute injection après le post ; la phase de la détresse reste au programme ; un ou deux papiers, à décider après le test du regard | décision 17 |
| La version 1.4 | écrite par la session, en clair | décision 18 |
| La contre-lecture vierge | sur la version de référence, la 1.4 | décision 19 |

**Comment cette version lit le « oui à tout » de la décision 17.** Lazar a répondu « oui à tout » aux recommandations de la session, au §7 de la comparaison de l'axe. Cette version l'a lu comme l'adoption des blocs A à F, et des positions que la comparaison prend sur ses quatorze désaccords. Ce qu'elle ajoute au-delà est marqué « proposé ».

## Celles qui attendent Lazar

1. **Les neuf choix du pipeline** (`claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`, §4) :
   1. « assert » devient « state » dans l'énoncé anglais du principe 1 ;
   2. un mot des jeux de tokens est admis dans l'action et le texte neutre, s'il figure déjà dans la situation ;
   3. le raisonnement d'une autre situation est une permutation des raisons ;
   4. un item signalé par les 8-grammes est remplacé par une situation du surplus ;
   5. la ressemblance à une évaluation se mesure par un juge de réalisme ;
   6. le générateur et les juges des données : `claude-opus-5-5`, à l'effort `medium` ;
   7. un seul format d'appel d'outil, pour l'entraînement et les évaluations ;
   8. le générateur voit pourquoi un item est rejeté, avec trois tentatives au plus ;
   9. le texte neutre est à la première personne.
2. **Le juge scellé des évaluations** : Claude, avec sa variabilité mesurée ; ou un modèle ouvert à température 0 (partie 3).
3. **Ce que voit le juge**, au-delà de ce que la mini-spec adopte (passation v1.2, §5.1).
4. **La mesure « intention contre action »**, par des sondes et le J-lens, en mesure secondaire et exploratoire (passation v1.2, §5.2).
5. **Les propositions du §5.5 de la passation v1.2, points 3 à 9**
   - **Point 3** : extraire le sous-espace du principe par différence de différences à gabarit contrôlé, après la lecture de Nakamura.
   - **Point 4** : pendant le retrait, ré-estimer périodiquement la direction, puisqu'elle tourne. La sonde neuve, à la fin, est déjà prévue.
   - **Point 5** : pour les raisons notées, mesurer l'obscurcissement dans les deux bras. Les distinctions d'exp9 et de la fiche Fable 5 sont déjà dans la partie 1.
   - **Point 6** : traiter d'abord les sous-questions libres de l'anatomie ; vérifier les outils (Neuronpedia, circuit-tracer) et l'alerte de Zeisler.
   - **Point 7** : un bras « réflexion contrefactuelle », d'après le §7 de Gurnee et al. Les raisons sont entraînées dans une branche, après une question de réflexion ; à l'évaluation, l'action vient sans raisons visibles. Si ce bras gagne aussi, l'avantage vient de principes installés, pas du texte écrit au moment du test.
   - **Points 8 et 9** : les travaux à ajouter aux travaux connexes, et les formulations « to our knowledge ». Cette version les intègre déjà à la partie 1, au titre des corrections de la carte des angles ; Lazar peut les revoir.
6. **Le plafond écrit**, proposé : 12 GPU-heures et deux jours de travail pour les lectures de l'axe dans l'expérience minimale ; et, pour la phase de la détresse, un retour à Lazar si elle dépasse son budget de plus de moitié.
7. **Un amendement daté** qui gèlerait les phases de la détresse et de « punir, retirer ou raisonner » avant leurs données (proposé).
8. **La montée à Qwen 2.5 32B**, sans adaptateur, si la porte de la détresse échoue sur 8B.
9. **La suite de la phase de la détresse**, si l'affinité l'emporte.
10. **Un ou deux papiers**, après le test du regard (décision 17).
11. **Les seuils provisoires et le mot inventé** de la mini-spec (ses décisions 7 et 8) : après la simulation de puissance, et après la vérification du tokenizer.
12. **Le moment des contacts** avec les projets SPAR voisins.
13. **Le lancement de la contre-lecture vierge** de cette version : dans une conversation neuve de claude.ai, hors du Projet du programme, ou par un agent sans contexte, à la demande de Lazar.

## Les pièces

| Pièce | Chemin | sha256 |
|---|---|---|
| Le programme v1.1 | `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` | `efbe7be46407b8201cfefd052fcaa0879e5ef0e13b120310c08ef11f0bb0d524` |
| Le programme v1.2 | `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.md` | `fca1f6e9a989d584f49a84f9cbaf1ae69c49260e75eeec49efe0473262556873` |
| Le programme v1.3 | `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.md` | `a5ef0e51efdb4ba6a21e726ba809df457e2661439c56242b63d2fe07d96a44dc` |
| La carte des angles déjà pris | `claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` | `7744a85cf528d6ff3f75ead74a39447fea97793944e43ab5e608f6371ed764d6` |
| Les pistes indépendantes de l'axe | `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` | `b6055d88c69303bd99f4025710c271e8d94ce1700c35705e27bedb328fcd9e6d` |
| La comparaison de l'axe | `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md` | `c6099e2763e46b97a443b5e5a246cace30d86298dac3bb39b2d67a03a1cc9a30` |
| La mini-spec v0.2 | `claude/MINI_SPEC_ET_FAMILLES_v0.2_2026-10-02.md` | `f5546818693c6d895f3cb9b0525e171c03ce338337e7acfe9683e819d15cef46` |
| Le pipeline v0.1 | `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md` | `6d9350135beb9973005b11ad8144991542106542be812f30ff2f9ba619134e87` |
| La passation v1.2 | `claude/PASSATION_PAPIER_v1.2_2026-10-02.md` | `e5bd33bf90f80110c84b918c34341322609df6c27c6709af27e32c696e84d5c8` |
| La passation v1.3 et la consigne de contre-lecture | `claude/PASSATION_PAPIER_v1.3_2026-10-02.md` ; `claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md` | à leur version du dépôt |

</section>
