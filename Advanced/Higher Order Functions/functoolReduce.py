import functools
def mult(x,y):
   return x*y

# Define a number to calculate factorial
n = 4
num = functools.reduce(mult, range(1, n+1))
print (f'Factorial of {n}: ',num)