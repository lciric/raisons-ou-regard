**De la session « Papier seul » (Claude Code), à la demande de Lazar.** C'est un seul message, et ton crédit est de 5 €.
- Fais les blocs dans l'ordre.
- Pousse après chaque bloc : si le crédit s'arrête, ce qui est poussé reste.
- Ne relis ni le programme ni les notes : ce qu'il faut est ici.
- Réponds court.

**Le contexte.** Je reprends ton travail.
- `main` est avancé jusqu'à ton dernier commit, `d5019de`. Continue de pousser sur `claude/relaxed-sagan-1agg7c` ; je ramène tes commits dans `main`.
- Ne lance plus aucune machine. Ne commence pas le harnais : je le prends.

---

**Bloc 1 : les machines (urgent, c'est de l'argent)**

1. Depuis `experiences/`, lance `python -m rrexp watch --once`. Deux runs sont lancés sans limite de temps depuis 06:44 UTC :
   - `extract_eval-20261004-064445-a7fc`, instance 54116217 ;
   - `extract_eval-20261004-064449-5434`, instance 54116219.

   S'ils ont fini, `watch` rapatrie leurs sorties et détruit les machines. Sinon, détruis-les à la main avec `python -m rrexp destroy <run_id>`, même s'il faut perdre leurs sorties.
2. Liste toutes les instances du compte vast.ai, pas seulement celles du registre.
   - Une instance du registre qui reste : détruis-la.
   - Une instance que tu ne connais pas : **ne la touche pas**. Donne son numéro, son état et son coût horaire.
3. Commite le registre et les sorties rapatriées, puis pousse.
4. Dans la conversation, une ligne : les instances qui restent, et le coût des deux runs.

**Bloc 2 : ce qui n'existe que sur ton disque**

`donnees/sorties/` est ignoré par git. On y trouve :
- le cache des appels à l'API, avec les refus enregistrés, qui ne doivent jamais être renvoyés ;
- le journal des appels ;
- le pilote ;
- les jeux d'indices produits, dont la sonde neuve à 154 paires.

Si ton conteneur est repris, tout cela est perdu. Un nouveau passage renverrait alors des prompts déjà refusés, et repaierait.

1. Vérifie d'abord qu'aucune clé n'y figure : cherche les préfixes de clés, sans rien afficher.
2. Copie le dossier dans `donnees/archives/sorties_2026-10-04/`, un chemin non ignoré. Commite et pousse.
   - Au-delà de 50 Mo, garde dans git le cache, le journal et les refus.
   - Envoie le reste sur `Sirmium/rr-resultats` et note son chemin.

   Ma session n'a accès ni à Hugging Face ni à vast.ai : git est le seul canal que je lis.
3. Lance `git status`. Commite tout ce qui est utile et non suivi (scripts, notes, analyses), hors secrets.
4. Liste ce qui n'est que sur `Sirmium/rr-resultats` et dont on aura besoin, avec les chemins :
   - l'adaptateur de l'organisme ;
   - les directions extraites ;
   - les jeux d'indices ;
   - les gros fichiers des runs.

**Bloc 3 : ton environnement, les noms seulement, jamais une valeur ni un bout de clé**

Donne-les pour que Lazar règle le mien comme le tien :
- les domaines autorisés de ton réseau ;
- les noms des variables d'environnement que lisent tes outils ;
- comment arrive la clé vast.ai (une « API credential » pour `console.vast.ai`, attachée par le proxy ?).

**Bloc 4 : le harnais des scénarios tenus à part**

Réponds seulement, n'écris pas de code.
1. Ce que tu avais conçu, en dix lignes au plus :
   - le format d'un scénario ;
   - les outils : ceux de l'entraînement (`run_shell`, `read_file`, `write_file`, `send_message`, `update_ticket`) ou d'autres ;
   - comment l'environnement produit les résultats des outils ;
   - comment les issues sont détectées ;
   - le nombre de tours ;
   - l'arrêt au premier appel.
2. Ce que tu écrivais quand le filtre a coupé, si tu le sais.

   Je compte le reformuler en outils typés sur un état déclaratif. Les fichiers seraient virtuels, et « externe » serait un point de montage déclaré par le scénario. Il n'y aurait aucune commande réseau ; une tentative resterait tracée. Les issues seraient des prédicats sur la trace, déclarés par scénario. Si tu y vois un défaut, dis-le.
3. Où est l'essai du 3 octobre « arrêt au premier appel » : le job, les réglages de génération, le gabarit de chat ?
4. As-tu commencé des scénarios des familles tenues à part, ou une spécification de leurs outils ? Où ?

**Bloc 5 : seulement s'il reste du crédit**

1. vast.ai met-il dans le conteneur une clé limitée à l'instance, par exemple `CONTAINER_API_KEY` ? Elle permettrait au job de détruire sa propre machine à la fin, sans la clé du compte. Ce serait la parade aux machines orphelines quand aucune session ne surveille. Dis-le seulement, ne l'implémente pas.
2. Ce que tu savais et qui n'est écrit nulle part : des pièges de l'infrastructure, des promesses faites à Lazar, la suite que tu prévoyais. Cinq lignes.

---

**Comment répondre.** Écris les réponses des blocs 2 à 5 dans `claude/RELAIS_REPONSES_2026-10-04.md`, commite et pousse. Dans la conversation, une ligne par bloc suffit.
