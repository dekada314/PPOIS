import pytest
from module_employee.driver import Driver
from module_assets.vehicle import Vehicle

def test_driver_init():
    d = Driver("Михаил")
    assert d.name == "Михаил"
    assert d.position == "Водитель"
    assert d.vehicles == []

def test_driver_assign_vehicle():
    d = Driver("Михаил")
    v = Vehicle("Газель", "A123BC")
    v.assign_driver(d)  
    assert d in v.drivers