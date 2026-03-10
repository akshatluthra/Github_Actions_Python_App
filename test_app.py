from app import app


def test_add():
    assert app.add(5, 3) == 8


def test_subtract():
    assert app.subtract(5, 3) == 2


def test_multiply():
    assert app.multiply(5, 3) == 15

    
def test_divide():
    assert app.divide(5, 3) == 5 / 3


def test_divide_by_zero():
    try:
        app.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
