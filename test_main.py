from check_divisible import is_divisible
from math_ops import add

def test_is_divisible():
    assert is_divisible(10, 2) == True
    assert is_divisible(10, 3) == False
    assert is_divisible(10, 0) == False

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
