"""
Exercise 2: Lambda Functions - Solution

Objective: Practice writing small lambda functions and using them as sort keys and predicates.

Explanation: get_score picks out the second element of each tuple, so sorted() can rank students by score. reverse=True puts the highest score first. is_pass is a one-line predicate: it simply returns whether score is at least 70.
"""

students = [("Amy", 82), ("Bo", 67), ("Cy", 91), ("Dee", 74)]

get_score = lambda s: s[1]
ranked = sorted(students, key=get_score, reverse=True)
is_pass = lambda score: score >= 70


if __name__ == "__main__":
    print(ranked)
    # [('Cy', 91), ('Amy', 82), ('Dee', 74), ('Bo', 67)]

    print(is_pass(74))     # True
    print(is_pass(67))     # False
