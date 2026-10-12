"""Exercise 6: Metaclass Interface Verifier (solution)."""


class InterfaceVerifier(type):
    def __new__(mcls, name, bases, namespace):
        # Runs when each class statement is executed, before the class exists.
        # A class with no parents (BaseComponent) is the base: skip the checks.
        if bases:
            doc = namespace.get("__doc__")
            if not doc or not doc.strip():
                raise TypeError(
                    f"Class '{name}' must define a non-empty docstring.")
            if not callable(namespace.get("validate")):
                raise TypeError(
                    f"Class '{name}' must implement a 'validate(self)' method.")
        return super().__new__(mcls, name, bases, namespace)


class BaseComponent(metaclass=InterfaceVerifier):
    pass


# Extension: the same rules with __init_subclass__, no metaclass needed
class SimpleBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not (cls.__doc__ or "").strip():
            raise TypeError(f"Class '{cls.__name__}' must define a non-empty docstring.")
        if not callable(cls.__dict__.get("validate")):
            raise TypeError(f"Class '{cls.__name__}' must implement a 'validate(self)' method.")


if __name__ == "__main__":
    class DatabaseComponent(BaseComponent):
        """Stores records in the database."""
        def validate(self):
            return True

    DatabaseComponent()
    print("DatabaseComponent created successfully.")

    try:
        class BrokenDoc(BaseComponent):
            def validate(self):
                return True
    except TypeError as err:
        print("Docstring check failed correctly:", err)

    try:
        class BrokenMethod(BaseComponent):
            """Has a docstring but no validate()."""
    except TypeError as err:
        print("Method check failed correctly:", err)

    try:
        class Base(BaseComponent):    # the name "Base" gives no exemption
            pass
    except TypeError as err:
        print("No loophole:", err)

    try:
        class AlsoBroken(SimpleBase):
            """Docstring present, validate() missing."""
    except TypeError as err:
        print("Extension check:", err)
