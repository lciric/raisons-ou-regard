# Reprendre le programme dans Claude Code depuis un autre compte (2 octobre 2026)

**Pour qui.** Pour Lazar, s'il veut continuer le travail de la session Claude Code du 2 octobre dans une session Claude Code ouverte avec un autre compte Claude.

**Le principe.** Tout passe par le dépôt GitHub privé `lciric/raisons-ou-regard`. Une session Claude Code tourne dans un conteneur éphémère : seul ce qui est poussé dans le dépôt survit d'une session à l'autre et d'un compte à l'autre.

**Une alternative.** Pour reprendre dans une conversation claude.ai plutôt que dans Claude Code, voir `COMMENT_REPRENDRE_SUR_CLAUDE_AI.md`, dans le même dossier.

---

## 1 · Ce qui suit, et ce qui ne suit pas

**Ce qui suit** : tout ce qui est dans le dépôt.
- Le README, avec la table des décisions.
- La passation v1.3 (`claude/PASSATION_PAPIER_v1.3_2026-10-02.md`) : ce que la session a fait, les décisions, l'état des tâches, ce qui reste.
- Le programme v1.1, les passations, les rapports d'antériorité, les fiches de lecture.
- La mini-spec v0.1 et le code du pipeline de données, au fur et à mesure qu'ils sont poussés.

**Ce qui ne suit pas**
- La conversation elle-même : la nouvelle session ne la voit pas.
- Les fichiers du conteneur qui ne sont pas encore dans le dépôt : le travail de la phase 1 de l'axe de douleur, la carte des angles, le cours v3.6 en cours.
- Les agents qui tournent en arrière-plan : ils s'arrêtent avec la session.
- L'environnement : le réseau autorisé et les variables d'environnement sont propres à chaque compte (§3, étape 2).

---

## 2 · Avant de quitter ce compte : le dire à la session

Un message suffit, par exemple : « on change de compte, pousse tout ».

La session fait alors trois choses :
1. Elle pousse dans le dépôt tout le travail du conteneur, sauf les pièces scellées.
2. Elle met à jour l'état des tâches dans la passation v1.3 (§3).
3. Si tu le demandes, elle fabrique en plus le paquet de reprise : des zips à garder de ton côté.

**Les pièces scellées ne vont jamais dans le dépôt.** C'est-à-dire le zip scellé, la v1.2 et la v1.3 du programme, et la partie scellée du complément. Garde le zip scellé de ton côté : tu le donneras à la nouvelle session au feu vert de la phase 2.

---

## 3 · Sur l'autre compte, pas à pas

### Étape 1 · L'accès au dépôt
1. Connecté à l'autre compte Claude, va sur https://claude.ai/connect-github.
2. Connecte un compte GitHub qui a accès au dépôt privé `lciric/raisons-ou-regard`. Deux possibilités :
   - ton compte GitHub `lciric` lui-même ;
   - un autre compte GitHub, que tu invites d'abord comme collaborateur du dépôt. Sur GitHub : le dépôt, puis *Settings*, *Collaborators*, *Add people*.
3. Si l'application Claude GitHub n'est pas installée sur le dépôt pour ce compte GitHub, installe-la depuis la même page.

### Étape 2 · L'environnement
Dans une session Claude Code sur le web, l'environnement se règle depuis son menu, dans la barre de titre de la session, puis *Edit*. On peut aussi en créer un nouveau.

**Le réseau (*Network access*).** Ajouter aux domaines autorisés, ou choisir un niveau d'accès plus large :
- `huggingface.co`, pour télécharger le tokenizer et les modèles. Si un téléchargement est refusé, la session dit quel domaine ajouter.
- `vast.ai` et `console.vast.ai`, pour les GPU.
- Les niveaux d'accès sont décrits sur https://code.claude.com/docs/en/claude-code-on-the-web.

**Les variables d'environnement**
- `HF_TOKEN` : le jeton Hugging Face, à accès restreint, qui ouvre le modèle Llama 3.1 8B Instruct.
- `VAST_API_KEY` : la clé vast.ai.
- `ANTHROPIC_API_KEY` : la clé de l'API Claude, pour générer les données et faire tourner les juges.

**Les règles qui vont avec**
- Les clés se saisissent dans les réglages de l'environnement, jamais dans le chat. La session ne dit que si elles sont présentes, oui ou non.
- Une session déjà ouverte ne voit pas un changement d'environnement : il faut en ouvrir une nouvelle.
- Règle confirmée le 2 octobre : aucune clé de l'API Claude sur les machines vast.ai. Les appels à l'API partent de la session Claude Code ou de ta machine.

### Étape 3 · Ouvrir la session
Ouvre une nouvelle session Claude Code avec le dépôt `lciric/raisons-ou-regard` sélectionné et l'environnement de l'étape 2. Le premier message peut être celui-ci, à coller tel quel :

> Tu reprends le programme « Raisons ou regard ? » dans le dépôt `lciric/raisons-ou-regard`. Lis d'abord, en entier : `README.md`, puis `claude/PASSATION_PAPIER_v1.3_2026-10-02.md`, puis les documents dans l'ordre que la passation indique. Le zip scellé n'est pas dans le dépôt : je te le donnerai au feu vert de la phase 2 de l'axe de douleur, et tu ne l'ouvres pas avant. Vérifie que `HF_TOKEN`, `VAST_API_KEY` et `ANTHROPIC_API_KEY` sont présentes, en répondant seulement oui ou non pour chacune, jamais leur valeur. Aucun agent sans ma demande. Dis-moi ensuite où en est le travail et ce que tu proposes de faire.

### Étape 4 · Vérifier
La nouvelle session doit :
- lire le dépôt et y pousser une branche ou un commit ;
- dire si les trois variables sont présentes ;
- joindre `huggingface.co`.

Si l'une de ces vérifications échoue, elle dit laquelle et ce qu'il faut régler.

---

## 4 · L'appli PC ou le web

- **Les sessions dans le cloud** sont les mêmes dans l'appli PC et sur le web : même conteneur, mêmes réglages d'environnement.
- **Ce que l'appli PC ajoute** : des sessions qui tournent sur ton ordinateur. Elles ont tout ton réseau, arXiv et Hugging Face compris, alors que la session du 2 octobre ne les joignait pas. Les fichiers y restent d'une fois sur l'autre.
- **Ce que l'appli PC coûte**
  - Ta machine doit rester allumée pendant le travail.
  - On revient aux règles de ta machine Windows : une commande PowerShell par bloc, ne jamais retirer `NoDefaultCurrentDirectoryInExePath=1`, les clés en local.
- **Les crédits** : non vérifié. À la connaissance de la session, ils dépendent du compte, pas de l'appli.
- **Le conseil de la session**
  - Une session cloud, avec un environnement bien réglé, pour le pipeline de données et le pilotage de vast.ai.
  - Une session sur ton PC pour ce que le réseau du cloud refuse, comme la lecture des papiers sur arXiv.

---

## 5 · Ce qui ne change pas, quel que soit le compte

- Aucun agent sans ta demande. Quand tu le demandes, tous les appels partent dans le même message.
- Les clés d'API ne s'affichent jamais.
- Rien de public sans ton accord explicite. Le dépôt reste privé.
- Un refus d'un modèle ou d'une API ne se rejoue pas et ne se reformule pas.
- Le copilote et ses documents restent à son instance.
- Le zip scellé ne s'ouvre qu'à ton feu vert, après la phase 1 de l'axe de douleur.
