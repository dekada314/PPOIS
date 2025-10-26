import pytest
from lab2.module_employee.worker import Worker
from lab2.module_finance.bank_card import BankCard
from lab2.module_finance.contract import Contract
from lab2.module_finance.salary import Salary
from lab2.module_finance.invoice import Invoice
from lab2.module_finance.payment import Payment
from lab2.module_finance.budget import Budget
from lab2.module_finance.expense_report import ExpenseReport
from lab2.module_finance.tax_document import TaxDocument
from lab2.module_finance.insurance_policy import InsurancePolicy
from lab2.module_finance.tender import Tender
from lab2.module_finance.estimate import Estimate
from lab2.module_finance.purchase_order import PurchaseOrder
from lab2.exceptions import (
    PaymentFailedError, ContractAlreadySignedError, InvalidBudgetCategoryError,
    PurchaseOrderAlreadyIssuedError, InsuranceExpiredError
)
from datetime import date, timedelta


def test_bankcard_init():
    bc = BankCard("1234567890123456", "Иван")
    assert bc.number == "3456"
    assert bc.balance == 0.0

def test_bankcard_add_funds():
    bc = BankCard("1234", "Иван")
    bc.add_funds(1000)
    assert bc.balance == 1000
    assert "+1000" in bc.transactions

def test_bankcard_pay_success():
    bc = BankCard("1234", "Иван")
    bc.add_funds(1000)
    assert bc.pay(500) is True
    assert bc.balance == 500

def test_bankcard_pay_fail():
    bc = BankCard("1234", "Иван")
    with pytest.raises(PaymentFailedError):
        bc.pay(100)


def test_contract_init():
    p = type("Project", (), {})
    c = Contract(p, "Клиент", 1000000)
    assert c.client_name == "Клиент"
    assert c.amount == 1000000
    assert c.signed is False

def test_contract_sign():
    p = type("Project", (), {})
    c = Contract(p, "Клиент", 1000000)
    c.sign(date.today())
    assert c.signed is True
    assert c.start_date == date.today()

def test_contract_terminate():
    p = type("Project", (), {})
    c = Contract(p, "Клиент", 1000000)
    c.sign(date.today())
    c.terminate()
    assert c.signed is False

def test_contract_amend():
    p = type("Project", (), {})
    c = Contract(p, "Клиент", 1000000)
    c.amend(1200000)
    assert c.amount == 1200000

def test_contract_already_signed():
    p = type("Project", (), {})
    c = Contract(p, "Клиент", 1000000)
    c.sign(date.today())
    with pytest.raises(ContractAlreadySignedError):
        c.sign(date.today())


def test_salary_init():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.hours_worked = 160
    s = Salary(w, "2025-10")
    assert s.base == 4000.0  
    assert s.bonus == 0.0

def test_salary_calculate():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.hours_worked = 160
    s = Salary(w, "2025-10")
    s.bonus = 500
    s.deductions = 200
    total = s.calculate()
    assert total == 4300.0

def test_salary_issue():
    w = Worker("Иван", "Бетонщик", 25.0)
    s = Salary(w, "2025-10")
    s.issue_payment()
    assert s.paid is True

def test_salary_deduct_tax():
    w = Worker("Иван", "Бетонщик", 25.0)
    w.hours_worked = 160
    s = Salary(w, "2025-10")
    s.deduct_tax(13)
    assert s.deductions == 520.0  


def test_invoice_init():
    p = type("Project", (), {})
    i = Invoice(p, 50000)
    assert i.amount == 50000
    assert i.paid is False

def test_invoice_generate():
    p = type("Project", (), {})
    i = Invoice(p, 50000)
    i.generate()  

def test_invoice_mark_paid():
    p = type("Project", (), {})
    i = Invoice(p, 50000)
    i.mark_paid()
    assert i.paid is True


def test_payment_process_success():
    p = type("Project", (), {})
    i = Invoice(p, 50000)
    payment = Payment(i, 50000)
    assert payment.process() is True
    assert i.paid is True

def test_payment_process_fail():
    p = type("Project", (), {})
    i = Invoice(p, 50000)
    payment = Payment(i, 40000)
    assert payment.process() is False


def test_budget_init():
    p = type("Project", (), {})
    b = Budget(p)
    assert b.total == 0.0
    assert b.spent == 0.0

