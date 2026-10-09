"""Le rang minimal par effacement itéré (texte déposé, annexe C.7), sur des états synthétiques où un concept est planté à
un rang connu : la procédure retrouve-t-elle ce rang ? Exploratoire, sans modèle ni machine.

    python analyses/rang_plante.py <fichier JSON de sortie> [répliques]

**Ce que dit l'annexe C.7.** À une couche, chaque nouvelle direction s'ajuste en forme close sur les états déjà effacés
par les précédentes, sur un nouveau lot de paires (après un effacement, rien ne sépare plus linéairement les deux côtés
des paires qui l'ont ajusté). Le rang minimal est le plus petit nombre de directions qui ramène le transfert au hasard :
en moyenne sur les couches, max(AUROC, 1 − AUROC) ≤ 0,55, pour la sonde linéaire et pour le perceptron. La sonde
s'entraîne sur d'autres paires que celles de l'ajustement, et se lit sur des paires de familles tenues à part. Le cas
connu est un concept planté dans un sous-espace de rang connu, dont la direction change d'un groupe de contextes à
l'autre dans ce sous-espace. **Le texte ne dit pas comment se forment les lots de paires.**

**La question, écrite avant le premier calcul (9 octobre 2026, 1 h UTC)** : selon la façon de former les lots, la
procédure retrouve-t-elle le rang planté ?
- des lots tirés au hasard parmi les paires d'ajustement, chacun mêlant les groupes ;
- un lot par groupe de contextes.

**Ce que j'attends.** Avec des lots mêlés, la première direction retire la différence moyenne des classes ; les lots
suivants, tirés de la même loi, n'ont presque plus de différence de moyennes, et leurs directions viennent surtout du
bruit d'échantillonnage. Le transfert vers les groupes tenus à part reste alors au-dessus du hasard, et le rang planté
n'est pas retrouvé (ou seulement par hasard, plus loin). Avec un lot par groupe, chaque direction retire celle d'un
groupe, et le rang planté est retrouvé.

**Le critère** : le rang trouvé (le premier rang, de 1 à 8, où la sonde linéaire et le perceptron sont au hasard sur les
groupes tenus à part) égale le rang planté dans au moins 9 répliques sur 10.

**Une seconde lecture, écrite après la première série et avant son propre calcul (9 octobre 2026, 1 h 35 UTC).** La
première série ne passe pas son critère : avec des lots mêlés, le rang trouvé est presque toujours 1 ; avec un lot par
groupe, de 1 à 6. Le transfert vers des groupes tenus à part ne lit que la part du concept commune aux groupes. La
seconde lecture garde l'ajustement et change la lecture : sur chaque groupe tenu à part, une sonde linéaire et un
perceptron s'entraînent sur la moitié de ses paires et se lisent sur l'autre moitié (le décodage au sein du groupe),
en moyenne sur les quatre groupes, avec le même seuil de 0,55. Ce que j'attends : avec un lot par groupe, le rang
planté est retrouvé (au moins 9 répliques sur 10, le même critère) ; avec des lots mêlés, non. Elle se lance par
`python analyses/rang_plante.py <sortie> 10 intra`.

**Une troisième lecture, écrite après la seconde série et avant son propre calcul (9 octobre 2026, 1 h 45 UTC).** La
seconde série ne passe pas non plus : au sein des groupes, avec un lot par groupe, le rang est surestimé (de 3 à 8 pour
un rang planté de 2 à 4). Le seuil fixe de 0,55 est proche du niveau d'une sonde sans signal à ces tailles : la lecture
symétrique d'une sonde au hasard vaut déjà environ 0,53. La troisième lecture garde un lot par groupe et prend, à
chaque rang, le seuil que l'annexe C.7 donne à sa précondition : le 95ᵉ centile de 20 sondes entraînées sur des
étiquettes permutées, sur les mêmes états effacés. « Au hasard » veut dire : pas au-dessus de ce centile, pour la sonde
linéaire et pour le perceptron. Elle se lit des deux façons, par transfert et au sein des groupes. Ce que j'attends : au
sein des groupes, le rang planté est retrouvé (au moins 9 répliques sur 10) ; par transfert, il reste sous-estimé dès
le rang 3. Elle se lance par `python analyses/rang_plante.py <sortie> 10 <transfer|intra> permutation`.

**Une quatrième piste, écrite après la troisième série et avant son propre calcul (9 octobre 2026, 1 h 50 UTC).** Aucune
lecture de l'effacement itéré ne passe le critère : le transfert sous un seuil calibré trouve des rangs épars (1 à 2
répliques sur 10), le décodage au sein des groupes n'est presque jamais au hasard. La quatrième piste n'itère plus : elle
ajuste les six groupes d'ajustement ensemble, comme le module d'effacement le fait déjà avec une colonne d'étiquettes par
jeu. Pour chaque groupe, la différence moyenne des deux côtés de ses paires (200 paires), blanchie par la covariance
intra-classe de tous les états d'ajustement ; le rang estimé est le nombre de valeurs singulières de la matrice de ces
six différences qui dépassent chacune le 95ᵉ centile de la même valeur singulière sous 50 permutations de signe (les deux
côtés de chaque paire échangés au hasard). Ce que j'attends : le rang planté est retrouvé dans au moins 9 répliques sur
10, pour les rangs 2, 3 et 4. Elle se lance par `python analyses/rang_plante.py <sortie> 10 spectral`.

**Une cinquième piste, la dernière de cette série, écrite après la quatrième et avant son propre calcul (9 octobre 2026,
1 h 55 UTC).** La quatrième surestime : elle compare la j-ième valeur singulière observée à la j-ième d'un bruit pur,
alors qu'au-delà du rang planté la valeur observée est la plus grande du bruit résiduel. Les rangs d'ordre ne
s'alignent pas : c'est une erreur de construction du test, connue. La cinquième est le test séquentiel standard. À
l'étape j, on retire les j − 1 premières directions singulières observées ; on compare la plus grande valeur singulière
restante au 95ᵉ centile de la même quantité sous les 50 permutations de signe, privées des mêmes directions ; on s'arrête
au premier échec. Ce que j'attends : le rang planté est retrouvé dans au moins 9 répliques sur 10, pour les rangs 2, 3 et
4. Elle se lance par `python analyses/rang_plante.py <sortie> 10 sequential`.

**La robustesse du test séquentiel, écrite après sa première série et avant son propre calcul (9 octobre 2026,
2 h UTC).** La cinquième piste passe son critère sur un seul monde. La confirmation varie ce monde : l'effet (1,2, comme
avant, et 0,6), le nombre de paires par groupe (200 et 100), le rang planté (de 0 à 5 ; au rang 0, aucun concept, et
l'estimateur doit rendre 0). Six groupes d'ajustement, donc au plus six directions visibles. Ce que j'attends : à l'effet
de 1,2, le rang planté est retrouvé dans au moins 9 répliques sur 10 pour tous les rangs et les deux tailles ; à l'effet
de 0,6 et 100 paires, il peut être sous-estimé aux rangs 4 et 5, faute de puissance. Le critère, pour qu'on puisse s'en
servir : au moins 9 sur 10 à l'effet de 1,2, et jamais de surestimation au-delà d'une réplique sur 10 nulle part. Elle se
lance par `python analyses/rang_plante.py <sortie> 10 robustesse`.

**Le modèle des états** (une couche) : largeur 64 ; un sous-espace de rang k (2, 3 ou 4) ; 10 groupes de contextes, chacun
avec sa direction du concept dans ce sous-espace et son décalage moyen ; les deux côtés d'une paire partagent leur
scénario (un bruit commun de covariance anisotrope) et diffèrent par le concept et un petit bruit propre. Les groupes 1 à
6 servent à l'ajustement et à l'entraînement de la sonde, sur des paires disjointes ; les groupes 7 à 10 sont tenus à
part, pour la lecture.

**Une correction, après le premier essai (une réplique, k = 2, avant toute série).** Les directions des groupes étaient
tirées au hasard dans le sous-espace, sans part commune : sans aucun effacement, le transfert vers les groupes tenus à
part était déjà au hasard (0,50 et 0,51). La précondition de l'annexe C.7 échouait, et le rang n'y est pas défini. La
direction d'un groupe est désormais une part commune à tous les groupes plus une part propre au groupe, de même norme,
toutes deux dans le sous-espace : le concept transfère, et sa direction change d'un groupe à l'autre, comme le demande le
cas connu. Les lots sont aussi plus grands (200 paires), pour que l'ajustement en largeur 64 soit stable. La question,
l'attente et le critère ne changent pas ; la précondition est maintenant rapportée.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

WIDTH, GROUPS, FIT_GROUPS, MAX_RANK, CHANCE = 64, 10, 6, 8, 0.55


def world(rng, k, width=WIDTH, groups=GROUPS, own_share=1.0):
    """Le sous-espace du concept, la direction de chaque groupe (une part commune plus une part propre, de même norme,
    dans le sous-espace), son décalage, et le facteur du bruit commun. Au rang 0, aucun concept : des directions nulles."""
    if k == 0:
        return {"basis": np.zeros((width, 0)), "dirs": np.zeros((groups, width)),
                "offsets": rng.normal(scale=0.7, size=(groups, width)),
                "mix": rng.normal(size=(width, width)) * np.linspace(0.3, 1.5, width)[None, :] / np.sqrt(width)}
    u = np.linalg.qr(rng.normal(size=(width, k)))[0]
    common = rng.normal(size=k)
    common /= np.linalg.norm(common)
    own = rng.normal(size=(groups, k))
    own /= np.linalg.norm(own, axis=1, keepdims=True)
    a = common[None, :] + own_share * own
    dirs = np.stack([u @ (x / np.linalg.norm(x)) for x in a])
    offsets = rng.normal(scale=0.7, size=(groups, width))
    mix = rng.normal(size=(width, width)) * np.linspace(0.3, 1.5, width)[None, :]
    return {"basis": u, "dirs": dirs, "offsets": offsets, "mix": mix / np.sqrt(width)}


def pairs(rng, w, group, n, effect=1.2, own_noise=0.25):
    """n paires d'un groupe : (états [2n, largeur], étiquettes [2n] en ±1)."""
    shared = rng.normal(size=(n, WIDTH)) @ w["mix"].T + w["offsets"][group]
    x_eval = shared + effect / 2 * w["dirs"][group] + own_noise * rng.normal(size=(n, WIDTH))
    x_dep = shared - effect / 2 * w["dirs"][group] + own_noise * rng.normal(size=(n, WIDTH))
    return np.concatenate([x_eval, x_dep]), np.concatenate([np.ones(n), -np.ones(n)])


