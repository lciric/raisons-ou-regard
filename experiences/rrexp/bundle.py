"""The code bundle a GPU run executes: the experiments and the data pipeline's code, as committed.

The bundle is a gzip tar, byte for byte reproducible from the same files (sorted names, null dates and owners).
Its SHA-256 names it in the results repository and goes into the run's record, with the git commit.
"""
import gzip
import hashlib
import io
import os
import subprocess
import tarfile

PATHS = ("experiences", "donnees")
EXCLUDE_PARTS = ("__pycache__", "sorties", "registre", "resultats", ".pytest_cache")


def _git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, check=True).stdout


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return _git(here, "rev-parse", "--show-toplevel").strip()


def _wanted(path):
    parts = path.split("/")
    return not any(p in EXCLUDE_PARTS for p in parts) and not path.endswith(".pyc")


def build(out_dir, root=None, paths=PATHS, allow_dirty=False):
    """Writes the bundle into out_dir. Refuses uncommitted changes under paths, unless allow_dirty (dry runs)."""
    root = root or repo_root()
    dirty = [l for l in _git(root, "status", "--porcelain", "--", *paths).splitlines() if _wanted(l[3:])]
    if dirty and not allow_dirty:
        raise RuntimeError("uncommitted changes under " + ", ".join(paths) + ": commit them first (" + "; ".join(dirty[:5]) + ")")
    head = _git(root, "rev-parse", "HEAD").strip()
    files = sorted(f for f in _git(root, "ls-files", "-co", "--exclude-standard", "--", *paths).splitlines()
                   if _wanted(f) and os.path.isfile(os.path.join(root, f)))
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for f in files:
            full = os.path.join(root, f)
            info = tarfile.TarInfo(f)
            info.size = os.path.getsize(full)
            info.mode = 0o755 if os.access(full, os.X_OK) else 0o644
            info.mtime, info.uid, info.gid, info.uname, info.gname = 0, 0, 0, "", ""
            with open(full, "rb") as fh:
                tar.addfile(info, fh)
    gz = io.BytesIO()
    with gzip.GzipFile(fileobj=gz, mode="wb", mtime=0) as z:
        z.write(raw.getvalue())
    data = gz.getvalue()
    sha = hashlib.sha256(data).hexdigest()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{sha[:16]}.tar.gz")
    with open(path, "wb") as fh:
        fh.write(data)
    return {"path": path, "sha256": sha, "repo_path": f"code/{sha[:16]}.tar.gz", "git_head": head,
            "dirty": bool(dirty), "files": len(files), "bytes": len(data)}
