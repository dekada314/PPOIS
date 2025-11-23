from lab3.module_medical.Patient import Patient


def test_age_calculation():
    p = Patient("P1", "Alice", "1990-05-15")
    assert p.age() >= 34  # 2025 - 1990

def test_update_name():
    p = Patient("P1", "Alice", "1990-05-15")
    p.update_name("Bob")
    assert p.name == "Bob"