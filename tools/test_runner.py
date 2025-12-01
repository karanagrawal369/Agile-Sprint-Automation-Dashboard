import random
import time

class TestRunner:
    def run_tests(self, tests):
        time.sleep(0.1)
        passed = random.choice([True, True, False])
        status = "passed" if passed else "failed"
        return {"status": status, "details": tests}
