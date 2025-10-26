import uuid

class Salary:
    def __init__(self, worker, month: str):
        self.id = str(uuid.uuid4())
        self.worker = worker
        self.month = month
        self.base = worker.hourly_rate * worker.hours_worked
        self.bonus = 0.0
        self.deductions = 0.0
        self.paid = False

    def calculate(self) -> float:
        self.total = self.base + self.bonus - self.deductions
        return self.total

    def issue_payment(self) -> None:
        self.paid = True

    def deduct_tax(self, percent: float) -> None:
        self.deductions += self.base * percent / 100