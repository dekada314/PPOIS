import pytest
from lab4.sort.MyClass import Myclass
from lab4.sort.counting_sort import counting_sort


def test_counting_sort_nums(non_sorted_nums, sorted_nums):
    assert counting_sort(non_sorted_nums) == sorted_nums


def test_insertion_sort_empty():
    assert counting_sort([]) == []


def test_counting_sort_single():
    assert counting_sort([3]) == [3]
