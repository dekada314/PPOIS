import pytest
from associations import Assignment
from exceptions import TaskAlreadyCompletedError
from module_projects.Task import Task

from lab2.module_employee.Worker import Worker


def test_task_init():
    proj = type("Project", (), {})
    t = Task("Фундамент", proj)
    assert t.description == "Фундамент"
    assert t.status == "pending"
    assert t.assignments == []

def test_task_assign():
    proj = type("Project", (), {})
    t = Task("Фундамент", proj)
    w = Worker("Иван", "Бетонщик", 25.0)
    a = t.assign_to_worker(w, 8.0)
    assert isinstance(a, Assignment)
    assert a in w.assignments
    assert a in t.assignments

def test_task_complete_twice():
    proj = type("Project", (), {})
    t = Task("Фундамент", proj)
    t.update_status("completed")
    with pytest.raises(TaskAlreadyCompletedError):
        t.update_status("pending")