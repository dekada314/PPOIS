from lab2.module_management.LegalAdvisor import LegalAdvisor


def test_legal_review():
    la = LegalAdvisor("Юрист")
    contract = type("Contract", (), {})
    result = la.review_contract(contract)
    assert result in ["Одобрено", "Отклонено"]