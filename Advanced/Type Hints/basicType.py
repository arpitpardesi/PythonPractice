from typing import Optional

# Integer type
def calculate_square_area(side_length: int) -> int:
   return side_length ** 2

# Float type
def calculate_circle_area(radius: float) -> float:
   return 3.14 * radius * radius

# String type
def greet(name: str) -> str:
   return f"Hello, {name}"

# Boolean type
def is_adult(age: int) -> bool:
   return age >= 18

# None type
def no_return_example() -> None:
   print("This function does not return anything")

# Optional type (Union of int or None)
def safe_divide(x: int, y: Optional[int]) -> Optional[float]:
   if y is None or y == 0:
      return None
   else:
      return x / y

# Example usage
print(calculate_square_area(5))
print(calculate_circle_area(3.0))
print(greet("Alice"))
print(is_adult(22))
no_return_example()
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, None))