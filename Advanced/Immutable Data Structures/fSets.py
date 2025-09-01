# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4])

# Attempting to add an element to the frozenset will raise an error
try:
   frozen_set.add(5)
except AttributeError as e:
   print(f"Error: {e}")

# Attempting to remove an element from the frozenset will also raise an error
try:
   frozen_set.remove(2)
except AttributeError as e:
   print(f"Error: {e}")

# The original frozenset remains unchanged
print("Original frozenset:", frozen_set)  