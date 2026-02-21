import pytest

from lab4.sort.CountingSort import CountingSort
from lab4.sort.MyClass import Myclass


def test_counting_sort_nums(non_sorted_nums, sorted_nums, countring_sorter):
    assert countring_sorter.counting_sort(non_sorted_nums) == sorted_nums


def test_insertion_sort_empty(countring_sorter):
    assert countring_sorter.counting_sort([]) == []


def test_counting_sort_single(countring_sorter):
    assert countring_sorter.counting_sort([3]) == [3]
