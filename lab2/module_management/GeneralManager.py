from .ChiefManager import ChiefManager


class GeneralManager(ChiefManager):
    def __init__(self, name: str):
        super().__init__(name)
        self.chief = None

    def report_to_board(self) -> None:
        pass