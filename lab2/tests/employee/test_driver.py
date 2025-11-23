from module_assets.Vehicle import Vehicle
from module_employee.Driver import Driver


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