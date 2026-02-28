import pytest
from Entities.bills.bill_state import BillState
from Entities.bills.economic_bill import EconomicBill
from Entities.exceptions import NotValidBillStateError
from Entities.government import Government
from Entities.parliament import Parliament
from Entities.president import President
from Entities.state import State


class DummyCitizens:
    def __init__(self):
        self.updated_salary = None

    def update_mean_salary(self, new_value):
        self.updated_salary = new_value


class DummyEconomy:
    def __init__(self):
        self.new_budget = None

    def change_state_budget(self, new_value):
        self.new_budget = new_value


def test_parliament_review_approves_bill_when_random_low(monkeypatch):
    parliament = Parliament()
    bill = EconomicBill("author", 0.01)
    bill.submit()
    monkeypatch.setattr("Entities.parliament.random", lambda: 0.5)

    parliament.review(bill)

    assert bill.state == BillState.APPROVED_BY_PARLIAMENT


def test_parliament_review_can_raise_on_reject_path(monkeypatch):
    parliament = Parliament()
    bill = EconomicBill("author", 0.01)
    bill.submit()
    monkeypatch.setattr("Entities.parliament.random", lambda: 0.95)

    with pytest.raises(NotValidBillStateError):
        parliament.review(bill)


def test_parliament_permissions_depend_on_random(monkeypatch):
    parliament = Parliament()
    monkeypatch.setattr("Entities.parliament.random", lambda: 0.1)
    assert parliament.give_permission_to_new_pm() is True
    monkeypatch.setattr("Entities.parliament.random", lambda: 0.95)
    assert parliament.consider_budget_allocation() is False


def test_government_change_mean_salary_delegates():
    government = Government()
    citizens = DummyCitizens()

    government.change_mean_salary(citizens, 1500)

    assert citizens.updated_salary == 1500


def test_government_change_prime_minister_requires_permission(monkeypatch):
    government = Government(prime_minister="old")
    parliament = Parliament()
    monkeypatch.setattr(parliament, "give_permission_to_new_pm", lambda: True)

    government.change_prime_minister(parliament, "new")

    assert government._prime_minister == "new"


def test_state_add_and_remove_organ():
    state = State("Belarus")

    state.add_organ("parliament", object())
    assert "parliament" in state.organs
    state.remove_organ("parliament")
    assert "parliament" not in state.organs


def test_state_register_bill_submits_it():
    state = State("Belarus")
    bill = EconomicBill("author", 0.01)

    state.register_bill(bill)

    assert bill.state == BillState.SUBMITTED


def test_state_enact_law_activates_law_and_returns_it():
    state = State("Belarus")
    bill = EconomicBill("author", 0.01)
    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    bill.sign()

    law = state.enact_law(bill)

    assert law.active is True


def test_president_sign_veto_and_approve_budget():
    president = President("name", 50)
    bill = EconomicBill("author", 0.01)
    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    economy = DummyEconomy()

    president.sign(bill)
    assert bill.state == BillState.SIGNED

    president.veto(bill)
    assert bill.state == BillState.VETOED

    president.approve_state_budget(economy, 1234)
    assert economy.new_budget == 1234
