class QualityControl:
    def __init__(self):
        self.passed = True
        self.last_check = None

    def run_check(self):
        self.passed = True
        self.last_check = "OK"

    def fail(self, reason: str):
        self.passed = False
        self.last_check = reason