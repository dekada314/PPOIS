class Test:
    def __init__(self, test_code: str, name: str, normal_range: str):
        self.test_code = test_code
        self.name = name
        self.normal_range = normal_range
        self.result = None

    def set_result(self, value: float):
        self.result = value

    def is_abnormal(self) -> bool:
        if self.result is None:
            return False
        low, high = map(float, self.normal_range.split('-'))
        return not (low <= self.result <= high)