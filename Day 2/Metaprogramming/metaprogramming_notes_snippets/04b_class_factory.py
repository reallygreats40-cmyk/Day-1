def make_model(name, fields):
    """Build a simple record class from a list of field names."""

    def __init__(self, **kwargs):
        for field in fields:
            setattr(self, field, kwargs.get(field))

    def __repr__(self):
        values = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{name}({values})"

    return type(name, (), {"__init__": __init__, "__repr__": __repr__})

# The field names could come from a database table or a JSON schema
Drug = make_model("Drug", ["name", "dose_mg"])
Ward = make_model("Ward", ["code", "beds"])

print(Drug(name="Paracetamol", dose_mg=500))
# Drug(name='Paracetamol', dose_mg=500)
print(Ward(code="B", beds=12))
# Ward(code='B', beds=12)
