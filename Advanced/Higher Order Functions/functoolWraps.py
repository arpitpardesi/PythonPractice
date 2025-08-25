import functools

def my_decorator(f):
   @functools.wraps(f)
   def wrapper(*args, **kwargs):
      print("Calling", f.__name__)
      return f(*args, **kwargs)
   return wrapper

@my_decorator
def invite(name):
   print(f"Welcome {name}!")

invite("Arpit")