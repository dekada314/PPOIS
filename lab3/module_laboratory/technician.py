class Technician:
    def __init__(self, tech_id: str, name: str, certification: str):
        self.tech_id = tech_id
        self.name = name
        self.certification = certification
        self.assigned_samples = []

    def assign(self, sample):
        self.assigned_samples.append(sample)