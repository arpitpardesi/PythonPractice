import json

# Create a dictionary
data = {"name": "Alice", "age": 25, "city": "San Francisco"}

# Serialize the di ctionary and write it to a file
with open("data.json", "w") as f:
   json.dump(data, f)
   print ("Success!!")

# JSON string
json_string = '{"name": "Alice", "age": 25, "city": "San Francisco"}'

# Deserialize the JSON string into a Python dictionary
loaded_data = json.loads(json_string)
print(loaded_data)