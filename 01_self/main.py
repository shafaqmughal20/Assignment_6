class Student:
    def __init__(self, name, marks):
        self.name = name        # Initializing the name attribute
        self.marks = marks      # Initializing the marks attribute

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Shan-E-Zehra", 92)
student1.display()
