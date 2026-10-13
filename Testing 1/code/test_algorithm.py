from algorithm import * 
import pytest


@pytest.mark.skip 
def test_smallest():
    values = (2, 3, 1, 4, 6)
    val = smallest(values)
    assert val == 1


def test_biggest():
    values = (2, 3, 1, 4, 6)
    val = biggest(values)
    assert val == 6
