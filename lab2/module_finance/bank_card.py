import uuid

from exceptions import PaymentFailedError


class BankCard:
    def __init__(self, number: str, holder: str):
        self.id = str(uuid.uuid4())
        self.number = number[-4:]
        self.holder = holder
        self.balance = 0.0
        self.transactions: list[str] = []

    def add_funds(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(f"+{amount}")

    def pay(self, amount: float) -> bool:
        if self.balance < amount:
            raise PaymentFailedError(
                f"Недостаточно средств: {self.balance} < {amount}"
            )
        self.balance -= amount
        self.transactions.append(f"-{amount}")
        return True