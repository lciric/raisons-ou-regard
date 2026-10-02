#!/usr/bin/env bash
# Fabrique le paquet de reprise du programme « Raisons ou regard ? », le zip scellé, le prompt de lancement rempli,
# et une copie en clair de la passation v1.3. Usage : bash faire_paquet_reprise.sh   (FORCE=1 pour un essai à blanc)
set -euo pipefail

S=/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad
REPO=/home/user/raisons-ou-regard
K=$S/papier/PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02
R=$S/raisons/RAISONS_OU_REGARD_PASSATION_2026-10-02
P1=$S/phase1_aveugle
U=/root/.claude/uploads/332d478c-da90-5795-bb10-27657d88c4d0
PACKSRC=$U/dd0b25d6-PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02_1.zip
WFROOT=/root/.claude/projects/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0
TS=$(TZ=Europe/Paris date +%Y-%m-%d_%Hh%M)
OUT=${OUT:-$S/livraison_reprise_$TS}
NOM=PACK_REPRISE_RAISONS_OU_REGARD_$TS
NOMS=SCELLE_NE_PAS_OUVRIR_AVANT_FEU_VERT_$TS
ST=$OUT/$NOM
PASS13=$REPO/claude/PASSATION_PAPIER_v1.3_2026-10-02.md

# 0. Garde-fous
echo "$(sha256sum $PACKSRC | cut -c1-64)" | grep -q '^9ce3082751b2a860df5d37c9a780963649873097a7f56f753cf835d71fe3b788$' \
  || { echo "ARRÊT : le paquet source n'a pas l'empreinte attendue"; exit 1; }
if grep -q 'ETAT_A_METTRE_A_JOUR_AVANT_LE_PAQUET' "$PASS13" && [ "${FORCE:-0}" != 1 ]; then
  echo "ARRÊT : le §3 de la passation v1.3 n'est pas à jour (retirer le marqueur après l'avoir mis à jour) (FORCE=1 pour un essai à blanc)"; exit 1
fi

rm -rf "$OUT"; mkdir -p "$ST"
cd "$ST"
mkdir -p 00_LIRE_D_ABORD 01_PROGRAMME_v1.1 02_ANTERIORITE 03_LECTURES 04_LE_PAPIER_DE_L_AXE \
  05_AXE_DOULEUR_PHASE1/consignes 06_PAQUETS_ET_PROMPTS_ANTERIEURS 07_DEPOT_GIT 99_ARCHIVES_ne_pas_lire

# 1. Les pièces
cp "$PASS13" 00_LIRE_D_ABORD/
cp $REPO/claude/PASSATION_PAPIER_v1.2_2026-10-02.md $REPO/claude/PASSATION_PAPIER_v1.0_2026-10-01.md \
   $REPO/claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md 00_LIRE_D_ABORD/
cp $REPO/passation/COMMENT_REPRENDRE_SUR_CLAUDE_AI.md 00_LIRE_D_ABORD/
cp $REPO/claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md $REPO/claude/PROGRAMME_RAISONS_OU_REGARD_v1.1_2026-10-01.pdf 01_PROGRAMME_v1.1/
cp $REPO/claude/ANTERIORITE_*.md 02_ANTERIORITE/
cp $REPO/claude/LECTURES_PRIORITAIRES_* $REPO/claude/CONTRE-LECTURE_FICHES_2026-10-01.md 03_LECTURES/
cp $REPO/papiers/arXiv_2609.16247v2_The_Pain_Axis.pdf $P1/pieces/papier/pain_axis_texte_par_page.txt 04_LE_PAPIER_DE_L_AXE/
cp $REPO/passation/LISEZMOI_PAQUET_PASSATION_PROGRAMME_2026-10-02.md $REPO/passation/MANIFEST_SHA256_PAQUET_PASSATION_PROGRAMME_2026-10-02.txt \
   $REPO/passation/00_LISEZ-MOI_NOUVEAU_COMPTE.md $REPO/passation/PROMPT_LANCEMENT_PAPIER_2026-10-02.txt 06_PAQUETS_ET_PROMPTS_ANTERIEURS/
cp $REPO/archives/PASSATION_PAPIER_v1.1_2026-10-02.md 99_ARCHIVES_ne_pas_lire/

# 2. La phase 1 de l'axe de douleur : livrable, travail des agents, pièces reçues, consignes, attestations
if [ -d $P1/livrable ] && [ -n "$(ls -A $P1/livrable)" ]; then
  mkdir -p 05_AXE_DOULEUR_PHASE1/livrable; cp -r $P1/livrable/. 05_AXE_DOULEUR_PHASE1/livrable/
