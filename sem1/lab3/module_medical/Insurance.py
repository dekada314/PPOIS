class Insurance:
    def __init__(self, policy: str, provider: str):
        self.policy = policy
        self.provider = provider
        self.patients = []
        self.active = True

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)

    def coverage(self, service: str) -> float:
        return 0.8 if service == "medication" else 0.5