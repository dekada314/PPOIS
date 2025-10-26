import pytest
from module_employee.safety_inspector import SafetyInspector

def test_safety_train():
    si = SafetyInspector("Ольга")
    w = type("Worker", (), {"certifications": []})
    si.train_worker(w, "ПТМ")
    assert "ПТМ" in w.certifications