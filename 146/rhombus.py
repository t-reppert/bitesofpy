STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    mid = (width - 1)//2
    spaces = mid
    points = 0
    rhombus = []
    for i in range(mid):
        line = " "*spaces+"*"+"*"*points+" "*spaces
        rhombus.append(line)
        spaces -= 1
        points += 2
    rhombus.append("*"*width)
    points = width - 3
    spaces = 1
    for i in range(mid,0,-1):
        line = " "*spaces+"*"+"*"*points+" "*spaces
        rhombus.append(line)
        spaces += 1
        points -= 2
    return rhombus