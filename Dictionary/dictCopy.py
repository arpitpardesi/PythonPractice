a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

sC = a.copy()
sC.update({'f':6, 'g':7, 'h':8, 'i':9, 'j':10})
sC['s'] = 11

print(a)
print(sC)

b = dict(a)
b.update({'f':6, 'g':7, 'h':8, 'i':9, 'j':10})
print(b)
