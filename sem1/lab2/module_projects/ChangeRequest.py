import uuid


class ChangeRequest:
    def __init__(self, project, description: str):
        self.id = str(uuid.uuid4())
        self.project = project
        self.description = description
        self.approved = False

    def submit(self) -> None:
        pass

    def approve(self) -> None:
        self.approved = True