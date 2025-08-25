import timeit

a = timeit.timeit("[i for i in range(10)]", number=10000)
print(a)