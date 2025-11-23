from lab3.module_billing.Account import Account
from lab3.module_billing.BillingItem import BillingItem
from lab3.module_billing.Invoice import Invoice


def test_add_invoice_and_balance():
    acc = Account("ACC001", "P123")
    assert acc.balance == 0.0
    
    inv = Invoice("INV001", "P123", "2025-11-14")
    item = BillingItem("SRV01", "Checkup", 100.0)
    inv.add_item(item)
    
    acc.add_invoice(inv)
    assert acc.balance == 100.0
    assert inv in acc.invoices