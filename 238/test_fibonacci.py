from fibonacci import fib
import pytest
# write one or more test functions below, they need to start with test_

def _fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b, a+b
        yield b


def test_fibonacci():
    fibs = []
    for i, f in enumerate(_fibs()):
        fibs.append(f)
        if i > 20:
            break

    with pytest.raises(ValueError):
        fib(-1)
    for i in range(20):
        assert fib(i) == fibs[i]
