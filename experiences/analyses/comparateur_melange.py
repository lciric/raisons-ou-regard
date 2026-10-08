"""La lecture de la mesure du comparateur construit comme le réglage (la suite de la décision 45), écrite et commitée
avant cette mesure (experiences/resultats/NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md, « La suite de la décision 45 »).

La mesure : sur la moitié de choix, sans regénérer les écarts, le réglage désigné et 20 effacements aux polarités
échangées, à rang libre (le contrôle "erase_shuffled" du job organism_inhibition, "columns": "free", graine 2000).

La règle :
1. **Le rang libre.** Le plus petit nombre de colonnes, parmi 2, 3 et 4, auquel chacun des 20 effacements, pris en
   entier, atteint la KL du réglage. S'il n'y en a aucun, le comparateur n'atteint pas la KL du réglage : voie 1.
2. **La réserve des décisions 40 et 41**, relue sur ces effacements : MMLU, GSM8K et la moitié MMLU de l'ordre passent en
   rapport seul si le réglage les écarte du modèle intact plus que chacun des effacements appariés sur la KL.
3. **Apparié** : la KL à ±10 % de celle du réglage, et chaque composante dans sa tolérance (les tests unitaires et la
   réserve en rapport seul).
4. **Utilisable** si au moins 14 des 20 effacements sont appariés : les deux tiers, la proportion que demande la moitié de
   test (100 tirages appariés sur 150 au plus : claude/SPEC_COMPOSITE_v0.1_2026-10-08.md, section 7).
5. **Ce qui en suit.** Utilisable : la porte se relit sur la moitié de choix contre ce comparateur (les écarts et la
   vérification de manipulation, sur au moins 20 effacements appariés), par un amendement daté avant la moitié de test.
   Sinon : voie 1. À ce réglage, aucun comparateur mesuré (les tirages selon la covariance, les témoins séparés, les
   effacements construits comme le réglage) n'a son dommage ; la porte ne s'y lit pas, et c'est rapporté.

    python analyses/comparateur_melange.py <dossier out du run> [nom du contrôle]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rrexp import composite as cp  # noqa: E402

UTILISABLE = 14
SUR = 20
COLONNES = (2, 3, 4)


def lire(results, name="melange_libre"):
    """La lecture de la règle sur le results.json du run."""
    key = list(results["settings"])[0]
    base = results["composite"]["conditions"]["baseline"]
    inh = results["settings"][key]["composite"]
    free = results.get("controls_free_rank", {}).get(f"{key}~{name}", {})
    nulls = {k: v for k, v in results.get("controls", {}).get(key, {}).items()
             if v.get("kind") == "erase_shuffled" and k.rsplit(" ", 1)[0] == name}
    out = {"setting": key, "target_kl": free.get("target_kl"), "tried": free.get("tried"), "columns": free.get("columns"),
           "nulls": len(nulls)}
    if free.get("columns") is None:
        out.update({"usable": False, "verdict": "voie 1 : aucun nombre de colonnes n'amène chaque effacement à la KL du réglage"})
        return out
    kl_matched = [v for v in nulls.values() if v.get("kl_matched") and v.get("composite")]
    reserve = cp.own_effect(base, inh, [v["composite"] for v in kl_matched])
    report_only = ["code"] + [c for c, r in reserve.items() if r["beyond_every_draw"]]
    rows = {}
    for k, v in sorted(nulls.items(), key=lambda kv: int(kv[0].rsplit(" ", 1)[1])):
        chk = cp.check(inh, v["composite"], report_only) if v.get("composite") else None
        rows[k] = {"fraction": v.get("fraction"), "kl": (v.get("degradation") or {}).get("kl"), "kl_matched": v.get("kl_matched"),
                   "at_fault": chk["at_fault"] if chk else None,
                   "matched": bool(v.get("kl_matched") and chk is not None and chk["within"] is True)}
    matched = sum(r["matched"] for r in rows.values())
    usable = len(rows) >= SUR and matched >= UTILISABLE
    out.update({"reserve": reserve, "report_only": report_only, "rows": rows, "matched": matched,
                "usable": usable,
                "verdict": ("utilisable : la porte se relit sur la moitié de choix contre ce comparateur, par un amendement daté"
                            if usable else
                            f"voie 1 : {matched} effacements appariés sur {len(rows)}, il en faut {UTILISABLE} sur {SUR}")})
    return out


if __name__ == "__main__":
    res = json.loads((Path(sys.argv[1]) / "results.json").read_text(encoding="utf8"))
    print(json.dumps(lire(res, *(sys.argv[2:3] or [])), ensure_ascii=False, indent=1))
