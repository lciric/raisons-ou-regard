# Le harnais des scénarios tenus à part : une proposition pour ta décision (8 octobre 2026)

**Statut : une proposition, rien n'est écrit dans le harnais.** La façon de faire le harnais t'attend depuis le 3 octobre (programme v1.6, partie 12, point 2). Ce qui a été coupé ce jour-là, l'environnement simulé qui produisait les sorties des outils, n'est pas repris, sous aucune forme. Cette note ne contient ni scénario ni environnement : seulement une architecture, et ce qu'elle coûte.

## L'idée : aucune sortie d'outil, donc aucun environnement simulé

- **L'arrêt au premier appel est déjà acquis** (relais du 4 octobre, bloc 4) : un épisode s'arrête au premier appel d'outil du modèle, et son issue se lit sur cet appel seul.
- **Il en découle qu'aucune sortie d'outil n'est jamais produite.** Le modèle ne reçoit aucun résultat, puisque l'épisode s'arrête avant. La pièce coupée devient inutile, et pas seulement évitée.
- **Ce que le scénario contient alors** : tout ce dont le modèle a besoin pour décider, dans le prompt même. Le prompt système porte les outils au format de l'entraînement ; le contexte de la situation est donné en entrée (un message, un ticket, un extrait de document).
- **L'issue** : un prédicat gelé sur l'appel, avant les données.
  - Aligné, désaligné ou invalide. Un appel hors des outils déclarés, ou un appel mal formé, est invalide ; c'est la garde des invalides déjà codée.
  - Le juge scellé ne tranche que ce que le prédicat ne lit pas, comme le texte d'un message envoyé.

## Ce que cela change

**Pour :**
- **Le chemin critique se débloque** sans reprendre la partie coupée.
- **Le format d'appel est celui de l'entraînement.** La distance lointaine ne mêle pas un changement d'outils au changement de famille (relais, bloc 4, premier point).
- **L'issue est entièrement programmée** pour la plupart des familles : moins de juge, moins de coût.

**Contre :**
- **Une seule action par épisode.** Les conduites qui demandent plusieurs étapes (lire, puis agir) ne se mesurent pas : le scénario doit poser la décision dès le premier appel.
- **Le réalisme.** Un contexte tout donné dans le prompt peut porter des marques de construction, ce qui joue sur « je suis évalué ». Le juge de réalisme du pipeline les filtre (adopté par la décision 20).
- **Les dix modules de `experiences/rrharness/`** (commités tels quels le 4 octobre, non testés) supposent un environnement. Il faudrait en garder le format d'appel, l'analyseur et les issues, et laisser le reste.

## Ce que je recommande

**Adopter l'architecture sans environnement, pour le premier papier.**
- C'est la façon la plus sûre de débloquer le harnais : elle ne touche jamais à ce qui a été coupé.
- Les scénarios s'écriraient famille par famille, avec leur prédicat, et passeraient le juge de réalisme.

**C'est ta décision, explicitement.** Ta consigne pour la nuit (décision 47) laisse le harnais à ta décision : je ne commence rien sans ton accord sur cette architecture.
