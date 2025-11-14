from lab3.module_medical.doctor import Doctor

def test_schedule_conflict():
    doc = Doctor("D1", "Dr. Smith", "Cardio")
    app1 = type("App", (), {"time": "10:00"})()
    app2 = type("App", (), {"time": "10:00"})()
    doc.schedule(app1)


def test_cancel_by_id():
    doc = Doctor("D1", "Dr. Smith", "Cardio")
    app = type("App", (), {"app_id": "A1234", "status": "scheduled"})()
    doc.appointments.append(app)
    doc.cancel_by_id("A1234")
    assert app.status == "cancelled"