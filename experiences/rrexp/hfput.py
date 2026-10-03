"""Uploads and downloads on the results repository with the Python standard library alone.

The container script uses it before any package is installed: the run reports that it started, fetches its code
bundle, and uploads its log even when pip, the code download or the runner fails. It is written to the machine as a
file by the script (see command.py), so it must not import anything outside the standard library.

    python3 hfput.py put <path in repo> <local file>
    python3 hfput.py get <path in repo> <local file>
"""
import base64
import json
import os
import sys
import urllib.request

ENDPOINT = os.environ.get("HF_ENDPOINT", "https://huggingface.co")


def _headers(extra=None):
    h = {"Authorization": "Bearer " + os.environ["HF_TOKEN"], "User-Agent": "rrexp-boot"}
    h.update(extra or {})
    return h


def put(repo, path, data, summary):
    """One commit with one small text file, inline (the commit endpoint's NDJSON format)."""
    lines = [{"key": "header", "value": {"summary": summary, "description": ""}},
             {"key": "file", "value": {"content": base64.b64encode(data).decode("ascii"), "path": path, "encoding": "base64"}}]
    body = "\n".join(json.dumps(l) for l in lines).encode("utf8")
    req = urllib.request.Request(f"{ENDPOINT}/api/datasets/{repo}/commit/main", data=body, method="POST",
                                 headers=_headers({"Content-Type": "application/x-ndjson"}))
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status


def get(repo, path, local):
    req = urllib.request.Request(f"{ENDPOINT}/datasets/{repo}/resolve/main/{path}", headers=_headers())
    with urllib.request.urlopen(req, timeout=600) as r, open(local, "wb") as fh:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            fh.write(chunk)
    return local


def main(argv):
    repo = os.environ["RR_RESULTS_REPO"]
    if argv[0] == "put":
        with open(argv[2], "rb") as fh:
            data = fh.read()[-400_000:]   # a log's last 400 kB at most: the inline commit is for small files
        print("put", put(repo, argv[1], data, f"rrexp: {argv[1]}"))
    elif argv[0] == "get":
        print("get", get(repo, argv[1], argv[2]))
    else:
        raise SystemExit("usage: hfput.py put|get <path in repo> <local file>")


if __name__ == "__main__":
    main(sys.argv[1:])
