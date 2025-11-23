from lab2.module_finance.ExpenseReport import ExpenseReport


def test_expense_report_init():
    worker = type("Worker", (), {"name": "Иван"})
    items = [{"amount": 100}, {"amount": 200}]
    er = ExpenseReport(worker, items)
    assert er.worker == worker
    assert er.total == 300
    assert er.approved is False

def test_expense_report_approve():
    worker = type("Worker", (), {})
    items = [{"amount": 100}]
    er = ExpenseReport(worker, items)
    er.approve()
    assert er.approved is True