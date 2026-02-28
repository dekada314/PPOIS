class NotValidNewMeanSalaryError(Exception):
    """Новое значение средней зарплаты не может быть ниже старого"""


class NotValidPopulationValueError(Exception):
    """Значение кол-ва населения не должно быть меньше 0"""


class NotValidWorkingAgeRatioError(Exception):
    """Доля работосособного население не может быть вне пределов промежутка: 0 < ratio < 1"""


class NotValidBillStateError(Exception):
    """Недопустимое для перехода состояние"""


class NotValidTaxRatioError(Exception):
    """Процент налогообложения не может выходить за пределеы промежутка 0 < tax_ratio < 1"""


class NotValidStateBudgetValueError(Exception):
    """Значение бюджета не может быть меньше 0"""


class NotValidStateBudgetUpdateValueError(Exception):
    """Значение бюджета не может увеличиться или уменьшиться более чем на 20%"""


class NotValidRoadsLengthError(Exception):
    """Значение общей протяженности дорог не может быть отрицательным"""


class NotValidSocialBuildingsCountError(Exception):
    """Количество соц здания не может быть отрицательным"""


class NotValidResourceAvailabilityError(Exception):
    """Значение доли обеспечения ресурсами не может быть вне интервала 0 < rate < 1"""


class LawCantBeSignedError(Exception):
    """Закон не может быть подписан(не та стадия)"""


class LawCantBeAppliedError(Exception):
    """Закон не может быть принят"""
