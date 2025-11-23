from module_projects.risk_assessment import RiskAssessment


def test_mitigate():
    proj = type("Project", (), {})
    ra = RiskAssessment(proj)
    assert ra.mitigate(5) == None