# string formatting
from tkinter.font import names

a = "Hello {}"

print(a.format("Arpit"))  # Using format method

b = "Hello {name}"
print(b.format(name="Arpit"))  # Using named placeholders

c = "Hello {0} {1}"
print(c.format("Arpit", "Pardesi"))  # Using positional placeholders

d = "Hello {name} {surname}"
print(d.format(name="Arpit", surname="Pardesi"))  # Using named placeholders with

name = "Arpit"
surname = "Pardesi"
print(f"Hello {name} {surname}")  # Using f-string for formatting