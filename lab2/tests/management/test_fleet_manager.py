import pytest
from module_management.fleet_manager import FleetManager
from module_assets.vehicle import Vehicle
from module_employee.driver import Driver
from exceptions import VehicleInUseError

def test_fleet_manager_init():
    fm = FleetManager("Автопарк")
    assert fm.name == "Автопарк"
    assert fm.vehicles == []

def test_fleet_assign_vehicle():
    fm = FleetManager("Автопарк")
    d = Driver("Михаил")
    v = Vehicle("Газель", "A123BC")
    fm.assign_vehicle(d, v)
    assert v in d.vehicles
    assert d in v.drivers

def test_fleet_assign_in_use():
    fm = FleetManager("Автопарк")
    d1 = Driver("Михаил")
    d2 = Driver("Пётр")
    v = Vehicle("Газель", "A123BC")
    fm.assign_vehicle(d1, v)
    with pytest.raises(VehicleInUseError):
        fm.assign_vehicle(d2, v)