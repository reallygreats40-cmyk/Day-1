class Account:
    pass

acc = Account()

# Every value has a type, including classes themselves
print(type(acc))       # <class '__main__.Account'>
print(type(Account))   # <class 'type'>
print(type(int))       # <class 'type'>

# Classes are ordinary values: store them, pass them around
kinds = [int, str, Account]
print([k.__name__ for k in kinds])   # ['int', 'str', 'Account']
