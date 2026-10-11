"""
Exercise 3: Simple Event Logger (Tracking State)
Goal: Create a logger closure that maintains an execution history list in memory.
"""

def make_logger():
    """
    Returns a function that appends a message to an enclosed list
    and returns the entire list of messages logged so far.
    """
    history = []  # Enclosing scope list
    
    def log(message):
        # We can append directly because lists are mutable
        history.append(message)
        return list(history)  # Return a copy of the list
    return log

# --- Verification ---
if __name__ == "__main__":
    logger = make_logger()
    
    print(logger("User logged in"))        # Expected: ['User logged in']
    print(logger("Database query run"))    # Expected: ['User logged in', 'Database query run']
    print(logger("User logged out"))       # Expected: ['User logged in', 'Database query run', 'User logged out']
