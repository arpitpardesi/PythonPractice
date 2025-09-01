from collections import namedtuple

# Define a named tuple type 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p1 = Point(1, 2)

# Access elements by index (like a tuple)
print(p1[0], p1[1])

# Access elements by name
print(p1.x)
print(p1.y)

print(p1)
# Attempt to modify the named tuple
# This will raise an AttributeError since named tuples are immutable
try:
   p1.x = 10
except AttributeError as e:
   print(f"Error occurred: {e}")

# Accessing elements in a named tuple is similar to accessing elements in a regular tuple
print(p1.x)
print(p1.y)