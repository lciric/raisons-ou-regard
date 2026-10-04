"""The linear erasure of "I am being evaluated" in closed form (LEACE: Belrose, Schneider-Joseph, Ravfogel, Cotterell,
Raff and Biderman, "LEACE: Perfect linear concept erasure in closed form", NeurIPS 2023).

**What it guarantees, and what not.** Fitted on states X and labels Z, the eraser r(x) = x - W⁺ P W (x - μ) makes the
cross-covariance of r(X) with Z zero on the fitting data, which is equivalent to linear guardedness there: no linear
classifier predicts Z from r(X) better than a constant (the paper's theorem). W whitens X (Σ_XX^{-1/2}, on the span of
the data), P projects onto the span of W Σ_XZ, and among the erasers with that property it changes the states the
least, in the whitened norm. It guarantees nothing for a nonlinear probe, nor for states of other prompts: a held-out
cue set is guarded only as far as its contrast shares the fitted directions. Hence the manipulation check, which
retrains a perceptron as well as a linear probe, on held-out cues.

**How many directions.** A binary label (evaluation against deployment, coded ±1) has a cross-covariance of rank one:
the eraser removes one direction per layer, the one that equalizes the two class means, chosen obliquely (in the
whitened geometry) rather than orthogonally. Several label columns remove several directions: with one column per cue
set (±1 within the set, 0 elsewhere), the eraser removes the span of the sets' own contrasts, one direction per set.

**Where.** As the Projector of inhibition_degradation: forward hooks on the output of chosen decoder layers, at every
position, with a fraction that scales the correction (1: the full erasure; less: for the matching on the KL). Fitted on
the state each layer hands to the next (manipulation.read_states), at the last prompt token by default.

**Sequentially.** Erasing at one layer changes the states of the layers above it. fit_layers fits the layers in
order, each on the states read with the erasers already fitted below it in place (the paper's "concept scrubbing");
independent fits, all on the clean states, are the cheaper option.

The fit works in the span of the data (an SVD of the centered states), never forming a width x width matrix.
"""


def fit_leace(x, z, rel_tol=1e-6):
    """x: [n, width] states; z: [n] or [n, m] label columns. Returns {"mean": [width], "B": [width, k], "C": [width, k]}
    in float32 on the CPU, with the eraser r(x) = x - B Cᵀ (x - mean) (B = W⁺ Q, C = W Q, Q an orthonormal basis of the
    span of W Σ_XZ). k is the rank of the cross-covariance (at most m)."""
    import torch  # noqa: WPS433
    x = x.double().cpu()
    z = torch.as_tensor(z, dtype=torch.float64)
    if z.dim() == 1:
        z = z[:, None]
    n = x.shape[0]
    if z.shape[0] != n:
        raise ValueError("as many labels as states")
    mu = x.mean(0)
    xc = x - mu
    zc = z - z.mean(0)
    u, s, vh = torch.linalg.svd(xc, full_matrices=False)          # xc = U S Vᵀ
    keep = s > rel_tol * s.max()
    u, s, v = u[:, keep], s[keep], vh[keep].T                      # the span of the data
    # W = V diag(√n / S) Vᵀ, W⁺ = V diag(S / √n) Vᵀ, and W Σ_XZ = V (Uᵀ zc) / √n
    a = u.T @ zc                                                   # [r, m]
    qa, sa, _ = torch.linalg.svd(a, full_matrices=False)
    qa = qa[:, sa > rel_tol * max(float(sa.max()), 1e-300)]        # Q' : an orthonormal basis of the span of Uᵀ zc
    d = n ** 0.5 / s
    b = v @ (qa / d[:, None])                                      # W⁺ Q = V D⁻¹ Q'
    c = v @ (qa * d[:, None])                                      # W Q = V D Q'
    return {"mean": mu.float(), "B": b.float().contiguous(), "C": c.float().contiguous()}


def apply(params, x, fraction=1.0):
    """The erased states, outside the model (for the tests and the readings)."""
    mu, b, c = (params[k].to(device=x.device, dtype=x.dtype) for k in ("mean", "B", "C"))
    return x - fraction * ((x - mu) @ c) @ b.T


def cross_covariance(x, z):
    """Σ_XZ of states and label columns: zero after a full erasure, on the fitting data."""
    import torch  # noqa: WPS433
    x = x.double()
    z = torch.as_tensor(z, dtype=torch.float64, device=x.device)
    if z.dim() == 1:
        z = z[:, None]
    return (x - x.mean(0)).T @ (z - z.mean(0)) / x.shape[0]


def polarity_columns(set_names):
    """Label columns from a list of (set name, polarity) per state: one column per set, +1 for its evaluation side,
    -1 for its deployment side, 0 for the states of the other sets. With one set, the plain binary label."""
    sets = sorted({s for s, _ in set_names})
    return [[(1.0 if p == "eval" else -1.0) if s == name else 0.0 for name in sets] for s, p in set_names], sets


class Eraser:
    """Forward hooks that apply fraction * the LEACE correction to the output of chosen decoder layers, at every
    position. params: {layer (1-based): fit_leace's dict}. Like the Projector, it accumulates the mean norm of the
    removed component over the positions where `mask` (set before each forward) is true."""

    def __init__(self, model, params, fraction=1.0):
        self.model, self.fraction, self.handles, self.mask = model, float(fraction), [], None
        self.params = dict(params)
        self.removed = {l: [0.0, 0] for l in params}

    def _hook(self, layer):
        p = self.params[layer]

        def hook(module, args, output):
            h = output[0] if isinstance(output, tuple) else output
            mu, b, c = (p[k].to(device=h.device, dtype=h.dtype) for k in ("mean", "B", "C"))
            comp = ((h - mu) @ c) @ b.T
            if self.mask is not None:
                nrm = comp.float().norm(dim=-1)[self.mask]
                self.removed[layer][0] += float(nrm.sum()) * self.fraction
                self.removed[layer][1] += int(nrm.numel())
            h = h - self.fraction * comp
            return (h,) + tuple(output[1:]) if isinstance(output, tuple) else h
        return hook

    def __enter__(self):
        layers = self.model.model.layers
        for l in self.params:
            self.handles.append(layers[l - 1].register_forward_hook(self._hook(l)))
        return self

    def __exit__(self, *exc):
        for h in self.handles:
            h.remove()
        self.handles = []

    def mean_removed(self):
        return {l: (s / n if n else 0.0) for l, (s, n) in self.removed.items()}


def fit_layers(model, tok, conversations, labels, layers, batch, device, sequential=True, readout="last", progress=None):
    """The erasers of the chosen layers (1-based), fitted on the states that each layer hands to the next, for the
    given conversations and label columns. Sequential: each layer on the states read with the erasers below it in
    place. Returns {layer: params}."""
    from .manipulation import read_states  # noqa: WPS433
    idx = 0 if readout == "last" else 1
    params = {}
    order = sorted(int(l) for l in layers)
    if not sequential:
        states = read_states(model, tok, conversations, batch, device)[idx]
        return {l: fit_leace(states[:, l - 1, :], labels) for l in order}
    for i, l in enumerate(order):
        if progress:
            progress(f"erasure fit: layer {l} ({i + 1}/{len(order)})")
        with Eraser(model, params, 1.0):
            states = read_states(model, tok, conversations, batch, device)[idx]
        params[l] = fit_leace(states[:, l - 1, :], labels)
    return params
