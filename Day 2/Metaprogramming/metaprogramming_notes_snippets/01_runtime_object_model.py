class Account:
    pass

class SavingsAccount(Account):
    pass

acc = SavingsAccount()

# __class__: the class that created this object
print(acc.__class__)
# <class '__main__.SavingsAccount'>

# __name__: the class's own name, as text
print(SavingsAccount.__name__)
# SavingsAccount

# __bases__: the classes it directly inherits from
print(SavingsAccount.__bases__)
# (<class '__main__.Account'>,)

# __mro__: the full order Python searches for attributes
print(SavingsAccount.__mro__)
# (<class '__main__.SavingsAccount'>,
#  <class '__main__.Account'>, <class 'object'>)
