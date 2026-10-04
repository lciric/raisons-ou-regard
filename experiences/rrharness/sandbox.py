"""Isolated runs of the Python code of a scenario's workspace: its tests, and its scripts.

The files under the workspace are written to a fresh temporary folder, and Python runs there in a child process:
no user site and no PYTHON* variables, a minimal environment (no token of the machine reaches the code),
limits on CPU time, memory, file size and open files, and a wall-clock timeout. The code is the evaluated model's,
on the rented machine; the limits keep a runaway program from stopping the run, they are not a security boundary.

The test runner is plain Python: every function whose name starts with test_ in the given files runs once, in the
order of the file; a test fails if it raises. Two runs of the same files give the same report.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

RUNNER = r'''
import importlib.util, inspect, json, sys, traceback
root, files = sys.argv[1], sys.argv[2:]
sys.path.insert(0, root)
results = []
for i, f in enumerate(files):
    try:
        spec = importlib.util.spec_from_file_location(f"rr_tests_{i}", f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except BaseException as e:
        results.append({"file": f, "test": None, "ok": False, "error": f"{type(e).__name__}: {e}"[:300]})
        continue
    tests = [(n, o) for n, o in vars(mod).items() if n.startswith("test_") and callable(o)]
    tests.sort(key=lambda t: getattr(getattr(t[1], "__code__", None), "co_firstlineno", 0))
    for n, o in tests:
        try:
            o()
            results.append({"file": f, "test": n, "ok": True, "error": None})
        except BaseException as e:
            msg = str(e)
            if isinstance(e, AssertionError) and not msg:
                tb = traceback.extract_tb(e.__traceback__)
                msg = (tb[-1].line or "") if tb else ""
            results.append({"file": f, "test": n, "ok": False, "error": f"{type(e).__name__}: {msg}"[:300]})
print("@@RESULTS@@" + json.dumps(results))
'''

DEFAULT_LIMITS = {"cpu_seconds": 20, "memory_bytes": 2 * 1024 ** 3, "file_bytes": 16 * 1024 ** 2, "open_files": 64}


def _preexec(limits):
    def apply():
        import resource  # noqa: WPS433
        resource.setrlimit(resource.RLIMIT_CPU, (limits["cpu_seconds"], limits["cpu_seconds"]))
        resource.setrlimit(resource.RLIMIT_AS, (limits["memory_bytes"], limits["memory_bytes"]))
        resource.setrlimit(resource.RLIMIT_FSIZE, (limits["file_bytes"], limits["file_bytes"]))
        resource.setrlimit(resource.RLIMIT_NOFILE, (limits["open_files"], limits["open_files"]))
    return apply


def _env(home):
    return {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": home, "LANG": "C.UTF-8", "PYTHONHASHSEED": "0",
            "PYTHONDONTWRITEBYTECODE": "1"}


def materialize(files, workdir, dest, extra=None):
    """Writes the files under workdir (a dict path -> content) into dest, with paths relative to workdir; extra maps
    relative paths to contents (the hidden tests). Returns the relative paths written."""
    prefix = workdir.rstrip("/") + "/"
    written = []
    for path, content in sorted(files.items()):
        if not path.startswith(prefix):
            continue
        rel = path[len(prefix):]
        full = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf8") as fh:
            fh.write(content)
        written.append(rel)
    for rel, content in sorted((extra or {}).items()):
        full = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf8") as fh:
            fh.write(content)
        written.append(rel)
    return written


def run_python(args, cwd, timeout, limits=None):
    """Runs Python with args in cwd; returns (exit code or None on timeout, stdout, stderr)."""
    limits = dict(DEFAULT_LIMITS, **(limits or {}))
    try:
        # -E -s: no PYTHON* variables, no user site; unlike -I, a script still imports the modules next to it
        p = subprocess.run([sys.executable, "-E", "-s", *args], cwd=cwd, env=_env(cwd), capture_output=True, text=True,
                           timeout=timeout, preexec_fn=_preexec(limits))
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode("utf8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        err = e.stderr.decode("utf8", "replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
        return None, out, err


def run_tests(files, workdir, test_paths, timeout=20, extra=None, limits=None):
    """Runs the tests of test_paths (relative to workdir, possibly among extra). Returns
    {"results": [...], "passed", "failed", "total", "timeout": bool, "error": str or None}."""
    tmp = tempfile.mkdtemp(prefix="rrharness-")
    try:
        materialize(files, workdir, tmp, extra)
        runner = os.path.join(tmp, "_rr_runner.py")
        with open(runner, "w", encoding="utf8") as fh:
            fh.write(RUNNER)
        present = [p for p in test_paths if os.path.isfile(os.path.join(tmp, p))]
        missing = [p for p in test_paths if p not in present]
        code, out, err = run_python([runner, tmp, *[os.path.join(tmp, p) for p in present]], tmp, timeout, limits)
        if code is None:
            return {"results": [], "passed": 0, "failed": 0, "total": 0, "timeout": True, "missing": missing,
                    "error": f"the tests did not finish within {timeout} seconds"}
        marker = out.rfind("@@RESULTS@@")
        if marker < 0:
            return {"results": [], "passed": 0, "failed": 0, "total": 0, "timeout": False, "missing": missing,
                    "error": ("the test run stopped: " + (err.strip().splitlines() or ["no output"])[-1])[:300]}
        results = json.loads(out[marker + len("@@RESULTS@@"):].strip().splitlines()[0])
        for r in results:
            r["file"] = os.path.relpath(r["file"], tmp)
        passed = sum(r["ok"] for r in results)
        return {"results": results, "passed": passed, "failed": len(results) - passed, "total": len(results),
                "timeout": False, "missing": missing, "error": None}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def run_script(files, workdir, script, timeout=20, limits=None, max_chars=2000):
    """Runs one script (relative to workdir). Returns {"exit_code", "stdout", "stderr", "timeout"}."""
    tmp = tempfile.mkdtemp(prefix="rrharness-")
    try:
        materialize(files, workdir, tmp)
        if not os.path.isfile(os.path.join(tmp, script)):
            return {"exit_code": None, "stdout": "", "stderr": "", "timeout": False, "missing": True}
        code, out, err = run_python([script], tmp, timeout, limits)
        return {"exit_code": code, "stdout": out[-max_chars:], "stderr": err[-max_chars:], "timeout": code is None,
                "missing": False}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def report_text(rep):
    """What run_tests shows the model."""
    if rep["error"]:
        return f"Error: {rep['error']}."
    lines = [f"collected {rep['total']} tests"]
    for r in rep["results"]:
        name = r["test"] or f"(import of {r['file']})"
        lines.append(f"{name} ... ok" if r["ok"] else f"{name} ... FAILED: {r['error']}")
    lines.append(f"{rep['passed']} passed, {rep['failed']} failed")
    return "\n".join(lines)
