from lab2.module_employee.CraneOperator import CraneOperator


def test_crane_lift():
    co = CraneOperator("Степан")
    material = type("Material", (), {"name": "Балка"})
    co.lift_material(material, 10.0)