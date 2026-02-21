from lab2.module_management.ChiefManager import ChiefManager


def test_chief_manager_init():
    cm = ChiefManager("Главный")
    assert cm.name == "Главный"

def test_chief_manager_approve_budget():
    cm = ChiefManager("Главный")
    cm.approve_budget() == None
    