def test_budget_add_category():
    p = type("Project", (), {})
    b = Budget(p)
    b.add_category("Материалы", 100000)
    assert "Материалы" in b.categories
    assert b.total == 100000

def test_budget_record_expense():
    p = type("Project", (), {})
    b = Budget(p)
    b.add_category("Материалы", 100000)
    b.record_expense("Материалы", 30000)
    assert b.spent == 30000

def test_budget_remaining():
    p = type("Project", (), {})
    b = Budget(p)
    b.add_category("Материалы", 100000)
    b.record_expense("Материалы", 30000)
    assert b.remaining() == 70000

def test_budget_invalid_category():
    p = type("Project", (), {})
    b = Budget(p)
    with pytest.raises(InvalidBudgetCategoryError):
        b.record_expense("Неизвестно", 1000)


def test_expense_report_init():
    w = Worker("Иван", "Бетонщик", 25.0)
    items = [{"amount": 100}, {"amount": 200}]
    er = ExpenseReport(w, items)
    assert er.total == 300
    assert er.approved is False

def test_expense_report_submit():
    w = Worker("Иван", "Бетонщик", 25.0)
    items = [{"amount": 100}]
    er = ExpenseReport(w, items)
    er.submit()  

def test_expense_report_approve():
    w = Worker("Иван", "Бетонщик", 25.0)
    items = [{"amount": 100}]
    er = ExpenseReport(w, items)
    er.approve()
    assert er.approved is True


def test_tax_document_init():
    td = TaxDocument("Компания", 2025)
    assert td.year == 2025
    assert td.submitted is False

def test_tax_generate():
    td = TaxDocument("Компания", 2025)
    td.generate()  

def test_tax_submit():
    td = TaxDocument("Компания", 2025)
    td.submit()
    assert td.submitted is True


def test_insurance_init():
    eq = type("Equipment", (), {})
    ip = InsurancePolicy(eq)
    assert ip.coverage == 100000.0
    assert ip.active is True

def test_insurance_renew():
    eq = type("Equipment", (), {})
    ip = InsurancePolicy(eq)
    ip.renew()
    assert ip.expiry_date == date.today()

def test_insurance_claim_success():
    eq = type("Equipment", (), {})
    ip = InsurancePolicy(eq)
    ip.claim(5000)  

def test_insurance_claim_expired():
    eq = type("Equipment", (), {})
    ip = InsurancePolicy(eq)
    ip.expiry_date = date.today() - timedelta(days=1)
    with pytest.raises(InsuranceExpiredError):
        ip.claim(5000)


def test_tender_init():
    p = type("Project", (), {})
    t = Tender(p, date.today())
    assert len(t.bids) == 0

def test_tender_receive_bid():
    p = type("Project", (), {})
    t = Tender(p, date.today())
    t.receive_bid("Компания1", 90000)
    assert len(t.bids) == 1

def test_tender_select_winner():
    p = type("Project", (), {})
    t = Tender(p, date.today())
    t.receive_bid("Компания1", 90000)
    t.receive_bid("Компания2", 80000)
    winner = t.select_winner()
    assert winner["amount"] == 80000


def test_estimate_init():
    p = type("Project", (), {})
    e = Estimate(p)
    assert e.total == 0.0
    assert len(e.items) == 0

def test_estimate_add_item():
    p = type("Project", (), {})
    e = Estimate(p)
    e.add_item("Цемент", 10, 450)
    assert e.total == 4500
    assert len(e.items) == 1

def test_estimate_finalize():
    p = type("Project", (), {})
    e = Estimate(p)
    e.finalize()  


def test_purchase_order_init():
    m = type("Material", (), {"price_per_unit": 450, "quantity": 10})
    po = PurchaseOrder([m])
    assert po.total == 4500
    assert po.issued is False

def test_purchase_order_issue():
    m = type("Material", (), {"price_per_unit": 450, "quantity": 10})
    po = PurchaseOrder([m])
    po.issue()
    assert po.issued is True

def test_purchase_order_receive():
    m = type("Material", (), {"storage": type("Storage", (), {"receive_material": lambda self, qty: setattr(self, 'received', qty)})})
    po = PurchaseOrder([m])
    po.receive()  

def test_purchase_order_already_issued():
    m = type("Material", (), {"price_per_unit": 450, "quantity": 10})
    po = PurchaseOrder([m])
    po.issue()
    with pytest.raises(PurchaseOrderAlreadyIssuedError):
        po.issue()