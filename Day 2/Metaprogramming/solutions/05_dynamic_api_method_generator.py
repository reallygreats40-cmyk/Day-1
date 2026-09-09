"""
Exercise 5: Dynamic API Method Generator - Solution

Objective:
    Attach dynamic helper methods to classes programmatically based on a
    configuration list of strings.

Explanation:
    To bind dynamic methods safely, lambdas are defined using a default-
    parameter capture trick (ep=endpoint) inside a helper function
    (make_method). This prevents late-binding bugs where every generated
    method would otherwise resolve to the last item in the list.
"""

def generate_api_client(endpoints):
    namespace = {}
    for endpoint in endpoints:
        method_name = f"get_{endpoint}"

        def make_method(ep=endpoint):
            return lambda self: self.mock_get(ep)

        namespace[method_name] = make_method()
    return type("DynamicApiClient", (ApiClient,), namespace)
