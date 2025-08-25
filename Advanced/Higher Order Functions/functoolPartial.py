import functools
def myfunction(a,b):
   return a*b

partfunction = functools.partial(myfunction,b = 10)
print(partfunction(10))