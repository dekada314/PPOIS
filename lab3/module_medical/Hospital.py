class Hospital:
    def __init__(self, name: str, city: str, beds: int):
        self.name = name
        self.city = city
        self.beds = beds
        self.occupied = 0

    def admit(self):
        if self.occupied >= self.beds:
            raise ValueError("No beds")
        self.occupied += 1

    def discharge(self):
        if self.occupied > 0:
            self.occupied -= 1