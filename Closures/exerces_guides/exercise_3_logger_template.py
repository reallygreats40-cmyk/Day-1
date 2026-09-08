"""
Exercise 3: Simple Event Logger (Tracking State)
Objective: Build a stateful logger make_logger() that preserves an execution history list in memory without using global variables.
"""

def make_logger():
    # Enclosing scope variable to store event history
    history = []
    
    def log(message):
        # TODO: Append the message to history and return the full list
        pass
    return log

# --- Verification ---
if __name__ == "__main__":
    logger = make_logger()
    
    print(logger("User logged in"))  # Expected: ['User logged in']
    print(logger("Query executed"))  # Expected: ['User logged in', 'Query executed']
