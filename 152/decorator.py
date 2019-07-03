from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            new_text = ""
            idx_to_swap = list(range(start, end))
            if start > len(kwargs['text']):
                return f(*args, **kwargs)
            for i, letter in enumerate(kwargs['text']):
                if i in idx_to_swap:
                    new_text += '.'
                else:
                    new_text += letter
            return f(new_text)
        return wrapper
    return deco