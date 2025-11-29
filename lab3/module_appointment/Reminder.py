class Reminder:
    def __init__(self, reminder_id: str, appointment, hours_before: int):
        self.reminder_id = reminder_id
        self.appointment = appointment
        self.hours_before = hours_before

    def trigger_time(self):
        from datetime import timedelta
        return self.appointment.slot.start - timedelta(hours=self.hours_before)