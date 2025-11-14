from lab3.module_billing.audit_log import AuditLog

def test_log_action_and_count():
    log = AuditLog()
    log.log_action("Create Invoice", "admin")
    log.log_action("Process Payment", "clerk")
    log.log_action("Create Invoice", "admin")
    
    assert log.count_by_user("admin") == 2
    assert log.count_by_user("clerk") == 1