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
- **The transfer** (optional): probes trained on another cue set (the extraction pairs kept out of the expert iteration
  and of the erasure's fit), under the same condition, and read on the held-out set. The two sets are written with
  other words (decision 24): a probe trained and tested on one set can read its words, which no removal of a few
  directions erases; a probe that carries over reads what the sets share.
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
    """A small perceptron (one hidden layer) on standardized features, by Adam on the full batch, on the device of
    x_train (initialized on the CPU, so that the seed gives the same start on any device). Returns a scorer."""
    import torch  # noqa: WPS433
    torch.manual_seed(seed)
    mu, sd = x_train.mean(0), x_train.std(0).clamp_min(1e-6)
    x = (x_train - mu) / sd
    y = torch.as_tensor(y_train, dtype=torch.float32, device=x_train.device)
    net = torch.nn.Sequential(torch.nn.Linear(x.shape[1], hidden), torch.nn.ReLU(), torch.nn.Linear(hidden, 1)).to(x_train.device)
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


def decodability(states, labels, pair_ids, train, test, mlp_steps=300, device=None):
    """Per layer: the test AUROC of a logistic probe and of a perceptron, both trained on the training pairs. The
    probes train on `device` (the states' own device by default): on the CPU, one condition of the 4 October rehearsal
    had not finished after 39 minutes, while the GPU waited."""
    import torch  # noqa: WPS433
    from .extract_eval import auroc, logistic_probe  # noqa: WPS433
    dev = torch.device(device) if device is not None else states.device
    tr = torch.tensor([p in train for p in pair_ids])
    te = torch.tensor([p in test for p in pair_ids])
    y = torch.as_tensor(labels)
    y_tr, y_te = y[tr].tolist(), y[te].tolist()
    out = []
    for l in range(states.shape[1]):
        x = states[:, l, :].to(dev)
        x_tr, x_te = x[tr.to(dev)], x[te.to(dev)]
        lin = logistic_probe(x_tr, y_tr)
        mlp = mlp_probe(x_tr, y_tr, steps=mlp_steps)
        out.append({"linear": round(auroc(lin(x_te).cpu(), y_te), 4), "mlp": round(auroc(mlp(x_te).cpu(), y_te), 4)})
    return out


def transfer(source, source_labels, target, target_labels, mlp_steps=300, device=None):
    """Per layer: the AUROC, on the target states, of a logistic probe and of a perceptron trained on all the source
    states. The source is another cue set, written with other words: a probe that carries over reads the distinction
    the two sets share, not the words of one of them (which a probe trained and tested on one set can read)."""
    import torch  # noqa: WPS433
    from .extract_eval import auroc, logistic_probe  # noqa: WPS433
    dev = torch.device(device) if device is not None else source.device
    out = []
    for l in range(source.shape[1]):
        xs, xt = source[:, l, :].to(dev), target[:, l, :].to(dev)
        lin = logistic_probe(xs, list(source_labels))
        mlp = mlp_probe(xs, list(source_labels), steps=mlp_steps)
        out.append({"linear": round(auroc(lin(xt).cpu(), list(target_labels)), 4),
                    "mlp": round(auroc(mlp(xt).cpu(), list(target_labels)), 4)})
    return out


def residual_projection(states_last, subspace, rank):
    """Per layer: the mean norm of the component of the last-token state in the first `rank` directions."""
    out = []
    for l in range(states_last.shape[1]):
        b = subspace[f"layer_{l + 1:02d}.basis"][:rank].float()
        out.append(round(float((states_last[:, l, :] @ b.T).norm(dim=-1).mean()), 4))
    return out


def check(model, tok, pairs, conditions, subspace, rank, batch, device, seed=0, mlp_steps=300, progress=None,
          probe_device=None, on_result=None, source=None):
    """pairs: [(pair_id, eval_messages, deploy_messages)] of a held-out cue set. conditions: {name: a context manager
    factory (an intervention), or None}. The probes train on probe_device (the CPU by default). on_result(name, result)
    is called as each condition ends, so that a run stopped midway keeps the conditions already done. source: pairs of
    another cue set, read under the same condition; probes trained on them are read on the held-out set (transfer).
    Returns {name: {"layers": [...], "summary": {...}}}."""
    import contextlib  # noqa: WPS433
    convs = [p[1] for p in pairs] + [p[2] for p in pairs]
    labels = [1] * len(pairs) + [0] * len(pairs)
    pids = [p[0] for p in pairs] * 2
    train, test = split_pairs([p[0] for p in pairs], seed)
    s_convs = [p[1] for p in source or []] + [p[2] for p in source or []]
    s_labels = [1] * len(source or []) + [0] * len(source or [])
    out = {}
    for name, make in conditions.items():
        if progress:
            progress(f"manipulation check: {name}")
        with (make() if make else contextlib.nullcontext()):
            last, mean = read_states(model, tok, convs, batch, device)
            if source:
                s_last, s_mean = read_states(model, tok, s_convs, batch, device)
        dl = decodability(last, labels, pids, train, test, mlp_steps, probe_device)
        dm = decodability(mean, labels, pids, train, test, mlp_steps, probe_device)
        res = residual_projection(last, subspace, rank)
        layers = [{"layer": l + 1, "linear_last": dl[l]["linear"], "mlp_last": dl[l]["mlp"], "linear_mean": dm[l]["linear"],
                   "mlp_mean": dm[l]["mlp"], "residual_projection": res[l]} for l in range(len(dl))]
        best = [max(x["linear_last"], x["mlp_last"], x["linear_mean"], x["mlp_mean"]) for x in layers]
        summary = {"best_auroc_mean_over_layers": round(sum(best) / len(best), 4), "best_auroc_max_over_layers": round(max(best), 4)}
        if source:
            tl = transfer(s_last, s_labels, last, labels, mlp_steps, probe_device)
            tm = transfer(s_mean, s_labels, mean, labels, mlp_steps, probe_device)
            for l, x in enumerate(layers):
                x.update({"transfer_linear_last": tl[l]["linear"], "transfer_mlp_last": tl[l]["mlp"],
                          "transfer_linear_mean": tm[l]["linear"], "transfer_mlp_mean": tm[l]["mlp"]})
            tb = [max(x["transfer_linear_last"], x["transfer_mlp_last"], x["transfer_linear_mean"], x["transfer_mlp_mean"])
                  for x in layers]
            summary.update({"transfer_best_auroc_mean_over_layers": round(sum(tb) / len(tb), 4),
                            "transfer_best_auroc_max_over_layers": round(max(tb), 4)})
        out[name] = {"layers": layers, "summary": summary}
        if on_result:
            on_result(name, out[name])
    return out
