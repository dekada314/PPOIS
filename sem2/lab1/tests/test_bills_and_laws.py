import pytest
from Entities.bills.bill_state import BillState
from Entities.bills.economic_bill import EconomicBill
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.exceptions import (
    LawCantBeAppliedError,
    LawCantBeSignedError,
    NotValidBillStateError,
)


def test_bill_valid_state_transitions_to_signed():
    bill = EconomicBill("author", 0.01)

    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    bill.sign()

    assert bill.state == BillState.SIGNED


def test_bill_invalid_transition_raises():
    bill = EconomicBill("author", 0.01)

    with pytest.raises(NotValidBillStateError):
        bill.approve()


def test_create_law_requires_signed_bill():
    bill = EconomicBill("author", 0.01)

    with pytest.raises(LawCantBeSignedError):
        bill.create_law(bill)


def test_create_law_returns_economic_law_for_signed_bill():
    bill = EconomicBill("author", 0.01)
    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    bill.sign()

    law = bill.create_law(bill)

    assert law.source_bill_id == bill.uuid
    assert law.tax_delta == 0.01


def test_economic_law_apply_requires_activation():
    bill = EconomicBill("author", 0.01)
    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    bill.sign()
    law = bill.create_law(bill)
    economy = Economy(EconomicConditions.RISE, 0.1, 1000, 0.2)

    with pytest.raises(LawCantBeAppliedError):
        law.apply(economy)


def test_economic_law_apply_changes_tax_ratio_when_active():
    bill = EconomicBill("author", 0.01)
    bill.submit()
    bill.review()
    bill.approve()
    bill.reject()
    bill.sign()
    law = bill.create_law(bill)
    law.activate()
    economy = Economy(EconomicConditions.RISE, 0.1, 1000, 0.2)

    law.apply(economy)

    assert economy._tax_ratio == pytest.approx(0.21)
