"""
Activity 4 solution -- Add __str__() (Student)

Task recap:
    Return to the Student class and add __str__() so that
    print(student) produces something useful, e.g. "Amina - Python - 78%".
    Remember: __str__() must return a string, not print one.
"""


class Student:
    """Represent a student with a readable string form."""

    def __init__(self, name, course, score):
        """Initialise the student's name, course and current score."""
        self.name = name
        self.course = course
        self.score = score

    def __str__(self):
        """Return a human-readable summary of the student."""
        return f"{self.name} \u2014 {self.course} \u2014 {self.score}%"


if __name__ == "__main__":
    student = Student("Amina", "Python", 78)
    print(student)   # Python automatically calls student.__str__() here
