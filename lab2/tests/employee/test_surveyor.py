from module_employee.surveyor import Surveyor


def test_surveyor_measure():
    s = Surveyor("Константин")
    height = s.measure_elevation("Точка A")
    assert isinstance(height, float)
    assert height > 0