from module_management.hr_manager import HRManager
from module_employee.worker import Worker

def test_hr_init():
    hr = HRManager("HR")
    assert hr.name == "HR"
    assert hr.employees == []

def test_hr_hire_fire():
    hr = HRManager("HR")
    w = Worker("Иван", "Бетонщик", 25.0)
    hr.hire_employee(w)
    assert w in hr.employees
    hr.fire_employee(w)
    assert w not in hr.employees