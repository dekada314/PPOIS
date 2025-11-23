from lab3.module_appointment.appointment import Appointment
from lab3.module_appointment.booking import Booking
from lab3.module_appointment.room import Room
from lab3.module_appointment.time_slot import TimeSlot


def test_release():
    room = Room("R102", "Exam Room", 1)
    slot = TimeSlot("2025-11-15T15:00:00", 30)
    app = Appointment("APP003", "P101", slot)
    booking = Booking("BKG001", app, room)
    
    assert room.occupied is True
    booking.release()
    assert room.occupied is False