def erase_all(params, x):
    """Les effacements dans l'ordre de leur ajustement."""
    import torch  # noqa: WPS433
    from rrexp.jobs.erasure import apply  # noqa: WPS433
    t = torch.as_tensor(x, dtype=torch.float32)
    for p in params:
        t = apply(p, t)
    return t.numpy()


def _symmetric(a):
    return max(a, 1 - a)


def null_within(parts, params, mlp_steps, rng, n_perm=20):
    """Le 95ᵉ centile de la lecture au sein des groupes, sous des étiquettes permutées (dans la moitié d'entraînement)."""
    out = {"linear": [], "mlp": []}
    for _ in range(n_perm):
        shuffled = []
        for x, y in parts:
            n = len(y) // 2
            half = n // 2
            yy = y.copy()
            tr = np.r_[0:half, n:n + half]
            yy[tr] = rng.permutation(yy[tr])
            shuffled.append((x, yy))
        r = within_groups(shuffled, params, mlp_steps, permuted=True)
        out["linear"].append(r["linear"])
        out["mlp"].append(r["mlp"])
    return {k: float(np.percentile(v, 95)) for k, v in out.items()}


def null_transfer(xp, yp, xr, yr, params, mlp_steps, rng, n_perm=20):
    """Le 95ᵉ centile du transfert, sous des étiquettes permutées à l'entraînement."""
    import torch  # noqa: WPS433
    from rrexp.jobs.manipulation import transfer  # noqa: WPS433
    src = torch.as_tensor(erase_all(params, xp))[:, None, :]
    tgt = torch.as_tensor(erase_all(params, xr))[:, None, :]
    out = {"linear": [], "mlp": []}
    for _ in range(n_perm):
        t = transfer(src, rng.permutation((yp > 0).astype(int)).tolist(), tgt, (yr > 0).astype(int).tolist(), mlp_steps=mlp_steps)[0]
        out["linear"].append(_symmetric(t["linear"]))
        out["mlp"].append(_symmetric(t["mlp"]))
    return {k: float(np.percentile(v, 95)) for k, v in out.items()}


