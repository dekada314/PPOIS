from datetime import timedelta

from lab3.module_appointment.Appointment import Appointment
from lab3.module_appointment.Reminder import Reminder
from lab3.module_appointment.TimeSlot import TimeSlot


def test_trigger_time():
    slot = TimeSlot("2025-11-15T16:00:00", 30)
    app = Appointment("APP004", "P202", slot)
    reminder = Reminder("REM001", app, 2)
    
    expected = slot.start - timedelta(hours=2)
    assert reminder.trigger_time() == expected