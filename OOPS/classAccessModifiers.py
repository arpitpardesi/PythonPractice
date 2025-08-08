class Employee:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute
        self.__salary = 50000  # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

# Example usage
emp = Employee("Alice", 30)
emp.display_info()  # Accessing public and protected attributes
emp._protected_method()  # Accessing protected method
# emp.__private_method()  # This will raise an AttributeError since it's private
# Accessing private attribute using name mangling
try:
    print(emp.__salary)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")
# Accessing private attribute using name mangling
print(emp._Employee__salary)  # Accessing private attribute using name mangling
emp._Employee__private_method()  # Accessing private method using name mangling
# Note: It's generally not recommended to access private attributes or methods outside the class.

