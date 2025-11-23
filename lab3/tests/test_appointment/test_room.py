from lab3.module_appointment.room import Room


def test_occupy_free():
    room = Room("R101", "Consultation Room", 2)
    assert room.occupied is False
    room.occupy()
    assert room.occupied is True
    room.free()
    assert room.occupied is False