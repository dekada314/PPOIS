class Refund:
    def __init__(self, refund_id: str, invoice, amount: float):
        self.refund_id = refund_id
        self.invoice = invoice
        self.amount = amount
        self.processed = False

    def process(self):
        self.processed = True
        self.invoice.paid = False

    def is_valid(self) -> bool:
        return self.amount <= self.invoice.total()