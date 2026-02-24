from abc import ABC, abstractmethod


class BillConsiders(ABC):
    
    @abstractmethod
    def bill_considering(self, serial_num: int) -> bool:
        ...