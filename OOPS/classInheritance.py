class A:
    def __init__(self):
        self.value = 5

    def display(self):
        print("Value in A:", self.value)

class B(A):
    def __init__(self):
        self.value = 10
    def display(self):
        print("Value in B:", self.value)
        super().display()

class C(B, A):
    def __init__(self):
        self.value = 15
    def display(self):
        print("Value in C:", self.value)
        super().display()

# Create instances of each class
a = A()
b = B()
c = C()
# Call the display method for each instance
a.display()
b.display()
c.display()

