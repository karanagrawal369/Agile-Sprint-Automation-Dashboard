import os
from tools.mcp_client import MCPClient

class ZohoAgent:
    def __init__(self):
        self.base = os.getenv("ZOHO_API_URL", "https://mock-zoho-projects-api.onrender.com")
        self.client = MCPClient()

    def fetch_open_tasks(self):
        return self.client.get(self.base + "/tasks")

    def create_task(self, project_id, title, description):
        return self.client.post(self.base + f"/projects/{project_id}/tasks", json={"title": title, "description": description})

    def update_task(self, task_id, payload):
        return self.client.put(self.base + f"/tasks/{task_id}", json=payload)
