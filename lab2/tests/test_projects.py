import pytest
from lab2.module_projects.project import Project
from lab2.exceptions import ProjectAlreadyStartedError


def test_project_start():
    p = Project("ЖК", 1000000)
    p.start()
    assert p.status == "in_progress"


def test_project_start_twice():
    p = Project("ЖК", 1000000)
    p.start()
    with pytest.raises(ProjectAlreadyStartedError):
        p.start()