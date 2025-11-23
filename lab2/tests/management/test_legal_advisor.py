from module_management.legal_advisor import LegalAdvisor

def test_legal_review():
    la = LegalAdvisor("Юрист")
    contract = type("Contract", (), {})
    result = la.review_contract(contract)
    assert result in ["Одобрено", "Отклонено"]