import uuid
from exceptions import PurchaseOrderAlreadyIssuedError


class PurchaseOrder:
    def __init__(self, materials: list):
        self.id = str(uuid.uuid4())
        self.materials = materials
        self.total = sum(m.price_per_unit * m.quantity for m in materials)
        self.issued = False

    def issue(self) -> None:
        if self.issued:
            raise PurchaseOrderAlreadyIssuedError(
                f"Заказ #{self.id[:8]} уже выдан"
            )
        self.issued = True

    def receive(self) -> None:
        for m in self.materials:
            if m.storage:
                m.storage.receive_material(m, m.quantity)