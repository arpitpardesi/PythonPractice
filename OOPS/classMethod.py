class Employee:
    empCount = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1

    def showcount(self):
        print(self.empCount)

    counter = classmethod(showcount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)


e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Alice", 30)

e1.showcount()
Employee.counter()

setattr()