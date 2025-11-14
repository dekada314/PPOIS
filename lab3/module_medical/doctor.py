# lab3/module_medical/doctor.py
class Doctor:
    def __init__(self, doctor_id: str, name: str, specialty: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def schedule(self, appointment):
        if any(a.time == appointment.time for a in self.appointments):
            raise ValueError("Time conflict")
        self.appointments.append(appointment)

    def cancel_by_id(self, app_id: str):
        for a in self.appointments:
            if a.app_id == app_id:
                a.status = "cancelled"
                break