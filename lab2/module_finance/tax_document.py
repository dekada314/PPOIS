import uuid

class TaxDocument:
    def __init__(self, company: str, year: int):
        self.id = str(uuid.uuid4())
        self.company = company
        self.year = year
        self.submitted = False

    def generate(self) -> None:
        pass

    def submit(self) -> None:
        self.submitted = True