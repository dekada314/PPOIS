from .worker import Worker

class Driver(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Водитель", 28.0)
        self.license_number = ""
        self.vehicles = []

    def deliver_material(self, material, destination):
        print(f"{self.name} доставил {material.name} в {destination}")

    def log_mileage(self, km: float):
        self.hours_worked += km / 50