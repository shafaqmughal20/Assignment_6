class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title   # Instance variable for book title
        self.author = author # Instance variable for book author
        # Increment total_books count whenever a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books in the library: {cls.total_books}")

# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

# Display the total number of books
Book.display_total_books()  # Output: Total books in the library: 2
