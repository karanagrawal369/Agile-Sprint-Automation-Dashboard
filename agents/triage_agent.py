from tools.llm_tools import LLMTool
from validators import TriageValidator
from tools.mcp_client import MCPClient

class TriageAgent:
    def __init__(self):
        self.llm = LLMTool()
        self.validator = TriageValidator()
        self.client = MCPClient()

    def run_triage_for_issues(self, issues):
        out = []
        for issue in issues:
            res = self.process_issue(issue)
            out.append(res)
            if res.get("priority") and res["priority"] != "Unchanged":
                self.client.put(self.client.base + f"/issues/{issue['id']}", json={"priority": res["priority"]})
        return out

    def process_issue(self, issue):
        labels = issue.get("labels", []) or []
        if "blocker" in labels or issue.get("priority") in ("Critical", "High"):
            return {"id": issue["id"], "priority": "Highest", "method": "rule"}
        suggestion = self.llm.complete(f"suggest priority for: {issue.get('summary','')}")
        if self.validator.validate_triage(suggestion):
            return {"id": issue["id"], "priority": suggestion["priority"], "method": "llm"}
        return {"id": issue["id"], "priority": "Unchanged", "method": "none"}
