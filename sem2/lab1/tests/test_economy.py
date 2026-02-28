import pytest
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.exceptions import (
    NotValidStateBudgetUpdateValueError,
    NotValidStateBudgetValueError,
    NotValidTaxRatioError,
)


class DummyCitizens:
    def __init__(self, tax_payment_value=0):
        self.tax_payment_value = tax_payment_value
        self.last_tax_ratio = None
        self.updated_salary = None
        self.inflation_rate = None

    def tax_payment(self, tax_ratio):
        self.last_tax_ratio = tax_ratio
        return self.tax_payment_value

    def update_mean_salary(self, new_value):
        self.updated_salary = new_value

    def apply_inflation(self, inflation_rate):
        self.inflation_rate = inflation_rate


@pytest.fixture
def economy():
    return Economy(EconomicConditions.RISE, 0.1, 1000, 0.2)


def test_init_with_invalid_inflation_rate_raises():
    with pytest.raises(NotValidTaxRatioError):
        Economy(EconomicConditions.RISE, 1, 1000, 0.2)


def test_init_with_invalid_state_budget_raises():
    with pytest.raises(NotValidStateBudgetValueError):
        Economy(EconomicConditions.RISE, 0.1, -1, 0.2)


def test_init_with_invalid_tax_ratio_raises():
    with pytest.raises(NotValidTaxRatioError):
        Economy(EconomicConditions.RISE, 0.1, 1000, 1)


def test_taxation_uses_default_tax_ratio(economy):
    citizens = DummyCitizens(tax_payment_value=50)

    economy.taxation(citizens)

    assert citizens.last_tax_ratio == 0.2
    assert economy._state_budget == 1050


def test_taxation_uses_custom_tax_ratio(economy):
    citizens = DummyCitizens(tax_payment_value=70)

    economy.taxation(citizens, tax_ratio=0.15)

    assert citizens.last_tax_ratio == 0.15
    assert economy._state_budget == 1070


def test_tax_change_raises_when_change_is_more_than_ten_percent(economy):
    with pytest.raises(ValueError):
        economy.tax_change(0.03)


def test_tax_change_updates_tax_ratio_for_valid_change(economy):
    economy.tax_change(0.02)

    assert economy._tax_ratio == pytest.approx(0.22)


def test_allocate_budget_reduces_state_budget_and_returns_allocated(
    economy, monkeypatch
):
    monkeypatch.setattr("Entities.economy.randint", lambda _a, _b: 10)

    allocated = economy.allocate_budget(max_share=0.25)

    assert allocated == 100
    assert economy._state_budget == 900


def test_change_mean_salary_delegates_to_citizens(economy):
    citizens = DummyCitizens()

    economy.change_mean_salary(citizens, 1500)

    assert citizens.updated_salary == 1500
