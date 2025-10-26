from .worker import Worker

class CraneOperator(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Крановщик", 38.0)
        self.crane = None

    def lift_material(self, material, height: float) -> None:
        pass

    def park_crane(self) -> None:
        pass