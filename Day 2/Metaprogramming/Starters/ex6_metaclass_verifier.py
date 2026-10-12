"""Exercise 6: Metaclass Interface Verifier (starter).

Complete InterfaceVerifier.__new__ so that every subclass of BaseComponent:
  - has a non-empty docstring, otherwise raise
    TypeError("Class '<name>' must define a non-empty docstring.")
  - defines a validate() method, otherwise raise
    TypeError("Class '<name>' must implement a 'validate(self)' method.")

The checks run when each class statement is executed. BaseComponent itself
has no parents (bases is empty), so it should be skipped. Do NOT exempt
classes by name: a subclass called "Base" must still be checked.

Extension: complete SimpleBase.__init_subclass__ to apply the same two
rules without a metaclass.
"""


class InterfaceVerifier(type):
    def __new__(mcls, name, bases, namespace):
        # TODO: if bases is not empty, check the docstring and validate()
        return super().__new__(mcls, name, bases, namespace)


class BaseComponent(metaclass=InterfaceVerifier):
    pass


# Extension: the same rules with __init_subclass__, no metaclass needed
class SimpleBase:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # TODO (extension): apply the same two checks to cls


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
