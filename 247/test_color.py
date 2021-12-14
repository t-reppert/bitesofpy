from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    with patch('color.sample') as color_sample:
        color_sample.return_value = [101, 236, 5]
        value = next(color.gen_hex_color())
        return value


def test_gen_hex_color(gen):
    assert gen == '#65EC05'
