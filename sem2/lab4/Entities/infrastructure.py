from .exceptions import (
    NotValidResourceAvailabilityError,
    NotValidRoadsLengthError,
    NotValidSocialBuildingsCountError,
)


class Infrastructure:
    def __init__(
        self,
        roads_length: int | float,
        social_buildings_count: int,
        resource_availability: float,
    ):
        self._validate_roads_length(roads_length)
        self._validate_social_buildings_count(social_buildings_count)
        self._validate_resource_availability(resource_availability)

        self._roads_length = roads_length
        self._social_buildings_count = social_buildings_count
        self._resource_availability = resource_availability

        self.costs = {"road": 1000, "building": 500000, "resources": 10000}

    def _validate_roads_length(self, value: int | float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise NotValidRoadsLengthError

    def _validate_social_buildings_count(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise NotValidSocialBuildingsCountError

    def _validate_resource_availability(self, value: float) -> None:
        if not isinstance(value, float) or not 0 <= value <= 1:
            raise NotValidResourceAvailabilityError

    def update_parametrs(self, allocated_budget: int | float) -> None:
        if allocated_budget <= 0:
            return

        self._roads_length += allocated_budget // self.costs["road"]
        self._social_buildings_count += allocated_budget // self.costs["building"]
        resource_delta = allocated_budget / (self.costs["resources"] * 100)
        self._resource_availability = min(1.0, self._resource_availability + resource_delta)
