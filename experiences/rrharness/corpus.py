"""The texts of the held-out scenarios, for the n-gram gate of the training data (mini-spec §8, point 4).

The gate (donnees/rrdata/assemble.py, config ngram.heldout_corpus) reads JSONL {"id", "text"}. One line per
scenario variant: every text a scenario holds, its cue markers removed (the framing cues are checked apart, by the
cue gate), the tool descriptions left out (they are shared with training by design).
"""
import json

from .scenario import fill_marks, load


def scenario_text(scn):
    d = scn.data
    env = d.get("environment") or {}
    parts = [d.get("system_prompt", "")]
    parts += [t.get("content", "") for t in d.get("turns") or []]
    for _, f in sorted((env.get("files") or {}).items()):
        parts.append(f if isinstance(f, str) else (f or {}).get("content", ""))
    for m in env.get("inbox") or []:
        parts += [m.get("subject", ""), m.get("body", "")]
    parts += [e.get("title", "") for e in env.get("calendar") or []]
    parts += [t.get("title", "") for t in (env.get("tickets") or {}).values()]
    for it in env.get("eval_items") or []:
        parts += [it.get("question", ""), str(it.get("answer", ""))]
    code = env.get("code") or {}
    parts += list((code.get("hidden_tests") or {}).values())
    truth = d.get("truth") or {}
    parts += [truth.get("task", ""), truth.get("authorized", ""), truth.get("aligned", "")] + list(truth.get("misaligned") or [])
    parts += [q.get("question", "") for q in d.get("judge_questions") or []]
    return "\n".join(fill_marks(p, None, None) for p in parts if p)


def write_corpus(paths, out_path, include_fixtures=False):
    """Writes the corpus of the scenario files; returns the number of lines. The fixtures (the harness's own
    examples) are left out unless asked."""
    n = 0
    with open(out_path, "w", encoding="utf8") as fh:
        for path in paths:
            for scn in load(path):
                if scn.fixture and not include_fixtures:
                    continue
                fh.write(json.dumps({"id": scn.id, "text": scenario_text(scn)}, ensure_ascii=False) + "\n")
                n += 1
    return n
