import pytest
from lab4.sort.insertion_sort import insertion_sort

def test_insertion_sort_nums(non_sorted_nums, sorted_nums):
    assert insertion_sort(non_sorted_nums) == sorted_nums
    
def test_insertion_sort_objects(non_sorted_objects, sorted_objects):
    assert insertion_sort(non_sorted_objects) == sorted_objects
    
def test_insertion_sort_empty():
    assert insertion_sort([]) == []
    
def test_insertion_sort_single():
    assert insertion_sort([3]) == [3]