fi
mkdir -p 05_AXE_DOULEUR_PHASE1/travail
tar -C $P1/travail --exclude='*.png' -cf - . | tar -C "$ST/05_AXE_DOULEUR_PHASE1/travail" -xf -
cp $P1/SHA256_PIECES.txt 05_AXE_DOULEUR_PHASE1/pieces_recues_par_les_agents_SHA256.txt
cp $WFROOT/workflows/scripts/axe-douleur-phase1*.js 05_AXE_DOULEUR_PHASE1/consignes/ 2>/dev/null || true
( cd 05_AXE_DOULEUR_PHASE1/consignes && sha256sum *.js > SHA256_CONSIGNES.txt 2>/dev/null || true )
python3 - "$WFROOT/subagents/workflows" "$ST/05_AXE_DOULEUR_PHASE1/attestations_des_agents.md" <<'EOF'
import json, sys, glob, os
racine, sortie = sys.argv[1], sys.argv[2]
lignes = ["# Les attestations des agents de la phase 1", "",
          "Extraites des journaux des workflows de la session : pour chaque agent qui a rendu son objet, le fichier écrit,",
          "les fichiers et les adresses qu'il déclare avoir ouverts, et ses alertes. Un agent arrêté avant la fin n'y figure pas.", ""]
for j in sorted(glob.glob(os.path.join(racine, '*', 'journal.jsonl'))):
    run = os.path.basename(os.path.dirname(j))
    lignes += [f"## Exécution {run}", ""]
    labels = {}
    for l in open(j, encoding='utf8'):
        d = json.loads(l)
        if d.get('type') == 'started': labels[d.get('agentId')] = d.get('label')
        r = d.get('result')
        if d.get('type') != 'result' or not isinstance(r, dict): continue
        lab = labels.get(d.get('agentId'), d.get('agentId'))
        lignes.append(f"### {lab}")
        for k in ('fichier', 'verdict', 'nombre_de_pistes'):
            if k in r: lignes.append(f"- {k} : {r[k]}")
        for k in ('fichiers_ouverts', 'urls_consultees', 'alertes', 'bloquants'):
            if k in r:
                v = r[k] or []
                lignes.append(f"- {k} ({len(v)}) :")
                lignes += [f"  - {x}" for x in v]
        if 'resume' in r: lignes.append(f"- resume : {r['resume']}")
        lignes.append("")
open(sortie, 'w', encoding='utf8').write("\n".join(lignes) + "\n")
EOF

# 3. Le dépôt git
git -C $REPO log --format='%H %ad %s' --date=iso > 07_DEPOT_GIT/git_log.txt
cp $REPO/README.md 07_DEPOT_GIT/README_DEPOT.md

# 4. Le LISEZMOI du paquet
cat > LISEZMOI.md <<EOF
# Paquet de reprise du programme « Raisons ou regard ? » ($TS, heure de Paris)

