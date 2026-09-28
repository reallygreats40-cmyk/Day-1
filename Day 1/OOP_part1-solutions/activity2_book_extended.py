"""
Activity 2 solution -- Add behaviour (Book)

Task recap:
    Extend the Book class with a describe() method that returns a
    sentence containing the title and page count, and a
    rename(new_title) method that changes the title. Challenge: add
    a method that returns True if the book has more than 300 pages.
"""


class Book:
    """Represent a book with descriptive behaviour."""

    def __init__(self, title, pages):
        """Initialise the book's title and page count."""
        self.title = title
        self.pages = pages

    def describe(self):
        """Return a sentence describing the book."""
        return f"{self.title} has {self.pages} pages."

    def rename(self, new_title):
        """Change the book's title."""
        self.title = new_title

    def is_long(self):
        """Return True if the book has more than 300 pages (the challenge)."""
        return self.pages > 300


if __name__ == "__main__":
    book = Book("Python Basics", 250)
    print(book.describe())

    book.rename("Python Basics: Second Edition")
    print(book.describe())          # title has changed, pages has not

    print("Is it long?", book.is_long())   # False, since 250 pages

    long_book = Book("The Complete Reference", 950)
    print("Is it long?", long_book.is_long())   # True
