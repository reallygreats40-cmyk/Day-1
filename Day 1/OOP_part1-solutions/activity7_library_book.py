"""
Activity 7 solution -- Consolidating activity: a small library system

Task recap:
    Create a LibraryBook class with attributes title, author, and
    internal _is_borrowed; borrow() and return_book() methods with
    sensible validation; __str__() showing title, author and
    availability; a method is_available(); at least two objects
    manipulated independently.

    Optional extension: a second class with the same __str__
    interface, printed alongside LibraryBook objects in one loop.
"""


class LibraryBook:
    """Represent a library book that can be borrowed and returned."""

    def __init__(self, title, author):
        """Initialise the book as available (not borrowed)."""
        self.title = title
        self.author = author
        self._is_borrowed = False   # Internal attribute by convention.

    def borrow(self):
        """Mark the book as borrowed, if it is currently available."""
        if self._is_borrowed:
            raise ValueError(f"'{self.title}' is already borrowed.")
        self._is_borrowed = True

    def return_book(self):
        """Mark the book as available again, if it was borrowed."""
        if not self._is_borrowed:
            raise ValueError(f"'{self.title}' was not borrowed, so it cannot be returned.")
        self._is_borrowed = False

    def is_available(self):
        """Return True if the book can currently be borrowed."""
        return not self._is_borrowed

    def __str__(self):
        """Return a readable description including title, author and availability."""
        status = "available" if self.is_available() else "borrowed"
        return f"{self.title} by {self.author} ({status})"


# --- Optional extension: a second, unrelated class sharing the same ---
# --- __str__ interface, so both kinds of object can be printed        ---
# --- together in one loop. This is the same polymorphism idea from    ---
# --- Activity 6, applied to __str__ instead of a custom method.       ---
class OnlineArticle:
    """Represent an online article, always available, for comparison."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable description in the same style as LibraryBook."""
        return f"{self.title} by {self.author} (always available online)"


if __name__ == "__main__":
    book_a = LibraryBook("Dune", "Frank Herbert")
    book_b = LibraryBook("Foundation", "Isaac Asimov")

    print(book_a)
    print(book_b)

    book_a.borrow()
    print("\nAfter borrowing book_a only:")
    print(book_a)   # borrowed
    print(book_b)   # still available -- independent state

    book_a.return_book()
    print("\nAfter returning book_a:")
    print(book_a)   # available again

    # Extension: prevent a book from being borrowed twice.
    book_b.borrow()
    try:
        book_b.borrow()
    except ValueError as error:
        print("\nCorrectly prevented double borrow:", error)

    # Optional extension: mix LibraryBook and OnlineArticle in one loop,
    # printing both through the same __str__ interface.
    print("\nAll resources:")
    resources = [LibraryBook("Dune", "Frank Herbert"), OnlineArticle("OOP in Python", "Real Python")]
    for resource in resources:
        print(resource)
