import pickle
class Person:
   def __init__(self, name, age, city):
      self.name = name
      self.age = age
      self.city = city

# Create an instance of the Person class
person = Person('Alice', 30, 'New York')

# Serialize the person object
with open('person.pkl', 'wb') as file:
   pickle.dump(person, file)

# Deserialize the person object
with open('person.pkl', 'rb') as file:
   person = pickle.load(file)

print(person.name, person.age, person.city)