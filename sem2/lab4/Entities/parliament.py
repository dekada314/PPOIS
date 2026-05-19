from random import random

from .bills.bill import Bill


class Parliament:
    def review(self, bill: Bill) -> None:
        approve = True if random() < 0.6 else False
        bill.review()
        if approve:
            bill.approve()
        else:
            bill.reject()

    def give_permission_to_new_pm(self) -> bool:
        return True if random() < 0.7 else False

    def consider_budget_allocation(self) -> bool:
        return True if random() < 0.9 else False
