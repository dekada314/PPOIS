from lab3.module_billing.statement import Statement
from lab3.module_billing.account import Account

def test_generate():
    acc = Account("ACC001", "P123")
    stmt = Statement("STMT001", acc)
    assert stmt.generated is False
    stmt.generate()
    assert stmt.generated is True