a={1,2,3,4,5}
print(a)

a.add(6)
a.add(7)
print(a)

a.update([8,9,10])
print(a)

b = {11,12,13,14,15}
a.update(b)
print(a)

c = {16,17,18,19,20}

d = a.union(c)
print(d)

e = {i**2 for i in d if i % 2 == 0}
print(e)

