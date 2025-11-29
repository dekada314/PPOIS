import uuid

from associations import MaterialUsage
from exceptions import InsufficientMaterialError


class Storage:
    def __init__(self, location: str):
        self.id = str(uuid.uuid4())
        self.location = location
        self.materials: list = []
        self.tools: list = []

    def receive_material(self, material, qty: float) -> None:
        material.quantity += qty

    def issue_material(self, material, qty: float, task) -> bool:
        if material.quantity < qty:
            raise InsufficientMaterialError(
                f"Недостаточно {material.name}: нужно {qty}, в наличии {material.quantity}"
            )
        material.quantity -= qty
        MaterialUsage(material, task, qty)
        return True

    def check_stock(self, material_name: str) -> float:
        for m in self.materials:
            if m.name == material_name:
                return m.quantity
        return 0.0
    
    def get_total_value(self):
        return sum(m.price_per_unit * m.quantity for m in self.materials)