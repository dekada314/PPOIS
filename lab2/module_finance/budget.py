import uuid
from exceptions import InvalidBudgetCategoryError


class Budget:
    def __init__(self, project):
        self.id = str(uuid.uuid4())
        self.project = project
        self.total = 0.0
        self.spent = 0.0
        self.categories: dict[str, float] = {}

    def add_category(self, name: str, amount: float) -> None:
        self.categories[name] = amount
        self.total += amount

    def record_expense(self, category: str, amount: float) -> None:
        if category not in self.categories:
            raise InvalidBudgetCategoryError(
                f"Категория '{category}' не существует в бюджете"
            )
        self.spent += amount

    def remaining(self) -> float:
        return self.total - self.spent