from os import write

lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]

with open("file1.txt", "w") as file1:
    file1.writelines(lines)
    file1.close()

with open("file1.txt", "a") as file1:
    file1.write("This is an appended line.\n")
    file1.close()

with open("file1.txt", "r") as file1:
    # file1.write("This is the first file.\n")
    # file1.write("It contains some text.\n")

    content = file1.read()
    print(content)

with open("fileB1.txt", "wb") as file1:
    file1.write(b"This is the first file in binary mode.\n")
    file1.write(b"It contains some text in binary format.\n")
    file1.close()