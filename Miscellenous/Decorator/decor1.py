def show(func):
    def wrapper():
        print("Helo")

        func()

    return wrapper


@show
def display():
    print("Display function called")


display()
print("......")
a = show(display)

print(a())