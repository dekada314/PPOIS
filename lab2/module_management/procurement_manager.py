from module_employee.worker import Worker
from typing import List, Any


class ProcurementManager(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Менеджер по закупкам", 40.0)
        self.orders: List[Any] = []

    def create_order(self, materials: List[Any]) -> Any:
        from module_finance.purchase_order import PurchaseOrder
        order = PurchaseOrder(materials)
        self.orders.append(order)
        return order
    
    def delete_order(self, order):
        if order in self.orders:
            self.order.remove(order)
            

    def track_order(self, order: str) -> str:
        return "В пути"