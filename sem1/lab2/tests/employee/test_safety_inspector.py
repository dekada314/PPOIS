from lab2.module_employee.SafetyInspector import SafetyInspector


def test_safety_train():
    si = SafetyInspector("Ольга")
    w = type("Worker", (), {"certifications": []})
    si.train_worker(w, "ПТМ")
    assert "ПТМ" in w.certifications