import yaml

# Create a Python dictionary
data = {"name": "Emily", "age": 35, "city": "Seattle"}

# Serialize the dictionary and write it to a YAML file
with open("data.yaml", "w") as f:
   yaml.dump(data, f, default_flow_style=False)
   print("Succes")

# Read the YAML file and deserialize it into aPython dictionary
with open("data.yaml", "r") as f:
   loaded_data = yaml.load(f, Loader=yaml.FullLoader)
   print(loaded_data)

