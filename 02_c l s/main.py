class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Increment the count each time an object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()  # Output: Total objects created: 3
