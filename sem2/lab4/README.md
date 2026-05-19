# Лабораторная работа №1 — Интерактивная модель государства

 Реализует консольное приложение, моделирующее состояние государства: население, экономику, инфраструктуру и органы власти. Проект находится в `sem2/lab1`. Точка входа — `sem2/lab1/Utilities/menu.py`.

Возможности

- Просматривать текущее состояние (экономика, инфраструктура, органы власти)
- Собирать налоги и изменять налоговую ставку
- Применять инфляцию и менять среднюю зарплату
- Выделять бюджет на инфраструктуру
- Инициировать и обрабатывать экономические законопроекты
- Управлять органами (добавлять/удалять органы власти)
- Усиливать безопасность и выдавать социальную поддержку
- Сохранять и загружать состояние в/из JSON

Ключевые сущности

- `State` — контейнер органов власти, законов и законопроектов
- `Citizens` — население: число, доля трудоспособных, средняя зарплата
- `Economy` — инфляция, бюджет, налоговая ставка и операции с бюджетом
- `Infrastructure` — дороги, соц. здания, доступность ресурсов
- `Government`, `Parliament`, `President` — логика институтов власти
- `ForeignRelations` — партнёры, уровень безопасности, фонд социальной поддержки
- `SaveManager` — сохранение/загрузка состояния

Краткая схема API (частично)

- `State.add_organ(name, obj)` / `State.remove_organ(name)`
- `Citizens.tax_payment(tax_ratio)` / `Citizens.update_mean_salary(value)`
- `Economy.taxation(citizens, tax_ratio=None)` / `Economy.tax_change(delta)`
- `SaveManager.save_program_state(path, ...)` / `SaveManager.load_program_state(path)`

Точка входа и запуск

Запустить меню из корня проекта:

```bash
python sem2/lab1/Utilities/menu.py
```

Или вызвать функцию `main()` напрямую:

```bash
python -c "from sem2.lab1.Utilities.menu import main; main()"
```

Тесты

Тесты находятся в `sem2/lab1/tests/`. Запустить все тесты:

```bash
pytest -v --cov
```

## Подробное описание всех классов

- `State`
  - Поля:
    - `name: str` — имя государства
    - `_organs: dict` — зарегистрированные органы (name -> объект)
    - `_laws: list[Law]` — список принятых законов
    - `_bills: list[Bill]` — список зарегистрированных законопроектов
  - Методы:
    - `add_organ(name: str, organ_obj: object) -> None` — зарегистрировать орган
    - `remove_organ(name: str) -> None` — удалить орган
    - `register_bill(bill: Bill) -> None` — зарегистрировать законопроект (вызывает `bill.submit()`)
    - `enact_law(bill: Bill) -> Law` — создать закон из законопроекта (`bill.create_law`) и активировать его

- `Citizens`
  - Поля:
    - `_total_population: int` — общее население
    - `_working_age_ratio: int|float` — доля трудоспособных
    - `_mean_salary: int|float` — средняя зарплата
  - Свойства и методы:
    - `population -> int` — возврат `_total_population`
    - `working_age_peoples -> int` — число трудоспособных (целая часть)
    - `mean_salary -> int|float` — текущее значение средней зарплаты (с геттером/сеттером)
    - `tax_payment(tax_ratio: float) -> float` — возвращает сумму собранных налогов (tax_ratio * mean_salary * working_age_peoples)
    - `apply_inflation(inflation_rate: float) -> None` — увеличивает среднюю зарплату с проверками
    - `update_mean_salary(new_value: float) -> None` — валидация и обновление зарплаты

- `EconomicConditions`
  - Enum строковых значений: `RISE`, `PEAK`, `RECESSION`, `CRISIS` — описывает состояние экономики

- `Economy`
  - Поля:
    - `_economic_cond: EconomicConditions`
    - `_inflation_rate: float`
    - `_state_budget: int|float`
    - `_tax_ratio: float`
  - Методы:
    - `_validate_*` — несколько приватных валидаций входных значений
    - `taxation(citizens: Citizens, tax_ratio: float | None) -> None` — собирает налоги и увеличивает `_state_budget`
    - `tax_change(delta: float) -> None` — меняет текущую налоговую ставку (с проверкой ограничения изменения)
    - `allocate_budget(max_share: float = 0.25) -> float` — выделяет часть бюджета (рандомно внутри диапазона)
    - `apply_inflation(citizens: Citizens) -> None` — применяет инфляцию к `Citizens`
    - `change_state_budget(new_value: float) -> None` — смена бюджета с валидацией (макс ±20%)

