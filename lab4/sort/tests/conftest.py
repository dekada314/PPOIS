import pytest
from lab4.sort.MyClass import Myclass

@pytest.fixture
def non_sorted_nums():
    return [5,3,1,8,6,6,4]

@pytest.fixture
def sorted_nums():
    return [1,3,4,5,6,6,8]

@pytest.fixture
def non_sorted_objects():
    return [
        Myclass(5),
        Myclass(3),
        Myclass(1),
        Myclass(6),
    ]
    
@pytest.fixture
def sorted_objects():
    return [
        Myclass(1),
        Myclass(3),
        Myclass(5),
        Myclass(6),
    ]
    