from random import random
from time import sleep
from functools import wraps

def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            value = func(*args)
            cache[args] = value
            return value
    return wrapper  


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'
    
    @property
    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        return (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                f'{self.SOLAR_MASS_UNITS}')

