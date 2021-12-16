def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    out = number // base
    rem = number % base
    if out != 0:
        return int(str(dec_to_base(out, base)) + str(rem))
    else:
        return rem