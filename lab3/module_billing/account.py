class Account:
    def __init__(self, account_id: str, patient_id: str):
        self.account_id = account_id
        self.patient_id = patient_id
        self.balance = 0.0
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)
        self.balance += invoice.total()