PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new_string = ""
    for i in text:
        if i.lower() in PYBITES:
            new_string += i.swapcase()
        else:
            new_string += i
    return new_string
    