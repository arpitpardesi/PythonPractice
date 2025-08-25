from string import Template

a = Template("My name is $name and I am $age years old.")

b = a.substitute(name="Arpit", age=27)
print(b)

dic = {'name': 'Arpit', 'age': 27}
c = a.substitute(dic)
print(c)

b = a.safe_substitute(name="Arpit")
print(b)
