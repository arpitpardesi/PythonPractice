with open("file1.txt", "r") as file2:
    content = file2.read()
    print(content)
    file2.close()

print("Reading file line:")
with open("file1.txt", "r") as file2:
    content = file2.readline()
    print(content)

print("Reading all lines into a list:")
with open("file1.txt", "r") as file2:
    content = file2.readlines()
    print(content)
    for i in content:
        print(i, end="")
    file2.close()

print("\nReading file in binary mode:")
with open("fileB1.txt", "rb") as file2:
    data = file2.read()
    print(data.decode(encoding='utf-8'))  # Decode bytes to string
    file2.close()

with open("file1.txt", "r+") as file2:
    content = file2.read()
    print("Current content of file1.txt:")
    print(content)

    # Writing new content to the file
    file2.write("\nThis is new content added in r+ mode.\n")

    # Move the cursor to the beginning of the file
    file2.seek(0)

    # Read the updated content
    updated_content = file2.read()
    print("Updated content of file1.txt:")
    print(updated_content)

    file2.close()