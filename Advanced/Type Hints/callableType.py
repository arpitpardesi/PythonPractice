from typing import Callable

# Define a function that takes another function as an argument
def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
   return operation(x, y)

# Example functions to be passed as arguments
def add(a: int, b: int) -> int:
   return a + b

def multiply(a: int, b: int) -> int:
   return a * b

# Using the apply_operation function with different operations
result1 = apply_operation(5, 3, add)        # result1 will be 8
result2 = apply_operation(5, 3, multiply)   # result2 will be 15

print(result1)
print(result2)                                                