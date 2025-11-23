import uuid

from lab2.module_employee.Worker import Worker


class HRManager:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.employees: list[Worker] = []

    def hire_employee(self, worker: Worker) -> None:
        self.employees.append(worker)

    def fire_employee(self, worker: Worker) -> None:
        self.employees.remove(worker)

    def conduct_interview(self, candidate: str) -> str:
        return "Принят"