import pytest


# def add(a, b):
# return a + b


# def test_add():
# assert add(2, 3) == 5
# assert add(0.1, 0.2) == pytest.approx(0.3)
# assert add('space', 'ship') == 'spaceship'


def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def test_factorial():
    assert factorial(2) == 2
    assert factorial(0) == pytest.approx(1)
    assert factorial(1) == pytest.approx(1)

    # Raise an error if factorial does *not* raise an error:
    with pytest.raises(ValueError):
        factorial(-1)  # raises ValueError