Fabriqué par la session Claude Code du 2 octobre 2026 (nouveau compte), pour l'instance qui reprend le programme. Chaque fichier a son
sha256 dans \`MANIFEST_SHA256.txt\`. Les documents de \`00\` à \`04\` sont des copies à l'octet du dépôt privé \`lciric/raisons-ou-regard\`.

**L'ordre de lecture**
1. \`00_LIRE_D_ABORD/PASSATION_PAPIER_v1.3_2026-10-02.md\`, en entier : ce que la session a fait, les décisions du 2 octobre, l'état de la
   tâche « axe de douleur » (§3) et la suite (§4).
2. \`00_LIRE_D_ABORD/PASSATION_PAPIER_v1.2_2026-10-02.md\`, en entier : le document de fond.
3. \`00_LIRE_D_ABORD/PASSATION_PAPIER_v1.0_2026-10-01.md\`, puis la partie ouverte du complément de l'architecte.
4. Le reste, dans l'ordre du §2 de la passation v1.2.

**Où est chaque pièce**
- \`00_LIRE_D_ABORD/\` : les passations, la partie ouverte du complément, et le mode d'emploi pour Lazar (\`COMMENT_REPRENDRE_SUR_CLAUDE_AI.md\`).
- \`01_PROGRAMME_v1.1/\` : le programme v1.1, markdown et PDF. Le nom du markdown ne porte pas le numéro.
- \`02_ANTERIORITE/\` : les onze rapports bruts d'antériorité, et les consignes complètes des sept agents de la nuit.
- \`03_LECTURES/\` : les lectures prioritaires, leurs fiches (la partie C est la genèse de l'idée) et leur contre-lecture.
- \`04_LE_PAPIER_DE_L_AXE/\` : *The Pain Axis* (arXiv 2609.16247v2), tel qu'arXiv le sert, et son texte extrait page par page.
- \`05_AXE_DOULEUR_PHASE1/\` : la phase 1, faite par des agents vierges.
  - \`livrable/\` : le fichier de pistes, s'il est écrit.
  - \`travail/\` : les fichiers des agents.
  - \`pieces_recues_par_les_agents_SHA256.txt\` : les seules pièces qu'ils pouvaient lire.
  - \`consignes/\` : leurs consignes exactes, avec leur empreinte.
  - \`attestations_des_agents.md\` : ce que chaque agent déclare avoir ouvert.
- \`06_PAQUETS_ET_PROMPTS_ANTERIEURS/\` : le LISEZMOI et le manifeste du paquet du 2 octobre (9 h 15), le LISEZ-MOI du nouveau compte, le
  premier prompt de lancement du papier.
- \`07_DEPOT_GIT/\` : l'historique et le README du dépôt.
- \`99_ARCHIVES_ne_pas_lire/\` : la passation v1.1, remplacée par la v1.2.

**Scellé, et absent de ce paquet** : les versions 1.2 et 1.3 du programme et la partie scellée du complément. Elles sont dans
\`$NOMS.zip\`, que Lazar garde à part et ne donne qu'après la phase 1 de la tâche « axe de douleur », à son feu vert.
EOF

# 5. Le manifeste, puis le zip
find . -type f ! -name MANIFEST_SHA256.txt | LC_ALL=C sort | sed 's|^\./||' | xargs -d '\n' sha256sum > MANIFEST_SHA256.txt
cd "$OUT" && zip -q -r -X "$NOM.zip" "$NOM"

# 6. Le zip scellé, tiré du paquet source sans rien lire du contenu
TMP=$(mktemp -d)
unzip -q "$PACKSRC" 'PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02/09_SCELLE_jusqu_a_la_fin_de_la_phase_1/*' -d "$TMP"
mkdir -p "$TMP/$NOMS"
mv "$TMP"/PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02/09_SCELLE_jusqu_a_la_fin_de_la_phase_1/* "$TMP/$NOMS/"
cat > "$TMP/$NOMS/LISEZMOI_SCELLE.md" <<EOF
# Scellé : ne pas ouvrir avant le feu vert de Lazar

Ce zip contient les versions 1.2 et 1.3 du programme « Raisons ou regard ? » (markdown et PDF) et la partie scellée du complément de
l'architecte, à l'octet, tirées du paquet \`PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02.zip\` (sha256 \`9ce3082751b2a860…\`).
On ne l'ouvre qu'après avoir écrit le fichier de pistes indépendantes de la phase 1 de la tâche « axe de douleur », donné son empreinte,
et reçu le feu vert de Lazar (passation v1.2, §6 et annexe B).
EOF
( cd "$TMP/$NOMS" && find . -type f ! -name MANIFEST_SHA256.txt | LC_ALL=C sort | sed 's|^\./||' | xargs -d '\n' sha256sum > MANIFEST_SHA256.txt )
# contrôle : les empreintes doivent être celles du manifeste du paquet source
for h in 06b425f7820ca3d3 fca1f6e9a989d584 332fb1c396684c95 a5ef0e51efdb4ba6 72ad347d469954e5; do
  grep -q "^$h" "$TMP/$NOMS/MANIFEST_SHA256.txt" || { echo "ARRÊT : pièce scellée $h introuvable ou altérée"; exit 1; }
done
( cd "$TMP" && zip -q -r -X "$OUT/$NOMS.zip" "$NOMS" )
rm -rf "$TMP"

# 7. Le prompt rempli, la passation en clair, et le récapitulatif
SHAP=$(sha256sum "$OUT/$NOM.zip" | cut -c1-64); SHAS=$(sha256sum "$OUT/$NOMS.zip" | cut -c1-64)
sed -e "s|@@NOM_PAQUET@@|$NOM.zip|" -e "s|@@SHA_PAQUET@@|$SHAP|" -e "s|@@NOM_SCELLE@@|$NOMS.zip|" -e "s|@@SHA_SCELLE@@|$SHAS|" \
  $REPO/passation/PROMPT_LANCEMENT_PAPIER_CLAUDE_AI_MODELE.txt > "$OUT/PROMPT_LANCEMENT_PAPIER_CLAUDE_AI_$TS.txt"
cp "$PASS13" "$OUT/"
cp $REPO/passation/COMMENT_REPRENDRE_SUR_CLAUDE_AI.md "$OUT/"
rm -rf "$ST"
cd "$OUT"
echo "== Livraison : $OUT"
ls -la "$OUT"
echo "== Empreintes"
sha256sum *.zip *.txt *.md
echo "== Fichiers dans le paquet : $(unzip -l "$NOM.zip" | tail -1)"
echo "== Fichiers dans le zip scellé : $(unzip -l "$NOMS.zip" | tail -1)"
