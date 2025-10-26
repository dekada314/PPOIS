import uuid

class ChiefManager:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.departments: list[str] = []

    def approve_budget(self) -> None:
        pass

    def strategic_planning(self) -> None:
        pass