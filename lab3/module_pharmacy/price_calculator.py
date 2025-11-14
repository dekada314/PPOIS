class PriceCalculator:
    def __init__(self):
        self.tax_rate = 0.08
        self.insurance_discount = 0.2

    def with_insurance(self, base_price: float) -> float:
        return (base_price * (1 - self.insurance_discount)) * (1 + self.tax_rate)

    def without_insurance(self, base_price: float) -> float:
        return base_price * (1 + self.tax_rate)

    def bulk_price(self, base_price: float, qty: int) -> float:
        discount = 0.1 if qty >= 100 else 0.0
        return base_price * (1 - discount) * qty