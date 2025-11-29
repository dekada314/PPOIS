from datetime import date

from .MedicalRecord import MedicalRecord


class Patient:
    def __init__(self, patient_id: str, name: str, birth_date: str):
        self.patient_id = patient_id
        self.name = name
        self.birth_date = date.fromisoformat(birth_date)
        self.record = MedicalRecord()

    def age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def update_name(self, new_name: str):
        self.name = new_name