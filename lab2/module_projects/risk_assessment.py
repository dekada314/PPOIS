class RiskAssessment:
    def __init__(self, project):
        self.project = project
        self.risks: list[dict] = []

    def identify_risk(self, description: str, probability: float, impact: float) -> None:
        self.risks.append({"desc": description, "prob": probability, "impact": impact})

    def mitigate(self, risk_index: int) -> None:
        pass