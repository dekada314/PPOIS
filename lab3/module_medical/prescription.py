from datetime import datetime, timedelta

from .medication import Medication


class Prescription:
    def __init__(self, med: Medication, doctor, dosage: str, days: int):
        self.rx_id = f"RX{abs(hash(dosage)) % 10000:04d}"
        self.medication = med
        self.doctor = doctor
        self.dosage = dosage
        self.days = days
        self.issued = datetime.now()
        self.expires = self.issued + timedelta(days=days)

    def is_valid(self) -> bool:
        return datetime.now() < self.expires

    def days_left(self) -> int:
        return max(0, (self.expires - datetime.now()).days)