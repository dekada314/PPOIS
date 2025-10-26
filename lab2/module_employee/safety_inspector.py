from .worker import Worker


class SafetyInspector(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Инспектор БД", 42.0)
        self.inspections: list = []

    def conduct_inspection(self, project) -> None:
        self.inspections.append(project)

    def issue_violation(self, worker: Worker, reason: str) -> None:
        pass

    def train_worker(self, worker: Worker, topic: str) -> None:
        worker.certifications.append(topic)