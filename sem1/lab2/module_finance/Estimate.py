import uuid


class Estimate:
    def __init__(self, project):
        self.id = str(uuid.uuid4())
        self.project = project
        self.total = 0.0
        self.items: list[dict] = []

    def add_item(self, name: str, qty: float, price: float) -> None:
        cost = qty * price
        self.items.append({"name": name, "cost": cost})
        self.total += cost

    def finalize(self) -> None:
        pass