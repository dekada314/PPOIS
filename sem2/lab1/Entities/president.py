from .bill import Bill
from .economy import Economy


class President:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def sign(self, bill: Bill) -> None:
        bill.sign()

    def veto(self, bill: Bill) -> None:
        bill.veto()

    def approve_state_budget(self,economy: Economy, new_value: int | float) -> None:
        economy.change_state_budget(new_value)