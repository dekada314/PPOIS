from lab3.module_billing.invoice import Invoice
from lab3.module_billing.billing_item import BillingItem

def test_add_item_and_total():
    inv = Invoice("INV001", "P123", "2025-11-14")
    item1 = BillingItem("SRV01", "Consultation", 150.0)
    item2 = BillingItem("LAB01", "Blood Test", 80.0)
    inv.add_item(item1)
    inv.add_item(item2)
    assert inv.total() == 230.0
    assert len(inv.items) == 2