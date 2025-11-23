from module_finance.Estimate import Estimate


def test_estimate_init():
    project = type("Project", (), {})
    e = Estimate(project)
    assert e.project == project
    assert e.total == 0.0
    assert e.items == []

def test_estimate_add_item():
    project = type("Project", (), {})
    e = Estimate(project)
    e.add_item("Цемент", 10, 450)
    assert e.total == 4500
    assert len(e.items) == 1