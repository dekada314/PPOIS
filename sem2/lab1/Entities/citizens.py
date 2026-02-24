from economy import Economy

from .Interfaces.bill_initializer import BillInitializer

type IntFl = int | float

class Citizens(BillInitializer):
    def __init__(self, total_population: int, perc_of_wa_people: IntFl):
        self._total_population = total_population
        self._perc_of_wa_people = perc_of_wa_people
        self.mean_salary = Economy.mean_salary
                
    @property
    def population(self): 
        return self._total_population
    
    @property
    def total_wa_people(self):
        return self._total_population * self._perc_of_wa_people
        
    def __repr__(self) -> str:
        return f"Население: {self._total_population}"
    
    def tax_payment(self, percent: float) -> float:
        pass
    
    def bill_init(self, serial_num: int) -> None:
        pass