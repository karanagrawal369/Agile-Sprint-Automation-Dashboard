class TriageValidator:
    def validate_triage(self, suggestion):
        return suggestion and isinstance(suggestion.get("priority"), str) and suggestion.get("priority") in {"Low","Medium","High","Highest"}

class TestGenerationValidator:
    def validate_tests(self, suggestion):
        return suggestion and isinstance(suggestion.get("tests"), list) and len(suggestion.get("tests"))>0
