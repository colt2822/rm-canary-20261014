from calc import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(1, 4) == -3


def test_multiply():
    assert multiply(3, 4) == 12
