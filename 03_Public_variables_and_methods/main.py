class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):         # Public method
        print(f"The {self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Call public method
my_car.start()
