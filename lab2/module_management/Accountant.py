from lab2.module_employee.Worker import Worker


class Accountant(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Бухгалтер", 42.0)
        self.invoices: list = []

    def reconcile_payments(self) -> None:
        pass

    def generate_report(self, period: str) -> str:
        return f"Отчёт за {period}"