# Method overloading

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    # This will not work as expected because the second add method overrides the first one
    def add(self, a, b, c, d):
        return a + b + c + d


# Example usage

math_ops = MathOperations()
# print(math_ops.add(1, 2))  # This will raise an error because
# the first add method is overridden
# print(math_ops.add(1, 2, 3))  # This will also

# raise an error because the second add method is overridden
print(math_ops.add(1, 2, 3, 4))  # This


# will work and return 10
# Note: Python does not support method overloading in the traditional sense.\
# Instead, the last defined method with the same name will be the one that is used.
# To achieve similar functionality, you can use default arguments or variable-length arguments.
class MathOperationsFlexible:
    def add(self, *args):
        return sum(args)


# Example usage
math_ops_flexible = MathOperationsFlexible()
print(math_ops_flexible.add(1, 2))  # This will return 3
print(math_ops_flexible.add(1, 2, 3))  # This will

# return 6
print(math_ops_flexible.add(1, 2, 3, 4))  # This will return 10
print(math_ops_flexible.add(1, 2, 3, 4,
                            5))  # This will return 15


# Overiding
class BaseClass:
    def display(self):
        print("Display from BaseClass")
class DerivedClass(BaseClass):
    def display(self):
        print("Display from DerivedClass")
        super().display()  # Call the base class method
# Example usage
base = BaseClass()
derived = DerivedClass()
base.display()  # Output: Display from BaseClass
derived.display()  # Output: Display from DerivedClass
# Output: Display from BaseClass (called from DerivedClass)
