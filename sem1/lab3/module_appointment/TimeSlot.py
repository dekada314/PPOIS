from datetime import datetime, timedelta


class TimeSlot:
    def __init__(self, start: str, duration_min: int):
        self.start = datetime.fromisoformat(start)
        self.duration = duration_min
        self.booked = False

    def book(self):
        self.booked = True

    def is_available(self) -> bool:
        return not self.booked

    def end_time(self) -> datetime:
        return self.start + timedelta(minutes=self.duration)