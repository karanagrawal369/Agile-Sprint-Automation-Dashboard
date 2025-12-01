import time

class InMemorySessionService:
    def __init__(self):
        self.store = {}

    def save(self, key, value):
        self.store[key] = {"value": value, "ts": time.time()}

    def load(self, key):
        v = self.store.get(key)
        return v["value"] if v else None

class MemoryBank:
    def __init__(self):
        self.db = {}

    def add(self, key, value):
        self.db.setdefault(key, []).append({"value": value, "ts": time.time()})

    def query(self, key):
        return self.db.get(key, [])
