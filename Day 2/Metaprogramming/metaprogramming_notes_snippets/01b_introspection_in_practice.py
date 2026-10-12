class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Invoice:
    def __init__(self, number, total):
        self.number = number
        self.total = total

def describe(obj):
    """Works for ANY object: no class names are hard-coded."""
    cls_name = type(obj).__name__
    fields = ", ".join(f"{k}={v!r}" for k, v in vars(obj).items())
    return f"{cls_name}({fields})"

print(describe(Patient("Amina", 34)))
# Patient(name='Amina', age=34)

print(describe(Invoice(101, 250.0)))
# Invoice(number=101, total=250.0)
