from typing import List, Tuple, Dict, Set, Iterable, Generator

# List of integers
def process_numbers(numbers: List[int]) -> List[int]:
   return [num * 2 for num in numbers]

# Tuple of floats
def coordinates() -> Tuple[float, float]:
   return (3.0, 4.0)

# Dictionary with string keys and integer values
def frequency_count(items: List[str]) -> Dict[str, int]:
   freq = {}
   for item in items:
      freq[item] = freq.get(item, 0) + 1
   return freq

# Set of unique characters in a string
def unique_characters(word: str) -> Set[str]:
   return set(word)

# Iterable of integers
def print_items(items: Iterable[int]) -> None:
   for item in items:
      print(item)

# Generator yielding squares of integers up to n
def squares(n: int) -> Generator[int, None, None]:
   for i in range(n):
      yield i * i

# Example usage
numbers = [1, 2, 3, 4, 5]
print(process_numbers(numbers))

print(coordinates())

items = ["apple", "banana", "apple", "orange"]
print(frequency_count(items))

word = "hello"
print(unique_characters(word))

print_items(range(5))

gen = squares(5)
print(list(gen))