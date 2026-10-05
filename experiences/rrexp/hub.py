"""The private results repository on Hugging Face: code bundles, run statuses, outputs, data.

The GPU machines cannot be reached from the session (no SSH): the session and the machines exchange everything
through this repository. Layout:
- code/<sha256, 16 characters>.tar.gz : the code a run executes;
- runs/<run_id>/launch.json, status.json, log.txt, out/... : one run;
- data/<name>/... : data the runs read (the arms of the training data, for instance).

The repository is read from RR_RESULTS_REPO, the token from HF_TOKEN; neither is printed.
"""
import json
import os
import time

REPO_TYPE = "dataset"


def rate_limited(error):
    """True for the repository's answer to too many commits (HTTP 429). Hugging Face takes at most 128 commits an hour
    on a repository: on October 5, 2026, three runs at once crossed it, and a finished run lost its final upload."""
    response = getattr(error, "response", None)
    return getattr(response, "status_code", None) == 429 or "429 Too Many Requests" in str(error)[:500]


def repo_id():
    r = os.environ.get("RR_RESULTS_REPO")
    if not r:
        raise RuntimeError("RR_RESULTS_REPO is not set (the private results repository, for instance lciric/rr-resultats)")
    return r


def hf_token():
    t = os.environ.get("HF_TOKEN")
    if not t:
        raise RuntimeError("HF_TOKEN is not set in the environment")
    return t


class Hub:
    def __init__(self, repo=None, token=None, api=None, sleep=time.sleep):
        self.repo = repo or repo_id()
        self.token = token if token is not None else hf_token()
        if api is None:
            from huggingface_hub import HfApi  # noqa: WPS433
            api = HfApi(token=self.token)
        self.api = api
        self.sleep = sleep

    def _patient(self, upload, patience):
        """Runs an upload; when the repository refuses it for too many commits, waits and tries again, for up to
        `patience` seconds in all (0, the default: the error is raised at once, as for any other error)."""
        waited = 0.0
        while True:
            try:
                return upload()
            except Exception as e:  # noqa: BLE001
                if not rate_limited(e) or waited >= patience:
                    raise
                step = min(300.0, patience - waited)
                print(f"[rrexp] too many commits on the repository: waiting {step:.0f} s ({waited / 60:.0f} min so far)",
                      flush=True)
                self.sleep(step)
                waited += step

    # writing
    def put_bytes(self, path, data, message=None, patience=0):
        self._patient(lambda: self.api.upload_file(path_or_fileobj=data, path_in_repo=path, repo_id=self.repo,
                                                   repo_type=REPO_TYPE, commit_message=message or f"rrexp: {path}"),
                      patience)

    def put_json(self, path, obj, message=None, patience=0):
        self.put_bytes(path, json.dumps(obj, ensure_ascii=False, indent=1).encode("utf8"), message, patience)

    def put_file(self, path, local, message=None, patience=0):
        self._patient(lambda: self.api.upload_file(path_or_fileobj=str(local), path_in_repo=path, repo_id=self.repo,
                                                   repo_type=REPO_TYPE, commit_message=message or f"rrexp: {path}"),
                      patience)

    def put_folder(self, path, local, message=None, ignore=None, patience=0):
        self._patient(lambda: self.api.upload_folder(repo_id=self.repo, folder_path=str(local), path_in_repo=path,
                                                     repo_type=REPO_TYPE, commit_message=message or f"rrexp: {path}",
                                                     ignore_patterns=ignore),
                      patience)

    # reading
    def exists(self, path):
        return self.api.file_exists(self.repo, path, repo_type=REPO_TYPE)

    def get_json(self, path):
        """A fresh read of a JSON file of the repository, or None if it does not exist."""
        if not self.exists(path):
            return None
        p = self.api.hf_hub_download(self.repo, path, repo_type=REPO_TYPE, force_download=True)
        with open(p, encoding="utf8") as fh:
            return json.load(fh)

    def download(self, path, local_dir):
        return self.api.hf_hub_download(self.repo, path, repo_type=REPO_TYPE, local_dir=str(local_dir), force_download=True)

    def snapshot(self, patterns, local_dir, ignore=None):
        return self.api.snapshot_download(self.repo, repo_type=REPO_TYPE, allow_patterns=patterns, ignore_patterns=ignore,
                                          local_dir=str(local_dir), force_download=True)

    def list(self, prefix=""):
        return [f for f in self.api.list_repo_files(self.repo, repo_type=REPO_TYPE) if f.startswith(prefix)]

    # checks
    def check(self, gated_model=None):
        """Who the token belongs to, whether it can write to the repository, and whether it opens the gated model."""
        out = {"repo": self.repo}
        who = self.api.whoami()
        out["user"] = who.get("name")
        try:
            self.api.auth_check(self.repo, repo_type=REPO_TYPE, write=True)
            out["repo_write"] = True
        except Exception as e:  # noqa: BLE001  (the reason is reported, never the token)
            out["repo_write"] = False
            out["repo_write_error"] = type(e).__name__
        if gated_model:
            try:
                self.api.auth_check(gated_model)
                out["model_read"] = True
            except Exception as e:  # noqa: BLE001
                out["model_read"] = False
                out["model_read_error"] = type(e).__name__
        return out
