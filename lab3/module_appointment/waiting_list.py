class WaitingList:
    def __init__(self):
        self.entries = []

    def add(self, patient_id: str, preferred_slot):
        self.entries.append({"patient": patient_id, "slot": preferred_slot})

    def find_match(self, slot) -> list:
        return [e for e in self.entries if e["slot"] == slot.start.isoformat()]