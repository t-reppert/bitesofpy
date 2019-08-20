from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        tries = 1
        while tries <= MAX_RETRIES:
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(e)
                tries += 1
                if tries > 3:
                    raise MaxRetriesException
                else:
                    continue
            return

    return wrapper
