import uuid
from datetime import date


class Invoice:
    def __init__(self, project, amount: float):
        self.id = str(uuid.uuid4())
        self.project = project
        self.amount = amount
        self.issued_date = date.today()
        self.due_date = date.today()
        self.paid = False

    def generate(self) -> None:
        pass

    def send_to_client(self, email: str) -> None:
        pass

    def mark_paid(self) -> None:
        self.paid = True