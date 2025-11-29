class Appointment:
    def __init__(self, app_id: str, patient_id: str, slot):
        self.app_id = app_id
        self.patient_id = patient_id
        self.slot = slot
        self.status = "confirmed"
        self.slot.book()

    def cancel(self):
        self.status = "cancelled"
        self.slot.booked = False