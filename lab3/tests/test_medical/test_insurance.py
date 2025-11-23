from lab3.module_medical.insurance import Insurance


def test_add_patient():
    ins = Insurance("POL123", "MediCare")
    p = type("P", (), {})()
    ins.add_patient(p)
    assert p in ins.patients

def test_coverage():
    ins = Insurance("POL123", "MediCare")
    assert ins.coverage("medication") == 0.8
    assert ins.coverage("consult") == 0.5