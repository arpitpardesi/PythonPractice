a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    res = a/b
    print("Result:", res)
except Exception as e:
    print("An error occurred:", e)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.", e)
else:
    print("Division successful, no errors occurred.")
finally:
    print("Execution completed.")