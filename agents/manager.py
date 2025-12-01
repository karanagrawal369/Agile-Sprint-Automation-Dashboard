# manager.py 
from .jira_agent import JiraAgent
from .zoho_agent import ZohoAgent
from .triage_agent import TriageAgent
from .QA_agent import QAAgent
from session_service import InMemorySessionService
from my_logging import AgentLogger

class AgentManager:
    def __init__(self):
        self.jira = JiraAgent()
        self.zoho = ZohoAgent()
        self.triage = TriageAgent()
        self.qa = QAAgent()
        self.session = InMemorySessionService()
        self.last_trace_index = 0

    def run_sprint_cycle(self):
        AgentLogger.log("manager", "START", "running sprint cycle")
        issues = self.jira.fetch_open_issues()
        triage_res = self.triage.run_triage_for_issues(issues)
        qa_res = self.qa.generate_tests_for_issues(issues)
        synced = []
        for t in triage_res:
            synced.append(t)
        self.session.save("last_cycle", {"issues": issues, "triage": triage_res, "qa": qa_res})
        AgentLogger.log("manager", "END", "sprint cycle completed")
        return {"triage": triage_res, "qa": qa_res}

    def run_qa_generation(self, sprint_id):
        issues = self.jira.fetch_issues_by_sprint(sprint_id)
        res = self.qa.generate_tests_for_issues(issues)
        self.session.save("last_qa", res)
        return res

    def run_triage(self):
        issues = self.jira.fetch_open_issues()
        res = self.triage.run_triage_for_issues(issues)
        self.session.save("last_triage", res)
        return res

    def get_last_session(self):
        return self.session.load("last_cycle")
