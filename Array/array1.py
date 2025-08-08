import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers
print(a)

b = arr.array('u', ['a', 'b', 'c', 'd', 'e'])  # 'u' indicates an array of unicode characters
print(b)

c = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])  # 'f' indicates an array of floats
print(c)

d = arr.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])  # 'd' indicates an array of doubles
print(d)
e = arr.array('b', [1, 2, 3, 4, 5])  # 'b' indicates an array of signed integers


for i in a:
    print(i, end=' ')

    