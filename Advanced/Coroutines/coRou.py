def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


# Instantiate the coroutine
coroutine = print_name("Welcome to")

# Start the coroutine
coroutine.__next__()

# Send values to the coroutine
coroutine.send("Tutorialspoint")
coroutine.send("Welcome to Tutorialspoint")

# Instantiate and start the coroutine
coroutine = print_name("Come")
coroutine.__next__()

# Send values to the coroutine
coroutine.send("Come back Thank You")
coroutine.send("Thank you")
