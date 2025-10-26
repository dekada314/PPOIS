import pytest
from module_employee.logistics_coordinator import LogisticsCoordinator

def test_logistics_track():
    lc = LogisticsCoordinator("Мария")
    status = lc.track_shipment("TRK123")
    assert status in ["В пути", "Доставлено"]