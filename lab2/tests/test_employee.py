import pytest
from lab2.module_employee.worker import Worker
from lab2.module_employee.foreman import Foreman
from lab2.exceptions import WorkerAlreadyAssignedError


def test_worker_id():
    w = Worker("Иван", "Бетонщик", 25.0)
    assert len(w.id) == 36


def test_foreman_assign():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    assignment = f.assign_task(w, task)
    assert assignment.worker == w


def test_foreman_assign_twice():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    f.assign_task(w, task)
    with pytest.raises(WorkerAlreadyAssignedError):
        f.assign_task(w, task)