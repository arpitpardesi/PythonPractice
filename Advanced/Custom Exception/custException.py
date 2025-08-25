# Define a custom exception
class CustomError(Exception):
   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

# Function that raises the custom exception
def check_value(value):
   if value < 0:
      raise CustomError("Value cannot be negative!")
   else:
      return f"Value is {value}"

# Using the function with exception handling
try:
   result = check_value(-5)
   print(result)
except CustomError as e:
   print(f"Caught an exception: {e.message}")