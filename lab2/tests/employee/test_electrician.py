import pytest
from module_employee.electrician import Electrician

def test_electrician_install():
    e = Electrician("Дмитрий")
    task = type("Task", (), {"status": "pending"})
    e.install_wiring(task)
    assert task.status == "completed"