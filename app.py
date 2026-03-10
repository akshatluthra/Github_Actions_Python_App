def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    result = add(5, 3)
    print(f"The result of adding 5 and 3 is: {result}")
    result = subtract(5, 3)
    print(f"The result of subtracting 3 from 5 is: {result}")
    result = multiply(5, 3)
    print(f"The result of multiplying 5 and 3 is: {result}")
    result = divide(5, 3)
    print(f"The result of dividing 5 by 3 is: {result}")
    