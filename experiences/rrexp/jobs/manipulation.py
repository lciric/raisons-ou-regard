"""The manipulation check (programme v1.5, part 3): does an intervention remove "I am being evaluated" from what the model
computes, and does it remove it more than the comparator does?

- **The state read.** The residual stream after each layer, read as the input of the next layer by a forward pre-hook,
  and after the last layer as the input of the final norm. That is the state the rest of the model sees under the
  intervention (see the caution of inhibition_degradation.Projector: the hidden states that transformers returns can
  be recorded before the projection).
- **Two readouts**: the last prompt token, where the extraction reads; and the mean over the prompt's positions.
- **Probes retrained under each condition.** A probe learned without intervention shares the inhibition's blind spot: a
  representation turned elsewhere would escape both. Per layer and readout, a logistic probe and a small perceptron
  are trained on half the pairs of a held-out cue set, and tested on the other half (the split is by pair, so the two
  sides of a pair stay together). The AUROC on the tested half is the decodability.
- **The residual projection**: the mean norm of the state's component in the first r directions of "I am being
  evaluated", at the last token.
- **The known case, a constructed failure**: an inhibition at one layer only. The decodability must fall at that layer
  and come back downstream; a check that did not see it come back would see nothing.

The criterion (comparative, fixed in advance in the programme): the residual decodability under the inhibition is
lower than under the comparator; an absolute threshold holds only at the layers where one projects.
"""
import hashlib


def split_pairs(pair_ids, seed=0):
    """Half the pairs for training, half for testing, by a hash of the pair id (stable, independent of order)."""
    def h(p):
        return hashlib.sha256(f"{seed}:{p}".encode()).hexdigest()
    ids = sorted(set(pair_ids), key=h)
    return set(ids[: len(ids) // 2]), set(ids[len(ids) // 2:])


def read_states(model, tok, conversations, batch, device):
    """The states after each layer, as the next one sees them: ([n, layers, width] at the last prompt token,
    [n, layers, width] averaged over the prompt positions), in float32 on the CPU."""
    import torch  # noqa: WPS433
    layers = model.model.layers
    n_layers = len(layers)
    grabbed = {}

    def grab(idx):
        def pre(module, args, kwargs):
            grabbed[idx] = (args[0] if args else kwargs["hidden_states"]).detach()
        return pre

    handles = [layers[i].register_forward_pre_hook(grab(i), with_kwargs=True) for i in range(1, n_layers)]
    handles.append(model.model.norm.register_forward_pre_hook(grab(n_layers), with_kwargs=True))
    tok.padding_side = "left"
    last, mean = [], []
    try:
        for i in range(0, len(conversations), batch):
            enc = tok.apply_chat_template(conversations[i:i + batch], add_generation_prompt=True, return_tensors="pt", padding=True,
                                          return_dict=True).to(device)
            grabbed.clear()
            with torch.no_grad():
                model(**enc)
            m = enc["attention_mask"].float()
            for_layers_last, for_layers_mean = [], []
            for j in range(1, n_layers + 1):
                x = grabbed[j].float()
                for_layers_last.append(x[:, -1, :])
                for_layers_mean.append((x * m[:, :, None]).sum(1) / m.sum(1, keepdim=True))
            last.append(torch.stack(for_layers_last, dim=1).cpu())
            mean.append(torch.stack(for_layers_mean, dim=1).cpu())
    finally:
        for h in handles:
            h.remove()
    return torch.cat(last), torch.cat(mean)


def mlp_probe(x_train, y_train, hidden=64, steps=300, lr=1e-3, weight_decay=1e-2, seed=0):
    """A small perceptron (one hidden layer) on standardized features, by Adam on the full batch. Returns a scorer."""
    import torch  # noqa: WPS433
    torch.manual_seed(seed)
    mu, sd = x_train.mean(0), x_train.std(0).clamp_min(1e-6)
    x = (x_train - mu) / sd
    y = torch.as_tensor(y_train, dtype=torch.float32)
    net = torch.nn.Sequential(torch.nn.Linear(x.shape[1], hidden), torch.nn.ReLU(), torch.nn.Linear(hidden, 1))
    opt = torch.optim.Adam(net.parameters(), lr=lr, weight_decay=weight_decay)
    for _ in range(steps):
        opt.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(net(x)[:, 0], y)
        loss.backward()
        opt.step()
    net.eval()

    def score(z):
        with torch.no_grad():
            return net((z - mu) / sd)[:, 0]
    return score


def decodability(states, labels, pair_ids, train, test, mlp_steps=300):
    """Per layer: the test AUROC of a logistic probe and of a perceptron, both trained on the training pairs."""
    import torch  # noqa: WPS433
    from .extract_eval import auroc, logistic_probe  # noqa: WPS433
    tr = torch.tensor([p in train for p in pair_ids])
    te = torch.tensor([p in test for p in pair_ids])
    y = torch.as_tensor(labels)
    out = []
    for l in range(states.shape[1]):
        x = states[:, l, :]
        lin = logistic_probe(x[tr], y[tr].tolist())
        mlp = mlp_probe(x[tr], y[tr].tolist(), steps=mlp_steps)
        out.append({"linear": round(auroc(lin(x[te]), y[te].tolist()), 4), "mlp": round(auroc(mlp(x[te]), y[te].tolist()), 4)})
    return out


def residual_projection(states_last, subspace, rank):
    """Per layer: the mean norm of the component of the last-token state in the first `rank` directions."""
    out = []
    for l in range(states_last.shape[1]):
        b = subspace[f"layer_{l + 1:02d}.basis"][:rank].float()
        out.append(round(float((states_last[:, l, :] @ b.T).norm(dim=-1).mean()), 4))
    return out


def check(model, tok, pairs, conditions, subspace, rank, batch, device, seed=0, mlp_steps=300, progress=None):
    """pairs: [(pair_id, eval_messages, deploy_messages)] of a held-out cue set. conditions: {name: a context manager
    factory (an intervention), or None}. Returns {name: {"layers": [...], "summary": {...}}}."""
    import contextlib  # noqa: WPS433
    convs = [p[1] for p in pairs] + [p[2] for p in pairs]
    labels = [1] * len(pairs) + [0] * len(pairs)
    pids = [p[0] for p in pairs] * 2
    train, test = split_pairs([p[0] for p in pairs], seed)
    out = {}
    for name, make in conditions.items():
        if progress:
            progress(f"manipulation check: {name}")
        with (make() if make else contextlib.nullcontext()):
            last, mean = read_states(model, tok, convs, batch, device)
        dl, dm = decodability(last, labels, pids, train, test, mlp_steps), decodability(mean, labels, pids, train, test, mlp_steps)
        res = residual_projection(last, subspace, rank)
        layers = [{"layer": l + 1, "linear_last": dl[l]["linear"], "mlp_last": dl[l]["mlp"], "linear_mean": dm[l]["linear"],
                   "mlp_mean": dm[l]["mlp"], "residual_projection": res[l]} for l in range(len(dl))]
        best = [max(x["linear_last"], x["mlp_last"], x["linear_mean"], x["mlp_mean"]) for x in layers]
        out[name] = {"layers": layers, "summary": {"best_auroc_mean_over_layers": round(sum(best) / len(best), 4),
                                                   "best_auroc_max_over_layers": round(max(best), 4)}}
    return out
