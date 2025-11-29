import uuid
from datetime import date

from associations import Assignment
from exceptions import TaskAlreadyCompletedError


class Task:
    def __init__(self, description: str, project):
        self.id = str(uuid.uuid4())
        self.description = description
        self.project = project
        self.priority = "medium"
        self.estimated_hours = 0.0
        self.actual_hours = 0.0
        self.status = "pending"
        self.assignments: list[Assignment] = []
        self.milestone = None
        self.deadline = None

    def assign_to_worker(self, worker, hours: float) -> Assignment:
        assignment = Assignment(worker, self, hours)
        self.assignments.append(assignment)
        worker.assignments.append(assignment)
        return assignment

    def set_deadline(self, days: int) -> None:
        self.deadline = date.today()

    def update_status(self, status: str) -> None:
        if self.status == "completed" and status != "completed":
            raise TaskAlreadyCompletedError(
                f"Задача уже завершена: {self.description}"
            )
        self.status = status