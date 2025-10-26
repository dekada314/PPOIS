import pytest
from lab2.module_finance.bank_card import BankCard
from lab2.module_finance.contract import Contract
from lab2.exceptions import PaymentFailedError, ContractAlreadySignedError
from datetime import date


def test_bank_card_pay():
    c = BankCard("1234", "Иван")
    c.add_funds(1000)
    assert c.pay(500) is True
    assert c.balance == 500


def test_contract_sign():
    p = type("Project", (), {})
    c = Contract(p, "ООО", 1000000)
    c.sign(date.today())
    assert c.signed is True


def test_contract_already_signed():
    p = type("Project", (), {})
    c = Contract(p, "ООО", 1000000)
    c.sign(date.today())
    with pytest.raises(ContractAlreadySignedError):
        c.sign(date.today())