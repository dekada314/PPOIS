import pytest

from lab4.sort.insertion_sort import InsertionSort


def test_insertion_sort_nums(non_sorted_nums, sorted_nums):
    assert InsertionSort.insertion_sort(non_sorted_nums) == sorted_nums


def test_insertion_sort_objects(non_sorted_objects, sorted_objects):
    assert InsertionSort.insertion_sort(non_sorted_objects) == sorted_objects


def test_insertion_sort_empty():
    assert InsertionSort.insertion_sort([]) == []


def test_insertion_sort_single():
    assert InsertionSort.insertion_sort([3]) == [3]
