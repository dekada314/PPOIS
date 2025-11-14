from datetime import datetime

class AuditLog:
    def __init__(self):
        self.records = []

    def log_action(self, action: str, user: str):
        self.records.append({
            "action": action,
            "user": user,
            "time": datetime.now()
        })

    def count_by_user(self, user: str) -> int:
        return sum(1 for r in self.records if r["user"] == user)