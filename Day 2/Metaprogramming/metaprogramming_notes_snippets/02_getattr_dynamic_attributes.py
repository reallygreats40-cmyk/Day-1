"""
Dynamic Attributes: intercepting attribute access with __getattr__
=====================================================================

WHAT THIS SHOWS
----------------
'__getattr__' is a fallback hook. Python only calls it when NORMAL
attribute lookup has already failed, that is, the name was not found on
the instance, on its class, or anywhere in the class's inheritance
chain. This is different from '__getattribute__', which runs on every
single attribute access, found or not; '__getattr__' only gets a chance
to "rescue" a lookup that would otherwise raise AttributeError.

Here, Settings stores a plain dict on self.values. Because "debug" and
"host" are never declared as real attributes anywhere, EVERY attribute
access on a Settings instance falls through to __getattr__, which looks
the name up in the dict instead.

WHY THIS MATTERS
----------------
It lets an object built around a flexible, schema-less data source (a
dict, a JSON blob, a row from a database) still be used with clean,
ordinary attribute syntax (settings.debug) instead of always writing
settings.values["debug"]. It also means you do not have to pre-declare
every possible key as a class attribute up front, which matters when the
set of keys is not known in advance, or changes between deployments.

WHERE THIS SHOWS UP IN REAL CODE
---------------------------------
- Configuration wrappers around environment variables or a config file.
- Proxy or adapter objects forwarding to something they wrap.
- Attributes that are computed lazily, the first time they are accessed.
"""


class Settings:
    def __init__(self, values):
        # The one REAL attribute on this instance: a dict holding every
        # configured value, e.g. {"debug": True}. Because this line runs
        # in __init__, "values" itself is found by NORMAL lookup, so
        # __getattr__ is never invoked for it, avoiding infinite
        # recursion.
        self.values = values

    def __getattr__(self, name):
        # This only runs when `name` was NOT found the normal way, e.g.
        # settings.debug, since "debug" is not a real attribute of self.
        # `name` arrives here as the missing attribute's name, as text,
        # e.g. "debug", so self.values[name] is just an ordinary
        # dictionary lookup: self.values["debug"].
        try:
            # Redirect the failed attribute lookup into a dict lookup.
            return self.values[name]
        except KeyError:
            # Convert a missing dict key into the exception Python (and
            # anything calling hasattr() or getattr() with a default)
            # expects for a missing attribute: AttributeError, not
            # KeyError.
            raise AttributeError(name)


if __name__ == "__main__":
    settings = Settings({"debug": True})

    print(settings.debug)  # Outputs: True

    try:
        print(settings.host)  # AttributeError!
    except AttributeError as e:
        print("AttributeError raised correctly:", e)

    # hasattr() works naturally here too, since it is implemented in
    # terms of catching AttributeError from a getattr() call.
    print("has debug:", hasattr(settings, "debug"))  # True
    print("has host:", hasattr(settings, "host"))    # False
