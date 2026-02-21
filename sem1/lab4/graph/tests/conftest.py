import pytest

from lab4.graph.graph import Graph


@pytest.fixture
def graph():
    adjancy_list = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [2],
        5: [1],
    }

    return Graph(adjancy_list)


@pytest.fixture
def vertices():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def edges():
    return [(1, 2), (1, 3), (2, 4), (2, 5), (4, 2), (5, 1)]
