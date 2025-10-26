import pytest
from module_management.storage import Storage
from module_assets.material import Material
from associations import MaterialUsage
from exceptions import InsufficientMaterialError

def test_storage_init():
    s = Storage("Склад 1")
    assert s.location == "Склад 1"
    assert s.materials == []
    assert s.tools == []

def test_storage_receive_material():
    s = Storage("Склад 1")
    m = Material("Цемент", "мешок", 450.0)
    s.receive_material(m, 100)
    assert m.quantity == 100

def test_storage_issue_material_success():
    s = Storage("Склад 1")
    m = Material("Цемент", "мешок", 450.0)
    m.quantity = 100
    t = type("Task", (), {})
    s.materials.append(m)
    usage = s.issue_material(m, 50, t)
    assert isinstance(usage, MaterialUsage) == False
    assert m.quantity == 50

def test_storage_issue_insufficient():
    s = Storage("Склад 1")
    m = Material("Цемент", "мешок", 450.0)
    m.quantity = 10
    t = type("Task", (), {})
    s.materials.append(m)
    with pytest.raises(InsufficientMaterialError):
        s.issue_material(m, 20, t)