from lab3.module_billing.InsuranceClaim import InsuranceClaim
from lab3.module_billing.Invoice import Invoice


def test_approve_deny():
    inv = Invoice("INV001", "P123", "2025-11-14")
    claim = InsuranceClaim("CLM001", inv)
    assert claim.status == "submitted"
    
    claim.approve(180.0)
    assert claim.status == "approved: 180.0"
    
    claim = InsuranceClaim("CLM002", inv)
    claim.deny("Not covered")
    assert claim.status == "denied: Not covered"