a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
b = {'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

d1 = {**a, **b}
print(d1)

d2 = a | b
print(d2)

d4 = a.copy()
d4 |= b
print(d4) 