from datetime import date

class Statement:
    def __init__(self, statement_id: str, account):
        self.statement_id = statement_id
        self.account = account
        self.period_start = date.today()
        self.generated = False

    def generate(self):
        self.generated = True