from lab3.module_pharmacy.Drug import Drug


def test_mark_generic():
    drug = Drug("Aspirin", "Bayer", 5.0)
    drug.mark_generic()
    assert drug.generic is True