# escape characters

s = "Hello\nWorld"
print(s)  # Newline character
s = "Hello\tWorld"
print(s)  # Tab character
s = "Hello\\World"
print(s)  # Backslash character
s = "Hello\'World"
print(s)  # Single quote character
s = "Hello\"World"
print(s)  # Double quote character
s = "Hello\bWorld"
print(s)  # Backspace character

#raw strings
s = r"Hello\nWorld"
print(s)  # Raw string, no escape characters processed
s = r"Hello\tWorld"
print(s)  # Raw string, no escape characters processed
s = r"Hello\\World"
print(s)  # Raw string, no escape characters processed
s = r"Hello\'World"
print(s)  # Raw string, no escape characters processed
s = r"Hello\"World"
print(s)  # Raw string, no escape characters processed
s = r"Hello\bWorld"
print(s)  # Raw string, no escape characters processed
s = r"Hello\World"
print(s)  # Raw string, no escape characters processed