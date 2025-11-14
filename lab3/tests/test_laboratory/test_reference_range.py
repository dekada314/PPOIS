from lab3.module_laboratory.reference_range import ReferenceRange

def test_validate():
    rr = ReferenceRange("GLU", "adult", 70.0, 110.0)
    assert rr.validate(90.0) is True
    assert rr.validate(120.0) is False