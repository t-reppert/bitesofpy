def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) == float or type(value) == int:
        if fmt.lower() == "cm" or fmt.lower() == "in":
            if fmt.lower() =="cm":
                return value / 0.39
            else:
                return 0.39 * value
        else:
            raise ValueError
    else:
        raise TypeError

