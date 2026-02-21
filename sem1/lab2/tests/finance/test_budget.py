import pytest
from exceptions import InvalidBudgetCategoryError
from module_finance.Budget import Budget


def test_budget_init():
    project = type("Project", (), {})
    b = Budget(project)
    assert b.project == project
    assert b.total == 0.0
    assert b.spent == 0.0
    assert b.categories == {}

def test_budget_add_category():
    project = type("Project", (), {})
    b = Budget(project)
    b.add_category("Материалы", 100000)
    assert b.categories["Материалы"] == 100000
    assert b.total == 100000

def test_budget_record_expense():
    project = type("Project", (), {})
    b = Budget(project)
    b.add_category("Материалы", 100000)
    b.record_expense("Материалы", 30000)
    assert b.spent == 30000

def test_budget_invalid_category():
    project = type("Project", (), {})
    b = Budget(project)
    with pytest.raises(InvalidBudgetCategoryError):
        b.record_expense("Неизвестно", 1000)