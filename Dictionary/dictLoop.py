a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for i in a:
    print(i, a[i])

for i, j in a.items():
    print(f"{i} : {j}")

for i in a.keys():
    print(i)

for i in a.values():
    print(i)
