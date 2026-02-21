from module_finance.Invoice import Invoice
from module_finance.Payment import Payment


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