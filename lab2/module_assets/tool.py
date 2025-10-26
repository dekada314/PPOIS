import uuid
from datetime import date
from associations import ToolAssignment
from exceptions import ToolAlreadyIssuedError


class Tool:
    def __init__(self, name: str, serial_number: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.serial_number = serial_number
        self.condition = "good"
        self.storage = None
        self.current_user = None

    def issue_to_worker(self, worker) -> ToolAssignment:
        if self.current_user is not None:
            raise ToolAlreadyIssuedError(
                f"Инструмент {self.name} уже выдан: {self.current_user.name}"
            )
        assignment = ToolAssignment(self, worker, date.today())
        self.current_user = worker
        return assignment

    def return_to_storage(self) -> None:
        self.current_user = None