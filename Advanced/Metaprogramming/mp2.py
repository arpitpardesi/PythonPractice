class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Defining class: {name}")

        # Dynamic attribute to the class
        attrs['dynamic_attribute'] = 'Added dynamically'

        # Dynamic method to the class
        def dynamic_method(self):
            return f"This is a dynamically added method for {name}"

        attrs['dynamic_method'] = dynamic_method

        return super().__new__(cls, name, bases, attrs)


# Define a class using the metaclass
class MyClass(metaclass=MyMeta):
    pass


obj = MyClass()
print(obj.dynamic_attribute)
print(obj.dynamic_method())