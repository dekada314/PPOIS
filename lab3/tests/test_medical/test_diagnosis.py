from lab3.module_medical.diagnosis import Diagnosis

def test_is_chronic():
    doc = type("Doc", (), {})()
    diag1 = Diagnosis("E11.9", "Diabetes", doc)
    diag2 = Diagnosis("A00", "Cholera", doc)
    assert diag1.is_chronic() is True
    assert diag2.is_chronic() is False

def test_update():
    doc = type("Doc", (), {})()
    diag = Diagnosis("I10", "Hypertension", doc)
    diag.update("Essential hypertension")
    assert diag.description == "Essential hypertension"