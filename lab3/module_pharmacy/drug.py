class Drug:
    def __init__(self, name: str, manufacturer: str, price: float):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.generic = False

    def mark_generic(self):
        self.generic = True