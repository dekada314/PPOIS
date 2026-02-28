import sys
from pathlib import Path

LAB1_DIR = Path(__file__).resolve().parent
ENTITIES_DIR = LAB1_DIR / "Entities"

if str(LAB1_DIR) not in sys.path:
    sys.path.insert(0, str(LAB1_DIR))
if str(ENTITIES_DIR) not in sys.path:
    sys.path.insert(0, str(ENTITIES_DIR))

from Entities.bills.economic_bill import EconomicBill
from Entities.citizens import Citizens
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.government import Government
from Entities.infrastructure import Infrastructure
from Entities.parliament import Parliament
from Entities.president import President
from Entities.state import State


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите число.")


def read_str(prompt: str) -> str:
    return input(prompt).strip()


def print_status(
    state: State,
    citizens: Citizens,
    economy: Economy,
    infrastructure: Infrastructure,
    government: Government,
    president: President,
) -> None:
    print("\n--- Состояние ---")
    print(f"Государство: {state.name}")
    print(f"Органы: {state.organs}")
    print(f"Президент: {president.name}")
    print(f"Премьер-министр: {government._prime_minister}")
    print(f"Население: {citizens.population}")
    print(f"Средняя зарплата: {citizens.mean_salary}")
    print(f"Бюджет: {economy._state_budget}")
    print(f"Налог: {economy._tax_ratio}")
    print(f"Инфляция: {economy._inflation_rate}")
    print(f"Дороги: {infrastructure._roads_length}")
    print(f"Соц. здания: {infrastructure._social_buildings_count}")
    print(f"Ресурсы: {infrastructure._resource_availability}")


def print_law_stats(state: State) -> None:
    print("\n--- Законы и законопроекты ---")
    print(f"Количество законопроектов: {len(state._bills)}")
    print(f"Количество законов: {len(state._laws)}")


def process_economic_bill(
    state: State,
    parliament: Parliament,
    president: President,
    economy: Economy,
) -> None:
    author = input("Автор законопроекта: ").strip() or "Unknown"
    tax_delta = read_float("Изменение налога (например 0.01): ")
    bill = EconomicBill(author, tax_delta)

    state.register_bill(bill)
    parliament.review(bill)

    if str(bill.state) != "approved_by_parliament":
        print("Парламент не принял законопроект.")
        return

    # В текущей реализации классов до подписи нужен reject.
    bill.reject()
    president.sign(bill)
    law = state.enact_law(bill)
    law.apply(economy)
    print("Закон принят и применен.")


def main() -> None:
    state = State("Belarus")
    parliament = Parliament()
    government = Government(prime_minister="И.О. Премьер-министра")
    president = President("Президент", 50)
    citizens = Citizens(5_000_000, 0.6, 1200)
    economy = Economy(EconomicConditions.RISE, 0.05, 1_000_000, 0.2)
    infrastructure = Infrastructure(10_000, 350, 0.6)

    state.add_organ("parliament", parliament)
    state.add_organ("government", government)
    state.add_organ("president", president)

    while True:
        print(
            """
========== МЕНЮ ==========
1. Показать состояние
2. Собрать налоги
3. Применить инфляцию
4. Изменить среднюю зарплату
5. Выделить бюджет на инфраструктуру
6. Провести экономический законопроект
7. Собрать налоги с другой ставкой
8. Изменить налоговую ставку (delta)
9. Изменить бюджет через президента
10. Сменить премьер-министра
11. Выделить бюджет (с одобрением парламента)
12. Показать кол-во законов и законопроектов
13. Добавить орган в государство
14. Удалить орган из государства
0. Выход
"""
        )
        choice = input("Выберите пункт: ").strip()

        try:
            if choice == "1":
                print_status(state, citizens, economy, infrastructure, government, president)
            elif choice == "2":
                economy.taxation(citizens)
                print("Налоги собраны.")
            elif choice == "3":
                economy.apply_inflation(citizens)
                print("Инфляция применена.")
            elif choice == "4":
                new_salary = read_float("Новая средняя зарплата: ")
                government.change_mean_salary(citizens, new_salary)
                print("Зарплата обновлена.")
            elif choice == "5":
                allocated = economy.allocate_budget()
                infrastructure.update_parametrs(allocated)
                print(f"Выделено на инфраструктуру: {allocated}")
            elif choice == "6":
                process_economic_bill(state, parliament, president, economy)
            elif choice == "7":
                custom_tax = read_float("Введите ставку налога (0..1): ")
                economy.taxation(citizens, custom_tax)
                print("Налоги собраны по пользовательской ставке.")
            elif choice == "8":
                delta = read_float("Введите delta налога (например 0.01): ")
                economy.tax_change(delta)
                print("Налоговая ставка изменена.")
            elif choice == "9":
                new_budget = read_float("Введите новый бюджет: ")
                president.approve_state_budget(economy, new_budget)
                print("Президент утвердил новый бюджет.")
            elif choice == "10":
                new_pm = read_str("Введите нового премьер-министра: ")
                government.change_prime_minister(parliament, new_pm)
                print(f"Текущий премьер-министр: {government._prime_minister}")
            elif choice == "11":
                if parliament.consider_budget_allocation():
                    allocated = economy.allocate_budget()
                    infrastructure.update_parametrs(allocated)
                    print(f"Парламент одобрил. Выделено: {allocated}")
                else:
                    print("Парламент не одобрил выделение.")
            elif choice == "12":
                print_law_stats(state)
            elif choice == "13":
                organ_name = read_str("Введите имя нового органа: ")
                if not organ_name:
                    print("Имя органа пустое.")
                else:
                    state.add_organ(organ_name, object())
                    print(f"Орган '{organ_name}' добавлен.")
            elif choice == "14":
                organ_name = read_str("Введите имя органа для удаления: ")
                state.remove_organ(organ_name)
                print(f"Орган '{organ_name}' удален.")
            elif choice == "0":
                print("Завершение работы.")
                break
            else:
                print("Нет такого пункта.")
        except Exception as exc:
            print(f"Ошибка: {exc.__class__.__name__}")


if __name__ == "__main__":
    main()
