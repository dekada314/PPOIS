from lab3.module_pharmacy.price_calculator import PriceCalculator

def test_with_insurance():
    calc = PriceCalculator()
    price = calc.with_insurance(100.0)
    assert round(price, 2) == 86.40  