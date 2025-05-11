# Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

# Department class with aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name  # Department name
        self.employee = employee  # Aggregation: Department has a reference to Employee

    def display_department_info(self):
        print(f"Department: {self.department_name}")
        self.employee.display_info()  # Access Employee's information

# Example usage
employee1 = Employee("Alice", "Manager")  # Employee object exists independently
department1 = Department("HR", employee1)  # Department stores reference to Employee
department1.display_department_info()
