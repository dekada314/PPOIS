from lab3.module_pharmacy.RefillRequest import RefillRequest


def test_approve_reject():
    req = RefillRequest(None, "RX123")
    req.approve()
    assert req.status == "approved"
    req = RefillRequest(None, "RX123")
    req.reject("expired")
    assert req.status == "rejected: expired"