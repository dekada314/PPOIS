from ..exceptions import LawCantBeSignedError
from ..laws.economic_law import EconomicLaw
from .bill import Bill
from .bill_state import BillState


class EconomicBill(Bill):
    def __init__(self, author: str, tax_delta = int | float):
        super().__init__(author)
        self.tax_delta = tax_delta
        
    def create_law(self, bill: Bill) -> EconomicLaw:
        if bill.state != BillState.SIGNED:
            raise LawCantBeSignedError
        return EconomicLaw(self.uuid, self.tax_delta)