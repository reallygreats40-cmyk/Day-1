class PluginMeta(type):
    """Records every plugin class the moment it is defined."""
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if bases:                            # skip the base class
            mcls.registry[name.lower()] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    pass

class CsvExporter(Plugin):
    def export(self):
        return "saved as CSV"

class PdfExporter(Plugin):
    def export(self):
        return "saved as PDF"

print(list(PluginMeta.registry))       # ['csvexporter', 'pdfexporter']

choice = "pdfexporter"                 # e.g. read from user settings
print(PluginMeta.registry[choice]().export())   # saved as PDF
