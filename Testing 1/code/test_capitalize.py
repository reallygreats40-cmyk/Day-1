from caps import capital_case
import pytest


def test_capital_case():
    assert capital_case('john') == 'John'


# run your test and note the outcome
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
