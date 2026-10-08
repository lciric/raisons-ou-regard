"""The vast.ai REST API, called as the official client does (vastai 1.8.3, read on October 3, 2026).

The Claude Code cloud session only reaches the network over HTTPS: no SSH reaches the machines. Instances are
therefore created, watched and destroyed through the API alone. They run their job as the container's command
(the "args" launch mode, with bash as entrypoint, as in the client's own example), so the container exits, and GPU
billing stops, when the job ends.

The key is read from VAST_API_KEY and never printed. Without it, requests go out without an Authorization header:
the environment's API credential for console.vast.ai, if there is one, is attached by the session's proxy, and the
session never sees the key (Claude Code cloud environments, "API credentials").
"""
import os
import time

import requests

API_BASE = os.environ.get("VAST_URL", "https://console.vast.ai") + "/api/v0"

# The client's default filters (vastai/api/offers.py, search_offers). gpu_ram is in MB in the API.
DEFAULT_FILTERS = {"verified": {"eq": True}, "external": {"eq": False}, "rentable": {"eq": True}, "rented": {"eq": False}}

# Statuses after which an instance never reaches "running" (vast.ai agent guide, vastai/SKILL.md).
DEAD_STATUSES = {"exited", "unknown", "offline"}


class VastError(RuntimeError):
    pass


def offer_query(gpu, num_gpus, disk_gb, filters, max_dph_per_gpu=None):
    """The search query for one GPU type, in the API's format. gpu: {"name", "min_gpu_ram_gb"}."""
    q = dict(DEFAULT_FILTERS)
    q["gpu_name"] = {"eq": gpu["name"]}
    q["num_gpus"] = {"eq": int(num_gpus)}
    if gpu.get("min_gpu_ram_gb"):
        q["gpu_ram"] = {"gte": float(gpu["min_gpu_ram_gb"]) * 1000}
    q["disk_space"] = {"gte": float(disk_gb)}
    if filters.get("reliability_min") is not None:
        q["reliability"] = {"gt": float(filters["reliability_min"])}
    if filters.get("inet_down_min_mbps") is not None:
        q["inet_down"] = {"gte": float(filters["inet_down_min_mbps"])}
    if filters.get("cuda_min") is not None:
        q["cuda_max_good"] = {"gte": float(filters["cuda_min"])}
    if filters.get("datacenter_only"):
        q["datacenter"] = {"eq": True}
    if max_dph_per_gpu is not None:
        q["dph_total"] = {"lte": float(max_dph_per_gpu) * int(num_gpus)}
    q["order"] = [["dph_total", "asc"]]
    q["type"] = "on-demand"
    q["allocated_storage"] = float(disk_gb)
    return q


def create_payload(image, env, disk_gb, label, script):
    """The body of PUT /asks/{offer}/ (vastai build_create_instance_payload), in the "args" launch mode.

    As in the client's example (`--onstart-cmd 'bash' --args -c '...'`), "onstart" overrides the entrypoint with
    bash and "args" holds `-c <script>`: the container runs the script and exits when it returns.
    """
    return {
        "client_id": "me", "image": image, "env": dict(env), "price": None, "disk": float(disk_gb), "label": label,
        "extra": None, "onstart": "bash", "image_login": None, "python_utf8": False, "lang_utf8": False,
        "use_jupyter_lab": False, "jupyter_dir": None, "force": False, "cancel_unavail": True,
        "template_hash_id": None, "user": None, "runtype": "args", "args": ["-c", script],
    }


