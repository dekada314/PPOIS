from .sample import Sample

class Lab:
    def __init__(self, lab_id: str, name: str, accreditation: str):
        self.lab_id = lab_id
        self.name = name
        self.accreditation = accreditation
        self.samples = []

    def receive_sample(self, sample: Sample):
        self.samples.append(sample)

    def process_all(self):
        for s in self.samples:
            s.process()