import json

from Entities.citizens import Citizens
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.foreign_relations import ForeignRelations
from Entities.government import Government
from Entities.infrastructure import Infrastructure
from Entities.president import President
from Entities.state import State
from Utilities.save_manager import SaveManager


def test_ensure_security_increases_security_level_and_registers_event():
    foreign_relations = ForeignRelations(security_level=40)

    new_level = foreign_relations.ensure_security(2)

    assert new_level == 43
    assert len(foreign_relations.security_events) == 1


def test_provide_social_support_changes_citizens_salary_and_fund():
    citizens = Citizens(1_000_000, 0.5, 1000)
    foreign_relations = ForeignRelations()

    support_per_worker = foreign_relations.provide_social_support(citizens, 0.01)

    assert support_per_worker == 10
    assert citizens.mean_salary == 1010
    assert foreign_relations.social_support_fund == 5_000_000


def test_save_manager_saves_complete_program_state(tmp_path):
    state = State("Belarus")
    government = Government(prime_minister="PM")
    president = President("President", 50)
    citizens = Citizens(5_000_000, 0.6, 1200)
    economy = Economy(EconomicConditions.RISE, 0.05, 1_000_000, 0.2)
    infrastructure = Infrastructure(10_000, 350, 0.6)
    foreign_relations = ForeignRelations(["Poland", "Lithuania"], 55, 1000)

    state.add_organ("government", government)
    state.add_organ("president", president)
    state.add_organ("foreign_relations", foreign_relations)

    save_path = tmp_path / "state.json"
    result_path = SaveManager.save_program_state(
        save_path,
        state,
        citizens,
        economy,
        infrastructure,
        government,
        president,
        foreign_relations,
    )

    payload = json.loads(result_path.read_text(encoding="utf-8"))

    assert payload["state"]["name"] == "Belarus"
    assert "foreign_relations" in payload["state"]["organs"]
    assert payload["economy"]["state_budget"] == 1_000_000
    assert payload["foreign_relations"]["security_level"] == 55


def test_save_manager_uses_utilities_folder_for_relative_path():
    state = State("Belarus")
    government = Government(prime_minister="PM")
    president = President("President", 50)
    citizens = Citizens(5_000_000, 0.6, 1200)
    economy = Economy(EconomicConditions.RISE, 0.05, 1_000_000, 0.2)
    infrastructure = Infrastructure(10_000, 350, 0.6)
    foreign_relations = ForeignRelations(["Poland"], 50, 0)

    result_path = SaveManager.save_program_state(
        "state_snapshot_test.json",
        state,
        citizens,
        economy,
        infrastructure,
        government,
        president,
        foreign_relations,
    )

    assert result_path.parent == SaveManager._resolve_path(".").resolve()
    result_path.unlink(missing_ok=True)


def test_save_manager_loads_state_from_json(tmp_path):
    state = State("Belarus")
    parliament = object()
    government = Government(prime_minister="PM")
    president = President("President", 50)
    citizens = Citizens(5_000_000, 0.6, 1200)
    economy = Economy(EconomicConditions.RISE, 0.05, 1_000_000, 0.2)
    infrastructure = Infrastructure(10_000, 350, 0.6)
    foreign_relations = ForeignRelations(["Poland", "Lithuania"], 55, 1000)
    foreign_relations.ensure_security(3)

    state.add_organ("parliament", parliament)
    state.add_organ("government", government)
    state.add_organ("president", president)
    state.add_organ("foreign_relations", foreign_relations)

    save_path = tmp_path / "state_load.json"
    SaveManager.save_program_state(
        save_path,
        state,
        citizens,
        economy,
        infrastructure,
        government,
        president,
        foreign_relations,
    )

    loaded = SaveManager.load_program_state(save_path)

    assert loaded["state"].name == "Belarus"
    assert loaded["economy"]._state_budget == 1_000_000
    assert loaded["citizens"].mean_salary == 1200
    assert loaded["foreign_relations"].security_level == 59
    assert "parliament" in loaded["state"]._organs
