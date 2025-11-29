from datetime import date


class Diagnosis:
    def __init__(self, code: str, desc: str, doctor):
        self.code = code
        self.description = desc
        self.doctor = doctor
        self.date = date.today()

    def is_chronic(self) -> bool:
        return self.code.startswith(("E11", "I10", "J45"))

    def update(self, new_desc: str):
        self.description = new_desc