from module_management.accountant import Accountant

def test_accountant_report():
    a = Accountant("Бухгалтер")
    report = a.generate_report("2025")
    assert "2025" in report