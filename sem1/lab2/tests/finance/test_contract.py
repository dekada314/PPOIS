from datetime import date

import pytest
from exceptions import ContractAlreadySignedError
from module_finance.Contract import Contract


def test_contract_init():
    project = type("Project", (), {})
    c = Contract(project, "ООО Клиент", 1000000)
    assert c.project == project
    assert c.client_name == "ООО Клиент"
    assert c.amount == 1000000
    assert c.signed is False

def test_contract_sign():
    project = type("Project", (), {})
    c = Contract(project, "ООО", 1000000)
    c.sign(date.today())
    assert c.signed is True
    assert c.start_date == date.today()

def test_contract_already_signed():
    project = type("Project", (), {})
    c = Contract(project, "ООО", 1000000)
    c.sign(date.today())
    with pytest.raises(ContractAlreadySignedError):
        c.sign(date.today())