from lab2.module_management.ITManager import ITManager


def deploy_software(capsys):
    it = ITManager("IT")
    assert it.deploy_software() == None
    