from module_finance.salary import Salary

from lab2.module_employee.Worker import Worker


def test_salary_init():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.hours_worked = 160
    s = Salary(w, "2025-10")
    assert s.worker == w
    assert s.month == "2025-10"
    assert s.base == 4000.0
    assert s.bonus == 0.0
    assert s.deductions == 0.0
    assert s.paid is False

def test_salary_calculate():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.hours_worked = 160
    s = Salary(w, "2025-10")
    s.bonus = 500
    s.deductions = 200
    assert s.calculate() == 4300.0

def test_salary_issue():
    w = Worker("Иван", "Бетонщик", 25.0)
    s = Salary(w, "2025-10")
    s.issue_payment()
    assert s.paid is True