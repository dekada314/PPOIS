# from lab3.module_laboratory.test_result import TestResult
# from lab3.module_laboratory.sample import Sample
# from lab3.module_laboratory.test import Test

# def test_record():
#     sample = Sample("S1", "P1", "2025-11-14")
#     test = Test("GLU", "Glucose", "70-110")
#     result = TestResult("R1", sample, test)
#     result.record(95.0, "mg/dL")
#     assert result.value == 95.0
#     assert result.unit == "mg/dL"
#     assert test.result == 95.0