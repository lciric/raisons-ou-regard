"""The first inhibition in the organism: the halves, the keys, and the job on a tiny Llama with two adapters, on CPU."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import peft  # noqa: F401
    import torch
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

from rrexp.jobs import organism_inhibition as oi


class TestPieces(unittest.TestCase):
    def test_the_test_half_waits_for_the_gate(self):
        tasks = [{"task_id": i} for i in range(6)]
        halves = {"choix": [0, 2, 4], "test": [1, 3, 5]}
        self.assertEqual([t["task_id"] for t in oi.half_tasks(tasks, halves, "choix")], [0, 2, 4])
        with self.assertRaises(ValueError):
            oi.half_tasks(tasks, halves, "test")
        self.assertEqual([t["task_id"] for t in oi.half_tasks(tasks, halves, "test", gate=True)], [1, 3, 5])
        with self.assertRaises(ValueError):          # a task of the half missing from MBPP test
            oi.half_tasks(tasks[:5], halves, "test", gate=True)

    def test_the_committed_halves(self):
        h = json.loads(oi.HALVES.read_text(encoding="utf8"))
        self.assertEqual((len(h["choix"]), len(h["test"])), (250, 250))
        self.assertFalse(set(h["choix"]) & set(h["test"]))

    def test_match_fraction_reaches_the_target(self):
        calls = []
        def quadratic(x):
            calls.append(x)
            return 0.4 * x * x
        x, k = oi.match_fraction(quadratic, [(0.5, 0.1), (1.0, 0.4)], 0.05)
        self.assertAlmostEqual(x, 0.05 ** 0.5 / 0.4 ** 0.5, places=6)   # a linear interpolation of the KL would give 0.25
        self.assertAlmostEqual(k, 0.05, places=6)
        self.assertEqual(len(calls), 1)
        x, k = oi.match_fraction(lambda x: 0.3 * x ** 1.2, [(0.25, 0.3 * 0.25 ** 1.2), (1.0, 0.3)], 0.1)
        self.assertLessEqual(abs(k - 0.1), 0.005)
        self.assertEqual(oi.match_fraction(lambda x: 0.01 * x, [(1.0, 0.01)], 0.1), (None, None))

    def test_full_fraction_within_the_tolerance(self):
        self.assertTrue(oi.full_fraction_within([(1.0, 0.095), (0.5, 0.02)], 0.1, 0.1))     # 5 % under the target, at 1
        self.assertFalse(oi.full_fraction_within([(0.5, 0.02), (1.0, 0.085)], 0.1, 0.1))    # 15 % under it
        self.assertFalse(oi.full_fraction_within([(0.5, 0.02), (1.0, 0.11)], 0.1, 0.1))     # above: a fraction reaches it
        self.assertFalse(oi.full_fraction_within([(0.5, 0.095)], 0.1, 0.1))                 # the curve stops before 1
        self.assertFalse(oi.full_fraction_within([], 0.1, 0.1))

    def test_keys_and_reduction(self):
        self.assertEqual(oi.setting_key(range(1, 33), 4, 1.0, 32), "all|r4|f1")
        self.assertEqual(oi.setting_key([4, 5, 6, 7, 8], 16, 0.5, 32), "4-8|r16|f0.5")
        self.assertEqual(oi.setting_key([6], 1, 1.0, 32), "6|r1|f1")
        self.assertEqual(oi.erase_key(range(1, 33), ["extraction"], 1.0, 32), "all|leace(extraction)|f1")
        self.assertEqual(oi.erase_key([4, 5, 6, 7, 8], ["extraction", "validation"], 0.5, 32), "4-8|leace(extraction+validation)|f0.5")
        self.assertEqual(oi.erase_key(range(1, 33), ["extraction"], 0.5, 32, "base"), "all|leace(extraction)@base|f0.5")
        self.assertEqual(oi.reduction({"gap_extraction": 0.3, "gap_framing": 0.1}, {"gap_extraction": 0.1, "gap_framing": 0.15}),
                         {"extraction": 20.0, "framing": -5.0})


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestJob(unittest.TestCase):
    def test_job_runs(self):
        from peft import LoraConfig, get_peft_model
        from safetensors.torch import save_file
        from transformers import AutoModelForCausalLM

        from rrexp.jobs import inhibition_degradation as idg
        from tests.test_train_lora import tiny_model

        class Ctx:
            pass

        tmp = Path(tempfile.mkdtemp())
        try:
            tiny_model(tmp / "model")
            for name, seed in (("sdf", 1), ("ei", 2)):     # two adapters that change the model (lora_B is zero at init)
                torch.manual_seed(seed)
                m = get_peft_model(AutoModelForCausalLM.from_pretrained(tmp / "model"),
                                   LoraConfig(r=2, lora_alpha=4, target_modules=["q_proj", "v_proj"]))
                for n, p in m.named_parameters():
                    if "lora_B" in n:
                        p.data.normal_(0, 0.05)
                m.save_pretrained(tmp / name)
            g = torch.Generator().manual_seed(4)
            sub = tmp / "sub"
            sub.mkdir()
            save_file({f"layer_{l:02d}.basis": idg.orthonormal_random(4, 32, g) for l in (1, 2)}, str(sub / "eval_subspace.safetensors"))
            cues = tmp / "cues"
            cues.mkdir()
            for name, slot, n in (("extraction", "system_prompt", 4), ("framing", "message_footer", 2), ("validation", "user_preamble", 4)):
                with open(cues / f"{name}.jsonl", "w", encoding="utf8") as fh:
                    for i in range(n):
                        for pol in ("eval", "deploy"):
                            fh.write(json.dumps({"pair": f"{name}-{i:04d}", "polarity": pol, "slot": slot, "text": f"{name} {pol} {i}"}) + "\n")
            with open(cues / "contexts.jsonl", "w", encoding="utf8") as fh:
                for i in range(3):
                    fh.write(json.dumps({"id": f"ctx-{i}", "use": "snippet", "text": f"Please help me plan the week {i}."}) + "\n")
            mb = tmp / "mbpp"
            mb.mkdir()
            with open(mb / "mbpp_test.jsonl", "w", encoding="utf8") as fh:
                for i in range(6):
                    fh.write(json.dumps({"task_id": f"t{i}", "text": "Write a function to add two numbers.", "test_list": ["assert add(1, 2) == 3"]}) + "\n")
            halves = tmp / "halves.json"
            halves.write_text(json.dumps({"choix": ["t0", "t2", "t4"], "test": ["t1", "t3", "t5"]}), encoding="utf8")

            ctx = Ctx()
            ctx.out, ctx.progress = tmp / "out", ""
            ctx.out.mkdir()
            save_file({f"layer_{l:02d}.basis": idg.orthonormal_random(4, 32, g) for l in (1, 2)}, str(sub / "stake.safetensors"))
            ctx.args = {"local_model": str(tmp / "model"), "local_sdf_adapter": str(tmp / "sdf"), "local_ei_adapter": str(tmp / "ei"),
                        "local_subspace": str(sub), "local_cues": str(cues), "local_mbpp": str(mb), "local_halves": str(halves),
                        "device": "cpu", "hp": {"ei.cue_pairs_for_training": 2},
                        "settings": [{"layers": "all", "rank": 1}, {"layers": [1], "rank": 2}],
                        "comparator": {"top": 1, "n_draws": 2, "multiples": [1, 2, 4], "fractions": [0.5, 1.0],
                                       "framings": ["eval_extraction", "deploy_extraction", "eval_framing", "deploy_framing"]},
                        "controls": [{"name": "sensibles", "kind": "sensitive"},
                                     {"name": "enjeu", "kind": "subspace", "local": str(sub / "stake.safetensors")}],
                        "rival": True, "deployment_prompt": "This is a live production deployment.",
                        "manipulation": {"cue_set": "validation", "draws": 1, "failure_layer": 1, "batch": 4, "mlp_steps": 20,
                                         "contexts_per_pair": 1},
                        "batch": 2, "kl_batch": 2, "max_new_tokens": 4, "n_contexts": 3, "answer_tokens": 4}
            res = oi.run(ctx)
            self.assertEqual(set(res["settings"]), {"all|r1|f1", "1|r2|f1"})
            self.assertIn("gap_extraction", res["baseline"])
            out = json.loads((ctx.out / "results.json").read_text(encoding="utf8"))
            self.assertEqual(out["tasks"], 3)
            self.assertEqual(out["framings"], {"eval_extraction": 2, "deploy_extraction": 2, "eval_framing": 2, "deploy_framing": 2, "none": 1})
            for s in out["settings"].values():
                self.assertGreaterEqual(s["degradation"]["kl"], -1e-3)
                self.assertIn("extraction", s["reduction"])
            rows = [json.loads(l) for l in (ctx.out / "measure_baseline.jsonl").read_text(encoding="utf8").splitlines()]
            self.assertEqual(len(rows), 3 * 5)
            self.assertEqual({r["task_id"] for r in rows}, {"t0", "t2", "t4"})
            self.assertEqual(len(out["comparator"]), 1)
            c = next(iter(out["comparator"].values()))
            self.assertTrue(c["tried"])
            if c["multiple"]:
                self.assertEqual(len(c["draws"]), 2)
                for d in c["draws"]:
                    if d["fraction"] is not None:
                        self.assertEqual(set(k for k in d["measure"] if k.startswith(("eval_", "deploy_"))),
                                         {"eval_extraction", "deploy_extraction", "eval_framing", "deploy_framing"})
            self.assertTrue((ctx.out / "reference_answers.jsonl").exists())
            # its fingerprint, for the pooling of an interrupted run with its resume (section 5.5), and the GPU model
            import hashlib
            self.assertEqual(out["reference"]["sha256"], hashlib.sha256((ctx.out / "reference_answers.jsonl").read_bytes()).hexdigest())
            self.assertEqual(out["gpu"], "cpu")
            # the rival manipulation, the separate controls and the gate summary
            self.assertIn("extraction", out["rival"]["reduction"])
            rival_rows = [json.loads(l) for l in (ctx.out / "measure_rival.jsonl").read_text(encoding="utf8").splitlines()]
            self.assertEqual(len(rival_rows), 3 * 5)
            key = next(iter(out["comparator"]))
            self.assertEqual(set(out["controls"][key]), {"sensibles", "enjeu"})
            for c in out["controls"][key].values():
                self.assertTrue(c["tried"])
                if c["multiple"]:
                    self.assertIn("kl_matched", c)
                    self.assertTrue(0.0 <= c["overlap_with_evaluated"] <= 1.0 + 1e-6)
            self.assertLess(out["controls"][key]["sensibles"].get("overlap_with_evaluated", 0.0), 1e-3)
            gate = out["porte"][key]
            self.assertEqual(set(gate), {"extraction", "framing"})
            for v in gate.values():
                self.assertIn("comparator_p95", v)
                self.assertIn("beats_comparator_p95", v)
            man = out["manipulation"][key]
            self.assertEqual(man["pairs"], 4)
            conds = man["conditions"]
            self.assertTrue({"none", f"inhibition {key}", "constructed failure: layer 1 only"} <= set(conds))
            for c in conds.values():
                self.assertEqual(len(c["layers"]), 2)
                self.assertTrue(all(0.0 <= x["linear_last"] <= 1.0 for x in c["layers"]))
            self.assertEqual(oi.percentile([1, 2, 3, 4, 5], 50), 3)
            self.assertAlmostEqual(oi.percentile(list(range(101)), 95), 95.0)
            self.assertIsNone(oi.percentile([], 95))
            # "measure_from" resumes an interrupted run: the same draws, matched again, measured from that index only
            ctx5 = Ctx()
            ctx5.out, ctx5.progress = tmp / "out_resume", ""
            ctx5.args = dict(ctx.args, comparator=dict(ctx.args["comparator"], measure_from=1))
            ctx5.out.mkdir()
            oi.run(ctx5)
            out5 = json.loads((ctx5.out / "results.json").read_text(encoding="utf8"))
            c5, c1 = out5["comparator"][key], out["comparator"][key]
            self.assertEqual([d["fraction"] for d in c5["draws"]], [d["fraction"] for d in c1["draws"]])
            self.assertEqual(out5["baseline"]["gap_extraction"], out["baseline"]["gap_extraction"])
            self.assertTrue(c1["multiple"] and c5["draws"][1]["fraction"] is not None)     # the tiny model reaches the KL
            if c1["multiple"]:
                self.assertEqual(c5["measure_from"], 1)
                self.assertNotIn("reduction", c5["draws"][0])
                self.assertFalse((ctx5.out / f"measure_comparator_{key.replace('|', '_')}_00.jsonl").exists())
                if c5["draws"][1]["fraction"] is not None:
                    self.assertEqual(c5["draws"][1]["reduction"], c1["draws"][1]["reduction"])
                    self.assertTrue((ctx5.out / f"measure_comparator_{key.replace('|', '_')}_01.jsonl").exists())
            # "gaps": false reruns the manipulation check alone: nothing generated, the same matched conditions
            ctx2 = Ctx()
            ctx2.out, ctx2.progress, ctx2.args = tmp / "out_check", "", dict(ctx.args, gaps=False)
            ctx2.out.mkdir()
            oi.run(ctx2)
            out2 = json.loads((ctx2.out / "results.json").read_text(encoding="utf8"))
            self.assertIs(out2["gaps"], False)
            self.assertEqual((ctx2.out / "measure_baseline.jsonl").read_text(encoding="utf8"), "")
            self.assertNotIn("rival", out2)
            self.assertNotIn("porte", out2)
            for k, s in out2["settings"].items():
                self.assertEqual(s["reduction"], {})
                self.assertAlmostEqual(s["degradation"]["kl"], out["settings"][k]["degradation"]["kl"], places=6)
            self.assertEqual([d["fraction"] for d in out2["comparator"][key]["draws"]],
                             [d["fraction"] for d in out["comparator"][key]["draws"]])
            man2 = out2["manipulation"][key]
            self.assertEqual(set(man2["conditions"]), set(conds))
            self.assertEqual(man2["conditions_planned"], list(man2["conditions"]))
            # the closed-form erasure as a setting: fitted, matched, checked, with its constructed failure
            ctx3 = Ctx()
            ctx3.out, ctx3.progress = tmp / "out_erase", ""
            ctx3.args = dict(ctx.args, gaps=False, rival=False, controls=[],
                             manipulation=dict(ctx.args["manipulation"], transfer_from="extraction", transfer_contexts_per_pair=1),
                             settings=[{"layers": "all", "erase": {"fit_sets": ["extraction"], "contexts_per_pair": 1}},
                                       {"layers": [1], "erase": {"fit_sets": ["extraction"], "contexts_per_pair": 1, "sequential": False}}],
                             comparator={"top": 2, "n_draws": 1, "multiples": [1, 2, 4], "fractions": [0.5, 1.0]})
            ctx3.out.mkdir()
            oi.run(ctx3)
            out3 = json.loads((ctx3.out / "results.json").read_text(encoding="utf8"))
            ekey, ekey1 = "all|leace(extraction)|f1", "1|leace(extraction)|f1"
            self.assertEqual(list(out3["settings"]), [ekey, ekey1])
            self.assertEqual(out3["erasure"][ekey]["directions_per_layer"], 1)
            self.assertEqual(out3["erasure"][ekey]["states"], 2 * 2)      # the 2 pairs of the expert iteration, 1 context, 2 sides
            self.assertGreater(out3["settings"][ekey]["degradation"]["kl"], 0.0)
            self.assertTrue({"none", f"inhibition {ekey}", "constructed failure: layer 1 only"} <= set(out3["manipulation"][ekey]["conditions"]))
            # the transfer: probes trained on the extraction pairs kept out of the expert iteration (pairs 2 and 3,
            # 1 context each), read on the validation set, under each condition
            man3 = out3["manipulation"][ekey]
            self.assertEqual((man3["transfer_from"], man3["transfer_pairs"]), ("extraction", 2))
            for res in man3["conditions"].values():
                self.assertIn("transfer_linear_last", res["layers"][0])
                self.assertIn("transfer_best_auroc_max_over_layers", res["summary"])
            # the condition without intervention is computed once, then shared with the second setting (same rank)
            m1 = out3["manipulation"][ekey1]
            self.assertEqual(m1.get("none_shared_from"), ekey)
            self.assertEqual(m1["conditions"]["none"], out3["manipulation"][ekey]["conditions"]["none"])
            # the erasure fitted on the starting model, before the adapters are merged (decision 34): the fit sees the
            # starting model's weights, not the organism's, and the fitted erasure is written out
            from safetensors.torch import load_file

            def q_sum(model):
                return float(model.model.layers[0].self_attn.q_proj.weight.double().sum())
            seen, fit = [], oi.er.fit_layers

            def spy(model, *args, **kw):
                seen.append(q_sum(model))
                return fit(model, *args, **kw)
            ctx4 = Ctx()
            ctx4.out, ctx4.progress = tmp / "out_erase_base", ""
            ctx4.args = dict(ctx3.args, settings=[{"layers": "all", "fraction": 0.5,
                                                   "erase": {"fit_sets": ["extraction"], "contexts_per_pair": 1, "fit_on": "base"}}],
                             comparator={"top": 1, "n_draws": 1, "multiples": [1, 2, 4], "fractions": [0.5, 1.0]})
            ctx4.out.mkdir()
            with mock.patch.object(oi.er, "fit_layers", spy):
                oi.run(ctx4)
            out4 = json.loads((ctx4.out / "results.json").read_text(encoding="utf8"))
            bkey = "all|leace(extraction)@base|f0.5"
            self.assertEqual(list(out4["settings"]), [bkey])
            self.assertEqual((out4["erasure"][bkey]["fit_on"], out4["erasure"][bkey]["states"]), ("base", 2 * 2))
            start = q_sum(AutoModelForCausalLM.from_pretrained(tmp / "model"))
            organism = q_sum(oi.load_organism(tmp / "model", tmp / "sdf", tmp / "ei", torch.float32, "cpu"))
            self.assertEqual(len(seen), 1)
            self.assertAlmostEqual(seen[0], start, places=5)
            self.assertGreater(abs(start - organism), 1e-3)
            saved = load_file(str(ctx4.out / "erasure_all_leace(extraction)@base_f0.5.safetensors"))
            self.assertEqual(set(saved), {f"layer_{l:02d}.{k}" for l in (1, 2) for k in ("mean", "B", "C")})
            self.assertGreater(out4["settings"][bkey]["degradation"]["kl"], 0.0)
            self.assertTrue({"none", f"inhibition {bkey}", "constructed failure: layer 1 only"} <= set(out4["manipulation"][bkey]["conditions"]))
            # the nulls built like the setting: erasures fitted on the same states, each pair's polarities swapped at
            # random, matched on the KL and checked on the composite; the random comparator skipped
            from tests.test_composite import FakeJev, tiny_items
            seen.clear()
            ctx8 = Ctx()
            ctx8.out, ctx8.progress = tmp / "out_shuffled", ""
            ctx8.args = dict(ctx4.args, gaps=False, manipulation=None, rival=False,
                             controls=[{"kind": "erase_shuffled", "name": "shuffled", "n": 2, "seed": 3}],
                             comparator={"top": 1, "n_draws": 0, "multiples": [1, 2, 4], "fractions": [0.5, 1.0]},
                             local_composite=str(tiny_items(tmp / "composite_items_8")), local_jev="unused",
                             composite={"report_only": ["code"], "batch": 2,
                                        "max_new": {c: 4 for c in ("gsm8k", "code", "coherence", "format", "tools")}})
            ctx8.out.mkdir()
            with mock.patch.object(oi.er, "fit_layers", spy), mock.patch("rrexp.jev.Jev", FakeJev):
                oi.run(ctx8)
            out8 = json.loads((ctx8.out / "results.json").read_text(encoding="utf8"))
            self.assertEqual(len(seen), 3)                                  # the setting, then its two nulls, on the base
            self.assertTrue(all(abs(s - start) < 1e-4 for s in seen))
            self.assertEqual(out8["comparator"][bkey]["draws"], [])
            ctl8 = out8["controls"][bkey]
            self.assertEqual(set(ctl8), {"shuffled 1", "shuffled 2"})
            for c in ctl8.values():
                self.assertEqual(c["kind"], "erase_shuffled")
                if c.get("fraction") is not None:
                    self.assertIn("composite_check", c)
            # the named draws only, with the polarities they have in a run of all n (the same curve as above); and a
            # null whose curve stops below the setting's KL within the tolerance, taken at fraction 1
            seen.clear()
            ctx9 = Ctx()
            ctx9.out, ctx9.progress = tmp / "out_shuffled_named", ""
            ctx9.args = dict(ctx8.args, controls=[{"kind": "erase_shuffled", "name": "shuffled", "n": 2, "seed": 3,
                                                   "draws": [2], "full_if_within": True}])
            ctx9.out.mkdir()
            with mock.patch.object(oi.er, "fit_layers", spy), mock.patch("rrexp.jev.Jev", FakeJev), \
                    mock.patch.object(oi, "match_fraction", lambda kl_at, pts, target: (None, None)), \
                    mock.patch.object(oi, "full_fraction_within", lambda pts, target, tol: True):
                oi.run(ctx9)
            out9 = json.loads((ctx9.out / "results.json").read_text(encoding="utf8"))
            self.assertEqual(len(seen), 2)                                  # the setting, then the named null only
            ctl9 = out9["controls"][bkey]
            self.assertEqual(set(ctl9), {"shuffled 2"})
            self.assertEqual(ctl9["shuffled 2"]["curve"], ctl8["shuffled 2"]["curve"])
            self.assertEqual((ctl9["shuffled 2"]["fraction"], ctl9["shuffled 2"]["at_full"]), (1.0, True))
            self.assertIn("composite_check", ctl9["shuffled 2"])
            bad = dict(ctx9.args, controls=[{"kind": "erase_shuffled", "name": "shuffled", "n": 2, "draws": [3]}])
            with self.assertRaises(ValueError):           # the draws are numbered from 1 to n
                oi.run(type("C", (), {"out": tmp / "out_bad_draws", "progress": "", "args": bad})())
            with self.assertRaises(ValueError):           # a null built like an erasure needs a setting that erases
                oi.run(type("C", (), {"out": tmp / "out_bad", "progress": "", "args": dict(ctx8.args, settings=[{"layers": "all", "rank": 1}])})())
            ctx4.args = dict(ctx4.args, settings=[{"layers": "all", "erase": {"fit_on": "elsewhere"}}])
            with self.assertRaises(ValueError):
                oi.run(ctx4)
            # the composite (registration, Appendix B.1): measured under the baseline, the setting, each measured draw
            # and each control; the coherence judged once the model is freed (a fixed scorer stands for JEV-27B); each
            # condition then checked against its setting, the code reported only (it shares the outcome's format)
            from tests.test_composite import FakeJev, tiny_items
            items = tiny_items(tmp / "composite_items")
            ctx6 = Ctx()
            ctx6.out, ctx6.progress = tmp / "out_composite", ""
            ctx6.args = dict(ctx.args, rival=False, manipulation=None, settings=[{"layers": "all", "rank": 1}],
                             local_composite=str(items), local_jev="unused",
                             composite={"report_only": ["code"], "batch": 2,
                                        "max_new": {c: 4 for c in ("gsm8k", "code", "coherence", "format", "tools")}},
                             comparator=dict(ctx.args["comparator"], gate_draws=1))
            ctx6.out.mkdir()
            with mock.patch("rrexp.jev.Jev", FakeJev):
                res6 = oi.run(ctx6)
            out6 = json.loads((ctx6.out / "results.json").read_text(encoding="utf8"))
            key6 = "all|r1|f1"
            conds6 = out6["composite"]["conditions"]
            self.assertTrue({"baseline", key6} <= set(conds6))
            self.assertEqual(out6["composite"]["report_only"], ["code"])
            self.assertEqual(out6["composite"]["items"]["mmlu"]["n"], 2)
            for name, vals in conds6.items():
                self.assertIn("coherence", vals, name)            # judged at the end
                self.assertIn("mmlu", vals, name)
            self.assertEqual(out6["settings"][key6]["composite"], conds6[key6])
            measured = [d for d in out6["comparator"][key6]["draws"] if "reduction" in d]
            self.assertTrue(measured)
            for d in measured:
                self.assertIn("composite_check", d)
                self.assertEqual(d["matched"], bool(d["kl_matched"]) and d["composite_check"]["within"] is True)
                self.assertEqual(d["composite_check"]["reported_only"], ["code"])
            for c in out6["controls"][key6].values():
                if "reduction" in c:
                    self.assertIn("matched", c)
            gate6 = out6["porte"][key6]["extraction"]
            self.assertEqual(gate6["matching"], "kl+composite")
            self.assertLessEqual(gate6["comparator_draws_matched"], 1)    # gate_draws: the first matched draw only
            self.assertIn("components_at_fault", gate6)
            self.assertEqual(res6["porte"], out6["porte"])
            # decision 40: the exam components, the setting's shift against every draw matched on the KL
            own6 = out6["composite"]["own_effect"][key6]
            self.assertEqual(set(own6), {"mmlu", "gsm8k", "order_mmlu"})
            self.assertEqual(own6["mmlu"]["draws"], sum(1 for d in measured if d["kl_matched"]))
            judged = [json.loads(l) for l in (ctx6.out / "composite_coherence_judged.jsonl").read_text(encoding="utf8").splitlines()]
            self.assertEqual(len(judged), 2 * len(conds6))               # two coherence requests per condition
            self.assertTrue((ctx6.out / "composite_baseline.jsonl").exists())
            # the composite alone, without the gaps: every condition checked, no gate summary
            ctx7 = Ctx()
            ctx7.out, ctx7.progress = tmp / "out_composite_alone", ""
            ctx7.args = dict(ctx6.args, gaps=False)
            ctx7.out.mkdir()
            with mock.patch("rrexp.jev.Jev", FakeJev):
                oi.run(ctx7)
            out7 = json.loads((ctx7.out / "results.json").read_text(encoding="utf8"))
            self.assertNotIn("porte", out7)
            self.assertEqual(set(out7["composite"]["conditions"]), set(conds6))
            for d in out7["comparator"][key6]["draws"]:
                if d.get("fraction") is not None:
                    self.assertIn("composite_check", d)
                    self.assertEqual(d["reduction"], {})            # no gap measured
            self.assertEqual((ctx7.out / "measure_baseline.jsonl").read_text(encoding="utf8"), "")
            ctx.args["half"] = "test"                     # the test half waits for the gate
            with self.assertRaises(ValueError):
                oi.run(ctx)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
