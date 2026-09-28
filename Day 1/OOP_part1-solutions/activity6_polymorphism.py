"""
Activity 6 solution -- One interface, different behaviour (Bus / Train)

Task recap:
    Create two classes, Bus and Train, each with a board(passengers)
    method that returns a different message. Write one function,
    announce_vehicle(vehicle), that calls board() without checking
    the class name.

Question answered at the bottom: what common behaviour allows the
function to work with both objects?
"""


class Bus:
    """A bus that can board passengers."""

    def board(self, passengers):
        """Return a message describing passengers boarding the bus."""
        return f"{passengers} passenger(s) boarded the bus."


class Train:
    """A train that can board passengers."""

    def board(self, passengers):
        """Return a message describing passengers boarding the train."""
        return f"{passengers} passenger(s) boarded the train."


def announce_vehicle(vehicle, passengers):
    """
    Announce boarding for any vehicle object, as long as it provides
    a board(passengers) method -- this function never checks the
    vehicle's class.
    """
    print(vehicle.board(passengers))


if __name__ == "__main__":
    for vehicle in (Bus(), Train()):
        announce_vehicle(vehicle, 12)

    # Answer to the question:
    # announce_vehicle() works with both objects because each one
    # provides a method with the same name and compatible signature,
    # board(passengers). Python does not check the object's class,
    # only that the method it is asked to call actually exists on
    # that object. This is "duck typing": if it can board(), it can
    # be used here, regardless of what kind of vehicle it is.
