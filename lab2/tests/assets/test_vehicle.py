import pytest
from exceptions import VehicleInUseError
from module_assets.vehicle import Vehicle
from module_employee.driver import Driver


def test_vehicle_init():
    v = Vehicle("Газель", "A123BC")
    assert v.model == "Газель"
    assert v.license_plate == "A123BC"
    assert v.mileage == 0
    assert v.drivers == []

def test_vehicle_assign_driver():
    v = Vehicle("Газель", "A123BC")
    d = Driver("Михаил")
    v.assign_driver(d)
    assert d in v.drivers

def test_vehicle_assign_in_use():
    v = Vehicle("Газель", "A123BC")
    d1 = Driver("Михаил")
    d2 = Driver("Пётр")
    v.assign_driver(d1)
    with pytest.raises(VehicleInUseError):
        v.assign_driver(d2)

def test_vehicle_log_trip():
    v = Vehicle("Газель", "A123BC")
    v.log_trip(150)
    assert v.mileage == 150