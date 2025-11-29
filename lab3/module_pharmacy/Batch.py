from datetime import date


class Batch:
    def __init__(self, batch_id: str, drug_name: str, expiry: str):
        self.batch_id = batch_id
        self.drug_name = drug_name
        self.expiry = date.fromisoformat(expiry)

    def is_expired(self) -> bool:
        return date.today() > self.expiry

    def days_until_expiry(self) -> int:
        return (self.expiry - date.today()).days