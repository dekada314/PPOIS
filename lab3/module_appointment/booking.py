from .room import Room
from .appointment import Appointment
class Booking:
    def __init__(self, booking_id: str, appointment, room):
        self.booking_id = booking_id
        self.appointment = appointment
        self.room = room
        self.room.occupy()

    def release(self):
        self.room.free()