
import pytest
from lab2.module_projects.project_manager import ProjectManager
from lab2.module_projects.project import Project
from lab2.module_projects.task import Task
from lab2.module_projects.milestone import Milestone
from lab2.module_projects.timeline import Timeline
from lab2.module_projects.risk_assessment import RiskAssessment
from lab2.module_projects.change_request import ChangeRequest
from lab2.module_projects.progress_report import ProgressReport
from lab2.module_finance.budget import Budget
from lab2.module_finance.estimate import Estimate
from lab2.exceptions import (
    ProjectAlreadyStartedError, TaskAlreadyCompletedError,
    MilestoneNotCompletedError
)
from datetime import date

def test_project_manager_init():
    pm = ProjectManager("Менеджер")
    assert pm.position == "Менеджер проекта"
    assert len(pm.projects) == 0

def test_project_manager_create():
    pm = ProjectManager("Менеджер")
    p = pm.create_project("ЖК", 1000000)
    assert isinstance(p, Project)
    assert len(pm.projects) == 1

def test_project_manager_track():
    pm = ProjectManager("Менеджер")
    p = type("Project", (), {"progress": lambda: 50.0})
    assert pm.track_progress(p) == 50.0

def test_project_init():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    assert p.name == "ЖК"
    assert p.budget == 1000000
    assert p.status == "pending"
    assert isinstance(p.budget_obj, Budget)
    assert isinstance(p.estimate, Estimate)

def test_project_start():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    assert p.status == "in_progress"
    assert p.start_date == date.today()

def test_project_close():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    m = Milestone("Этап 1", p)
    m.completed = True
    p.milestones = [m]
    p.close()
    assert p.status == "completed"
    assert p.end_date == date.today()

def test_project_progress():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    t1 = Task("Задача 1", p)
    t2 = Task("Задача 2", p)
    t1.status = "completed"
    p.tasks = [t1, t2]
    assert p.progress() == 50.0

def test_project_start_twice():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    with pytest.raises(ProjectAlreadyStartedError):
        p.start()

def test_project_close_fail():
    pm = type("ProjectManager", (), {})
    p = Project("ЖК", 1000000, pm)
    p.start()
    m = Milestone("Этап 1", p)
    p.milestones = [m]
    with pytest.raises(MilestoneNotCompletedError):
        p.close()

def test_task_init():
    p = type("Project", (), {})
    t = Task("Фундамент", p)
    assert t.description == "Фундамент"
    assert t.status == "pending"
    assert t.priority == "medium"

def test_task_assign():
    p = type("Project", (), {})
    t = Task("Фундамент", p)
    w = type("Worker", (), {"assignments": []})
    assignment = t.assign_to_worker(w, 8.0)
    assert len(t.assignments) == 1
    assert len(w.assignments) == 1

def test_task_set_deadline():
    p = type("Project", (), {})
    t = Task("Фундамент", p)
    t.set_deadline(7) 

def test_task_update_status():
    p = type("Project", (), {})
    t = Task("Фундамент", p)
    t.update_status("in_progress")
    assert t.status == "in_progress"

def test_task_completed_fail():
    p = type("Project", (), {})
    t = Task("Фундамент", p)
    t.update_status("completed")
    with pytest.raises(TaskAlreadyCompletedError):
        t.update_status("pending")

def test_milestone_init():
    p = type("Project", (), {})
    m = Milestone("Фундамент", p)
    assert m.name == "Фундамент"
    assert m.completed is False
    assert len(m.tasks) == 0

def test_milestone_add_task():
    p = type("Project", (), {})
    m = Milestone("Фундамент", p)
    t = type("Task", (), {"milestone": None})
    m.add_task(t)
    assert len(m.tasks) == 1
    assert t.milestone == m

def test_milestone_complete():
    p = type("Project", (), {})
    m = Milestone("Фундамент", p)
    t1 = type("Task", (), {"status": "completed"})
    t2 = type("Task", (), {"status": "completed"})
    m.tasks = [t1, t2]
    assert m.complete() is True
    assert m.completed is True

def test_milestone_incomplete():
    p = type("Project", (), {})
    m = Milestone("Фундамент", p)
    t1 = type("Task", (), {"status": "pending"})
    m.tasks = [t1]
    assert m.complete() is False

def test_timeline_init():
    p = type("Project", (), {})
    tl = Timeline(p)
    assert len(tl.milestones) == 0

def test_timeline_gantt():
    p = type("Project", (), {})
    tl = Timeline(p)
    assert tl.generate_gantt() == "Gantt chart generated"

def test_risk_init():
    p = type("Project", (), {})
    ra = RiskAssessment(p)
    assert len(ra.risks) == 0

def test_risk_identify():
    p = type("Project", (), {})
    ra = RiskAssessment(p)
    ra.identify_risk("Задержка", 0.5, 10)
    assert len(ra.risks) == 1
    assert ra.risks[0]["desc"] == "Задержка"

def test_risk_mitigate():
    p = type("Project", (), {})
    ra = RiskAssessment(p)
    ra.mitigate(0) 

def test_change_init():
    p = type("Project", (), {})
    cr = ChangeRequest(p, "Изменить план")
    assert cr.description == "Изменить план"
    assert cr.approved is False

def test_change_submit():
    p = type("Project", (), {})
    cr = ChangeRequest(p, "Изменить план")
    cr.submit() 

def test_change_approve():
    p = type("Project", (), {})
    cr = ChangeRequest(p, "Изменить план")
    cr.approve()
    assert cr.approved is True

def test_progress_init():
    t = type("Task", (), {})
    pr = ProgressReport(t)
    assert pr.percent_complete == 0

def test_progress_generate():
    t = type("Task", (), {})
    pr = ProgressReport(t)
    assert pr.generate() == 75 
    assert pr.percent_complete == 75