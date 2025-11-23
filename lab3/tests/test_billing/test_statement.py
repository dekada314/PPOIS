from lab3.module_billing.Account import Account
from lab3.module_billing.Statement import Statement


def test_generate():
    acc = Account("ACC001", "P123")
    stmt = Statement("STMT001", acc)
    assert stmt.generated is False
    stmt.generate()
    assert stmt.generated is True