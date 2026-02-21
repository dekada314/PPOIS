from lab3.module_pharmacy.Pharmacist import Pharmacist


def test_total_dispensed():
    ph = Pharmacist("L123", "Anna")
    ph.dispense_prescription(None)
    ph.dispense_prescription(None)
    assert ph.total_dispensed() == 2