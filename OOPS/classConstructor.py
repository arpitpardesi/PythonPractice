class Student:
    # def __init__(self):
    #     self.name = "Arpit Pardesi"

    def __init__(self, name = "Arpit Pardesi"):
        self.name = name

    def show(self):
        print(f"Student Name: {self.name}")

# Creating an instance of Student
q = Student()
q.show()
s = Student("John Doe")
s.show()