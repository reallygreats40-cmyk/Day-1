"""
Closures Notes Section 8: Transitioning Closures into Decorators
Demonstrating how decorators leverage the underlying closure mechanics to wrap functions.
"""

def make_transaction_logger(func):
    # 'func' is the enclosing free variable (the function being wrapped)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing transaction: {func.__name__} with parameters {args}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed execution with result: {result}")
        return result
    return wrapper

# Standard decorator syntax is syntactic sugar for wrapper = make_transaction_logger(wrapped_function)
@make_transaction_logger
def transfer_funds(source, target, amount):
    return f"Transferred ${amount} from {source} to {target}"

def main():
    # Calling the decorated function executes the wrapper closure!
    outcome = transfer_funds("Account_A", "Account_B", 250)
    print(f"Transaction Outcome: {outcome}")

if __name__ == "__main__":
    main()
