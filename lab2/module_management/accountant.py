from module_employee.worker import Worker

class Accountant(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Бухгалтер", 42.0)
        self.invoices: list = []

    def reconcile_payments(self) -> None:
        pass

    def generate_report(self, period: str) -> str:
        return f"Отчёт за {period}"