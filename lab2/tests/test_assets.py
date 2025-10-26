import pytest
from lab2.module_assets.tool import Tool
from lab2.exceptions import ToolAlreadyIssuedError


def test_tool_issue():
    t = Tool("Перфоратор", "001")
    w = type("Worker", (), {"name": "Иван"})
    t.issue_to_worker(w)
    assert t.current_user == w


def test_tool_already_issued():
    t = Tool("Перфоратор", "001")
    w1 = type("Worker", (), {"name": "Иван"})
    w2 = type("Worker", (), {"name": "Пётр"})
    t.issue_to_worker(w1)
    with pytest.raises(ToolAlreadyIssuedError):
        t.issue_to_worker(w2)