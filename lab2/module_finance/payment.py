from datetime import date
import uuid


class Payment:
    def __init__(self, invoice, amount: float):
        self.id = str(uuid.uuid4())
        self.invoice = invoice
        self.amount = amount
        self.date = date.today()
        self.method = "bank_transfer"

    def process(self) -> bool:
        if self.invoice.amount <= self.amount:
            self.invoice.mark_paid()
            return True
        return False