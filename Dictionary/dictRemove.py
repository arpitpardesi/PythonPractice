a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
b = {'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

del a['e']
print(a)

del b

print(a.pop('d'))

print(a.popitem())

b = {'f':6, 'g':7, 'h':8, 'i':9, 'j':10}
print(b.clear())

