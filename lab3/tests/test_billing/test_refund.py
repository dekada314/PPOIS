from lab3.module_billing.refund import Refund
from lab3.module_billing.invoice import Invoice

def test_process_refund():
    inv = Invoice("INV001", "P123", "2025-11-14")
    inv.paid = True
    refund = Refund("REF001", inv, 50.0)
    
    assert refund.processed is False
    assert inv.paid is True
    
    refund.process()
    assert refund.processed is True
    assert inv.paid is False
    