from datetime import datetime, timedelta

from lab3.module_medical.medication import Medication
from lab3.module_medical.prescription import Prescription


def test_is_valid():
    med = Medication("Aspirin", "tab", "100mg")
    doc = type("Doc", (), {})()
    rx = Prescription(med, doc, "1/day", 30)
    assert rx.is_valid() is True
    rx.expires = datetime.now() - timedelta(days=1)
    assert rx.is_valid() is False

def test_days_left():
    med = Medication("Aspirin", "tab", "100mg")
    doc = type("Doc", (), {})()
    rx = Prescription(med, doc, "1/day", 30)
    rx.expires = datetime.now() + timedelta(days=5)
    assert rx.days_left() == 4