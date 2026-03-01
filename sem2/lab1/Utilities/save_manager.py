from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from Entities.citizens import Citizens
from Entities.economic_conditions import EconomicConditions
from Entities.economy import Economy
from Entities.foreign_relations import ForeignRelations
from Entities.government import Government
from Entities.infrastructure import Infrastructure
from Entities.parliament import Parliament
from Entities.president import President
from Entities.state import State


class SaveManager:
    @staticmethod
    def _resolve_path(file_path: str | Path) -> Path:
        target = Path(file_path)
        if target.is_absolute():
            return target
        return Path(__file__).resolve().parent / target

    @staticmethod
    def _state_to_dict(state: State) -> dict[str, Any]:
        return {
            "name": state.name,
            "organs": list(state._organs.keys()),
            "laws_count": len(state._laws),
            "bills_count": len(state._bills),
        }

    @staticmethod
    def _citizens_to_dict(citizens: Citizens) -> dict[str, Any]:
        return {
            "population": citizens.population,
            "working_age_peoples": citizens.working_age_peoples,
            "mean_salary": citizens.mean_salary,
        }

    @staticmethod
    def _economy_to_dict(economy: Economy) -> dict[str, Any]:
        return {
            "economic_condition": str(economy._economic_cond),
            "inflation_rate": economy._inflation_rate,
            "state_budget": economy._state_budget,
            "tax_ratio": economy._tax_ratio,
        }

    @staticmethod
    def _infrastructure_to_dict(infrastructure: Infrastructure) -> dict[str, Any]:
        return {
            "roads_length": infrastructure._roads_length,
            "social_buildings_count": infrastructure._social_buildings_count,
            "resource_availability": infrastructure._resource_availability,
        }

    @staticmethod
    def _government_to_dict(government: Government) -> dict[str, Any]:
        return {
            "prime_minister": government._prime_minister,
            "prime_minister_deputies": government._prime_minister_deputies,
            "ministries": government._ministries,
        }

    @staticmethod
    def _president_to_dict(president: President) -> dict[str, Any]:
        return {"name": president.name, "age": president.age}

    @staticmethod
    def _foreign_relations_to_dict(foreign_relations: ForeignRelations) -> dict[str, Any]:
        return {
            "partner_countries": foreign_relations.partner_countries,
            "security_level": foreign_relations.security_level,
            "social_support_fund": foreign_relations.social_support_fund,
            "security_events": foreign_relations.security_events,
        }

    @classmethod
    def save_program_state(
        cls,
        file_path: str | Path,
        state: State,
        citizens: Citizens,
        economy: Economy,
        infrastructure: Infrastructure,
        government: Government,
        president: President,
        foreign_relations: ForeignRelations,
    ) -> Path:
        target = cls._resolve_path(file_path)

        payload = {
            "state": cls._state_to_dict(state),
            "citizens": cls._citizens_to_dict(citizens),
            "economy": cls._economy_to_dict(economy),
            "infrastructure": cls._infrastructure_to_dict(infrastructure),
            "government": cls._government_to_dict(government),
            "president": cls._president_to_dict(president),
            "foreign_relations": cls._foreign_relations_to_dict(foreign_relations),
        }

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return target

    @classmethod
    def load_program_state(cls, file_path: str | Path) -> dict[str, Any]:
        target = cls._resolve_path(file_path)
        payload = json.loads(target.read_text(encoding="utf-8"))

        state = State(payload["state"]["name"])

        citizens_data = payload["citizens"]
        citizens = Citizens(
            citizens_data["population"],
            citizens_data["working_age_peoples"] / citizens_data["population"],
            citizens_data["mean_salary"],
        )

        economy_data = payload["economy"]
        economy = Economy(
            EconomicConditions(economy_data["economic_condition"]),
            economy_data["inflation_rate"],
            economy_data["state_budget"],
            economy_data["tax_ratio"],
        )

        infrastructure_data = payload["infrastructure"]
        infrastructure = Infrastructure(
            infrastructure_data["roads_length"],
            infrastructure_data["social_buildings_count"],
            infrastructure_data["resource_availability"],
        )

        government_data = payload["government"]
        government = Government(
            prime_minister=government_data["prime_minister"],
            prime_minister_deputies=government_data["prime_minister_deputies"],
            ministries=government_data["ministries"],
        )

        president_data = payload["president"]
        president = President(president_data["name"], president_data["age"])

        foreign_data = payload["foreign_relations"]
        foreign_relations = ForeignRelations(
            partner_countries=foreign_data["partner_countries"],
            security_level=foreign_data["security_level"],
            social_support_fund=foreign_data["social_support_fund"],
        )
        for event in foreign_data.get("security_events", []):
            foreign_relations._security_events.append(event)

        organs_map: dict[str, object] = {
            "parliament": Parliament(),
            "government": government,
            "president": president,
            "foreign_relations": foreign_relations,
        }
        for organ_name in payload["state"]["organs"]:
            state.add_organ(organ_name, organs_map.get(organ_name, object()))

        return {
            "state": state,
            "citizens": citizens,
            "economy": economy,
            "infrastructure": infrastructure,
            "government": government,
            "president": president,
            "foreign_relations": foreign_relations,
            "parliament": state._organs.get("parliament"),
            "file_path": target,
        }
