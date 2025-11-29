class Medication:
    def __init__(self, name: str, form: str, strength: str):
        self.name = name
        self.form = form
        self.strength = strength
        self.in_stock = True

    def full_name(self) -> str:
        return f"{self.name} {self.strength}"

    def set_out_of_stock(self):
        self.in_stock = False