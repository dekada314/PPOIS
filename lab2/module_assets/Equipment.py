import uuid
from datetime import date


class Equipment:
    def __init__(self, name: str, model: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.model = model
        self.purchase_date = date.today()
        self.last_maintenance = None
        self.status = "operational"
        self.projects: list = []

    def schedule_maintenance(self, date: date) -> None:
        self.last_maintenance = date

    def register_usage(self, hours: float) -> None:
        print('Пользователь зарегистрирован')

    def decommission(self) -> None:
        self.status = "decommissioned"