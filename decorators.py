def decorator(func):

    def wrapper():
        print('Started')
        func()
        print("ended")
    return wrapper

#@decorator    
def hello():
    print("Some process")

hello1 = decorator(hello)
hello1()