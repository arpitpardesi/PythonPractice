a = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(a)

a['name'] = 'Arpit'
a['age'] = 27
print(a)

a.update({'name': 'Arpit Pardesi', 'city': 'Mhow'})
print(a)

a['country'] = 'India'
print(a)

a.setdefault('state', 'Madhya Pradesh')
print(a)