from datetime import datetime


class EquipmentLog:
    def __init__(self):
        self.entries = []

    def log_use(self, equipment_id: str, user: str):
        self.entries.append({
            "eq": equipment_id,
            "user": user,
            "time": datetime.now()
        })

    def usage_count(self, equipment_id: str) -> int:
        return sum(1 for e in self.entries if e["eq"] == equipment_id)