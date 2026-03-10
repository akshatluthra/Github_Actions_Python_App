from app import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15


def test_divide():
    assert divide(5, 3) == 5 / 3


def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
