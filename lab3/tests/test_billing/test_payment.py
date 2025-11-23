from lab3.module_billing.invoice import Invoice
from lab3.module_billing.payment import Payment


def test_apply_payment():
    inv = Invoice("INV001", "P123", "2025-11-14")
    payment = Payment("PAY001", inv, 200.0)
    assert inv.paid is False
    payment.apply()
    assert inv.paid is True