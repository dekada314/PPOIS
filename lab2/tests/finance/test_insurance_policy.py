from datetime import date, timedelta

import pytest
from exceptions import InsuranceExpiredError
from module_finance.insurance_policy import InsurancePolicy


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