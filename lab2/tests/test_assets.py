
import pytest
from lab2.module_assets.equipment import Equipment
from lab2.module_assets.material import Material
from lab2.module_assets.tool import Tool
from lab2.module_assets.vehicle import Vehicle
from lab2.exceptions import ToolAlreadyIssuedError, VehicleInUseError
from lab2.associations import ToolAssignment
from datetime import date


def test_equipment_init():
    e = Equipment("Кран", "Kran-1")
    assert e.name == "Кран"
    assert e.model == "Kran-1"
    assert e.status == "operational"
    assert len(e.projects) == 0

def test_equipment_maintenance():
    e = Equipment("Кран", "Kran-1")
    e.schedule_maintenance(date.today())
    assert e.last_maintenance == date.today()

def test_equipment_register_usage():
    e = Equipment("Кран", "Kran-1")
    e.register_usage(10.0)  

def test_equipment_decommission():
    e = Equipment("Кран", "Kran-1")
    e.decommission()
    assert e.status == "decommissioned"


def test_material_init():
    m = Material("Цемент", "мешок", 450.0)
    assert m.name == "Цемент"
    assert m.unit == "мешок"
    assert m.price_per_unit == 450.0
    assert m.quantity == 0.0
    assert m.approved is False

def test_material_update_quantity():
    m = Material("Цемент", "мешок", 450.0)
    m.update_quantity(100)
    assert m.quantity == 100


def test_tool_init():
    t = Tool("Перфоратор", "HILTI-001")
    assert t.name == "Перфоратор"
    assert t.serial_number == "HILTI-001"
    assert t.condition == "good"
    assert t.current_user is None

def test_tool_issue():
    t = Tool("Перфоратор", "HILTI-001")
    w = type("Worker", (), {"name": "Иван"})
    assignment = t.issue_to_worker(w)
    assert t.current_user == w
    assert isinstance(assignment, ToolAssignment)

def test_tool_return():
    t = Tool("Перфоратор", "HILTI-001")
    t.return_to_storage()
    assert t.current_user is None

def test_tool_already_issued():
    t = Tool("Перфоратор", "HILTI-001")
    w1 = type("Worker", (), {"name": "Иван"})
    w2 = type("Worker", (), {"name": "Пётр"})
    t.issue_to_worker(w1)
    with pytest.raises(ToolAlreadyIssuedError):
        t.issue_to_worker(w2)


def test_vehicle_init():
    v = Vehicle("Газель", "A123BC")
    assert v.model == "Газель"
    assert v.license_plate == "A123BC"
    assert v.mileage == 0
    assert len(v.drivers) == 0

def test_vehicle_schedule():
    v = Vehicle("Газель", "A123BC")
    v.schedule_service()  

def test_vehicle_log_trip():
    v = Vehicle("Газель", "A123BC")
    v.log_trip(100)
    assert v.mileage == 100

def test_vehicle_assign_driver():
    v = Vehicle("Газель", "A123BC")
    d = type("Driver", (), {"name": "Иван"})
    v.assign_driver(d)
    assert len(v.drivers) == 1

def test_vehicle_in_use():
    v = Vehicle("Газель", "A123BC")
    d1 = type("Driver", (), {"name": "Иван"})
    d2 = type("Driver", (), {"name": "Пётр"})
    v.assign_driver(d1)
    with pytest.raises(VehicleInUseError):
        v.assign_driver(d2)