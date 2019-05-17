from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(type(char) != int for char in args):
            raise TypeError
        elif any( char < 0 for char in args):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper
    