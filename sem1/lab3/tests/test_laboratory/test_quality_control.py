from lab3.module_laboratory.QualityControl import QualityControl


def test_run_check():
    qc = QualityControl()
    qc.run_check()
    assert qc.passed is True
    assert qc.last_check == "OK"

def test_fail():
    qc = QualityControl()
    qc.fail("Reagent expired")
    assert qc.passed is False
    assert qc.last_check == "Reagent expired"