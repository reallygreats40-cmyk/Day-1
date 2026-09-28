"""
Activity 3 solution -- Manipulate an object (Student)

Task recap:
    Create a Student class with name, course and score. Add methods
    to update the score, return whether the student has passed
    (score >= 50), and return a short summary. Create at least two
    students and demonstrate that their state is independent.
"""


class Student:
    """Represent a student and their course performance."""

    def __init__(self, name, course, score):
        """Initialise the student's name, course and current score."""
        self.name = name
        self.course = course
        self.score = score

    def update_score(self, new_score):
        """Replace the student's score with a new value."""
        self.score = new_score

    def has_passed(self):
        """Return True if the score is 50 or above."""
        return self.score >= 50

    def summary(self):
        """Return a short summary of the student."""
        return f"{self.name} is studying {self.course} with a score of {self.score}."


if __name__ == "__main__":
    student1 = Student("Amina", "Computer Science", 72)
    student2 = Student("David", "Mathematics", 45)

    print(student1.summary())
    print(student2.summary())

    # Only student1's score changes here.
    student1.update_score(90)

    print("\nAfter updating student1's score only:")
    print(student1.has_passed(), student1.score)   # True, 90
    print(student2.has_passed(), student2.score)   # False, 45 -- unchanged
