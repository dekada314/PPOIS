from lab3.module_pharmacy.DispenseLog import DispenseLog


def test_today_count():
    log = DispenseLog()
    log.log("RX1", "P1", "Aspirin")
    assert log.today_count() >= 1