def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    spaces = (rows * 2 - 2)//2
    points = 0
    xmas_tree = ""
    for i in range(rows):
        line = " "*spaces+"*"+"*"*points+" "*spaces
        xmas_tree += line+"\n"
        spaces -= 1
        points += 2
    return xmas_tree.rstrip()