from lab3.module_pharmacy.Batch import Batch


def test_days_until_expiry():
    batch = Batch("B1", "Aspirin", "2025-12-31")
    assert batch.days_until_expiry() > 0