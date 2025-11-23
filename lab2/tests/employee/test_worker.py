from associations import ToolAssignment
from module_assets.tool import Tool

from lab2.module_employee.Worker import Worker


def test_worker_init():
    w = Worker("Иван", "Бетонщик", 25.0)
    assert w.name == "Иван"
    assert w.position == "Бетонщик"
    assert w.hourly_rate == 25.0
    assert w.tools == []

def test_worker_request_tool():
    w = Worker("Иван", "Бетонщик", 25.0)
    t = Tool("Дрель", "D001")
    ta = w.request_tool(t)
    assert isinstance(ta, ToolAssignment)