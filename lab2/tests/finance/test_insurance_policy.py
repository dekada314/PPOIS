import pytest
from module_finance.insurance_policy import InsurancePolicy
from exceptions import InsuranceExpiredError
from datetime import date, timedelta

def test_insurance_init():
    equipment = type("Equipment", (), {})
    ip = InsurancePolicy(equipment)
    assert ip.equipment == equipment
    assert ip.coverage == 100000.0
    assert ip.active is True

def test_insurance_claim_expired():
    equipment = type("Equipment", (), {})
    ip = InsurancePolicy(equipment)
    ip.expiry_date = date.today() - timedelta(days=1)
    with pytest.raises(InsuranceExpiredError):
        ip.claim(5000)