from typing import Dict

class Inventory:
    def __init__(self):
        self.stock: Dict[str, int] = {}
        self.min_level = 10

    def add(self, med_name: str, qty: int):
        self.stock[med_name] = self.stock.get(med_name, 0) + qty

    def reduce(self, med_name: str, qty: int):
        if self.stock.get(med_name, 0) < qty:
            raise ValueError("Insufficient stock")
        self.stock[med_name] -= qty

    def has_stock(self, med_name: str, qty: int) -> bool:
        return self.stock.get(med_name, 0) >= qty

    def low_stock_items(self):
        return [k for k, v in self.stock.items() if v < self.min_level]