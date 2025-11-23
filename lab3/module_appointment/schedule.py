from .time_slot import TimeSlot


class Schedule:
    def __init__(self, schedule_id: str, doctor_id: str):
        self.schedule_id = schedule_id
        self.doctor_id = doctor_id
        self.slots = []
        self.active = True

    def add_slot(self, slot: TimeSlot):
        self.slots.append(slot)

    def available_slots(self):
        return [s for s in self.slots if s.is_available()]