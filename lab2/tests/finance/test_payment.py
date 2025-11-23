from module_finance.payment import Payment
from module_finance.invoice import Invoice

def test_payment_process_success():
    project = type("Project", (), {})
    i = Invoice(project, 50000)
    p = Payment(i, 50000)
    assert p.process() is True
    assert i.paid is True

def test_payment_process_fail():
    project = type("Project", (), {})
    i = Invoice(project, 50000)
    p = Payment(i, 40000)
    assert p.process() is False