- `Infrastructure`
  - Поля:
    - `_roads_length: int|float`
    - `_social_buildings_count: int`
    - `_resource_availability: float` (0..1)
    - `costs: dict` — словарь цен для расчётов
  - Методы:
    - `update_parametrs(allocated_budget: int|float) -> None` — увеличивает параметры инфраструктуры пропорционально выделенному бюджету

- `Government`
  - Поля (инкапсулированы):
    - `_prime_minister: str`
    - `_prime_minister_deputies: list[str]`
    - `_ministries: list[str]`
  - Методы:
    - `change_mean_salary(citizens: Citizens, new_value: float) -> None` — делегирует изменение зарплаты
    - `change_prime_minister(parliament: Parliament, new_prime_minister: str) -> None` — просит разрешение у парламента и обновляет премьер-министра

- `Parliament`
  - Методы:
    - `review(bill: Bill) -> None` — рассматривает законопроект, переводя его через стадии (review -> approve/reject)
    - `give_permission_to_new_pm() -> bool` — случайное одобрение назначения премьер-министра
    - `consider_budget_allocation() -> bool` — случайное решение об одобрении выделения бюджета

- `President`
  - Поля:
    - `name: str`
    - `age: int`
  - Методы:
    - `sign(bill: Bill) -> None` — вызывает `bill.sign()`
    - `veto(bill: Bill) -> None` — вызывает `bill.veto()`
    - `approve_state_budget(economy: Economy, new_value: float) -> None` — делегирует изменение бюджета в `Economy`

- `ForeignRelations`
  - Поля:
    - `_partner_countries: set[str]`
    - `_security_level: int|float`
    - `_social_support_fund: int|float`
    - `_security_events: list[str]`
  - Методы:
    - `partner_countries -> list[str]` — список партнёров (отсортирован)
    - `ensure_security(threat_level: float = 1) -> float` — повышает уровень безопасности, регистрирует событие
    - `provide_social_support(citizens: Citizens, support_ratio: float = 0.01) -> float` — выдаёт поддержку и увеличивает фонд соц. поддержки

- `Bill`
  - Поля:
    - `uuid: UUID` — уникальный идентификатор
    - `author: str`
    - `creation_data: date`
    - `state: BillState` — текущее состояние (enum)
  - Методы:
    - `submit()`, `review()`, `approve()`, `reject()`, `sign()`, `veto()` — переводят состояние между шагами (с проверками `_require_state`)
    - `_require_state(require_state: BillState) -> None` — приватная проверка правильности перехода
    - `create_law()` — абстрактный метод, должен возвращать объект `Law`

- `BillState`
  - Enum состояний: `CREATE`, `SUBMITTED`, `UNDER_REVIEW`, `APPROVED_BY_PARLIAMENT`, `REJECTED`, `SIGNED`, `VETOED`

- `EconomicBill` (file: `Entities/bills/economic_bill.py`) — наследует `Bill`
  - Поля:
    - `tax_delta: int|float` — изменение налоговой ставки, предлагаемое законом
  - Методы:
    - `create_law(bill: Bill) -> EconomicLaw` — проверяет, что законопроект подписан, и возвращает `EconomicLaw`

- `Law`
  - Поля:
    - `source_bill_id: UUID` — id исходного законопроекта
    - `active: bool` — флаг активации
  - Методы:
    - `activate()` / `deactivate()` — переключают флаг `active`

- `EconomicLaw` — наследует `Law`
  - Поля:
    - `tax_delta: int|float`
  - Методы:
    - `apply(economy: Economy) -> None` — если закон активен, вызывает `economy.tax_change(self.tax_delta)`, иначе бросает `LawCantBeAppliedError`

- `SaveManager`
  - Статические/классовые методы:
    - `_resolve_path(file_path: str|Path) -> Path` — нормализует путь (относительный к каталогу `Utilities`)
    - `save_program_state(file_path, state, citizens, economy, infrastructure, government, president, foreign_relations) -> Path` — собирает словарь-данные и сохраняет JSON
    - `load_program_state(file_path) -> dict` — читает JSON, создаёт объекты домена (`State`, `Citizens`, `Economy`, `Infrastructure`, `Government`, `President`, `ForeignRelations`, `Parliament`) и возвращает их в словаре

- `exceptions` (file: `Entities/exceptions.py`) — кастомные исключения:
  - `NotValidNewMeanSalaryError`, `NotValidPopulationValueError`, `NotValidWorkingAgeRatioError`, `NotValidBillStateError`, `NotValidTaxRatioError`, `NotValidStateBudgetValueError`, `NotValidStateBudgetUpdateValueError`, `NotValidRoadsLengthError`, `NotValidSocialBuildingsCountError`, `NotValidResourceAvailabilityError`, `LawCantBeSignedError`, `LawCantBeAppliedError`, `TaxChangeTooHighError`
