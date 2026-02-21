from lab3.module_pharmacy.Inventory import Inventory


def test_low_stock_items():
    inv = Inventory()
    inv.add("Aspirin", 5)
    inv.add("Paracetamol", 50)
    assert "Aspirin" in inv.low_stock_items()
    assert "Paracetamol" not in inv.low_stock_items()