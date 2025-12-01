from tools.llm_tools import LLMTool
from tools.test_runner import TestRunner
from validators import TestGenerationValidator

class QAAgent:
    def __init__(self):
        self.llm = LLMTool()
        self.runner = TestRunner()
        self.validator = TestGenerationValidator()

    def generate_tests_for_issues(self, issues):
        results = []
        for issue in issues:
            res = self.generate_and_run(issue)
            results.append(res)
        return results

    def generate_and_run(self, issue):
        suggestion = self.llm.complete(f"generate tests for: {issue.get('summary','')}")
        if not self.validator.validate_tests(suggestion):
            return {"id": issue["id"], "status": "validation_failed"}
        run = self.runner.run_tests(suggestion.get("tests", []))
        return {"id": issue["id"], "status": run.get("status", "unknown"), "details": run.get("details")}
