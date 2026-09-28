"""
Activity 5 solution -- Encapsulate a temperature

Task recap:
    Create a Temperature class that stores degrees Celsius internally
    as _celsius, rejects values below absolute zero in __init__,
    provides to_fahrenheit(), and provides change_by(amount) while
    preserving the validity rule. Test both a valid and an invalid value.
"""


class Temperature:
    """Store a temperature in Celsius and expose safe operations on it."""

    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius):
        """Initialise the temperature, rejecting values below absolute zero."""
        if celsius < Temperature.ABSOLUTE_ZERO:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = celsius   # Internal attribute by convention.

    def get_celsius(self):
        """Return the current temperature in Celsius."""
        return self._celsius

    def to_fahrenheit(self):
        """Return the temperature converted to Fahrenheit."""
        return (self._celsius * 9 / 5) + 32

    def change_by(self, amount):
        """
        Change the temperature by amount (positive or negative),
        re-applying the same validity rule used in __init__.
        """
        new_value = self._celsius + amount
        if new_value < Temperature.ABSOLUTE_ZERO:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = new_value


if __name__ == "__main__":
    # A valid value: everything works as expected.
    room = Temperature(20)
    print(room.to_fahrenheit())   # 68.0
    room.change_by(5)
    print(room.get_celsius())     # 25

    # An invalid starting value: the constructor must refuse it.
    try:
        Temperature(-300)
    except ValueError as error:
        print("Rejected invalid starting value:", error)

    # An invalid change: change_by() must protect the same rule.
    try:
        room.change_by(-1000)
    except ValueError as error:
        print("Rejected invalid change:", error)
