class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Example usage
logger1 = Logger()

# Explicitly delete the object to trigger the destructor
del logger1
