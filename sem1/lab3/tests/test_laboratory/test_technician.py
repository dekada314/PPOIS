from lab3.module_laboratory.Sample import Sample
from lab3.module_laboratory.Technician import Technician


def test_assign():
    tech = Technician("T1", "Alice", "CLIA")
    sample = Sample("S1", "P1", "2025-11-14")
    tech.assign(sample)
    assert sample in tech.assigned_samples