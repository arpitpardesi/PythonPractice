# inner class

class Outer:
    def __init__(self, outer_value):
        self.outer_value = outer_value

    class Inner:
        def __init__(self, inner_value):
            self.inner_value = inner_value

        def display(self):
            print(f"Inner value: {self.inner_value}")

    def display(self):
        print(f"Outer value: {self.outer_value}")
        inner_instance = self.Inner("Inner Value")
        inner_instance.display()

# Example usage
outer_instance = Outer("Outer Value")
outer_instance.display()  # Display outer value and inner value
# Accessing inner class directly
inner_instance = Outer.Inner("Direct Inner Value")
inner_instance.display()  # Display inner value directly
# Note: Inner class can be accessed directly using Outer.Inner

