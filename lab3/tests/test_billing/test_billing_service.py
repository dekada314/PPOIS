from lab3.module_billing.billing_service import BillingService

def test_calculate_and_discount():
    service = BillingService("SRV01", "X-Ray", 120.0)
    assert service.calculate(2) == 240.0
    assert service.apply_discount(240.0, 0.1) == 216.0