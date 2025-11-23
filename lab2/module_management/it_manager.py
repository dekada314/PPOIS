from lab2.module_employee.Worker import Worker


class ITManager(Worker):
    def __init__(self, name: str):
        super().__init__(name, "IT-менеджер", 45.0)

    def deploy_software(self) -> None:
        pass

    def backup_data(self) -> None:
        pass