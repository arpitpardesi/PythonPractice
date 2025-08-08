a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(a)
print(b)

c = a + b
print(c)

d = [j for i in [a,b] for j in i]
print(d)

a = [1,2,3,4,5]
b = [6,7,8,9,10]

for i in b:
    a.append(i)
print(a)

a = [1,2,3,4,5]
b = [6,7,8,9,10]

a.extend(b)
print(a)