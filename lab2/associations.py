from datetime import date
import uuid

class Assignment:
    def __init__(self, worker, task, hours_planned: float):
        self.id = str(uuid.uuid4())
        self.worker = worker
        self.task = task
        self.hours_planned = hours_planned
        self.hours_actual = 0.0
        self.status = "pending"

    def log_hours(self, hours: float):
        self.hours_actual += hours
        if self.hours_actual >= self.hours_planned:
            self.status = "completed"

class MaterialUsage:
    def __init__(self, material, task, quantity: float):
        self.id = str(uuid.uuid4())
        self.material = material
        self.task = task
        self.quantity = quantity
        self.date = date.today()

class ToolAssignment:
    def __init__(self, tool, worker, issue_date: date):
        self.id = str(uuid.uuid4())
        self.tool = tool
        self.worker = worker
        self.issue_date = issue_date
        self.return_date = None

    def return_tool(self):
        self.return_date = date.today()