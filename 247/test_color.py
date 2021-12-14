from unittest.mock import patch
import types
import pytest

import color


@pytest.fixture(scope="module")
def gen():
    with patch('color.sample') as color_sample:
        color_sample.return_value = [101, 236, 5]
        value = next(color.gen_hex_color())  #65EC05
        return next(color.gen_hex_color())


def test_gen_hex_color(gen):
    with patch('color.sample') as color_sample:
        color_sample.return_value = [101, 236, 5]
        g = color.gen_hex_color()  #65EC05
        assert type(g) == types.GeneratorType
        assert next(g) == '#65EC05'
        color_sample.return_value = [236, 101, 100]
        g = color.gen_hex_color()
        assert type(g) == types.GeneratorType        
        assert next(g) == '#EC6564'