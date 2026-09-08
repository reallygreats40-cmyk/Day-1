"""
Closures Notes Section 5: State Retention with Closures
Demonstrating how closures maintain private, persistent state between executions.
"""

def make_averager():
    # Persistent local state stored inside the enclosing scope
    numbers = []
    
    def averager(new_number):
        nonlocal numbers
        numbers.append(new_number)
        return sum(numbers) / len(numbers)
    return averager

def main():
    avg = make_averager()
    print(avg(10))  # Output: 10.0
    print(avg(20))  # Output: 15.0
    print(avg(30))  # Output: 20.0
    
    # The list is completely hidden from the caller, ensuring perfect encapsulation!
    # print(avg.numbers) -> AttributeError!

if __name__ == "__main__":
    main()
