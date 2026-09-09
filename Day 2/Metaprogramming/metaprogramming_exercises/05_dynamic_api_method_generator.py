"""
Exercise 5: Dynamic API Method Generator

Objective:
    Attach dynamic helper methods to classes programmatically based on a
    configuration list of strings.

Instructions:
    Write a function generate_api_client(endpoints) that dynamically binds
    helper methods named get_<endpoint>, each executing mock_get(endpoint)
    internally.

Expected Shell Output:
    Users API: GET request succeeded for https://api.system.internal/users
    Orders API: GET request succeeded for https://api.system.internal/orders
"""

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def mock_get(self, endpoint):
        return f"GET request succeeded for {self.base_url}/{endpoint}"


def generate_api_client(endpoints):
    # TODO: Construct and populate class namespace with helper methods
    pass
