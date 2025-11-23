from module_finance.Salary import Salary
from lab2.module_management.PayrollSpecialist import PayrollSpecialist

from lab2.module_employee.Worker import Worker


def test_payroll_process():
    ps = PayrollSpecialist("Зарплата")
    w = Worker("Иван", "Бетонщик", 25.0)
    s = Salary(w, "2025-10")
    ps.process_payroll([s])
    assert s.paid is True