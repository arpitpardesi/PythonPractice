a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = '0123456789'

print(list(a)[::-1])
print(list(b))
print(list(c))

import array as ar

# initializing a string
s1="WORD"
print ("original string:", s1)

# converting it to an array
sar=ar.array('u', s1)

# inserting an element
sar.insert(3,"L")

# getting back the modified string
s1=sar.tounicode()
print ("Modified string:", s1)