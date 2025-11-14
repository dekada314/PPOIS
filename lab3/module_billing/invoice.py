from .billing_item import BillingItem

class Invoice:
    def __init__(self, invoice_id: str, patient_id: str, date: str):
        self.invoice_id = invoice_id
        self.patient_id = patient_id
        self.date = date
        self.items = []
        self.paid = False

    def add_item(self, item: BillingItem):
        self.items.append(item)

    def total(self) -> float:
        return sum(item.amount for item in self.items)

    def total_covered(self) -> float:
        return sum(item.amount for item in self.items if item.covered)

    def due_amount(self) -> float:
        return self.total() - self.total_covered()