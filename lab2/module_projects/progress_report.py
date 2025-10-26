from datetime import date


class ProgressReport:
    def __init__(self, task):
        self.task = task
        self.date = date.today()
        self.percent_complete = 0

    def generate(self) -> int:
        self.percent_complete = 75
        return self.percent_complete