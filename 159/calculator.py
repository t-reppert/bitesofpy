def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    num1, oper, num2, *extra = calculation.split()
    num1 = int(num1)
    num2 = int(num2)
    if extra:
        raise ValueError
    if oper not in '+-*/':
        raise ValueError
    if '*' in oper:
        return num1 * num2
    elif '-' in oper:
        return num1 - num2
    elif '+' in oper:
        return num1 + num2
    elif '/' in oper:
        if num2 == 0:
            raise ValueError
        return num1 / num2
    
    
