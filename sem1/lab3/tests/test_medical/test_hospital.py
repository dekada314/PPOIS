from lab3.module_medical.Hospital import Hospital


def test_admit_discharge():
    h = Hospital("City", "NY", 1)
    h.admit()
    h.discharge()
    assert h.occupied == 0