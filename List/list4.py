import copy

a = ['a', 'b', 'c', 'd', 'e']

shallow_copy = copy.copy(a)
deep_copy = copy.deepcopy(a)
print("Original:", a)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# Modifying the original list
a[0] = '1'
print("After modification:")
print("O:", a)
print("S:", shallow_copy)
print("D:", deep_copy)

# The shallow copy reflects the change in the original list,
# while the deep copy remains unchanged.
# This demonstrates the difference between shallow and deep copies in Python.
# A shallow copy creates a new object, but inserts references into it to the objects found in
# the original. A deep copy creates a new object and recursively adds copies of nested objects found in the original.
# This is useful when you want to copy a list but not its nested objects.
# In this case, since the list contains only strings (which are immutable), both copies behave
# similarly. However, if the list contained mutable objects (like lists or dictionaries),
# the difference would be more pronounced.

