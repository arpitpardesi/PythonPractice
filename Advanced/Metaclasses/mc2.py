# Define a custom metaclass
class MyMetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['version'] = 1.0

        # Modify the class name
        name = 'Custom' + name

        return super().__new__(cls, name, bases, dct)


# MetaClass acts as a template for the custom metaclass
class Demo(metaclass=MyMetaClass):
    pass


# Instantiate the class
obj = Demo()

# Print the class name and version attribute
print("Class Name:", type(obj).__name__)
print("Version:", obj.version)