class BaseLabException(Exception):
    """Базовое исключение для лабораторной работы"""


class InvalidCardNumberException(BaseLabException):
    """Некорректный номер карты"""


class InsufficientFundsException(BaseLabException):
    """Недостаточно средств на счёте"""


class CardExpiredException(BaseLabException):
    """Срок действия карты истёк"""


class InvalidPinException(BaseLabException):
    """Неверный PIN-код"""


class AccountLockedException(BaseLabException):
    """Аккаунт заблокирован"""


class DuplicateOrderException(BaseLabException):
    """Заказ с таким номером уже существует"""


class DriverNotAvailableException(BaseLabException):
    """Водитель недоступен для назначения"""


class InvalidGPSCoordinatesException(BaseLabException):
    """Некорректные GPS-координаты"""


class PaymentGatewayException(BaseLabException):
    """Ошибка шлюза оплаты"""


class InvoiceAlreadyPaidException(BaseLabException):
    """Счёт уже оплачен"""


class NegativeAmountException(BaseLabException):
    """Сумма не может быть отрицательной"""


class WarehouseCapacityExceededException(BaseLabException):
    """Превышена вместимость склада"""