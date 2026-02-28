from random import randint

from .citizens import Citizens
from .economic_conditions import EconomicConditions
from .exceptions import (
    NotValidStateBudgetUpdateValueError,
    NotValidStateBudgetValueError,
    NotValidTaxRatioError,
)

type IntFl = int | float


class Economy:
    def __init__(
        self,
        economic_cond: EconomicConditions,
        inflation_rate: IntFl,
        state_budget: IntFl,
        tax_ratio: IntFl,
    ):
        self._validate_inflation_rate(inflation_rate)
        self._validate_state_budget(state_budget)
        self._validate_tax_ratio(tax_ratio)

        self._economic_cond = economic_cond
        self._inflation_rate = inflation_rate
        self._state_budget = state_budget
        self._tax_ratio = tax_ratio

    def _validate_inflation_rate(self, value: float) -> None:
        if not isinstance(value, float) or not 0 < value < 1:
            raise NotValidTaxRatioError

    def _validate_state_budget(self, value: IntFl) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise NotValidStateBudgetValueError

    def _validate_state_budget_update(self, updated_value: IntFl) -> None:
        if abs(1 - updated_value / self._state_budget) > 0.2:
            raise NotValidStateBudgetUpdateValueError

    def _validate_tax_ratio(self, value: float) -> None:
        if not isinstance(value, float) or not 0 < value < 1:
            raise NotValidTaxRatioError
        
    def _validate_tax_change(self, tax_delta: IntFl) -> None:
        if tax_delta / self._tax_ratio > 0.1:
            raise ValueError

    def taxation(self, citizens: Citizens, tax_ratio: IntFl = None) -> None:
        rate = self._tax_ratio if tax_ratio is None else tax_ratio
        self._state_budget += citizens.tax_payment(rate)

    def tax_change(self, tax_delta: IntFl) -> None:
        self._validate_tax_change(tax_delta)
        self._tax_ratio += tax_delta

    def allocate_budget(self, max_share: float = 0.25) -> IntFl:
        allocated_budget = self._state_budget * randint(5, int(max_share * 100)) / 100
        self._state_budget -= allocated_budget
        return allocated_budget

    def change_mean_salary(self, citizens: Citizens, new_value: IntFl) -> None:
        citizens.update_mean_salary(new_value)

    def apply_inflation(self, citizens: Citizens) -> None:
        citizens.apply_inflation(self._inflation_rate)

    def change_state_budget(self, new_value: IntFl) -> None:
        self._validate_state_budget_update(new_value)
        self._state_budget = new_value
