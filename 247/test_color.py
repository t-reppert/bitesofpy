from unittest.mock import patch
import types
import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def sample(x, y):
    if max(x) > 256:
        raise ValueError
    if y > 3:
        raise ValueError
    return x[0], x[1], x[2]

def test_gen_hex_color(gen):
    with patch('color.sample') as color_sample:
        color_sample.return_value = sample([101, 236, 5], 3)
        value = next(gen)
        print(value)
        assert value == '#65EC05'
        g = color.gen_hex_color()  #65EC05
        assert type(g) == types.GeneratorType
        assert next(g) == '#65EC05'
        color_sample.return_value = sample([236, 101, 100], 3)
        g = color.gen_hex_color()
        assert type(g) == types.GeneratorType        
        assert next(g) == '#EC6564'
        g = color.gen_hex_color()
        assert next(g) == '#EC6564'
        assert next(g).isupper()
        assert len(next(g)) == 7
        assert "#" in next(g)
        color_sample.return_value = sample([0, 171, 242], 3)
        g = color.gen_hex_color()
        assert type(g) == types.GeneratorType        
        assert next(g) == '#00ABF2'

def  test_bad_gen_hex_color(gen):
    with patch('color.sample') as color_sample: 
        with pytest.raises(ValueError):
            color_sample.return_value = sample([101, 236, 5, 100], 4)
            value = next(gen)
        with pytest.raises(ValueError):
            color_sample.return_value = sample([299, 100, 5], 3)
            value = next(gen)
