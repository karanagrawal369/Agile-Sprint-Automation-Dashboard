import os
from tools.mcp_client import MCPClient

class JiraAgent:
    def __init__(self):
        self.base = os.getenv("JIRA_API_URL", "https://mock-jira-api.onrender.com")
        self.client = MCPClient()

    def fetch_open_issues(self):
        return self.client.get(self.base + "/issues")

    def fetch_issues_by_sprint(self, sprint_id):
        return self.client.get(self.base + f"/issues?sprint={sprint_id}")

    def update_issue(self, issue_key, payload):
        return self.client.put(self.base + f"/issues/{issue_key}", json=payload)
