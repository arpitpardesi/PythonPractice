import array

a = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers

a.remove(5)
print(a)

a.pop(3)
print(a)