def within_groups(parts, params, mlp_steps, permuted=False):
    """Le décodage au sein de chaque groupe : les sondes entraînées sur une moitié des paires du groupe, lues sur
    l'autre ; la lecture symétrique, en moyenne sur les groupes."""
    import torch  # noqa: WPS433
    from rrexp.jobs.extract_eval import auroc, logistic_probe  # noqa: WPS433
    from rrexp.jobs.manipulation import mlp_probe  # noqa: WPS433
    lin, mlp = [], []
    for x, y in parts:
        n = len(y) // 2                                       # les n premiers : un côté, puis l'autre (voir pairs)
        half = n // 2
        tr = np.r_[0:half, n:n + half]
        te = np.r_[half:n, n + half:2 * n]
        xe = torch.as_tensor(erase_all(params, x))
        yl = (y > 0).astype(int)                              # permuted : la moitié d'entraînement est déjà mélangée
        f = logistic_probe(xe[tr], yl[tr].tolist())
        g = mlp_probe(xe[tr], yl[tr].tolist(), steps=mlp_steps)
        a1, a2 = auroc(f(xe[te]), yl[te].tolist()), auroc(g(xe[te]), yl[te].tolist())
        lin.append(max(a1, 1 - a1))
        mlp.append(max(a2, 1 - a2))
    return {"linear": round(float(np.mean(lin)), 4), "mlp": round(float(np.mean(mlp)), 4)}


