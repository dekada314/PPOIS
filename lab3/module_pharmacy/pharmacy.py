from .Inventory import Inventory


class Pharmacy:
    def __init__(self, pharm_id: str, name: str, address: str):
        self.pharm_id = pharm_id
        self.name = name
        self.address = address
        self.inventory = Inventory()

    def dispense(self, rx, qty: int):
        med_name = rx.medication.name
        if not self.inventory.has_stock(med_name, qty):
            raise ValueError("Not enough stock")
        self.inventory.reduce(med_name, qty)

    def restock(self, med_name: str, qty: int):
        self.inventory.add(med_name, qty)