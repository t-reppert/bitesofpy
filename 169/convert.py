def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) == float or type(value) == int:
        if fmt.lower() == "cm" or fmt.lower() == "in":
            if fmt.lower() =="cm":
                # value is in inches
                return round(float(value * 2.54),4)
            else:
                # value is in cm
                return round(float(value / 2.54),4)
        else:
            raise ValueError
    else:
        raise TypeError

