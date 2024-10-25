import pytest
from count_and_sum_even_positives import count_and_sum_even_positives

def test_example():
    numbers = [1, 2, 3, 4, 5, 6, -2, -4, 0, 8, 10]
    count, total_sum = count_and_sum_even_positives(numbers)
    assert count == 5 
    assert total_sum == 30 

def test_empty_list():
    numbers = []
    count, total_sum = count_and_sum_even_positives(numbers)
    assert count == 0
    assert total_sum == 0

def test_no_positives():
    numbers = [-1, -2, -3, -4, -5]
    count, total_sum = count_and_sum_even_positives(numbers)
    assert count == 0
    assert total_sum == 0

def test_all_positives():
    numbers = [2, 4, 6, 8, 10]
    count, total_sum = count_and_sum_even_positives(numbers)
    assert count == 5
    assert total_sum == 30
