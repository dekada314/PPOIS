from lab3.module_appointment.appointment import Appointment
from lab3.module_appointment.time_slot import TimeSlot


def test_cancel():
    slot = TimeSlot("2025-11-15T11:00:00", 30)
    app = Appointment("APP001", "P456", slot)
    
    assert app.status == "confirmed"
    assert slot.booked is True
    
    app.cancel()
    assert app.status == "cancelled"
    assert slot.booked is False