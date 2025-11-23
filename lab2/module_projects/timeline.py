from typing import Any, List


class Timeline:
    def __init__(self, project: Any):
        self.project = project
        self.milestones: List[Any] = []

    def generate_gantt(self) -> str:
        return "Gantt chart generated"