class TestResult:
    def __init__(self, result_id: str, sample, test):
        self.result_id = result_id
        self.sample = sample
        self.test = test
        self.value = 0.0
        self.unit = ""

    def record(self, value: float, unit: str):
        self.value = value
        self.unit = unit
        self.test.set_result(value)