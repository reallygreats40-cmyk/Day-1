"""Exercise 5: Dynamic API Method Generator (starter).

Complete generate_api_client(endpoints) so that it returns a subclass of
ApiClient with one method per endpoint, named get_<endpoint>
(e.g. get_users, get_orders). Each method returns self.mock_get(endpoint).

Hint: write a helper make_method(endpoint) that creates and returns one
method. Defining the methods directly inside a loop would make every
method use the LAST endpoint in the list (late binding).
"""


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def mock_get(self, endpoint):
        return f"GET request succeeded for {self.base_url}/{endpoint}"


def make_method(endpoint):
    """Return a method that calls mock_get for one fixed endpoint."""
    # TODO: define and return the method
    pass


def generate_api_client(endpoints):
    """Return a subclass of ApiClient with one get_<endpoint> method each."""
    # TODO: build a namespace dict of methods, then use
    #       type("DynamicApiClient", (ApiClient,), namespace)
    pass


if __name__ == "__main__":
    Client = generate_api_client(["users", "orders"])
    client = Client("https://api.system.internal")
    print("Users API:", client.get_users())
    print("Orders API:", client.get_orders())
    print("Generated methods:",
          sorted(n for n in vars(Client) if n.startswith("get_")))
