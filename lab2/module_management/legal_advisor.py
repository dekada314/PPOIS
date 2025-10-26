from module_employee.worker import Worker

class LegalAdvisor(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Юрист", 50.0)

    def review_contract(self, contract) -> str:
        return "Одобрено"

    def handle_dispute(self) -> None:
        pass