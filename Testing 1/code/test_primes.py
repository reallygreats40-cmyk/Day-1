from primes import *

def test_prime_low_number():
    assert is_prime(1) == False


def test_prime_number():
    assert is_prime(29)