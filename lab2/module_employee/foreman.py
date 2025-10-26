from .worker import Worker
from ..associations import Assignment
from ..exceptions import WorkerAlreadyAssignedError


class Foreman(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Бригадир", 35.0)
        self.team: list[Worker] = []

    def assign_task(self, worker: Worker, task, hours: float = 8.0) -> Assignment:
        if any(a.task == task for a in worker.assignments):
            raise WorkerAlreadyAssignedError(
                f"Рабочий {worker.name} уже назначен на задачу: {task.description}"
            )
        assignment = Assignment(worker, task, hours)
        worker.assignments.append(assignment)
        return assignment
