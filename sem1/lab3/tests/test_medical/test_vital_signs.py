from lab3.module_medical.VitalSigns import VitalSigns


def test_risk_level():
    vs = VitalSigns()
    vs.record(190, 100, 170, 37.0)
    assert vs.risk() == "critical"
    vs.record(120, 80, 90, 36.8)
    assert vs.risk() == "normal"