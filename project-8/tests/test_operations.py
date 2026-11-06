import pytest
from src.math_adv.operations import add, multiply, is_prime

def test_add():
    assert add(1, 2, 3) == 6
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(5, 0) == 0

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (4, False),
    (17, True),
    (1, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected
