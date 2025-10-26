
import pytest
from lab2.module_management.chief_manager import ChiefManager
from lab2.module_management.general_manager import GeneralManager
from lab2.module_management.hr_manager import HRManager
from lab2.module_management.storage import Storage
from lab2.module_management.procurement_manager import ProcurementManager
from lab2.module_management.fleet_manager import FleetManager
from lab2.module_management.it_manager import ITManager
from lab2.module_management.legal_advisor import LegalAdvisor
from lab2.module_management.accountant import Accountant
from lab2.module_management.payroll_specialist import PayrollSpecialist
from lab2.exceptions import VehicleInUseError
from lab2.module_employee.worker import Worker
from lab2.module_finance.purchase_order import PurchaseOrder
from lab2.module_assets.vehicle import Vehicle

from lab2.exceptions import InsufficientMaterialError


def test_chief_init():
    cm = ChiefManager("Директор")
    assert len(cm.departments) == 0

def test_chief_approve_budget():
    cm = ChiefManager("Директор")
    b = type("Budget", (), {"approved": False})
    cm.approve_budget(b)
    assert b.approved is True

def test_chief_strategic():
    cm = ChiefManager("Директор")
    cm.strategic_planning()  


def test_general_init():
    gm = GeneralManager("Гендиректор")
    assert gm.chief is None

def test_general_report():
    gm = GeneralManager("Гендиректор")
    gm.report_to_board()  


def test_hr_init():
    hr = HRManager("HR")
    assert len(hr.employees) == 0

def test_hr_hire():
    hr = HRManager("HR")
    w = Worker("Иван", "Бетонщик", 25.0)
    hr.hire_employee(w)
    assert len(hr.employees) == 1

def test_hr_fire():
    hr = HRManager("HR")
    w = Worker("Иван", "Бетонщик", 25.0)
    hr.hire_employee(w)
    hr.fire_employee(w)
    assert len(hr.employees) == 0

def test_hr_interview():
    hr = HRManager("HR")
    assert hr.conduct_interview("Кандидат") == "Принят"


def test_storage_init():
    s = Storage("Склад 1")
    assert len(s.materials) == 0
    assert len(s.tools) == 0

def test_storage_receive():
    s = Storage("Склад 1")
    m = type("Material", (), {"quantity": 0})
    s.receive_material(m, 100)
    assert m.quantity == 100

def test_storage_check_stock():
    s = Storage("Склад 1")
    m1 = type("Material", (), {"name": "Цемент", "quantity": 50})
    m2 = type("Material", (), {"name": "Кирпич", "quantity": 100})
    s.materials = [m1, m2]
    assert s.check_stock("Цемент") == 50
    assert s.check_stock("Неизвестно") == 0.0

def test_storage_issue_success():
    s = Storage("Склад 1")
    m = type("Material", (), {"name": "Цемент", "quantity": 100})
    t = type("Task", (), {})
    s.materials.append(m)
    assert s.issue_material(m, 30, t) is True
    assert m.quantity == 70

def test_storage_issue_fail():
    s = Storage("Склад 1")
    m = type("Material", (), {"name": "Цемент", "quantity": 10})
    t = type("Task", (), {})
    s.materials.append(m)
    with pytest.raises(InsufficientMaterialError):
        s.issue_material(m, 20, t)


def test_procurement_init():
    pm = ProcurementManager("Закупки")
    assert len(pm.orders) == 0

def test_procurement_create_order():
    pm = ProcurementManager("Закупки")
    m = type("Material", (), {"price_per_unit": 100, "quantity": 5})
    order = pm.create_order([m])
    assert isinstance(order, PurchaseOrder)
    assert len(pm.orders) == 1

def test_procurement_track():
    pm = ProcurementManager("Закупки")
    assert pm.track_order("ORD123") == "В пути"


def test_fleet_init():
    fm = FleetManager("Автопарк")
    assert len(fm.vehicles) == 0

def test_fleet_schedule():
    fm = FleetManager("Автопарк")
    v = type("Vehicle", (), {"model": "Газель"})
    fm.schedule_maintenance(v)  

def test_fleet_assign_success():
    fm = FleetManager("Автопарк")
    d = Worker("Иван", "Водитель", 28.0)  
    v = Vehicle("Газель", "A123BC")
    fm.assign_vehicle(d, v)
    assert len(v.drivers) == 1
    assert len(d.vehicles) == 1

def test_fleet_assign_fail():
    fm = FleetManager("Автопарк")
    d1 = Worker("Иван", "Водитель", 28.0)
    d2 = Worker("Пётр", "Водитель", 28.0)
    v = Vehicle("Газель", "A123BC")
    fm.assign_vehicle(d1, v)
    with pytest.raises(VehicleInUseError):
        fm.assign_vehicle(d2, v)


def test_it_deploy():
    it = ITManager("IT")
    it.deploy_software()  

def test_it_backup():
    it = ITManager("IT")
    it.backup_data()  


def test_legal_review():
    la = LegalAdvisor("Юрист")
    c = type("Contract", (), {})
    assert la.review_contract(c) == "Одобрено"

def test_legal_dispute():
    la = LegalAdvisor("Юрист")
    la.handle_dispute()  


def test_accountant_init():
    a = Accountant("Бухгалтер")
    assert len(a.invoices) == 0

def test_accountant_reconcile():
    a = Accountant("Бухгалтер")
    a.reconcile_payments()  

def test_accountant_report():
    a = Accountant("Бухгалтер")
    assert "Отчёт за 2025" in a.generate_report("2025")


def test_payroll_process():
    ps = PayrollSpecialist("Зарплата")
    s1 = type("Salary", (), {"issue_payment": lambda: setattr(s1, 'paid', True)})
    s2 = type("Salary", (), {"issue_payment": lambda: setattr(s2, 'paid', True)})
    ps.process_payroll([s1, s2])
    assert s1.paid is True
    assert s2.paid is True