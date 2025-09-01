class Descriptor:
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        instance._value = value

class MyClass:
    attr = Descriptor()

    def __init__(self, value):
        self.attr = value

obj = MyClass(42)
print(obj.attr)
obj.attr = 100
print(obj.attr)
obj.attr = 100.5
print(obj.attr)