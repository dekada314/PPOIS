from datetime import date

import pytest
from exceptions import MilestoneNotCompletedError, ProjectAlreadyStartedError
from module_projects.milestone import Milestone
from module_projects.project import Project


def test_project_init():
    pm = type("PM", (), {})
    p = Project("ЖК", 1000000, pm)
    assert p.name == "ЖК"
    assert p.budget == 1000000
    assert p.status == "pending"
    assert p.milestones == []
    assert p.tasks == []

def test_project_start():
    pm = type("PM", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    assert p.status == "in_progress"
    assert p.start_date == date.today()

def test_project_start_twice():
    pm = type("PM", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    with pytest.raises(ProjectAlreadyStartedError):
        p.start()

def test_project_close_fail():
    pm = type("PM", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    m = Milestone("Фундамент", p)
    m.completed = False
    p.milestones.append(m)
    with pytest.raises(MilestoneNotCompletedError):
        p.close()

def test_project_close_success():
    pm = type("PM", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    m = Milestone("Фундамент", p)
    m.completed = True
    p.milestones.append(m)
    p.close()
    assert p.status == "completed"