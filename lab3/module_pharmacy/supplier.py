class Supplier:
    def __init__(self, sup_id: str, name: str, contact: str):
        self.sup_id = sup_id
        self.name = name
        self.contact = contact
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)