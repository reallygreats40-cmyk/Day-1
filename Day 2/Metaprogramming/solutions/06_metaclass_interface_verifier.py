"""
Exercise 6: Metaclass Interface Verifier - Solution

Objective:
    Enforce structural layout rules and docstring presence at class
    compilation time.

Explanation:
    Metaclasses intercept the low-level class-object creation step. The
    namespace dict is inspected inside type.__new__ and the required rules
    are enforced. If a subclass fails verification, a TypeError is raised to
    abort compilation before import completes.
"""

class InterfaceVerifier(type):
    def __new__(mcls, name, bases, namespace):
        is_base = name in ("BaseComponent", "Base") or not bases
        if not is_base:
            doc = namespace.get("__doc__")
            if not doc or not doc.strip():
                raise TypeError(
                    f"Class '{name}' must define a non-empty docstring.")
            if "validate" not in namespace:
                raise TypeError(
                    f"Class '{name}' must implement a 'validate(self)' method.")
        return super().__new__(mcls, name, bases, namespace)
