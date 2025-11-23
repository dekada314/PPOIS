import pytest

from lab3.module_pharmacy.Pharmacy import Pharmacy


def test_dispense_insufficient():
    pharm = Pharmacy("PH1", "City Pharm", "123 St")
    rx = type("Rx", (), {"medication": type("Med", (), {"name": "Aspirin"})()})()
    with pytest.raises(ValueError, match="Not enough stock"):
        pharm.dispense(rx, 5)

def test_restock():
    pharm = Pharmacy("PH1", "City Pharm", "123 St")
    pharm.restock("Aspirin", 100)
    assert pharm.inventory.stock["Aspirin"] == 100