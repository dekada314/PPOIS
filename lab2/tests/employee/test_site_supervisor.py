from lab2.module_employee.SiteSupervisor import SiteSupervisor


def test_site_briefing(capsys):
    a = SiteSupervisor('Андрей')
    assert a.daily_briefing() == None