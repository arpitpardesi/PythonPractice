a = ['a','b','c','d','e']

for key, value in enumerate(a):
    print(key, value)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = [i**2 for i in b if i%2 == 0]
print(c)

 