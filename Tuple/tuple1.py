a = (1,2,3,4,5)

print(a[0])
print(a[1:3])

b = a[1:4]
print(b)

c = a + b
print(c)

del c

#updating tuple is not allowed

c = (6,7,8,9,10)
a = a + c
print(a)

list_A = list(a)
list_d = [i ** 2 for i in list_A if i % 2 == 0]
print(list_d)

d = tuple(list_d)
print(d)

q,w,e,r,t = d
print(q, w, e, r, t)

q,w,e,r,*t = a
print(q, w, e, r, t)

q,w,*e,r,t = a
print(q, w, e, r, t)

z = sum((a,d),())
print(z)

