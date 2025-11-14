class Analyzer:
    def __init__(self, model: str, serial: str):
        self.model = model
        self.serial = serial
        self.calibrated = True

    def calibrate(self):
        self.calibrated = True

    def analyze(self, sample):
        if not self.calibrated:
            raise ValueError("Not calibrated")
        sample.process()