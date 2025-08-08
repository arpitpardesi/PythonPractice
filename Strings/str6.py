# string methods
a = " Hello World "

print(a.lower())  # Convert to lowercase
print(a.upper())  # Convert to uppercase
print(a.title())  # Convert to title case
print(a.capitalize())  # Capitalize the first letter
print(a.swapcase())  # Swap case of all letters
print(a.replace("World", "Python"))  # Replace substring
print(a.split())  # Split string into a list of words
print(a.split("o"))  # Split string by a specific character
print(a.strip())  # Remove leading and trailing whitespace
print(a.lstrip())  # Remove leading whitespace
print(a.rstrip())  # Remove trailing whitespace
print(a.find("World"))  # Find the index of a substring
print(a.index("World"))  # Find the index of a substring (raises error if not found)
print(a.count("o"))  # Count occurrences of a substring
print(a.startswith("Hello"))  # Check if string starts with a substring
print(a.endswith("World"))  # Check if string ends with a substring
print(a.isalpha())  # Check if all characters are alphabetic
print(a.isdigit())  # Check if all characters are digits
print(a.isalnum())  # Check if all characters are alphanumeric
print(a.islower())  # Check if all characters are lowercase
print(a.isupper())  # Check if all characters are uppercase
print(a.isspace())  # Check if all characters are whitespace
print(a.startswith("Hello"))  # Check if string starts with a substring
print(a.endswith("World"))  # Check if string ends with a substring
print(a.isidentifier())  # Check if string is a valid identifier
print(a.isprintable())  # Check if string is printable
print(a.zfill(15))  # Pad string with zeros to a specified width
print(a.center(20))  # Center the string within a specified width
print(a.ljust(20))  # Left justify the string within a specified width
print(a.rjust(20))  # Right justify the string within a specified width
print(a.expandtabs(4))  # Expand tabs to spaces (default is 8 spaces)
print(a.partition(" "))  # Split string into three parts: before, separator, after
print(a.rpartition(" "))  # Split string into three parts: before, separator, after
print(a.splitlines())  # Split string into a list of lines
print(a.join(["Hello", "Python"]))  # Join a list of strings with the original string as a separator
print(a.removeprefix("Hello "))  # Remove prefix from the string
print(a.removesuffix(" World"))  # Remove suffix from the string
