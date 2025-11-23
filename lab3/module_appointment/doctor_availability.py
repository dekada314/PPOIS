from datetime import datetime, timedelta

from .time_slot import TimeSlot


class DoctorAvailability:
    def __init__(self, doctor_id: str, day: str, start: str, end: str):
        self.doctor_id = doctor_id
        self.day = day
        self.start = start
        self.end = end

    def generate_slots(self, interval: int):
        slots = []
        current = datetime.fromisoformat(f"2025-01-01 {self.start}")
        end_time = datetime.fromisoformat(f"2025-01-01 {self.end}")
        while current + timedelta(minutes=interval) <= end_time:
            slots.append(TimeSlot(current.isoformat(), interval))
            current += timedelta(minutes=interval)
        return slots