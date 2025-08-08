a,b = map(int, input("Enter two numbers: ").split())

try:
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative.")
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#Raising Exceptions in Python

class CustomError(Exception):
    """Custom exception class for demonstration."""
    pass
try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"Caught a custom error: {e}")
else:
    print("No exceptions were raised.")
finally:
    print("This block always executes, regardless of exceptions.")

