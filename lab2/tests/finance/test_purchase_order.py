import pytest
from exceptions import PurchaseOrderAlreadyIssuedError
from module_finance.purchase_order import PurchaseOrder


def test_purchase_order_init():
    material = type("Material", (), {"price_per_unit": 450, "quantity": 10})
    po = PurchaseOrder([material])
    assert po.total == 4500
    assert po.issued is False

def test_purchase_order_issue_twice():
    material = type("Material", (), {"price_per_unit": 450, "quantity": 10})
    po = PurchaseOrder([material])
    po.issue()
    with pytest.raises(PurchaseOrderAlreadyIssuedError):
        po.issue()