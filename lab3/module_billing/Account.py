class Account:
    def __init__(self, account_id: str, patient_id: str):
        self.account_id = account_id
        self.patient_id = patient_id
        self.balance = 0.0
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)
        self.balance += invoice.due_amount()

    def total_due(self) -> float:
        return self.balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Overpayment not allowed")
        self.balance -= amount

    def has_overdue(self, days: int = 30) -> bool:
        from datetime import datetime, timedelta
        cutoff = datetime.now() - timedelta(days=days)
        return any(inv.date < cutoff.isoformat()[:10] and not inv.paid for inv in self.invoices)