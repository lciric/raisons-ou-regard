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

REPO_TYPE = "dataset"


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
    def __init__(self, repo=None, token=None, api=None):
        self.repo = repo or repo_id()
        self.token = token if token is not None else hf_token()
        if api is None:
            from huggingface_hub import HfApi  # noqa: WPS433
            api = HfApi(token=self.token)
        self.api = api

    # writing
    def put_bytes(self, path, data, message=None):
        self.api.upload_file(path_or_fileobj=data, path_in_repo=path, repo_id=self.repo, repo_type=REPO_TYPE,
                             commit_message=message or f"rrexp: {path}")

    def put_json(self, path, obj, message=None):
        self.put_bytes(path, json.dumps(obj, ensure_ascii=False, indent=1).encode("utf8"), message)

    def put_file(self, path, local, message=None):
        self.api.upload_file(path_or_fileobj=str(local), path_in_repo=path, repo_id=self.repo, repo_type=REPO_TYPE,
                             commit_message=message or f"rrexp: {path}")

    def put_folder(self, path, local, message=None, ignore=None):
        self.api.upload_folder(repo_id=self.repo, folder_path=str(local), path_in_repo=path, repo_type=REPO_TYPE,
                               commit_message=message or f"rrexp: {path}", ignore_patterns=ignore)

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
