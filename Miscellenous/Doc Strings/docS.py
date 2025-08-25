def Add(a,b):
    """This function adds two numbers and returns the result.
    Args:
        a (int, float): The first number to be added.
        b (int, float): The second number to be added.

    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b

result = Add(5, 3)
print("The sum is:", result)

print(Add.__doc__)