a = [1,2,3,4,5,'a','b','c']

print(a)
print(a[5:])
del a[5:]
print(a[::-1])

a[4] = 6
print(a)

a.insert(4, 5)
print(a)

a.insert(6, 8)
print(a)

del a[6]
print(a)

a.append(7)
print(a)

a.extend([11, 8, 9, 10])
print(a)

a.remove(11)
print(a)

a.pop(9) #index a[9]
print(a)

a.clear()
print(a)