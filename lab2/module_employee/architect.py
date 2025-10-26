from .worker import Worker

class Architect(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Архитектор", 50.0)

    def create_blueprint(self, project) -> str:
        return f"Чертеж для {project.name}"

    def revise_drawing(self) -> None:
        pass