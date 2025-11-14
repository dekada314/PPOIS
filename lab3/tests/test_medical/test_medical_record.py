from lab3.module_medical.medical_record import MedicalRecord
from lab3.module_medical.diagnosis import Diagnosis

def test_add_diagnosis():
    rec = MedicalRecord()
    doc = type("Doc", (), {"name": "Dr. X"})()
    diag = Diagnosis("A00", "Cholera", doc)
    rec.add_diagnosis(diag)
    assert rec.visit_count == 1
    assert len(rec.diagnoses) == 1

def test_add_prescription():
    rec = MedicalRecord()
    rx = type("Rx", (), {"is_valid": lambda: True})()
    rec.add_prescription(rx)
    assert len(rec.prescriptions) == 1