class Vast:
    def __init__(self, key=None, base=None, http=None, retries=6, timeout=60, sleep=time.sleep):
        self.key = key if key is not None else os.environ.get("VAST_API_KEY")
        self.via_proxy = not self.key   # the proxy attaches the environment's credential for console.vast.ai
        self.base = base or API_BASE
        self.http = http or requests.Session()
        self.retries, self.timeout, self.sleep = retries, timeout, sleep

    def _call(self, method, path, body=None, params=None):
        headers = {"User-Agent": "rrexp"}
        if self.key:
            headers["Authorization"] = "Bearer " + self.key
        for attempt in range(self.retries):
            try:
                r = self.http.request(method, self.base + path, json=body, params=params, headers=headers, timeout=self.timeout)
            except (requests.ConnectionError, requests.Timeout) as e:
                if attempt == self.retries - 1:
                    raise VastError(f"{method} {path}: {type(e).__name__}") from None
                self.sleep(2 ** attempt)
                continue
            if r.status_code in (429, 502, 503, 504) and attempt < self.retries - 1:
                wait = 2 ** (attempt + 1)
                if r.status_code == 429:  # the API allows about 5 requests at a time and says when to retry
                    try:
                        wait = max(wait, float(r.json().get("retry_after", 0)) + 1)
                    except Exception:  # noqa: BLE001
                        pass
                self.sleep(wait)
                continue
            if r.status_code in (401, 403) and self.via_proxy:
                raise VastError(f"{method} {path}: HTTP {r.status_code}: no VAST_API_KEY, and no API credential for console.vast.ai "
                                "attached by the environment")
            if r.status_code >= 400:
                raise VastError(f"{method} {path}: HTTP {r.status_code}: {r.text[:300]}")
            return r.json() if r.content else {}
        raise VastError(f"{method} {path}: no answer")

    def user(self):
        """The account (credit balance among others); the API removes the key from the answer."""
        u = self._call("GET", "/users/current")
        u.pop("api_key", None)
        return u

    def search_offers(self, query):
        return self._call("POST", "/bundles/", body=query).get("offers", [])

    def create_instance(self, offer_id, payload):
        """Returns the new instance id."""
        r = self._call("PUT", f"/asks/{int(offer_id)}/", body=payload)
        if not r.get("success") or not r.get("new_contract"):
            raise VastError(f"instance not created: {r}")
        return int(r["new_contract"])

    def show_instance(self, instance_id):
        """The instance row, or None when it no longer exists."""
        try:
            return self._call("GET", f"/instances/{int(instance_id)}/", params={"owner": "me"}).get("instances")
        except VastError as e:
            if "HTTP 404" in str(e):
                return None
            raise

    def destroy_instance(self, instance_id):
        return self._call("DELETE", f"/instances/{int(instance_id)}/", body={})

    def request_logs(self, instance_id, tail=300):
        """The URL where vast.ai puts the container's last log lines (to fetch separately; its host may be closed)."""
        return self._call("PUT", f"/instances/request_logs/{int(instance_id)}/", body={"tail": str(tail)}).get("result_url")


def offer_cost(offer, hours, download_gb):
    """The expected cost of a run on an offer: its hourly price over the expected hours, plus its download price over
    the volume the job downloads. vast.ai bills the bandwidth apart from the hourly price: 0.039 $ per GB on the H100 of
    composite_check-20261008-075025-3d6a, about 2.7 $ for its 70 GB of models, against 0.83 $ of rental."""
    return float(offer.get("dph_total") or 0.0) * float(hours) + float(offer.get("inet_down_cost") or 0.0) * float(download_gb)


def pick_offer(vast, gpus, num_gpus, disk_gb, filters, max_dph_per_gpu, hours=1.0, download_gb=0.0):
    """Among the offers of the first GPU type, in order of preference, that has one, the cheapest for the run
    (offer_cost: the hourly price over the expected hours, plus the download price). Returns (gpu, offer, tried)."""
    tried = []
    for gpu in gpus:
        offers = vast.search_offers(offer_query(gpu, num_gpus, disk_gb, filters, max_dph_per_gpu))
        tried.append({"gpu": gpu["name"], "offers": len(offers)})
        if offers:
            return gpu, min(offers, key=lambda o: offer_cost(o, hours, download_gb)), tried
    return None, None, tried
