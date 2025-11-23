from module_projects.timeline import Timeline


def test_timeline_gantt():
    proj = type("Project", (), {})
    tl = Timeline(proj)
    gantt = tl.generate_gantt()
    assert "Gantt" in gantt or "Timeline" in gantt