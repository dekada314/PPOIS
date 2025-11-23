from lab3.module_billing.BillingItem import BillingItem


def test_mark_covered():
    item = BillingItem("MED01", "Aspirin", 25.0)
    assert item.covered is False
    item.mark_covered()
    assert item.covered is True