import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("test_input,expected",
                         [([4, 2, 8], 428), 
                          ([1, 2], 12),
                          ([3], 3),
                          ([1,2,3,4,5,6,7,8,9,0],1234567890),
                          ])
def test_correct(test_input, expected):
    result = list_to_decimal(test_input)
    assert result == expected


def test_boolean_error():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])

def test_boolean_error2():
    with pytest.raises(TypeError):
        list_to_decimal([False, 6, 2])

def test_neg_error():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])

def test_neg_error2():
    with pytest.raises(ValueError):
        list_to_decimal([10, -3, 12])

def test_dec_error():
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 4, 1])

def test_dec_error2():
    with pytest.raises(TypeError):
        list_to_decimal([9, 2, 3.6, 4, 1])

def test_string_error():
    with pytest.raises(TypeError):
        list_to_decimal(["4", 5, 3, 1])

def test_string_error2():
    with pytest.raises(TypeError):
        list_to_decimal([8, 6, "4", 5, "Five", 1])

