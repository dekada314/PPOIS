from lab2.module_projects.ChangeRequest import ChangeRequest


def test_change_approve():
    proj = type("Project", (), {})
    cr = ChangeRequest(proj, "Добавить окно")
    cr.approve()
    assert cr.approved is True
    # assert cr.status == "approved"

def test_chage_submit():
    proj = type("Project", (), {})
    cr = ChangeRequest(proj, "Добавить окно")
    assert cr.submit() == None
    
def test_change_approve():
    proj = type("Project", (), {})
    cr = ChangeRequest(proj, "Добавить окно")
    cr.approve()
    assert cr.approved is True