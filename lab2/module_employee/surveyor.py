from .worker import Worker


class Surveyor(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Геодезист", 40.0)

    def measure_elevation(self, point: str) -> float:
        return 125.4

    def mark_foundation(self, project) -> None:
        pass