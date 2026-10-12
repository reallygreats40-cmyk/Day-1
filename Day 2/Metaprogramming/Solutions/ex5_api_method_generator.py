"""Exercise 5: Dynamic API Method Generator (solution)."""


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def mock_get(self, endpoint):
        return f"GET request succeeded for {self.base_url}/{endpoint}"


def make_method(endpoint):
    """Return a method that calls mock_get for one fixed endpoint.

    Each call to make_method creates a new closure, so every method
    remembers its own endpoint. Defining the method directly inside the
    loop would make every method use the LAST endpoint in the list.
    """
    def method(self):
        return self.mock_get(endpoint)
    method.__name__ = f"get_{endpoint}"
    return method


def generate_api_client(endpoints):
    """Return a subclass of ApiClient with one get_<endpoint> method each."""
    namespace = {f"get_{ep}": make_method(ep) for ep in endpoints}
    return type("DynamicApiClient", (ApiClient,), namespace)


if __name__ == "__main__":
    Client = generate_api_client(["users", "orders"])
    client = Client("https://api.system.internal")
    print("Users API:", client.get_users())
    print("Orders API:", client.get_orders())
    print("Generated methods:",
          sorted(n for n in vars(Client) if n.startswith("get_")))
