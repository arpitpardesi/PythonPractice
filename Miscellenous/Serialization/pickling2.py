from pickle import Pickler, Unpickler

# Open a file in binary write mode
with open("dataC.txt", "wb") as f:
   # Create a dictionary
   dct = {'name': 'Ravi', 'age': 23, 'Gender': 'M', 'marks': 75}
   # Create a Pickler object and write the dictionary to the file
   Pickler(f).dump(dct)
   print ("Success!!")

with open("dataC.txt", "rb") as f:
   # Create an Unpickler object and load the dictionary from the file
   dct = Unpickler(f).load()
   # Print the dictionary
   print(dct)