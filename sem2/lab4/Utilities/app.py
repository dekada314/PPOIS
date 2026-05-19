import os
import sys
from pathlib import Path

LAB4_DIR = Path(__file__).resolve().parents[1]
ENTITIES_DIR = LAB4_DIR / "Entities"
UTILITIES_DIR = LAB4_DIR / "Utilities"

if str(LAB4_DIR) not in sys.path:
    sys.path.insert(0, str(LAB4_DIR))
if str(ENTITIES_DIR) not in sys.path:
    sys.path.insert(0, str(ENTITIES_DIR))
if str(UTILITIES_DIR) not in sys.path:
    sys.path.insert(0, str(UTILITIES_DIR))

import json

from Entities.bills.economic_bill import EconomicBill
from Entities.citizens import Citizens
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.foreign_relations import ForeignRelations
from Entities.government import Government
from Entities.infrastructure import Infrastructure
from Entities.parliament import Parliament
from Entities.president import President
from Entities.state import State
from flask import Flask, flash, redirect, render_template, request, url_for
from Utilities.save_manager import SaveManager

state_dict = {
    "state": State("Belarus"),
    "parliament": Parliament(),
    "government": Government(prime_minister="И.О. Премьер-министра"),
    "president": President("Президент", 50),
    "citizens": Citizens(5_000_000, 0.6, 1200),
    "economy": Economy(EconomicConditions.RISE, 0.05, 1_000_000, 0.2),
    "infrastructure": Infrastructure(10_000, 350, 0.6),
    "foreign_relations": ForeignRelations(["Poland", "Lithuania"]),
}
state = state_dict.get("state")
state.add_organ("parliament", state_dict.get("parliament"))
state.add_organ("government", state_dict.get("government"))
state.add_organ("president", state_dict.get("president"))
state.add_organ("foreign_relations", state_dict.get("foreign_relations"))
state_dict["state"] = state

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", state=state_dict)


@app.route("/action/taxation", methods=["POST"])
def taxation():
    try:
        economy: Economy = state_dict.get("economy")
        citizens: Citizens = state_dict.get("citizens")
        economy.taxation(citizens)
        flash(message="Налоги успешно собраны", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/apply_inflation", methods=["POST"])
def apply_inflation():
    try:
        economy: Economy = state_dict.get("economy")
        citizens: Citizens = state_dict.get("citizens")
        economy.apply_inflation(citizens)
        flash(message="Инфляция успешно применена", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/change_salary", methods=["POST"])
def change_salary():
    try:
        new_salary = float(request.form["new_salary"])
        economy: Economy = state_dict.get("economy")
        citizens: Citizens = state_dict.get("citizens")
        economy.change_mean_salary(citizens, new_salary)
        flash(message="Средняя зарплата успешно изменена", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/allocate_budget", methods=["POST"])
def allocate_budget():
    try:
        economy: Economy = state_dict.get("economy")
        allocated = economy.allocate_budget()

        infrastructure: Infrastructure = state_dict.get("infrastructure")
        infrastructure.update_parametrs(allocated)
        flash(message=f"На инфраструктуру выделено {allocated}", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/taxation_with_custom_tax", methods=["POST"])
def taxation_with_custom_tax():
    try:
        custom_tax = float(request.form["custom_tax"]) / 100
        economy: Economy = state_dict.get("economy")
        citizens: Citizens = state_dict.get("citizens")
        economy.taxation(citizens, custom_tax)
        flash(
            message=f"Налоги успешно собраны по ставке {custom_tax}", category="message"
        )
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/tax_change", methods=["POST"])
def tax_change():
    try:
        tax_delta = float(request.form["tax_delta"])
        economy: Economy = state_dict.get("economy")
        economy.tax_change(tax_delta)
        flash(message=f"Ставка успешно изменена", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/approve_state_budget", methods=["POST"])
def approve_state_budget():
    try:
        new_budget = float(request.form["new_budget"])
        president: President = state_dict.get("president")
        economy: Economy = state_dict.get("economy")
        president.approve_state_budget(economy, new_budget)
        flash(message=f"Новый бюджет одобрен", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/change_prime_minister", methods=["POST"])
def change_prime_minister():
    try:
        new_pm = request.form["new_pm"]
        government: Government = state_dict.get("government")
        parliament: Parliament = state_dict.get("parliament")
        government.change_prime_minister(parliament, new_pm)
        flash(message=f"Новый бюджет одобрен", category="message")
    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/add_organ", methods=["POST"])
def add_organ():
    try:
        organ_name = request.form["organ_name"]
        if not organ_name:
            flash(message="Имя органа пустое", category="warning")
        else:
            state: State = state_dict.get("state")
            state.add_organ(organ_name, object())
            flash(message=f"Орган '{organ_name}' добавлен.", category="message")

    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/remove_organ", methods=["POST"])
def remove_organ():
    try:
        organ_name = request.form["organ_name"]
        if not organ_name:
            flash(message="Имя органа пустое", category="warning")
        else:
            state: State = state_dict.get("state")
            state.remove_organ(organ_name)
            flash(message=f"Орган '{organ_name}' удален.", category="message")

    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/ensure_security", methods=["POST"])
def ensure_security():
    try:
        threat_level = request.form["threat_level"]
        foreight_relations: ForeignRelations = state_dict.get("foreign_relations")
        foreight_relations.ensure_security(threat_level)
        flash(message=f"Уровень безопасности: {threat_level}.", category="message")

    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))


@app.route("/action/provide_social_support", methods=["POST"])
def provide_social_support():
    try:
        support_ratio = request.form["support_ratio"]
        foreight_relations: ForeignRelations = state_dict.get("foreign_relations")
        citizens: Citizens = state_dict.get("citizens")
        foreight_relations.provide_social_support(citizens, support_ratio)
        flash(message=f"Новая доля поддержки введена.", category="message")

    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))

@app.route("/action/save_program_state", methods=["POST"])
def save_program_state():
    try:        
        state: State = state_dict.get("state")
        economy: Economy = state_dict.get("economy")
        citizens: Citizens = state_dict.get("citizens")
        president: President = state_dict.get("president")
        government: Government = state_dict.get("government")
        parliament: Parliament = state_dict.get("parliament")
        infrastructure: Infrastructure = state_dict.get("infrastructure")
        foreight_relations: ForeignRelations = state_dict.get("foreign_relations")
        
        saved_to = SaveManager.save_program_state(
            "state_snapshot.json",
            state,
            citizens,
            economy,
            infrastructure,
            government,
            president,
            foreight_relations
        )
        flash(message=f"Данные сохранены.", category="message")

    except Exception as e:
        flash(message=f"Ошибка: {e}", category="danger")
    return redirect(url_for("dashboard"))

@app.route("/action/load_program_state", methods=["POST"])
def load_program_state():
    loaded_state = SaveManager.load_payload()
        
    state_dict["state"] = loaded_state.get("state")
    state_dict["economy"] = loaded_state.get("economy")
    state_dict["citizens"] = loaded_state.get("citizens")
    state_dict["president"] = loaded_state.get("president")
    state_dict["government"] = loaded_state.get("government")
    state_dict["infrastructure"] = loaded_state.get("infrastructure")
    state_dict["foreign_relations"] = loaded_state.get("foreign_relations")
    
    flash(message=f"Данные загружены из файла.", category="message")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
