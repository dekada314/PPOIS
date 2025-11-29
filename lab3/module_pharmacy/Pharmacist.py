class Pharmacist:
    def __init__(self, license: str, name: str):
        self.license = license
        self.name = name
        self.dispensed_count = 0

    def dispense_prescription(self, rx):
        self.dispensed_count += 1

    def total_dispensed(self) -> int:
        return self.dispensed_count