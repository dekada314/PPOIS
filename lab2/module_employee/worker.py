from datetime import date
from ..associations import ToolAssignment
import uuid

class Worker:
    def __init__(self, name: str, position: str, hourly_rate: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.hours_worked = 0.0
        self.phone = ""
        self.certifications = []
        self.assignments = []
        self.tools = []

    def start_shift(self):
        print(f"{self.name} начал смену.")

    def complete_task(self, assignment):
        assignment.status = "completed"
        print(f"{self.name} завершил задачу {assignment.task.description}")

    def request_tool(self, tool):
        return ToolAssignment(tool, self, date.today())