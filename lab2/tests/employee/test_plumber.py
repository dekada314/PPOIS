import pytest
from module_employee.plumber import Plumber

def test_plumber_install():
    p = Plumber("Николай")
    task = type("Task", (), {"status": "pending"})
    p.install_pipes(task)
    assert task.status == "completed"