from module_projects.TimeLine import Timeline


def test_timeline_gantt():
    proj = type("Project", (), {})
    tl = Timeline(proj)
    gantt = tl.generate_gantt()
    assert "Gantt" in gantt or "Timeline" in gantt