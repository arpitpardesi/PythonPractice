import sys

a = "Arpit"
print(sys.getrefcount(a))
print(a)
print(id(a))
print(type(a))
print(sys.getrefcount(a))