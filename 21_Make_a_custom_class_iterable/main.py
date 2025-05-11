class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # The object is iterable, so return self
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop the iteration when we reach 0 or less
        self.current -= 1
        return self.current + 1  # Return the current value before decrementing

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)
