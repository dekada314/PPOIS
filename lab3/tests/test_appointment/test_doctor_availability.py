from lab3.module_appointment.doctor_availability import DoctorAvailability

def test_generate_slots():
    avail = DoctorAvailability("D123", "Monday", "09:00:00", "12:00:00")
    slots = avail.generate_slots(60)
    
    assert len(slots) == 3
    assert slots[0].start.isoformat() == "2025-01-01T09:00:00"
    assert slots[1].start.isoformat() == "2025-01-01T10:00:00"
    assert slots[2].start.isoformat() == "2025-01-01T11:00:00"