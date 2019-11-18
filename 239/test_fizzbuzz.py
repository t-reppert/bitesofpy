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
    (7, 7),
    (14, 14),
])
def test_fizzbuzz(num, expected):
    actual = fizzbuzz(num)
    if (num % 3) != 0 and (num % 5) != 0:
        assert actual == num
    else:
        assert actual == expected
