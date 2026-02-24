from .Interfaces.bill_considers import BillConsiders
from .Interfaces.bill_initializer import BillInitializer
from economy import Economy


class Government(BillConsiders, BillInitializer):
    def __init__(self, prime_minister: str = '', prime_minister_deputies: list[str] = [], ministries: list[str] = []):
        self.prime_minister = prime_minister
        self.prime_minister_deputies = prime_minister_deputies
        self.ministries = ministries
        
    def bill_considering(self, serial_num: int) -> bool:
        pass
    
    def bill_initialization(self, serial_num: int) -> bool:
        pass
    
    def change_mean_salary(self, new_value: int | float) -> str:
        pass