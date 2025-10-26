from .worker import Worker

class LogisticsCoordinator(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Логист", 35.0)

    def plan_delivery(self, material, date) -> None:
        pass

    def track_shipment(self, tracking_id: str) -> str:
        return "В пути"