import pytest
from lab2.module_employee.worker import Worker
from lab2.module_employee.foreman import Foreman
from lab2.module_employee.driver import Driver
from lab2.module_employee.master import Master
from lab2.module_employee.engineer import Engineer
from lab2.module_employee.architect import Architect
from lab2.module_employee.electrician import Electrician
from lab2.module_employee.plumber import Plumber
from lab2.module_employee.crane_operator import CraneOperator
from lab2.module_employee.safety_inspector import SafetyInspector
from lab2.module_employee.logistics_coordinator import LogisticsCoordinator
from lab2.module_employee.site_supervisor import SiteSupervisor
from lab2.module_employee.quality_controller import QualityController
from lab2.module_employee.surveyor import Surveyor
from lab2.exceptions import WorkerAlreadyAssignedError
from lab2.associations import ToolAssignment
from datetime import date

def test_worker_init():
    w = Worker("Иван", "Бетонщик", 25.0)
    assert w.name == "Иван"
    assert w.position == "Бетонщик"
    assert w.hourly_rate == 25.0
    assert w.hours_worked == 0.0
    assert len(w.id) == 36
    assert len(w.certifications) == 0

def test_worker_start_shift():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.start_shift()

def test_worker_request_tool():
    w = Worker("Иван", "Бетонщик", 25.0)
    tool = type("Tool", (), {"name": "Молоток"})
    assignment = w.request_tool(tool)
    assert isinstance(assignment, ToolAssignment)
    assert assignment.worker == w
    assert assignment.issue_date == date.today()

def test_worker_log_hours():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.log_hours(8.0)
    assert w.hours_worked == 8.0

def test_foreman_init():
    f = Foreman("Сергей")
    assert f.position == "Бригадир"
    assert f.hourly_rate == 35.0
    assert len(f.team) == 0

def test_foreman_assign_task():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    assignment = f.assign_task(w, task, 8.0)
    assert assignment.hours_planned == 8.0
    assert len(w.assignments) == 1

def test_foreman_assign_twice():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {"description": "Сварка"})
    f.assign_task(w, task)
    with pytest.raises(WorkerAlreadyAssignedError):
        f.assign_task(w, task)

def test_foreman_check_progress():
    f = Foreman("Сергей")
    w = Worker("Пётр", "Сварщик", 30.0)
    task = type("Task", (), {})
    assignment = f.assign_task(w, task)
    assignment.status = "in_progress"
    progress = f.check_progress()
    assert len(progress) > 0


def test_driver_init():
    d = Driver("Михаил")
    assert d.position == "Водитель"
    assert d.hourly_rate == 28.0
    assert len(d.vehicles) == 0

def test_driver_deliver_material():
    d = Driver("Михаил")
    material = type("Material", (), {"name": "Цемент"})
    d.deliver_material(material, "Сайт")  

def test_driver_log_mileage():
    d = Driver("Михаил")
    d.log_mileage(100)
    assert d.hours_worked == 2.0 


def test_master_supervise():
    m = Master("Алексей")
    task = type("Task", (), {"description": "Строительство"})
    m.supervise_work(task)  

def test_master_approve_quality():
    m = Master("Алексей")
    task = type("Task", (), {"status": "pending"})
    m.approve_quality(task)
    assert task.status == "completed"


def test_engineer_design():
    e = Engineer("Виктор")
    project = type("Project", (), {"name": "Мост"})
    e.design_structure(project)  

def test_engineer_validate():
    e = Engineer("Виктор")
    blueprint = "Чертеж v1"
    assert e.validate_plan(blueprint) is True


def test_architect_create_blueprint():
    a = Architect("Елена")
    project = type("Project", (), {"name": "Дом"})
    blueprint = a.create_blueprint(project)
    assert "Чертеж для Дом" in blueprint

def test_architect_revise():
    a = Architect("Елена")
    blueprint = "Чертеж v1"
    changes = "Добавить окно"
    a.revise_drawing(blueprint, changes)  

# Electrician
def test_electrician_install():
    el = Electrician("Дмитрий")
    task = type("Task", (), {"status": "pending"})
    el.install_wiring(task)
    assert task.status == "completed"

def test_electrician_test():
    el = Electrician("Дмитрий")
    assert el.test_circuit() == "OK"

def test_plumber_install():
    p = Plumber("Николай")
    task = type("Task", (), {"status": "pending"})
    p.install_pipes(task)
    assert task.status == "completed"

def test_plumber_fix():
    p = Plumber("Николай")
    p.fix_leak()  

def test_crane_lift():
    co = CraneOperator("Степан")
    material = type("Material", (), {"name": "Балка"})
    co.lift_material(material, 10.0)  

def test_crane_park():
    co = CraneOperator("Степан")
    co.park_crane()  

def test_inspector_conduct():
    si = SafetyInspector("Ольга")
    project = type("Project", (), {"name": "Сайт 1"})
    si.conduct_inspection(project)
    assert len(si.inspections) == 1

def test_inspector_issue_violation():
    si = SafetyInspector("Ольга")
    w = Worker("Иван", "Бетонщик", 25.0)
    si.issue_violation(w, "Нарушение ПДД")  

def test_inspector_train():
    si = SafetyInspector("Ольга")
    w = Worker("Иван", "Бетонщик", 25.0)
    si.train_worker(w, "Безопасность")
    assert "Безопасность" in w.certifications

def test_logistics_plan():
    lc = LogisticsCoordinator("Мария")
    material = type("Material", (), {"name": "Кирпич"})
    lc.plan_delivery(material, date.today())  

def test_logistics_track():
    lc = LogisticsCoordinator("Мария")
    assert lc.track_shipment("TRK123") == "В пути"

def test_site_briefing():
    ss = SiteSupervisor("Андрей")
    ss.daily_briefing()  

def test_site_close():
    ss = SiteSupervisor("Андрей")
    ss.close_site()  

def test_quality_test():
    qc = QualityController("Татьяна")
    assert "Прочность: 35 МПа" in qc.test_concrete("Проба 1")

def test_quality_approve():
    qc = QualityController("Татьяна")
    material = type("Material", (), {"approved": False})
    qc.approve_material(material)
    assert material.approved is True

def test_surveyor_measure():
    s = Surveyor("Константин")
    assert s.measure_elevation("Точка 1") == 125.4

def test_surveyor_mark():
    s = Surveyor("Константин")
    project = type("Project", (), {"name": "Фундамент"})
    s.mark_foundation(project)  