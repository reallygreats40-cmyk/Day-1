class ApiClient:
    base_url = "https://api.example.com"

def make_endpoint(path):
    """Create one method that calls a single API endpoint."""
    def call(self, **params):
        query = "&".join(f"{k}={v}" for k, v in params.items())
        return f"GET {self.base_url}/{path}?{query}"
    call.__name__ = path
    return call

# One method per endpoint, generated from a list of names
for path in ["patients", "appointments", "invoices"]:
    setattr(ApiClient, path, make_endpoint(path))

client = ApiClient()
print(client.patients(ward="B"))
# GET https://api.example.com/patients?ward=B
print(client.invoices(month=10))
# GET https://api.example.com/invoices?month=10
