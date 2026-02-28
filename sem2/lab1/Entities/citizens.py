from exceptions import (
    NotValidNewMeanSalaryError,
    NotValidPopulationValueError,
    NotValidTaxRatioError,
    NotValidWorkingAgeRatioError,
)

type IntFl = int | float


class Citizens:
    def __init__(
        self, total_population: int, working_age_ratio: IntFl, mean_salary: IntFl
    ):
        self._validate_population(total_population)
        self._validate_working_age_ratio(working_age_ratio)
        self._validate_mean_salary(mean_salary)

        self._total_population = total_population
        self._working_age_ratio = working_age_ratio
        self._mean_salary = mean_salary

    @property
    def population(self) -> int:
        return self._total_population

    @property
    def working_age_peoples(self) -> int:
        return int(self._total_population * self._working_age_ratio)

    @property
    def mean_salary(self) -> IntFl:
        return self._mean_salary

    @mean_salary.setter
    def mean_salary(self, new_value: IntFl):
        if (
            not isinstance(new_value, (int, float))
            or new_value > 1.3 * self._mean_salary
        ):
            raise NotValidNewMeanSalaryError
        self._mean_salary = new_value

    def _validate_population(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise NotValidPopulationValueError

    def _validate_working_age_ratio(self, ratio: IntFl) -> None:
        if not isinstance(ratio, (int, float)) or not 0 < ratio < 1:
            raise NotValidWorkingAgeRatioError

    def _validate_mean_salary(self, value: IntFl) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise NotValidNewMeanSalaryError

    def _taxation_calculate(self, tax_ratio: IntFl) -> IntFl:
        if not 0 <= tax_ratio <= 1:
            raise NotValidTaxRatioError
        return tax_ratio * self._mean_salary * self.working_age_peoples

    def tax_payment(self, tax_ratio: IntFl) -> IntFl:
        return self._taxation_calculate(tax_ratio)

    def apply_inflation(self, inflation_rate: IntFl) -> None:
        self.mean_salary = self._mean_salary * (1 + inflation_rate)

    def update_mean_salary(self, new_value: IntFl) -> None:
        self.mean_salary = new_value

    def __repr__(self) -> str:
        return f"Население: {self._total_population}"
