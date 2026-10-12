# TDD - Test Driven Development

from calculator import addition

def test_addition():
    assert addition(1,2) == 3


def test_add_morethan2():
    assert addition(1,2,3) == 6



