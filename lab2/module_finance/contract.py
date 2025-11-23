import uuid
from datetime import date

from exceptions import ContractAlreadySignedError


class Contract:
    def __init__(self, project, client_name: str, amount: float):
        self.id = str(uuid.uuid4())
        self.project = project
        self.client_name = client_name
        self.amount = amount
        self.signed = False
        self.start_date = None
        self.end_date = None

    def sign(self, date: date) -> None:
        if self.signed:
            raise ContractAlreadySignedError(
                f"Договор уже подписан {self.start_date}"
            )
        self.signed = True
        self.start_date = date

    def terminate(self) -> None:
        self.signed = False

    def amend(self, new_amount: float) -> None:
        self.amount = new_amount