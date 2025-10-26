from .worker import Worker

class Master(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Мастер", 40.0)

    def supervise_work(self, task) -> None:
        pass

    def approve_quality(self, task) -> None:
        task.status = "completed"