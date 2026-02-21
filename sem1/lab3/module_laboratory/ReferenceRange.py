class ReferenceRange:
    def __init__(self, test_code: str, age_group: str, low: float, high: float):
        self.test_code = test_code
        self.age_group = age_group
        self.low = low
        self.high = high

    def validate(self, value: float) -> bool:
        return self.low <= value <= self.high