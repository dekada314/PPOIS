import pytest
from module_assets.tool import Tool
from associations import ToolAssignment
from exceptions import ToolAlreadyIssuedError
from datetime import date

def test_tool_init():
    t = Tool("Перфоратор", "HILTI-001")
    assert t.name == "Перфоратор"
    assert t.serial_number == "HILTI-001"
    assert t.current_user is None

def test_tool_assign_to_worker():
    t = Tool("Перфоратор", "HILTI-001")
    w = type("Worker", (), {"name": "Иван"})
    ta = t.issue_to_worker(w)
    assert t.current_user == w
    assert isinstance(ta, ToolAssignment)
    assert ta.issue_date == date.today()
