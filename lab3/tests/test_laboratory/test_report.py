from lab3.module_laboratory.Report import Report
from lab3.module_laboratory.Sample import Sample


def test_generate():
    sample = Sample("S1", "P1", "2025-11-14")
    report = Report("REP1", sample)
    assert report.is_ready() is False
    report.generate()
    assert report.is_ready() is True