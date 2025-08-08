a = {"a":1, "b":2, "c":3, "d":4, "e":5}
print(a)

print(a['a'])

print(a.get('b',))

print(a.get('f', 'Key not found'))

print(a.keys())

print(a.values())

for i, j in a.items():
    print(f"{i} : {j}")