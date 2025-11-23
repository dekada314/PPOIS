from lab3.module_appointment.Calendar import Calendar


def test_add_event_and_conflicts():
    cal = Calendar()
    cal.add_event("Meeting", "2025-11-15T10:00:00")
    cal.add_event("Review", "2025-11-15T10:00:00")
    cal.add_event("Lunch", "2025-11-15T12:00:00")
    
    assert len(cal.events) == 3
    assert cal.conflicts("2025-11-15T10:00:00") == 2
    assert cal.conflicts("2025-11-15T12:00:00") == 1