import pytest
from module_management.general_manager import GeneralManager
from module_projects.project import Project

def test_general_manager_init():
    gm = GeneralManager("Генеральный")
    assert gm.name == "Генеральный"
    
def test_report_to_board():
    gm = GeneralManager('Генеральный')
    assert gm.report_to_board() == None
