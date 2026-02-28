from ..economy import Economy
from ..exceptions import LawCantBeAppliedError
from .law import Law


class EconomicLaw(Law):
    def __init__(self, source_bill_id, tax_delta: int | float):
        super().__init__(source_bill_id)
        self.tax_delta = tax_delta
    
    def apply(self, economy: Economy) -> None:
        if not self.activate:
            raise LawCantBeAppliedError
        economy.tax_change(self.tax_delta)
        
    