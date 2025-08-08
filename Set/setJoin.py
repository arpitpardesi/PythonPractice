a = {1,2,3,4,5}
b = {6,7,8,9,10}

j1 = a | b
print(j1)

j2 = a.union(b)
print(j2)

j3 = {*a, *b}
print(j3)

j4 = {j for i in [a,b] for j in i}
print(j4)

j5 = set()
for i in a:
    j5.add(i)
for i in b:
    j5.add(i)
print(j5)

a.update(b)
print(a)