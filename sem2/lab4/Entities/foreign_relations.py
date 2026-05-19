from __future__ import annotations

from .citizens import Citizens

type IntFl = int | float


class ForeignRelations:
    def __init__(
        self,
        partner_countries: list[str] | None = None,
        security_level: IntFl = 50,
        social_support_fund: IntFl = 0,
    ):
        self._partner_countries: set[str] = set(partner_countries or [])
        self._security_level: IntFl = security_level
        self._social_support_fund: IntFl = social_support_fund
        self._security_events: list[str] = []

    @property
    def partner_countries(self) -> list[str]:
        return sorted(self._partner_countries)

    @property
    def security_level(self) -> IntFl:
        return self._security_level

    @property
    def social_support_fund(self) -> IntFl:
        return self._social_support_fund

    @property
    def security_events(self) -> list[str]:
        return self._security_events.copy()

    def add_partner_country(self, country_name: str) -> None:
        if country_name:
            self._partner_countries.add(country_name.strip())

    def remove_partner_country(self, country_name: str) -> None:
        self._partner_countries.discard(country_name.strip())

    def ensure_security(self, threat_level: IntFl = 1) -> IntFl:
        normalized_threat = max(0, min(float(threat_level), 10))
        growth = 1 + normalized_threat
        self._security_level = min(100, self._security_level + growth)
        self._security_events.append(
            f"security_protocol_t{normalized_threat:.1f}_lvl{self._security_level:.1f}"
        )
        return self._security_level

    def provide_social_support(self, citizens: Citizens, support_ratio: float = 0.01) -> IntFl:
        ratio = max(0.0, min(float(support_ratio), 0.03))
        if ratio == 0:
            return 0

        support_amount = citizens.mean_salary * ratio
        citizens.update_mean_salary(citizens.mean_salary + support_amount)
        self._social_support_fund += support_amount * citizens.working_age_peoples
        return support_amount
