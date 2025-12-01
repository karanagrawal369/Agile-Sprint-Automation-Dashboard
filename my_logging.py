import time
import threading

class AgentLogger:
    _lock = threading.Lock()
    _trace = []

    @classmethod
    def log(cls, agent, kind, message):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        entry = {"ts": ts, "agent": agent, "kind": kind, "message": message}
        with cls._lock:
            cls._trace.append(entry)
        print(f"[{ts}] {agent} | {kind} | {message}")

    @classmethod
    def get_trace(cls, since=0):
        with cls._lock:
            return cls._trace[since:]

    @classmethod
    def reset(cls):
        with cls._lock:
            cls._trace = []
