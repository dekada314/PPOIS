from datetime import date

from associations import ToolAssignment


def test_tool_assignment_init():
    tool = type("Tool",(),{})
    worker = type("Worker",(),{})
    ta = ToolAssignment(tool, worker, date.today())
    assert ta.tool == tool
    assert ta.worker == worker
    assert ta.issue_date == date.today()
    assert ta.return_date is None
    assert len(ta.id) == 36

def test_tool_assignment_return():
    ta = ToolAssignment(None, None, date.today())
    ta.return_tool()
    assert ta.return_date == date.today()