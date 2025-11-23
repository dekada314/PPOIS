from module_finance.tax_document import TaxDocument


def test_tax_document_init():
    td = TaxDocument("Компания", 2025)
    assert td.company == "Компания"
    assert td.year == 2025
    assert td.submitted is False

def test_tax_submit():
    td = TaxDocument("Компания", 2025)
    td.submit()
    assert td.submitted is True