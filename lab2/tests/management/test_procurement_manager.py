from lab2.module_finance.PurchaseOrder import PurchaseOrder
from lab2.module_management.ProcurementManager import ProcurementManager


def test_procurement_init():
    pm = ProcurementManager("Закупки")
    assert pm.name == "Закупки"
    assert pm.orders == []

def test_procurement_create_order():
    pm = ProcurementManager("Закупки")
    m = type("Material", (), {"price_per_unit": 100, "quantity": 5})
    order = pm.create_order([m])
    assert isinstance(order, PurchaseOrder)
    assert order in pm.orders