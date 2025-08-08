a, b = 4, 0

try:
    print(a + b)
    print("This is the outer try block")
    try:
        print(a / b)
        print("This is a nested try block")
    except ZeroDivisionError:
        print("Inner ZeroDivisionError caught")
except ZeroDivisionError:
    print("Outer ZeroDivisionError caught")
finally:
    print("This is the finally block, executed regardless of exceptions")
print("End of the program")

