class BillingService:
    def __init__(self, service_id: str, name: str, base_rate: float):
        self.service_id = service_id
        self.name = name
        self.base_rate = base_rate

    def calculate(self, quantity: int) -> float:
        return self.base_rate * quantity

    def apply_discount(self, amount: float, percent: float) -> float:
        return amount * (1 - percent)

    def tax(self, amount: float, rate: float = 0.08) -> float:
        return amount * rate

    def final_price(self, quantity: int, discount: float = 0.0, tax_rate: float = 0.08) -> float:
        subtotal = self.calculate(quantity)
        after_discount = self.apply_discount(subtotal, discount)
        return after_discount + self.tax(after_discount, tax_rate)