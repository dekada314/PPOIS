from datetime import datetime

class Payment:
    def __init__(self, payment_id: str, invoice, amount: float):
        self.payment_id = payment_id
        self.invoice = invoice
        self.amount = amount
        self.date = datetime.now()

    def apply(self):
        self.invoice.paid = True

    def overpayment(self) -> float:
        return max(0, self.amount - self.invoice.due_amount())

    def is_partial(self) -> bool:
        return self.amount < self.invoice.due_amount()