from lab3.module_laboratory.technician import Technician
from lab3.module_laboratory.sample import Sample

def test_assign():
    tech = Technician("T1", "Alice", "CLIA")
    sample = Sample("S1", "P1", "2025-11-14")
    tech.assign(sample)
    assert sample in tech.assigned_samples