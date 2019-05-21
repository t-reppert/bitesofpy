from collections import OrderedDict

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if type(decimal_number) != int:
        raise ValueError
    elif not 0 < decimal_number < 4000:
        raise ValueError
    numerals = OrderedDict()
    numerals[1000] = 'M'
    numerals[900] = 'CM'
    numerals[500] = 'D'
    numerals[400] = 'CD'
    numerals[100] = 'C'
    numerals[90] = 'XC'
    numerals[50] = 'L'
    numerals[40] = 'XL'
    numerals[10] = 'X'
    numerals[9] = 'IX'
    numerals[5] = 'V'
    numerals[4] = 'IV'
    numerals[1] = 'I'
    roman = ''
    while decimal_number > 0:
        for i in numerals.keys():
            if decimal_number - i > 0:
                decimal_number -= i
                roman += numerals[i]
                break
            elif decimal_number - i < 0:
                continue
            else:
                decimal_number -= i
                roman += numerals[i]
                break
    return roman


    