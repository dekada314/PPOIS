from exceptions import VehicleInUseError

from lab2.module_employee.Worker import Worker


class FleetManager(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Менеджер автопарка", 38.0)
        self.vehicles: list = []

    def schedule_maintenance(self, vehicle) -> None:
        pass

    def assign_vehicle(self, driver, vehicle) -> None:
        if vehicle.drivers:
            raise VehicleInUseError(
                f"ТС {vehicle.license_plate} уже используется"
            )
        vehicle.drivers.append(driver)
        driver.vehicles.append(vehicle)