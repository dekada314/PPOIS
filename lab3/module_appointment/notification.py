from datetime import datetime

class Notification:
    def __init__(self, notif_id: str, appointment):
        self.notif_id = notif_id
        self.appointment = appointment
        self.sent = False
