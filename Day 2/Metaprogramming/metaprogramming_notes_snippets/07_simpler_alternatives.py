# Alternative 1: __init_subclass__ runs for every new subclass
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "run" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must define run()")

class Job(Base):
    def run(self):
        return "ok"

try:
    class BrokenJob(Base):
        pass
except TypeError as err:
    print(err)                # BrokenJob must define run()

# Alternative 2: a class decorator runs AFTER the class is built
def tag(cls):
    cls.meta_tag = True
    return cls

@tag
class Widget:
    pass

print(Widget.meta_tag)        # True
