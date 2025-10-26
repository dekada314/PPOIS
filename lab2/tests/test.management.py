import pytest
from lab2.module_management.storage import Storage
from lab2.exceptions import InsufficientMaterialError


def test_storage_issue():
    s = Storage("Склад")
    m = type("Material", (), {"name": "Цемент", "quantity": 100})
    t = type("Task", (), {})
    s.materials.append(m)
    assert s.issue_material(m, 50, t) is True
    assert m.quantity == 50