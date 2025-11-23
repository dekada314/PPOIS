from lab3.module_laboratory.Analyzer import Analyzer
from lab3.module_laboratory.Sample import Sample


def test_analyze_not_calibrated():
    analyzer = Analyzer("ModelX", "SN123")
    analyzer.calibrated = False
    sample = Sample("S1", "P1", "2025-11-14")

def test_analyze():
    analyzer = Analyzer("ModelX", "SN123")
    sample = Sample("S1", "P1", "2025-11-14")
    analyzer.analyze(sample)
    assert sample.status == "processed"