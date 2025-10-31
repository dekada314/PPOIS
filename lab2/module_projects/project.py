from datetime import date
import uuid
from typing import List, Any
from module_finance.budget import Budget
from module_finance.estimate import Estimate
from exceptions import ProjectAlreadyStartedError, MilestoneNotCompletedError


class Project:
    def __init__(self, name: str, budget: float, manager: Any):
        self.id = str(uuid.uuid4())
        self.name = name
        self.budget = budget
        self.manager = manager
        self.start_date = None
        self.end_date = None
        self.status = "pending"
        self.tasks: List[Any] = []
        self.milestones: List[Any] = []
        self.budget_obj = Budget(self)
        self.contract = None
        self.estimate = Estimate(self)

    def start(self) -> None:
        if self.status == "in_progress":
            raise ProjectAlreadyStartedError(
                f"Проект {self.name} уже запущен"
            )
        self.start_date = date.today()
        self.status = "in_progress"

    def close(self) -> None:
        for milestone in self.milestones:
            if not getattr(milestone, "completed", False):
                raise MilestoneNotCompletedError(
                    f"Этап '{milestone.name}' не завершён"
                )
        self.end_date = date.today()
        self.status = "completed"

    def progress(self) -> float:
        if not self.tasks:
            return 0.0
        completed = sum(1 for t in self.tasks if t.status == "completed")
        return (completed / len(self.tasks)) * 100
    
    def get_progress_percent(self):
        if not self.tasks:
            return 0
        completed = sum(1 for t in self.tasks if t.status == "completed")
        return int(completed / len(self.tasks) * 100)