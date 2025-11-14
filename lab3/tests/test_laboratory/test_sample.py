# from lab3.module_laboratory.sample import Sample
# from lab3.module_laboratory.test import Test

# def test_add_test():
#     sample = Sample("S1", "P1", "2025-11-14")
#     test = Test("CBC", "Complete Blood Count", "4.5-11.0")
#     sample.add_test(test)
#     assert test in sample.tests

# def test_process():
#     sample = Sample("S1", "P1", "2025-11-14")
#     assert sample.status == "received"
#     sample.process()
#     assert sample.status == "processed"