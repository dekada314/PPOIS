import pytest
from module_projects.milestone import Milestone

def test_milestone_init():
    proj = type("Project", (), {})
    m = Milestone("Этап 1", proj)
    assert m.name == "Этап 1"
    assert m.completed is False
    assert m.tasks == []

def test_milestone_complete():
    proj = type("Project", (), {})
    m = Milestone("Этап 1", proj)
    t1 = type("Task", (), {"status": "completed"})
    t2 = type("Task", (), {"status": "completed"})
    m.tasks = [t1, t2]
    assert m.complete() is True
    assert m.completed is True