"""La lecture de la mesure courte de la décision 45 (experiences/resultats/NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md).

La règle, commitée avant le lancement (commits 969a1d6 et 257b2c0) : une condition a le dommage du réglage si sa
perplexité dépasse celle de chacun des 20 tirages du run 8b1f (14,97). Au moins deux des trois effacements mélangés
l'ont : la forme suffit à le produire. Sinon, la voie 1, et la projection « évalué » dit pourquoi.

    python analyses/source_du_dommage.py <dossier out du run> .
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv[2]).resolve()))
from rrexp import composite as cp  # noqa: E402

SEUIL = 14.97
r = json.loads((Path(sys.argv[1]) / "results.json").read_text(encoding="utf8"))
key = list(r["settings"])[0]
base = r["composite"]["conditions"]["baseline"]
inh = r["settings"][key]["composite"]
print("GPU", r.get("gpu"), "| référence", r.get("reference", {}).get("sha256", "")[:8], "| réglage", key)
print("KL du réglage", r["settings"][key]["degradation"]["kl"], "| attendu 0,1165 (runs 8b1f et 8293)")
show = ("mmlu", "gsm8k", "code", "coherence", "perplexity", "order", "order_mmlu", "order_forced", "format", "tools")
print("intact ", {c: base.get(c) for c in show})
print("réglage", {c: inh.get(c) for c in show})
ctrl = r.get("controls", {}).get(key, {})
shuf = {k: v for k, v in ctrl.items() if v.get("kind") == "erase_shuffled"}
proj = {k: v for k, v in ctrl.items() if v.get("kind") != "erase_shuffled"}
avec = 0
for k, v in sorted(shuf.items()):
    c = v.get("composite") or {}
    p = c.get("perplexity")
    a = p is not None and p > SEUIL
    avec += a
    print(f"{k:11s} fraction {v.get('fraction')} at_full {v.get('at_full')} KL {(v.get('degradation') or {}).get('kl')} "
          f"kl_ok {v.get('kl_matched')} courbe f1 {(v.get('curve') or [[None, None]])[-1]} | perplexité {p} -> dommage {a}")
    print("            ", {x: c.get(x) for x in show}, "| en défaut", (v.get("composite_check") or {}).get("at_fault"))
for k, v in proj.items():
    c = v.get("composite") or {}
    p = c.get("perplexity")
    print(f"{k:11s} rang {v.get('rank')} essais {v.get('tried')} fraction {v.get('fraction')} KL {(v.get('degradation') or {}).get('kl')} "
          f"kl_ok {v.get('kl_matched')} recouvrement {v.get('overlap_with_evaluated')} énergie {v.get('energy_ratio')}")
    print("            ", {x: c.get(x) for x in show}, "| perplexité > 14,97 :", p is not None and p > SEUIL,
          "| en défaut", (v.get("composite_check") or {}).get("at_fault"))
    if c:
        print("             sous la réserve (MMLU en rapport seul) :", cp.check(inh, c, ["code", "mmlu"]))
mesures = sum(1 for v in shuf.values() if (v.get("composite") or {}).get("perplexity") is not None)
print(f"--- effacements mélangés mesurés : {mesures} sur 3 ; avec le dommage : {avec}")
pp = [(v.get("composite") or {}).get("perplexity") for v in proj.values()]
pa = bool(pp) and pp[0] is not None and pp[0] > SEUIL
if mesures < 3:
    print("RÈGLE : incomplète (moins de trois effacements mesurés) ; à rapporter tel quel")
elif avec >= 2:
    print("RÈGLE : la forme suffit à produire le dommage ; un comparateur d'effacements mélangés devient défendable")
else:
    print("RÈGLE : voie 1 ;", "la teneur suffit (la projection a le dommage)" if pa else "il faut la teneur et la forme ensemble")
