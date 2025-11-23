from module_management.it_manager import ITManager

def deploy_software(capsys):
    it = ITManager("IT")
    assert it.deploy_software() == None
    