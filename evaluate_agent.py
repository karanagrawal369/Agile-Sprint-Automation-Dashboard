from agents.manager import AgentManager
import json

if __name__ == "__main__":
    mgr = AgentManager()
    res = mgr.run_sprint_cycle()
    print(json.dumps(res, indent=2))
