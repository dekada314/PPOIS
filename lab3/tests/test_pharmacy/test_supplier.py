from lab3.module_pharmacy.supplier import Supplier


def test_add_order():
    sup = Supplier("S1", "MediSupply", "contact@med.com")
    order = type("Order", (), {})()
    sup.add_order(order)
    assert order in sup.orders