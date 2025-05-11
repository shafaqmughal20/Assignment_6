class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (by convention)
        self.__ssn = ssn        # Private variable (name mangling)

# Create an object of Employee
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing public variable
print("Name:", emp.name)  # ✅ Accessible

# Accessing protected variable
print("Salary:", emp._salary)  # ⚠️ Accessible, but not recommended

# Accessing private variable directly
try:
    print("SSN:", emp.__ssn)  # ❌ Raises AttributeError
except AttributeError as e:
    print("Error accessing __ssn directly:", e)

# Accessing private variable via name mangling
print("SSN (via name mangling):", emp._Employee__ssn)  # ✅ Accessible but discouraged
