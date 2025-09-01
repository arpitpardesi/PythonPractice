class Descriptor:
   def __get__(self, instance, owner):
      if instance is None:return self
      return instance._value

class MyClass:
   attr = Descriptor()

   def __init__(self, value):
      self._value = value

obj = MyClass(42)
print(obj.attr)  