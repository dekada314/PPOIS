import pytest
from module_employee.foreman import Foreman
from module_employee.worker import Worker
from associations import Assignment
from exceptions import WorkerAlreadyAssignedError

def test_foreman_init():
    f = Foreman("Сергей")
    assert f.name == "Сергей"
    assert f.position == "Бригадир"
    assert f.hourly_rate == 35.0
    assert f.team == []

def test_foreman_assign_task():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    assignment = f.assign_task(w, task, 8.0)
    assert isinstance(assignment, Assignment)
    assert assignment.worker == w
    assert assignment.task == task
    assert assignment.hours_planned == 8.0
    assert assignment.status == "pending"
    assert assignment in w.assignments

def test_foreman_assign_duplicate():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    f.assign_task(w, task)
    with pytest.raises(WorkerAlreadyAssignedError):
        f.assign_task(w, task)