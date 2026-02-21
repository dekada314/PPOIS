from datetime import datetime


class DispenseLog:
    def __init__(self):
        self.entries = []

    def log(self, rx_id: str, patient_id: str, med_name: str):
        self.entries.append({
            "rx": rx_id,
            "patient": patient_id,
            "med": med_name,
            "time": datetime.now()
        })

    def today_count(self) -> int:
        today = datetime.today().date()
        return sum(1 for e in self.entries if e["time"].date() == today)