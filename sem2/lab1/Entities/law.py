from uuid import UUID


class Law:
    def __init__(self, source_bill_id: UUID):
        self.source_bill_id = source_bill_id
        self.active = False
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False