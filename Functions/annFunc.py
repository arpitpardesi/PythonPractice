def add(a: int, b: int):
    """Returns the sum of two integers."""

    return a + b


def div(a: int, b: int) -> int:
    """Returns the difference of two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b


print(add(1, 2))
print(div(10, 2))
print(div.__annotations__)
