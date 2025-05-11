# Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"The {self.engine_type} engine is now running."

# Car class with composition
class Car:
    def __init__(self, brand, engine):
        self.brand = brand        # Car brand
        self.engine = engine      # Composition: Car has an Engine

    def start_car(self):
        print(f"{self.brand} car is starting.")
        print(self.engine.start())  # Access Engine's start method

# Example usage
engine = Engine("V8")        # Create an Engine object
car = Car("Ford Mustang", engine)  # Pass Engine object to Car
car.start_car()
