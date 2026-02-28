import pytest
from Entities.exceptions import (
    NotValidResourceAvailabilityError,
    NotValidRoadsLengthError,
    NotValidSocialBuildingsCountError,
)
from Entities.infrastructure import Infrastructure


def test_init_with_invalid_roads_length_raises():
    with pytest.raises(NotValidRoadsLengthError):
        Infrastructure(-1, 10, 0.5)


def test_init_with_invalid_social_buildings_count_raises():
    with pytest.raises(NotValidSocialBuildingsCountError):
        Infrastructure(10, -1, 0.5)


def test_init_with_invalid_resource_availability_raises():
    with pytest.raises(NotValidResourceAvailabilityError):
        Infrastructure(10, 10, 2.0)


def test_update_parameters_increases_roads_when_budget_enough(monkeypatch):
    infra = Infrastructure(10, 5, 0.5)
    monkeypatch.setattr("Entities.infrastructure.randint", lambda _a, _b: 0)

    infra.update_parametrs(5000)

    assert infra._roads_length == 15


def test_update_parameters_with_nonzero_random_does_not_change_buildings(monkeypatch):
    infra = Infrastructure(10, 5, 0.5)
    monkeypatch.setattr("Entities.infrastructure.randint", lambda _a, _b: 1)

    infra.update_parametrs(1_000_000)

    assert infra._social_buildings_count == 5


def test_update_parameters_with_nonzero_random_does_not_change_resources(monkeypatch):
    infra = Infrastructure(10, 5, 0.5)
    monkeypatch.setattr("Entities.infrastructure.randint", lambda _a, _b: 2)

    infra.update_parametrs(30_000)

    assert infra._resource_availability == 0.5
