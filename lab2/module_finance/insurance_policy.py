from datetime import date
import uuid
from ..exceptions import InsuranceExpiredError


class InsurancePolicy:
    def __init__(self, equipment):
        self.id = str(uuid.uuid4())
        self.equipment = equipment
        self.coverage = 100000.0
        self.expiry_date = date.today()
        self.active = True

    def renew(self) -> None:
        self.expiry_date = date.today()

    def claim(self, damage: float) -> None:
        if date.today() > self.expiry_date:
            raise InsuranceExpiredError(
                f"Страховка истекла: {self.expiry_date}"
            )