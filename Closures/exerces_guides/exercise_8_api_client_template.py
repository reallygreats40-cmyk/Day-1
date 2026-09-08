"""
Exercise 8: Secure API Token Wrapper (Enclosing Private Properties)
Objective: Create a client closure create_api_client(auth_token) that encloses an authentication token, allowing requests to be sent securely without exposing the raw token attribute.
"""

def create_api_client(auth_token):
    def client(endpoint):
        # TODO: Return mock response dictionary using 'auth_token'
        pass
    return client

# --- Verification ---
if __name__ == "__main__":
    api = create_api_client("secret_token")
    
    print(api("/data"))  # Runs request securely
    
    try:
        print(api.auth_token)
    except AttributeError:
        print("Inaccessible: token is safe inside closure!")
