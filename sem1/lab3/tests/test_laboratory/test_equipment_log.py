from lab3.module_laboratory.EquipmentLog import EquipmentLog


def test_log_use():
    log = EquipmentLog()
    log.log_use("EQ1", "TechA")
    log.log_use("EQ1", "TechB")
    assert log.usage_count("EQ1") == 2
    assert log.usage_count("EQ2") == 0