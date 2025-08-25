import pickle

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Open a file in binary write mode
with open('data.pkl', 'wb') as file:
   # Serialize the data and write it to the file
   pickle.dump(data, file)
   print ("File created!!")

with open('data.pkl', 'rb') as file:
   # Deserialize the data
   data = pickle.load(file)
print(data)