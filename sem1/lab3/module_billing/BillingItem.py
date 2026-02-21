class BillingItem:
    def __init__(self, code: str, description: str, amount: float):
        self.code = code
        self.description = description
        self.amount = amount
        self.covered = False

    def mark_covered(self):
        self.covered = True

    def is_covered(self) -> bool:
        return self.covered

    def tax_amount(self, rate: float = 0.08) -> float:
        return self.amount * rate