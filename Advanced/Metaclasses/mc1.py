class Demo:
    pass


obj = Demo()

print(obj)

# Creating a class dynamically using type()
DemoClass = type('DemoClass', (), {})
obj = DemoClass()
print(obj)