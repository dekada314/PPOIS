import uuid


class Material:
    def __init__(self, name: str, unit: str, price_per_unit: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.unit = unit
        self.price_per_unit = price_per_unit
        self.quantity = 0.0
        self.supplier = ""
        self.delivery_date = None
        self.storage = None
        self.approved = False

    def update_quantity(self, qty: float) -> None:
        self.quantity = qty