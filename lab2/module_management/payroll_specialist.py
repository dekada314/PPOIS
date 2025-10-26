from ..module_employee.worker import Worker
from typing import List, Any


class PayrollSpecialist(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Специалист по зарплате", 35.0)

    def process_payroll(self, salaries: List[Any]) -> None:
        for s in salaries:
            s.issue_payment()