def one_replicate(seed, k, scheme, n_fit=200, n_probe=240, n_read=240, mlp_steps=150, reading="transfer", threshold="fixed"):
    """Le rang trouvé, et la lecture à chaque rang (0 : sans effacement) : le transfert vers les groupes tenus à part
    (« transfer », la lecture de l'annexe C.7), ou le décodage au sein de chacun d'eux (« intra »)."""
    import torch  # noqa: WPS433
    from rrexp.jobs.erasure import fit_leace  # noqa: WPS433
    from rrexp.jobs.manipulation import transfer  # noqa: WPS433
    rng = np.random.default_rng(seed)
    w = world(rng, k)
    # les lots d'ajustement : un par groupe (cycliquement), ou chacun tiré au hasard parmi les six groupes
    batches = []
    for r in range(MAX_RANK):
        if scheme == "un lot par groupe":
            batches.append(pairs(rng, w, r % FIT_GROUPS, n_fit))
        else:
            parts = [pairs(rng, w, g, max(1, n_fit // FIT_GROUPS)) for g in range(FIT_GROUPS)]
            batches.append((np.concatenate([p[0] for p in parts]), np.concatenate([p[1] for p in parts])))
    probe_parts = [pairs(rng, w, g, n_probe // FIT_GROUPS + 1) for g in range(FIT_GROUPS)]
    per_group = n_read // (GROUPS - FIT_GROUPS) + 1 if reading == "transfer" else 200
    read_parts = [pairs(rng, w, g, per_group) for g in range(FIT_GROUPS, GROUPS)]
    xp, yp = np.concatenate([p[0] for p in probe_parts]), np.concatenate([p[1] for p in probe_parts])
    xr, yr = np.concatenate([p[0] for p in read_parts]), np.concatenate([p[1] for p in read_parts])
    params, readings, found = [], [], None
    for r in range(MAX_RANK + 1):
        if r > 0:
            xb, yb = batches[r - 1]
            params.append(fit_leace(torch.as_tensor(erase_all(params, xb)), yb))
        if reading == "transfer":
            src = torch.as_tensor(erase_all(params, xp))[:, None, :]
            tgt = torch.as_tensor(erase_all(params, xr))[:, None, :]
            t = transfer(src, (yp > 0).astype(int).tolist(), tgt, (yr > 0).astype(int).tolist(), mlp_steps=mlp_steps)[0]
            sym = {name: round(max(v, 1 - v), 4) for name, v in t.items()}
        else:
            sym = within_groups(read_parts, params, mlp_steps)
        readings.append({"rank": r, **sym})
        if threshold == "permutation":
            prng = np.random.default_rng(seed * 100 + r)
            null = (null_transfer(xp, yp, xr, yr, params, mlp_steps, prng) if reading == "transfer"
                    else null_within(read_parts, params, mlp_steps, prng))
            readings[-1]["null95"] = {key: round(v, 4) for key, v in null.items()}
            at_chance = all(sym[key] <= null[key] for key in ("linear", "mlp"))
        else:
            at_chance = all(v <= CHANCE for v in sym.values())
        if r > 0 and found is None and at_chance:
            found = r
    # la part du sous-espace planté que les directions retirées couvrent
    removed = np.stack([p["B"].numpy()[:, 0] for p in params])
    q = np.linalg.qr(removed.T)[0]
    covered = float(np.linalg.norm(q.T @ w["basis"]) ** 2 / k)
    pre = readings[0]
    return {"found": found, "readings": readings, "planted_covered_by_8": round(covered, 4),
            "precondition": bool(all(pre[name] > CHANCE for name in ("linear", "mlp")))}


def spectral_rank(seed, k, n_fit=200, n_flip=50, sequential=False, effect=1.2):
    """Le rang estimé par le spectre des différences moyennes des groupes d'ajustement, blanchies, contre des
    permutations de signe des paires."""
    rng = np.random.default_rng(seed)
    w = world(rng, k)
    groups = [pairs(rng, w, g, n_fit, effect=effect) for g in range(FIT_GROUPS)]
    xs = np.concatenate([x for x, _ in groups])
    ys = np.concatenate([y for _, y in groups])
    # la covariance intra-classe de tous les états d'ajustement, et son inverse en racine carrée
    xc = np.concatenate([xs[ys > 0] - xs[ys > 0].mean(0), xs[ys < 0] - xs[ys < 0].mean(0)])
    vals, vecs = np.linalg.eigh(xc.T @ xc / len(xc))
    whiten = vecs @ np.diag(1 / np.sqrt(np.maximum(vals, 1e-9))) @ vecs.T

    def matrix(signs=None):
        cols = []
        for i, (x, _) in enumerate(groups):
            n = len(x) // 2
            d = x[:n] - x[n:]                                  # les différences des paires, côté évaluation moins déploiement
            if signs is not None:
                d = d * signs[i][:, None]
            cols.append(whiten @ d.mean(0))
        return np.stack(cols, axis=1)

    def spectrum(signs=None):
        return np.linalg.svd(matrix(signs), compute_uv=False)

    s_obs = spectrum()
    flips = [[rng.choice([-1.0, 1.0], size=len(x) // 2) for x, _ in groups] for _ in range(n_flip)]
    null = np.stack([spectrum(f) for f in flips])
    q95 = np.percentile(null, 95, axis=0)
    if sequential:
        d_obs = matrix()
        u_obs = np.linalg.svd(d_obs, full_matrices=False)[0]
        d_null = [matrix(f) for f in flips]
        rank = 0
        for j in range(d_obs.shape[1]):
            proj = np.eye(d_obs.shape[0]) - u_obs[:, :j] @ u_obs[:, :j].T          # sans les j directions retenues
            top = np.linalg.norm(proj @ d_obs, 2)
            top_null = [np.linalg.norm(proj @ dn, 2) for dn in d_null]
            if top > np.percentile(top_null, 95):
                rank = j + 1
            else:
                break
    else:
        above = s_obs > q95
        rank = int(np.argmin(above)) if not above.all() else len(above)    # les premières valeurs, tant qu'elles dépassent
    # la part du sous-espace planté couverte par les r premières directions singulières, ramenées dans l'espace d'origine
    u = np.linalg.svd(np.stack([whiten @ (x[:len(x) // 2] - x[len(x) // 2:]).mean(0) for x, _ in groups], axis=1),
                      full_matrices=False)[0][:, :max(rank, 1)]
    q = np.linalg.qr(np.linalg.inv(whiten) @ u)[0]
    covered = float(np.linalg.norm(q.T @ w["basis"]) ** 2 / k) if k else None
    return {"found": rank, "singular_values": [round(float(v), 4) for v in s_obs], "null95": [round(float(v), 4) for v in q95],
            "planted_covered": round(covered, 4)}


def main_spectral(dest, reps=10, sequential=False):
    out = {"reps": reps, "method": "spectre des différences moyennes des groupes, blanchies, contre 50 permutations de signe"
                                   + (", test séquentiel" if sequential else ", valeur par valeur"), "rows": []}
    for k in (2, 3, 4):
        runs = [spectral_rank(1000 * k + i, k, sequential=sequential) for i in range(reps)]
        row = {"planted": k, "found": [r["found"] for r in runs], "recovered": sum(r["found"] == k for r in runs),
               "planted_covered": round(float(np.mean([r["planted_covered"] for r in runs])), 4),
               "example": runs[0]}
        out["rows"].append(row)
        print(json.dumps({x: row[x] for x in ("planted", "found", "recovered", "planted_covered")}, ensure_ascii=False), flush=True)
    Path(dest).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf8")


def main_robustesse(dest, reps=10):
    out = {"reps": reps, "method": "test séquentiel sur le spectre, 50 permutations de signe", "rows": []}
    for effect in (1.2, 0.6):
        for n_fit in (200, 100):
            for k in range(6):
                found = [spectral_rank(5000 + 100 * k + i, k, n_fit=n_fit, sequential=True, effect=effect)["found"]
                         for i in range(reps)]
                row = {"effect": effect, "pairs_per_group": n_fit, "planted": k, "found": found,
                       "recovered": sum(f == k for f in found), "over": sum(f > k for f in found),
                       "under": sum(f < k for f in found)}
                out["rows"].append(row)
                print(json.dumps(row, ensure_ascii=False), flush=True)
    Path(dest).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf8")


def _task(args):
    import torch  # noqa: WPS433
    torch.set_num_threads(1)          # quatre processus sur quatre cœurs : un fil chacun (de petites matrices)
    seed, k, scheme, reading, threshold = args
    return one_replicate(seed, k, scheme, reading=reading, threshold=threshold)


def main(dest, reps=10, reading="transfer", threshold="fixed", workers=4):
    from multiprocessing import Pool
    out = {"reps": reps, "chance": CHANCE if threshold == "fixed" else "95e centile de 20 permutations", "max_rank": MAX_RANK,
           "reading": reading, "threshold": threshold, "rows": []}
    schemes = ("lots mêlés", "un lot par groupe") if threshold == "fixed" else ("un lot par groupe",)
    cases = [(k, scheme) for k in (2, 3, 4) for scheme in schemes]
    with Pool(workers) as pool:
        done = pool.map(_task, [(1000 * k + i, k, scheme, reading, threshold) for k, scheme in cases for i in range(reps)])
    for c, (k, scheme) in enumerate(cases):
        runs = done[c * reps:(c + 1) * reps]
        row = {"planted": k, "scheme": scheme, "found": [r["found"] for r in runs],
               "recovered": sum(r["found"] == k for r in runs), "precondition": sum(r["precondition"] for r in runs),
               "transfer_by_rank": [{"rank": j, "linear": round(float(np.mean([r["readings"][j]["linear"] for r in runs])), 4),
                                     "mlp": round(float(np.mean([r["readings"][j]["mlp"] for r in runs])), 4)}
                                    for j in range(MAX_RANK + 1)],
               "planted_covered_by_8": round(float(np.mean([r["planted_covered_by_8"] for r in runs])), 4)}
        out["rows"].append(row)
        print(json.dumps({x: row[x] for x in ("planted", "scheme", "found", "recovered", "precondition")}, ensure_ascii=False),
              flush=True)
    Path(dest).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[3] == "robustesse":
        main_robustesse(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) > 3 and sys.argv[3] in ("spectral", "sequential"):
        main_spectral(sys.argv[1], int(sys.argv[2]), sequential=sys.argv[3] == "sequential")
    else:
        main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 10, sys.argv[3] if len(sys.argv) > 3 else "transfer",
             sys.argv[4] if len(sys.argv) > 4 else "fixed")
