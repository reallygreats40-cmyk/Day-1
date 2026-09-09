from calculator import add, is_prime, sum_of_primes


def test_add():
    assert add(2, 4, 5) == 11


def test_prime_low_number():
    assert is_prime(1) == False


def test_prime_number():
    assert is_prime(29)


def test_non_prime():
    assert is_prime(15) == False


def test_sum_of_primes_empty_list():
    assert sum_of_primes([]) == 0


def test_sum_of_primes_mixed_list():
    assert sum_of_primes([11, 15, 17, 18, 20, 100]) == 28
