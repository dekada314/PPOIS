class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event: str, time: str):
        self.events.append({"event": event, "time": time})

    def conflicts(self, time: str) -> int:
        return sum(1 for e in self.events if e["time"] == time)