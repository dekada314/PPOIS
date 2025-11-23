class DiscountPolicy:
    def __init__(self, policy_id: str, name: str, percent: float):
        self.policy_id = policy_id
        self.name = name
        self.percent = percent

    def apply(self, amount: float) -> float:
        return amount * (1 - self.percent)