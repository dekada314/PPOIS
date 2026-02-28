from enum import Enum, auto


class BillState(Enum):
    CREATE = auto()
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED_BY_PARLIAMENT = auto()
    REJECTED = auto()
    SIGNED = auto()
    VETOED = auto()
