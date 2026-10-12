class Record:
    """Remembers which fields have changed since loading."""

    def __init__(self, **fields):
        # Use object.__setattr__ so loading is not counted as a change
        object.__setattr__(self, "_changed", set())
        for key, value in fields.items():
            object.__setattr__(self, key, value)

    def __setattr__(self, name, value):
        self._changed.add(name)                 # mark as changed
        object.__setattr__(self, name, value)   # then store it

r = Record(name="Amina", ward="B", bed=4)
r.ward = "C"
r.name = "Amina K."

print(sorted(r._changed))   # ['name', 'ward']
# Only these two fields need to be saved to the database
