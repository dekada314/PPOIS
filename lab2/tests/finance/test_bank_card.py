import pytest
from module_finance.bank_card import BankCard

def test_bank_card_init():
    bc = BankCard("1234567890123456", "Иван")
    assert bc.number.endswith("3456")
    assert bc.holder == "Иван"
    assert bc.balance == 0.0
    assert bc.transactions == []

def test_bank_card_add_funds():
    bc = BankCard("1234", "Иван")
    bc.add_funds(1000)
    assert bc.balance == 1000
    assert bc.transactions == ["+1000"]

def test_bank_card_pay_success():
    bc = BankCard("1234", "Иван")
    bc.add_funds(1000)
    bc.pay(500)
    assert bc.balance == 500
    assert bc.transactions == ["+1000", "-500"]

def test_bank_card_pay_fail():
    bc = BankCard("1234", "Иван")
    with pytest.raises(Exception):
        bc.pay(100)