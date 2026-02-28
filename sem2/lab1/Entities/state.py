from .bills.bill import Bill
from .laws.law import Law


class State:
    def __init__(self, name: str):
        self.name: str = name
        self._organs: dict = {}
        self._laws: list[Law] = []
        self._bills: list[Bill] = []
        
    @property
    def organs(self):
        return ", ".join(list(self._organs))

    def add_organ(self, name: str, organ_obj: object) -> None:
        self._organs[name] = organ_obj

    def remove_organ(self, name: str) -> None:
        del self._organs[name]
        
    def register_bill(self, bill: Bill) -> None:
        bill.submit()
        self._bills.append(bill)
    
    def enact_law(self, bill: Bill) -> Law:
        law = bill.create_law()
        law.activate()
        self._laws.append(law)
        return law
    
    def __repr__(self) -> str:
        return f"""
        Государсво: {self.name}
        Органы: {self.organs}
        """
