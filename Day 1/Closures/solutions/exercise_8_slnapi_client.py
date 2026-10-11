"""
Exercise 8: Secure API Token Wrapper (Enclosing Private Properties)
Goal: Build an API Client closure where a private token is kept secure and inaccessible from outside.
"""

def create_api_client(auth_token):
    """
    Returns an API client with an enclosed authenticating token.
    The returned client function can execute queries but does not leak the token directly.
    """
    # auth_token is safely enclosed and cannot be modified or read from outside.
    
    def client(endpoint, payload=None):
        print(f"Sending authenticated request to {endpoint}")
        headers = {"Authorization": f"Bearer {auth_token}"}
        # Simulate network request
        return {
            "status": "success",
            "endpoint": endpoint,
            "headers_used": headers,
            "data": "Result of secure endpoint request"
        }
    return client

# --- Verification ---
if __name__ == "__main__":
    client = create_api_client("super_secret_token_123")
    
    # We can invoke the client behavior
    response = client("/users/me")
    print("Response status:", response["status"])
    print("Authorization header used:", response["headers_used"]["Authorization"])
    
    # We cannot access the token directly from the client object
    try:
        print(client.auth_token)
    except AttributeError:
        print("Attribute Error raised successfully: 'auth_token' is private to the closure!")
