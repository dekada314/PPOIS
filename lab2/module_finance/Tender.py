import uuid
from datetime import date


class Tender:
    def __init__(self, project, deadline: date):
        self.id = str(uuid.uuid4())
        self.project = project
        self.deadline = deadline
        self.bids: list[dict] = []

    def receive_bid(self, company: str, amount: float) -> None:
        self.bids.append({"company": company, "amount": amount})

    def select_winner(self) -> dict:
        return min(self.bids, key=lambda x: x["amount"])