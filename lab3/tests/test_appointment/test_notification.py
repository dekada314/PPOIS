from lab3.module_appointment.Appointment import Appointment
from lab3.module_appointment.Notification import Notification
from lab3.module_appointment.TimeSlot import TimeSlot


def test_send():
    slot = TimeSlot("2025-11-15T14:00:00", 30)
    app = Appointment("APP002", "P789", slot)
    notif = Notification("NOT001", app)
