import uuid

from exceptions import VehicleInUseError


class Vehicle:
    def __init__(self, model: str, license_plate: str):
        self.id = str(uuid.uuid4())
        self.model = model
        self.license_plate = license_plate
        self.mileage = 0
        self.last_service = None
        self.drivers: list = []

    def assign_driver(self, driver) -> None:
        if self.drivers:
            raise VehicleInUseError(
                f"ТС {self.license_plate} уже используется: {self.drivers[0].name}"
            )
        self.drivers.append(driver)

    def schedule_service(self) -> None:
        pass

    def log_trip(self, km: float) -> None:
        self.mileage += km
        
    def needs_service(self):
        return self.mileage >= 10000