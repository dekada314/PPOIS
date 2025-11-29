from .Worker import Worker


class Engineer(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Инженер", 45.0)

    def design_structure(self, project):
        print(f"Инженер {self.name} проектирует для {project.name}")

    def validate_plan(self, blueprint):
        return True