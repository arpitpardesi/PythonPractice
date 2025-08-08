class Demo:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Demo class instance with name: {self.name}")

d = Demo('Arpit Pardesi')
d.display()

d2 = Demo('Another Instance')
d2.age = 30  # Adding a new attribute dynamically
print(f"Dynamic attribute 'age' added: {d2.age}")
d2.name = 'Updated Name'  # Updating an existing attribute
print(f"Updated name: {d2.name}")
d2.display()
del d2.age  # Deleting the dynamically added attribute


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3