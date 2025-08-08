string = input("Enter a string to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))

for i in string:
    if i.isalpha():
        if i.islower():
            print(chr((ord(i) - 97 + shift) + 97), end="")
        else:
            print(chr((ord(i) - 65 + shift) + 65), end="")
    else:
        print(i, end="")
print()

ziddle-Outz
