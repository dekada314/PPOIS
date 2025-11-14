from datetime import datetime

class Report:
    def __init__(self, report_id: str, sample):
        self.report_id = report_id
        self.sample = sample
        self.generated_at = None

    def generate(self):
        self.generated_at = datetime.now()

    def is_ready(self) -> bool:
        return self.generated_at is not None