class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor for multiplication

    def __call__(self, number):
        """Multiply the input number by the factor"""
        return number * self.factor

# Example usage
multiplier = Multiplier(5)

# Test if the object is callable
print(callable(multiplier))  # Output: True

# Use the object like a function to multiply a number
result = multiplier(10)  # Equivalent to calling multiplier.__call__(10)
print("Result of multiplication:", result)
