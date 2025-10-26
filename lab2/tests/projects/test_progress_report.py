import pytest
from module_projects.progress_report import ProgressReport

def test_progress_generate():
    task = type("Task", (), {"status": "in_progress"})
    pr = ProgressReport(task)
    percent = pr.generate()
    assert 0 <= percent <= 100
    assert pr.percent_complete == percent