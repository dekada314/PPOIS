class Order:
    def __init__(self, order_id: str, supplier):
        self.order_id = order_id
        self.supplier = supplier
        self.items = {}
        self.total_cost = 0.0

    def add_item(self, drug_name: str, qty: int, price: float):
        self.items[drug_name] = (qty, price)
        self.total_cost += qty * price

    def finalize(self):
        self.status = "sent"
        