from lab2.module_employee.QualityController import QualityController


def test_quality_test():
    qc = QualityController("Татьяна")
    result = qc.test_concrete("Проба 1")
    assert "МПа" in result