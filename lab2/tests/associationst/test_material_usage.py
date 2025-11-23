from datetime import date

from associations import MaterialUsage


def test_material_usage_init():
    m = type("Material",(),{})
    t = type("Task",(),{})
    u = MaterialUsage(m, t, 50.0)
    assert u.material == m
    assert u.task == t
    assert u.quantity == 50.0
    assert u.date == date.today()
    assert len(u.id) == 36