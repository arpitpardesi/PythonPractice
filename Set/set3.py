a = {1,2,3,4,5,6,7,8,9,10}
print(a)

a.remove(10)
print(a)

a.discard(10)
print(a)
a.discard(9)
print(a)

print(a.pop())
print(a)

b= a
print(b)

b.clear()
print(b)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.intersection_update(s2)
print ("s1 after running intersection_update: ", s1)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 s2 before running ^: ", s1, s2)
s3 = s1^ s2
print ("s1 after running ^: ", s3)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print (s3)
print (s1)