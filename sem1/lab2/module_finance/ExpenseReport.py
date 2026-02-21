import uuid


class ExpenseReport:
    def __init__(self, worker, items: list[dict]):
        self.id = str(uuid.uuid4())
        self.worker = worker
        self.items = items
        self.total = sum(i['amount'] for i in items)
        self.approved = False

    def submit(self) -> None:
        pass

    def approve(self) -> None:
        self.approved = True