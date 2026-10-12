class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age            # goes through __setattr__ too

    def __setattr__(self, name, value):
        # Runs for EVERY assignment, e.g. p.age = 35
        if name == "age" and not 0 <= value <= 130:
            raise ValueError(f"age must be 0 to 130, got {value}")
        # Writing self.age = value here would call this method
        # again, forever. object.__setattr__ does the real write.
        object.__setattr__(self, name, value)

p = Patient("Amina", 34)
p.age = 35                        # accepted
print(p.age)                      # 35

try:
    p.age = -5                    # rejected
except ValueError as err:
    print(err)                    # age must be 0 to 130, got -5
