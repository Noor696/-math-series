import pytest
from math_series.series import fibonacci,fibonacci_other,lucas,sum_series

'''
fibonacci
0, 1, 2, 3, 4, 5, 6,  7, ...
0, 1, 1, 2, 3, 5, 8, 13, ...
'''

def test_fibonacci_N0():
 
    actual= fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_N1():
 
    actual= fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_N3():
 
    actual= fibonacci(7)
    expected = 13
    assert actual == expected

def test_fibonacci_other_N4():
 
    actual= fibonacci_other(5)
    expected = 5
    assert actual == expected


'''
lucas
0, 1, 2, 3, 4,  5,  6,  7, ...
2, 1, 3, 4, 7, 11, 18, 29, ...
'''

def test_lucas_N0():
 
    actual= lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_N1():
 
    actual= lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_N3():
 
    actual= lucas(6)
    expected = 18
    assert actual == expected


'''
sum_series
if we put primary number (n) -> call fibonacci
if we put primary number (n) & v1 = 0 , v2 = 1 -> call fibonacci
if we put primary number (n) & v1 = 2 , v2 = 1 -> call lucas
'''

def test_sum_series_N0():
 
    actual= sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_N1():
 
    actual= sum_series(6)
    expected = 8
    assert actual == expected

def test_sum_series_N2():
 
    actual= sum_series(4,0,1)
    expected = 3
    assert actual == expected

def test_sum_series_N3():
 
    actual= sum_series(4,2,1)
    expected = 7
    assert actual == expected