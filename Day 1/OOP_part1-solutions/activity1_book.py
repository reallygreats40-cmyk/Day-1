"""
Activity 1 solution -- Create your first class (Book)

Task recap:
    Create a Book class with title and pages attributes, a method
    add_pages(number) that increases the page count, and two Book
    objects with different starting values. Add pages to only one
    book and demonstrate that the other is unchanged.
"""


class Book:
    """Represent a book with a title and a page count."""

    def __init__(self, title, pages):
        """Initialise the book's title and page count."""
        self.title = title
        self.pages = pages

    def add_pages(self, number):
        """Increase the page count by the given number."""
        self.pages += number


if __name__ == "__main__":
    book1 = Book("Python Basics", 250)
    book2 = Book("Advanced Algorithms", 400)

    print(book1.title, book1.pages)
    print(book2.title, book2.pages)

    # Only book1 is changed here.
    book1.add_pages(50)

    print("\nAfter adding 50 pages to book1 only:")
    print(book1.title, book1.pages)   # 300 -- changed
    print(book2.title, book2.pages)   # 400 -- unchanged, proving objects are independent
