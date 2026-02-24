from abc import ABC, abstractmethod


class BillInitializer(ABC):
    
    @abstractmethod
    def bill_initialization(self, serial_num: int) -> bool:
        ...