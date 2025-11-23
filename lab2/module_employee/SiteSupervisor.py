from .foreman import Foreman


class SiteSupervisor(Foreman):
    def __init__(self, name: str):
        super().__init__(name)
        self.site = None

    def daily_briefing(self) -> None:
        pass

    def close_site(self) -> None:
        pass