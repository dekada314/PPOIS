from lab3.module_appointment.time_slot import TimeSlot

def test_book_and_available():
    slot = TimeSlot("2025-11-15T09:00:00", 45)
    assert slot.is_available() is True
    slot.book()
    assert slot.is_available() is False