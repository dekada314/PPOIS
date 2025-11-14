from datetime import datetime

class VitalSigns:
    def __init__(self):
        self.bp_sys = 0
        self.bp_dia = 0
        self.pulse = 0
        self.temp = 0.0

    def record(self, sys: int, dia: int, pulse: int, temp: float):
        if not (90 <= sys <= 200 and 60 <= dia <= 120):
            raise ValueError("Invalid BP")
        self.bp_sys = sys
        self.bp_dia = dia
        self.pulse = pulse
        self.temp = temp

    def risk(self) -> str:
        if self.bp_sys > 180 or self.pulse > 160:
            return "critical"
        return "normal"