from lab3.module_appointment.appointment import Appointment
from lab3.module_appointment.notification import Notification
from lab3.module_appointment.time_slot import TimeSlot


def test_send():
    slot = TimeSlot("2025-11-15T14:00:00", 30)
    app = Appointment("APP002", "P789", slot)
    notif = Notification("NOT001", app)
