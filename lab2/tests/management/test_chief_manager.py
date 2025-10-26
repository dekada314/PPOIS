import pytest
from module_management.chief_manager import ChiefManager
from module_finance.budget import Budget
from module_projects.project import Project

def test_chief_manager_init():
    cm = ChiefManager("Главный")
    assert cm.name == "Главный"

def test_chief_manager_approve_budget():
    cm = ChiefManager("Главный")
    cm.approve_budget() == None
    
def test_chief_manager_strategic_planning(capsys):
    cm = ChiefManager("Главный")
    assert cm.strategic_planning() == None