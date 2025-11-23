from lab3.module_medical.appointment import Appointment


def test_reschedule():
    p = type("P", (), {})()
    d = type("D", (), {})()
    app = Appointment(p, d, "2025-11-20T10:00:00", "Checkup")
    app.reschedule("2025-11-21T11:00:00")
    assert app.time.isoformat() == "2025-11-21T11:00:00"
    assert app.status == "scheduled"  

def test_cancel():
    p = type("P", (), {})()
    d = type("D", (), {})()
    app = Appointment(p, d, "2025-11-20T10:00:00", "Checkup")
    app.cancel()
    assert app.status == "cancelled"