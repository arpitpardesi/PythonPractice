def hello(name = "arpit"):
    print(f"Hello {name}")
    return;

hello(name="abc")
# print(hello())


# This function uses keyword-only parameter syntax
# Note: The `*` indicates that all parameters after it must be specified as keyword arguments
def hello(*, name = "arpit"):
    print(f"Hello {name}")
    return;

# This function uses positional-only parameter syntax
# Note: The `/` indicates that all parameters before it must be specified as positional arguments
def hello(name = "arpit", /):
    print(f"Hello {name}")
    return;

# This function accepts both positional and keyword arguments
# Note: The `*args` collects all positional arguments, and `**kwargs` collects all keyword arguments
def arbFunc(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    return;

arbFunc(1, 2, 3, name="arpit", age=25)
arbFunc(1,2,3,'a','B', name="arpit", age=25, city="Delhi")

def arbK(**kwargs):
    for i, j in kwargs.items():
        print(f"{i} = {j}")
    return;

arbK(name="arpit", age=25, city="Delhi")