import pytest
from module_employee.architect import Architect

def test_architect_init():
    a = Architect("Елена")
    assert a.name == "Елена"
    assert a.position == "Архитектор"
    assert a.hourly_rate == 50.0

def test_revise_drawing():
    a = Architect("Елена")
    assert a.revise_drawing() == None