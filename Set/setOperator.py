a = {1,2,3,4,5,6,7,8,9,10}
b = {11,12,13,14,15,16,17,18,19,20}

c = a | b
# c = a.union(b)
print(c)

a = {1,4,7,3,7,8,3,6}
b = {2,3,4,5,6,7,8,9,10}

d = a & b
# d = a.intersection(b)
print(d)

e = a - b
# e = a.difference(b)
print(e)

f = b ^ a
# f = a.symmetric_difference(b)
# f = a.symmetric_difference_update(b)
print(f)

g = a <= b
# g = a.issubset(b)
print(g)