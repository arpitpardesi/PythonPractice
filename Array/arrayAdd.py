import array

a = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers

a.append(6)  # Adding an element to the end of the array
print(a)

a.insert(0, 0)  # Inserting an element at the beginning of the arra
print(a)

b = array.array('i', [7, 8, 9])  # Another array of integers

a.extend(b)  # Extending the array with another array
print(a)