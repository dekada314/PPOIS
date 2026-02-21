from module_employee.Engineer import Engineer


def test_engineer_init():
    e = Engineer("Виктор")
    assert e.name == "Виктор"
    assert e.position == "Инженер"
    assert e.hourly_rate == 45.0

def test_engineer_design(capsys):
    e = Engineer("Виктор")
    project = type("Project", (), {"name": "Мост"})
    e.design_structure(project)
    captured = capsys.readouterr()
    assert "проектирует" in captured.out.lower()