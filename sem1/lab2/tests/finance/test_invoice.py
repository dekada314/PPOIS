from module_finance.Invoice import Invoice


def test_invoice_init():
    project = type("Project", (), {})
    i = Invoice(project, 50000)
    assert i.project == project
    assert i.amount == 50000
    assert i.paid is False

def test_invoice_mark_paid():
    project = type("Project", (), {})
    i = Invoice(project, 50000)
    i.mark_paid()
    assert i.paid is True