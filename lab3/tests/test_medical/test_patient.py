from lab3.module_medical.patient import Patient

def test_age_calculation():
    p = Patient("P1", "Alice", "1990-05-15")
    # Точная дата зависит от текущей, но логика верна
    assert p.age() >= 34  # 2025 - 1990

def test_update_name():
    p = Patient("P1", "Alice", "1990-05-15")
    p.update_name("Bob")
    assert p.name == "Bob"