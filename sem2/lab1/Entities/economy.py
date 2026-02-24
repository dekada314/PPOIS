from random import randint

from exceptions import NotValidNewMeanSalaryError

from .citizens import Citizens
from .economic_conditions import EconomicConditions

type IntFl = int | float

class Economy:
    def __init__(
        self,
        economic_cond: EconomicConditions,
        inflation_rate: IntFl,
        state_budget: IntFl,
        income_tax: IntFl,
        mean_salary: IntFl
    ):
        self._economic_cond = economic_cond
        self._inflation_rate = inflation_rate
        self._state_budget = state_budget
        self._income_tax = income_tax
        self._mean_salary = mean_salary
        
    @property
    def mean_salary(self):
        return self._mean_salary
        
    def _taxation_calculate(self, precent: IntFl):
        return precent * Citizens.mean_salary * Citizens.total_wa_people
    
    def _check_valid_mean_salary(self, new_value: IntFl):
        if self._mean_salary > new_value:
            raise NotValidNewMeanSalaryError
        return True
        
    def taxation(self, precent: IntFl) -> str:
        taxation_calculate = self._taxation_calculate(precent)
        self._state_budget += taxation_calculate
        return f"{taxation_calculate} в ходе налогооблажения было добавлено в бюджет"
        
    def allocate_budget(self) -> IntFl:
        return self._state_budget * randint(1,5)
    
    def change_mean_salary(self, new_value = IntFl):
        if self._check_valid_mean_salary(new_value):
            self._mean_salary = new_value
            
        
        
        
        