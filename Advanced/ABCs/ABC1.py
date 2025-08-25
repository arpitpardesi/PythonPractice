from abc import ABC, abstractmethod

class MyABC(ABC):
    @abstractmethod
    def my_method(self):
        pass
    def my_method2(self):
        return "This is a concrete method"

class ConcreteClass(MyABC):
    def my_method(self):
        return "Hello, World!"

obj = ConcreteClass()
print(obj.my_method())
