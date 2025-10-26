from .worker import Worker


class Electrician(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Электрик", 32.0)

    def install_wiring(self, task) -> None:
        task.status = "completed"

    def test_circuit(self) -> str:
        return "OK"