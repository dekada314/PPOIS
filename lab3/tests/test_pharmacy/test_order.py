from lab3.module_pharmacy.Order import Order


def test_finalize():
    supplier = type("Sup", (), {})()
    order = Order("O1", supplier)
    order.add_item("Aspirin", 100, 0.5)
    order.finalize()
    assert order.status == "sent"