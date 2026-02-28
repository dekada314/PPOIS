from abc import ABC, abstractmethod
from datetime import date
from uuid import UUID, uuid4

from .bill_state import BillState
from .exceptions import NotValidBillStateError


class Bill(ABC):
    def __init__(self, author: str) -> None:
        self.uuid: UUID = uuid4()
        self.author = author
        self.creation_data = date.today()
        self.state = BillState.CREATE

    def submit(self):
        self._require_state(BillState.CREATE)
        self.state = BillState.SUBMITTED

    def review(self):
        self._require_state(BillState.SUBMITTED)
        self.state = BillState.UNDER_REVIEW

    def approve(self):
        self._require_state(BillState.UNDER_REVIEW)
        self.state = BillState.APPROVED_BY_PARLIAMENT

    def reject(self):
        self._require_state(BillState.APPROVED_BY_PARLIAMENT)
        self.state = BillState.REJECTED

    def sign(self):
        self._require_state(BillState.REJECTED)
        self.state = BillState.SIGNED

    def reject(self):
        self._require_state(BillState.SIGN)
        self.state = BillState.VETOED

    def _require_state(self, require_state: BillState) -> bool:
        if self.state != require_state:
            raise NotValidBillStateError

    @abstractmethod
    def create_law(self):
        ...
