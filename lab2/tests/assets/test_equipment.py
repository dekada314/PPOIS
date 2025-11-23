from datetime import date

from module_assets.Equipment import Equipment


def test_equipment_init():
    e = Equipment("Кран", "Kran-1")
    assert e.name == "Кран"
    assert e.model == "Kran-1"
    assert e.status == "operational"

def test_equipment_maintenance():
    e = Equipment("Кран", "Kran-1")
    e.schedule_maintenance(date.today())
    assert e.last_maintenance == date.today()

def test_equipment_decommission():
    e = Equipment("Кран", "Kran-1")
    e.decommission()
    assert e.status == "decommissioned"