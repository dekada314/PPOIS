import uuid


class Milestone:
    def __init__(self, name: str, project):
        self.id = str(uuid.uuid4())
        self.name = name
        self.project = project
        self.due_date = None
        self.completed = False
        self.tasks: list = []

    def add_task(self, task) -> None:
        self.tasks.append(task)
        task.milestone = self

    def complete(self) -> bool:
        self.completed = all(t.status == "completed" for t in self.tasks)
        return self.completed