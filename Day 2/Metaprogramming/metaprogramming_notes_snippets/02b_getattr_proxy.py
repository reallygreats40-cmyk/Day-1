class LoggingProxy:
    """Wraps any object and logs each attribute it passes on."""

    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        # Anything the proxy itself lacks is fetched from the target
        print(f"[log] accessing {name}")
        return getattr(self._target, name)

items = LoggingProxy([3, 1, 2])

items.append(5)          # [log] accessing append
items.sort()             # [log] accessing sort
print(items._target)     # [1, 2, 3, 5]
