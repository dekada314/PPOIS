class RefillRequest:
    def __init__(self, patient, rx_id: str):
        self.patient = patient
        self.rx_id = rx_id
        self.status = "pending"

    def approve(self):
        self.status = "approved"

    def reject(self, reason: str):
        self.status = f"rejected: {reason}"