from typing import List
from .diagnosis import Diagnosis

class MedicalRecord:
    def __init__(self):
        self.diagnoses: List[Diagnosis] = []
        self.visit_count = 0
        self.prescriptions = []

    def add_diagnosis(self, diag: Diagnosis):
        self.diagnoses.append(diag)
        self.visit_count += 1

    def add_prescription(self, rx):
        self.prescriptions.append(rx)