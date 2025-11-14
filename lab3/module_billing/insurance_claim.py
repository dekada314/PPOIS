class InsuranceClaim:
    def __init__(self, claim_id: str, invoice):
        self.claim_id = claim_id
        self.invoice = invoice
        self.status = "submitted"

    def approve(self, amount: float):
        self.status = f"approved: {amount}"

    def deny(self, reason: str):
        self.status = f"denied: {reason}"

    def is_approved(self) -> bool:
        return self.status.startswith("approved")

    def approved_amount(self) -> float:
        if self.is_approved():
            return float(self.status.split(":")[1].strip())
        return 0.0