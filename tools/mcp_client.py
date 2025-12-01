import httpx
import os

class MCPClient:
    def __init__(self):
        self.base = ""
        self.timeout = 10
        self.headers = {}

    def get(self, url, params=None):
        r = httpx.get(url, params=params, timeout=self.timeout)
        return r.json() if r.status_code == 200 else []

    def post(self, url, json=None):
        r = httpx.post(url, json=json, timeout=self.timeout)
        try:
            return r.json()
        except Exception:
            return {"status": r.status_code}

    def put(self, url, json=None):
        r = httpx.put(url, json=json, timeout=self.timeout)
        try:
            return r.json()
        except Exception:
            return {"status": r.status_code}
