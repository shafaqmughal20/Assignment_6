# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Dr. Smith", "Physics")
teacher1.display()
