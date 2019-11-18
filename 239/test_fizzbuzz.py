from fizzbuzz import fizzbuzz
import pytest
# write one or more test functions below, they need to start with test_
@pytest.mark.parametrize("num, expected", [
    (15, 'Fizz Buzz'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (25, 'Buzz'),
    (21, 'Fizz'),
    (30, 'Fizz Buzz'),
])
def test_fizzbuzz(num, expected):
    actual = fizzbuzz(num)
    assert actual == expected