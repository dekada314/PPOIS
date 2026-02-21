from datetime import date

from module_finance.Tender import Tender


def test_tender_init():
    project = type("Project", (), {})
    t = Tender(project, date.today())
    assert t.project == project
    assert t.deadline == date.today()
    assert t.bids == []

def test_tender_select_winner():
    project = type("Project", (), {})
    t = Tender(project, date.today())
    t.receive_bid("Компания1", 90000)
    t.receive_bid("Компания2", 80000)
    winner = t.select_winner()
    assert winner["amount"] == 80000