class Settings:
    def __init__(self, values):
        self.values = values      # a normal attribute

    def __getattr__(self, name):
        # Called ONLY when normal lookup fails
        print(f"  __getattr__ called for {name!r}")
        try:
            return self.values[name]
        except KeyError:
            raise AttributeError(f"No setting called {name!r}") from None

settings = Settings({"debug": True, "port": 8080})

print(settings.port)      # __getattr__ called for 'port', then 8080
print(settings.values)    # found normally: __getattr__ is NOT called

try:
    settings.host         # not in the dict
except AttributeError as err:
    print(err)            # No setting called 'host'
