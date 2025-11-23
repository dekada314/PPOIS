from module_employee.site_supervisor import SiteSupervisor

def test_site_briefing(capsys):
    a = SiteSupervisor('Андрей')
    assert a.daily_briefing() == None