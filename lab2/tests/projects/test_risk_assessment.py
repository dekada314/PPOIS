from lab2.module_projects.RiskAssessment import RiskAssessment


def test_mitigate():
    proj = type("Project", (), {})
    ra = RiskAssessment(proj)
    assert ra.mitigate(5) == None