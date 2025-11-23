from typing import Any, List

from ..module_employee.Worker import Worker


class ProjectManager(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Менеджер проекта", 55.0)
        self.projects: List[Any] = []

    def create_project(self, name: str, budget: float) -> Any:
        from .project import Project
        project = Project(name, budget, self)
        self.projects.append(project)
        return project

    def track_progress(self, project: Any) -> float:
        return project.progress()