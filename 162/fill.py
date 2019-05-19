HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    diff = abs(column_length - len(str(value)))
    if diff > 0:
        return f'{fill_char*diff}{value}'
    else:
        return str(value)
        