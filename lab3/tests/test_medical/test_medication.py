from lab3.module_medical.medication import Medication

def test_full_name():
    med = Medication("Paracetamol", "tablet", "500mg")
    assert med.full_name() == "Paracetamol 500mg"

def test_set_out_of_stock():
    med = Medication("Paracetamol", "tablet", "500mg")
    med.set_out_of_stock()
    assert med.in_stock is False