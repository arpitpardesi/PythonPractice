from typing import TypeVar, List

# Define a type variable T
T = TypeVar('T')

# Generic function that returns the first element of a list
def first_element(items: List[T]) -> T:
   return items[0]

# Example usage
int_list = [1, 2, 3, 4, 5]
str_list = ["apple", "banana", "cherry"]

first_int = first_element(int_list)      # first_int will be of type int
first_str = first_element(str_list)      # first_str will be of type str

print(first_int)
print(first_str)                                              