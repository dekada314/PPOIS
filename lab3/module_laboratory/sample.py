from .test import Test

class Sample:
    def __init__(self, sample_id: str, patient_id: str, collection_date: str):
        self.sample_id = sample_id
        self.patient_id = patient_id
        self.collection_date = collection_date
        self.tests = []
        self.status = "received"

    def add_test(self, test: Test):
        self.tests.append(test)

    def process(self):
        self.status = "processed"