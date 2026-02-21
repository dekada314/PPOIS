class ConstructionCompanyError(Exception):
    """Базовое исключение для строительной компании."""

class WorkerAlreadyAssignedError(ConstructionCompanyError):
    """Рабочий уже назначен на задачу."""

class InsufficientMaterialError(ConstructionCompanyError):
    """Недостаточно материала на складе."""

class ToolAlreadyIssuedError(ConstructionCompanyError):
    """Инструмент уже выдан другому рабочему."""

class PaymentFailedError(ConstructionCompanyError):
    """Платёж не прошёл — недостаточно средств."""

class ContractAlreadySignedError(ConstructionCompanyError):
    """Договор уже подписан."""

class ProjectAlreadyStartedError(ConstructionCompanyError):
    """Проект уже запущен."""

class TaskAlreadyCompletedError(ConstructionCompanyError):
    """Задача уже завершена."""

class InvalidBudgetCategoryError(ConstructionCompanyError):
    """Категория бюджета не существует."""

class PurchaseOrderAlreadyIssuedError(ConstructionCompanyError):
    """Заказ уже выдан."""

class VehicleInUseError(ConstructionCompanyError):
    """Транспорт уже используется другим водителем."""

class InsuranceExpiredError(ConstructionCompanyError):
    """Страховка истекла."""

class MilestoneNotCompletedError(ConstructionCompanyError):
    """Этап не завершён — нельзя закрыть проект."""