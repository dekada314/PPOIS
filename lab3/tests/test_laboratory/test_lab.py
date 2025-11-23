from lab3.module_laboratory.lab import Lab
from lab3.module_laboratory.sample import Sample

def test_receive_sample():
    lab = Lab("L1", "Central Lab", "ISO123")
    sample = Sample("S1", "P1", "2025-11-14")
    lab.receive_sample(sample)
    assert sample in lab.samples

def test_process_all():
    lab = Lab("L1", "Central Lab", "ISO123")
    sample = Sample("S1", "P1", "2025-11-14")
    lab.receive_sample(sample)
    lab.process_all()
    assert sample.status == "processed"