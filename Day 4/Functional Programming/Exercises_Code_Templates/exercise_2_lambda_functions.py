"""
Exercise 2: Lambda Functions

Objective: Practice writing small lambda functions and using them as sort keys and predicates.
Instructions: Replace each None with a lambda that satisfies the comment above it.
"""

students = [("Amy", 82), ("Bo", 67), ("Cy", 91), ("Dee", 74)]

# TODO: a lambda that extracts the score (2nd element) of a student tuple
get_score = None

# TODO: sort students by score, highest first, using get_score as the key
ranked = None

# TODO: a lambda that returns True if a score is a "pass" (>= 70)
is_pass = None


if __name__ == "__main__":
    print(ranked)
    # Expected: [('Cy', 91), ('Amy', 82), ('Dee', 74), ('Bo', 67)]

    print(is_pass(74))     # Expected: True
    print(is_pass(67))     # Expected: False
