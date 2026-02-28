from random import random

from .citizens import Citizens
from .parliament import Parliament


class Government:
    def __init__(
        self,
        prime_minister: str = "",
        prime_minister_deputies: list[str] = [],
        ministries: list[str] = [],
    ):
        self._prime_minister = prime_minister
        self._prime_minister_deputies = prime_minister_deputies
        self._ministries = ministries

    def change_mean_salary(self, citizens: Citizens, new_value: int | float) -> None:
        citizens.update_mean_salary(new_value)

    def change_prime_minister(
        self, parliemant: Parliament, new_prime_minister: str
    ) -> None:
        approve = parliemant.give_permission_to_new_pm()
        if approve and isinstance(new_prime_minister, str):
            self._prime_minister = new_prime_minister
