from datetime import datetime


class Appointment:
    def __init__(self, patient, doctor, time_str: str, reason: str):
        self.app_id = f"A{abs(hash(time_str)) % 10000:04d}"
        self.patient = patient
        self.doctor = doctor
        self.time = datetime.fromisoformat(time_str)
        self.reason = reason
        self.status = "scheduled"

    def cancel(self):
        self.status = "cancelled"

    def reschedule(self, new_time: str):
        self.time = datetime.fromisoformat(new_time)