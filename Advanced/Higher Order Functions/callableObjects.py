class Rectangle:
    def __init__(self, l):
       self.l = l

    def __call__(self, a):
        return self.l * a

r = Rectangle(5)
print(r(10))  # Outputs: 50