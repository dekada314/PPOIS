import pytest
from module_assets.material import Material

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

