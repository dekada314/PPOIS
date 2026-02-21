import pytest

from lab4.sort.InsertionSort import InsertionSort


def test_insertion_sort_nums(non_sorted_nums, sorted_nums, insertion_sorter):
    assert insertion_sorter.insertion_sort(non_sorted_nums) == sorted_nums


def test_insertion_sort_objects(non_sorted_objects, sorted_objects, insertion_sorter):
    assert insertion_sorter.insertion_sort(non_sorted_objects) == sorted_objects


def test_insertion_sort_empty(insertion_sorter):
    assert insertion_sorter.insertion_sort([]) == []


def test_insertion_sort_single(insertion_sorter):
    assert insertion_sorter.insertion_sort([3]) == [3]
