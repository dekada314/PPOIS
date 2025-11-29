from .Worker import Worker


class Plumber(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Сантехник", 30.0)

    def install_pipes(self, task) -> None:
        task.status = "completed"

    def fix_leak(self) -> None:
        pass